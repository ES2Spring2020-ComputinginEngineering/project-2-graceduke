#Grace Duke
#Project 2 Steps 2 and 3

import numpy as np
import matplotlib.pyplot as plt
import random 

# FUNCTIONS
# step 2

#Function openckdfile takes no arguments
#Opens the file containing the data for glucose, hemoglobin and classification
#Returns an array for each set of data
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#Function normalizeData takes 3 parameters (glucose, hemoglobin, and classification)
#Normalizes each data set so they are comparable
#Returns the 3 normalized arrays
def normalizeData(glucose, hemoglobin, classification):
    gnorm = (glucose - 70)/ (490-70)
    hnorm = (hemoglobin - 3.1) / (17.8 - 3.1)
    gnorm = np.array(gnorm)
    hnorm = np.array(hnorm)
    return (gnorm, hnorm, classification)

#Function graphData takes 3 arguments, gnorm, hnorm and classification
#Creates a scatter plot with hemoglobin on the x-axis and glucose on the y
#Points with classification 1 are blue and those with 0 are red
def graphData(gnorm, hnorm, classification):
    plt.scatter(hemoglobin, glucose)
    plt.xlabel('Hemoglobin')
    plt.ylabel('Glucose')
    plt.title ('CKD Classification by Hemoglobin and Glucose')
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.legend()
    plt.show()

#Function createTestCase takes no parameters
#Returns random values for a new glucose, hemoglobin test point
def createTestCase():
    newglucose = np.random.random()
    newhemoglobin = np.random.random()
    return (newhemoglobin, newglucose)

#Function takes 4 parameters glucose, newglucose, hemoglobin and newhemoglobin
#Creates an array of the distances using the distance formula
def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distance_array = np.array (np.sqrt((newhemoglobin - hemoglobin)**2 + (newhemoglobin - hemoglobin)**2))
    return distance_array

#Function takes 5 parameters, finds the minimum distance from the distance array
#Classifies the point based on the classification of the point with at minimum distance
def nearestNeighborClassifier (newglucose, newhemoglobin, glucose, hemoglobin, classification):
    nearest_neighbor = np.argmin (distance_array)
    new_classification= classification[nearest_neighbor]
    return new_classification 

#Function graphData takes 5 arguments, newglucose, newhemoglobin, glucose, hemoglobin and classification
#Creates a scatter plot with hemoglobin on the x-axis and glucose on the y
#Points with classification 1 are blue and those with 0 are red
def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.scatter(hemoglobin, glucose)
    plt.xlabel('Hemoglobin')
    plt.ylabel('Glucose')
    plt.title ('CKD Test Case Classification')
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot([newhemoglobin], [newglucose], marker = 'o', markersize = 5, color = 'orange')
    plt.legend()
    plt.show()

# step 3
#Function takes 6 parameters, newglucose, newhemoglobin, glucose, hemoglobin, classificiation, and k.
#The value for k determines the amount of points the function will use to classify the new point
#If more of the neighboring points are classified as 1, the new point will also be classified as 1, and vice versa
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
    distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sortedindices = np.argsort (distance_array)
    k_indices = sortedindices[:k]
    kclassifications = classification [k_indices]
    zeros = 0 
    ones = 0 
    for i in kclassifications:
        if i == 0:
            zeros = 1 + zeros
        if i == 1:
            ones = 1 + ones 
    if ones > zeros:
        kclass = 1
    else:
        kclass = 0
    return kclass

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
newglucose, newhemoglobin = createTestCase()
distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
new_classification = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphData(glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
kclass = kNearestNeighborClassifier(11, newglucose, newhemoglobin, glucose, hemoglobin, classification)
print("Classification:", new_classification)
print ("K Classification:" , kclass)
