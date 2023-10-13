import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os 

fig = plt.figure()
ax = plt.axes()

ax.set_title("National Annual Cancer Death Population")
ax.set_xlabel('Annual')
ax.set_ylabel('Death Population')
annual_cencer_dt = pd.read_csv('annual_cencer.csv')

x = annual_cencer_dt['年度'].array
print(annual_cencer_dt.columns)
ax.plot(x,annual_cencer_dt['氣管、支氣管和肺癌 '].values,label='Lung Cancer',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['肝和肝內膽管癌 '].values,label='Liver Cancer',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['結腸、直腸和肛門癌 '].values,label='Colorectal Cancer',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['女性乳癌 '].values,label='Breast Cancer',marker='o',markersize=4);
ax.plot(x,annual_cencer_dt['口腔癌 '].values,label='Oral Cancer',marker='o',markersize=4);
plt.legend()
plt.show();



