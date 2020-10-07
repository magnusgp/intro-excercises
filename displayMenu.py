#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:37:38 2020

@author: magnus
"""

import numpy as np
from inputNumber import inputNumber

def displayMenu(options):
# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen.
##Usage: choice = displayMenu(options)
##Input options Menu options (array of strings)
# Output choice Chosen option (integer)
# Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
# Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
        return choice