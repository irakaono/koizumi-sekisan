# KKai 外壁 数量抽出プロトコル（Wall Quantity Extraction）— Step6-1／6-2

> **DRAFT / 2026-07-24（v6・設計フェーズ完了・骨格固定：Evidence Quality／Canonical Geometry Model・Projection・Identity／Identity Generation Rules・Geometry Change Policy LOCK）** — Phase3 Step6-1 の作業文書（Step6-2 実測中）。目的は式でも棟追加でもなく、Step5 で「内訳書からは取れない」と判明した二次数量（役物下地長・目地長）を**再現性をもって定義**できるか検証すること。KKai の順序「Quantity → Evidence → Engine」を守る。ここで定義が固まった数量だけが `VARIABLE_DEFINITIONS.md` の正式 Variable に昇格する。**律速はデータ数ではなく Quantity Definition。**
>
> **v3（2026-07-24）：** gap 2〜7 を**確定文言化（Definition 補完）**。**Definition＝施工対象／Extraction＝探し方** の分離を徹底。
>
> **v4（2026-07-24）：** P_opening で**段窓の中間無目二重計上**が発覚→Definition に「施工される連続外周を採用」を一文追記して LOCK。`仮説→文書→実証→Evidence→修正` の初適用。今野 P_opening＝**約73.6m**。
>
> **v5（2026-07-24）：** 今野の図面3枚をチャット受領。P_footprint の照合で**私の誤り**を発見：内訳「底辺系141m」を単一幾何量へ直接照合したのが誤り（141m は非正規化合計）。→ **Definition 無変更・新 Variable なし、直すのは Reconcile 方法**（区間別対応表）。141m単純合計照合は撤回。L_corner も推定停止→出隅台帳へ。
>
> **v6（2026-07-24・Evidence Quality 層）：** footprint 位相を意匠PDFから安定抽出できなかったのは **Source の否定ではなく Method 側の Evidence**。**Extraction を Source／Method に分け、レイヤー「Evidence Quality」を新設**。DXF があれば Canonical、無ければ manual_from_pdf→後日 cad_verified 昇格。
>
> **v6 追補（2026-07-24・Canonical Geometry Model／Projection／Identity＝Roof Runtime 整合）：** Geometry の正規データ（**Canonical Geometry Model**）は **Extraction の成果物**。**Corner/Segment Ledger・Polygon・Quantity はその Projection**、Runtime が保持するのは **Model だけ**（Roof Runtime `Model → Projection` と同一）。**Recognizer は Geometry Builder**。**Identity（VertexID/SegmentID/CornerID）は Model に属す**。工種一般化＝KKai の Geometry Layer。
>
> **設計フェーズ完了・骨格固定（2026-07-24）：** `Definition → Extraction → Canonical Geometry Model → Projection → Evidence Quality → Reconcile → Engine` が責務重複なく閉じ、Roof Runtime・Persistence・Projection・Recognizer と整合。**Identity Generation Rules と Geometry Change Policy を LOCK**（下記）。これで「どの層が何を変更できるか」まで定義され、**設計骨格を固定（frozen）**。以後は概念追加でなく**実証**（今野邸で破綻しないことの積み上げ・実データで必要最小限の修正のみ）。※ ENGINE_PRINCIPLES 昇格は外壁実証後。

## Definition of Done（Step6-1 の完了条件）

Step6-1 は「図面から数量が取れた」では完了しない。次の2つを満たして完了とする。

1. **取得可能性：** 定義した数量が、いずれかの再現可能なソース（図面／CAD／将来 Recognizer）から取得できる。
2. **Inter-observer reproducibility（観測者間再現性）：** **別の人・別の手段が同じ図面から測っても同じ値になる。** 例：`P_footprint` を小野が54.32m、私が54.28m、将来 Recognizer が54.30m と出せば成功。54／61／49 のように割れるなら、それは数量の問題ではなく**定義の曖昧さ**であり、Definition へ差し戻す。
   > **パイロットで「ここは出隅に数える？」と1回でも迷ったら、それは Definition が足りないという Evidence。** その迷いを全部拾って定義へ戻すことが Step6-1 で最も価値ある成果。

## Quantity Definition と Extraction Protocol を分離する（設計方針）

