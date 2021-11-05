import warnings

warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid', font_scale=1.5)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print ('训练数据集:',train.shape,'测试数据集:',test.shape)

#合并数据集 方便同时对两个数据集进行清洗
full = train.append(test,ignore_index=True)
print(full.isnull().sum())