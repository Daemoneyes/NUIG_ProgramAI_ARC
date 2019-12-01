# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 03:39:12 2019

@author: Weihong Xu
"""

import numpy as np
import sys
from tools import read_JsonFile, read_JsonPath


def solve(data):
    dataArray = np.array(data)
    # first step is locate each 3x3 block out
    # store list of the 3x3 np array in tempList
    tempList = []
    for i in np.vsplit(dataArray, 3): 
        for j in np.hsplit(i, 3):
            tempList.append(j)
    resultList = []        
    for i in tempList:
        # Loop the i in the tempList, each i represent 3x3 array
        commonColor = np.argmax(np.bincount(i.flatten()))
        # create a new np array with the most common color
        i = np.full(9, commonColor).reshape(3, 3)
        # readd into the List
        resultList.append(i)
    # Multiple stack/split on horzion vertical side to rebuild the array
    result = np.hstack(np.vsplit(np.vstack(resultList), 3))
    print(f"{dataArray} {result}")


if __name__ == "__main__":
    jsonFilePath = read_JsonPath(sys.argv)
    trainX, trainY, testX, testY = read_JsonFile(jsonFilePath)
    for i in trainX:
        solve(i)
    for i in testX:
        solve(i)


