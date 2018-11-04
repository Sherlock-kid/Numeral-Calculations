# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:20:05 2018

@author: 16023
"""
#拉格朗日(Lagrange)插值

def lagr_interpolation_basis_func(Range, x, k, n):
    '''
    拉格朗日插值基函数
    input:
        Range:已知点的横纵坐标tuple，类型list
        x:插值点，类型float
        k:需要计算的第k个基函数值
        n:n次插值, int
    output:
        l_k
    '''          
    x_k = Range[k][0]
    l_k = 1
    #l_k = ∏(x-x_i)/(x_k-x_i) ,i≠k
    for i in range(len(Range)):
        l_k *= (x-Range[i][0])/(x_k-Range[i][0]) if k != i else 1
    
    return l_k


def lagr_interpolation(xy_i, x, n):
    '''
    n次拉格朗日代数插值
    input:
        xy_i:已知点的横纵坐标tuple，类型list
        x:插值点，类型float
        n:插值次数, int
    output:
        插值结果
    '''
     #选取范围插值点
    Range = []
    for i in range(len(xy_i)):
        if xy_i[i][0] <= x < xy_i[i+1][0]:
            for j in range(n+1):
                Range.append(xy_i[i+j])
    
    #L(x) = Σl_k*y(k)
    num = 0
    for j in range(len(Range)):
        num = num + lagr_interpolation_basis_func(Range, x, j, n)*Range[j][1]
        
    return num

'''
示例：
R = [(10,2.3026),(11,2.3979),(12,2.4849),(13,2.5649),(14,2.6391)]
m = lagr_interpolation(R, 11.75, 2)
print(m)
'''
