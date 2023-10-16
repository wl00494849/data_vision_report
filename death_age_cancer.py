import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os 
import seaborn as sns

fig = plt.figure()
ax = plt.axes()

df = pd.read_csv('age_death_cencer.csv')
plt.rcParams['font.sans-serif'] = 'PingFang HK'
print(df.columns)
print(df['惡性腫瘤（男）'].value_counts())
print(df['惡性腫瘤（男）'].value_counts().index)

x = np.arange(len(df['年齡'].array))
width = 0.3
plt.bar(x, df['惡性腫瘤（男）'].values, width, color='#4A6FF5', label='男')
plt.bar(x + width, df['惡性腫瘤（女）'].values, width, color='#F54520', label='女')
plt.xticks(x + width / 2, df['年齡'])

plt.xlabel('年齡')
plt.ylabel('死亡人數')
plt.title('110年齡與性別癌症死亡人數')

plt.legend()
plt.show()