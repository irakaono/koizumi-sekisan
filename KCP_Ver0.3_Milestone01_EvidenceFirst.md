# KKai Project Studio — Architecture Specification
**Version:** 0.1.0  
**Date:** 2026-07-22  
**Author:** 小野哲也（株式会社小泉建設）× Claude（Anthropic）

---

## 1. ビジョン

> **「Excelを読む」ではなく「案件を開く」**

KKai Project Studioは、公共工事における見積・実行予算・変更協議・ANDPAD投入を  
一つの案件（Project）として統合管理するためのWebアプリケーションである。

単なるExcel変換ツールではなく、**ANDPAD運用の設計・検証・履歴管理環境**として機能する。

---

## 2. コアコンセプト

```
KKai Project Studio
│
├── Project（案件）        ← すべての中心
│     ├── Rule Package    ← この案件のルールセット
│     ├── Simulator       ← ANDPADでの見え方をリアルタイム確認
│     ├── Validator       ← 投入前チェック（4カテゴリ）
│     ├── Change Manager  ← 変更履歴（Revision管理）
│     └── Export          ← ANDPADインポートExcel出力
│
└── Rule Library           ← 会社・工種別の再利用可能ルール集
```

### 原則
1. **Project First** — あらゆる操作は案件に紐付く
2. **Simulate Before Import** — ANDPADに投入する前に必ずシミュレーション
3. **Evidence First** — 変更は必ず履歴として残る
4. **Rule Reuse** — 学習したルールは次の案件で使い回す

---

## 3. プロジェクト構造

```
Project
├── meta.json              案件情報（工事名・工期・元請・現場住所など）
├── rules/
│   ├── folder_rules.json  フォルダマッピングルール
│   ├── item_rules.json    明細変換ルール（IF/THEN）
│   ├── profit_rules.json  粗利ルール
│   ├── import_rules.json  インポートフォーマットルール
│   └── validator_rules.json バリデーションルール
├── sources/
│   └── *.xlsx             取り込み元Excel（業者見積・内訳書など）
├── revisions/
│   ├── rev001.json        Revision 1（初版）
│   ├── rev002.json        Revision 2（変更①）
│   └── ...
└── exports/
    └── *.xlsx             出力済みANDPADインポートファイル
```

---

## 4. モジュール定義

### 4-1. Project Manager
| 機能 | 説明 |
|------|------|
| 案件新規作成 | 工事名・工期・発注者・元請などのメタ情報入力 |
| 案件一覧 | 過去案件の一覧・検索・開く |
| 案件エクスポート | 案件全体をZIPで保存 |
| 案件インポート | 過去案件の読み込み・引き継ぎ |

### 4-2. Rule Package
ルールは単一JSONではなく**パッケージ**として管理する。

```json
{
  "package": "koizumi_public_works_v1",
  "version": "1.2.0",
  "description": "小泉建設 公共工事標準ルール",
  "rules": {
    "folder": "folder_rules.json",
    "item": "item_rules.json",
    "profit": "profit_rules.json",
    "import": "import_rules.json",
    "validator": "validator_rules.json"
  }
}
```

#### Folder Rules（IF/THEN形式）
```json
{
  "rules": [
    {
      "id": "sign_kiso_ari",
      "description": "基礎あり設置 → 外構/サイン基礎",
      "conditions": [
        { "field": "gyoshu", "op": "eq", "value": "サイン施工" },
        { "field": "has_kiso", "op": "eq", "value": true }
      ],
      "action": {
        "folder1": "外構",
        "folder2": "サイン基礎",
        "folder3": "{{sign_no}}"
      }
    },
    {
      "id": "sign_kiso_nashi",
      "description": "基礎なし設置 → サイン/図面番号/設置",
      "conditions": [
        { "field": "gyoshu", "op": "eq", "value": "サイン施工" },
        { "field": "has_kiso", "op": "eq", "value": false }
      ],
      "action": {
        "folder1": "サイン",
        "folder2": "{{sign_no}}",
        "folder3": "設置（基礎なし）"
      }
    }
  ]
}
```

### 4-3. ANDPAD Simulator
ANDPADの実際の画面に近いUIでフォルダツリーを表示。

- **Folder Explorer**（左ペイン）: Windows Explorer型ツリー
- **Item List**（右ペイン）: 選択フォルダ内の明細一覧
- **リアルタイム更新**: ルール変更 → 即座にツリーが更新
- **統計パネル**: フォルダ数・明細数・重複・分断・金額合計

### 4-4. Validator（4カテゴリ）
```
Folder Validation  : 重複・分断・並び順・空フォルダ・子フォルダ重複
Item Validation    : 明細名なし・数量0・単価0・負の値
Import Validation  : ANDPAD列数・列名・必須列・文字コード・形式
Business Validation: 粗利率異常・金額異常・原価0・フォルダ別金額
```

### 4-5. Change Manager（Revision管理）
Gitに近い概念で変更履歴を管理する。

```
Revision 1  2026/07/09  初版（実行予算インポート）
            + 外構/舗装 26行 ¥16,664,858
            + サイン/サイン材料 54行 ¥2,839,370
            + ... 合計302行

Revision 2  2026/07/20  カイシン外壁 数量調査後変更
            △ 外壁/RC補修 差額追加 +¥172,300

Revision 3  2026/07/22  時計塔 高所作業車を時計塔/撤去へ移動
            ~ 外構/解体 → 時計塔/撤去 1行移動
```

