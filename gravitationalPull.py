#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:33:01 2020

@author: magnus
"""

import numpy as np
import matplotlib.pyplot as plt

def gravitationalPull(x):
    y=np.zeros(len(x))
    x=np.arange(1,10e6,1e4)
    g0=9.82
    R=6.371*10**6
    for i in range(len(x)):
        if R<=x[i]:
            g=g0*(R**2/x**2)
        elif 0<=x[i] and x[i]<R:
            g=(g0*(x[i]/R))
    return g
plt.plot(x,gravitationalPull(x))
plt.show()
