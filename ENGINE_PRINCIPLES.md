<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>エンジン設計原則（Engine Principles）</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
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
<body><div class="hero"><div class="brand">KKai ｜ ENGINE PRINCIPLES v1.0 (LOCKED)</div><h1>エンジン設計原則（Engine Principles）</h1></div>
<div class="wrap"><div class="content"><h1>KKai エンジン設計原則（Engine Principles）</h1>
<blockquote>
<p><strong>ENGINE_PRINCIPLES v1.0（LOCKED / 2026-07-19）</strong> — KKai の設計思想（憲法級）。工種に依存せず「Engine はどう考えるか」を定める。個別工種で得た Evidence（例：外壁）は各工種の構造文書に置き、本書には持ち込まない。<strong>以後は原則を増やさず、各工種の Evidence で実証する。</strong> 変更は説明の明確化（Documentation Correction）に限り、思想（第一原理・Rule 1〜3・層構造）の意味変更は v2.0 として別途合意する。原則の寿命は工種の Evidence より長い——KKai が続く限り変わらない層。</p>
</blockquote>
<h2>設計書の階層</h2>
<pre><code>CONSTITUTION            なぜ KKai を作るか（利益を守る概算 / Evidence First / Scope First）
   ↓
ENGINE_PRINCIPLES      Engine はどう考えるか  ← 本書
   ↓
ENGINE_SPEC (v1.0)     Engine は何を返すか（EngineResult 契約・LOCKED）
   ↓
VARIABLE_DEFINITIONS   何を事実として保持するか（Variables 契約）
   ↓
&lt;工種&gt;_STRUCTURE       その工種で原則がどう Evidence になったか（例：WALL_COST_STRUCTURE）
   ↓
calcXxx                実装（Engine）
</code></pre>
<p>各層の責務：CONSTITUTION＝「なぜ作るか」／ENGINE_PRINCIPLES＝「どう考えるか」／ENGINE_SPEC＝「何を返すか」／VARIABLE_DEFINITIONS＝「何を事実として保持するか」／構造文書＝「ある工種で思想がどう実証されたか」。</p>
<h2>実行時アーキテクチャの層（責務分界・層構造の正典）</h2>
<pre><code>Variables → Engine → Trade → UI
</code></pre>
<ul>
<li><strong>Variables</strong>：図面／プランから得た数量・属性（延床・形状・基礎面積A・軒先長…）。自動推定・実測・将来は KCP 由来。<strong>KCP はここまで責任を持つ。</strong></li>
<li><strong>Engine</strong>：数量を工種原価へ変換し EngineResult を返す。<strong>KKai はここから下に責任を持つ。</strong></li>
<li><strong>Trade</strong>：工種（<code>gaisan_basis.json</code> の trades）。</li>
<li><strong>UI</strong>：概算画面・見積書。Engine の実装を知らない（疎結合）。</li>
</ul>
<p>紛らわしい2語を、ここで<strong>一度だけ</strong>定義する（他文書では再定義しない）：</p>
<ul>
<li><strong>Category（集計区分：仮設/躯体/外装/設備/仕上）</strong> は UI 側の<strong>表示グルーピング</strong>であって、設計層ではない。</li>
<li><strong>施工系統（Rule 2）</strong> は Engine 内部概念であって、この層には現れない。Variable にも Trade にもしない。</li>
</ul>
<blockquote>
<p><strong>この層構造の定義は本書だけが正典。</strong> ENGINE_SPEC・VARIABLE_DEFINITIONS は本書を参照する（同期対象を1か所に固定する）。</p>
</blockquote>
<h2>第一原理</h2>
<blockquote>
<p><strong>Engine は工種をモデル化するのではない。施工をモデル化する。</strong></p>
</blockquote>
<p>KKai は「◯◯工事」という名前を数式化するのではなく、<strong>実際の施工がどの数量に支配されているか</strong>をモデル化する。出発点は工種名ではなく施工原理（Evidence First）。この一文は KKai だけでなく、KCP・Recognizer・Estimator・将来の積算AIエージェントすべてに通用する。</p>
<h2>Rule 1 — EngineResult 契約（Engine は「何を返すか」）</h2>
<p>ENGINE_SPEC v1.0 の要約。Engine は工種と ctx を受け取り、<strong>必ず</strong> <code>{ genka, qty, basis, used, fallback, confidence }</code> を返す。数量が無くても必ず値を出す（坪単価フォールバック）。<strong>契約は LOCKED、内部実装は自由。</strong></p>
<h2>Rule 2 — Trade ≠ Driver（Engine は「中で何を選ぶか」）</h2>
<blockquote>
<p><strong>工種（Trade）と Engine のドライバー粒度は一致を前提にしない。Engine は工種を施工系統へ分解し、施工系統ごとに一次ドライバーを選択する。</strong></p>
</blockquote>
<ul>
<li><strong>施工系統</strong>＝施工方法が同じひとまとまり。施工方法が違えば数量ドライバーも違う。「カテゴリ（分類）」ではなく「施工系統（因果）」と呼ぶ。</li>
<li><strong>施工系統は Engine 内部でのみ存在する概念であり、Variable でも Trade でもない。Variable として保存しない</strong>（JSON に <code>construction_group</code> 等を作らない）。分解は Engine が計算時に行い、外に持ち出さない。</li>
<li>「1工種＝1ドライバー」は、施工系統が1つだった特殊ケース（基礎・屋根）にすぎない。</li>
<li>この原則は内装・給排水・電気・外構など<strong>多系統の工種すべて</strong>に効く。</li>
<li>Rule 1 が「何を返すか」なら、Rule 2 は「中で何を選ぶか」。両者は独立し、どちらも侵さない。</li>
</ul>
<blockquote>
<p><strong>系の原則：施工系統ごとに一次ドライバーは存在するが、Trade 全体に一次ドライバーが存在するとは限らない。</strong> 基礎・屋根は Trade に一次ドライバーが1つ存在した特殊ケース、外壁はそれが存在しない一般ケース。これ一文で基礎・屋根・外壁・将来の設備まで説明できる。</p>
</blockquote>
<h2>Rule 3 — Variables are never invented（Engine は Variable を生成しない）</h2>
<blockquote>
<p><strong>Engine は Variable を生成しない。Variable は Evidence（図面・実測・KCP）から取得する。Engine は Variable を採用するだけ。</strong></p>
</blockquote>
<ul>
<li>数量・属性を生み出す責任は上流（Recognizer／実測／KCP）と <code>VARIABLE_DEFINITIONS.md</code> にある。Engine は取得済みの事実を<strong>選択し合成する</strong>だけで、無い数量をでっち上げない。</li>
<li>未取得の Variable があれば、推定でも捏造でもなく<strong>フォールバック</strong>（坪単価等）で必ず値を出す（Rule 1）。</li>
<li>これにより Evidence First を実装レベルで担保する。Rule 2（何を選ぶか）と対で、「Engine は事実を<strong>選ぶ</strong>が、事実を<strong>作らない</strong>」を固定する。</li>
</ul>
<h2>ドライバー階層（用語の固定）</h2>
<p>「支配変数」「採用変数」などの混在表現は使わない。次の3階層で統一する。</p>
<ul>
<li><strong>一次ドライバー</strong>：その施工系統の原価を主に決める数量。</li>
<li><strong>二次ドライバー</strong>：一次を修飾する要因（グレード等）。</li>
<li><strong>補正</strong>：特殊納まり等の個別要因。</li>
</ul>
<p>根拠の順序は <strong>施工原理が先、統計は裏付け</strong>。KKai は統計モデルではなく<strong>建築数量モデル</strong>なので、n が小さい段階では相関係数より「施工方法から見てこの数量以外で説明できない」の方が強い Evidence になる。</p>
<h2>Engine 設計プロセス（全工種共通）</h2>
<pre><code>        Trade（工種）
            │
            ▼   ① 施工系統へ分解
   施工系統 A ／ B ／ C …
            │
            ▼   ② 各施工系統の一次ドライバーを決定（施工原理が先・統計は裏付け）
   Driver（一次）＋ 二次 ＋ 補正
            │
            ▼   ③ Evidence 取得（数量と原価を同一ルールで）
            │
            ▼   ④ 各施工系統を単体で較正（棟数を足す）
            │
            ▼   ⑤ Engine 内部で合成（Σ 施工系統）
            │
            ▼
   EngineResult { genka, qty, basis, used, fallback, confidence }
