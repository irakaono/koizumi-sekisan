{
  "meta": {
    "dict": "geometry",
    "note": "幾何辞典。建物を Face(面)→ Line(線)→ Point(点)で理解する。谷は部材ではなく『屋根面2枚の内側接続線』。",
    "principle": "Face同士の接続がLineを生む。外側接続=隅棟、内側接続=谷。材質に依存しない共通幾何。",
    "why": "shape経由でも、将来のFace直接認識でも、同じgeometryを生成できる。公共のRC屋根・折板も Faceの種類が違うだけ。"
  },

  "face": {
    "label": "屋根面",
    "attributes": ["勾配", "方位", "面積", "外形"],
    "note": "1枚の傾いた屋根の平面。屋根面積・流れ長さの基"
  },

  "line": {
    "label": "線(面と面、または面と端部の境界)",
    "types": {
      "mune":     {"label": "棟",   "born_from": "2面が外側・頂部で接続", "quantifies": "長さ"},
      "sumimune": {"label": "隅棟", "born_from": "2面が外側・下り方向で接続(出隅)", "quantifies": "長さ(勾配伸び)"},
      "tani":     {"label": "谷",   "born_from": "2面が内側で接続(入隅)", "quantifies": "長さ(勾配伸び)"},
      "keraba":   {"label": "ケラバ", "born_from": "面の妻側端部(接続なし)", "quantifies": "長さ"},
      "nokisaki": {"label": "軒先", "born_from": "面の最下端(接続なし)", "quantifies": "長さ"},
      "amaoshie": {"label": "雨押え", "born_from": "面と壁の接続", "quantifies": "長さ"}
    }
  },

  "point": {
    "label": "点(線の端部・交点)",
    "types": {
      "tani_end":     {"label": "谷終点", "note": "谷板金の納まり位置"},
      "mune_cross":   {"label": "棟交点", "note": "棟と隅棟の交点など"},
      "sumimune_top": {"label": "隅棟頂部", "note": "隅棟が棟/頂点に集まる点"}
    },
    "note": "Pointは役物・納まりの数量に効く(将来)"
  }
}
