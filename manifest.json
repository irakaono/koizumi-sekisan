# KKai Project Studio — Data Model
**Version:** 1.0.0 (LOCKED)
**Date:** 2026-07-22
**Status:** Architecture v1.0 — 変更は必ず設計レビューを経ること

---

## 概要

KKai Project Studioのすべてのデータは、この7つのエンティティで構成される。
画面・機能・ストレージ技術がどう変わっても、このモデルは変わらない。

```
Project
 ├── Sources[]       取り込み元ファイル
 ├── RulePackage     ルールセット
 ├── Items[]         処理済み明細行
 ├── Revisions[]     変更履歴
 └── Exports[]       出力済みファイル
```

---

## 1. Project

案件（工事）の最上位エンティティ。すべてはProjectに属する。

```typescript
interface Project {
  id:           string;     // "26008_urawa_godo"  UUID or slug
  name:         string;     // "26008 浦和合同庁舎外構ほか改修工事"
  code:         string;     // "26008"
  client:       string;     // "関東地方整備局"（発注者）
  contractor:   string;     // "株式会社武井工務店"（元請）
  manager:      string;     // "株式会社小泉建設"（管理）
  site:         string;     // "さいたま市浦和区北浦和5-6-5"
  start_date:   string;     // "R8.6.10"
  end_date:     string;     // "R8.10.21"
  created_at:   string;     // ISO8601
  updated_at:   string;     // ISO8601
  status:       ProjectStatus;
  rule_package_id: string;  // 使用中のRulePackage.id

  // 集計（派生値・キャッシュ）
  latest_revision: number;
  item_count:   number;
  total_sekkei: number;     // 設計金額合計
  total_jikko:  number;     // 実行予算合計
}

type ProjectStatus = 'active' | 'completed' | 'archived';
```

---

## 2. Source

プロジェクトに取り込んだ元ファイル。

```typescript
interface Source {
  id:           string;     // "src_001"
  project_id:   string;
  filename:     string;     // "26008_浦和合同庁舎_業種別予算集計.xlsx"
  source_type:  SourceType;
  uploaded_at:  string;     // ISO8601
  uploaded_by:  string;     // "小野哲也"
  sheet_count:  number;
  row_count:    number;
  vendor:       string;     // "北日本産商"（業者名、任意）
  memo:         string;

  // 生データ（正規化前）
  raw_rows:     RawRow[];
}

type SourceType =
  | 'budget_summary'    // 業種別予算集計
  | 'estimate_request'  // 見積依頼書
  | 'vendor_estimate'   // 業者見積
  | 'breakdown'         // 提出内訳書
  | 'andpad_template'   // ANDPADテンプレート
  | 'other';

interface RawRow {
  sheet:    string;
  row_num:  number;
  tekiyo:   string;
  suryo:    number | null;
  tani:     string | null;
  tanka:    number | null;
  kingaku:  number | null;
  biko:     string | null;
  [key: string]: any;   // 追加列
}
```

---

## 3. RulePackage

フォルダ・明細・粗利・バリデーションのルール集合。
現場固有の情報を持たない。

```typescript
interface RulePackage {
  id:           string;     // "koizumi_public_works_v1"
  name:         string;     // "小泉建設 公共工事標準ルール"
  version:      string;     // "1.0.0"
  created_at:   string;
  updated_at:   string;
  author:       string;

  folder_rules:    FolderRule[];
  item_rules:      ItemRule[];
  profit_rules:    ProfitRule[];
  import_rules:    ImportRule;
  validator_rules: ValidatorRule;
  company_rules:   CompanyRule[];
}

// フォルダルール（IF/THEN）
interface FolderRule {
  id:           string;
  priority:     number;     // 小さいほど高優先
  description:  string;
  source:       'manual' | 'learned' | 'default';
  learned_at:   string | null;
  learned_by:   string | null;
  conditions:   Condition[];
  action:       FolderAction;
}

interface Condition {
  field:  string;           // "gyoshu" | "meisho" | "sign_no" | ...
  op:     ConditionOp;
  value:  any;
}

type ConditionOp =
  | 'eq' | 'neq'
  | 'contains' | 'not_contains'
  | 'in_set' | 'not_in_set'
  | 'matches'               // 正規表現
  | 'gt' | 'gte' | 'lt' | 'lte';

interface FolderAction {
  folder1:  string;
  folder2:  string;
  folder3:  string | null;
  folder4:  string | null;
}

// 粗利ルール
interface ProfitRule {
  id:          string;
  description: string;
  conditions:  Condition[];
  gross_rate:  number;      // 0〜99
}

// インポートルール（フォーマット定義）
interface ImportRule {
  mode:     'mitsumori' | 'jikko' | 'henko';
  columns:  string[];       // ANDPADの列名リスト
  qty:      'fixed_1' | 'original';
  unit:     'fixed_shiki' | 'original';
  price:    'amount' | 'unit_price';
  sort:     'folder_order' | 'original';
}

// バリデーションルール
interface ValidatorRule {
  error_on_dup_folder:      boolean;
  error_on_broken_folder:   boolean;
  error_on_no_name:         boolean;
  error_on_negative_qty:    boolean;
  error_threshold_price:    number;   // この金額以上はエラー
  warn_threshold_price:     number;   // この金額以上は警告
  max_gross_rate:           number;
  min_gross_rate:           number;
}
```

