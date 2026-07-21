<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>概算エンジン v0（坪単価法＋安全係数）3棟検証メモ</title>
<style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:900px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;}
.hero h1{margin:6px 0 0;font-size:24px;font-weight:800;line-height:1.35;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:34px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h1{display:none;}
.content h2:first-of-type{margin-top:4px;}
.content p{margin:12px 0;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:'SFMono-Regular',Consolas,monospace;font-size:.9em;}
.content strong{color:#12351f;}
.content ul,.content ol{margin:12px 0;padding-left:24px;}
.content li{margin:7px 0;}
.content hr{border:none;border-top:1px solid var(--line);margin:24px 0;}
.content em{color:var(--mut);}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13.5px;overflow:hidden;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:10px 12px;text-align:right;border-bottom:2px solid #a8dfc0;white-space:nowrap;}
thead th:first-child,tbody td:first-child{text-align:left;}
tbody td{padding:9px 12px;text-align:right;border-bottom:1px solid #eef3ef;white-space:nowrap;}
tbody tr:nth-child(even){background:#fafdfb;}
tbody tr:hover{background:#f2fbf5;}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}
@media print{body{background:#fff;}.hero{box-shadow:none;}.content{border:none;box-shadow:none;}}</style></head>
<body><div class="hero"><div class="brand">KKai VALIDATION ｜ 3棟検証</div><h1>概算エンジン v0（坪単価法＋安全係数）3棟検証メモ</h1></div>
<div class="wrap"><div class="content">
<h1>概算エンジン v0（坪単価法 ＋ 安全係数）3棟検証メモ</h1>
<p>基準棟：今野様邸（原価内訳書より 工種別原価 ÷ 基準延床31.9坪 → cost_per_tsubo）
検証棟：安原様邸・小峰様邸
設定：目標着工粗利30% / <strong>安全係数1.08</strong> / 諸経費固定1,370,000</p>
<h2>実績データ</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th>延床(坪)</th>
<th>実原価</th>
<th>実原価/坪</th>
<th>税抜合計</th>
<th>税込合計</th>
<th>税込調整(値引き)</th>
<th>調整後</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野(基準)</td>
<td>31.9</td>
<td>27,013,747</td>
<td>846,826</td>
<td>37,360,943</td>
<td>41,097,037</td>
<td>−24,817</td>
<td>41,072,220</td>
</tr>
<tr>
<td>安原</td>
<td>22.8</td>
<td>20,268,450</td>
<td>888,967</td>
<td>27,811,581</td>
<td>30,592,739</td>
<td>−9,739</td>
<td>30,583,000</td>
</tr>
<tr>
<td>小峰</td>
<td>33.1</td>
<td>24,138,195</td>
<td>728,590</td>
<td>36,803,986</td>
<td>40,484,384</td>
<td><strong>−6,484,384</strong></td>
<td>34,000,000</td>
</tr>
</tbody>
</table>
<p>※延床坪：今野=木工事31.9坪、安原=建方費22.8坪、小峰=木工事109.52㎡→33.13坪（施工床から換算）。</p>
<h2>検証結果（今野基準の概算エンジン ／ 目標30%・安全係数1.08）</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th>延床(坪)</th>
<th>概算原価(エンジン)</th>
<th>実原価との誤差</th>
<th>素価格(目標粗利ライン)</th>
<th>提示(税込丸め)</th>
<th>素価格を実原価で見た粗利</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野</td>
<td>31.9</td>
<td>27,013,813</td>
<td>±0%</td>
<td>39,961,162</td>
<td>47,480,000</td>
<td>32.4%</td>
</tr>
<tr>
<td>安原</td>
<td>22.8</td>
<td>19,307,678</td>
<td>−4.7%</td>
<td>28,952,398</td>
<td>34,400,000</td>
<td>30.0%</td>
</tr>
<tr>
<td>小峰</td>
<td>33.1</td>
<td>28,055,412</td>
<td>+16.2%</td>
<td>41,449,159</td>
<td>49,250,000</td>
<td>41.8%</td>
</tr>
</tbody>
</table>
<p>※概算原価はcost_per_tsubo方式のため今野で+66円の丸め差（27,013,813 vs 実27,013,747）。</p>
<h2>このエンジンの目的（最重要）</h2>
<p><strong>目的は「原価を当てること」ではなく「粗利を守ること」。</strong>
安原は概算原価19,307,678 vs 実原価20,268,450で約−5%外れているが、素価格ライン（目標粗利）を実原価で見た着地は30.0%ぴったり＝目的達成。
概算精度そのものより、着工粗利の下限を守れるかが評価軸である。</p>
<h2>結論</h2>
<ol>
<li><strong>単棟基準（n=1）の限界を実証。</strong> 原価坪単価は729k〜889k（±約14%）に散らばる。今野基準は安原で−4.7%（良好）だが、小峰で+16.2%外れる。<strong>小峰は坪単価が約14%低かった。原因はSWパネル仕様・ビルトインガレージ構成・工種構成差などが考えられる（現時点では原因候補。工種別分析は未実施で、次段階で行う）。</strong> memoの「n=1では検証にならない」を裏付け。</li>
<li><strong>利益を守るアンカーとしては v0 は機能。</strong> 3棟とも、素価格ライン（目標粗利）まで値引いても実原価ベースの粗利は30%以上（32.4／30.0／41.8）。目標28〜30%を下回った棟はゼロ。概算精度は粗くても、着工粗利の下限確保という目的は達成。</li>
<li><strong>小峰の21.9%は積算ではなく値引き運用が主因、と確定。</strong> 小峰の税抜は34.41%で正しく積算。税込40,484,384を34,000,000へ丸めた<strong>−648万の一括値引き</strong>で21.9%に低下。エンジンなら49,250,000提示（安全係数1.08）。アンカー維持＋値引き抑制で粗利は守れた。</li>
</ol>
<h2>意味づけ：積算ソフト → 経営支援ソフト</h2>
<p>「粗利21.9%の本丸は商談時の丸め値引き」＝積算が悪かったのではなく営業運用が悪かった、を数字で証明した。
KKaiが積算ソフトから経営支援ソフトへ変わった瞬間。
<strong>定義：KKai Ver0.3 は「概算金額を当てるAI」ではなく「利益を守るための概算エンジン」。</strong></p>
<h2>次の一手（基準は平均にしない）</h2>
<p>n=3で平均を取ると偶然に引っ張られるため、平均化はまだ早い。今野を残したまま参照を版管理する。
- <strong>基準の版管理</strong>：現行（今野単独）を <code>reference=n1</code> として据え置き。<code>reference=n3</code> を<strong>別に</strong>作り、いつでも比較できるようにする（n1を上書きしない）。
  将来像：<code>basis/reference_n1.json</code> / <code>reference_n3.json</code> / <code>reference_sw.json</code> / <code>reference_standard.json</code>
- <strong>工種別の誤差分析（V0.4）</strong>：どの工種が坪単価法でぶれやすいか（基礎・木工事・設備）を分解。小峰−</p>
</div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-13</div></div></body></html>