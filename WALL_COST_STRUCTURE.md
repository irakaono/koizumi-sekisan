# KKai エンジン設計原則（Engine Principles）

> **ENGINE_PRINCIPLES v1.0（LOCKED / 2026-07-19）** — KKai の設計思想（憲法級）。工種に依存せず「Engine はどう考えるか」を定める。個別工種で得た Evidence（例：外壁）は各工種の構造文書に置き、本書には持ち込まない。**以後は原則を増やさず、各工種の Evidence で実証する。** 変更は説明の明確化（Documentation Correction）に限り、思想（第一原理・Rule 1〜3・層構造）の意味変更は v2.0 として別途合意する。原則の寿命は工種の Evidence より長い——KKai が続く限り変わらない層。

## 設計書の階層

```
CONSTITUTION            なぜ KKai を作るか（利益を守る概算 / Evidence First / Scope First）
   ↓
ENGINE_PRINCIPLES      Engine はどう考えるか  ← 本書
   ↓
ENGINE_SPEC (v1.0)     Engine は何を返すか（EngineResult 契約・LOCKED）
   ↓
VARIABLE_DEFINITIONS   何を事実として保持するか（Variables 契約）
   ↓
<工種>_STRUCTURE       その工種で原則がどう Evidence になったか（例：WALL_COST_STRUCTURE）
   ↓
calcXxx                実装（Engine）
```

各層の責務：CONSTITUTION＝「なぜ作るか」／ENGINE_PRINCIPLES＝「どう考えるか」／ENGINE_SPEC＝「何を返すか」／VARIABLE_DEFINITIONS＝「何を事実として保持するか」／構造文書＝「ある工種で思想がどう実証されたか」。

## 実行時アーキテクチャの層（責務分界・層構造の正典）

```
Variables → Engine → Trade → UI
```

- **Variables**：図面／プランから得た数量・属性（延床・形状・基礎面積A・軒先長…）。自動推定・実測・将来は KCP 由来。**KCP はここまで責任を持つ。**
- **Engine**：数量を工種原価へ変換し EngineResult を返す。**KKai はここから下に責任を持つ。**
- **Trade**：工種（`gaisan_basis.json` の trades）。
- **UI**：概算画面・見積書。Engine の実装を知らない（疎結合）。

紛らわしい2語を、ここで**一度だけ**定義する（他文書では再定義しない）：

- **Category（集計区分：仮設/躯体/外装/設備/仕上）** は UI 側の**表示グルーピング**であって、設計層ではない。
- **施工系統（Rule 2）** は Engine 内部概念であって、この層には現れない。Variable にも Trade にもしない。

> **この層構造の定義は本書だけが正典。** ENGINE_SPEC・VARIABLE_DEFINITIONS は本書を参照する（同期対象を1か所に固定する）。

## 第一原理

> **Engine は工種をモデル化するのではない。施工をモデル化する。**

KKai は「◯◯工事」という名前を数式化するのではなく、**実際の施工がどの数量に支配されているか**をモデル化する。出発点は工種名ではなく施工原理（Evidence First）。この一文は KKai だけでなく、KCP・Recognizer・Estimator・将来の積算AIエージェントすべてに通用する。

## Rule 1 — EngineResult 契約（Engine は「何を返すか」）

ENGINE_SPEC v1.0 の要約。Engine は工種と ctx を受け取り、**必ず** `{ genka, qty, basis, used, fallback, confidence }` を返す。数量が無くても必ず値を出す（坪単価フォールバック）。**契約は LOCKED、内部実装は自由。**

## Rule 2 — Trade ≠ Driver（Engine は「中で何を選ぶか」）

> **工種（Trade）と Engine のドライバー粒度は一致を前提にしない。Engine は工種を施工系統へ分解し、施工系統ごとに一次ドライバーを選択する。**

