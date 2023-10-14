import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os 

fig = plt.figure()
ax = plt.axes()

#中文字型
plt.rcParams['font.sans-serif'] = 'PingFang HK'

ax.set_title('失業人口與癌症死亡關係')
ax.set_xlabel('年度')
ax.set_ylabel('人口數')

dt = pd.read_csv('cancer_unemployment.csv')

x = dt['年度'].array

print(dt.columns)

ax.plot(x,dt['惡性腫瘤（女性）'].values,label='惡性腫瘤（女性）',marker='o',markersize=4);
ax.plot(x,dt['惡性腫瘤（男性）'].values,label='惡性腫瘤（男性）',marker='o',markersize=4);
ax.plot(x,dt[' 失業人口（男性）'].values,label='失業人口（男性）',marker='o',markersize=4);
ax.plot(x,dt['失業人口（女性）'].values,label='失業人口（女性）',marker='o',markersize=4);

plt.legend()
plt.show();
