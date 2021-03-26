# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:09:39 2021

@author: caear
"""
from random import randint

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
        
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'
        
                     
def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]


def buildRandomItems(n):
    return [Item(str(i),10*randint(1,10),randint(1,10))
            for i in range(n)]


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 2:
                bag1.append(str(items[j]))
            elif (i // 3**j) % 3 == 1:
                bag2.append(str(items[j]))
        yield bag1, bag2


#Test 1
items = buildItems()
combos = yieldAllCombos(items)

#Test 2
#items = buildRandomItems(1)
#combos = yieldAllCombos(items)