同じ数量でも「**何か（Definition）**」と「**どう取るか（Extraction）**」は別レイヤーにする。理由：将来 Recognizer が CAD から直接数量を出すようになれば Extraction は差し替わるが、Definition は不変。分けておけば Recognizer 導入時に定義文書を書き換えずに済む。

```
Quantity Definition   … その数量が物理的に何か（不変・長寿命）＝施工対象で書く
        ↑ 参照
Extraction Protocol   … 現時点でどのソースからどう取るか（差し替え可）＝探し方で書く
   現在: 意匠図の寸法/注記を人がトレース
   将来: CAD属性 / Recognizer が自動抽出
```

> **v3 で確立した書き分けルール：** Definition は**施工物**で書く。図面注記（「下端土間天」等）は Definition に書かず **Extraction Rule** に落とす。gap5・gap7・P_opening(v4) はこの原則で書いた。

### Canonical Geometry Model と Projection（v6追補・Runtime 正規モデル／Model→Projection）

**Canonical Geometry Model（Geometry の正規データ）は Extraction の成果物であり、Corner Ledger・Segment Ledger はその Projection である。Runtime が保持する正規データは Canonical Geometry Model である。**（Definition だけでは Model は存在しない——DXF でも PDF でも Recognizer でも、Extraction して初めて生成される。）

> **用語（一度だけ明示）：** 「Repository」は**保存方法**（DB・ストレージの含み）を帯びるが、ここで言いたいのは「Runtime が保持する唯一の真実」という**意味**。正式名は **Canonical Geometry Model**（＝Model＝意味／Repository はその保存形）。Runtime 層で書くと `Extraction → Canonical Geometry Model → Projection → Runtime View`。**Corner Ledger も Quantity も Geometry の View**。ENGINE_PRINCIPLES / Roof Runtime（Model だけ保存し Drawing/Quantity/Material は Projection）と完全一致。

- **層順：** `Definition → Extraction → Canonical Geometry Model（Extraction の成果物）→ Projection（Corner／Segment／Polygon／Quantity）→ Evidence Quality → Reconcile`。Model は Extraction の後（成果物）。
- **Model → Projection：** Runtime が永続保持するのは Canonical Geometry Model だけ。Corner/Segment Ledger・Polygon・**Quantity すら Projection**（保存せず Model から生成）。Recognizer が将来 Polygon だけ／Face・Edge・Vertex だけ返しても、Ledger は Model から射影できる。
- **Identity（Model の一部・Persistence の芯）：** Canonical Geometry Model は幾何**と Geometry Identity（`VertexID / SegmentID / CornerID`）**を合わせて初めて Canonical。同じ実体は源に依らず**同一 ID**（例：`SegmentID=S013 { geometry: polyline…, attributes:{type:GL} }`）。**Projection は幾何をコピーせず Identity を参照するだけ**＝Persistence の芯。Roof Runtime の「**NodeID は不変**」と同一。
- **Recognizer ＝ Geometry Builder：** 従来 `Recognizer → Quantity` を **`Recognizer → Canonical Geometry Model → Projection → Quantity`** に置換。Recognizer は数量エンジンでなく **Geometry Builder**。ここで Geometry Layer と Runtime Layer が接続。今回 DXF から作る Model ＝ Recognizer 教師データ。
- **工種一般化：** 屋根=Ridge／基礎=Footing／開口=Opening／樋 も同じ `Extraction → Canonical Geometry Model → Projection → Engine`＝KKai 全体の Geometry Layer。

> **Observation（ENGINE_PRINCIPLES 昇格の前提メモ・未昇格）：**
> ```
> Geometry is not a quantity.
> Geometry is the canonical model from which
> all quantity projections are derived.
>
> Identity belongs to the canonical geometry model,
> not to its projections.
> ```
> この2文で 屋根／外壁／基礎／開口／樋 が全て `Extraction → Canonical Geometry Model → Projection → Engine` に乗り、Runtime／Persistence／Recognizer／Projection が一本でつながる。昇格は外壁で実証後。

