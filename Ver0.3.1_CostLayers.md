<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Ver0.4.0 Phase1 基礎数量化</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;} body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:920px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;} .hero h1{margin:6px 0 0;font-size:23px;font-weight:800;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:32px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h1{display:none;} .content h2:first-of-type{margin-top:4px;} .content p{margin:12px 0;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:Consolas,monospace;font-size:.9em;}
.content pre{background:#0f241a;color:#dff5e8;border-radius:10px;padding:16px 18px;overflow:auto;} .content pre code{background:none;border:none;color:inherit;padding:0;}
.content strong{color:#12351f;} .content ul,.content ol{margin:12px 0;padding-left:24px;} .content li{margin:7px 0;} .content hr{border:none;border-top:1px dashed #cfe3d6;margin:30px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13px;overflow:hidden;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:9px 10px;text-align:right;border-bottom:2px solid #a8dfc0;}
thead th:first-child,tbody td:first-child{text-align:left;} tbody td{padding:8px 10px;text-align:right;border-bottom:1px solid #eef3ef;} tbody td:first-child{text-align:left;}
tbody tr:nth-child(even){background:#fafdfb;} .foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}</style></head>
<body><div class="hero"><div class="brand">KKai ｜ Ver0.4.0 数量エンジン開始</div><h1>Phase1：基礎工事の数量化（4棟）</h1></div>
<div class="wrap"><div class="content"><h1>Ver0.4.0 数量エンジン開始 — Phase1：基礎工事の数量化（4棟データ）</h1>
<p><strong>位置づけ：</strong> 坪単価法の役割は終わり、工種を数量ベースへ置換するVer0.4.0を開始。その第一歩＝基礎工事。4棟（今野・安原・小峰・村田）の原価内訳書から基礎の数量明細を抽出し、モデル化の土台を固めた。</p>
<h2>4棟の基礎データ</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th>基礎原価</th>
<th>基礎面積A(㎡)</th>
<th>外周長P(m)</th>
<th>耐圧(㎥)</th>
<th>立上り(㎥)</th>
<th>原価/A</th>
<th>原価/P</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野</td>
<td>1,459,675</td>
<td>53.00</td>
<td>35.50</td>
<td>18.5</td>
<td>5.5</td>
<td>27,541</td>
<td>41,118</td>
</tr>
<tr>
<td>安原</td>
<td>1,565,683</td>
<td>39.75</td>
<td>26.40</td>
<td>14.0</td>
<td>4.5</td>
<td>39,388</td>
<td>59,306</td>
</tr>
<tr>
<td>小峰</td>
<td>1,724,743</td>
<td>114.86</td>
<td>49.14</td>
<td>25.0</td>
<td>4.0</td>
<td>15,016</td>
<td>35,099</td>
</tr>
<tr>
<td>村田</td>
<td>1,498,886</td>
<td>62.30</td>
<td>34.58</td>
<td>14.0</td>
<td>4.5</td>
<td>24,059</td>
<td>43,345</td>
</tr>
</tbody>
</table>
<p>（A＝スラブスキ取り＝型枠面積＝基礎面積、P＝外周掘削長。いずれも平面図から拾える。）</p>
<h2>発見1 — 単価は会社標準で安定、数量が原価を決める</h2>
<p>基礎工事の明細は4棟で共通：外周掘削(P)、スラブ/型枠(A)、RC砕石、捨てコン、耐圧、立上り、鉄筋、付帯（ポンプ・ユンボ・玄関土間・アンカー・生コン試験・諸経費）。単価は会社標準でほぼ一定。<strong>変わるのは数量だけ</strong>。これが「数量化すれば原価を説明できる」根拠。</p>
<h2>発見2 — 基礎は「固定費（大）＋ 面積・外周比例分」</h2>
<p>原価/A が 15,016〜39,388（2.6倍）、原価/P が 35,099〜59,306（1.7倍）とばらつく。理由は、ポンプ・ユンボ・玄関土間・鉄筋・生コン試験・諸経費など<strong>規模に関係しない固定費が基礎に大きく含まれる</strong>ため。
→ 小型の安原は固定費が相対的に重く、単価当たりでは高く見える（外れ値の正体）。基礎原価は単純な「面積×単価」ではなく <strong>固定費 + a×A + b×P</strong> の形が正しい。</p>
<h2>発見3 — なぜ坪単価では説明できないか</h2>
<p>延床坪単価（45,758/坪）で村田を出すと 1,435,428、実績1,498,886に対し−4.2%と偶然近い。だがこれは固定費と面積のバランスが<strong>たまたま合っただけ</strong>。数量モデルなら「村田は総二階で基礎面積が延床に対し小さい→基礎が相対的に安い」と<strong>理由を説明できる</strong>。エンジンは平均ではなく、理由を持つべき——今回の方針の核心。</p>
<h2>Phase1 モデル案（Ver0.4.0）</h2>
<pre><code>基礎原価 = 固定費F + a × 基礎面積A(㎡) + b × 外周長P(m)
        （F,a,b は会社標準単価から導出。4棟でフィット・検証）
</code></pre>
<ul>
<li>JSONに <code>trades[基礎]</code> の数量モデルを追加。<strong>坪単価はフォールバックとして残す</strong>（数量が未取得のプラン段階でも動く）。</li>
<li>安原型の特殊要因（地盤改良・深基礎など、面積・外周で説明できない上振れ）は<strong>補正係数／フラグ</strong>で扱い、モデル本体は汚さない。</li>
</ul>
<h2>次に決めること（プラン段階の入力）</h2>
<p>数量化には基礎面積Aと外周長Pが要る。プラン段階でこれをどう得るか：
（1）平面図から直接入力（最も正確）／（2）延床・階数・総二階率などから推定（入力は延床のみで簡便）。
ここを決めれば、係数フィット → JSON追加 → 村田で再検証、へ進める。3層コスト構造は不変。</p>
<hr />
<h2>実装完了（Ver0.4.0）</h2>
<p>基礎コストモデルと自動推定UIをエンジンに実装した。3層コスト構造は不変。</p>
<p><strong>モデル：</strong> <code>基礎原価 = 1,366,743 + 2,897 × 基礎面積A(㎡)</code>（外周単独・A+P同時は過学習のため不採用。基礎は固定費が支配的なためF+a×Aを採用。最大誤差5.4%／n=4暫定）。</p>
<p><strong>入力（合意仕様）：</strong> 「延床＋建物形状」→ 基礎面積A・外周長Pを自動推定 → 詳細で実測値に上書き可（積算段階）。
- 形状：総二階／部分2階／L型／コの字／平屋。A=延床㎡×形状比、P=4√A×形状係数。
- 自動推定＝営業が30秒、実測上書き＝積算で精度UP、実績蓄積で推定式を学習（将来）。
- 数量未使用・A未取得時は<strong>坪単価にフォールバック</strong>（プラン初期でも必ず動く）。</p>
<p><strong>4棟検証（実測Aで）：</strong> 今野+4.2%／安原−5.4%／小峰−1.5%／村田+3.2%。基礎の工種テーブルに「数量」バッジ表示。</p>
<p><strong>位置づけ：</strong> 基礎は固定費支配で精度改善幅は小さいが、<strong>数量→原価のパイプラインを確立した最初の工種</strong>。次のPhase2（屋根面積）・Phase3（外壁面積）は変動費の比重が大きく、精度改善の本丸。</p></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-18</div></div></body></html>