- **施工系統**＝施工方法が同じひとまとまり。施工方法が違えば数量ドライバーも違う。「カテゴリ（分類）」ではなく「施工系統（因果）」と呼ぶ。
- **施工系統は Engine 内部でのみ存在する概念であり、Variable でも Trade でもない。Variable として保存しない**（JSON に `construction_group` 等を作らない）。分解は Engine が計算時に行い、外に持ち出さない。
- 「1工種＝1ドライバー」は、施工系統が1つだった特殊ケース（基礎・屋根）にすぎない。
- この原則は内装・給排水・電気・外構など**多系統の工種すべて**に効く。
- Rule 1 が「何を返すか」なら、Rule 2 は「中で何を選ぶか」。両者は独立し、どちらも侵さない。

> **系の原則：施工系統ごとに一次ドライバーは存在するが、Trade 全体に一次ドライバーが存在するとは限らない。** 基礎・屋根は Trade に一次ドライバーが1つ存在した特殊ケース、外壁はそれが存在しない一般ケース。これ一文で基礎・屋根・外壁・将来の設備まで説明できる。

## Rule 3 — Variables are never invented（Engine は Variable を生成しない）

> **Engine は Variable を生成しない。Variable は Evidence（図面・実測・KCP）から取得する。Engine は Variable を採用するだけ。**

- 数量・属性を生み出す責任は上流（Recognizer／実測／KCP）と `VARIABLE_DEFINITIONS.md` にある。Engine は取得済みの事実を**選択し合成する**だけで、無い数量をでっち上げない。
- 未取得の Variable があれば、推定でも捏造でもなく**フォールバック**（坪単価等）で必ず値を出す（Rule 1）。
- これにより Evidence First を実装レベルで担保する。Rule 2（何を選ぶか）と対で、「Engine は事実を**選ぶ**が、事実を**作らない**」を固定する。

## ドライバー階層（用語の固定）

「支配変数」「採用変数」などの混在表現は使わない。次の3階層で統一する。

- **一次ドライバー**：その施工系統の原価を主に決める数量。
- **二次ドライバー**：一次を修飾する要因（グレード等）。
- **補正**：特殊納まり等の個別要因。

根拠の順序は **施工原理が先、統計は裏付け**。KKai は統計モデルではなく**建築数量モデル**なので、n が小さい段階では相関係数より「施工方法から見てこの数量以外で説明できない」の方が強い Evidence になる。

## Engine 設計プロセス（全工種共通）

```
        Trade（工種）
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
```

基礎・屋根は①で施工系統が1つだった特殊ケース。設備・内装でもこの手順をなぞるだけになる。

## Engine Type（ドライバー構造による分類）

「成熟度」や優劣ではなく、**ドライバー構造の型**。外壁（Type B）が基礎（Type A）より上位という意味ではない。工種ごとに適切な型を選ぶ。

| Type | 名称 | 例 | Engine の作り |
|---|---|---|---|
| Type A | Single Driver（単一ドライバーで説明できる） | 基礎（コンクリート量）／屋根（軒先長） | `F + a×Driver` |
| Type B | Composite Driver（複数ドライバー） | 外壁（面材／軒裏／役物／シーリング） | 内部で施工系統別に計算し**合成** |
| Type C | Hierarchical Composition（施工系統の階層合成） | 設備・内装 など多系統 | 施工系統を階層的に合成 |

> **Type A の注意：** Type A も式は `F + a×Driver`＝**固定費（F）＋変動費（a×Driver）の2項構造**。「Driver が1つ」であって「項が1つ」ではない。Type A ＝ **単一 Driver で説明できる Engine** の意。

**原則：Engine は複数の「項」を持つのではなく、内部で施工系統ごとに原価を計算し、その和を EngineResult として返す。** ENGINE_SPEC v1.0 の契約は一切変わらない。

## より広い位置づけ（積算AIの設計原理）

本原則は KKai の Engine 層に閉じない。積算 AI 全体のパイプラインに一般化できる。

```
図面認識(Recognizer) → Variable抽出 → 施工系統へ分解 → Driver決定 → Engine(Estimator) → Estimate
```

同じ骨格が KCP・Recognizer・Estimator・積算 OS 全体に流用できる。

## 各工種での実証

本原則が実際に成立したことは、各工種の構造文書で Evidence として示す。**最初の実証例は外壁**（→ `WALL_COST_STRUCTURE.md`）：単一ドライバーで説明できない初の工種で、Rule 2（Trade ≠ Driver）が成立した。