> **Identity Generation Rules（v6・LOCK）：**
> 1. **Identity は Canonical Geometry Model 生成時に一度だけ発番**する。
> 2. **Projection は Identity を変更・生成しない**（参照のみ）。
> 3. **Evidence Quality の変更では Identity は変わらない。**
> 4. **Extraction Method が変わっても、同一 Geometry と判定された場合は Identity を維持**する。
>
> **含意：** manual_from_pdf / cad_verified / Recognizer の3経路が同じ建物を読んでも、同一 Geometry 判定なら SegmentID/CornerID は不変（manual で S013 → DXF 再Extraction で同一判定 → S013 維持、Evidence Quality だけ `manual_from_pdf → cad_verified` 昇格）。逆に別 ID を振ると Projection・Persistence・比較が崩れる。

> **Geometry Change Policy（v6・LOCK／運用規約）：**
> 1. **Evidence Quality の変更では Model を変更しない**（格だけ上がる）。
> 2. **Projection の修正では Model を変更しない。**
> 3. **Reconcile 結果では Model を変更しない。**
> 4. **Definition が変更された場合のみ Model の再生成を認める。**
>
> **含意：** 「DXF の方が正確だから Model を書き換える」を禁じ、`manual_from_pdf → cad_verified → Recognizer` は **Evidence Quality の昇格に一本化**（Identity 維持との境界を曖昧にしない）。これで「どの層が何を変更できるか」まで閉じる＝ **Definition→Model 再生成／Extraction→Model 生成／Evidence Quality→格のみ／Projection・Reconcile→Model 不変**。**設計骨格はここで固定（frozen）。以後は実データで必要最小限の修正のみ。**

### Reconcile 一般則（v5・照合レイヤー／Definition でも Variable でもない）

**非正規化された内訳数量を、単一の幾何数量へ直接照合してはならない。** 内訳書の役物ラベル（水切／スターター／土台水切／コ型見切／板金／窓回りモール…）は、純粋な外周長ではなく**発注・施工単位・施工高さ・重畳**を含む。幾何量（P_footprint・L_corner・P_opening）と内訳を突き合わせるときは：

1. まず幾何量を**区間別**にトレース（重複しない幾何ラインの総長）。
2. 内訳各行を、**位置／対応する幾何区間／同一区間への重複か／外壁下端でなく中間見切・開口・商品仕様由来か**でマップ。
3. 比較は「幾何量 ↔ 内訳合計」ではなく「**区間別トレース ↔ 内訳各行の対応表**」で行う。

これは Definition 差し戻しでも新 Variable でもない **Reconcile 方法の修正**。既存 LOCK を壊さず・新概念を足さずに非正規化内訳を幾何プリミティブへ戻す照合規約。

### Evidence Quality（v6・Extraction の質を Reconcile 前に明示する）

Extraction は「探し方」だが、その**質**は Source と Method の組で決まり、Canonical Geometry Model の Inter-observer reproducibility を左右する。**Source を否定する前に Method と Quality を分けて記録する**。3軸で記録：

- **Extraction Source：** `意匠PDF / CAD(DXF) / IFC / Recognizer` — Geometry の出所。
- **Extraction Method：** `Manual(人) / CAD属性 / CV / Hybrid` — 取り出し方。
- **Evidence Quality：** `Verified / CAD-derived / Manual(manual_from_pdf) / Estimated` — 再現性の格。

> **層構造（v6 確定）：** `Definition → Extraction(Source/Method) → Canonical Geometry Model（Extraction 成果物・Runtime 正規データ・Identity 付き） → Projection(Corner/Segment/Polygon/Quantity) → Evidence Quality → Reconcile`。
> **含意：** Model の値と Identity は不変で、後日ソースが上がれば **evidence_quality だけが `manual_from_pdf → cad_verified` へ昇格**する（Geometry Change Policy と一致）。Projection（台帳）各行に `evidence_quality`（と必要なら source/method）列を持たせる。
> **今回の Evidence（Method 側）：** footprint 位相について `Source=意匠PDF・Method=人＋ベクタ抽出` は外郭コンターが安定せず Evidence Quality が本目的に対して不足。→ DXF があれば `Source=CAD・Method=CAD属性・Quality=CAD-derived` を Canonical に。

## Primary / Derived / Engine の境界（本フェーズで初めて明文化）

