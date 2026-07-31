<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>KKai 数量エンジン評価シート</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;} body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:920px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;} .hero h1{margin:6px 0 0;font-size:22px;font-weight:800;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:30px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h1{display:none;} .content h2:first-of-type{margin-top:4px;} .content p{margin:12px 0;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:Consolas,monospace;font-size:.9em;}
.content strong{color:#12351f;} .content ul,.content ol{margin:10px 0;padding-left:22px;} .content li{margin:6px 0;} .content hr{border:none;border-top:1px dashed #cfe3d6;margin:26px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13px;box-shadow:0 1px 4px rgba(0,0,0,.05);border-radius:10px;overflow:hidden;}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:9px 11px;text-align:left;border-bottom:2px solid #a8dfc0;}
tbody td{padding:8px 11px;text-align:left;border-bottom:1px solid #eef3ef;} tbody tr:nth-child(even){background:#fafdfb;}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}</style></head>
<body><div class="hero"><div class="brand">KKai ｜ ENGINE EVALUATION LOG</div><h1>数量エンジン評価シート</h1></div>
<div class="wrap"><div class="content"><h1>KKai 数量エンジン評価シート（Engine Evaluation Log）</h1>
<p><strong>目的：</strong> 各数量エンジンの「採用した変数」「棟数」「誤差」「状態」を同一フォーマットで記録し、採用理由・却下変数・再評価条件を1エンジン1ページで残す。将来30棟に増えても「なぜその変数を採用したか」を完全に追跡できるようにする（Evidence First の台帳）。ENGINE_SPEC v1.0 に準拠。</p>
<h2>一覧</h2>
<table>
<thead>
<tr>
<th>Engine</th>
<th>工種</th>
<th>採用変数</th>
<th>棟数</th>
<th>最大誤差</th>
<th>状態</th>
</tr>
</thead>
<tbody>
<tr>
<td>calcKiso</td>
<td>基礎工事</td>
<td>基礎面積A</td>
<td>4</td>
<td>±5.4%</td>
<td>採用（Ver0.4.0）</td>
</tr>
<tr>
<td>calcRoof</td>
<td>樋・屋根工事(RoofEnvelope)</td>
<td>軒先長 eave_length</td>
<td>4</td>
<td>+10.3%</td>
<td>採用（Ver0.4.3）</td>
</tr>
<tr>
<td>calcWall</td>
<td>外壁工事</td>
<td>（外壁面積 想定）</td>
<td>–</td>
<td>–</td>
<td>未着手（Phase3）</td>
</tr>
</tbody>
</table>
<p>confidence 目安：実測0.90〜0.95／自動推定0.78〜0.88／坪単価フォールバック0.55〜0.65。</p>
<hr />
<h2>calcKiso（基礎工事）</h2>
<ul>
<li><strong>採用モデル：</strong> <code>基礎原価 = 1,366,743 + 2,897 × 基礎面積A(㎡)</code>（n=4暫定）</li>
<li><strong>棟数 / 誤差：</strong> 4棟（今野+4.2%／安原−5.4%／小峰−1.5%／村田+3.2%）→ 最大±5.4%</li>
<li><strong>採用理由：</strong> 基礎は固定費（ポンプ・ユンボ・玄関土間・鉄筋・生コン試験・諸経費）が支配的で、変動分は基礎面積に比例。物理構成に一致し、係数もすべて正。</li>
<li><strong>却下した変数：</strong></li>
<li>外周長P単独 … 面積より説明力が低い。</li>
<li>面積A＋外周P（2数量）… n=4で外周係数がマイナス（過学習）。</li>
<li>延床坪単価 … 総二階でA/延床比が小さい棟（村田）を過大評価（+14%）。</li>
<li><strong>再評価条件：</strong> 棟数増で係数更新。特に小型で固定費が相対的に重い棟（安原型）や、地盤改良・深基礎の特殊要因は補正フラグで扱う。</li>
<li><strong>保持Variables：</strong> 基礎面積A・外周長P（Pは将来の立上り/外周系モデル用に保持、現モデル未使用）。</li>
</ul>
<hr />
<h2>calcRoof（樋・屋根工事 / RoofEnvelope）</h2>
<ul>
<li><strong>採用モデル：</strong> <code>屋根原価 = 212,823 + 50,478 × 軒先長(m)</code>（n=4暫定）</li>
<li><strong>棟数 / 誤差：</strong> 4棟（今野−3.8%／安原+10.3%／小峰+1.5%／村田−6.4%）→ 最大+10.3%</li>
<li><strong>採用理由：</strong> この工種は屋根材だけでなく樋・軒先換気・雪止・破風・水切・役物（＝縁まわり部材）を含む広い工種（RoofEnvelope）。縁の部材が原価を支配し、それが軒先長に比例する。<strong>統計ではなく工種の物理構成から説明できる</strong>（単相関：軒先長0.98＞屋根面積0.87）。</li>
<li><strong>却下した変数：</strong></li>
<li>屋根面積単独 … F+a×面積で最大−18%（今野の造作庇・破風を拾えない）。</li>
<li>面積＋軒先長（2数量）… 軒先長を入れると面積係数≈0（面積は不要）。</li>
<li>面積＋ケラバ（2数量）… 誤差1%だが係数がマイナス（過学習）。</li>
<li>棟長 … 単相関0.65と弱い（片流れは棟=0）。</li>
<li><strong>再評価条件：</strong> ~20棟集まった時点で 屋根面積・軒先長・複合モデルを再比較。将来 屋根材／樋／破風／換気が別工種に分かれると相関が変わるため要再評価。</li>
<li><strong>保持Variables：</strong> roof_area・eave_length・ridge_length・gable_length（全保持。現モデルは eave_length のみ使用）。</li>
</ul>
<hr />
<h2>calcWall（外壁工事・Phase3 未着手）</h2>
<ul>
<li><strong>想定変数：</strong> 外壁面積（開口控除の有無で複数案）。棟長・出隅役物・水切も候補。</li>
<li><strong>進め方（ENGINE_SPEC共通）：</strong> 4棟の外壁原価と数量を同一ルールで抽出 → 相関分析 → 説明力のある最小モデル → <code>ENGINE_MAP.wall</code> へ登録。変数は欲張らず、固定費＋1数量から。</li>
<li><strong>状態：</strong> 未着手。村田含む4棟の立面図・建具表が検証データになる。</li>
</ul>
<hr />
<h2>Phase進捗</h2>
<ul>
<li><strong>Phase1（基礎）：完了</strong>（Ver0.4.0）</li>
<li><strong>Phase2（屋根）：完了・クローズ</strong>（Ver0.4.3）— ENGINE_MAP方式の実証、Engine Interface固定、Confidence導入、Variables/Engineの責任分離まで達成。</li>
<li><strong>Phase3（外壁）：次</strong>（calcWall）— 新しい仕組みは作らず、完成済みの仕組みにエンジンを1つ追加する作業。</li>
</ul></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-18</div></div></body></html>