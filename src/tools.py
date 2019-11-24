# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 03:37:37 2019

@author: Weihong Xu
"""
import json

# Method to read the Json file and then response with
# TrainX, TrainY, TestX,TestY
def read_JsonFile(filePath):
    with open(filePath,"r") as f:
        data = json.load(f)
    trainX = []
    trainY = []
    testX = []
    testY = []
    for i in data["train"]:
        trainX.append(i["input"])
        trainY.append(i["output"])
    for i in data["test"]:
        testX.append(i["input"])
        testY.append(i["output"])
    
    return trainX,trainY,testX,testY