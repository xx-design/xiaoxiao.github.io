# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 4 * np.pi, 100) 
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1) #在画布一行两列的第一列显示
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x, y) #以x为横坐标,y为纵坐标绘制连线图


#
y1 = 2*np.sin(x*2)
plt.subplot(1,2,2) #在画布一行两列的第二列显示
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=2sin(x)$') #显示标题
plt.plot(x,y1)#以x为横坐标,y1为纵坐标绘制连线图
plt.show()#显示图像