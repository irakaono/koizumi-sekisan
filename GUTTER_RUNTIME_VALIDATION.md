# KKai Gutter Runtime Validation — Graph 位相の検証（Step7.5）

> **DRAFT / 2026-07-28 更新 / 状態：`仮説 → 文書` 段階（Roof Edge Identity 契約確定済／**Downspout Node の責務を Candidate 契約として確定＝本更新**／Node 以降の実データ実証は未実施）。**
> 目的は**樋数量を作ることではない**。Wall（Polygon）で実証済みの **Canonical Geometry Model / Identity 抽象が Graph 位相でも無改訂で成立するか**の検証。
> 分離規約：**Canonical＝`WALL_QUANTITY_EXTRACTION`（何を実証したか）／Plan＝`PHASE3_HANDOFF §1.5`（次に何をやるか）／本書＝Gutter validation の作業文書。** LOCK（ENGINE_SPEC v1.0・Identity Generation Rules・Geometry Change Policy・Canonical Segment 契約）は一切触らない。新概念は実証が通るまで **Observation**、契約は実証が通るまで **Candidate** に留める（Evidence First）。
>
> **本更新（2026-07-28）：** §4 の本丸 **Downspout Node** を、**LOCKED 契約からの演繹（`文書` 段階）で Candidate 契約として確定**（§4.5）。仮説A＝(b) host_segment+t 採用／仮説B＝Drainage Projection（Geometry ではない）／判定基準＝**新 Geometry Identity 不要**（第3の答え）。中心仮説「Canonical Geometry は topology-independent」への **contract-level Evidence が Finding 1/2 に続き2つ目（Finding 4/5/6）**。**ただし実データ実証（今野屋根伏図＋竪樋位置）は未実施・昇格しない。** Contract → Evidence → Validation の順序を守り、先に契約を固定した。
> **レビュー反映（2026-07-28・小野）：** (1) 契約の host 参照粒度について、寄棟・谷・複雑屋根で将来 `host_run`/`host_face` が要る可能性を**観測点として §4.5.4／§7 に一行追記**（LOCK でも追加でもない・実データで Evidence が出たら見る）。(2) DownspoutNode の **Canonical/Projection 二重の読み**（対 Geometry では Drainage Projection 要素／Drainage 層内では非派生の Canonical State）を §4.5.4 に一文追記（用語の締め・実体の設計は不変）。

## 0. 位置づけと非目標

- **実証済み：** Wall/Foundation ＝ Polygon（閉ループ）位相。今野邸で Canonical Geometry Ledger 固定・Acceptance 4点通過（2026-07-25・`WALL_QUANTITY_EXTRACTION`「今野邸 実証結果」）。
- **本書：** Gutter ＝ KKai 最初の **Graph 位相**。`Roof Edge → Segment → Node → Downspout Graph`。Identity が Polygon の **Vertex** から Graph の **Node** へ移る初めてのケース。
- **非目標：** 樋長・竪樋本数・排水面積を作ること。**目標：抽象（Canonical Geometry / Identity）が Graph で壊れないかの Evidence。** 壊れなければ Geometry Runtime は「一般化された」と見なせる（HANDOFF §1.5）。
- **着手順（Wall と同じ・数量は最後）：** `Roof Edge → Edge Identity → Downspout Node → Connectivity → Graph`。**本書は Roof Edge Identity（契約確定・§2）に続き、Downspout Node の責務を Candidate 契約として確定する（§4.5）。実データ実証はその後。**

## 1. 中心仮説（Hypothesis・要実証）

```
Canonical Geometry の契約
   Vertex  { id, (X, Y) }
   Segment { id, from, to }
は topology-independent である。

Polygon は「全 Vertex が degree=2・単一 cycle をなす」という
Projection 時の制約を課した Graph の特殊形にすぎない。
契約そのものは最初から Graph（辺リスト）表現だった。
```

**検証命題：** Gutter（degree 可変・非閉ループ・排水に方向あり）に対して、同じ契約・同じ Identity Generation Rules・同じ Geometry Change Policy が**無改訂**で成立するか。成立すれば、HANDOFF 保留 Observation（「Canonical Geometry は topology-independent であるべき」）を昇格候補にできる。**昇格は Node/Downspout の実データ実証まで**（Roof Edge＋契約演繹だけでは足りない）。

