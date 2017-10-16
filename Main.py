#encoding: utf-8
import csv
import pandas as pd
from scipy import  stats as ss
import seaborn as sns
import matplotlib.pyplot as plt
# Reading data from web
data_local = "C:\\Users\\lenovo\Desktop\\data.csv"
data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
csv_reader = csv.reader(open(data_local,'r'))
df = pd.read_csv(data_local)
des= df.describe()#样本数据描述，包括最大最小值
t = ss.ttest_1samp(a = df.ix[:, 'Abra'], popmean = 15000)#单样本t检验
all= ss.ttest_1samp(a=df,popmean=15000)
plt.show(sns.lmplot("Benguet", "Ifugao", df))
# plt.show(sns.distplot(df.ix[:, 2], rug=True, bins=15))#某一列的直方图
# with sns.axes_style("white"):
#     plt.show(sns.jointplot(df.ix[:,1], df.ix[:,2], kind = "kde"))
# print csv_reader
# for row in csv_reader:
#  print row