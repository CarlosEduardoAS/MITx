# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:13:58 2021

@author: caear
"""

def isPalindrome(aString):
    '''
    aString: a string
    '''
    aString = aString.strip().lower().split()
    aString = ''.join(aString)
    inverse = ''
    for letter in range(len(aString) - 1, -1, -1):
        inverse += aString[letter]
    return aString == inverse
    

def primes_list(N):
    '''
    N: an integer
    '''
    def isPrime(num):
        for number in range(2, num):
            if num % number == 0:
                return False
        return True
    primes = []
    for num in range(2, N+1):
        if isPrime(num):
            primes.append(num)
    return primes


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    keys = []
    for k in aDict.keys():
        count = 0
        for value in aDict.values():
            if aDict[k] == value:
                count += 1
        if count == 1:
            keys.append(k)
    return sorted(keys)

aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print(uniqueValues(aDict))