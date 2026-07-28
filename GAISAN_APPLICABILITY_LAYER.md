# KKai 概算 適用ルール基盤（Applicability Layer）— Applicability Adapter

> **状態（2026-07-28）：** **採用・実装・検証済み（第1世代）**。概算見積の「工種が付く／付かない」を、数量エンジンでも計算コアでもなく **Plan組立層** の責務として切り出した基盤。初適用＝ガレージハウスのシャッター工事。`gaisanCompute` / `tradeGenka` / `ENGINE_MAP` は**一切変更していない**（原本とバイト一致を機械確認）。
>
> **位置づけ：** これは「シャッター対応」という一機能ではなく、**概算見積全体の適用ルール基盤（Applicability Layer）の獲得**。KCP 全体の思想「**Evidence First / Engine 不変 / Rule 追加で機能拡張**」にそのまま一致する。以後、建物タイプ・設備・地域などの分岐は原則この層の宣言（`applies_when`）だけで表現し、コアは触らない。

## 1. なぜ Plan組立層に切り出したか（棄却案の記録）

適用判定をどこに置くかで3案を比較し、**第3案（Applicability Adapter）**を採用した。

- **A案（棄却）：** `ENGINE_MAP.shutter` が非該当時 `genka:0` を返す。→ コアは触らないが、**数量化(quantity_engine)と適用判定(applies_when)が混ざる**。「数量化するには ENGINE_MAP に関数を足す」という約束の意味が濁る。将来必ず効いてくるため棄却。
- **B案（棄却）：** `gaisanCompute` のトレード列を1行 `filter`。意味は素直だが「`gaisanCompute` 無変更」の約束を破る。
- **C案＝採用：Applicability Adapter。** 適用判定を独立レイヤーにし、**コアへ渡す直前に「今回の Plan に適用される工種だけ」を組み立てる**。コアも ENGINE_MAP も無変更、意味も混ざらない。

```
gaisan_basis.json（canonical：全工種）
      ↓  applies_when を評価（共通評価関数 tradeApplies）
      ↓  Plan組立層：今回のPlanに適用される工種だけを組み立てる（assemblePlan）
      ↓
既存 gaisanCompute / tradeGenka（無変更）
      ↓
結果画面（同じ適用結果を使うので、非該当工種はコスト・内訳とも自然に消える）
```

**責務境界（LOCK 相当の運用則）：** 適用判定は **Plan組立層のみ**が持つ。`quantity_engine`（数量化）にも計算コアにも適用判定を持ち込まない。canonical（全工種）は保持し、Plan は canonical からの射影。

## 2. 第1世代の契約（現行実装）

宣言は `gaisan_basis.json` の各 trade に置く。評価は共通関数1つ。

```json
{
  "no": 14,
  "name": "シャッター工事",
  "cost_per_tsubo": 13292,
  "applies_when": { "building_shape": ["ガレージハウス"], "shutter": ["手動", "電動"] },
  "evidence_status": "provisional"
}
```

- **`applies_when`（宣言型）：** キー＝context 変数、値＝許容値の配列。**複数キーは AND**、各キー内は **includes（いずれか一致）**。条件なしの工種は常に適用。
- **共通評価関数：**
  ```js
  function tradeApplies(t, ctx){
    const c = t.applies_when;
    if(!c) return true;                                   // 無条件は常に適用
    return Object.keys(c).every(k => !Array.isArray(c[k]) || c[k].includes(ctx[k]));
  }
  ```
- **Plan組立層：**
  ```js
  let PLAN_ALL_TRADES = [];                               // canonical（全工種）を一度だけ保持
  function assemblePlan(){                                // コアへ渡す直前に射影
    const ctx = planContext();                            // { building_shape, shutter, ... }
    GAISAN_BASIS.trades = PLAN_ALL_TRADES.filter(t => tradeApplies(t, ctx));
  }
  ```
  `calcGaisan()` の先頭で `assemblePlan()` を呼ぶだけ。`gaisanCompute`/`tradeGenka` は無変更。
- **`evidence_status`：** `provisional`（Evidence 未確立）/ 将来 `verified` 等。金額・係数の格を示す。

## 3. 実証結果（実データ・今野基準 32坪）

| 建物形状 | シャッター | シャッター工事 | 工事原価（Σ cost_per_tsubo×坪） |
|---|---|---|---|
| 総二階 ほか | — | 除外 | 26,673,152 |
| ガレージハウス | なし | 除外 | 26,673,152 |
| ガレージハウス | 手動 / 電動 | 計上 | 27,098,496（+425,344） |

