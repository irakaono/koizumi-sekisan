<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Ver0.4 Phase2 屋根分析</title><style>:root{--g:#27ae60;--g2:#2ecc71;--ink:#233027;--mut:#6b7c70;--line:#dfeee5;--bg:#f4f8f5;}
*{box-sizing:border-box;} body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,'Hiragino Sans','Yu Gothic UI','Segoe UI',sans-serif;line-height:1.75;}
.wrap{max-width:920px;margin:0 auto;padding:0 20px 80px;}
.hero{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;padding:30px 34px;border-radius:0 0 18px 18px;box-shadow:0 4px 16px rgba(39,174,96,.25);margin-bottom:26px;}
.hero .brand{font-size:12px;letter-spacing:2px;opacity:.9;font-weight:700;} .hero h1{margin:6px 0 0;font-size:23px;font-weight:800;}
.content{background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 40px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
.content h2{font-size:18px;font-weight:800;color:var(--g);margin:32px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line);}
.content h1{display:none;} .content h2:first-of-type{margin-top:4px;} .content p{margin:12px 0;}
.content code{background:#eef6ef;color:#1a5c33;border:1px solid #d6ebde;border-radius:5px;padding:1px 6px;font-family:Consolas,monospace;font-size:.9em;}
.content pre{background:#0f241a;color:#dff5e8;border-radius:10px;padding:16px 18px;overflow:auto;} .content pre code{background:none;border:none;color:inherit;padding:0;}
.content strong{color:#12351f;} .content ul,.content ol{margin:12px 0;padding-left:24px;} .content li{margin:7px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:13px;box-shadow:0 1px 4px rgba(0,0,0,.05);border-radius:10px;overflow:hidden;}
thead th{background:#e8f8ef;color:#12502e;font-weight:700;padding:9px 11px;text-align:right;border-bottom:2px solid #a8dfc0;} thead th:first-child,tbody td:first-child{text-align:left;}
tbody td{padding:8px 11px;text-align:right;border-bottom:1px solid #eef3ef;} tbody td:first-child{text-align:left;} tbody tr:nth-child(even){background:#fafdfb;}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:24px;}</style></head>
<body><div class="hero"><div class="brand">KKai ｜ Ver0.4 Phase2</div><h1>屋根工事の数量分析（calcRoof設計前）</h1></div>
<div class="wrap"><div class="content"><h1>Ver0.4 Phase2 — 屋根工事の数量分析（4棟・calcRoof設計前）</h1>
<p><strong>結論：</strong> 屋根原価は「屋根面積」より <strong>軒先長</strong> で説明できる。最小モデルは <strong>屋根原価 = F + a×軒先長</strong>（1数量＋固定費）。基礎と同じく「固定費＋1数量」で、変数は欲張らない。</p>
<h2>4棟の屋根データ（樋・屋根工事・同一集計）</h2>
<table>
<thead>
<tr>
<th>棟</th>
<th>屋根面積(㎡)</th>
<th>棟長(m)</th>
<th>軒先長(m)</th>
<th>ケラバ長(m)</th>
<th>屋根原価</th>
<th>原価/㎡</th>
</tr>
</thead>
<tbody>
<tr>
<td>今野</td>
<td>77.08</td>
<td>9.4</td>
<td>18.8</td>
<td>16.4</td>
<td>1,207,734</td>
<td>15,669</td>
</tr>
<tr>
<td>安原</td>
<td>57.43</td>
<td>0（片流れ）</td>
<td>12.21</td>
<td>12.21</td>
<td>751,411</td>
<td>13,084</td>
</tr>
<tr>
<td>小峰</td>
<td>146.30</td>
<td>12.0</td>
<td>24.0</td>
<td>49.6</td>
<td>1,402,730</td>
<td>9,588</td>
</tr>
<tr>
<td>村田</td>
<td>65.82</td>
<td>11.3</td>
<td>11.3</td>
<td>15.8</td>
<td>836,585</td>
<td>12,710</td>
</tr>
</tbody>
</table>
<h2>単相関（原価との相関係数）</h2>
<table>
<thead>
<tr>
<th>数量</th>
<th>相関</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>軒先長</strong></td>
<td><strong>0.980</strong></td>
</tr>
<tr>
<td>屋根面積</td>
<td>0.873</td>
</tr>
<tr>
<td>ケラバ長</td>
<td>0.811</td>
</tr>
<tr>
<td>棟長</td>
<td>0.646</td>
</tr>
</tbody>
</table>
<p>軒先長が最も高い。この工種は屋根材だけでなく <strong>樋・軒先換気・破風・広小舞・雪止め・水切など「縁まわりの役物」</strong> を多く含み、それが軒先長に比例するため。今野が面積比で高い（造作庇・破風）のも軒先長なら説明できる。</p>
<h2>モデル比較（最小二乗・4棟）</h2>
<table>
<thead>
<tr>
<th>モデル</th>
<th>係数</th>
<th>最大誤差</th>
<th>判定</th>
</tr>
</thead>
<tbody>
<tr>
<td>① F + a×屋根面積</td>
<td>F=475,672 / a=6,623</td>
<td>−18.3%（今野）</td>
<td>面積だけでは弱い</td>
</tr>
<tr>
<td>② a×屋根面積（固定費なし）</td>
<td>a=11,337</td>
<td>−27.6%</td>
<td>不採用</td>
</tr>
<tr>
<td><strong>④ F + a×軒先長</strong></td>
<td><strong>F=212,823 / a=50,478</strong></td>
<td><strong>+10.3%（安原）</strong></td>
<td><strong>採用候補</strong></td>
</tr>
<tr>
<td>⑤ F + a×面積 + b×軒先長</td>
<td>面積係数≈0</td>
<td>+10.5%</td>
<td>面積は不要</td>
</tr>
<tr>
<td>③ F + a×面積 + b×ケラバ</td>
<td>F,b が負</td>
<td>1%だが過学習</td>
<td>不採用</td>
</tr>
</tbody>
</table>
<h2>採用モデル（Phase2）</h2>
<pre><code>屋根原価 = 212,823 + 50,478 × 軒先長(m)     （n=4暫定）
</code></pre>
<ul>
<li><strong>変数は軒先長ひとつ</strong>。面積を軒先長に置き換えるだけで誤差18%→10%に改善し、2つ目の変数は効かない（Scope First・欲張らない）。</li>
<li>棟長・ケラバは今は使わない（棟長は相関0.65と弱く、ケラバは過学習を招く）。棟数増で明確な改善が確認できたら追加を再検討。</li>
<li>ENGINE_SPEC v1.0 準拠：軒先長は延床＋形状から自動推定→屋根伏図の実測で上書き。未取得なら坪単価にフォールバック。confidence は実測0.9/推定0.8/坪単価0.6の目安。</li>
</ul>
<h2>次のステップ</h2>
<ol>
<li>軒先長の「延床＋形状→自動推定」係数を較正（4棟の footprint と軒先長の関係）。</li>
<li><code>calcRoof(trade, ctx)</code> を実装し <code>ENGINE_MAP.roof</code> に登録、JSONの樋・屋根工事に <code>"quantity_engine":"roof"</code>。</li>
<li>4棟で検証（実測軒先長で±10%以内を確認）。</li>
</ol></div><div class="foot">株式会社小泉建設 ｜ KKai / KCP ｜ 2026-07-18</div></div></body></html>