#### Revision データ構造
```json
{
  "revision": 3,
  "date": "2026-07-22",
  "author": "小野哲也",
  "comment": "時計塔 高所作業車を時計塔/撤去へ移動",
  "diff": {
    "added": [],
    "removed": [],
    "modified": [
      {
        "row_id": "row_107",
        "before": { "folder1": "外構", "folder2": "解体" },
        "after":  { "folder1": "時計塔", "folder2": "撤去" }
      }
    ]
  },
  "snapshot": "rev003_snapshot.json"
}
```

### 4-6. Folder Explorer（最優先UI）

```
┌─────────────────────────────────────────────────┐
│ 📁 外構                               163行      │
│   📁 舗装                              26行      │  ← 選択中
│   📁 排水・縁石                         9行      │
│   📁 インターロッキング                 10行      │
│   📁 サイン基礎                         38行     │
│     📁 サイン2                           2行     │
│     📁 サイン11                          2行     │
│                                                   │
│ 📁 サイン                              141行     │
│   📁 サイン材料（北日本産商）            55行    │
│   📁 サイン1                             3行     │
└─────────────────────────────────────────────────┘
         ↕ 分割
┌─────────────────────────────────────────────────┐
│ 外構 › 舗装                                      │
│ ────────────────────────────────────────────── │
│ 1工区 舗装版切断 アスファルト版15cm以下  ¥13,580 │
│ 1工区 アスファルト舗装とりこわし         ¥231,099│
│ 北側入口 路床整正                        ¥200,232│
│ ...                                              │
│                                 計 ¥8,825,027   │
└─────────────────────────────────────────────────┘
```

### 4-7. 学習機能
ユーザーが手動でフォルダを変更した際に、そのパターンをルールとして保存する。

```
「シーリング（PS-2）館名石取付廻り」
  建具 → サイン18/塗装 に変更しました。

  このルールを保存しますか？
  ✓ はい（「PS-2」かつ「館名石」を含む → サイン18/塗装）
  × いいえ
```

---

## 5. データフロー

```
[業者Excel / 内訳書PDF]
        ↓
[Source Parser]      ← 様々な形式のExcelを正規化
        ↓
[Rule Engine]        ← Rule Packageを適用
        ↓
[ANDPAD Simulator]   ← フォルダツリー・Explorerで確認
        ↓
[Validator]          ← 4カテゴリ・全項目チェック
        ↓
   問題なし？ → [Export] → ANDPADインポートExcel
   問題あり？ → Rule修正 → ループ
        ↓
[Change Manager]     ← Revisionとして履歴保存
```

---

## 6. 技術スタック（現在）

| レイヤー | 技術 | 理由 |
|---------|------|------|
| UI | HTML/CSS/JS（Single File） | GitHub Pages対応・依存なし |
| Excel I/O | SheetJS（xlsx.js） | ブラウザ完結 |
| データ保存 | localStorage / JSON | サーバー不要 |
| ルール定義 | JSON | 人間が読める・編集可能 |

### 将来的な拡張
| フェーズ | 追加技術 | 目的 |
|---------|---------|------|
| Phase 2 | IndexedDB | 大容量案件データの保存 |
| Phase 3 | ANDPAD API | リアルタイム差分取得 |
| Phase 4 | AI（Claude API） | PDFからの自動データ抽出 |

---

## 7. ファイル構成（GitHub Pages）

```
irakaono/andpad-estimate-converter/
├── index.html              KKaiトップページ
├── estimate.html           見積インポート変換
├── estimate2.html          粗利設定付き見積変換
├── budget.html             KKai Project Studio（本ファイル）
├── manifest.json           PWA設定
├── icon.png                KKaiアイコン
└── rules/
    ├── andpad_default.json     小泉建設標準ルールパッケージ
    └── andpad_sign.json        サイン工事専用ルール
```

---

## 8. 開発ロードマップ

### Phase 1（現在）✅
- [x] Excel読込・フォルダマッピング
- [x] ANDPADシミュレーター（ツリー表示）
- [x] バリデーター（4カテゴリ）
- [x] Change Manager（Before/After比較）
- [x] Export（見積/実行予算/変更）

### Phase 2（次期）
- [ ] **Folder Explorer**（最優先）
- [ ] Rule PackageのJSON外出し
- [ ] IF/THENルールエディタGUI
- [ ] Revision管理（履歴スタック）
- [ ] 学習機能（ルール自動保存）

### Phase 3
- [ ] Project Manager（案件管理）
- [ ] PDF自動解析（Claude API連携）
- [ ] ANDPAD API連携（差分取得）

### Phase 4
- [ ] Rule Library（会社間共有）
- [ ] 積算OS連携

---

## 9. 命名規則

| 現在の名称 | 正式名称 | 説明 |
|-----------|---------|------|
| budget.html | KKai Project Studio | アプリ全体 |
| Rule Engine | Rule Package | ルールの集合体 |
| Validator | ANDPAD Validator | ANDPAD特化バリデーター |
| Change Manager | Revision Manager | Git的な変更履歴管理 |
| Tree Preview | Folder Explorer | Explorer型UI |
| Simulator | ANDPAD Simulator | ANDPAD投入前シミュレーション |

---

*このドキュメントはKKai Project Studioの設計基準書です。*  
*実装はこの仕様に従い、変更は必ずこのドキュメントを更新してから行う。*
