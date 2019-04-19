import sys
import numpy as np
import pandas as pd
import csv


##  读入测试数据
raw_data = np.genfromtxt('train.csv', delimiter = ',') ## 读入测试数据
data = raw_data[1:,1:]
where_are_nans = np.isnan(data)
data[where_are_nans] = 0


## 数据处理
x1 = data[:,0:1]
x2 = data[:,1:2]
x3 = data[:,2:3]
x4 = data[:,3:4]
x5 = data[:,4:5]
x6 = data[:,5:6]
y = data[:,7:8]