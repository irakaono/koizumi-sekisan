# KKai 概算 適用ルール基盤（Applicability Layer）— Applicability Adapter / Rule Engine

> **状態（2026-07-28）：** **採用・実装・検証済み（第1世代）＋ Rule Engine 化（評価核の分離・今回）**。概算見積の「工種が付く／付かない」を、数量エンジンでも計算コアでもなく **Plan組立層** の責務として切り出した基盤。初適用＝ガレージハウスのシャッター工事。`gaisanCompute` / `tradeGenka` / `ENGINE_MAP` は**一切変更していない**。
>
> **更新（2026-07-28・Rule Engine 化・評価核の分離／設計主導・最小実装）：** 適用判定の評価を**純粋関数 `evaluateRule(rule, ctx)`** に切り出し、`tradeApplies()` はその**呼び出し側（薄いラッパ）**にした。責務チェーン `Canonical Trade → evaluateRule() → Applicability Projection → Plan → Quantity → Cost` を維持したまま、**Applicability Layer だけを一段抽象化**。第1世代の意味論（複数キー AND・キー内 includes・無条件は常時適用）は **不変・後方互換**（シャッター実例を含む17ケースで確認）。**今回の実装範囲は equals＋boolean/無条件のみ。** 比較演算子（`>=`,`>`,…）・明示 boolean 演算子（`and`/`or`/`not`）・`exclude`/`priority` は **Observation 据え置き（未実装）**。`gaisanCompute`/`tradeGenka`/`ENGINE_MAP` は無変更（設計上・コード反映時に機械確認）。詳細は §2・§5.1。
>
> **位置づけ：** これは「シャッター対応」という一機能ではなく、**概算見積全体の適用ルール基盤（Applicability Layer）の獲得**。KCP 全体の思想「**Evidence First / Engine 不変 / Rule 追加で機能拡張**」にそのまま一致する。以後、建物タイプ・設備・地域などの分岐は原則この層の宣言（`applies_when`）だけで表現し、コアは触らない。

## 1. なぜ Plan組立層に切り出したか（棄却案の記録）

適用判定をどこに置くかで3案を比較し、**第3案（Applicability Adapter）**を採用した。

- **A案（棄却）：** `ENGINE_MAP.shutter` が非該当時 `genka:0` を返す。→ コアは触らないが、**数量化(quantity_engine)と適用判定(applies_when)が混ざる**。「数量化するには ENGINE_MAP に関数を足す」という約束の意味が濁る。将来必ず効いてくるため棄却。
- **B案（棄却）：** `gaisanCompute` のトレード列を1行 `filter`。意味は素直だが「`gaisanCompute` 無変更」の約束を破る。
- **C案＝採用：Applicability Adapter。** 適用判定を独立レイヤーにし、**コアへ渡す直前に「今回の Plan に適用される工種だけ」を組み立てる**。コアも ENGINE_MAP も無変更、意味も混ざらない。

```
gaisan_basis.json（canonical：全工種）
      ↓  applies_when を evaluateRule() で評価（評価核＝純粋関数）
      ↓  tradeApplies()（呼び出し側の薄いラッパ）
      ↓  Plan組立層：今回のPlanに適用される工種だけを組み立てる（assemblePlan）
      ↓
既存 gaisanCompute / tradeGenka（無変更）
      ↓
結果画面（同じ適用結果を使うので、非該当工種はコスト・内訳とも自然に消える）
```

**責務境界（LOCK 相当の運用則）：** 適用判定は **Plan組立層のみ**が持つ。`quantity_engine`（数量化）にも計算コアにも適用判定を持ち込まない。canonical（全工種）は保持し、Plan は canonical からの射影。

## 2. 現行実装（Rule Engine 化後・評価核と呼び出し側）

宣言は `gaisan_basis.json` の各 trade に置く。評価は**純粋関数 `evaluateRule` 一本**、`tradeApplies` はそれを呼ぶだけ。

