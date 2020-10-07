#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:13:28 2020

@author: magnus
"""

import numpy as np

def acuteAngle(v1,v2):
    acute = np.arccos(np.dot(v1,v2))
    if acute > np.pi/2:
        theta = np.pi-acute
    elif acute < np.pi/2:
        theta = acute
    return theta

