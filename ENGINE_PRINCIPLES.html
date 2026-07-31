# KKai Rule Package — 仕様書
**Version:** 0.1.0  
**Date:** 2026-07-22

---

## 1. Rule Packageとは

Rule Packageは、ANDPADへのデータ投入に関わるすべてのルールをまとめた設定ファイル群。  
現場固有の情報を持たず、**工種・業種・条件に基づく変換ロジックのみ**を定義する。

```
rules/
├── package.json          パッケージ定義
├── folder_rules.json     フォルダマッピング（IF/THEN）
├── item_rules.json       明細変換ルール
├── profit_rules.json     粗利率ルール
├── import_rules.json     インポートフォーマット定義
├── validator_rules.json  バリデーション基準
└── company_rules.json    会社固有ルール（発注先マッピング等）
```

---

## 2. folder_rules.json

### 基本構造
```json
{
  "version": "1.0.0",
  "description": "小泉建設 公共工事 フォルダルール",
  "f1_order": ["外構", "サイン", "外壁", "建具", "仮設", "時計塔", "産廃", "その他"],
  "rules": [...]
}
```

### ルール定義（IF/THEN）

各ルールは `conditions`（条件）と `action`（適用するフォルダ）から構成される。

```json
{
  "id": "rule_001",
  "priority": 10,
  "description": "基礎あり設置 → 外構/サイン基礎/図面番号",
  "conditions": [
    { "field": "gyoshu",   "op": "eq",       "value": "サイン施工" },
    { "field": "saimoku",  "op": "eq",       "value": "改修" },
    { "field": "sign_no",  "op": "in_set",   "value": [2,7,11,12,13,15,16,17,23,24,25,26,34,35,36,37,38,39,40,41] }
  ],
  "action": {
    "folder1": "外構",
    "folder2": "サイン基礎",
    "folder3": "サイン{{sign_no}}",
    "folder4": null
  }
}
```

### 条件演算子（op）一覧

| op | 説明 | 例 |
|----|------|-----|
| `eq` | 等しい | `"field": "gyoshu", "op": "eq", "value": "土木"` |
| `neq` | 等しくない | |
| `contains` | 文字列を含む | `"field": "meisho", "op": "contains", "value": "基礎共"` |
| `not_contains` | 文字列を含まない | |
| `in_set` | リストに含まれる | `"field": "sign_no", "op": "in_set", "value": [2,7,11]` |
| `not_in_set` | リストに含まれない | |
| `matches` | 正規表現マッチ | `"field": "meisho", "op": "matches", "value": "PS-2"` |
| `gt` | より大きい | |
| `gte` | 以上 | |
| `lt` | より小さい | |
| `lte` | 以下 | |

### テンプレート変数（action内）

| 変数 | 説明 | 例 |
|------|------|-----|
| `{{sign_no}}` | 看板図面番号 | `サイン{{sign_no}}` → `サイン17` |
| `{{gyoshu}}` | 業種名 | |
| `{{kamoku}}` | 科目名 | |
| `{{chukamoku}}` | 中科目名 | |
| `{{saimoku}}` | 細目名 | |

### 優先度（priority）
- 数値が**小さいほど高優先**（先にマッチしたルールが適用）
- 同一priorityは定義順

---

## 3. item_rules.json

明細の変換ルール（名称補正・備考付与・数量単位正規化）

```json
{
  "rules": [
    {
      "id": "item_001",
      "description": "PS-2シーリング + 館名石 → サイン18/塗装",
      "source": "learned",
      "learned_at": "2026-07-22",
      "learned_by": "小野哲也",
      "conditions": [
        { "field": "meisho", "op": "matches", "value": "PS-2" },
        { "field": "meisho", "op": "contains", "value": "館名石" }
      ],
      "action": {
        "folder1": "サイン",
        "folder2": "サイン18",
        "folder3": "塗装"
      }
    },
    {
      "id": "item_002",
      "description": "数量・単位の正規化（全行1式に統一）",
      "conditions": [],
      "action": {
        "suryo": 1,
        "tani": "式",
        "genka": "{{kingaku}}"
      }
    }
  ]
}
```

---

## 4. profit_rules.json

```json
{
  "default_rate": 30,
  "rules": [
    {
      "description": "外構工事（市川興業）は粗利なし（原価管理のみ）",
      "conditions": [
        { "field": "folder1", "op": "eq", "value": "外構" }
      ],
      "action": { "gross_rate": 0, "mode": "cost_only" }
    },
    {
      "description": "北日本産商材料は粗利25%",
      "conditions": [
        { "field": "folder2", "op": "contains", "value": "北日本産商" }
      ],
      "action": { "gross_rate": 25 }
    }
  ]
}
```

---

## 5. validator_rules.json

```json
{
  "folder": {
    "allow_duplicate_f1": false,
    "allow_duplicate_f2": false,
    "allow_broken_f1": false,
    "warn_out_of_order": true
  },
  "item": {
    "error_on_no_name": true,
    "error_on_negative_qty": true,
    "warn_on_zero_price": true,
    "error_threshold_price": 10000000
  },
  "business": {
    "max_gross_rate": 99,
    "min_gross_rate": 0,
    "warn_large_amount": 1000000,
    "error_large_amount": 10000000
  }
}
```

---

## 6. 学習ルールの保存フロー

```
ユーザーがフォルダを手動変更
        ↓
「このルールを保存しますか？」
        ↓ はい
条件を自動生成（変更前後の差分から）
        ↓
item_rules.json に追記
  "source": "learned"
  "learned_at": "2026-07-22"
  "learned_by": "小野哲也"
        ↓
次回同じ条件の行に自動適用
```

---

## 7. Rule Package 切り替え

```javascript
// 小泉建設標準
loadRulePackage('rules/koizumi_public_works_v1.json');

// サイン工事特化
loadRulePackage('rules/koizumi_sign_works_v1.json');

// 将来：他社標準
loadRulePackage('rules/takei_kensetsu_v1.json');
```

---

*このドキュメントはRule Packageの設計仕様書です。*
