<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KKai / KCP ロードマップ</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;} body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:920px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;} .hero h1{margin:6px 0 0;font-size:23px;font-weight:800;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:32px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h1{display:none;} .content h2:first-of-type{margin-top:4px;} .content p{margin:12px 0;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:Consolas,monospace;font-size:.9em;}
.content pre{background:#0f241a;color:#dff5e8;border-radius:10px;padding:16px 18px;overflow:auto;line-height:1.5;} .content pre code{background:none;border:none;color:inherit;padding:0;}
.content strong{color:#12351f;} .content ul,.content ol{margin:12px 0;padding-left:24px;} .content li{margin:7px 0;}
.content hr{border:none;border-top:1px dashed #cfe3d6;margin:30px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13.5px;overflow:hidden;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:10px 12px;text-align:left;border-bottom:2px solid #a8dfc0;}
tbody td{padding:9px 12px;text-align:left;border-bottom:1px solid #eef3ef;}
tbody tr:nth-child(even){background:#fafdfb;} .foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}
@media print{body{background:#fff;}.hero{box-shadow:none;}.content{border:none;box-shadow:none;}}</style></head>
<body><div class="hero"><div class="brand">KKai / KCP ｜ ROADMAP</div><h1>Ver0.3（UI完成）→ Ver0.4 数量化開始</h1></div>
<div class="wrap"><div class="content">
<h1>KKai / KCP ロードマップ</h1>
<p><strong>区切り：</strong> Ver0.3系で「営業が安心して使える画面」は完成。以降はUIではなく <strong>精度（数量化）</strong> のフェーズに入る。</p>
<h2>これまで — Ver0.3系（UI完成）</h2>
<table>
<thead>
<tr>
<th>Ver</th>
<th>内容</th>
<th>位置づけ</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ver0.3.1</td>
<td>3層コスト構造（変動費／固定費の分離）</td>
<td>原価思想の定義</td>
</tr>
<tr>
<td>Ver0.3.2</td>
<td>設計関連費 自動／手動</td>
<td>入力者が迷わない</td>
</tr>
<tr>
<td>Ver0.3.3</td>
<td>営業向けUI（金額表示・補足文・0円防止）</td>
<td>毎日使える画面</td>
</tr>
<tr>
<td>Ver0.3.4</td>
<td>誤操作防止（2段階の意思確認）</td>
<td>営業が間違えない</td>
</tr>
</tbody>
</table>
<p>→ ここでUIフェーズは区切り。これ以上「詳細設定」を増やさない（今が一番軽い）。</p>
<h2>これから — 精度フェーズ（坪単価 → 数量へ、1工種ずつ）</h2>
<table>
<thead>
<tr>
<th>Ver</th>
<th>内容</th>
<th>状態</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ver0.4</strong></td>
<td><strong>数量化開始（基礎）</strong> — 基礎工事を坪単価→数量ベース（外周長→基礎数量）</td>
<td>次はここ</td>
</tr>
<tr>
<td>Ver0.5</td>
<td>KCP連携 — 図面から数量生成 → KKai概算へ接続</td>
<td>予定</td>
</tr>
<tr>
<td>Ver1.0</td>
<td>住宅積算完成</td>
<td>目標</td>
</tr>
</tbody>
</table>
<h2>全体の流れ</h2>
<pre><code>Ver0.3  営業が安心して使える
   ↓
Ver0.4  数量化開始（基礎）
   ↓
Ver0.5  KCP連携
   ↓
Ver1.0  住宅積算完成
</code></pre>
<h2>この設計の核</h2>
<p>画面の中身はまだ坪単価を使っているが、設計思想は完全に「<strong>数量積算へ移行するための受け皿</strong>」になっている。3層コスト構造（①工事原価／②現場諸経費・②設計関連費）は崩さず、<code>trades</code> の各工種を坪単価から数量ベースへ差し替えるだけで精度が上がる。</p>
<p>今後はUIを増やすより、1工種ずつ坪単価を数量へ置き換えることに集中する。これがKKaiを「坪単価ソフト」から「数量積算へ自然に進化する概算エンジン」へ進める最短路。</p>
<h2>Ver0.4 の最初の一手（基礎工事の数量化）</h2>
<ul>
<li>対象：<code>trades[no=4] 基礎工事</code>（現状 cost_per_tsubo=45,758）</li>
<li>置換：延床坪 → <strong>基礎外周長・基礎数量</strong> ベースへ。</li>
<li>構造：JSON側に基礎の数量係数を持たせ、坪単価はフォールバックとして残す（データ欠損時も動く）。</li>
<li>検証：今野・安原・小峰の3棟で、数量ベース原価が実績とどれだけ一致するかを再検算。</li>
</ul>
</div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-18</div></div></body></html>