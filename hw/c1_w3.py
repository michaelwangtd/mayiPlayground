#!/usr/bin python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def compute_cost_test_case():
    np.random.seed(1)
    Y_assess = np.random.randn(1, 3)
    parameters = {'W1': np.array([[-0.00416758, -0.00056267],
                                  [-0.02136196, 0.01640271],
                                  [-0.01793436, -0.00841747],
                                  [0.00502881, -0.01245288]]),
                  'W2': np.array([[-0.01057952, -0.00909008, 0.00551454, 0.02292208]]),
                  'b1': np.array([[0.],
                                  [0.],
                                  [0.],
                                  [0.]]),
                  'b2': np.array([[0.]])}

    a2 = (np.array([[0.5002307, 0.49985831, 0.50023963]]))

    return a2, Y_assess, parameters

def load_planar_dataset():
    '''
        获取原始的数据
    '''
    np.random.seed(1)
    m = 400  # number of examples
    N = int(m / 2)  # number of points per class
    D = 2  # dimensionality
    X = np.zeros((m, D))  # data matrix where each row is a single example
    Y = np.zeros((m, 1), dtype='uint8')  # labels vector (0 for red, 1 for blue)
    a = 4  # maximum ray of the flower

    for j in range(2):
        ix = range(N * j, N * (j + 1))
        t = np.linspace(j * 3.12, (j + 1) * 3.12, N) + np.random.randn(N) * 0.2  # theta
        r = a * np.sin(4 * t) + np.random.randn(N) * 0.2  # radius
        X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
        Y[ix] = j

    X = X.T
    Y = Y.T

    return X, Y

def show_data(X,Y):
    print('X shape:', X.shape)
    print('X shape:', Y.shape)

    # plt.figure()
    # plt.scatter(X[0, :], X[1, :], c=Y[0, :], s=40, cmap=plt.cm.Spectral)
    # plt.show()

def get_layer_size(X,Y):
    l_x = X.shape[0]
    l_h = 4
    l_y = Y.shape[0]
    return l_x,l_h,l_y

def init_parameter(l_x,l_h,l_y):
    w1 = np.random.randn(l_h,l_x)
    b1 = np.zeros((l_h,1))
    w2 = np.random.randn(l_y,l_h)
    b2 = np.zeros((l_y,1))

    params = {'w1':w1,'b1':b1,'w2':w2,'b2':b2}
    return params

def fp(X,params):
    w1 = params['w1']
    b1 = params['b1']
    w2 = params['w2']
    b2 = params['b2']

    Z1 = np.dot(w1.T,X)+b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(w2.T,A1)+b2
    A2 = np.tanh(Z2)

    cache = {'Z1':Z1,'A1':A1,'Z2':Z2,'A2':A2}
    return A2,cache

def compute_cost(A2,Y):
    m = Y.shape[1]
    logprobs = Y*np.log(A2)+(1-Y)*np.log(1-A2)
    cost = -1/m * np.sum(logprobs)
    # print(cost.shape)
    # print(cost)
    return cost

def func_test():
    a2, y, params = compute_cost_test_case()
    compute_cost(a2, y)


if __name__ == '__main__':
    X,Y = load_planar_dataset()
    show_data(X,Y)

    l_x,l_h,l_y = get_layer_size(X,Y)
    print(l_x,l_h,l_y)
    params = init_parameter(l_x,l_h,l_y)
    print(params['w1'].shape)
    print(params['b1'].shape)
    print(params['w2'].shape)
    print(params['b2'].shape)




