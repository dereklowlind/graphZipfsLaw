import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
from scipy import stats
import csv


def plotZipf(intValues,ax):
    intValues.sort(reverse=True)
    # print(intValues)
    intValuesRank = []
    for i in range(len(intValues)):
        intValuesRank.append(i+1)

    logx = [math.log(value) for value in intValues]
    logy = [math.log(value) for value in intValuesRank]
    ax.plot(logx, logy, 'o', label='original data')


    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(logx,logy)
    print("slope: %f    intercept: %f   r_value: %f" % (slope, intercept, r_value))

    line = [ (slope*value)+intercept for value in logx]
    ax.plot(logx, line, 'r', label='r_value = \n' + str(r_value)[:6])
    plt.legend()

    ax.set_xlabel('log value')
    ax.set_ylabel('log rank')
    return ax

def graphZipfsLaw():
    with open('Canada2001.csv') as csvFile:
        csvReader = csv.reader(csvFile)
        citySizes = [int(row[3]) for row in csvReader]
        # print(citySizes)
        ax1 = plt.subplot(131)
        ax1.set_title("Canada City Sizes")
        ax1 = plotZipf(citySizes,ax1)
        csvFile.close()
    
    with open('USA2010.csv') as csvFile:
        csvReader = csv.reader(csvFile)
        citySizes = [int(row[2]) for row in csvReader]
        # print(citySizes)
        ax2 = plt.subplot(132)
        ax2.set_title("USA City Sizes")
        ax2 = plotZipf(citySizes,ax2)
        csvFile.close()

    with open('World2017.csv') as csvFile:
        csvReader = csv.reader(csvFile)
        citySizes = [int(row[3]) for row in csvReader]
        # print(citySizes)
        ax3 = plt.subplot(133)
        ax3.set_title("World City Sizes")
        ax3 = plotZipf(citySizes,ax3)
        csvFile.close()
    
    plt.show()
   
graphZipfsLaw()