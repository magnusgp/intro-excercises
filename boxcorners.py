#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:28:03 2020

@author: magnus
"""

import numpy as np

def boxArea (boxCorners, area):
    x1,x2,x3,x4,y1,y2,y3,y4 = boxCorners
    
    a1 = (x2-x1)*(y2-y1)
    a2 = (x4-x3)*(y4-y3)
    a0 = max(0,min(x2,x4)-max(x1,x3))*max(0,min(y2,y4)-max(y1,y3))
    
    if area == "Box1":
        A = a1
        
    elif area == "Box2":
        A = a2
        
    elif area == "Intersection":
        A = a0
        
    elif area == "Union":
        A = (a1 + a2) - a0
        
    return A


print(boxArea(np.array([5,20,14,25,12,23,5,17]), "Intersection"))