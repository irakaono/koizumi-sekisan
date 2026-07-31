{
  "meta": {
    "dict": "assemblies",
    "note": "Assembly → Operation → Resource の3層構造。建築積算エンジンの最終形。全工種・全業種共通。",
    "principle": "施工方法(Operation)が必要リソース(Resource)を決める。部材を直接ぶら下げない。",
    "constitution": "憲法 第5条(全業種共通パイプライン)・第6条(辞典/会社マスター分離)に従う"
  },

  "resource_types": {
    "material":    "材料(板金・ビス・シーラー・サイディング・生コン…)",
    "labor":       "人工(板金工・大工・左官・鉄筋工…)",
    "machine":     "機械(ラフター・高所作業車・ポンプ車…)",
    "service":     "役務(ガードマン・交通誘導・産廃処分・運搬…)",
    "subcontract": "外注一式(専門業者への丸投げ工事…)"
  },

  "template": {
    "assembly_type": "longsize_bankin",
    "label": "長尺板金 一式",
    "input": {"from": "Line Instance(実長)", "envelope": "value/score/status/reason を引き継ぐ"},
    "note": "谷・棟包み・ケラバ水切・軒先唐草・雨押えに共通。Operationの有無で必要Resourceが変わる。",

    "operations": [
      {
        "operation": "kakou", "label": "加工",
        "condition": "現場加工の場合のみ。既製品なら skip",
        "resources": [
          {"resource": "加工人工", "resource_type": "labor", "qty": "??? 実長 × 人工/m"}
        ]
      },
      {
        "operation": "mage", "label": "曲げ",
        "condition": "現場加工の場合のみ。既製品なら skip",
        "resources": [
          {"resource": "板金材(平板)", "resource_type": "material", "qty": "??? 実長 × 働き幅補正"}
        ]
      },
      {
        "operation": "toritsuke", "label": "取付",
        "condition": "常に必要",
        "resources": [
          {"resource": "板金本体(既製品時)", "resource_type": "material", "qty": "発注本数(定尺丸め)"},
          {"resource": "ビス", "resource_type": "material", "qty": "??? 実長1mあたり本数。メーカーにより不要な場合あり"},
          {"resource": "取付人工", "resource_type": "labor", "qty": "??? 実長 × 人工/m"}
        ]
      },
      {
        "operation": "setsugou", "label": "接合",
        "condition": "継手がある場合(実長 > 定尺)",
        "resources": [
          {"resource": "ジョイント", "resource_type": "material", "qty": "継手数"},
          {"resource": "シーラー(止水)", "resource_type": "material", "qty": "??? 継手数 × 消費量"}
        ]
      },
      {
        "operation": "seisou", "label": "清掃",
        "condition": "常に必要",
        "resources": [
          {"resource": "清掃人工", "resource_type": "labor", "qty": "??? 一式 or 面積比例"}
        ]
      }
    ],

    "quantity_pipeline": [
      "Line水平長 → 勾配伸び → Line実長 → ラップ加算 → 必要長 → 定尺丸め → 発注本数"
    ],
    "params": {"定尺": "???", "ラップ長": "???", "継手数": "ceil(実長÷定尺)-1"}
  },

  "instances": [
    {"assembly":"tani",       "label":"谷",       "uses":"longsize_bankin", "施工方法":"??? 現場加工 or 既製品"},
    {"assembly":"munetsutsumi","label":"棟包み",   "uses":"longsize_bankin"},
    {"assembly":"keraba",     "label":"ケラバ水切","uses":"longsize_bankin"},
    {"assembly":"nokikarakusa","label":"軒先唐草", "uses":"longsize_bankin"},
    {"assembly":"amaoshie",   "label":"雨押え",   "uses":"longsize_bankin"}
  ]
}
