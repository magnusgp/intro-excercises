#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:01:39 2020

@author: magnus
"""

import turtle
bob = turtle.Turtle()
print(bob)
for i in range(8):
    bob.fd(25)
    bob.lt(45)
    bob.fd(25)
turtle.mainloop()

import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

#%%
def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob,7,70)

#%%
import turtle
import math
bob = turtle.Turtle()

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)