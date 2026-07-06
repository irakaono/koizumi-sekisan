# koizumi-sekisan — 小泉建設 積算プラットフォーム(KCP)

小泉建設の施工判断をデジタル化したプラットフォーム。
積算だけでなく、設計支援・施工管理・品質管理・ANDPAD連携までの共通基盤。

**これはAIの辞典ではなく、小泉建設の辞典です。**
追加するときは「一般的にどうか」ではなく「小泉建設ならどう判断するか」だけを考える。

## 構成

```
constitution/    憲法(不変コア)。第7条で LOCKED。第8条は作らない。
  KCP_CONSTITUTION.json    7条
  result_envelope.json     value/score/status/reason

dictionary/      辞典(知識)。ここを育てるのが今後の仕事。
  geometry/      Face/Line/Point の定義
  shapes/        屋根形状・建物形状 → geometry生成
  methods/       工法選択(現場加工/既製品、金具/釘打ち…)
  operations/    施工動作(measure/install/fasten/seal…)+歩掛/品質/写真/安全/工具
  assemblies/    Line→一式展開(谷・棟・ケラバ…)
  rules/         幾何変換(勾配伸び等)

company_master/  会社マスター(実データ。時期で変動)
  vendors/       協力業者
  materials/     材料単価(毎月改定)
  labor/         人工単価(年1回改定)

domains/         業種別の差分
  housing/       新築住宅(drawings.json, variables.json)
  remodel/       リフォーム(将来)
  public/        公共工事(将来)
```

## 憲法 7条(LOCKED)

1. すべての生成物は Result Envelope(value/score/reason/status)を持つ
2. 建物は Face / Line / Point で理解する
3. Type(定義)と Instance(実体)を分離する
4. 建物は Tree ではなく Graph で表す(Shapeは結果)
5. 積算パイプライン: Drawings→Graph→Shape→Variables→Rules→Assemblies→Method→Operation→Resource→Cost→Estimate→Budget→Purchase→ANDPAD
6. 辞典(知識)と 会社マスター(実データ)を分離する
7. Assembly と Operation の間に Method(工法選択)を置く

**第8条は作らない。** 設計フェーズは完了。以降は辞典を編集するフェーズ。

## フェーズ

- 設計フェーズ … 完了(憲法LOCKED)
- 辞典編集フェーズ … 進行中。Operation・Method・Assemblyを1項目ずつ完成版にしていく
  - 例: Operation No.001 "measure" を完成 → 次 "install" → 次 "fasten" …

## 関連

- KKai (業務ポータル / フロントエンド) … 別リポジトリ。domains/housing の drawings/variables を読む
