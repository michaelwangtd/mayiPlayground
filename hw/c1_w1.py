#!/usr/bin python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd


def sigmod(x):
    return 1/(1+np.exp(-x))
def sigmod_derivative(x):
    s = sigmod(x)
    return s * (1-s)

# shape reshape
def usage_shapereshape():
    image = np.array([[[0.67826139, 0.29380381],
                       [0.90714982, 0.52835647],
                       [0.4215251, 0.45017551]],

                      [[0.92814219, 0.96677647],
                       [0.85304703, 0.52351845],
                       [0.19981397, 0.27417313]],

                      [[0.60659855, 0.00533165],
                       [0.10820313, 0.49978937],
                       [0.34144279, 0.94630077]]])
    # image = np.array([
    #     [[1,2]],
    #     [[3,4]],
    #     [[5,6]]
    # ])
    print(image.shape)
    image = image.reshape(image.shape[0]*image.shape[1],image.shape[2])
    print(image.shape)
    print(image)

# normalize
def normalizeRows(x):
    x_norm = np.linalg.norm(x,axis=1,keepdims=True)
    # x_norm = np.linalg.norm(x,axis=1)
    print('x_norm:')
    print(x_norm)
    x = x/x_norm
    print('x:')
    print(x)

# softmax
def softmax(x):
    print('x:')
    print(x)
    x_exp = np.exp(x)
    print('x_exp:')
    print(x_exp)
    x_sum = np.sum(x_exp,axis=1,keepdims=True)
    print('x_sum:')
    print(x_sum)
    x_soft = x_exp / x_sum
    print('x_soft:')
    print(x_soft)

# dot() outer() multiply()
def usage_d_o_m():
    x1 = np.array([1,3,5,7])
    x2 = np.array([2,4,6,8])
    x_dot = np.dot(x1,x2)
    print('x_dot:') #点乘
    print(x_dot)
    x_outer = np.outer(x1,x2)
    print('x_outer:')
    print(x_outer)
    x_multiply = np.multiply(x1,x2) #叉乘
    print('x_multiply:')
    print(x_multiply)

# l1 loss and l2 loss
def l1_loss(y_hat,y):
    y_abs = np.abs(y_hat-y)
    print('y_abs:')
    print(y_abs)
    y_l1 = np.sum(y_abs)
    return y_l1

def l2_loss(y_hat,y):
    y_diff = y_hat-y
    print('y_diff:')
    print(y_diff)
    y_l2 = np.dot(y_diff,y_diff.T)
    return y_l2



if __name__ == '__main__':
    x1 = np.array([[0,4],[1,5]])
    y_hat = np.array([.9,.2,0.1,.4,.9])
    y = np.array([1,0,0,1,1])

    # 6
    print(l1_loss(y_hat,y))
    print(l2_loss(y_hat,y))

    # 5
    # usage_d_o_m()

    # 4
    # softmax(x1)

    # 2
    # usage_shapereshape()

    # 3
    # x = np.array([[2,4],[4,6]])
    # normalizeRows(x)