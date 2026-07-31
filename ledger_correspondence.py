# geometry_runtime / Ledger 対応表 — 今野 Canonical Ledger の頂点を物理角へ写像
# 座標＋massing のみ（数量は参照しない）。V02/V06 の Roof Face 取り合いを特定する。
# 詳細: ../GUTTER_RUNTIME_VALIDATION.md §4.5 ／ ./README.md

# Ledger↔図面 対応表：Vertex を物理的な角へ写像（座標＋massingのみ。数量は参照しない）
V = {'V01':(0,0),'V02':(3640,0),'V03':(3640,1365),'V04':(9100,1365),
     'V05':(9100,7735),'V06':(3640,7735),'V07':(3640,5915),'V08':(0,5915)}
loop=['V01','V02','V03','V04','V05','V06','V07','V08']
XMAX=9100; YMAX=7735; MID_X=3640   # garage(西 X<3640) / 主屋(東 X>=3640)

def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def kind(name):
    i=loop.index(name); p=V[loop[i-1]]; c=V[name]; n=V[loop[(i+1)%len(loop)]]
    x=cross(p,c,n); return '出隅' if x>0 else ('入隅' if x<0 else '—')
def compass(x,y):
    ns='南' if y==0 else ('北' if y==YMAX else ('南寄り' if y< YMAX/2 else '北寄り'))
    ew='西' if x==0 else ('東' if x==XMAX else '中(段差X=3640)')
    return ns,ew
def mass(x): return 'ガレージ(西)' if x< MID_X else ('境界X=3640' if x==MID_X else '主屋(東)')

print(f"{'V':4}{'座標(mm)':14}{'種別':6}{'方位':16}{'棟':14}物理的な角 / 取り合い")
notes={
 'V01':'ガレージ 南西外角',
 'V02':'南側の段差出隅＝ガレージ南張り出しのSE肩。取り合い: ガレージ南 ↔ 主屋南(Y=1365セットバック)',
 'V03':'南セットバックの入隅（主屋南西の入り角）',
 'V04':'主屋 南東外角',
 'V05':'主屋 北東外角',
 'V06':'北側の段差出隅＝主屋北西の肩。取り合い: 主屋北(Y=7735) ↔ ポーチ欠き込み(Y=5915)',
 'V07':'ポーチ欠き込みの入隅',
 'V08':'ガレージ 北西外角（ポーチ西）',
}
for name in loop:
    x,y=V[name]; ns,ew=compass(x,y)
    star=' ★' if name in ('V02','V06') else ''
    print(f"{name:4}{str(V[name]):14}{kind(name):6}{ns+'/'+ew:16}{mass(x):14}{notes[name]}{star}")

print("\n★=eave(N/S)側の段差出隅＝自由軒/abut が未確定の2点")
print("Acceptance band: 18.8m(0.1丸め) → 真値 18.75〜18.85m")
print("Builder scenarios:  両abut=18.60(帯外) / 片方自由=18.80(帯内) / 両自由=19.00(帯外)")
