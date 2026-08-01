/* drawing_bundle.js — Drawing Bundle Extractor / Canonical Drawing Index
 * ADR-001（プロジェクト doc「DRAWING_BUNDLE_EXTRACTOR.md」）。Extraction Layer の共通入口。
 *
 * Purpose:
 *   Drawing Bundle Extractor transforms heterogeneous drawing packages
 *   into a Canonical Drawing Index. It never interprets geometry. It only identifies pages.
 *
 * 責務分解:  Drawing Package(PDF) → [ Extraction → Classification → Index ] → Canonical Drawing Index
 *   Extraction     : 入力からページ列とテキストを取り出す（実装差=pdf.js はここに閉じる）
 *   Classification : Title Block(第一証拠) → Body keyword(fallback) → unknown（推測で埋めない）
 *   Index          : 契約(CanonicalDrawingIndex)を組み立てる
 *
 * 触らない（Geometry 非依存）: DOM / KKai(drawings.json) / Roof/Wall/Vertex/Polygon/Segment / 数量。
 * 依存方向: UI → DrawingBundle → Canonical Drawing Index（このモジュールは UI を知らない）。
 *
 * 契約（LOCK・§5）:
 *   CanonicalDrawingIndex { file:string, pages:PageEntry[] }
 *   PageEntry { id, page, type, confidence, evidence, source }
 *     type       : "site"|"plan"|"elevation"|"roof_plan"|"section"|"sash"|
 *                  "foundation_plan"|"area_calc"|"detail"| null
 *     confidence : "high"|"medium"|"confirmed"|"none"
 *     source     : "title_block"|"body_keyword"|"manual"|"none"
 *   ※ label は契約に持たない（消費側が type から導出）。表示補助として label(type) を提供。
 *   ※ Projection ≠ Evidence: confidence/source は Canonical 側の属性。用途(KKai/Leak/Roof)で変えない。
 *
 * Candidate（実データで育てる・未 LOCK）: Title Block 候補ラベル / confidence 段階 / id 生成 / Classification 実装。
 */
(function(global){
  "use strict";

  // 種別語彙（Candidate: 語彙拡張は実データで）。kkai=KKai 必要図面か（消費側 Projection の手掛かり）。
  var TYPES = [
    {type:"site",            label:"配置図",   kkai:true,  tokens:["配置図"]},
    {type:"elevation",       label:"立面図",   kkai:true,  tokens:["立面図"]},
    {type:"roof_plan",       label:"屋根伏図", kkai:true,  tokens:["屋根伏図","屋根伏","伏図"]},
    {type:"section",         label:"矩計図",   kkai:true,  tokens:["矩計図","矩計","かなばかり","断面図"]},
    {type:"sash",            label:"建具表",   kkai:true,  tokens:["建具表","建具リスト","サッシ表","窓表"]},
    {type:"foundation_plan", label:"基礎伏図", kkai:true,  tokens:["基礎伏図","基礎伏"]},
    {type:"plan",            label:"平面図",   kkai:true,  tokens:["平面図"]},        // 最後（◯階平面図も拾う）
    {type:"area_calc",       label:"求積図",   kkai:false, tokens:["求積図","面積表","求積"]},
    {type:"detail",          label:"詳細図",   kkai:false, tokens:["詳細図","納まり図"]}
  ];

  // Title Block ラベル候補（Candidate: 実データで増やす／推測で増やさない）
  var TITLE_LABELS = ["図面名称","図面名","図名","TITLE","DRAWING TITLE"];
  var TITLE_WINDOW = 60; // ラベル近傍窓（Candidate）。本文に引っ張られないための窓。

  function labelOf(type){
    if(!type) return "未判定";
    for(var i=0;i<TYPES.length;i++){ if(TYPES[i].type===type) return TYPES[i].label; }
    return type;
  }
  function isKkaiType(type){
    for(var i=0;i<TYPES.length;i++){ if(TYPES[i].type===type) return !!TYPES[i].kkai; }
    return false;
  }
  function scanTokens(hay){
    for(var i=0;i<TYPES.length;i++){
      var g=TYPES[i];
      for(var j=0;j<g.tokens.length;j++){
        if(hay.indexOf(g.tokens[j])>=0) return {type:g.type, evidence:g.tokens[j]};
      }
    }
    return null;
  }

  // Classification: 1ページのテキスト → {type,confidence,evidence,source}
  //   Title Block(第一証拠/high) → Body keyword(fallback/medium) → unknown(none)
  //   ※ 部屋名・寸法(1階/2階等)は種別語に使わない（求積図が平面図に化けるのを防ぐ）。
  function classifyText(raw){
    var text=(raw||"").replace(/[\n\r]/g," ");
    // Title Block: 候補ラベルのどれかを見つけ、その近傍窓だけを見る（第一証拠）
    for(var i=0;i<TITLE_LABELS.length;i++){
      var idx=text.indexOf(TITLE_LABELS[i]);
      if(idx>=0){
        var hit=scanTokens(text.slice(idx, idx+TITLE_WINDOW));
        if(hit) return {type:hit.type, confidence:"high", evidence:hit.evidence, source:"title_block"};
      }
    }
    // Body keyword: 本文中の種別語（fallback）
    var b=scanTokens(text);
    if(b) return {type:b.type, confidence:"medium", evidence:b.evidence, source:"body_keyword"};
    // unknown: 推測で埋めない（Evidence First）
    return {type:null, confidence:"none", evidence:null, source:"none"};
  }

  // Extraction: PDF → ページ列(テキスト)。実装差(pdf.js)はここに閉じる。
  async function extractPages(file){
    if(!global.pdfjsLib) throw new Error("pdf.js(pdfjsLib)未ロード");
    var buf=await file.arrayBuffer();
    var doc=await global.pdfjsLib.getDocument({data:new Uint8Array(buf)}).promise;
    var out=[];
    for(var i=1;i<=doc.numPages;i++){
      var pg=await doc.getPage(i);
      var tc=await pg.getTextContent();
      out.push({page:i, text:tc.items.map(function(it){return it.str;}).join("")});
    }
    return out;
  }

  // id 生成（Candidate）: 現状はページ番号ベース。「順序不変」はまだ Evidence が無い。
  function makeId(file, page){ return "p"+page; }

  // 公開: Drawing Package(PDF) → Canonical Drawing Index（一度だけ生成）
  async function extract(file){
    var pages=await extractPages(file);
    var entries=pages.map(function(pg){
      var c=classifyText(pg.text);
      return { id:makeId(file,pg.page), page:pg.page, type:c.type,
               confidence:c.confidence, evidence:c.evidence, source:c.source };
    });
    return { file:(file&&file.name)||"", pages:entries };
  }

  var api = {
    TYPES: TYPES,
    TITLE_LABELS: TITLE_LABELS,
    label: labelOf,
    isKkaiType: isKkaiType,
    classifyText: classifyText,   // 純粋分類（テスト用・Node でも動く）
    extract: extract              // Extraction + Classification + Index
  };
  global.DrawingBundle = api;
  if(typeof module!=="undefined" && module.exports){ module.exports = api; } // Node(テスト)用
})(typeof window!=="undefined" ? window : (typeof globalThis!=="undefined"?globalThis:this));
