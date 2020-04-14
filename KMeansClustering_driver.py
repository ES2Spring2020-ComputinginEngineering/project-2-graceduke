#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions

glucose, hemoglobin, classification = kmc.openckdfile()
gnorm, hnorm, classification = kmc.normalizeData(glucose, hemoglobin, classification)

k = 3

centroids = kmc.centroid_points(k)
c_assignment = kmc.assign_centroids (centroids, glucose, hemoglobin)

#c_assignments, updated_array, glucose, hemoglobin, classification = kmc.iterate(2, 100)
#
#kmc.graphingKMeans(glucose, hemoglobin, c_assignment, updated_array)

TP, FP, TN, FN, CKD, nCKD = kmc.calc_positive_negatives(classification, c_assignment)
print( kmc.calc_percentages(TP, FP, TN, FN, CKD, nCKD))
