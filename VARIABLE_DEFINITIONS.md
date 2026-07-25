# KKai Phase3（calcWall）引き継ぎ書

> **状態（2026-07-24 更新）：** 概算アーキテクチャの**設計フェーズ終了・凍結**。**Phase3 Step1〜Step5 完了・Step6-1 クローズ（Quantity Definition 確定）。Step6-2 着手：今野ラスタ受領 → P_opening 確定（73.6m）→ 外壁数量抽出を KKai Geometry Runtime へ一般化**（`WALL_QUANTITY_EXTRACTION.md` **v6**：Canonical Geometry Model／Projection／Identity／Identity Generation Rules・Geometry Change Policy LOCK・**設計骨格固定**）。**概算UIも v1.1 精緻化**（`GAISAN_UI_PRINCIPLES`：Variables は表示可能・位置は Progressive Disclosure）。**次は実証フェーズ**：今野を `manual_from_pdf` で Canonical Geometry Model 化 → Corner/Segment Ledger 射影 → 内訳照合 → DXF で Identity 維持検証。式（calcWall）はまだ作らない（n=4 過学習回避）。

## Observations（ENGINE_PRINCIPLES 昇格候補・未昇格／実証が通ったものから順次昇格）

実証前は断定せず **Observation** に留める（`仮説→文書→実証→Evidence→修正`）。説明・比較図は昇格時に書く。

```
Geometry is not a quantity.
Geometry is the canonical model from which
all quantity projections are derived.

Identity belongs to the canonical geometry model,
not to its projections.

UI is a projection of runtime state.
```

上3つ（Geometry/Identity）は `WALL_QUANTITY_EXTRACTION` 由来、4つ目（UI）は概算UI v1.1 由来。外壁実証が通ったら `Runtime State → Projection { Geometry / Quantity / UI / Schedule / Carbon }`（"Runtime state is never consumed directly; every consumer observes a projection."）として ENGINE_PRINCIPLES へ昇格候補。**今は一行の目印のみ・LOCK 維持。**

### メタ観測（開発方法論の萌芽・未文書化・DEVELOPMENT_PRINCIPLES は作らない）

```
Architecture is stabilizing.
Methodology is emerging.
```

今回一連で固定したのは**構造（Architecture）**：Geometry Runtime／UI Principles／Engine契約／Identity／Projection。その上に、本引き継ぎ全体で繰り返し現れた **Evidence Lifecycle**＝`Hypothesis → Document → Experiment → Evidence → Correction → Lock` があり、**開発方法論（Methodology）そのものが姿を現し始めた**（P_opening／P_footprint／UI v1.1 は全て同一ライフサイクル）。将来 ENGINE_PRINCIPLES の上に `DEVELOPMENT_PRINCIPLES`（工種・層に依らない開発原則）が一冊立ちうる。**ただし今は作らない**——今作れば概念が増える。まず外壁実証を完了させる（Evidence First の順序）。Observation に留める。

## 0. 設計フェーズ終了・実証フェーズへ（2026-07-24）

**ロックされたのは文書ではなく「変更ルール」。** 設計変更を許可するのは次のサイクルだけ：`仮説 → 文書 → 実証 → Evidence → 修正`。「思いついた→良さそう→新概念追加」はしない。この変更ルールは KKai の Rule 0（Evidence First）そのもの＝設計が自分の原則で自分を律している。

**データフロー（一本）：** `Evidence → Variable → Priority → Policy → Engine → UI`。

**calcWall ＝ この一本の最初の実証実験。** 問題が出たら、まず疑うのは実装ではなく**アーキテクチャ上の位置**——「Evidence が足りないのか／Variable 定義が不足なのか／Priority の運用なのか」。

**実証サイクル（住宅数十棟で反復）：** 1. 実データ（今野様邸〜）→ 2. Variable 抽出 → 3. Engine 実行 → 4. 概算結果 → 5. 内訳との比較 → 6. 差分分析 → 7. **Evidence があるものだけ修正**。思想を崩さず精度だけが育つ。

## 1. 現在地と次アクション

