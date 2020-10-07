#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:43:03 2020

@author: magnus
"""

def computePassesGoalLine(point, directionVector):
    
    x,y=point
    vx,vy=directionVector

    if vx>0:
        xgoal=105
        a=(xgoal-x)/vx
        ygoal=y+a*vy
        
    if vx<0:
        xgoal=0
        a=(xgoal-x)/vx
        ygoal=y+a*vy
        
    if vx==0:
        ygoal=0
    
    if 30.34<ygoal and ygoal<37.66:
        score=True
    
    else:
        score=False
    return score