## 2. Roof Edge Identity（契約レベル確定範囲）

### 2.1 Roof Edge とは（施工対象で書く）

屋根境界・面骨格の線的要素：**軒先（eave）／けらば（rake, 妻側）／棟（ridge）／隅棟（hip）／谷（valley）**。
樋（軒樋）が載るのは **eave**。ridge/hip/valley は drainage area（集水面）に効くが、樋自体は eave に沿う。よって Gutter Runtime の一次線は **type=eave の Roof Edge**。

### 2.2 契約テスト：Segment 契約は Roof Edge を覆うか

Canonical Segment 契約（`WALL_QUANTITY_EXTRACTION` Clarification・LOCKED）：
```
Segment : id, from, to
（length / orientation / 出隅・入隅 は runtime-derived。契約外）
```
Roof Edge は 2 つの roof vertex を結ぶ線 → `{ id, from, to }`。length・type は派生。

> **Finding 1（契約レベル確定）：Roof Edge Identity は新契約を要しない。`Segment{id,from,to}` が無改訂で Roof Edge を覆う。** Edge に固有の Identity 種別（"EdgeID"）を新設する必要はない ＝ SegmentID がそのまま Edge Identity。

### 2.3 Polygon との発散点：Vertex degree

- **Polygon footprint（今野）：** 8 Vertex すべて degree=2（単一閉ループ V01→…→V08→V01）。
- **Roof graph：** 一般に degree>2 の頂点が出る（hip 頂点＝eave＋隅棟2本で度3、valley 頂点、棟と谷の交点 等）。非閉ループ・複数ラン。
- **契約の反応：** Vertex 契約 `{id,(X,Y)}` は degree に一切言及しない ＝ **degree-agnostic**。degree=2 の頂点も degree=3 の頂点も同じ契約。

> **Finding 2（契約レベル確定）：可変 degree・非単一ループという発散は、すべて Projection 層（＝辿り方／loop 再構成）に落ち、Identity/Model 契約には及ばない。** Polygon の「degree=2・単一 cycle」は **Projection 時の制約**であって、Canonical contract の一部ではなかった。
>
> **含意：** Canonical contract は元から Graph（辺リスト）。Polygon は cycle をなす Graph の特殊形。→ 中心仮説（§1）への**最初の Evidence**。ただし Node が通るまで Observation 据え置き。

### 2.4 Edge type は Projection（出隅/入隅 と同型）

eave / ridge / valley / rake の判別は、**隣接する屋根面（Face）から決定的に導ける**：低側で「面↔外気」＝eave、「面↔面」で凸稜＝ridge、凹稜＝valley、妻側の斜辺＝rake。
これは Polygon で出隅/入隅を Face 隣接から導いた（契約外・runtime-derived）のと**同型**。

> **Finding 3（確定）：Edge type classification は Projection。契約に載せない**（出隅/入隅を契約から外したのと一貫）。ただし判別には**屋根面（Face）が必要** → §3。

### 2.5 既存資産との整合：eave_length は Roof Edge graph の Projection

`calcRoof` の一次ドライバー **eave_length**（今野=18.8m・4棟確定）は、Roof Edge のうち **type=eave の Σlength** ＝ **Projection**。`P_footprint = Σlength(footprint loop)` と完全同型（今野=33.67m）。

> **Observation（calcRoof は無変更・Engine 契約に触れない）：** eave_length は Primary Variable のままだが、実体は **Roof Edge graph の Projection**。P_footprint が footprint polygon の Projection Result であるのと同じ再理解。**これは Engine の変更ではなく、既存 Variable が Geometry Runtime に整合的に載る確認**（Graph 抽象が既存工種と衝突しない Evidence の一つ）。

## 3. Face の一般化（Observation・未昇格）

