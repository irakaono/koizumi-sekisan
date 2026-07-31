# geometry_runtime / Offset Builder v0 — WIP（実証コード・製品コードではない）
# 状態: Generation Determinism=validated / Projection Fidelity=pending / Open: V02,V06
# 詳細: ../GUTTER_RUNTIME_VALIDATION.md §2.5・§4.5 ／ ./README.md
# 注意: Acceptance は mm一致ではなく「既存数量の丸め精度内(18.75〜18.85m)で一致」。
#       V02/V06 の自由軒/abut は屋根ラインから独立判定する（18.8mに合わせる逆算は禁止）。

# KKai Geometry Runtime — Offset Builder（Roof Edge Candidate 生成器）参照実装 v0
# Canonical Footprint(固定) → Offset(d) → Roof Edge Candidate → type=eave Projection → eave_length
# 今野 Canonical Geometry Ledger（manual_from_pdf・2026-07-25 固定）を入力にする。fitting はしない。

import itertools

# --- Canonical Footprint（固定・mm・原点SW・X東/Y北）---
V = {
 'V01':(0,0), 'V02':(3640,0), 'V03':(3640,1365), 'V04':(9100,1365),
 'V05':(9100,7735), 'V06':(3640,7735), 'V07':(3640,5915), 'V08':(0,5915),
}
loop = ['V01','V02','V03','V04','V05','V06','V07','V08']  # CCW
seg = [('S01','V01','V02'),('S02','V02','V03'),('S03','V03','V04'),('S04','V04','V05'),
       ('S05','V05','V06'),('S06','V06','V07'),('S07','V07','V08'),('S08','V08','V01')]

def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def length(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])  # 直交なのでマンハッタン=実長

# --- 辺の向き分類：ΔY=0→NS面(eave候補)/ΔX=0→EW面(けらば) ---
def orient(a,b):
    d=sub(b,a)
    return 'NS_eave' if d[1]==0 else 'EW_keraba'

# --- 頂点 convex/concave：CCWで左折=convex ---
def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
vkind={}
n=len(loop)
for i,name in enumerate(loop):
    prev=V[loop[i-1]]; cur=V[name]; nxt=V[loop[(i+1)%n]]
    c=cross(prev,cur,nxt)
    vkind[name]='convex' if c>0 else ('concave' if c<0 else 'flat')

print("=== 頂点分類（Ledgerから決定的に導出） ===")
print(" convex(出隅):", [k for k in loop if vkind[k]=='convex'])
print(" concave(入隅):",[k for k in loop if vkind[k]=='concave'])

# --- eave(NS)辺と base 長 ---
eave_segs=[(sid,a,b) for (sid,a,b) in seg if orient(V[a],V[b])=='NS_eave']
base=sum(length(V[a],V[b]) for (sid,a,b) in eave_segs)
print("\n=== type=eave（NS面）辺と base 長 ===")
for (sid,a,b) in eave_segs:
    print(f"  {sid} {a}-{b}  len={length(V[a],V[b])}  面Y={V[a][1]}")
print("  Σ base(eave, d=0) =", base, "mm =", base/1000, "m")

# --- 各 eave 辺の端点：convex(free/abut) or concave(trim) ---
# 端点が convex かつ 隣接が外壁けらば → free overhang(+d)
# 端点が convex だが 段差(garage↔house step)で隣が自由軒でない → abut(0)  ← V02,V06 が該当候補
# 端点が concave → trim(-d)
STEP_CORNERS={'V02','V06'}   # 段差の出隅（自由軒か abut かが未確定＝実証の争点）
eave_ends=[]
for (sid,a,b) in eave_segs:
    for endpt in (a,b):
        eave_ends.append((sid,endpt,vkind[endpt]))
print("\n=== eave 辺の端点（角の寄与判定対象） ===")
for sid,pt,k in eave_ends:
    tag = 'concave-trim' if k=='concave' else ('convex-STEP?' if pt in STEP_CORNERS else 'convex-free')
    print(f"  {sid} @ {pt}: {k} -> {tag}")

def eave_length(d=200, d510_end=None, step_free={'V02':True,'V06':True}):
    """d: 標準軒の出。d510_end: 510mmを与える端点名(or None)。step_free: 段差出隅が自由軒か。"""
    total=base
    detail=[]
    for sid,pt,k in eave_ends:
        dd = 510 if pt==d510_end else d
        if k=='concave':
            total-=dd; detail.append(f"{pt}:-{dd}(trim)")
        elif pt in STEP_CORNERS:
            if step_free.get(pt,False):
                total+=dd; detail.append(f"{pt}:+{dd}(step-free)")
            else:
                detail.append(f"{pt}:0(abut)")
        else:  # convex-free
            total+=dd; detail.append(f"{pt}:+{dd}(free)")
    return total, detail

TARGET=18800
print("\n=== シナリオ（calcRoof eave_length = 18.8m = 18800mm と突き合わせ） ===")
scenarios=[
 ("d=0（footprintそのもの）", dict(d=0)),
 ("d=200 均一・両段差とも自由軒", dict(d=200, step_free={'V02':True,'V06':True})),
 ("d=200・両段差とも abut", dict(d=200, step_free={'V02':False,'V06':False})),
 ("d=200・V02のみ自由軒/V06 abut", dict(d=200, step_free={'V02':True,'V06':False})),
 ("d=200・V06のみ自由軒/V02 abut", dict(d=200, step_free={'V02':False,'V06':True})),
 ("d=200・両自由軒・西南V01を510", dict(d=200, d510_end='V01', step_free={'V02':True,'V06':True})),
]
for name,kw in scenarios:
    val,detail=eave_length(**kw)
    diff=val-TARGET
    print(f"  {name:32s}: {val:6d}mm ({val/1000:.2f}m)  vs18.8m 残差{diff:+5d}mm ({diff/TARGET*100:+.1f}%)")
