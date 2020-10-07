#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:46:40 2020

@author: magnus
"""

def bacteriaGrowth(n0, alpha, K, N):
    tN = 0 
    while n0 <= N:
        n0 = (1+alpha*(1-(n0/K)))*n0
        tN +=1
    return tN