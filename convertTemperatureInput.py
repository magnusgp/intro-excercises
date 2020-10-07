#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:53:53 2020

@author: magnus
"""
from convertTemperature import convertTemperature


while True:
    try:
        T = float(input("Please input a temperature:"))
        unitFrom = str(input("Please input the unit of temperature (Celsius, Fahrenheit, or Kelvin):"))
        unitTo = str(input("Please input the unit to convert to (Celsius, Fahrenheit, or Kelvin):"))
        TN = convertTemperature(T, unitFrom, unitTo)
        print(("{} {} = {} {}".format(T,unitFrom,TN,unitTo)))
        break
    except ValueError:
        print("Not valid number. Please try again.")
