#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:11:13 2020

@author: magnus
"""
import math

def classifyBMI(height, weight):
       
    bmi = weight/height**2

    
    if bmi < 16 :
        return "Severely underweight"
    
    elif 16 <= bmi <= 18.5 :
       return "Underweight"
        
    elif 18.5 <= bmi <= 25 :
        return "Normal"
        
    elif 25 <= bmi <= 30 :
        return "Overweight"
        
    elif 30 <= bmi <= 40 :
        return "Obese"
    
    elif 40 <= bmi :
        return "Severely obese"
    
    return BMIGroup

print(classifyBMI(1.85, 88))