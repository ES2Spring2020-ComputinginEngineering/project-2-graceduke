This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Grace Duke Project 2- Biomedical Data Analysis

To run the code:

For NearestNeighborClassification.py, the code just needs to be run. The code produces 2 graphs, the CKD classification graph and the test case graph. Below the graphs the classification and well as the K-classification are printed.

For KMeansClustering_Functions.py, the code does not to be run, it simply holds the functions/algorithm used in the driver. This file 

K-Means Clustering Algorithm:

def openckdfile():  Function takes no arguments, opens the file containing the data for glucose, hemoglobin and classification and returns an array for each set of data.

def normalizeData(glucose, hemoglobin, classification): Function takes 3 parameters (glucose, hemoglobin, and classification)and normalizes each data set so they are comparable and returns the 3 normalized arrays

def centroid_points(k): Function takes one parameter, k to determine the number of centroids to be made and returns the random centroids

def assign_centroids(centroids, glucose, hemoglobin): Function takes 3 parameters, the random centroids, glucose and hemoglobin. It calculates the distance from each point to the centroid and then finds the smallest distance and these distance values are the assigned values for each centroid. The function returns the assignment and the distances for each centroid.

def update(k, c_assignment, glucose, hemoglobin): Function takes 4 parameters-- k (same from centroid_pints), c_assignments, glucose, and hemoglobin. It updates the centroid values to be more accurate by finding the mean glucose and hemoglobin. Returns the updated array.

def iterate(k, iterations): Function takes 2 parameters-- same k from centroid_points, used for update, and iterations which is the number of times the function will run.The normalized arrays are called, assign_centroids and update are in the while loop that continuously creates more accurate clusters.The function returns c_assignments, updated_array, glucose, hemoglobin, and classification

def graphKMeans(k, glucose, hemoglobin, c_assignment, update):Function takes 5 parameters and graphs the data returned by iterate. It graphs the points with a certain color based on its centroid assignment

def calc_positive_negatives(classification, c_assignment):Function takes 2 parameters, classification and c_assignment. If the classification are the same, they return either true positive or negative tests; otherwise, they return false postives/negatives. It returns the amount of true positives, negatives and false positives, negatives.

def percentages(TP, FP, TN, FN, CKD, nCKD):Function has 6 parameters, the return values of calc_positive_negatives.It calculates the percentages of each of the results, and returns the percentages

For KMeansClustering_Driver.py,you must input a number for k, as well as the number of iterations you want. Run this file for the results of the functions- graphs and the percentage values of true/false positives and negatives