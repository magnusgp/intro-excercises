
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:47:23 2020

@author: magnus
"""
def thermoEquilibrium(N, r):
    t = 0
    NR = 0
    NL = N
    while NL != NR :
        if t > len(r)-1:
            t=0
            break
        
        if r[t] <= NL/N:
            NL -= 1
            NR += 1
            t += 1
        else :
            NL += 1
            NR -= 1
            t += 1
    return t

import numpy as np
print(thermoEquilibrium(12.0, np.array([0.16, 0.04, 0.72, 0.09, 0.17, 0.60, 0.26, 0.65, 0.69, 0.74, 0.45, 0.61, 0.23, 0.37, 0.15, 0.83, 0.61, 1.00, 0.08, 0.44])))
