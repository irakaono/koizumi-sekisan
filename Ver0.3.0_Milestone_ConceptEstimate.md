<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Phase3（calcWall）引き継ぎ書</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;} body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:920px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;} .hero h1{margin:6px 0 0;font-size:22px;font-weight:800;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:32px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h3{font-size:14.5px;font-weight:800;color:#1b5e3a;margin:20px 0 8px;}
.content h1{display:none;} .content h2:first-of-type{margin-top:4px;} .content p{margin:12px 0;}
.content blockquote{background:#eaf7ef;border-left:4px solid #27ae60;margin:14px 0;padding:10px 16px;border-radius:0 8px 8px 0;color:#1b4f30;font-size:13.5px;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:Consolas,monospace;font-size:.9em;}
.content pre{background:#0f241a;color:#dff5e8;border-radius:10px;padding:16px 18px;overflow:auto;} .content pre code{background:none;border:none;color:inherit;padding:0;}
.content strong{color:#12351f;} .content ul,.content ol{margin:12px 0;padding-left:24px;} .content li{margin:7px 0;} .content hr{border:none;border-top:1px dashed #cfe3d6;margin:30px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13px;box-shadow:0 1px 4px rgba(0,0,0,.05);border-radius:10px;overflow:hidden;}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:9px 11px;text-align:left;border-bottom:2px solid #a8dfc0;}
tbody td{padding:8px 11px;text-align:left;border-bottom:1px solid #eef3ef;} tbody tr:nth-child(even){background:#fafdfb;}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}</style></head>
<body><div class="hero"><div class="brand">KKai ｜ PHASE3 HANDOFF</div><h1>Phase3（calcWall）引き継ぎ書</h1></div>
<div class="wrap"><div class="content"><h1>KKai Phase3（calcWall）引き継ぎ書</h1>
<blockquote>
<p><strong>状態（2026-07-19 更新）：</strong> Ver0.4.3 完了・タグ済み。Phase3 は <strong>Step1〜Step3 完了</strong>。外壁は「面積では説明できない」ことが Evidence 確定し、現在は <strong>外壁原価の構造分解フェーズ</strong>（<code>WALL_COST_STRUCTURE.md</code>）。<strong>calcWall の式はまだ作らない</strong>（n=4で式を作ると過学習になり ENGINE_SPEC の思想に反するため）。</p>
</blockquote>
<h2>1. 現在地と次アクション</h2>
<ul>
<li>✅ Step1：4棟の外壁ブロック抽出（付録A）</li>
<li>✅ Step2：Variable定義（<code>VARIABLE_DEFINITIONS.md</code>）＋4棟 opening_area 確定（正典サッシ表）</li>
<li>✅ Step3：net での相関 → <strong>面積は gross/net とも外壁原価を説明しない</strong>（Evidence確定）</li>
<li>▶ 現在：<strong>構造分解</strong>。各施工系統の一次ドライバーを特定（<code>WALL_COST_STRUCTURE.md</code>）</li>
<li>次：①面材グレードの扱い ②役物の下地長 ③コーキング目地長 を数量化できるか検証 → 棟数を足して各ドライバー単体を較正 → <strong>その後に calcWall 設計</strong></li>
</ul>
<h2>2. 固定ルール（変更しない）</h2>
<ul>
<li>ENGINE_SPEC <strong>v1.0 LOCKED</strong>。コアロジック <code>tradeGenka</code>／<code>gaisanCompute</code> は無変更。</li>
<li>EngineResult 契約固定：<code>genka / qty / basis / used / fallback / confidence</code>。</li>
<li>Variables ＝ 取得した事実。<strong>Variables に推定ロジックを書かない。</strong> Engine は Variable を生成せず<strong>選択する</strong>（取得したが未使用の Variable があってよい＝Rule 3）。</li>
<li>Scope First / Evidence First。新しい仕組みは作らず、ENGINE_MAP にエンジンを1つ足す。</li>
<li><strong>式を焦って作らない。</strong> 単一変数で説明できないことが確認できたら、まず工種を施工系統へ分解して一次ドライバーを特定してからモデル化する。</li>
</ul>
<h2>3. 既存エンジン</h2>
<table>
<thead>
<tr>
<th>Engine</th>
<th>工種</th>
<th>モデル</th>
<th>n</th>
<th>最大誤差</th>
</tr>
</thead>
<tbody>
<tr>
<td>calcKiso</td>
<td>基礎工事</td>
<td><code>F + a×基礎面積A</code>（F=1,366,743 / a=2,897）</td>
<td>4</td>
<td>±5.4%</td>
</tr>
<tr>
<td>calcRoof</td>
<td>樋・屋根工事(RoofEnvelope)</td>
<td><code>F + a×軒先長</code>（F=212,823 / a=50,478）</td>
<td>4</td>
<td>+10.3%</td>
</tr>
<tr>
<td><strong>calcWall</strong></td>
<td>外壁工事</td>
<td><strong>未定・複数ドライバー（分解中）</strong></td>
<td>4</td>
<td>—</td>
</tr>
</tbody>
</table>
<blockquote>
<p>基礎＝1ドライバー、屋根＝1ドライバー、<strong>外壁＝複数ドライバー</strong>が初めて Evidence で確定。EngineResult さえ返せば内部が何項でも契約は守れるため ENGINE_SPEC v1.0 は無傷。</p>
</blockquote>
<h2>4. 4棟 確定データ（envelope・今野ガレージ内装は Scope 除外）</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th style="text-align: right;">envelope原価</th>
<th style="text-align: right;">gross</th>
<th style="text-align: right;">opening</th>
<th style="text-align: right;">net</th>
<th style="text-align: right;">開口率</th>
<th style="text-align: right;">eave長</th>
<th>面材商品</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野</td>
<td style="text-align: right;">2,452,250</td>
<td style="text-align: right;">199㎡</td>
<td style="text-align: right;">23.05㎡</td>
<td style="text-align: right;">175.95㎡</td>
<td style="text-align: right;">11.6%</td>
<td style="text-align: right;">18.8m</td>
<td>金属ガルスクエア（突出）</td>
</tr>
<tr>
<td>安原</td>
<td style="text-align: right;">1,607,050</td>
<td style="text-align: right;">164㎡</td>
<td style="text-align: right;">18.40㎡</td>
<td style="text-align: right;">145.60㎡</td>
<td style="text-align: right;">11.2%</td>
<td style="text-align: right;">12.21m</td>
<td>KMEW 新フラット16</td>
</tr>
<tr>
<td>小峰</td>
<td style="text-align: right;">1,794,150</td>
<td style="text-align: right;">181㎡</td>
<td style="text-align: right;">19.91㎡</td>
<td style="text-align: right;">161.09㎡</td>
<td style="text-align: right;">11.0%</td>
<td style="text-align: right;">24.0m</td>
<td>ニチハ ルビドフラット</td>
</tr>
<tr>
<td>村田</td>
<td style="text-align: right;">1,462,700</td>
<td style="text-align: right;">193㎡</td>
<td style="text-align: right;">18.56㎡</td>
<td style="text-align: right;">174.44㎡</td>
<td style="text-align: right;">9.6%</td>
<td style="text-align: right;">11.3m</td>
<td>KMEW シマンフラット</td>
</tr>
</tbody>
</table>
<ul>
<li>opening_area の正典は<strong>サッシ見積書／Nプランの外枠W×H</strong>（室内建具は除外）。今野は gross・原価にガレージ外壁を含むため、Scope整合上ガレージ外部開口も控除して 23.05㎡。</li>
<li>開口率は 9.6〜11.6% に収束（n=4）。</li>
</ul>
<h2>5. Step3 の結論（Evidence）</h2>
<ul>
<li>原価 vs gross面積：r=0.524／原価 vs net面積：r=0.562（4棟）。<strong>開口控除しても改善せず。</strong></li>
<li>ガレージ無し3棟のみ：原価 vs net面積 <strong>r=−0.40（負）</strong>。村田は net 最大なのに原価最小、小峰は net 中位なのに原価最高。</li>
<li>結論：<strong>面積（gross/net）は外壁原価を説明しない。</strong> 「外壁＝面積」という直感を否定できた。</li>
</ul>
<h2>6. 構造分解の結論（<code>WALL_COST_STRUCTURE.md</code> 要約）</h2>
<p>外壁原価は少なくとも次の施工系統に分解される（各施工系統の相関Evidence付き）：</p>
<ul>
<li><strong>面材（52〜62%）→ net面積 × グレード単価</strong>。面材 vs net r=0.578（弱）。実効単価 5,212〜8,596円/net㎡（グレードで±60%）。固定係数1本では不可。</li>
<li><strong>軒天＋軒廻り換気（8〜18%）→ 軒先長 eave_length</strong>。r=0.745。<strong>屋根の eave_length を再利用できる</strong>（Variables跨ぎの初例）。</li>
<li><strong>下地シート＋コーキング＋廃材（15〜19%）→ 面積（弱 r=0.29）</strong>。コーキングは目地長・塗布回数依存の隠れ数量あり。</li>
<li><strong>役物（出隅・水切・スターター・見切・板金・モール 8〜12%）→ 周長・開口の複合</strong>。出隅 vs 役物 r=0.886 は小分散の罠で棄却、単一数量に落ちない。</li>
<li><strong>諸経費（1.6〜2.0%）→ 固定費</strong>。</li>
</ul>
<p>支配構造（式ではなく構造）：</p>
<blockquote>
<p>外壁原価 ≒ [面材：net面積×グレード]＋[軒先系：∝軒先長]＋[面積系：シート・コーキング・廃材]＋[役物：周長・開口]＋[固定費]</p>
</blockquote>
<h2>7. calcWall 設計方針（決定済み）</h2>
<ul>
<li>net_wall_area は<strong>正式Variable</strong>として保持（説明変数でないが事実として保持。Engineが採用しないだけ）。</li>
<li>siding_product は保持、<code>grade_factor</code> は Evidence 不足のため<strong>作らない</strong>。</li>
<li>最小モデル1数量では不可と確定 → <strong>分解型（固定費＋面積項＋軒先項＋…）</strong>になる見込み。ただし <strong>n=4では確定しない</strong>。棟数を足して各ドライバー単体を較正してから式を作る。</li>
<li>軒先系は屋根 eave_length を再利用検討。</li>
</ul>
<h2>8. Phase3 手順（現在地＝構造分解の後半）</h2>
<ol>
<li>✅ 外壁ブロック抽出</li>
<li>✅ Variable定義・4棟 opening_area 確定</li>
<li>✅ 相関分析（単一変数不可を確定）</li>
<li>▶ <strong>構造分解（施工系統ごとの一次ドライバー）</strong> ← 現在</li>
<li>各ドライバーの数量化（グレード／役物下地長／目地長）＋棟数追加で較正</li>
<li>calcWall 実装（分解型）</li>
<li><code>ENGINE_MAP.wall</code> 登録＋JSON <code>quantity_engine:"wall"</code></li>
<li>検証・リリース（Ver0.4.4／各docを更新、VARIABLE_DEFINITIONS を v1.0 昇格）</li>
</ol>
<h2>関連ドキュメント（設計書の階層）</h2>
<pre><code>CONSTITUTION → ENGINE_PRINCIPLES → ENGINE_SPEC → VARIABLE_DEFINITIONS → WALL_COST_STRUCTURE → calcWall
</code></pre>
<ul>
<li><code>ENGINE_PRINCIPLES.md</code>（★新設・工種非依存の設計原則。第一原理／Rule1・Rule2・Rule3／ドライバー階層／Engine設計プロセス／Engine Type）</li>
<li><code>ENGINE_SPEC.md</code>（v1.0 LOCKED・EngineResult契約）／<code>ENGINE_EVALUATION.md</code>（エンジン評価台帳）</li>
<li><code>VARIABLE_DEFINITIONS.md</code>（Variables契約・opening/net/gross 定義）</li>
<li><code>WALL_COST_STRUCTURE.md</code>（外壁で Rule2 が成立した Evidence。原則は ENGINE_PRINCIPLES に分離済み）</li>
</ul>
<h2>付録A：4棟 外壁工事 全明細（Step1 生Evidence）</h2>
<h3>今野邸（合計 2,876,700 / うちガレージ[G] 424,450）</h3>
<p>金属サイディング ガルスクエア 179㎡=1,342,500／出隅 45m=60,750／水切 65m=61,750／スターター 60m=72,000／コ型見切 80m=88,000／ナナメ壁加工 1式=20,000／窯業サイディング アクセント 20㎡=170,000／シート張り 199㎡=89,550／軒天 6㎡=48,000／軒天(ケイミュー) 2㎡=11,600／軒廻り換気 46m=101,200／コーキング 199㎡=169,150／廃材 205㎡=71,750／諸経費=30,000／窓回りモール 19m=53,200／[G]ガレージ内軒天 21㎡=168,000／[G]コーキング 21㎡=17,850／[G]廃材 21㎡=7,350／屋根形状変更 -4㎡=-30,000／コーキング 199㎡=39,800／[G]ガレージ内壁 37㎡=192,400／[G]コーキング 37㎡=38,850／土台水切り 16m=11,200／軒廻り換気 19m=41,800</p>
<h3>安原邸（合計 1,607,050）</h3>
<p>本体(メイン)＋15mm通気金具 142㎡=710,000／本体(アクセント)＋通気金具 22㎡=176,000／L型出隅役物 40m=92,000／シート張り 164㎡=98,400／板金 30m=21,000／板金 17m=20,400／軒天 13㎡=126,100／軒廻り換気 48m=120,000／コーキング 142㎡=156,200／廃材 177㎡=61,950／諸経費 1式=25,000</p>
<h3>小峰邸（合計 1,794,150）</h3>
<p>メイン:ニチハ ルビドフラット 173㎡=899,600／同質出隅 31m=124,000／斜め壁部分出隅 12m=30,000／アクセント:コートリーウッド 8㎡=46,400／シート張り 181㎡=81,450／板金(土台水切) 53m=37,100／軒天 26m=209,300／軒廻り換気 50㎡=110,000／コーキング 181m=153,850／廃材 207=72,450／諸経費 1式=30,000</p>
<h3>村田様邸（合計 1,462,700）</h3>
<p>kmew シマンフラット メイン 166㎡=780,200／同 アクセント 22㎡=103,400／kmew エーデルウッド 玄関 5㎡=25,500／L型出隅 42m=96,600／シート張り 193㎡=86,850／板金(土台水切) 39m=27,300／板金(オーバーハング水切) 3m=3,600／軒天 6㎡=27,600／軒廻り換気 37m=92,500／コーキング 166㎡=124,500／廃材 199㎡=69,650／諸経費 1式=25,000</p>
<h2>付録B：4棟 開口面積（Step2 確定・正典サッシ表 外枠W×H）</h2>
<ul>
<li>今野＝23.05㎡（居室13開口16.43＋ガレージ外部開口6.62〔土間ガレージFIX1690×2230・640×2230＋テラス640×2230〕。gross・原価にガレージ外壁を含むため控除）</li>
<li>安原＝18.40㎡（AD-01玄関＋AW-01〜11 の13開口）</li>
<li>小峰＝19.91㎡（AD-01＋AW-01〜15 の17開口）</li>
<li>村田＝18.56㎡（AD-01＋AW-01〜10 の12開口）</li>
<li>補足：原価内訳書のサッシ行は棟により寸法欠落・誤ラベル（今野の土間ガレージ窓を「1階ホール」と表記）。正典はサッシ見積書／Nプラン。</li>
</ul></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-19</div></div></body></html>