#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:36:27 2020

@author: magnus
"""

def inputNumber(prompt):
# INPUTNUMBER Prompts user to input a number
## Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
# number. Repeats until user inputs a valid number.
## Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
            try:
                num = float(input(prompt))
                break
            except ValueError:
                pass
    return num