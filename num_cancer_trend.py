import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os 

fig = plt.figure()
ax = plt.axes()

#中文字型
plt.rcParams['font.sans-serif'] = 'PingFang HK'

ax.set_title('全國前五癌症死亡人口趨勢')
ax.set_xlabel('年度')
ax.set_ylabel('死亡人口')
annual_cencer_dt = pd.read_csv('annual_cencer.csv')

# 取得年度欄位array
x = annual_cencer_dt['年度'].array
# print data column名稱
print(annual_cencer_dt.columns)

# annual_cencer_dt['氣管、支氣管和肺癌 '].values 取得氣管、支氣管和肺癌內的值並轉換成陣列
# marker 折線圖點
# marker 折線圖點大小
ax.plot(x,annual_cencer_dt['惡性腫瘤'].values,label='惡性腫瘤',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['氣管、支氣管和肺癌'].values,label='氣管、支氣管和肺癌',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['肝和肝內膽管癌'].values,label='肝和肝內膽管癌',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['結腸、直腸和肛門癌'].values,label='結腸、直腸和肛門癌',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['口腔癌'].values,label='口腔癌',marker='o',markersize=4);

# 畫出來
plt.legend()
plt.show();



