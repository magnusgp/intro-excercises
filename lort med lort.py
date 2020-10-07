#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:17:36 2020

@author: magnus
"""

for i in range(10):
    print("I love programming!")
    
#%%
import numpy as np
x = np.array([])
for i in range(np.array(10)):
    x=0
    if x[i] < x:
        x+=x*2
    print(x)
    
#%%
import numpy as np

for x in range(1, 11):
    print("The square root of {:0.4f} is {:0.4f}".format(x,np.sqrt(x)))

#%%
import numpy as np
for x in range(1,8):
    h = 13
    m = 36
    m += 20
    if m > 60:
        m = m - 60 and h = h + 1
    print("The train will leave at {:0d}:{:0d} tomorrow".format(h,m))

#%%
import numpy as np

N = 1000000
approxpi = 0
for n in range(N+1):
    approxpi = approxpi + 4*(((-1)**n)/(2*n+1))
print(approxpi)
#%%

import numpy as np

def sqrt_function(a):
    for i in range(5):
        x = a/2
        if x != np.sqrt(2):
            x=(x+a/x)/2
            return x
        #%%





