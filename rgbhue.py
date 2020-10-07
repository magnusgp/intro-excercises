#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:55:20 2020

@author: magnus
"""

def rgb2hue(R, G, B):

    vb = max(R, G, B)-min(R, G, B)    
    
    if R >= G and R >= B:
        H = 60*((G-B)/vb)
    
    elif G >= R and G >= B:
        H = 120+60*((B-R)/vb)
        
    elif B >= R and B >= G:
        H = 240+60*((R-G)/vb)   
    
    if H < 0:
        H = H + 360
    
    return H

print(rgb2hue(0.9, 0.9, 0.3))

