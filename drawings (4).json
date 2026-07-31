# KCP Ver0.3 Milestone 01：Evidence First

**日付**：2026-07-07
**検証物件**：安原様邸（志木市中宗岡）
**使用図面**：1階平面図・2階平面図・1階電気配線図・2階電気配線図・案内図・矩計図・配置図・立面図

---

## 背景

「図面を入れたら概算見積りが出る」というVer1.0のゴールに向けて、まずGraph Builder（Face/Line/Point生成）を実装しようとした。しかし実装前に、以下の順で設計の見直しが発生した。

1. Method/Operation/Assembly辞典 → Ver2.0へ格上げ（Ver1.0はVariable辞典が先）
2. Variable辞典 → タグはGraph生成の「結果」であり「入力」ではないため、先にBuilding Graph仕様が必要と判明
3. Building Graph仕様書 v1.0を策定・LOCK（`constitution/BUILDING_GRAPH_SPEC.json`）
4. Graphを作ろうとしたが、安原様邸には屋根伏図が存在せず、矩計図・立面図から逆算しようとして数値的な矛盾（軒高6205・棟高6788.3・勾配0.5/10が幾何的に整合しない）に遭遇
5. その矛盾は「Recognizer層が必要」という新たな抽象化の提案を生んだが、これは**実装で詰まった証拠がない推測**だと判断し、いったん停止
6. 代わりに、小野さんの「図面を読む順番」（平面図→立面図→屋根伏図→矩計図。矩計図は納まり確認用で最後に見る）を確認。矩計図からRoofFaceを組み立てる、というアプローチ自体が現場の思考順と逆だったことが判明
7. 「この図面だけで拾えるか／他の図面が必要か／図面だけでは無理」という現場の一次判断があることが分かり、**Drawing Completeness Checker**という発想が生まれた
8. 屋根だけでなく、階段まわり（特に階段下用途：収納/トイレ/PS/点検口）でも同種の情報不足が頻発することを確認
9. 判定対象を「図面の種類」から「Information（実際に図面内に存在する記載）」へ修正。判定ロジックを実装する過程で、「矩計図があるから段数が分かる」「立面図があるから手摺が分かる」という誤判定を2回犯し、実際の図面を見直して自己訂正した
10. この経験から **Rule 0：Evidence First** を策定
11. 「屋根伏図がなくても経験豊富な積算者は概算できる」ことと「情報が揃っている」ことは別問題であるという指摘から、**Information Layer**と**Estimator Knowledge Layer**を分離
12. Estimator Knowledgeは「今必要になったから」ではなく「実務で実際に使った経験則を再利用したいから」登録する、という**登録条件**を確立。屋根面積のEstimator Knowledgeは器（アーキテクチャ）のみ確定し、値は空のまま（Reserved）とした

## 成果物

1. **Rule 0: Evidence First**（`DICTIONARY_EDITING_RULES.json` 内 `editing_workflow.rule_0_evidence_first`）
2. **Estimator Knowledge登録条件**（同ファイル `editing_workflow.estimator_knowledge_registration_condition`）
3. **Information Completeness Checker**（実装済み・動作確認済み。`/home/claude/kcp_v031/information_completeness_v3.py`）
   - 屋根_数量確認：🟡 Review（形状・勾配はEvidenceあり。長さ・面積はmissing）
   - 階段_数量仕上げ確認：🟡 Review（位置のみEvidenceあり。段数・寸法・手摺・仕上材・階段下用途はmissing。階段下用途はhigh_risk）
4. **開発ルール（今回の経験則）**：「新しい層は、実装で詰まった時だけ作る」「実装できているものは、設計を増やさない」

## 明示的に「まだやらない」と決めたこと

- Recognizer層の仕様化（実装の詰まりから生まれた証拠がまだない）
- Operation辞典への「情報収集Operation」（Confirm Roof Plan等）の追加（Ver2.0の範囲）
- 屋根面積のEstimator Knowledge（総2階/切妻/4寸→延床×n、等）の登録（実務で使った実績がまだない）
- Building Graph仕様書の再編集（今回の矛盾はGraph仕様の欠陥ではなく、矩計図の使い方の誤りだったため）

## 次のステップ（未着手）

- Information Completeness Checkerを他工種（外壁・造作収納・キッチン・UB/洗面・建具・外構・電気・給排水・照明）へ展開
- 各Operationの`required_evidence`リストを、小野さんの確認を得て`draft`→`review`→`approved`へ進める
- 一覧表示（🟢🟡🔴のテーブル形式）をKKai側の画面機能として実装するかどうかの検討
