# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 05:36:16 2019

@author: Weihong Xu
"""
import sys
import numpy as np
from tools import read_JsonFile


    
    

def solve(data):
    # first step, find the most common color in the array
    dataArray = np.array(data)
    x,y = dataArray.shape
    commonColor = np.argmax(np.bincount(dataArray.flatten()))
    # Second Create a new NP array with the largest color
    result = np.full(x*y,commonColor).reshape(x,y)
    print(f"{dataArray} {result}")
    

if __name__ == "__main__":
    if(len(sys.argv)==2):
        jsonFilePath = sys.argv[1]
        trainX,trainY,testX,testY = read_JsonFile(jsonFilePath)
        for i in trainX:
            solve(i)
        for i in testX:
            solve(i)
    else:
        raise "Please Provide File Path"



