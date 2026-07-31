{
  "meta": {
    "dict": "shapes",
    "trade": "roof",
    "note": "屋根形状辞典 v2。shapeは『geometryを生成する』。combination_rulesはFaceを追加するルール。",
    "principle": "shape → generate_geometry(Face/Lineを生成) → 各Lineがitem・数量に繋がる。"
  },

  "shapes": [
    {
      "shape": "kirizuma", "label": "切妻",
      "generate_geometry": [
        {"type": "face", "count": 2},
        {"type": "line", "geometry": "mune",     "count": 1},
        {"type": "line", "geometry": "keraba",   "count": 2},
        {"type": "line", "geometry": "nokisaki", "count": 2}
      ]
    },
    {
      "shape": "yosemune", "label": "寄棟",
      "generate_geometry": [
        {"type": "face", "count": 4},
        {"type": "line", "geometry": "mune",     "count": 1},
        {"type": "line", "geometry": "sumimune", "count": 4},
        {"type": "line", "geometry": "nokisaki", "count": 4}
      ]
    },
    {
      "shape": "katanagare", "label": "片流れ",
      "generate_geometry": [
        {"type": "face", "count": 1},
        {"type": "line", "geometry": "mune",     "count": 1},
        {"type": "line", "geometry": "keraba",   "count": 2},
        {"type": "line", "geometry": "nokisaki", "count": 1}
      ],
      "note": "安原様邸。Face1枚。谷・隅棟は生成されない"
    },
    {
      "shape": "hougyou", "label": "方形",
      "generate_geometry": [
        {"type": "face", "count": 4},
        {"type": "line", "geometry": "sumimune", "count": 4},
        {"type": "line", "geometry": "nokisaki", "count": 4}
      ],
      "note": "頂点に集まる。棟なし"
    }
  ],

  "combination_rules": [
    {
      "rule": "shu_plus_geya",
      "label": "主屋 + 下屋",
      "action": "add_face",
      "effect": "下屋Faceが主屋Faceと内側で接続 → tani(谷)Lineが生成される",
      "generated_line": {"geometry": "tani", "count": "接続数による", "score": 68, "status": "review",
                          "reason": "主屋・下屋の取り合いから谷を検出。本数は屋根伏図の確認要"},
      "note": "shape単独では判定できない。Faceの追加で幾何が変わる例。これがcombination_rulesの本質"
    }
  ]
}
