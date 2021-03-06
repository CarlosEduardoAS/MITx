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
# population = getHighs()
# sampleSize = 200
# numSamples = 1000
# maxMeanDiff = 0
# maxSDDiff = 0
# sampleMeans = []
# for i in range(numSamples):
#     sample = random.sample(population, sampleSize)
#     popMean, sampleMean, popSD, sampleSD =\
#         getMeanAndSDs(population, sample, verbose = False)
#     sampleMeans.append(sampleMean)
#     if abs(popMean - sampleMean) > maxMeanDiff:
#         maxMeanDiff = abs(popMean - sampleMean)
#     if abs(popSD - sampleSD) > maxSDDiff:
#         maxSDDiff = abs(popSD - sampleSD)
# print('Mean of sample Means =',
#       round(sum(sampleMeans)/len(sampleMeans), 3))
# print('Standard deviation of sample means =',
#       round(numpy.std(sampleMeans), 3))
# print('Maximum difference in means =',
#       round(maxMeanDiff, 3))
# print('Maximum difference in standard deviations =',
#       round(maxSDDiff, 3))
# makeHist(sampleMeans, 'Means of Samples', 'Mean', 'Frequency')
# pylab.axvline(x = popMean, color = 'r')


#Standard Error
def sem(popSD, sampleSize):
    return popSD/sampleSize**0.5


# sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
# numTrials = 50
# population = getHighs()
# popSD = numpy.std(population)
# sems = []
# sampleSDs = []
# for size in sampleSizes:
#     sems.append(sem(popSD, size))
#     means = []
#     for t in range(numTrials):
#         sample = random.sample(population, size)
#         means.append(sum(sample)/len(sample))
#     sampleSDs.append(numpy.std(means))
# pylab.plot(sampleSizes, sampleSDs,
#            label = 'Std of 50 means')
# pylab.plot(sampleSizes, sems, 'r--', label = 'SEM')
# pylab.title('SEM vs. SD for 50 Means')
# pylab.legend()


def getDiffs(population, sampleSizes):
    popStd = numpy.std(population)
    diffsFracs = []
    for sampleSize in sampleSizes:
        diffs = []
        for t in range(100):
            sample = random.sample(population, sampleSize)
            diffs.append(abs(popStd - numpy.std(sample)))
        diffMean = sum(diffs)/len(diffs)
        diffsFracs.append(diffMean/popStd)
    return pylab.array(diffsFracs)*100
    
def plotDiffs(sampleSizes, diffs, title, label):
    pylab.plot(sampleSizes, diffs, label = label)
    pylab.xlabel('Sample Size')
    pylab.ylabel('% Difference in SD')
    pylab.title(title)
    pylab.legend()

# sampleSizes = range(20, 600, 1)
# diffs = getDiffs(getHighs(), sampleSizes)
# plotDiffs(sampleSizes, diffs,
#           'Sample SD vs Population SD, Temperatures',
#            label = 'High temps')


def plotDistributions():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    makeHist(uniform, 'Uniform', 'Value', 'Frequency')
    pylab.figure()
    makeHist(normal, 'Gaussian', 'Value', 'Frequency')
    pylab.figure()
    makeHist(exp, 'Exponencial', 'Value', 'Frequency')
    
    
#plotDistributions()

def compareDists():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    sampleSizes = range(20, 600, 1)
    udiffs = getDiffs(uniform, sampleSizes)
    ndiffs = getDiffs(normal, sampleSizes)
    ediffs = getDiffs(exp, sampleSizes)
    plotDiffs(sampleSizes, udiffs,
              'Sample SD vc Population SD',
              'Uniform population')
    plotDiffs(sampleSizes, ndiffs,
              'Sample SD vs Population SD',
              'Normal population')
    plotDiffs(sampleSizes, ediffs,
              'Sample SD vs Population SD',
              'Exponencial population')

compareDists()