Polygon Face 契約：`{ id, boundary(host_segment), height_range }`。
屋根面（roof surface）も **boundary は host_segment で不変**、`height_range` の代わりに **slope-plane（勾配・基準面）** を持つ。**boundary(host_segment) 部分は invariant**、可変なのは面属性のみ。
→ Face 一般化（wall＝height_range／roof＝slope-plane、boundary は共通）は妥当に見えるが、**実証は Downspout 以降**（Face が drainage area の母集合になるため、Node ステップで自然に検証される）。今は Observation。

## 4. 本丸：Downspout Node（Graph 位相の核・Vertex→Node 移行）

ここが Vertex→Node 移行の実体。**Roof Edge だけでは Graph を実証したことにならない**理由がここ。§4 は問いの設定、§4.5 が本更新での契約レベル確定。

- **仮説A（mid-segment 問題）：** 竪樋（落し口）は eave ラン**中間**に付きうる（既存 Vertex でない点）。この点を (a) Segment を分割する新 Vertex とするか、(b) host_segment＋パラメータ t で参照する Projection ノードとするか。
- **仮説B（drainage 意味の帰属）：** Node は排水方向・集水面積という**意味**を持つ。これは Geometry か。**Material 境界の類推**（`Material は Geometry ではない ＝ Material Projection`・Clarification LOCKED）から、**drainage 意味も Geometry ではなく "Drainage Projection"** が有力仮説。
- **判定基準：** Node Identity が Vertex Identity と**同型（0-cell として同じ契約）**か、**別 Identity（連結性を担う新種）**か。

## 4.5 Downspout Node ADR — Candidate 契約（契約レベル演繹・`文書`段階）

> **状態：Candidate（Observation 未満・LOCK 遠く）。** これは今野の実測ではなく、**LOCKED 契約（Material Projection／Opening.boundary／Face.boundary(host_segment)／Geometry Change Policy／Identity Generation Rules）からの演繹**。Finding 1〜3 と同じ `文書` 段階の確定であり、`実証` は今野屋根伏図＋竪樋位置で行う（§5・ブロッカー不変）。**Contract → Evidence → Validation の順序を守り、先に契約を固定する。**

### 4.5.0 なぜ先に契約を固定するか（開発規律）

Geometry Runtime も Applicability Layer も「Runtime Contract／責務を先に固定 → Evidence で実証」の順で作った。Downspout Node も同じ。**先に実トレースすると図面に引っ張られ「今野邸専用の設計」に堕す危険がある。** ここでは Node の責務を契約として固定し、今野は「この契約で表現できるか」を検証する Evidence に徹させる。順序を崩さない：`Contract → Evidence → Validation`。

### 4.5.1 仮説A（mid-segment 問題）の判定 → **(b) host_segment + t を採用**

**判定：(b)。** LOCKED 契約からの演繹：

- **Geometry Change Policy（LOCK）**：「Model 再生成は Definition 変更のときだけ／Projection・Reconcile では Model を変更しない」。竪樋という**排水金物の都合**で eave Segment を分割すれば、屋根の幾何は何も変わっていないのに Canonical Geometry Model（Vertex 追加・Segment の from/to 変化）を書き換えることになり、**Policy 違反**。
- **Identity Generation Rules（LOCK・Rule 4）**：「同一 Geometry 判定なら Identity 維持」。分割すると同じ軒先線の SegmentID が割れ、Projection・Persistence・比較が崩れる。**竪樋の有無で SegmentID が変わってはならない。**
- **既存契約に (b) の機構が既にある**：`Opening : id, boundary, schedule_ref` と `Face : id, boundary(host_segment), height_range` は、いずれも **host を分割せずに参照する**。Downspout Node が host_segment を t で参照する形は**これと同型**で、新契約を要しない。

> **Finding 4（契約レベル確定）：Downspout の取り付け点は Canonical Vertex ではない。host_segment ＋ t で参照する Projection ノードであり、Opening.boundary / Face.boundary(host_segment) と同型。Segment 分割（Model 改変）はしない。**

### 4.5.2 仮説B（drainage 意味の帰属）の判定 → **Drainage Projection（Geometry ではない）**

**判定：Drainage Projection。** Material 境界（LOCK）からの演繹：

