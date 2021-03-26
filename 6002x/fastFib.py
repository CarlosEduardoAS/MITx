# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:01:53 2021

@author: caear
"""

def fastFib(n, memo = {}):
    '''Assumes n is an int >= 0,
       memo used only by recursive calls
       Returns Fibonacci of n'''
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    
for i in range(121):
    print(f'Fib({str(i)}) = {fastFib(i)}')