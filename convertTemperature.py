#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:23:00 2020

@author: magnus
"""

def convertTemperature(T, unitFrom, unitTo):
    if unitFrom == "Celsius" and unitTo == "Fahrenheit":
            T = 1.8 * T + 32
    elif unitFrom == "Celsius" and unitTo == "Kelvin":
            T = T + 273.15
    elif unitFrom == "Fahrenheit" and unitTo == "Celsius":
            T = (T - 32)/1.8
    elif unitFrom == "Fahrenheit" and unitTo == "Kelvin":
            T = (T+459.67)/1.8
    elif unitFrom == "Kelvin" and unitTo == "Celsius":
            T = T - 273.15
    elif unitFrom == "Kelvin" and unitTo == "Fahrenheit":
            T = 1.8 * T - 459.67
    return T