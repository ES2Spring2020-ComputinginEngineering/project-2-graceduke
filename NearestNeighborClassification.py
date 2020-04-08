#Grace Duke
#Project 2 Steps 2 and 3

import numpy as np
import matplotlib.pyplot as plt
import random
import math 

# FUNCTIONS
# steo 2
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    gnorm = (glucose - 70)/ (490-70)
    hnorm = (hemoglobin - 3.1) / (17.8 - 3.1)
    gnorm = np.array(gnorm)
    hnorm = np.array(hnorm)
    return (gnorm, hnorm, classification)

def graphData(glucose, hemoglobin, classification):
    plt.scatter(hemoglobin, glucose)
    plt.xlabel('Hemoglobin')
    plt.ylabel('Glucose')
    plt.title ('CKD Classification by Hemoglobin and Glucose')
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.legend()
    plt.show()

def createTestCase():
    newglucose = np.random.randint(1,500)
    newhemoglobin = np.random.randint(1,20)
    return (newhemoglobin, newglucose)
    
#def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
#    distance_array = np.array (math.sqrt((newhemoglobin - hemoglobin)**2 + (newhemoglobin - hemoglobin)**2))
#    return distance_array

def nearestNeighborClassifier (newglucose, newhemoglobin, glucose, hemoglobin, classification):
    nearest_neighbor = np.argmin (distance_array)
    new_classification= classification[nearest_neighbor]
    return new_classification 

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.scatter(hemoglobin, glucose)
    plt.xlabel('Hemoglobin')
    plt.ylabel('Glucose')
    plt.title ('CKD Test Case Classification')
    plt.plot([newhemoglobin], [newglucose], marker = 'o', markersize = 5, color = 'green')
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.legend()
    plt.show()

# step 3
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
    
    return (newglucose, newhemoglobin)

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
newglucose, newhemoglobin = createTestCase()
#distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
new_classification = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)

graphData(glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