- ✅ Step1：4棟の外壁ブロック抽出（付録A）
- ✅ Step2：Variable定義（`VARIABLE_DEFINITIONS.md`）＋4棟 opening_area 確定（正典サッシ表）
- ✅ Step3：net での相関 → **面積は gross/net とも外壁原価を説明しない**（Evidence確定）
- ✅ Step4：**構造分解**。各施工系統の一次ドライバーを特定（`WALL_COST_STRUCTURE.md`）
- ✅ Step5：**数量化検証（n=4）**。面材と役物は同型＝[数量]×[グレード]。二次数量は内訳書だけでは確定できない。
- ✅ Step6-1（Quantity Definition 確定・クローズ）：gap2-7 を確定文言化（v3）。**Definition ✅ Closed／Extraction ⏳ Waiting。** meta成果＝`施工対象 → Definition → Extraction → Recognizer` 階層。
- ✅ **Step6-2 着手・Geometry Runtime 一般化（2026-07-24）：** 今野ラスタ3枚受領（1階平面図0718・2階平面図0716・立面図0718）。**P_opening＝73.6m 確定**（段窓の連続外周・v4 が Evidence→Definition の初適用）。P_footprint 照合の誤り（内訳「底辺系141m」への単純合計照合）を **Reconcile 一般則**で修正（141m は非正規化合計＝区間別対応表で照合）。footprint 位相の Extraction は意匠PDFでは **Method 側の Evidence Quality 不足**→ **DXF を Canonical Source**（無ければ manual_from_pdf→cad_verified 昇格）。外壁数量抽出が **`Definition → Extraction → Canonical Geometry Model → Projection（Corner/Segment Ledger・Quantity・UI）→ Evidence Quality → Reconcile`** の Geometry Runtime へ一般化（→ `WALL_QUANTITY_EXTRACTION.md` **v6**・設計骨格固定）。**Recognizer＝Geometry Builder／Identity（VertexID/SegmentID/CornerID）は Model に属す／Identity Generation Rules・Geometry Change Policy LOCK。**
- ✅ **概算UI v1.1（2026-07-24）：** 屋根数量・基礎A/P を①金額から②詳細へ（Variable だから・工種の例外を作らない）。シャッターは既に optional。原則を「Variables は見せる」→「**Variables は表示可能・位置は Progressive Disclosure**」に精緻化（Ver0.4.4 実証由来・原則追加でなく wording 修正）。→ `GAISAN_UI_PRINCIPLES` v1.1。
- ▶ **現在＝実証フェーズ（設計は固定）：** 今野を `manual_from_pdf` で **Canonical Geometry Model 化**（footprint polygon＋Identity 発番）→ Corner/Segment Ledger を **Projection** → **Reconcile**（L_corner ↔ 出隅45m／P_footprint 区間別 ↔ 水切65・スターター60・土台水切16 の対応表）→ **DXF 入手後に再Extraction し Identity 維持＆Evidence Quality 昇格を検証**。合否＝**Acceptance Criteria（Completeness／Consistency／Determinism／Projection Fidelity）**。

## 2. 固定ルール（変更しない）

- ENGINE_SPEC **v1.0 LOCKED**。コアロジック `tradeGenka`／`gaisanCompute` は無変更。EngineResult 契約固定：`genka / qty / basis / used / fallback / confidence`。
- Variables ＝ 取得した事実。**Variables に推定ロジックを書かない。** Engine は Variable を生成せず選択する（Rule 3）。
- Scope First / Evidence First。新しい仕組みは作らず、ENGINE_MAP にエンジンを1つ足す。
- **式を焦って作らない。** 施工系統へ分解して一次ドライバーを特定してからモデル化。
- **Definition ≠ Extraction、その上に 施工対象 → Definition → Extraction → Recognizer。** さらに v6 で `Definition → Extraction → Canonical Geometry Model → Projection → Evidence Quality → Reconcile` に一般化・骨格固定。**Model 変更は Definition 変更のときだけ（Geometry Change Policy）。Identity は同一 Geometry 判定なら源が変わっても不変（Identity Generation Rules）。**

## 3. 既存エンジン

| Engine | 工種 | モデル | n | 最大誤差 |
|---|---|---|---|---|
| calcKiso | 基礎工事 | `F + a×基礎面積A`（F=1,366,743 / a=2,897） | 4 | ±5.4% |
| calcRoof | 樋・屋根工事(RoofEnvelope) | `F + a×軒先長`（F=212,823 / a=50,478） | 4 | +10.3% |
| **calcWall** | 外壁工事 | **未定・複数ドライバー（分解済・数量化検証済／式は未着手）** | 4 | — |

> 基礎＝1ドライバー、屋根＝1ドライバー、**外壁＝複数ドライバー**が初めて Evidence で確定。EngineResult さえ返せば内部が何項でも契約は守れるため ENGINE_SPEC v1.0 は無傷。

## 4. 4棟 確定データ（envelope・今野ガレージ内装は Scope 除外）

