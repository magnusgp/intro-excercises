#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:55:59 2020

@author: magnus
"""
import numpy as np

#%%

grades = [10, 2, 7]

def grades_mean(grades):
    return sum(grades)/len(grades)

exam_avg = grades_mean(grades)
print('My mean is ' + str(exam_avg))

dk_scale = [-3,0,2,4,7,10,12]
ects_scale = ["F","Fx","E","D","C","B","A"]

def dk_to_ects_grade(dk_grade):
    index = dk_scale.index(dk_grade)
    return ects_scale[index]

print(dk_to_ects_grade(7))

#%%

ects_grades = [dk_to_ects_grade(grade) for grade in grades]
print(ects_grades)

exam_results = {
        "courses": ["Matematik", "Fysik", "Kemi"],
        "grades": np.array(grades),
        "points": np.array([15, 5, 10])
    }

exam_results["weigths"] = exam_results["points"] / sum(exam_results["points"])
print(exam_results)

def grades_weighted_mean(results):
    return sum(results["weigths"] * results["grades"])

print(grades_weighted_mean(exam_results))
#%%