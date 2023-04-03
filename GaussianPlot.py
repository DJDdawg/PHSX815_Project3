#! /usr/bin/env python

#Creates Plot of Data

#import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    
    data = [] # will turn 2D array into 1D array
    
    Nmeas = 1 #Will redefine later. 
    Nexp = 0 #will count 1 by 1. Each new line in data file is a new experiment.
    
    #Count total number of dice rolls and each count of each dice roll
    with open(InputFile) as ifile:
        for line in ifile: #Each line is a new experiment. 
            lineVals = line.split() #Each experiment.
            Nmeas = len(lineVals) #Each experiment has Nmeas measurements.
            
            for v in lineVals: #each measurement in an experiment.
               val = float(v) 
               data.append(val) #each measurement in the 2D array gets fed into a 1D array.

            Nexp += 1 

    #Calculate total amount of measurements throughout all experiments
    Ntot = Nmeas * Nexp
   
    #Print out data to see if working correctly
    #print(data) 
    
#Create graph of data
    data = np.asarray(data)
    
    n, bins, patches = plt.hist(data, 16, edgecolor = 'black', linewidth = 3, density = True, facecolor = 'orange', alpha=0.75)

# plot formating options
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('P(x | $\mu, \sigma$)', fontsize = 15)
    plt.title('Gaussian Distribution', fontsize = 20)
    plt.grid(True)
    plt.show()
