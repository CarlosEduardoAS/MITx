# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:49:09 2021

@author: caear
"""

import random
random.seed(0)
numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize//communitySize
numTrials = 100
numGreater = 0
for t in range(numTrials):
    locs = [0]*numCommunities
    for i in range(numYears*numCasesPerYear):
        locs[random.choice(range(numCommunities))] += 1
    if max(locs) >= 143:
        numGreater += 1
prob = round(numGreater/numTrials, 4)
print('Est. probability of at least one region having \
      at least 143 cases =', prob)