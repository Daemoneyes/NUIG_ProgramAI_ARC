# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 06:15:09 2019

@author: WeihongXu
"""
import numpy as np
import sys
from tools import read_JsonFile, read_JsonPath



def solve(data):
    dataArray = np.array(data)
    resultArray = dataArray.copy()
    (x,y) = resultArray.shape
    # Loop all the point in the data
    for row in range(x):
        for colume in range(y):
            # if the point is not at board and its not a black point
            if((not(row in (0,x-1) or colume in (0,y-1))) and resultArray[row,colume] != 0):
                if(resultArray[row-1,colume] == resultArray[row,colume-1] == resultArray[row+1,colume] == resultArray[row,colume+1]):
                    # Set the mid point to black color
                    resultArray[row,colume] = 0
            else:
                continue
    print(f"{dataArray} {resultArray}")
    


if __name__=="__main__":
    jsonFilePath = read_JsonPath(sys.argv)
    trainX,trainY,testX,testY = read_JsonFile(jsonFilePath)
    for i in trainX:
        solve(i)
    for i in testX:
        solve(i)