```json
{
  "no": 14,
  "name": "シャッター工事",
  "cost_per_tsubo": 13292,
  "applies_when": { "building_shape": ["ガレージハウス"], "shutter": ["手動", "電動"] },
  "evidence_status": "provisional"
}
```

- **`applies_when`（宣言型・第1世代スキーマ）：** キー＝context 変数、値＝許容値の配列。**複数キーは AND**、各キー内は **includes（equals の集合＝いずれか一致）**。条件なしの工種は常に適用。
- **評価核 `evaluateRule(rule, ctx)`（純粋関数・Rule Engine の心臓部）：**
  ```js
  // 副作用なし・throw しない・Geometry/Quantity/Material/Engine を参照しない。
  function evaluateRule(rule, ctx){
    if(rule == null)             return true;   // 無条件＝canonical は既定で Plan に載る
    if(typeof rule === 'boolean') return rule;  // 明示 true / false
    if(typeof rule !== 'object')  return true;  // 未知形は無条件扱い（安全側）
    const c = ctx || {};
    return Object.keys(rule).every(k => {
      const cond = rule[k];
      if(!Array.isArray(cond)) return true;      // 未実装(比較演算等)は課さない＝前方混入耐性
      return cond.includes(c[k]);                // equals（いずれか一致）
    });
  }
  ```
- **呼び出し側 `tradeApplies(t, ctx)`（薄いラッパ・API 不変）：**
  ```js
  function tradeApplies(t, ctx){ return evaluateRule(t.applies_when, ctx); }
  ```
- **Plan組立層（無変更・tradeApplies を呼ぶだけ）：**
  ```js
  let PLAN_ALL_TRADES = [];                               // canonical（全工種）を一度だけ保持
  function assemblePlan(){                                // コアへ渡す直前に射影
    const ctx = planContext();                            // { building_shape, shutter, ... }
    GAISAN_BASIS.trades = PLAN_ALL_TRADES.filter(t => tradeApplies(t, ctx));
  }
  ```
  `calcGaisan()` の先頭で `assemblePlan()` を呼ぶだけ。`gaisanCompute`/`tradeGenka` は無変更。

> **evaluateRule の契約（今回 LOCK 候補・純粋関数）：**
> ```
> evaluateRule(rule, context) -> boolean
>   ・全域性：どんな入力でも boolean を返す（未知形は「無条件＝適用」の安全側）。
>   ・純粋：副作用なし・context を変更しない・throw しない。
>   ・分離：Geometry / Quantity / Material / Engine を一切参照しない（import も held state も無し）。
>   ・唯一の責務：適用判定（trade が Plan に載るか）。数量化・原価・材料は知らない。
> ```

- **`evidence_status`：** `provisional`（Evidence 未確立）/ 将来 `verified` 等。金額・係数の格を示す。適用判定（evaluateRule）とは独立の軸。

## 3. 実証結果（実データ・今野基準 32坪）

| 建物形状 | シャッター | シャッター工事 | 工事原価（Σ cost_per_tsubo×坪） |
|---|---|---|---|
| 総二階 ほか | — | 除外 | 26,673,152 |
| ガレージハウス | なし | 除外 | 26,673,152 |
| ガレージハウス | 手動 / 電動 | 計上 | 27,098,496（+425,344） |

- **ガレージハウスを選んだだけでは加算しない**（`shutter` が `手動/電動` のときのみ）。仕様一致。
- 非該当時は Plan に入らないため、**コストも内訳表示も自動で除外**（¥0 行の小細工不要）。
- コア無変更（`gaisanCompute` / `tradeGenka` 原本一致・`ENGINE_MAP` にシャッターキー無し）。
- **Rule Engine 化の後方互換：** 上表の適用結果は `evaluateRule` 切り出し後も不変。第1世代スキーマ（複数キー AND・キー内 includes・無条件常時適用）の意味論を保存していることを **17ケースの単体テスト**で確認（無条件／boolean／シャッター AND・includes・context 欠落／単一キー／前方混入耐性／context 非破壊）。

