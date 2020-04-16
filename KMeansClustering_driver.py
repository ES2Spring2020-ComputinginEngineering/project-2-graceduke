#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions

glucose, hemoglobin, classification = kmc.openckdfile()
gnorm, hnorm, classification = kmc.normalizeData(glucose, hemoglobin, classification)

k = 3


centroids = kmc.centroid_points(k)
c_assignment = kmc.assign_centroids (centroids, gnorm, hnorm)

c_assignment, updated_array, gnorm, hnorm, classification = kmc.iterate(k, 100)

kmc.graphKMeans(k, gnorm, hnorm, c_assignment, updated_array)

TP, FP, TN, FN, CKD, nCKD = kmc.calc_positive_negatives(classification, c_assignment)
print (kmc.percentages(TP, FP, TN, FN, CKD, nCKD))