- 「Geometry Runtime owns geometry only. Material assignment は Geometry の外＝Material Projection」。排水（方向・集水面・落し口の役割）は**幾何ではなく機能／意味**。Material と同型に、**Geometry ではなく Drainage Projection** に属す。

> **Finding 5（契約レベル確定）：Drainage（方向・集水面・排水役割）は Geometry ではない。Material Projection と対になる Drainage Projection に属す。Canonical Geometry graph が持つのは Vertex ＋ Segment のみ。**

### 4.5.3 判定基準（Node Identity）→ **新 Geometry Identity は不要（第3の答え）**

§4 の判定基準は「Node Identity が Vertex Identity と同型か、別 Identity か」だった。演繹の帰結は**どちらでもない、より強い第3の答え**：

- **Downspout Node は Geometry Identity を発番しない。** 幾何グラフの 0-cell は **degree-agnostic な Vertex のまま（Finding 2）**で、屋根の連結（軒先↔けらば↔隅棟）は既に**共有 Vertex** が担う。竪樋は Segment 上の**金物（fixture）**であって、Segment 同士の**接合点ではない**。
- したがって Vertex→Node 移行は「Geometry が新 Identity を生やすか」ではなく、**「Geometry は新 Identity を要しない／Node は Drainage Projection 要素」**として解決する。**これは topology-independence の最強形**：本丸と見えた Downspout Node が、幾何層を一切拡張しない。

> **Finding 6（契約レベル確定・中心仮説への第2 Evidence）：Downspout Node は新 Geometry Identity を要しない。幾何グラフは Vertex＋Segment のみで閉じ、Node は host_segment を参照する Drainage Projection 要素。中心仮説「Canonical Geometry は topology-independent」への contract-level Evidence が Finding 1/2 に続き2つ目。ただし昇格は今野実証後。**

### 4.5.4 Downspout Node の契約（Candidate）

各層の Canonical は「Evidence から得る・派生しない事実」だけを持ち、残りは Projection で導く（Geometry の最小契約と同じ規律）。

```
[Drainage Canonical（Evidence・記録する）]
DownspoutNode : id, host_segment, t          // 落し口の同一性と位置（host 参照）
                                             // 位置は設計者が決める Evidence（屋根伏図/竪樋マーク）
                                             // ＝ Opening が schedule_ref を持つのと同型の「記録された金物」

[Drainage Projection（派生・保存しない）]
  drains_faces[]   … 集水する Roof Face 集合（屋根勾配・谷から導出）
  flow_direction   … 排水方向
  gutter_run       … その落し口が受け持つ軒樋区間
  ── Quantity Projection ──
  gutter_length / downspout_count / drainage_area   // ← 数量。保存しない
```

- **Canonical/Projection の二重の読み（用語の締め・レビュー 2026-07-28 小野）：** **DownspoutNode は Canonical Geometry に対しては Drainage Projection 要素である**（幾何 Model の外・host_segment を参照するだけ＝Finding 6）。**一方、Drainage 層の内部では、Evidence から記録される非派生の Canonical State として扱う**（＝上の `[Drainage Canonical]`）。両者は矛盾しない——「対 Geometry では Projection／Drainage 層内では Canonical」という二視点であり、実体の設計は同じ。実証で Drainage 層を実際に組む時、`Canonical`／`Projection` の呼び方で混乱しないための線引き。
- **Runtime が保持するのは `{ id, host_segment, t }`（＋ evidence_quality）だけ。** 集水面・方向・長さ・本数はすべて Projection Result（Model から生成・非保存）。「Quantity すら Projection」（WALL v6）と一致。
- **Edge ↔ Node 接続条件：** DownspoutNode は host eave Segment を**1本**参照し、位置 t∈[0,1]（端点に載る場合は当該 Vertex を参照）。**軒先ラン間の連結は既存の共有 Vertex が担い、Node は担わない**（Node は接合点ではなく金物）。
- **Roof Face との関係：** `drains_faces` は Face（roof surface・boundary(host_segment)＋slope-plane）から**導出される Projection**。Face 一般化（§3）はこの導出で自然に検証される。
- **将来の観測点（Observation・今は採用しない／レビュー 2026-07-28 小野）：** 寄棟・谷・複雑屋根では、`host_segment` **一本だけ**では「その落し口が**どの排水ランに属するか**」が不足しうる。そのとき `host_run`（受け持つ軒樋ランの参照）あるいは `host_face`（集水面の参照）という host 粒度が要る可能性がある。**現時点は host_segment で十分**——LOCK も追加もしない。**今野の寄棟・谷で実データ Evidence が出たら見る**観測点として一行だけ残す（§7 に再掲）。この場合も追加されるのは Drainage 側の参照であって、Geometry Model（Vertex/Segment）は不変（Finding 4/6 と矛盾しない）。

