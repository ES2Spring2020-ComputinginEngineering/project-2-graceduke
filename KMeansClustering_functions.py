#Grace Duke
#Project 2 Step 4 Function 

import numpy as np
import matplotlib.pyplot as plt
import random

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
    return gnorm, hnorm, classification


#Function takes one parameter, k to determine the number of centroids to be made
#Returns the random centroids
def centroid_points(k):
    centroids = np.random.rand(k,2)
    return centroids

#Function takes 3 parameters, the random centroids, glucose and hemoglobin
#Calculates the distance from each point to the centroid and then finds the smallest distance
#These distance values are the assigned values for each centroid 
#Returns the assignment and the distances for each centroid
def assign_centroids (centroids, glucose, hemoglobin):
    #glucose = openckdfile()
    k = centroids.shape[0]
    d_array = np.zeros((158, k))
    c_assignments = np.zeros(158) 
    for i in range(k):
        g = centroids[i,1]
        h = centroids [i,0]
        distances = np.array (np.sqrt(((h-hemoglobin)**2)+((g-glucose)**2)))
        d_array[:,i]= distances
    c_assignments = np.argmin(d_array, axis = 1)
    return c_assignments#, d_array

#Function takes 4 parameters-- k (same from centroid_pints), c_assignments, glucose, and hemoglobin
#Updates the centroid values to be more accurate by finding the mean glucose and hemoglobin
#Returns the updated array
def update(k, c_assignments, glucose, hemoglobin):
    updated_array = np.zeros((k,2))
    h_centroid = np.zeros ((1))
    g_centroid = np.zeros((1))
    for i in range (updated_array.shape[0]):
        h_centroid = np.mean(hemoglobin[c_assignments == i])
        g_centroid = np.mean(glucose[c_assignments == i])
        updated_array[i] = np.append(h_centroid, g_centroid)
    return updated_array

#Function takes 2 parameters same k from centroid_points, used for update, and
#iterations which is the number of times the function will run
#The normalized arrays are called, assign_centroids and update are in the while loop that 
#continuously creates more accurate clusters.
#Returns c_assignments, updated_array, glucose, hemoglobin, and classification
def iterate(k, iterations):
    glucose, hemoglobin, classification = openckdfile()
    gnorm, hnorm, classification = normalizeData(glucose, hemoglobin, classification)
    centroids = centroid_points(k)
    c_assignments = assign_centroids(centroids, gnorm, hnorm)
    updated_array = centroid_points(k)
    while iterations != 0 :
        c_assignments = assign_centroids(updated_array, gnorm, hnorm)
        updated_array = update(k, c_assignments, gnorm, hnorm)
        iterations = iterations - 1
    return c_assignments, updated_array, glucose, hemoglobin, classification

#Function takes 5 parameters and graphs the data returned by iterate
#Graphs the points with a certain color based on its centroid assignment
def graphKMeans(k, glucose, hemoglobin, c_assignment, centroids):
    glucose, hemoglobin, classification = openckdfile()
    gnorm, hnorm, classification = normalizeData(glucose, hemoglobin, classification)
    #centroids = centroid_points(k)
    #c_assignment = assign_centroids (centroids, glucose, hemoglobin)
    plt.figure()
    for i in range(k):
        rcolor = np.random.rand(3,)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
        plt.plot(hnorm[c_assignment== i], gnorm[c_assignment==i], ".", label = "Class " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

#Function takes 2 parameters, classification and c_assignment
#If the classification are the same, they return either true positive or negative tests
#Otherwise, they return false postives/negatives
#Returns the amount of true positives, negatives and false positives, negatives
def calc_positive_negatives(classification, c_assignment):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    CKD = 0
    nCKD= 0
    for i in range (158):
        if (classification[i] + c_assignment[i])==2:
            TN += 1
            nCKD +=1
        elif (classification[i] + c_assignment[i])==0:
            TP += 1
            CKD +=1
        elif (classification[i] + c_assignment[i])==1:
            if classification[i] == 0:
                FN +=1
                CKD +=1
            elif classification[i] == 1:
                FP +=1
                nCKD +=1
    return TP, FP, TN, FN, CKD, nCKD

#Function has 6 parameters, return values of calc_positive_negatives
#Calculates the percentages of each of the results
def percentages(TP, FP, TN, FN, CKD, nCKD):
    percentTP = "Percentage of True Positves:" + str((TP/CKD)*100) + "%"
    percentFP = "Percentage of False Positives:" + str((FP/nCKD)*100) + "%"
    percentTN = "Percentage of True Negatives:" + str((TN/nCKD)*100)+ "%"
    percentFN = "Percentage of False Negatives:" + str((FN/CKD)*100)+ "%"
    return percentTP, percentFP, percentTN, percentFN


    
    
    
    
    