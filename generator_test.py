#!/sur/bin python
# -*- coding:utf-8 -*-


testList = [[1,2,3],[4,5,6]]
inputList = []

class Generator():
    def __init__(self,inputList):
        self.inputList = inputList

    def __iter__(self):
        for itTuple in testList:
            for item in itTuple:
                yield item

for item in Generator(inputList):
    print(item)
