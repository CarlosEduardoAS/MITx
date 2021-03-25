# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:20:52 2021

@author: caear
"""

def get_ratios(L1, L2):
    """
    Parameters
    ----------
    L1 and L2 are lists of equal length of numbers

    Returns a list containing L1[i/L2[i]
    -------
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bard arg')
    return ratios

