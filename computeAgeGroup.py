#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:03:21 2020

@author: magnus
"""

def computeAgeGroup(age):

    if age<1:
        return "Infant"
    if 1<=age and age<3:
        return "Toddler"
    if 3<=age and age<13:
        return "Child"
    if 13<=age and age<20:
        return "Teenager"
    if age>=20:
        return "Adult"
    return ageGroup
    