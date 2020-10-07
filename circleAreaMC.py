#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:24:54 2020

@author: magnus
"""

import numpy as np
#from randomSequence import *
#   xvals = np.random.rand(-1,1,len(xvals))
#   yvals = np.random.rand(-1,1,len(yvals))
#   vals = [[x, y] for x, y in zip(xvals, yvals)]
#   print(vals)

def circleAreaMC(xvals, yvals):
    n = 0
    for i in range(np.size(xvals)):
        if np.linalg.norm(np.array([xvals[i],yvals[i]])) < 1:
            n += 1      
    Ac = 4*(n/np.size(xvals))
    return Ac