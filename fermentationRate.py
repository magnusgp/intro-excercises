#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:20:27 2020

@author: magnus
"""

import numpy as np

def fermentationRate(measuredRate, lowerBound, upperBound):
    if 15 < measuredRate and measuredRate < 25:
        averageRate = (((sum.all(measuredRate)))/len(measuredRate))
        return averageRate
    
#%%
import numpy as np

def fermentationRate(measuredRate, lowerBound, upperBound):
    validMeasure = np.logical_and (measuredRate > lowerBound, measuredRate < upperBound)
    averageRate = (((np.sum(validMeasure)))/len(validMeasure))
    print(validMeasure)
    
#%% 
import numpy as np
def fermentationRate(measuredRate, lowerBound, upperBound):
    for i in np.linspace(measuredRate,upperBound):
        if np.logical_and(i > lowerBound, i < upperBound):
            averageRate = sum(i)/len(i)
            return averageRate
#%%
def fermentationRate(measuredRate,lowerBound,upperBound):
    b=measuredRate[measuredRate>lowerBound]
    c=b[b<upperBound]
    averageRate=sum(c)/len(c)
    return averageRate