外壁の数量整理で、Variable 層がさらに2段に分かれることが見えた。**この境界は Rule 3 と矛盾しない**——Rule 3 は「**Engine** が Variable を生成しない」であって、Variable 同士から**固定された定義**で別の Variable を導出することは禁じていない。

```
Primary Variable（測定した Evidence）
   gross_wall_area / opening_area(サッシ表) / eave_length / siding_product /
   board_module(商品仕様) / L_corner(図面) / P_footprint(図面)
        │  固定された定義で導出（Variable 層の責務・Engine ではない）
        ▼
Derived Variable（Primary の決定的関数）
   net_wall_area = gross − opening
   P_opening     = Σ 2(W+H)  ※施工される連続外周（段窓/連窓は合成）＝v4
   横目地長      = net / board_module
        ▼
Engine（Primary も Derived も「採用」するだけ・生成しない）
```

- **含意：** `net_wall_area` は確定 Variable だが実は Derived（gross−opening）。誰が計算しても同じ。Derived は決定的計算なので Evidence First を壊さない。
- Primary/Derived 境界は Variable 契約一般に効くが、**今は原則本体へ昇格させない**（外壁で実証しきってから）。

---

## 図面実査結果（2026-07-23 フィージビリティ／2026-07-24 ラスタ受領）

プロジェクト文書からはラスタ画像を展開できない（`project_read` はテキストのみ）。**2026-07-24、今野の改訂図3枚をチャット受領**し、ベクタ座標＋モジュールグリッドで外周トレースを試行（PyMuPDF・寸法線から縮尺較正：9,100幅＝515.8pt・7,735高＝438.5pt・≈17.64mm/pt、1F/2F 同一レジストレーション）。

| 図面（受領版） | 棟 | 種別 | 縮尺 | 日付 |
|---|---|---|---|---|
| 1階平面図0718.pdf | 今野 | 1F 平面 | 1/50 | 2026.07.03 |
| 2階平面図0716.pdf | 今野 | 2F 平面 | 1/50 | 2026.06.20 |
| 立面図0718.pdf | 今野 | 4面立面 | 1/100 | 2026.07.18（軒高6,205/6,571・軒ゼロ・ガルバ＋北面窯業アクセント） |

**今野 massing（実測所見・Evidence Quality=Manual）：** 総2階・軒ゼロ・軒高6,205（低側）〜6,571（高側・北）。外形は単純箱ではなく、ガレージ（左・X0〜3640・Y1820〜7735・壁＝外壁材＝envelope）＋主屋（右・X3640〜9100・Y0〜約6370）＋ポーチ欠き込み（左上）＋WC/収納の入隅・セットバック段差。基礎400/1F 2,955/2F 2,850。面材＝金属ガルバ（出隅grade＝金属）、北面ポーチ背面のみ窯業アクセント。**1F と 2F の外形は不一致**（出隅は通し/1階/2階を区別要）。
**Method 所見：** 外郭コンターの自動抽出は寸法線・建具姿図・軒/竪樋の混線で不安定（bbox 化）。→ footprint 位相は DXF が来れば Canonical に、無ければ manual_from_pdf で生成（下記 (a)(b)）。

---

## 各数量：Definition と Extraction

### fitting_substrate_length（役物下地長）

役物は稜線・底辺・開口周りの3位置に沿う線的部材。位置ごとに別数量とし、役物グレードをタグ付け（Step5：長さ×グレードでないと較正できない）。

#### (a) L_corner — 外周稜線長（出隅役物）

- **Quantity Definition（施工対象・v3 gap2〜4 確定・無変更）：** 外壁外周のうち**出隅（外向き凸角）に沿う垂直稜線の総長**。入隅は含めない。稜線高さ＝左右2面がともに envelope 外装面として成立する垂直区間の実高を積算（本数×階高では数えない・通し出隅は連続区間で1本）。非直角出隅も算入（`斜め壁`タグ別グレード）。両隣が envelope 外装面の出隅のみ算入（内装側除外）。
- **Geometry / Projection：** Corner は Canonical Geometry Model の要素（Identity＝`CornerID`）、**Corner Ledger はその Projection（View）**。源が PDF/DXF/Recognizer でも同一 Model・同一 CornerID → 同一 Ledger。
- **Extraction（v6・出隅台帳方式）：** 推定禁止。**出隅を1本ずつ台帳化**して合計。Projection 列：
  `corner_id | 位置(X,Y) | 左右2面の向き | 通し/1F/2F | 下端z | 上端z | 実高 | corner_grade | evidence(図面) | evidence_quality`
  出隅/入隅は footprint 幾何から判定（gap1）。台帳合計 ↔ 内訳「出隅45m」は Reconcile 一般則で対応表照合。
