#! /usr/bin/env python

#Import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng


# main function for our Analysis
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of data file ")
        print ("   -Mean [float number]  Mean of the Gaussian Distribution")
        print ("   -Sigma [float number]  Standard Deviation of the Gaussian Distribution")
        print
        sys.exit(1)
        
    #Initialize Variables
    Mean = 0 #mean of gaussian distribution
    Sigma = 1 #standard deviation of gaussian distribution
    Nmeas = 0 #Will redefine later. 
    Nexp = 0 #will count 1 by 1. Each new line in data file is a new experiment.
    
    #System Inputs          
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]

    if '-Mean' in sys.argv:
        p = sys.argv.index('-Mean')
        ptemp = float(sys.argv[p+1])
        Mean = ptemp

    if '-Sigma' in sys.argv:
        p = sys.argv.index('-Sigma')
        ptemp = float(sys.argv[p+1])
        Sigma = ptemp
           
    #Analyze Data
    data_0 = [] # will turn 2D array into 1D array
    
    #Count Nmeas and Nexp
    with open(InputFile0) as ifile:
        for line in ifile: #Each line is a new experiment. 
            lineVals = line.split() #All measurements in one line (experiment) 
            Nmeas = len(lineVals) #Each experiment has Nmeas measurements (constant).       
            
            for v in lineVals: #all measurements in a single experiment
               val = float(v) #turns string into float
               data_0.append(val) #each measurement gets fed into a 1D array.

            Nexp += 1

    #Print out results to see if correct
    #print(data_0) 
    print(f"Number of experiments: {Nexp}")
    print(f"Number of measurements/experiment: {Nmeas}")
    
    #Calculate Log Likelihood for one measurement
    def Gaussloglikelihood(measurement, Mean, Sigma):
        GLL =  -1/2 * np.log(2 * np.pi) - 1/2 * np.log(Sigma**2) - 1/(2*Sigma**2) * (measurement - Mean)**2
        return GLL
    
    #make sure function works
    #print(f"likelihood of x = 0.3: {np.exp(Gaussloglikelihood(0.3, 1.0, 1.0))}")
    
    #analytical solution for maximum likelihood
    x_max = Mean
    y_max = np.exp(Gaussloglikelihood(x_max, Mean, Sigma))
    
    #error on analytical solution
    
    
    print(f"Likelihood is maximized at x = {x_max} for the analytical solution")
    
    
    #numerical maximization using Scipy
    def f(x):
        f = -1/2 * np.log(2 * np.pi) - 1/2 * np.log(Sigma**2) - 1/(2*Sigma**2) * (x - Mean)**2
        return -1 * f
    
    result = optimize.minimize_scalar(f) #maximize
    print(f'Scipy minimization was successful: {result.success}') # check if solver was successful

    x_num = result.x
    print(f'numerical x-value found to maximize likelihood: {x_num}')
    
    num_result = np.exp(-1 * f(x_num))
    print(f'maximal value: {num_result}')
    
    
    #plotting likelyhood
    x = np.linspace(-2, 4, 10000)
    y= []
    
    for i in range(len(x)):
        y.append(np.exp(Gaussloglikelihood(x[i], Mean, Sigma)))
        
    plt.plot(x,y, label = 'numerical evaluations')
    plt.plot(x_max, y_max, color = 'red', marker = 'o', label = 'analytical maximum')
    plt.plot(x_num, num_result, color = 'green', marker = 'v', label = 'numerical maximum')
    
    plt.xlabel('Gaussian parameter')
    plt.ylabel('Likelihood')
    
    plt.title('Likelihood for various values of the parameter')
    
    plt.grid()
    plt.legend(loc = 'lower center')
    plt.show()
    
    
    
