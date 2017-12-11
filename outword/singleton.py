#!/usr/bin python
# -*- coding:utf-8 -*-

class Singleton(object):
    # _instance是一个类变量
    _instance = None
    # cls指代当前类
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
    print(s1==s2)
    print(id(s1),id(s2))
    """
    <__main__.Singleton object at 0x000001DA6FC8B860>
    <__main__.Singleton object at 0x000001DA6FC8B860>
    True
    2037689923680 2037689923680
    """