- **役物グレードタグ：** `corner_grade ∈ {同質, L型, 金属, 斜め壁, その他}`。今野＝金属ガルバ。Step5＝同質4,000／L型2,300／金属1,350円/m。

#### (b) P_footprint — footprint周長（底辺役物）

- **Quantity Definition（施工対象・一行・v3 のまま無変更）：** **P_footprint ＝ 外装面（envelope）下端に施工される底辺役物（水切・スターター・土台水切）の水平長総和**（＝外装面下端に存在する、**重複しない幾何ラインの総長**）。控除（gap5）：底辺役物が連続施工されない水平区間は控除（判定手段は Extraction 側）。外装面のみ算入（gap6）。探索範囲（gap7）：GL に限らず下屋・オーバーハング等、外装面が途中から開始する水平下端を含む。
- **Geometry / Projection：** 下端 Segment は Canonical Geometry Model の要素（Identity＝`SegmentID`）、**Segment Ledger はその Projection**。源が変わっても同一 Model・同一 SegmentID。
- **Extraction（v6・Segment 台帳方式）：** 外装面下端の**重複しない幾何ライン**を区間別に台帳化。Projection 列（Geometry と Reconcile を分離）：
  `[Geometry] seg_id | 長さ | 幾何区間(GL/下屋/OH) | 下端種別 | evidence | evidence_quality ‖ [Reconcile] 内訳対応(水切/スターター/土台水切) | 重複 | 由来`
  控除区間（下端土間天・GL 注記等）を明示（例：ガレージシャッター W3000）。
- **Reconcile Rule（v5・141m単純照合を撤回）：** 内訳「底辺系141m＝水切65＋スターター60＋土台水切16」を P_footprint と単純合計比較しない。区間別トレース ↔ 内訳各行（＋コ型見切80/窓回りモール19 との境界非正規化に注意）を対応表で照合。

#### (c) P_opening — 開口周長（見切/モール/開口周囲役物）

- **Quantity Definition（施工対象・v4 LOCK）：** **外装見切・モール・開口周囲役物が実際に施工される連続外周を採用**（`Σ 2(W+H)`）。複合開口（段窓・連窓・親子ドア）はユニット単位でなく**1つの連続開口の外周**（中間無目・方立を含めない）。**Derived**。
  > **Evidence→Definition 修正（初）：** 段窓3か所が中間無目を二重計上（78.5 vs 73.6、差5.0m）。「連続外周」に一文追記して LOCK。opening_area（ユニット単位）と P_opening（連続外周）は目的が違うので数え方が一致しなくてよい。
- **Extraction：** サッシ表 W×H。段窓は無目で連続判定（テキスト・Quality=Verified）。水平連窓は平面/立面隣接で判定（画像）。

> **今野 P_opening（v4）＝約73.6m**（evidence_quality＝Verified：サッシ表テキスト）。母集合面積和＝23.05㎡（opening_area と一致）。残る微確認：2F 南 AW-09/AW-10 の水平連窓判定（受領図で確定）。

### joint_length（目地長）— 関数仮説は棄却、共通ドライバーへ

`横目地長 ≒ net/board_module` は残差を埋めない（r=0.202）。コーキング目地長＝横目地＋縦目地(形状)＋開口周(P_opening)＋稜線(L_corner)。P_opening・L_corner は役物とコーキングの共通ドライバー。joint_length は独立 Evidence にせず再利用で組む。縦目地(形状項)のみ未取得。

---

## パイロット（今野）で採れた gap 一覧

