# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:07:12 2018

@author: 16023
"""

def comput_Discrimination(x, y, n):
    '''
    计算差商表
    input:
        x:已知点的横坐标，类型list
        y:已知点的纵坐标，类型list
        n:n次插值
    output:
        差商表，类型：二维List
    '''
    #差商计算公式：上一阶相邻差商之差/间隔为差商阶数的横坐标之差
    total = []
    total.append(y)
    P = y
    for i in range(1, n+1):
        L = []
        for j in range(len(P)-1):
            L.append((P[j+1]-P[j])/(x[j+i]-x[j]))
        total.append(L)
        P = L
        
    return total

def multiplicative(x, n, x_i):
    '''
    计算累乘
    input:
        x:插值数值
        n:累乘次数
        x_i:累乘元素范围, list
    output:
        累乘结果
    '''
    # k*(x-x0)*(x-x1)*...
    k = 1
    for i in range(n):
        k *= (x-x_i[i])
    
    return k

def Newton_interpolation(xy_i, x, n):
    '''
    n次牛顿插值
    input:
        xy_i:已知点横纵坐标tuple, 类型list [(1,1),(1,1),(2,1)]
        x:插值点
        n:n次插值
    output:
        插值结果
    '''
    #选取范围插值点
    x_i = []
    y = []
    for i in range(len(xy_i)):
        if xy_i[i][0] <= x < xy_i[i+1][0]:
            for j in range(n+1):
                x_i.append(xy_i[i+j][0])
                y.append(xy_i[i+j][1])
    
    #获取差商表
    total = comput_Discrimination(x_i ,y,n)
  
    #计算插值结果
    #N_n(x) = k0 + k1*(x-x0) + k2*(x-x0)(x-x1)+...
    num = 0
    for j in range(n+1):
        num = num + total[j][0]* multiplicative(x,j, x_i)
    
    return num

'''
试例：
R = [(10,2.3026),(11,2.3979),(12,2.4849),(13,2.5649),(14,2.6391)]
m = Newton_interpolation(R, 11.75, 2)
print(m)
'''   
    
    
    