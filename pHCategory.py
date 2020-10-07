#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:10:02 2020

@author: magnus
"""

import numpy as np

def pH2Category(pH):
    category = pH
#alle tal under 7 rundes ned   
    if pH < 7:
          pH=np.floor(pH)
#alle tal over 7 rundes op
    if pH > 7: 
          pH=np.ceil(pH)
    if 0<=pH and pH<3:
        return "Strongly acidic"
    if 3<=pH and pH<5:
        return "Weakly acidic"
    if 6<=pH and pH<8:
        return "Neutral"
    if 9<=pH and pH<11:
        return "Weakly basic"
    if 12<=pH and pH<14:
        return "Strongly basic"
    if pH>14:
        return "pH out of range"
    return category

