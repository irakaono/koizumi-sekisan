# geometry_runtime — Roof Edge / Offset Builder（WIP・実証コード）

> **状態（2026-07-28）：** これは Gutter Runtime 検証（`../GUTTER_RUNTIME_VALIDATION.md`）の**作業コード**であって、製品コード（`../index.html`）ではない。数量を作るためではなく、**Roof Edge が Footprint(Canonical Geometry) の Projection として再現できるか**の Evidence を残すためのもの。

## 位置づけ（屋根伏図なしで軒先線を作る）

小泉建設は屋根伏図を作らない。そこで屋根伏図を「読む」のではなく、**footprint（固定済 Canonical Geometry Ledger）を軒の出 d でオフセットして Roof Edge を射影**する：

```
Canonical Footprint（固定）
        │
        ▼  Offset Builder（本フォルダ）＝Geometry Projection の生成器（Recognizer の兄弟）
Roof Edge Candidate
        │
        ▼  type=eave Projection（けらば/妻側を落とす）
Roof Edge Runtime
        │
        ▼
eave_length ほか
```

## ステータス（誤読防止・正確な線引き）

```
Offset Builder v0
  Generation Determinism : validated        # 頂点 convex/concave を Ledger から決定的に導出（出隅6/入隅2 一致）
  Projection Fidelity    : pending          # 「実証成功」ではない。mm 一致は主張しない
  Open Interpretation    : V02 / V06        # 南ガレージ肩・北ポーチ肩の Roof Face 取り合い（自由軒/abut）
  Extraction Protocol §5 : pending          # 屋根伏図ブロッカーの正式解除は②が閉じてから
```

- **Acceptance は「mm 一致」ではなく「既存数量の丸め精度内で一致」。** `calcRoof eave_length=18.8m` は 0.1 丸めなので真値は 18.75〜18.85m。
- 今野で Offset Builder は 18.8m を **±0.20m でブラケット**（footprint=18.20m／両abut=18.60m／両自由=19.00m）。
- **1ビット（V02・V06 が自由軒か abut か）は数量を見ずに屋根ラインから独立判定する**。18.8m に合う方を選ぶのは逆算（fit）なので禁止。判定不能なら `evidence_quality: review / reason: interpretation_required` で止める。

## ファイル

- `ledger_correspondence.py` — 今野 Canonical Ledger の V01–V08 を物理的な角へ写像（座標＋massing のみ・数量不参照）。V02/V06 の Roof Face 取り合いを特定。
- `offset_builder.py` — footprint ⊕ 軒の出 → Roof Edge Candidate → type=eave Projection → eave_length。角寄与をパラメータ化し、シナリオ別に 18.8m と照合する。

## 実行

```
python3 geometry_runtime/ledger_correspondence.py
python3 geometry_runtime/offset_builder.py
```

## 次アクション（②を閉じる条件）

北面・西面立面または2階平面の屋根ライン（V02＝南ガレージ肩／V06＝北ポーチ肩）を、**数量を見ずに** `free_eave / abut / indeterminate` に分類 → 確定構成で Offset Builder 実行 → 18.75〜18.85m 帯と照合。通れば `Extraction Protocol` を「footprint＋立面図（軒の出）を第一 Source、屋根伏図は代替」に更新（`GUTTER_RUNTIME_VALIDATION §5`）。