### 4.5.5 独立性の宣言（責務境界）

- **Quantity から独立：** 契約に gutter_length / downspout_count / drainage_area を持たない（すべて Projection）。
- **Material から独立：** 竪樋の製品・色・材質は Material Projection。契約に材料を持たない。
- **Geometry Identity から独立：** VertexID も新 NodeID も発番しない。既存 SegmentID を参照するだけ（「Projection は Identity を参照し、生成しない」＝Identity Generation Rules Rule 2 と一致）。

### 4.5.6 実証（今野・Step2）で確かめること（すべて pending・演繹では埋められない）

契約は固定した。今野は「この契約で本当に表現できるか」だけを検証する Evidence：

- 今野の各竪樋が **mid-segment か既存 roof vertex 上か**（実測・Finding 4 が現物で成立するか）。
- 排水連結（どの軒先ランがどの落し口へ／集水 Face のグルーピング）が、**幾何層に Node を足さず Drainage Projection だけで表現できるか**（Finding 6 の本試験）。
- 接続条件が host_segment 参照だけで足りるか（谷・寄棟での集水合流に geometry-node が要らないか）。**ここで §4.5.4 の観測点＝`host_run`/`host_face` が要るかどうかも同時に判明する**（host_segment 一本で排水ラン帰属が決まらなければ観測点が発火）。
- evidence_quality＝`manual_from_pdf`、DXF 入手で `cad_verified`（Model 値・Identity 不変＝Geometry Change Policy）。

### 4.5.7 昇格経路（Contract → Evidence → Validation）

```
Candidate（本節・契約レベル演繹／今）
   ↓  今野で Acceptance 4点（§6 に Downspout 行を追加）
Observation（実データで破綻しないことを確認）
   ↓  複数棟 or DXF で再現
LOCK（Geometry Runtime＝topology-independent を §7 で昇格）
```

> **Evidence First：今野の竪樋マーク（各隅・平面図に既載）と屋根伏図をトレースして初めて Candidate → Observation。** 演繹は契約を固定しただけで、実データ実証の代わりにはならない。

## 5. 必要 Evidence（次アクションのブロッカー・不変）

- **要るもの：** 今野邸の**屋根伏図**＋**竪樋（縦樋）位置**。竪樋マークは今野平面図に既載（HANDOFF §1.5・calcRoof 資産）。
- **制約：** `project_read` はテキストのみでラスタ展開不可。プロジェクト同梱の `立面図0622.pdf` は 4 面立面（軒高は取れるが伏図位相は取れない）。**屋根伏図の位相トレースには、図面フォルダ接続／屋根伏図の再添付／DXF のいずれかが必要**（Wall の footprint トレースと同じ制約）。
- **受領後：** Downspout Node を実測 → §4.5.6 を Evidence で判定（Candidate 契約が現物で成立するか）→ Connectivity → Graph へ。evidence_quality は `manual_from_pdf`、DXF 入手で `cad_verified` 昇格（Model 値・Identity 不変＝Geometry Change Policy）。

## 6. 現時点の Acceptance

### 6.1 Roof Edge Identity 範囲（契約レベル・2026-07-25）

| 基準 | 判定 | 根拠 |
|---|---|---|
| Completeness | ✅（契約レベル） | Roof Edge を Segment として過不足なく表現可（新フィールド不要） |
| Consistency | ✅（契約レベル） | Vertex/Segment 契約無改訂で参照解決・degree 制約に非依存 |
| Determinism | ◐ | edge type は Face 隣接から決定的導出（Face が要る）。**実データ（今野屋根伏図）での再現トレースは未実施** |
| Projection Fidelity | ✅ | eave_length = Σlength(type=eave) が Model を忠実射影（P_footprint と同型） |

