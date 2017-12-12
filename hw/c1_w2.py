#!/usr/bin python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from homework import index
import os

"""
    利用神经网络构建一个分类器的例子
"""

def load_data():
    # 从数据获取就可以体会到h5的好处
    train_path = os.path.join(index.hw_dir,'data','train_catvnoncat.h5')
    test_path = os.path.join(index.hw_dir,'data','test_catvnoncat.h5')

    train_ds = h5py.File(train_path,'r')
    train_x_orig = np.array(train_ds['train_set_x'][:])
    train_y_orig = np.array(train_ds['train_set_y'][:])

    test_ds = h5py.File(test_path,'r')
    test_x_orig = np.array(test_ds['test_set_x'][:])
    test_y_orig = np.array(test_ds['test_set_y'][:])
    # 注意：这样的shape是不规范的结构，在编程过程中尽量避免，要使用reshape进行规范处理
    print(test_y_orig.shape, test_y_orig)

    classes = np.array(test_ds['list_classes'][:])

    train_y_orig = train_y_orig.reshape(1,train_y_orig.shape[0])
    test_y_orig = test_y_orig.reshape(1,test_y_orig.shape[0])


    print('train x:',train_x_orig.shape)
    print('train y:',train_y_orig.shape)
    print('test x:',test_x_orig.shape)
    print('test y:',test_y_orig.shape,test_y_orig)
    print('classes:',classes.shape,classes)
    return train_x_orig,train_y_orig,test_x_orig,test_y_orig,classes

def show_sample(idx,dsx,dsy):
    '''
        获取对一个样本直观的描述
    '''
    if idx < dsx.shape[0]:
        print('--------------')
        sample = dsx[idx]
        print('sample:',sample.shape)
        # print(sample)
        label = dsy[0][idx]
        print('label:',label.shape,label)
        print(classes[label].decode('utf-8'))

        plt.figure()
        plt.imshow(sample)
        plt.show()



if __name__ == '__main__':
    np.set_printoptions(linewidth=1000,threshold=np.nan)

    train_x_orig,train_y_orig,test_x_orig,test_y_orig,classes = load_data()

    show_sample(12,test_x_orig,test_y_orig)