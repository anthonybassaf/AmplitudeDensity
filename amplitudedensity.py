import csv
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.style.use('seaborn')
 

def plotData():
    data = open('file1.csv', newline='')
    reader = csv.reader(data)
    values = list(reader)
    nums = list()


    for value in values:
        nums.append(float(value[0]))


    


    fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3, sharex = True, sharey = True)
    ax1.hist(nums, 10, density = 1, ec = "black")
    ax2.hist(nums, 50, density = 1, ec = "black")
    ax3.hist(nums, 100, density = 1, ec = "black")

    fig.suptitle("Amplitude for Bins  = 10, 50, 100")

    ax1.set_xlabel("Range")
    ax1.set_ylabel("Amplitude")

    ax2.set_xlabel("Range")
    ax2.set_ylabel("Amplitude")

    ax3.set_xlabel("Range")
    ax3.set_ylabel("Amplitude")

    plt.show()

plotData()