</code></pre>
<p>基礎・屋根は①で施工系統が1つだった特殊ケース。設備・内装でもこの手順をなぞるだけになる。</p>
<h2>Engine Type（ドライバー構造による分類）</h2>
<p>「成熟度」や優劣ではなく、<strong>ドライバー構造の型</strong>。外壁（Type B）が基礎（Type A）より上位という意味ではない。工種ごとに適切な型を選ぶ。</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>名称</th>
<th>例</th>
<th>Engine の作り</th>
</tr>
</thead>
<tbody>
<tr>
<td>Type A</td>
<td>Single Driver（単一ドライバーで説明できる）</td>
<td>基礎（コンクリート量）／屋根（軒先長）</td>
<td><code>F + a×Driver</code></td>
</tr>
<tr>
<td>Type B</td>
<td>Composite Driver（複数ドライバー）</td>
<td>外壁（面材／軒裏／役物／シーリング）</td>
<td>内部で施工系統別に計算し<strong>合成</strong></td>
</tr>
<tr>
<td>Type C</td>
<td>Hierarchical Composition（施工系統の階層合成）</td>
<td>設備・内装 など多系統</td>
<td>施工系統を階層的に合成</td>
</tr>
</tbody>
</table>
<blockquote>
<p><strong>Type A の注意：</strong> Type A も式は <code>F + a×Driver</code>＝<strong>固定費（F）＋変動費（a×Driver）の2項構造</strong>。「Driver が1つ」であって「項が1つ」ではない。Type A ＝ <strong>単一 Driver で説明できる Engine</strong> の意。</p>
</blockquote>
<p><strong>原則：Engine は複数の「項」を持つのではなく、内部で施工系統ごとに原価を計算し、その和を EngineResult として返す。</strong> ENGINE_SPEC v1.0 の契約は一切変わらない。</p>
<h2>より広い位置づけ（積算AIの設計原理）</h2>
<p>本原則は KKai の Engine 層に閉じない。積算 AI 全体のパイプラインに一般化できる。</p>
<pre><code>図面認識(Recognizer) → Variable抽出 → 施工系統へ分解 → Driver決定 → Engine(Estimator) → Estimate
</code></pre>
<p>同じ骨格が KCP・Recognizer・Estimator・積算 OS 全体に流用できる。</p>
<h2>各工種での実証</h2>
<p>本原則が実際に成立したことは、各工種の構造文書で Evidence として示す。<strong>最初の実証例は外壁</strong>（→ <code>WALL_COST_STRUCTURE.md</code>）：単一ドライバーで説明できない初の工種で、Rule 2（Trade ≠ Driver）が成立した。</p></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-19</div></div></body></html>