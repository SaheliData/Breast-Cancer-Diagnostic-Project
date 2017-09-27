# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 04:39:20 2016

@author: Saha
"""

import numpy as np
import urllib2
from sys import argv
import matplotlib.pyplot as plt
import math
import random
import subprocess
import pandas as pd
import urllib3 as url
import random as rnd


points = list()
i_list = list()
final_data = list()
k = raw_input("Enter the value for K:")
k = int(k)
iterate_bound = raw_input("Enter the value for iteration count:")
iterate_bound = int(iterate_bound)
threshold_bound = raw_input("Enter the threshold value:")
threshold_bound = int(threshold_bound)

def initialize_centroid(points, k):
    data_points = points.copy()
    Index_value = list()
    ini_centroid = list()
    data_count = data_points.shape
    row_count = int(data_count[0])
    for i in range(k):
        Index_value.append(rnd.randrange(0,row_count))
    for j in Index_value:
        ini_centroid.append(data_points.ix[j])
    print "Initial centroid",ini_centroid
    return ini_centroid
        

def initial_assign_data(points,k):
    ini_centroid = initialize_centroid(points,k)
    k_mean = k
    data_points = points.copy()
    distance = dict()
    clusters = [[] for i in ini_centroid]
    #clusters = dict()
    min_distance = dict()
## Assigning data for initial centroid
    for i in range(len(data_points)):
        for j in range(len(ini_centroid)):
            distance[j] = np.sqrt(sum(np.square(abs((np.array(data_points.ix[i]) - np.array(ini_centroid[j]))))))
        min_distance = min(distance.values())
        print min_distance
        print distance
        print type(distance)
        for key,v in distance.iteritems():
            if distance[key] == min_distance:
                clusters[key].append(data_points.ix[i])
    print "Initial assigned data", clusters
    return clusters

def update_Centroid_data_assign(points,k,iterate_bound,threshold_bound):
    data_points = points.copy()
    k_mean = k
    first_clusters = initial_assign_data(points,k)
    iterate_count = 0
    iterate_count = iterate_count + 1  # First iteration already done in assign_data function
    new_clusters = initial_assign_data(points,k)
    mean_centroid = list()
    ini_iterate_count = 0
    new_centroid = list()
    clusters = list()
## Update centroids except the first centroid initialization
    for i in range(k_mean):
        for j in range(len(data_points.ix[0])):
            sum = 0
            for k in range(1,(len(new_clusters[i]))):
                sum = sum + new_clusters[i][k][j]
            if (len(new_clusters[i]) == 0):
                mean_centroid = sum
            else:
                mean_centroid = sum / len(new_clusters[i])
                new_centroid.append(mean_centroid)
                #new_centroid.append(mean_centroid)
            iterate_count = iterate_count + 1
    print "New Centroids",new_centroid
## Threshold value checking after the first iteration
    if iterate_count == 1:
        ini_centroid = initialize_centroid(points, k)
        for i in range(len(ini_centroid)):
            for j in range(len(new_centroid)):
                threshold_value = np.sqrt(sum(np.square(abs((np.array(ini_centroid[i]) - np.array(new_centroid[j]))))))
        print "Initial threshold value",threshold_value

## Threshold value checking for after the second iteration
    elif iterate_count < iterate_bound:
        for i in range(len(new_centroid)):
            threshold_value = np.sqrt(sum(np.square(abs((np.array(new_centroid[i-1]) - np.array(new_centroid[i]))))))
    print "Threshold values after the first calculation", threshold_value

## Data assigning to the new centroid
    if (threshold_value < threshold_bound and iterate_count <= iterate_count):
        for i in range(len(data_points)):
            for j in range(len(new_centroid)):
                distance[j] = np.sqrt(sum(np.square(abs((np.array(data_points.ix[i]) - np.array(ini_centroid[j]))))))
            min_distance = min(distance.values())
            for key, v in distance.iteritems():
                if distance[key] == min_distance:
                    clusters[key].append(data_points.ix[i])
    else:
        print "Maximum threshold value",threshold_value,"or iteration count Achieved",iterate_count
    print "List of the clusters",clusters
#    return clusters

#Program starts here

http = url.PoolManager()
resp = http.request('GET', 'http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data')
tgtf = open('E:\\IUB Fall\\1st Sem\\Data Mining\\Assignments\\A-2\\restData.csv', 'w')
tgtf.write('sampler,clump_thickness,cell_size,cell_shape,adhesion,epithelial_cell_size,nuclei,chromatin,normal_nucleoli,mitoses,class\n')

if resp.status == 200 :
    wdat = resp.data
    tgtf.write(wdat.decode('utf-8'))

    tgtf.close()
    aldt = pd.read_csv("E:\\IUB Fall\\1st Sem\\Data Mining\\Assignments\\A-2\\restData.csv", header = 0)
    data = aldt.ix[:, 1:10]

final_data = data.replace("?",0)
final_data['nuclei'] = final_data['nuclei'].astype(int)
initialize_centroid(final_data,k)
initial_assign_data(final_data,k)
#update_Centroid_data_assign(final_data,k,iterate_bound,threshold_bound)






     
         



    


