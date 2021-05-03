# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:42:38 2021

@author: caear
"""
import pylab
import numpy
import random


def makeHist(data, title, xlabel, ylabel, bins = 20):
    pylab.hist(data, bins = bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    

def getHighs():
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    return population


def getMeanAndSDs(population, sample, verbose = False):
    popMean = sum(population)/len(population)
    sampleMean = sum(sample)/len(sample)
    if verbose:
        makeHist(population,
                 'Daily High 1961-2015, Population\n' +\
                 '[mean = ' + str(round(popMean, 2)) + ']',
                 'Degrees C', 'Number Days')
        pylab.figure()
        makeHist(sample, 'Daily High 1961-2015, Sample\n' +\
                 '[mean = ' + str(round(sampleMean, 2)) + ']',
                 'Degrees C', 'Number Days')
        print('Population mean =', popMean)
        print('Standard deviation of population =',
              numpy.std(population))
        print('Sample mean =', sampleMean)
        print('Standard deviation of sample =',
              numpy.std(sample))
    return popMean, sampleMean,\
        numpy.std(population), numpy.std(sample)
        

random.seed(0)
population = getHighs()
sampleSize = 100
numSamples = 2000
maxMeanDiff = 0
maxSDDiff = 0
sampleMeans = []
for i in range(numSamples):
    sample = random.sample(population, sampleSize)
    popMean, sampleMean, popSD, sampleSD =\
        getMeanAndSDs(population, sample, verbose = False)
    sampleMeans.append(sampleMean)
    if abs(popMean - sampleMean) > maxMeanDiff:
        maxMeanDiff = abs(popMean - sampleMean)
    if abs(popSD - sampleSD) > maxSDDiff:
        maxSDDiff = abs(popSD - sampleSD)
print('Mean of sample Means =',
      round(sum(sampleMeans)/len(sampleMeans), 3))
print('Standard deviation of sample means =',
      round(numpy.std(sampleMeans), 3))
print('Maximum difference in means =',
      round(maxMeanDiff, 3))
print('Maximum difference in standard deviations =',
      round(maxSDDiff, 3))
makeHist(sampleMeans, 'Means of Samples', 'Mean', 'Frequency')
pylab.axvline(x = popMean, color = 'r')


