<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>概算見積（プラン段階）— Ver0.3.0 マイルストーン</title>
<style>
:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:900px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;}
.hero h1{margin:6px 0 0;font-size:24px;font-weight:800;line-height:1.35;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:34px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h1{display:none;}
.content h2:first-of-type{margin-top:4px;}
.content p{margin:12px 0;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:'SFMono-Regular',Consolas,monospace;font-size:.9em;}
.content strong{color:#12351f;}
.content ul,.content ol{margin:12px 0;padding-left:24px;}
.content li{margin:7px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13.5px;overflow:hidden;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:10px 12px;text-align:right;border-bottom:2px solid #a8dfc0;white-space:nowrap;}
thead th:first-child,tbody td:first-child{text-align:left;}
tbody td{padding:9px 12px;text-align:right;border-bottom:1px solid #eef3ef;white-space:nowrap;}
tbody tr:nth-child(even){background:#fafdfb;}
tbody tr:hover{background:#f2fbf5;}
.callout{background:#fff8ec;border-left:4px solid #f0a500;border-radius:8px;padding:2px 16px;margin:14px 0;}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}
@media print{body{background:#fff;}.hero{box-shadow:none;}.content{border:none;box-shadow:none;}}
</style></head>
<body><div class="hero"><div class="brand">KKai MILESTONE ｜ Ver 0.3.0</div><h1>概算見積（プラン段階）— Ver0.3.0 マイルストーン</h1></div>
<div class="wrap"><div class="content">
<h1>KKai Ver0.3.0 マイルストーン — 概算見積（プラン段階）</h1>
<h2>定義（プロジェクトの核）</h2>
<p><strong>KKai Ver0.3 は「概算金額を当てるAI」ではなく「利益を守るための概算エンジン」。</strong>
目的は原価を当てることではなく、着工粗利の下限を守ること。3棟検証（今野・安原・小峰）で
「積算は正しく、粗利を落としたのは商談時の丸め値引き」を数字で証明した。これはKKaiが
積算ソフトから経営支援ソフトへ変わった瞬間である。</p>
<h2>目的</h2>
<p>プラン作成段階で、仮プラン平面図の延床坪数から「ちょっと高め」の概算を出し、
着工時の粗利28〜30%を確保できるようにする。</p>
<h2>方式（坪単価法 v0 ＋ 安全係数）</h2>
<p>AI図面認識は使わず、延床坪数1本を入力とする最小構成。</p>
<pre><code>仮プラン延床（坪）
    ↓  × cost_per_tsubo（基準原価 ÷ 基準延床31.9坪。JSONに計算済みで保持）
概算原価（25工種）
    ↓  ÷ (1 − 目標粗利率)
素価格（目標粗利ライン）
    ↓  × 安全係数（粗利・値引き・端数を丸ごと吸収する“ちょっと高め”係数）
提示概算（税込・1万円切上げ）
</code></pre>
<ul>
<li><strong>素価格</strong>：目標粗利で成立する価格ライン。商談でこの線を割って値引きすると着工粗利は目標割れ。</li>
<li><strong>安全係数</strong>：営業が「今回は1.08」と直感で選べる単一値。値引率を固定しない現実に合わせた設計。</li>
</ul>
<h2>レビュー反映（実装前の4点）</h2>
<ol>
<li><code>genka</code> → <strong><code>base_cost</code></strong>（今野31.9坪から導いた基準原価であることを明確化）</li>
<li><strong><code>cost_per_tsubo</code> をJSONに計算済みで保持</strong>（実行時に÷31.9しない）</li>
<li>諸経費を trades から外し <strong><code>fixed.overhead</code></strong> に統一（trade26を廃止 → 25工種）</li>
<li>UIの「想定丸め値引き率」→ <strong>「安全係数（Safety Factor）」</strong> に変更</li>
</ol>
<h2>検証（実コード・3棟 / 目標30%・安全係数1.08）</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th>延床(坪)</th>
<th>概算原価</th>
<th>素価格</th>
<th>提示税込(丸め)</th>
<th>提示時粗利</th>
<th>素価格を実原価で見た粗利</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野(基準)</td>
<td>31.9</td>
<td>27,013,813</td>
<td>39,961,162</td>
<td>47,480,000</td>
<td>37.4%</td>
<td>32.4%</td>
</tr>
<tr>
<td>安原</td>
<td>22.8</td>
<td>19,307,678</td>
<td>28,952,398</td>
<td>34,400,000</td>
<td>38.3%</td>
<td>30.0%</td>
</tr>
<tr>
<td>小峰</td>
<td>33.1</td>
<td>28,055,412</td>
<td>41,449,159</td>
<td>49,250,000</td>
<td>37.3%</td>
<td>41.8%</td>
</tr>
</tbody>
</table>
<ul>
<li>cost_per_tsubo方式でも今野の基準原価を再現（27,013,813 vs 実27,013,747、差66円＝丸め）。</li>
<li>3棟とも素価格ライン＝目標粗利30%以上を確保。安全係数が商談の値引き余地。</li>
</ul>
<h2>基準データ（真実は1つ = KCP）</h2>
<ul>
<li><code>housing/gaisan_basis.json</code> … meta / fixed.overhead / trades[base_cost, cost_per_tsubo]</li>
<li>画面はこれを fetch。読めない時のみ内蔵フォールバック（drawings.json と同方式）</li>
<li>出典：今野様邸 原価内訳書（見積ID 22094675-4928491 / 2026-07-04）</li>
</ul>
<h2>今回変更しなかったもの（Scope First）</h2>
<ul>
<li>「新築住宅積算（sekisan-view）」のロジック・変数生成ログ・Drawing Set：無変更</li>
<li>「見積変換ツール（tool-view）」のパーサ・粗利計算・出力：無変更</li>
<li>会社情報・設定・localStorage：無変更</li>
<li>概算は既存Rule Engineとは独立（坪単価法）</li>
</ul>
<h2>将来（ハイブリッド概算＝Ver1.0の最終形）</h2>
<p>工種ごとに坪単価→数量ベースへ1つずつ差し替える。</p>
<pre><code>基礎  ： 延床 → 基礎外周長 → 基礎数量 → 基礎原価（V004）
屋根  ： 延床 → 屋根数量 → 屋根原価
木工事： 延床（坪のまま）
設備  ： 延床（坪のまま）
</code></pre>
<p>→「基礎だけ数量／屋根だけ数量／木工事・設備は坪」というハイブリッド概算に育つ。
cost_per_tsubo をJSONで持つ現構造は、工種単位で数量式へ差し替えても他工種に影響しない。</p>
<h2>ロードマップ（3棟検証から最も自然な流れ）</h2>
<p>Ver0.4 のテーマは「精度向上」ではなく「誤差の原因を分解すること」。
- <strong>V0.4：工種別誤差分析</strong> — どの工種が坪単価法でぶれやすいか（基礎・木工事・設備）。小峰−14%の原因（SW/ガレージ/工種構成）を切り分ける。
- <strong>V0.5：数量ベースへの置換</strong> — ぶれの大きい工種から数量式へ（まず基礎工事の外周長→基礎数量）。
- <strong>V1.0：ハイブリッド概算エンジン</strong> — 坪単価法と数量ベースを組み合わせる（基礎だけ数量／屋根だけ数量／木工事・設備は坪）。</p>
<h2>基準データの版管理（平均にはしない）</h2>
<p>n=3で平均を取ると偶然に引っ張られるため、平均化はまだ早い。今野を残して版管理する。
- 現行（今野単独）を <strong><code>reference=n1</code></strong> として据え置き（上書きしない）。
- <strong><code>reference=n3</code></strong> を別に作り、いつでも n1 と比較できるようにする。
- 将来像：<code>basis/reference_n1.json</code> / <code>reference_n3.json</code> / <code>reference_sw.json</code> / <code>reference_standard.json</code></p>
<h2>保留・運用課題</h2>
<ul>
<li>V004（基礎外周長）：基礎工事だけ数量ベース化（V0.5で着手）</li>
<li>仕様係数（SW有無・ビルトインガレージ有無）での層別化は、V0.4の工種別分析の結果を見てから判断</li>
<li>粗利21.9%の本丸は商談時の丸め値引き運用（KKai範囲外の社内運用課題）。概算アンカーを商談基準額として運用ルール化</li>
</ul>
</div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-13</div></div></body></html>