| 棟 | envelope原価 | gross | opening | net | 開口率 | eave長 | 面材商品 |
|---|--:|--:|--:|--:|--:|--:|---|
| 今野 | 2,452,250 | 199㎡ | 23.05㎡ | 175.95㎡ | 11.6% | 18.8m | 金属ガルスクエア（突出） |
| 安原 | 1,607,050 | 164㎡ | 18.40㎡ | 145.60㎡ | 11.2% | 12.21m | KMEW 新フラット16 |
| 小峰 | 1,794,150 | 181㎡ | 19.91㎡ | 161.09㎡ | 11.0% | 24.0m | ニチハ ルビドフラット |
| 村田 | 1,462,700 | 193㎡ | 18.56㎡ | 174.44㎡ | 9.6% | 11.3m | KMEW シマンフラット |

- opening_area の正典は**サッシ見積書／Nプランの外枠W×H**（室内建具は除外）。今野は gross・原価にガレージ外壁を含むため、Scope整合上ガレージ外部開口も控除して 23.05㎡。
- 開口率は 9.6〜11.6% に収束（n=4）。
- **4棟の付録A明細合計 = envelope原価 に全棟一致（再検算 2026-07-23）。** Step5 の数量化はこの構造化明細から算出。
- **今野 P_opening（連続外周・v6）＝約73.6m**（母集合面積和 23.05㎡ で opening_area と一致）。

## 5. Step3 の結論（Evidence）

- 原価 vs gross面積：r=0.524／原価 vs net面積：r=0.562（4棟）。**開口控除しても改善せず。**
- ガレージ無し3棟のみ：原価 vs net面積 **r=−0.40（負）**。
- 結論：**面積（gross/net）は外壁原価を説明しない。**

## 6. 構造分解＋数量化検証の結論（`WALL_COST_STRUCTURE.md` 要約）

外壁原価は少なくとも次の施工系統に分解され、Step5 で各系統の**二次数量が取れるか**を判定した：

- **面材（52〜62%）→ net面積 × グレード。** メイン単体単価＝金属7,500／窯業4,700〜5,200円/㎡。金属/窯業の2帯まで構造的に見えるが確定係数化は保留。
- **軒天＋軒廻り換気（8〜18%）→ 軒先長 eave_length。** r=0.745。屋根の eave_length を再利用できる。
- **下地シート＋コーキング＋廃材（15〜19%）。** コーキングは面積で説明されない。真のドライバー＝目地長は内訳書に無い隠れ数量。
- **役物（8〜12%）→ 下地長 × 役物グレード。** 内訳書ラベルからは正規化下地長に落ちない。
- **諸経費（1.6〜2.0%）→ 固定費。**

> **新発見（Step5）：面材と役物は同型＝[数量]×[グレード]。**
> **新発見（Step6-1）：開口周長・稜線長は役物とコーキングの共通ドライバー**（共有幾何プリミティブ2組目）。

## 7. calcWall 設計方針（決定済み）

- net_wall_area は正式Variable として保持（Engineが採用しないだけ）。
- siding_product は保持、`grade_factor` は Evidence 不足のため作らない。
- 最小モデル1数量では不可 → 分解型（固定費＋面積項＋軒先項＋…）。n=4では確定しない。
- 軒先系は屋根 eave_length を再利用検討。
- 役物・コーキングの二次数量（下地長・目地長）は図面／割付が要る。calcWall はまず軒裏系＋面材（net×2帯）＋固定費で骨格を組む。

## 8. Phase3 手順（現在地＝Step6-2 実証フェーズ・manual_from_pdf 待ち）

1〜5. ✅ ブロック抽出／Variable定義／相関／構造分解／数量化検証。
6. ✅ **Step6-1（Quantity Definition 確定・クローズ）** → `WALL_QUANTITY_EXTRACTION` v3。
7. ◐ **Step6-2（Extraction＝実測）・実証フェーズ：** ✅ 今野ラスタ受領・P_opening=73.6m 確定・Geometry Runtime 一般化（v6・骨格固定）。▶ **manual_from_pdf で Canonical Geometry Model → Corner/Segment Ledger（Projection）→ Reconcile → DXF で Identity 維持検証**（Acceptance Criteria 4点）。→ 取れた数量を `VARIABLE_DEFINITIONS.md` へ昇格（Primary/Derived・evidence_quality 明記）。
8. calcWall 実装（分解型）
9. `ENGINE_MAP.wall` 登録＋JSON `quantity_engine:"wall"`
10. 検証・リリース（Ver0.4.4／各docを更新、VARIABLE_DEFINITIONS を v1.0 昇格）