### 6.2 Downspout Node 範囲（Candidate 契約・実データ実証は pending・2026-07-28）

| 基準 | 判定 | 根拠 / 実証で確かめること |
|---|---|---|
| Completeness | ◐（契約レベルのみ） | `{id, host_segment, t}` で落し口を過不足なく表現可（演繹）。**今野の全竪樋が欠落なく載るか＋host 粒度が足りるか（§4.5.4 観測点）は未トレース** |
| Consistency | ◐（契約レベルのみ） | host_segment 参照・新 Identity 不要（Finding 4/6）。**参照が全解決するかは実データ未確認** |
| Determinism | ✕（未実施） | **今野屋根伏図＋竪樋位置のトレース待ち**（Node 位置が同一入力から同一に決まるか） |
| Projection Fidelity | ✕（未実施） | drains_faces / gutter_run / 数量 が Model＋Node を忠実射影するか（Drainage Projection だけで排水連結を表せるか＝Finding 6 本試験） |

> **正直な線引き：** Finding 1・2・3・**4・5・6** は **LOCKED 契約からの演繹（`文書` 段階の確定）**。Polygon で契約レベルが先に固まったのと同じ強さ。**しかし実データ実証（`実証` 段階＝今野屋根グラフを実際にトレースし、フィールド欠落ゼロ・新種 Identity 不要・Drainage Projection だけで排水連結が表現できることを確認）は未了。** Candidate 契約はここを Node/Downspout 実測で埋めて初めて Observation、複数棟/DXF で LOCK。

## 7. 保留 Observation（Canonical にも Principle にも書かない・会話/本書に保持）

- 「Polygon は一つの位相、Graph は別の位相。Canonical Geometry は topology-independent であるべき」（HANDOFF §1.5 由来）— §2 の Finding 1/2 と §4.5 の Finding 4/5/6 で **contract-level Evidence を2つ得た**が、**Node/Downspout の実データ実証が通るまで昇格しない**。
- Downspout/drainage ＝ Drainage Projection（Material Adapter と対）仮説 — §4.5.2 Finding 5 で**契約レベルは確定（Candidate）**。実データ判定は §4.5.6。
- Face 一般化（wall=height_range／roof=slope-plane・boundary 共通）— §3、Node ステップ（drains_faces 導出）で自然検証。
- Downspout Node contract `{id, host_segment, t}` が Opening と同型（記録された金物・host 参照・数量は Projection）— §4.5.4。Material Adapter が v7 で正式化する際、**Drainage Adapter も同じ列**で扱う候補。
- **Downspout Node の host 参照粒度（レビュー 2026-07-28・小野）**— 寄棟・谷・複雑屋根で `host_segment` 一本では「どの排水ランに属するか」が不足しうる。将来 `host_run` / `host_face` が要る可能性の**観測点**（§4.5.4）。**今は host_segment で十分・LOCK も追加もしない。** 実データ（今野の寄棟・谷、§4.5.6）で Evidence が出たら判断。要るとしても追加は Drainage 側の参照で、Geometry Model は不変。

**Not adopted / Not locked yet.** これらは Gutter が Graph 位相で実際に動いてから（Candidate → Observation → LOCK）、ENGINE_PRINCIPLES 昇格（Geometry/Identity/UI Projection の外壁実証後昇格と同じ列）で一括判断する。今は実証を優先し、版も原則も上げない。

## 関連
- `WALL_QUANTITY_EXTRACTION.md`（Canonical Geometry Ledger／Identity Generation Rules／Geometry Change Policy／Material 境界 — 本書 §4.5 の演繹はすべてこの LOCKED 契約に依拠）
- `PHASE3_HANDOFF.md`（§1.5 Next Runtime Validation Candidate・Plan／§8 手順）
- `GAISAN_APPLICABILITY_LAYER.md`（§5.3 の「Applicability も Projection の一種」は本書の Drainage Projection と兄弟＝`Canonical → Projection → Runtime` 系列）
