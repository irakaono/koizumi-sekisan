# KKai 数量エンジン仕様（Engine Interface）

> **ENGINE_SPEC v1.0（LOCKED / 2026-07-18）** — 本仕様は契約として凍結。今後追加する全エンジンはこの契約に従う。変更は後方互換を原則とし、破壊的変更は v2.0 として別途扱う（フィールド追加＝minor、意味変更＝major）。

**目的：** すべての数量エンジン（calcKiso／calcRoof／calcWall …）が従う共通の入出力契約を1枚に固定する。これを先に決めることで、エンジン追加時に迷わず、コアロジック（`tradeGenka`／`gaisanCompute`）を一切触らずに拡張できる。対応実装：Ver0.4.3（ENGINE_MAP方式・kiso／roof）。契約バージョン：**v1.0（LOCKED）**。

## 位置づけ

本仕様は **Engine が「何を返すか」（EngineResult 契約）のみ**を定める。**アーキテクチャの層構造（`Variables → Engine → Trade → UI`）と設計思想は `ENGINE_PRINCIPLES.md` を正典とする**（責務分離：層構造の定義は1か所に固定）。責任分界だけ再掲すると、KCP は Variables まで、KKai は Engine から下（EngineResult）に責任を持つ。

> 注：本節の層図を ENGINE_PRINCIPLES へ移設したのは **Documentation Correction**（説明図の集約）であり、EngineResult 契約のフィールドには一切触れていない。v1.0 の LOCK は保たれる。

## 登録方法（2ステップ・コアの if は増やさない）
1. **JSON**：対象工種に `"quantity_engine":"roof"` を追加。
2. **JS**：`calcRoof` を実装し `ENGINE_MAP` に登録。

## エンジン契約（インターフェース）
### シグネチャ
```js
ENGINE_MAP[name] = function(trade, ctx) => EngineResult
```

### 入力
| 引数 | 内容 |
|---|---|
| `trade` | 工種オブジェクト（no, name, category, cost_per_tsubo, quantity_engine …） |
| `ctx` | 概算コンテキスト：`ensho_tsubo`（延床坪）、`shape`（建物形状）、`settings`（諸経費率・目標粗利・安全係数）、`variables`（A, P, 屋根面積, 軒先長 … 取得不能はnull） |

### 出力 EngineResult
| フィールド | 型 | 意味 | 現状 |
|---|---|---|---|
| `genka` | number | 工種の概算原価（円） | 実装済 |
| `qty` | bool | 数量が実際に効いたか（「数量」バッジ表示） | 実装済 |
| `basis` | string | 根拠（使用した式・モデル名） | 実装済(Ver0.4.3) |
| `used` | object | 使用した変数と値（例 `{A:62.3}` `{eave_length:18.8}`） | 実装済(Ver0.4.3) |
| `fallback` | bool | 坪単価にフォールバックしたか | 実装済(Ver0.4.3) |
| `confidence` | number(0–1) | この工種原価をどれだけ信用してよいか（KCPの`score`に相当） | 実装済(Ver0.4.3) |

`genka` 以外が無くてもコアは動く。KCPの Result Envelope `{value, score, reason, status}` と整合する（genka=value、confidence=score、basis=reason、fallback/qty=status系）。

### 変数選択の自由（LOCKED）
Engine は Variables のうち**利用する変数を自由に選べる**。`Variables`＝取得できた事実、`Engine`＝現時点で採用する式。取得したが使わない変数があってよい（Evidence First）。採用変数はデータ量で見直す前提で、`variables` には取得した全数量を残す。

### フォールバック規約（LOCKED）
- `quantity_engine` が無い／`ENGINE_MAP` に未登録 → **坪単価** `cost_per_tsubo × 延床`。
- 必要な変数（数量）が未取得 → **坪単価にフォールバック**（`fallback=true`）。
- **「数量が無くても必ず動く」ことを全エンジンが保証する**（プラン初期でも壊れない）。積算システムは「数量が足りません」で止まりがちだが、KKaiは必ず見積りを出す。これはKKaiの強み。

## 全体信頼度（Confidence）
各エンジンは `confidence`（0–1）を返す。数量の質で決まる社内向けの指標で、**顧客提示用ではなく「どこを実測に置き換えると精度が上がるか」を判断する材料**。

**目安：**

| 原価の出どころ | confidence 目安 |
|---|---|
| 実測数量 × 数量モデル | 0.90〜0.95 |
| 自動推定数量 × 数量モデル | 0.78〜0.88 |
| 坪単価フォールバック（数量なし） | 0.55〜0.65 |

**全体信頼度** ＝ 各工種 `confidence` を原価で加重平均。例：基礎0.95／屋根0.82／外壁0.74 … → 見積全体「Confidence 87%」。低い工種＝実測に置き換える優先度が高い工種、と一目で分かる。原価加重なので、金額影響の大きい工種を優先して確認できる。

## 実装例
### calcKiso（実装済・基礎）
- 変数：A（基礎面積㎡）。延床×形状比で自動推定、実測で上書き可。
- 式：`genka = F + a×A`（F=1,366,743／a=2,897・n=4暫定）。
- A未取得 → 坪単価フォールバック。
- 戻り：`{ genka, qty, basis, used, fallback, confidence }`。

### calcRoof（実装済・Ver0.4.3）
- **樋・屋根工事は広い工種（RoofEnvelope：屋根材＋樋＋軒先換気＋雪止＋破風＋水切＋役物）**。相関は工種構成に依存する点に注意。
- 変数：`roof_area`／`eave_length`／`ridge_length`／`gable_length` を**すべて取得・保持**。
- 採用式：`genka = F + a×eave_length`（F=212,823／a=50,478・n=4暫定）。4棟で軒先長が最も説明力が高い（単相関0.98＞屋根面積0.87）。屋根面積・棟・ケラバは保持のみ（現モデル未使用）。
- **再評価条件：~20棟集まった時点で屋根面積・軒先長・複合モデルを再比較**（棟形状の多様性が増えると相関が変わりうるため）。
- eave未取得 → 坪単価フォールバック。戻り：`{ genka, qty, basis, used, fallback, confidence }`。

## Phase の進め方（各工種共通）
1. 4棟（今野・安原・小峰・村田）の当該工種の原価と数量を同一ルールで抽出。
2. 数量と原価の相関分析（単相関→最小二乗）。過学習を避け、係数が物理的に妥当かを確認。
3. 説明力のある最小モデル（固定費＋1数量程度）を採用。変数は欲張らない。
4. `calcXxx` を実装し `ENGINE_MAP` へ登録＋JSONに `quantity_engine`。

## バージョン・ガバナンス（v1.0 LOCKED）
- 本契約は **v1.0 として凍結（LOCKED）**。Ver0.5・Ver1.0 と進んでエンジンは増えても、**契約は変えない**のが原則。
- EngineResult のフィールド追加は後方互換（minor）。破壊的変更（既存フィールドの意味変更・削除）は **v2.0** として別途合意のうえ行う。
- まず契約を固定し、実装は後から揃える（Scope First）。これにより、KKaiは「エンジンは増えるが契約は不変」という強い基盤になる。
