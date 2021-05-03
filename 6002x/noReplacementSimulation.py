# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:03:46 2021

@author: caear
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numSuccess = 0
    for trial in range(numTrials):
        if oneTrial() == True:
            numSuccess += 1
    return numSuccess / numTrials

def oneTrial():
    bucket = ['R', 'R', 'R', 'G', 'G', 'G']
    comb = random.sample(bucket, 3)
    if comb[0] == comb[1] == comb[2]:
        return True
    else:
        return False