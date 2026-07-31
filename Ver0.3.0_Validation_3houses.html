{
  "meta": {
    "dict": "rules",
    "trade": "roof",
    "note": "屋根 数量ルール。Ruleは幾何変換のみ(水平長→実長)。部材はここに登場しない(憲法第2条)。",
    "principle": "Face→Line→Point→Assembly。Ruleは Line の value を変換するだけ。板金化はAssembly段。"
  },

  "slope_extension_table": {
    "label": "勾配伸び率表",
    "formula": "sqrt(10^2 + 勾配寸数^2) / 10",
    "values": {
      "1":1.005,"2":1.020,"3":1.044,"4":1.077,"5":1.118,
      "6":1.166,"7":1.221,"8":1.281,"9":1.345,"10":1.414
    }
  },

  "rules": [
    {
      "rule": "valley_slope_extension",
      "label": "谷Line 勾配伸び",
      "target": "valley_line",
      "transform": "Line水平長 → Line実長",
      "input": ["谷Line水平長", "屋根勾配(主屋)", "屋根勾配(下屋)"],
      "formula": "実長 = 水平長 × 勾配伸び率(勾配寸数)",
      "output": "谷Line.value を実長へ更新(部材はまだ登場しない)",
      "judgment": {
        "同勾配":     {"status":"ok",     "score":95,"reason":"左右同勾配。勾配伸び率で自動算出"},
        "異勾配":     {"status":"review", "score":60,"reason":"主屋・下屋の勾配が異なるため人確認"},
        "屋根伏図なし":{"status":"missing","score":0, "reason":"谷長さが読めない(屋根伏図が必要)"}
      },
      "reusable_for": "この勾配伸びは 隅棟Line・谷Line 等、傾斜方向の全Lineで共通",
      "status": "draft"
    }
  ]
}