**L_corner（gap1〜4）／P_footprint（gap5〜8）：** gap2〜7 は v3 で Definition 確定。gap1・8 は Extraction gap（外周トレース＝画像/CAD要）。**v6：Method 側の Evidence Quality を分離。**
**P_opening（gap9〜10）：** gap9（段窓二重計上）は v4 で Definition 確定（Evidence→Definition 初）。gap10（水平連窓）は Extraction gap。
**Reconcile（v5）：** 非正規化内訳を単純合計照合しようとした Reconcile 方法の誤り→区間別対応表を新設。
**Geometry / Identity / Evidence Quality / 運用規約（v6）：** Corner/Segment Ledger は Canonical Geometry Model の **Projection**（Model が Extraction 成果物・Runtime 正規データ・Identity 付き）。Recognizer＝Geometry Builder。Identity Generation Rules・Geometry Change Policy LOCK。**設計フェーズ完了・骨格固定。**

## 数量取得可否サマリ（Step6-2・v6）

| 数量 | 種別 | Definition | Extraction Source/Method | Evidence Quality | 状態 |
|---|---|---|---|---|---|
| P_opening | Derived | 確定（連続外周・v4） | サッシ表/テキスト | Verified | ✅ 73.6m（連窓のみ微確認） |
| net_wall_area | Derived | 確定 | 既存 | Verified | ○ |
| siding_main_unit_rate | Primary | 確定 | 内訳書メイン行 | Verified | ○(Step5) |
| L_corner | Primary | 確定（v3・無変更） | 意匠PDF/Manual →（DXF/CAD属性で昇格） | manual_from_pdf→cad_verified | ◐ manual で Model→Corner Ledger 生成予定 |
| P_footprint | Primary | 確定（v3・無変更） | 意匠PDF/Manual →（DXF/CAD属性で昇格） | manual_from_pdf→cad_verified | ◐ manual で Model→Segment Ledger 生成予定 |
| board_module | Primary | 確定(商品仕様) | カタログ/発注 | — | △ 未取得 |
| 縦目地(形状項) | Primary | 未定義 | 割付図/定尺 | — | ✕ 意匠図に無い |

## 次アクション（設計完了・骨格固定 → 実証フェーズ）

設計フェーズ完了・骨格固定（frozen）。以後は概念追加でなく、実データで破綻しないことの積み上げ：

1. ▶ **今野邸を `manual_from_pdf` で Canonical Geometry Model 化**（footprint polygon＋`VertexID / SegmentID / CornerID` を Identity Generation Rules に従い一度だけ発番）。
2. ▶ **Identity 付与**（規約準拠）。
3. ▶ **Projection 生成**：Corner Ledger／Segment Ledger（Model からの射影・evidence_quality=manual_from_pdf）。
4. ▶ **Reconcile 実施**：L_corner Corner Ledger ↔ 出隅45m／P_footprint Segment Ledger ↔ 水切65・スターター60・土台水切16（＋コ型見切80・窓回りモール19）を区間別対応表で。ずれたら疑うのは Extraction か Evidence（Definition は疑わない）。
5. ▶ **DXF 入手後に再Extraction**し、同一 Geometry 判定で **Identity が維持されるか**を検証（維持されれば Evidence Quality のみ `manual_from_pdf → cad_verified` 昇格・Model 値と Identity は不変＝Geometry Change Policy 準拠）。

> **Canonical Geometry Model Acceptance Criteria（各案件で「実証OK」を判定する4点・v6）：**
> - **Completeness：** 必要な Vertex/Segment/Corner がすべて存在するか。
> - **Consistency：** ID 参照が切れていないか（Projection→Model の参照がすべて解決）。
> - **Determinism：** 同じ入力から同じ Model（Identity 含む）が生成されるか。
> - **Projection Fidelity：** Projection（Corner/Segment Ledger・Quantity）が Model を忠実に表現しているか。
>
> この4点を各案件で満たして初めて「実証OK」。上記5ステップの合否基準として使う。

→ **この5＋4基準が通れば、Canonical Geometry Model・Projection・Identity は概念でなく KKai Runtime で実証済みアーキテクチャ。**

（実証後：共通ドライバー展開（P_opening・L_corner を役物とコーキング両系統に）／`VARIABLE_DEFINITIONS.md` 昇格（Primary/Derived・evidence_quality 明記）／棟追加較正 → calcWall。順序 Quantity → Evidence → Engine を崩さない。）
