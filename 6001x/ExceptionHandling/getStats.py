# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:36:30 2021

@author: caear
"""

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats


def avg(grades):
    try:
        return sum(grades)/len(grades)
    except:
        print('no grades data')
        return 0.0
    
test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
               [['deadpool'], []]]