## 4. 一般化（同じ層に載る将来の分岐）

建物タイプ・設備・地域は、コード改変なしに宣言追加だけで増える（**第1世代スキーマの範囲内**＝equals 集合）：

```json
{ "trade": "太陽光工事",   "applies_when": { "solar": ["あり"] } }
{ "trade": "防火サッシ",   "applies_when": { "region": ["準防火地域","防火地域"] } }
{ "trade": "耐雪仕様",     "applies_when": { "snow_region": ["あり"], "roof_shape": ["切妻"] } }
```

想定属性：ガレージハウス／二世帯住宅／店舗併用住宅／長期優良住宅／GX志向型住宅／ZEH／太陽光／蓄電池／全館空調 …。すべて `applies_when`（equals 集合）で表現。**比較演算が要る分岐（床面積 ≥ 40 等）は §5.1 の Observation 側**で、実装されるまで JSON に書かない。

## 5. Observations（将来候補・実装済との境界を明確化）

Architecture Freeze / Evidence First に従う。**今回実装したのは §5.1 の「評価核の分離」まで。** それ以外は**記録のみ（未実装）**。

### 5.1 Rule Engine（評価核の分離＝今回実装／比較演算は Observation 据え置き）

第1世代は「配列 includes（equals 集合）」のみ。今回、評価を **`evaluateRule(rule, ctx)` に集約**し、`tradeApplies()` は `return evaluateRule(t.applies_when, ctx)` を呼ぶだけにした（§2）。これで **Rule Engine の骨格が成立**し、概算見積に限らず **数量エンジン／製品選定／補助金判定／見積テンプレート／確認申請チェック** まで、同じ純粋関数を共通利用できる素地ができた。

**実装済 / Observation の境界（この表が正典）：**

| rule 形 | 例 | 状態 |
|---|---|---|
| 無条件（rule なし） | `applies_when` 省略 | ✅ 実装（常時適用） |
| boolean リテラル | `true` / `false` | ✅ 実装 |
| equals 集合（第1世代） | `{ "shutter": ["手動","電動"] }` | ✅ 実装（複数キー AND・キー内 includes） |
| 比較演算子 | `{ "floor_area": { ">=": 40 } }` | ⏸ Observation（**未実装・JSON に書かない**） |
| 明示 boolean 演算子 | `{ "and":[…] }` `{ "or":[…] }` `{ "not":… }` | ⏸ Observation（未実装） |
| exclude / priority | §5.2 リッチ構造 | ⏸ Observation（未実装） |

将来 比較演算が欲しくなったら（`{ "floor_area": { ">=": 40 } }` / `{ "garage_count": { ">": 1 } }`）、**`evaluateRule` の内側に演算子ディスパッチを1段足すだけ**で済む（`tradeApplies`・`assemblePlan`・JSON スキーマの呼び出し形は不変）。

> **前方混入耐性（設計判断）：** 未実装形（配列でない条件＝比較演算子やネスト boolean）は、`evaluateRule` が**「その条件を課さない（無条件）」とみなして無視**する（安全側）。これは「実装前に experimental な applies_when が混入しても第1世代評価を壊さない」ための頑健性であって、**運用上は比較演算子を含む applies_when を `gaisan_basis.json` に書かない**（実装されるまで Observation）。演算子を実装する時点で、この分岐は「無視」から「評価」に変わる。

### 5.2 リッチ構造 `applicability:{}` の候補（未実装）

`applies_when` の名前は当面据え置き。ただし将来 **優先順位・除外条件・説明文・根拠** を持たせたくなる可能性が高いので、次の構造を**候補として記録**する（採用ではない）：
```json
{
  "applicability": {
    "when":   { ... },          // ＝現行 applies_when
    "status": "provisional",    // ＝現行 evidence_status
    "priority": 0,
    "exclude": { ... },
    "note": "…",
    "evidence": "…"
  }
}
```
**判断：今は変更しない。** 現行 `applies_when` + `evidence_status` で十分。この構造は、除外条件や優先順位が実際に必要になった時点で（Evidence が出てから）判断する。

