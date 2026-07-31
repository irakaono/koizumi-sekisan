# Change Manager (Revision Manager) — 仕様書
**Version:** 0.1.0  
**Date:** 2026-07-22

---

## 1. 概念

公共工事では変更協議が多い。  
**すべての変更を履歴として残し、変更協議資料として活用できる**ことがゴール。

Gitのコミット履歴に相当するRevisionを積み上げる。

---

## 2. Revision構造

```
Project: 26008 浦和合同庁舎外構ほか改修工事
│
├── Rev.001  2026-07-09  小野哲也  「初版 実行予算インポート」
│   302行  ¥27,677,976
│
├── Rev.002  2026-07-20  小野哲也  「カイシン外壁 数量調査後変更」
│   +1行   +¥172,300
│   合計 ¥27,850,276
│
├── Rev.003  2026-07-22  小野哲也  「時計塔 高所作業車を時計塔/撤去へ移動」
│   ~1行移動  金額変更なし
│
└── Rev.004  （予定）  「市川興業実見積入力後の実行予算更新」
```

---

## 3. Revisionデータ構造

```json
{
  "project_id": "26008_urawa_godo",
  "revision": 2,
  "created_at": "2026-07-20T14:30:00+09:00",
  "author": "小野哲也",
  "comment": "カイシン外壁 数量調査後変更 差額¥172,300追加",
  "tags": ["外壁", "カイシン", "変更協議"],

  "summary": {
    "rows_added": 1,
    "rows_removed": 0,
    "rows_modified": 0,
    "rows_moved": 0,
    "amount_delta": 172300,
    "total_after": 27850276
  },

  "diff": {
    "added": [
      {
        "id": "row_new_001",
        "folder1": "外壁",
        "folder2": "カイシン",
        "folder3": "カイシン（数量調査後変更）",
        "meisai": "RC補修 数量調査後変更 差額",
        "suryo": 1,
        "tani": "式",
        "genka": 172300,
        "jikko": 172300,
        "biko": "ひび割れ処理・爆裂処理・浮き補修追加"
      }
    ],
    "removed": [],
    "modified": [],
    "moved": []
  },

  "snapshot_id": "snap_rev002"
}
```

---

## 4. タイムライン表示

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Rev.001  2026/07/09
  初版 実行予算インポート
  302行追加  合計 ¥27,677,976

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Rev.002  2026/07/20  [外壁] [カイシン]
  カイシン外壁 数量調査後変更
  +1行  △ +¥172,300  合計 ¥27,850,276
  ┌──────────────────────────────────────────┐
  │ + 外壁/カイシン/数量調査後変更             │
  │   RC補修 差額  ¥172,300                  │
  └──────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Rev.003  2026/07/22
  時計塔 高所作業車を時計塔/撤去へ移動
  ~1行移動  金額変更なし
  ┌──────────────────────────────────────────┐
  │ ~ 外構/解体 → 時計塔/撤去               │
  │   建設機械（高所作業車）¥32,980          │
  └──────────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 5. 変更協議書への出力

RevisionのタイムラインをExcelまたはPDFに出力。

```
変更協議資料（実行予算変更履歴）
工事名：26008 浦和合同庁舎外構ほか改修工事

変更番号  日付        内容                     金額増減
────────  ──────────  ─────────────────────────  ──────────
第1回    2026/07/20  カイシン外壁数量調査後変更  +¥172,300
第2回    （予定）    市川興業実見積反映          未確定
```

---

## 6. 実装仕様

### localStorage スキーマ
```javascript
// プロジェクト一覧
localStorage.setItem('kkai_projects', JSON.stringify([
  { id: '26008_urawa', name: '26008 浦和合同庁舎', latest_rev: 3 }
]));

// 各Revision
localStorage.setItem('kkai_rev_26008_urawa_001', JSON.stringify(revision001));
localStorage.setItem('kkai_rev_26008_urawa_002', JSON.stringify(revision002));

// 最新スナップショット（全行データ）
localStorage.setItem('kkai_snap_26008_urawa_latest', JSON.stringify(allRows));
```

### Revision作成のトリガー
1. **Export時** — エクスポートするたびに自動でRevision作成
2. **手動保存** — 「Revisionを保存」ボタンを押したとき
3. **フォルダ移動** — Folder Explorerでフォルダを移動したとき

### 差分計算アルゴリズム
```javascript
function calcDiff(before, after) {
  const beforeMap = new Map(before.map(r => [r.id, r]));
  const afterMap  = new Map(after.map(r => [r.id, r]));

  return {
    added:    after.filter(r => !beforeMap.has(r.id)),
    removed:  before.filter(r => !afterMap.has(r.id)),
    modified: after.filter(r => {
      const b = beforeMap.get(r.id);
      return b && JSON.stringify(b) !== JSON.stringify(r);
    }),
    moved: after.filter(r => {
      const b = beforeMap.get(r.id);
      return b && (b.folder1 !== r.folder1 || b.folder2 !== r.folder2);
    })
  };
}
```

---

## 7. 将来拡張

### ANDPAD API差分（Phase 3）
現在ANDPADに入っているデータをAPIで取得し、  
新しいRevisionとの差分をChange Managerで確認してから投入。

```
ANDPAD現状 ←→ Rev.004（新規）
差分確認
  + サイン材料 北日本産商実見積 54行
  △ 外壁 RC補修 ¥356,800→¥529,100
確認後にANDPAD更新
```

---

*このドキュメントはChange Manager（Revision Manager）の設計仕様書です。*
