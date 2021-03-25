# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:56:41 2021

@author: caear
"""

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt +=1
    

test = [1, 5, 3, 8, 4, 9, 6, 2]