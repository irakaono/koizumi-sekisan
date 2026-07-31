<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KKai Ver0.3.1 コスト3層構造</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
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
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13.5px;overflow:hidden;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:10px 12px;text-align:right;border-bottom:2px solid #a8dfc0;white-space:nowrap;}
thead th:first-child,tbody td:first-child{text-align:left;} tbody td{padding:9px 12px;text-align:right;border-bottom:1px solid #eef3ef;white-space:nowrap;} tbody td:first-child{text-align:left;}
tbody tr:nth-child(even){background:#fafdfb;} .foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}
@media print{body{background:#fff;}.hero{box-shadow:none;}.content{border:none;box-shadow:none;}}</style></head>
<body><div class="hero"><div class="brand">KKai CHANGELOG ｜ Ver0.3.1</div><h1>変動費・固定費の分離（3層コスト構造）</h1></div>
<div class="wrap"><div class="content">
<h1>KKai Ver0.3.1 — 変動費・固定費の分離（3層コスト構造）</h1>
<h2>目的</h2>
<p>概算を「利益を設計する」道具にするため、コストを性質で分離した。
KKaiが「工事を積算する」から「利益を設計する」へ進む分岐点。</p>
<h2>3層コスト構造</h2>
<table>
<thead>
<tr>
<th>層</th>
<th>内容</th>
<th>性質</th>
<th>V0.3.1</th>
</tr>
</thead>
<tbody>
<tr>
<td>① 工事原価</td>
<td>材料・外注・労務（24工種）</td>
<td>数量／坪単価で決まる変動費</td>
<td>実装</td>
</tr>
<tr>
<td>② プロジェクト固定費</td>
<td>現場諸経費（工事原価×率）＋設計関連費（固定）</td>
<td>原価に比例／案件管理コスト</td>
<td>実装</td>
</tr>
<tr>
<td>③ 会社経費</td>
<td>販管費・利益</td>
<td>会社方針で決まる</td>
<td>未実装（V0.5以降）</td>
</tr>
</tbody>
</table>
<p>※「18〜21%」は現場諸経費ではなく③会社経費（販管費）の水準。混同を避けるためV0.3.1には入れない。</p>
<h2>計算フロー（V0.3の思想は不変）</h2>
<pre><code>① 工事原価 = Σ(cost_per_tsubo × 延床坪)
② 現場諸経費 = 工事原価 × 現場諸経費率
② 設計関連費 = 固定額（延床帯テーブル／手入力上書き可）
   総原価 = ① + ② + ②
   素価格 = 総原価 ÷ (1 − 目標粗利率)     ← 目標粗利ライン
   提示   = 素価格 × 安全係数
   提示（税込）= 1万円切上げ
</code></pre>
<h2>デフォルト値（3棟実績から算出・決め打ちしない）</h2>
<table>
<thead>
<tr>
<th>項目</th>
<th>今野</th>
<th>安原</th>
<th>小峰</th>
<th>既定</th>
</tr>
</thead>
<tbody>
<tr>
<td>現場諸経費率（工事原価比）</td>
<td>5.24%</td>
<td>5.88%</td>
<td>6.46%</td>
<td><strong>5.9%</strong>（平均5.86%）</td>
</tr>
<tr>
<td>設計関連費（原価）</td>
<td>872,600</td>
<td>705,700</td>
<td>766,990</td>
<td><strong>780,000</strong>（平均781,763・暫定）</td>
</tr>
</tbody>
</table>
<ul>
<li>設計関連費は延床帯テーブル構造のみ先行実装。1棟/帯で根拠不足のため全帯とも暫定780,000。棟数が増えたら実績で更新する。</li>
<li>設計関連費には設計／確認申請／長期優良／性能評価等が混在しうるため、分離はデータが増えてから判断。</li>
</ul>
<h2>データ構造（gaisan_basis.json）</h2>
<ul>
<li><code>trades</code>：24工種（<strong>設計・申請を工事原価から分離</strong>）。</li>
<li><code>fixed.genba_keihi_rate</code>：現場諸経費率。</li>
<li><code>fixed.design_fee</code>：<code>default</code> ＋ <code>table</code>（延床帯）。JSONで変更可能。</li>
<li><code>meta.cost_model</code>：3層構造を明文化。</li>
<li>reference=n1（今野基準）は据え置き。cost_per_tsuboは四捨五入保持。</li>
</ul>
<h2>UI（画面はシンプルに）</h2>
<p>入力は「現場諸経費率(%)／設計関連費(円)／目標着工粗利率(%)／安全係数」。
延床を変えると設計費は延床帯から自動更新（手入力すると以後その値を尊重）。
結果に「①工事原価 ＋ ②現場諸経費 ＋ ②設計関連費 ＝ 総原価」の内訳を表示。</p>
<h2>検証（3棟・現場諸経費5.9%／設計費78万／目標30%／安全係数1.08）</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th>工事原価</th>
<th>現場諸経費</th>
<th>設計費</th>
<th>総原価</th>
<th>提示税込(丸め)</th>
<th>提示時粗利</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野</td>
<td>26,141,221</td>
<td>1,542,332</td>
<td>780,000</td>
<td>28,463,553</td>
<td>48,310,000</td>
<td>35.2%</td>
</tr>
<tr>
<td>安原</td>
<td>18,684,007</td>
<td>1,102,356</td>
<td>780,000</td>
<td>20,566,364</td>
<td>34,910,000</td>
<td>35.2%</td>
</tr>
<tr>
<td>小峰</td>
<td>27,149,174</td>
<td>1,601,801</td>
<td>780,000</td>
<td>29,530,975</td>
<td>50,120,000</td>
<td>35.2%</td>
</tr>
</tbody>
</table>
<p>今野の工事原価26,141,221は実測26,141,147（総原価−設計872,600）とほぼ一致（cost_per_tsubo丸め差）。
提示時粗利35.2%は素価格（目標粗利ライン30%）に安全係数1.08を掛けた"ちょっと高め"の水準。</p>
<h2>今回変更しなかったもの</h2>
<ul>
<li>新築住宅積算（sekisan-view）・見積変換ツール（tool-view）は無変更。</li>
<li>会社経費（③販管費・利益）は未実装。次に足すときも同じ3層構造のまま拡張できる。</li>
</ul>
</div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-13</div></div></body></html>