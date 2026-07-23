<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>外壁原価の構造分解（Wall Cost Structure）</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
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
<body><div class="hero"><div class="brand">KKai ｜ WALL COST STRUCTURE</div><h1>外壁原価の構造分解（Wall Cost Structure）</h1></div>
<div class="wrap"><div class="content"><h1>KKai 外壁原価の構造分解（Wall Cost Structure）</h1>
<blockquote>
<p><strong>DRAFT / 2026-07-19</strong> — 本書は <code>ENGINE_PRINCIPLES.md</code> の <strong>Rule 2（Trade ≠ Driver）が外壁で成立したことを示す Evidence 文書</strong>。設計原則そのもの（第一原理・Rule 1/2/3・ドライバー階層・Engine 設計プロセス・Engine Type）は <code>ENGINE_PRINCIPLES.md</code> にある。本書は<strong>外壁固有の Evidence</strong> に限定する。式（calcWall）はまだ作らない。</p>
</blockquote>
<h2>なぜ外壁で「施工系統へ分解」したのか</h2>
<p>基礎は「コンクリート量」、屋根は「軒先長」という単一の施工系統で説明できた。しかし外壁は<strong>面積（gross/net）単独では説明できない</strong>（ガレージ無し3棟で net vs 原価 r=−0.40）。理由は、外壁が <strong>面材・軒裏・役物・シーリング</strong>という物理的に別々の施工系統の合成だから。これが Rule 2（Trade ≠ Driver）の最初の実証であり、外壁は「1工種＝1ドライバー」が崩れた初の工種になった。</p>
<h2>前提（Scope・4棟 envelope）</h2>
<ul>
<li>今野のガレージ内装は Scope 除外（原価 424,450円）。envelope 原価で比較。</li>
<li>開口は正典サッシ表（外枠W×H）。今野は gross・原価にガレージ外壁を含むため、Scope整合上ガレージ外部開口も控除して opening_area = 23.05㎡。</li>
</ul>
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
</tr>
<tr>
<td>安原</td>
<td style="text-align: right;">1,607,050</td>
<td style="text-align: right;">164㎡</td>
<td style="text-align: right;">18.40㎡</td>
<td style="text-align: right;">145.60㎡</td>
<td style="text-align: right;">11.2%</td>
<td style="text-align: right;">12.21m</td>
</tr>
<tr>
<td>小峰</td>
<td style="text-align: right;">1,794,150</td>
<td style="text-align: right;">181㎡</td>
<td style="text-align: right;">19.91㎡</td>
<td style="text-align: right;">161.09㎡</td>
<td style="text-align: right;">11.0%</td>
<td style="text-align: right;">24.0m</td>
</tr>
<tr>
<td>村田</td>
<td style="text-align: right;">1,462,700</td>
<td style="text-align: right;">193㎡</td>
<td style="text-align: right;">18.56㎡</td>
<td style="text-align: right;">174.44㎡</td>
<td style="text-align: right;">9.6%</td>
<td style="text-align: right;">11.3m</td>
</tr>
</tbody>
</table>
<h2>カテゴリ構成比（envelope・全4棟で検算一致）</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th style="text-align: right;">面材</th>
<th style="text-align: right;">下地シート</th>
<th style="text-align: right;">コーキング</th>
<th style="text-align: right;">廃材</th>
<th style="text-align: right;">軒天</th>
<th style="text-align: right;">軒廻り換気</th>
<th style="text-align: right;">役物(周長)</th>
<th style="text-align: right;">開口まわり</th>
<th style="text-align: right;">諸経費</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野</td>
<td style="text-align: right;">61.7%</td>
<td style="text-align: right;">3.7%</td>
<td style="text-align: right;">8.5%</td>
<td style="text-align: right;">2.9%</td>
<td style="text-align: right;">2.4%</td>
<td style="text-align: right;">5.8%</td>
<td style="text-align: right;">12.0%</td>
<td style="text-align: right;">2.2%</td>
<td style="text-align: right;">2.0%</td>
</tr>
<tr>
<td>安原</td>
<td style="text-align: right;">55.1%</td>
<td style="text-align: right;">6.1%</td>
<td style="text-align: right;">9.7%</td>
<td style="text-align: right;">3.9%</td>
<td style="text-align: right;">7.8%</td>
<td style="text-align: right;">7.5%</td>
<td style="text-align: right;">8.3%</td>
<td style="text-align: right;">0%</td>
<td style="text-align: right;">1.6%</td>
</tr>
<tr>
<td>小峰</td>
<td style="text-align: right;">52.7%</td>
<td style="text-align: right;">4.5%</td>
<td style="text-align: right;">8.6%</td>
<td style="text-align: right;">4.0%</td>
<td style="text-align: right;">11.7%</td>
<td style="text-align: right;">6.1%</td>
<td style="text-align: right;">10.7%</td>
<td style="text-align: right;">0%</td>
<td style="text-align: right;">1.7%</td>
</tr>
<tr>
<td>村田</td>
<td style="text-align: right;">62.2%</td>
<td style="text-align: right;">5.9%</td>
<td style="text-align: right;">8.5%</td>
<td style="text-align: right;">4.8%</td>
<td style="text-align: right;">1.9%</td>
<td style="text-align: right;">6.3%</td>
<td style="text-align: right;">8.7%</td>
<td style="text-align: right;">0%</td>
<td style="text-align: right;">1.7%</td>
</tr>
</tbody>
</table>
<p>（今野のみ 屋根形状変更調整 −1.2%、諸経費にナナメ壁加工を含む）</p>
<h2>外壁の施工系統ごとの一次ドライバー（施工原理が先・統計は裏付け）</h2>
<p>ドライバー階層の定義は <code>ENGINE_PRINCIPLES.md</code> を参照。以下は外壁で観測した各施工系統の一次ドライバーと、その施工原理・裏付け。</p>
<h3>A. 面材（52〜62%・最大）</h3>
<ul>
<li><strong>施工原理：</strong> サイディングは外壁面のうち開口を除いた実貼り面に、商品ごとの単価で施工される。一次ドライバーは <strong>net面積</strong>、二次ドライバーは<strong>面材グレード（siding_product）</strong>。形は <code>net面積 × グレード単価</code>。</li>
<li><strong>裏付け：</strong> 面材実効単価は 今野 8,596／安原 6,085／小峰 5,872／村田 5,212 円/net㎡ と金属＞窯業のグレード順に並ぶ。面材 vs net面積 r=0.578 は面積単独では弱いが、これは単価がグレードで±60%動くためで、「net面積が不要」という意味ではない。</li>
</ul>
<h3>B. 軒天＋軒廻り換気（8〜18%）</h3>
<ul>
<li><strong>施工原理：</strong> 軒天材・軒裏換気材は軒の出（軒先・けらば）に沿って施工される線的部材。一次ドライバーは <strong>軒先長 eave_length</strong>。屋根 calcRoof の「縁部材は軒先長に比例」と同じ物理。</li>
<li><strong>裏付け：</strong> 軒天＋換気 vs 軒先長 r=0.745。小峰（24.0m→319,300）と村田（11.3m→120,100）が両端を締める。<strong>外壁の軒裏系は屋根の eave_length を工種跨ぎで再利用できる</strong>（初例）。</li>
</ul>
<h3>C. 下地シート＋コーキング＋廃材（15〜19%）</h3>
<ul>
<li><strong>施工原理：</strong> 透湿防水シートは壁全面、コーキングは面材の<strong>目地（継手）長</strong>、廃材は施工量。面積系だが、コーキングは目地長という別数量を内包する。</li>
<li><strong>裏付け：</strong> 面積系 vs 面積 r=0.29（弱）。今野は2回塗り（169,150＋39,800）で膨らむなど、目地長・塗布回数のノイズが乗り、純粋な面積比例には落ちない。</li>
</ul>
<h3>D. 役物（出隅・水切・スターター・見切・板金・モール／8〜12%）</h3>
<ul>
<li><strong>施工原理：</strong> 建物の稜線（出隅・入隅）・底辺（水切・スターター）・開口周り（見切・モール）に沿う線的部材。一次ドライバーは複数の下地長（外周長・開口周長・底辺長）の<strong>合成</strong>で、単一数量に落ちない。</li>
<li><strong>裏付け：</strong> 役物 vs 出隅長 r=0.886 は<strong>棄却</strong>（出隅は4棟40〜45mで分散が無く、小分散変数の見かけ相関。回帰傾きが非現実的）。役物 vs net r=0.519。</li>
</ul>
<h3>E. 諸経費（1.6〜2.0%）</h3>
<ul>
<li><strong>施工原理：</strong> 現場共通費。一次ドライバーは<strong>固定費</strong>。</li>
</ul>
<h2>結論（外壁の Evidence）</h2>
<ul>
<li><strong>面積（gross/net）単独では外壁原価を説明できない</strong>（3棟 net vs 原価 r=−0.40）。だが「面積が無関係」ではなく、外壁が複数の施工系統の合成だから。</li>
<li>外壁の支配構造（式ではなく構造）：<blockquote>
<p>外壁原価 ≒ [面材：net面積 × グレード]＋[軒裏系：∝ 軒先長]＋[面積系：シート・コーキング（目地長）・廃材]＋[役物：外周・開口・底辺の下地長の合成]＋[固定費：諸経費]</p>
</blockquote>
</li>
<li>これが Rule 2 の最初の実証。設計上の含意（Engine 内部で施工系統別に計算し合成）は <code>ENGINE_PRINCIPLES.md</code> 参照。</li>
</ul>
<h2>次にやること（外壁固有・式より先に）</h2>
<ol>
<li><strong>面材のグレード（二次ドライバー）</strong>：siding_product（金属／窯業／付加断熱）で単価帯が分かれるかを施工原理と棟数追加で検証。grade は Evidence が揃うまで確定係数化しない。</li>
<li><strong>役物の下地長</strong>を数量として取れるか（外周長 P・開口周長・水切底辺長）。Variables に候補追加（保持のみ）。</li>
<li><strong>コーキングの目地長</strong>が面材枚数・割付から出せるか（面積系のノイズ源）。</li>
<li>上記が揃い、棟数を足して各施工系統を単体で較正できて初めて、<strong>合成型 calcWall</strong> を設計する。n=4 では確定しない。</li>
</ol></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-19</div></div></body></html>