---

## 4. Item

RulePackageを適用した後の処理済み明細行。実体データ。

```typescript
interface Item {
  id:           string;     // "item_26008_001"
  project_id:   string;
  source_id:    string;     // どのSourceから来たか
  revision:     number;     // 何番目のRevisionで生成/変更されたか

  // フォルダ階層
  folder1:      string;     // "外構"
  folder2:      string;     // "サイン基礎"
  folder3:      string | null;  // "サイン17"
  folder4:      string | null;

  // 明細
  meisai:       string;     // 明細名
  suryo:        number;     // 数量
  tani:         string;     // 単位
  biko:         string;     // 備考

  // 金額
  sekkei:       number;     // 設計金額（見積金額単価）
  gross_rate:   number;     // 粗利率(%)
  mitsumori:    number;     // 見積金額（sekkei / (1 - gross_rate/100)）
  jikko:        number | null;  // 実行予算単価（null=未決定）

  // メタ
  torihiki:     string | null;  // 取引先名
  memo:         string | null;  // メモ（"仮入力（設計金額）"など）
  created_at:   string;
  updated_at:   string;
}
```

---

## 5. Revision

Itemの変更履歴。Gitのコミットに相当。

```typescript
interface Revision {
  id:           string;     // "rev_26008_003"
  project_id:   string;
  revision:     number;     // 1, 2, 3...
  created_at:   string;
  author:       string;
  comment:      string;     // "カイシン外壁 数量調査後変更"
  tags:         string[];   // ["外壁", "カイシン", "変更協議"]

  // 差分サマリー
  summary: {
    rows_added:     number;
    rows_removed:   number;
    rows_modified:  number;
    rows_moved:     number;
    amount_delta:   number;   // 金額変化（正=増額、負=減額）
    total_after:    number;   // 変更後の合計金額
  };

  // 差分詳細
  diff: {
    added:    ItemDiff[];
    removed:  ItemDiff[];
    modified: ItemDiff[];
    moved:    ItemDiff[];
  };

  // このRevision時点のスナップショット（全Item）
  snapshot: Item[];
}

interface ItemDiff {
  item_id:  string;
  before:   Partial<Item> | null;
  after:    Partial<Item> | null;
}
```

---

## 6. Export

出力済みファイルの記録。

```typescript
interface Export {
  id:           string;     // "exp_26008_003"
  project_id:   string;
  revision:     number;     // どのRevisionを出力したか
  created_at:   string;
  created_by:   string;
  filename:     string;     // "26008_実行予算インポート_最終版v13.xlsx"
  format:       ExportFormat;
  row_count:    number;
  total_amount: number;
  hide_cost:    boolean;
  hide_gross:   boolean;
  memo:         string;
}

type ExportFormat =
  | 'andpad_mitsumori'    // アンドパッド見積インポート
  | 'andpad_jikko'        // アンドパッド実行予算インポート
  | 'andpad_henko'        // アンドパッド実行予算変更
  | 'csv';
```

---

## 7. エンティティ関係図

```
Project (1)
  │
  ├── Source (N)          xlsx / PDF / csv
  │     └── RawRow (N)   正規化前データ
  │
  ├── RulePackage (1)     ルール集合
  │     ├── FolderRule (N)
  │     ├── ItemRule (N)
  │     ├── ProfitRule (N)
  │     ├── ImportRule (1)
  │     └── ValidatorRule (1)
  │
  ├── Item (N)            処理済み明細（RulePackage適用後）
  │     ↑ Source + RulePackage → Item
  │
  ├── Revision (N)        変更履歴
  │     └── ItemDiff (N)  行単位の差分
  │
  └── Export (N)          出力記録
        ↑ Revision → Export
```

---

## 8. ストレージ戦略

### Phase 1（現在）: localStorage
```javascript
// キー設計
'kkai_projects'              → Project[]
'kkai_project_{id}'          → Project
'kkai_sources_{project_id}'  → Source[]
'kkai_items_{project_id}'    → Item[]
'kkai_revisions_{project_id}'→ Revision[]
'kkai_exports_{project_id}'  → Export[]
'kkai_rule_{package_id}'     → RulePackage

// 自社情報（既存）
'kkai_company'               → 会社情報
```

### Phase 2: IndexedDB
大容量データ（Itemが1000行超、Revision履歴が10件超）に対応。

### Phase 3: GitHub / API
案件データをGitHubリポジトリに保存。チーム共有・バックアップ対応。

---

## 9. バージョニング原則

- このDataModelはv1.0.0としてロックする
- フィールドの**追加**は許可（後方互換）
- フィールドの**削除・型変更・名前変更**は禁止（要メジャーバージョンアップ）
- 変更時は必ず`ARCHITECTURE_CHANGELOG.md`に記録する

---

*このドキュメントはKKai Project Studioのデータモデル定義書（v1.0.0 LOCKED）です。*
*実装はすべてこのモデルに準拠すること。*