### 5.3 Applicability は Topology と同じ「Projection」（横断 Observation・未昇格）

今回の整理で見えた構造：

```
Canonical Trade
      │
      ▼  Applicability Projection（evaluateRule で評価）
Plan  ──▶  Quantity  ──▶  Cost
```

**Canonical** には `シャッター工事` が**存在する**。しかし **Plan** では `applies_when` によって「存在する／しない」が決まる。これは Graph Runtime の `Canonical Graph → Projection` と**同型**であり、すなわち **Applicability も Projection の一種**。式で書けば：

```
Plan = Canonical × Applicability Projection
```

例（GX住宅）：Canonical は `太陽光 / 蓄電池 / HEMS` を全部持つ。**普通住宅では Projection されず、GX住宅では Projection される。**

**含意（将来・未検証）：** これが実証されれば、`Geometry Runtime`／`Graph Runtime`／`Applicability Runtime` がすべて **`Canonical → Projection → Runtime`** という共通パターンで説明できる可能性がある。**Gutter 側の Drainage Projection（`GUTTER_RUNTIME_VALIDATION §4.5`：Downspout Node は Geometry ではなく Drainage Projection）は、この横断 Observation の兄弟**——排水も適用も「Canonical を Projection して Runtime を得る」同じ骨格。KKai の既存 Observation 群（「Geometry is the canonical model from which all quantity projections are derived」「UI is a projection of runtime state」）と同じ系列。

> **ただし昇格しない。** Evidence はシャッター1件のみ。「Runtime と同じ概念」と言い切る証拠は無い。ここでは **「Graph Runtime の Projection と非常によく似た構造を持つ」という観察として残すだけ**にとどめ、一般化（共通パターンへの統合）は行わない。この“記録だけ”という現方針がちょうど良い。

## 6. Evidence 未確立（provisional のまま据え置き）

以下は 4棟に実績が無く（n=0）、**でっち上げない（Rule 3）**。Evidence が付いてから確定：
- シャッター工事の金額（現状は坪単価由来の暫定値）。
- 手動／電動の金額差。
- 幅・高さ・台数による数量化、ガレージ面積との連動。
- ガレージハウスの形状係数（`ensho_to_A`/`P_shape_factor` は総二階と同値の暫定）。

## 7. KCP 思想との整合

`Evidence First`（未確立は provisional・据え置き／比較演算子は実装まで Observation）／`Engine 不変`（gaisanCompute・tradeGenka・ENGINE_MAP 無変更）／`Rule 追加で機能拡張`（宣言を足すだけ）。**適用ルールを「工種の数」でなく「宣言の数」で増やす**という、UI 側 Observation「Variable が増えるのではなく必要な Variable だけ開く」の工種版。Rule Engine 化はこれを一段進め、**「宣言の数」で増やす評価を1つの純粋関数に集約**した（呼び出し側・JSON スキーマ・コアはすべて不変）。

## 関連
- `GAISAN_UI_PRINCIPLES.md`（UI 層。シャッター＝optional の初期表示スコープ。本層はその原価側の実装基盤）
- `WALL_QUANTITY_EXTRACTION.md` / `GUTTER_RUNTIME_VALIDATION.md`（Canonical → Projection 系列。§5.3 の横断 Observation はこの系列の兄弟。**Gutter の Drainage Projection と Applicability Projection は同じ `Canonical → Projection → Runtime` 骨格**）
- 実装：`index.html`（`evaluateRule`（評価核・純粋関数）／`tradeApplies`（呼び出し側ラッパ）／`assemblePlan` / `PLAN_ALL_TRADES`・`calcGaisan` 先頭で `assemblePlan()`）／`housing/gaisan_basis.json`（`applies_when`＝第1世代スキーマ）。evaluateRule＋tradeApplies は index.html に統合済み（17ケースの単体テストで第1世代後方互換を確認）。
