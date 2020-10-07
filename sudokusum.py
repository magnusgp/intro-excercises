#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:57:40 2020

@author: magnus
"""


def fillSudokuRow(s) : 
    s[s==0]=45-sum(s)
    return s

