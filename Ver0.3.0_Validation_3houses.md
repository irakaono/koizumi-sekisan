<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>数量エンジン仕様（Engine Interface）</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
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
<body><div class="hero"><div class="brand">KKai ｜ ENGINE SPEC v1.0 (LOCKED)</div><h1>数量エンジン仕様（Engine Interface）</h1></div>
<div class="wrap"><div class="content"><h1>KKai 数量エンジン仕様（Engine Interface）</h1>
<blockquote>
<p><strong>ENGINE_SPEC v1.0（LOCKED / 2026-07-18）</strong> — 本仕様は契約として凍結。今後追加する全エンジンはこの契約に従う。変更は後方互換を原則とし、破壊的変更は v2.0 として別途扱う（フィールド追加＝minor、意味変更＝major）。</p>
</blockquote>
<p><strong>目的：</strong> すべての数量エンジン（calcKiso／calcRoof／calcWall …）が従う共通の入出力契約を1枚に固定する。これを先に決めることで、エンジン追加時に迷わず、コアロジック（<code>tradeGenka</code>／<code>gaisanCompute</code>）を一切触らずに拡張できる。対応実装：Ver0.4.3（ENGINE_MAP方式・kiso／roof）。契約バージョン：<strong>v1.0（LOCKED）</strong>。</p>
<h2>位置づけ</h2>
<p>本仕様は <strong>Engine が「何を返すか」（EngineResult 契約）のみ</strong>を定める。<strong>アーキテクチャの層構造（<code>Variables → Engine → Trade → UI</code>）と設計思想は <code>ENGINE_PRINCIPLES.md</code> を正典とする</strong>（責務分離：層構造の定義は1か所に固定）。責任分界だけ再掲すると、KCP は Variables まで、KKai は Engine から下（EngineResult）に責任を持つ。</p>
<blockquote>
<p>注：本節の層図を ENGINE_PRINCIPLES へ移設したのは <strong>Documentation Correction</strong>（説明図の集約）であり、EngineResult 契約のフィールドには一切触れていない。v1.0 の LOCK は保たれる。</p>
</blockquote>
<h2>登録方法（2ステップ・コアの if は増やさない）</h2>
<ol>
<li><strong>JSON</strong>：対象工種に <code>"quantity_engine":"roof"</code> を追加。</li>
<li><strong>JS</strong>：<code>calcRoof</code> を実装し <code>ENGINE_MAP</code> に登録。</li>
</ol>
<h2>エンジン契約（インターフェース）</h2>
<h3>シグネチャ</h3>
<pre><code class="language-js">ENGINE_MAP[name] = function(trade, ctx) =&gt; EngineResult
</code></pre>
<h3>入力</h3>
<table>
<thead>
<tr>
<th>引数</th>
<th>内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>trade</code></td>
<td>工種オブジェクト（no, name, category, cost_per_tsubo, quantity_engine …）</td>
</tr>
<tr>
<td><code>ctx</code></td>
<td>概算コンテキスト：<code>ensho_tsubo</code>（延床坪）、<code>shape</code>（建物形状）、<code>settings</code>（諸経費率・目標粗利・安全係数）、<code>variables</code>（A, P, 屋根面積, 軒先長 … 取得不能はnull）</td>
</tr>
</tbody>
</table>
<h3>出力 EngineResult</h3>
<table>
<thead>
<tr>
<th>フィールド</th>
<th>型</th>
<th>意味</th>
<th>現状</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>genka</code></td>
<td>number</td>
<td>工種の概算原価（円）</td>
<td>実装済</td>
</tr>
<tr>
<td><code>qty</code></td>
<td>bool</td>
<td>数量が実際に効いたか（「数量」バッジ表示）</td>
<td>実装済</td>
</tr>
<tr>
<td><code>basis</code></td>
<td>string</td>
<td>根拠（使用した式・モデル名）</td>
<td>実装済(Ver0.4.3)</td>
</tr>
<tr>
<td><code>used</code></td>
<td>object</td>
<td>使用した変数と値（例 <code>{A:62.3}</code> <code>{eave_length:18.8}</code>）</td>
<td>実装済(Ver0.4.3)</td>
</tr>
<tr>
<td><code>fallback</code></td>
<td>bool</td>
<td>坪単価にフォールバックしたか</td>
<td>実装済(Ver0.4.3)</td>
</tr>
<tr>
<td><code>confidence</code></td>
<td>number(0–1)</td>
<td>この工種原価をどれだけ信用してよいか（KCPの<code>score</code>に相当）</td>
<td>実装済(Ver0.4.3)</td>
</tr>
</tbody>
</table>
<p><code>genka</code> 以外が無くてもコアは動く。KCPの Result Envelope <code>{value, score, reason, status}</code> と整合する（genka=value、confidence=score、basis=reason、fallback/qty=status系）。</p>
<h3>変数選択の自由（LOCKED）</h3>
<p>Engine は Variables のうち<strong>利用する変数を自由に選べる</strong>。<code>Variables</code>＝取得できた事実、<code>Engine</code>＝現時点で採用する式。取得したが使わない変数があってよい（Evidence First）。採用変数はデータ量で見直す前提で、<code>variables</code> には取得した全数量を残す。</p>
<h3>フォールバック規約（LOCKED）</h3>
<ul>
<li><code>quantity_engine</code> が無い／<code>ENGINE_MAP</code> に未登録 → <strong>坪単価</strong> <code>cost_per_tsubo × 延床</code>。</li>
<li>必要な変数（数量）が未取得 → <strong>坪単価にフォールバック</strong>（<code>fallback=true</code>）。</li>
<li><strong>「数量が無くても必ず動く」ことを全エンジンが保証する</strong>（プラン初期でも壊れない）。積算システムは「数量が足りません」で止まりがちだが、KKaiは必ず見積りを出す。これはKKaiの強み。</li>
</ul>
<h2>全体信頼度（Confidence）</h2>
<p>各エンジンは <code>confidence</code>（0–1）を返す。数量の質で決まる社内向けの指標で、<strong>顧客提示用ではなく「どこを実測に置き換えると精度が上がるか」を判断する材料</strong>。</p>
<p><strong>目安：</strong></p>
<table>
<thead>
<tr>
<th>原価の出どころ</th>
<th>confidence 目安</th>
</tr>
</thead>
<tbody>
<tr>
<td>実測数量 × 数量モデル</td>
<td>0.90〜0.95</td>
</tr>
<tr>
<td>自動推定数量 × 数量モデル</td>
<td>0.78〜0.88</td>
</tr>
<tr>
<td>坪単価フォールバック（数量なし）</td>
<td>0.55〜0.65</td>
</tr>
</tbody>
</table>
<p><strong>全体信頼度</strong> ＝ 各工種 <code>confidence</code> を原価で加重平均。例：基礎0.95／屋根0.82／外壁0.74 … → 見積全体「Confidence 87%」。低い工種＝実測に置き換える優先度が高い工種、と一目で分かる。原価加重なので、金額影響の大きい工種を優先して確認できる。</p>
<h2>実装例</h2>
<h3>calcKiso（実装済・基礎）</h3>
<ul>
<li>変数：A（基礎面積㎡）。延床×形状比で自動推定、実測で上書き可。</li>
<li>式：<code>genka = F + a×A</code>（F=1,366,743／a=2,897・n=4暫定）。</li>
<li>A未取得 → 坪単価フォールバック。</li>
<li>戻り：<code>{ genka, qty, basis, used, fallback, confidence }</code>。</li>
</ul>
<h3>calcRoof（実装済・Ver0.4.3）</h3>
<ul>
<li><strong>樋・屋根工事は広い工種（RoofEnvelope：屋根材＋樋＋軒先換気＋雪止＋破風＋水切＋役物）</strong>。相関は工種構成に依存する点に注意。</li>
<li>変数：<code>roof_area</code>／<code>eave_length</code>／<code>ridge_length</code>／<code>gable_length</code> を<strong>すべて取得・保持</strong>。</li>
<li>採用式：<code>genka = F + a×eave_length</code>（F=212,823／a=50,478・n=4暫定）。4棟で軒先長が最も説明力が高い（単相関0.98＞屋根面積0.87）。屋根面積・棟・ケラバは保持のみ（現モデル未使用）。</li>
<li><strong>再評価条件：~20棟集まった時点で屋根面積・軒先長・複合モデルを再比較</strong>（棟形状の多様性が増えると相関が変わりうるため）。</li>
<li>eave未取得 → 坪単価フォールバック。戻り：<code>{ genka, qty, basis, used, fallback, confidence }</code>。</li>
</ul>
<h2>Phase の進め方（各工種共通）</h2>
<ol>
<li>4棟（今野・安原・小峰・村田）の当該工種の原価と数量を同一ルールで抽出。</li>
<li>数量と原価の相関分析（単相関→最小二乗）。過学習を避け、係数が物理的に妥当かを確認。</li>
<li>説明力のある最小モデル（固定費＋1数量程度）を採用。変数は欲張らない。</li>
<li><code>calcXxx</code> を実装し <code>ENGINE_MAP</code> へ登録＋JSONに <code>quantity_engine</code>。</li>
</ol>
<h2>バージョン・ガバナンス（v1.0 LOCKED）</h2>
<ul>
<li>本契約は <strong>v1.0 として凍結（LOCKED）</strong>。Ver0.5・Ver1.0 と進んでエンジンは増えても、<strong>契約は変えない</strong>のが原則。</li>
<li>EngineResult のフィールド追加は後方互換（minor）。破壊的変更（既存フィールドの意味変更・削除）は <strong>v2.0</strong> として別途合意のうえ行う。</li>
<li>まず契約を固定し、実装は後から揃える（Scope First）。これにより、KKaiは「エンジンは増えるが契約は不変」という強い基盤になる。</li>
</ul></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-19</div></div></body></html>