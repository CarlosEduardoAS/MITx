# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:32:06 2021

@author: caear
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    nums = []
    for num in range(100):
        if num % 2 == 0:
            nums.append(num)
    return random.choice(nums)


def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    for num in range(9, 21):
        if num % 2 == 0:
            return num
        

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    while True:
        num = random.randint(9, 21)
        if num % 2 == 0:
            return num
        
    
def rollDice():
    '''Return a random int between 1 and 6'''
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDice())
    print(result)


def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDice())
        if result == goal:
            total += 1
    print('Actual probability =', 
          round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability =', 
          round(estProbability, 8))
    
runSim('11111', 1000000)


def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDice() == 6 and rollDice() == 6:
            numBoxCars += 1
    return numBoxCars/numTests

print('Frequency of double 6 =', str(fracBoxCars(100000)*100)+'%')