- **ガレージハウスを選んだだけでは加算しない**（`shutter` が `手動/電動` のときのみ）。仕様一致。
- 非該当時は Plan に入らないため、**コストも内訳表示も自動で除外**（¥0 行の小細工不要）。
- コア無変更を機械確認（`gaisanCompute` / `tradeGenka` 原本一致・`ENGINE_MAP` にシャッターキー無し）。

## 4. 一般化（同じ層に載る将来の分岐）

建物タイプ・設備・地域は、コード改変なしに宣言追加だけで増える：

```json
{ "trade": "太陽光工事",   "applies_when": { "solar": ["あり"] } }
{ "trade": "防火サッシ",   "applies_when": { "region": ["準防火地域","防火地域"] } }
{ "trade": "耐雪仕様",     "applies_when": { "snow_region": ["あり"], "roof_shape": ["切妻"] } }
```

想定属性：ガレージハウス／二世帯住宅／店舗併用住宅／長期優良住宅／GX志向型住宅／ZEH／太陽光／蓄電池／全館空調 …。すべて `applies_when` で表現。

## 5. Observations（unapplied・将来候補・**今は作らない**）

Architecture Freeze / Evidence First に従い、以下は**記録のみ**。第1世代 `applies_when` で現段階は十分。

### 5.1 Rule Engine（比較演算への拡張）

第1世代は「配列 includes」のみ。将来は比較演算が欲しくなる：
```json
{ "floor_area": { ">=": 40 } }
{ "garage_count": { ">": 1 } }
```
そのとき評価は **`evaluateRule(rule, context)`** 一本に集約し、`tradeApplies()` は `return evaluateRule(t.applies_when, ctx)` を呼ぶだけになる。これで **Rule Engine** が成立し、概算見積に限らず **数量エンジン／製品選定／補助金判定／見積テンプレート／確認申請チェック** まで共通利用できる。

### 5.2 リッチ構造 `applicability:{}` の候補

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
      ▼  Applicability Projection（applies_when で評価）
Plan  ──▶  Quantity  ──▶  Cost
```

**Canonical** には `シャッター工事` が**存在する**。しかし **Plan** では `applies_when` によって「存在する／しない」が決まる。これは Graph Runtime の `Canonical Graph → Projection` と**同型**であり、すなわち **Applicability も Projection の一種**。式で書けば：

```
Plan = Canonical × Applicability Projection
```

例（GX住宅）：Canonical は `太陽光 / 蓄電池 / HEMS` を全部持つ。**普通住宅では Projection されず、GX住宅では Projection される。**

**含意（将来・未検証）：** これが実証されれば、`Geometry Runtime`／`Graph Runtime`／`Applicability Runtime` がすべて **`Canonical → Projection → Runtime`** という共通パターンで説明できる可能性がある。KKai の既存 Observation 群（「Geometry is the canonical model from which all quantity projections are derived」「UI is a projection of runtime state」）と同じ系列。

> **ただし昇格しない。** Evidence はシャッター1件のみ。「Runtime と同じ概念」と言い切る証拠は無い。ここでは **「Graph Runtime の Projection と非常によく似た構造を持つ」という観察として残すだけ**にとどめ、一般化（共通パターンへの統合）は行わない。この“記録だけ”という現方針がちょうど良い。

## 6. Evidence 未確立（provisional のまま据え置き）

以下は 4棟に実績が無く（n=0）、**でっち上げない（Rule 3）**。Evidence が付いてから確定：
- シャッター工事の金額（現状は坪単価由来の暫定値）。
- 手動／電動の金額差。
- 幅・高さ・台数による数量化、ガレージ面積との連動。
- ガレージハウスの形状係数（`ensho_to_A`/`P_shape_factor` は総二階と同値の暫定）。

## 7. KCP 思想との整合

`Evidence First`（未確立は provisional・据え置き）／`Engine 不変`（gaisanCompute・tradeGenka・ENGINE_MAP 無変更）／`Rule 追加で機能拡張`（宣言を足すだけ）。**適用ルールを「工種の数」でなく「宣言の数」で増やす**という、UI 側 Observation「Variable が増えるのではなく必要な Variable だけ開く」の工種版。

## 関連
- `GAISAN_UI_PRINCIPLES.md`（UI 層。シャッター＝optional の初期表示スコープ。本層はその原価側の実装基盤）
- `WALL_QUANTITY_EXTRACTION.md` / `GUTTER_RUNTIME_VALIDATION.md`（Canonical → Projection 系列。§5.3 の横断 Observation はこの系列の兄弟）
- 実装：`index.html`（tradeApplies / assemblePlan / PLAN_ALL_TRADES・`calcGaisan` 先頭で `assemblePlan()`）／`housing/gaisan_basis.json`（`applies_when`）