## 関連ドキュメント（設計書の階層・概念層は 2026-07-24 LOCK）
```
CONSTITUTION → ENGINE_PRINCIPLES → ENGINE_SPEC → VARIABLE_DEFINITIONS → INPUT_PRIORITY → WALL_COST_STRUCTURE → WALL_QUANTITY_EXTRACTION → calcWall
                                                                       ↘ GAISAN_UI_PRINCIPLES（UI層）
```
- `ENGINE_PRINCIPLES.md`（**LOCKED**・工種非依存の設計原則。※ Observations（Geometry/Identity/UI Projection）は外壁実証後に昇格候補）
- `ENGINE_SPEC.md`（**v1.0 LOCKED**・EngineResult契約）／`ENGINE_EVALUATION.md`（エンジン評価台帳）
- `VARIABLE_DEFINITIONS.md`（Variables契約。候補Variable＝L_corner／P_footprint／P_opening／siding_main_unit_rate は保持予約）
- `INPUT_PRIORITY.md`（**LOCKED**・入力重要度のドメイン指標）
- `GAISAN_UI_PRINCIPLES.md`（**LOCKED v1.1**・Variables は表示可能／位置は Progressive Disclosure／3段表示／シャッター optional／Ver0.4.4 適用ノート）
- `WALL_COST_STRUCTURE.md`（外壁で Rule2 が成立した Evidence＋Step5 数量化検証）
- `WALL_QUANTITY_EXTRACTION.md`（**v6**・設計骨格固定・Canonical Geometry Model／Projection／Identity／Identity Generation Rules／Geometry Change Policy／Evidence Quality／Reconcile 一般則／Acceptance Criteria。P_opening=73.6m 確定・L_corner/P_footprint は manual_from_pdf 実証待ち）

## 付録A：4棟 外壁工事 全明細（Step1 生Evidence／全棟 envelope 検算一致）

### 今野邸（合計 2,876,700 / うちガレージ[G] 424,450／envelope 2,452,250）
金属サイディング ガルスクエア 179㎡=1,342,500／出隅 45m=60,750／水切 65m=61,750／スターター 60m=72,000／コ型見切 80m=88,000／ナナメ壁加工 1式=20,000／窯業サイディング アクセント 20㎡=170,000／シート張り 199㎡=89,550／軒天 6㎡=48,000／軒天(ケイミュー) 2㎡=11,600／軒廻り換気 46m=101,200／コーキング 199㎡=169,150／廃材 205㎡=71,750／諸経費=30,000／窓回りモール 19m=53,200／[G]ガレージ内軒天 21㎡=168,000／[G]コーキング 21㎡=17,850／[G]廃材 21㎡=7,350／屋根形状変更 -4㎡=-30,000／コーキング 199㎡=39,800／[G]ガレージ内壁 37㎡=192,400／[G]コーキング 37㎡=38,850／土台水切り 16m=11,200／軒廻り換気 19m=41,800

### 安原邸（合計 1,607,050）
本体(メイン)＋15mm通気金具 142㎡=710,000／本体(アクセント)＋通気金具 22㎡=176,000／L型出隅役物 40m=92,000／シート張り 164㎡=98,400／板金 30m=21,000／板金 17m=20,400／軒天 13㎡=126,100／軒廻り換気 48m=120,000／コーキング 142㎡=156,200／廃材 177㎡=61,950／諸経費 1式=25,000

### 小峰邸（合計 1,794,150）
メイン:ニチハ ルビドフラット 173㎡=899,600／同質出隅 31m=124,000／斜め壁部分出隅 12m=30,000／アクセント:コートリーウッド 8㎡=46,400／シート張り 181㎡=81,450／板金(土台水切) 53m=37,100／軒天 26㎡=209,300／軒廻り換気 50m=110,000／コーキング 181㎡=153,850／廃材 207=72,450／諸経費 1式=30,000

### 村田様邸（合計 1,462,700）
kmew シマンフラット メイン 166㎡=780,200／同 アクセント 22㎡=103,400／kmew エーデルウッド 玄関 5㎡=25,500／L型出隅 42m=96,600／シート張り 193㎡=86,850／板金(土台水切) 39m=27,300／板金(オーバーハング水切) 3m=3,600／軒天 6㎡=27,600／軒廻り換気 37m=92,500／コーキング 166㎡=124,500／廃材 199㎡=69,650／諸経費 1式=25,000

## 付録B：4棟 開口面積（Step2 確定・正典サッシ表 外枠W×H）
- 今野＝23.05㎡（居室13開口16.43＋ガレージ外部開口6.62〔土間ガレージFIX1690×2230・640×2230＋テラス640×2230〕。gross・原価にガレージ外壁を含むため控除）／P_opening（連続外周）＝73.6m
- 安原＝18.40㎡（AD-01玄関＋AW-01〜11 の13開口）
- 小峰＝19.91㎡（AD-01＋AW-01〜15 の17開口）
- 村田＝18.56㎡（AD-01＋AW-01〜10 の12開口）
- 補足：原価内訳書のサッシ行は棟により寸法欠落・誤ラベル。正典はサッシ見積書／Nプラン。
