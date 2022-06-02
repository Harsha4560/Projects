import os
os.system('cls||clear')
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import random
sns.set()
from sklearn.cluster import KMeans

#reading the given csv file
data = pd.read_csv('C:\\Users\\Harsha\\Desktop\\python ml\\spotify ml\\genres_v2.csv')
#print(data)

#selecting only the required quantities form the csv
x = data.iloc[:,0:11]

#to find the number of clusters needed
#wcss = []
#for i in range(1, 20):
#    kmeans = KMeans(i)
#    kmeans.fit(x)
#    wcss_iter = kmeans.inertia_
#    wcss.append(wcss_iter)
#    print(i)
#no_clusters = range(1, 20)
#plt.plot(no_clusters, wcss)
#plt.title('Elbow finder')
#plt.xlabel('No. of clusters')
#plt.ylabel('WCSS')
#plt.show()
#the number of clusters needed was found to be 5

kmeans = KMeans(5)
kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)
data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters
#print(data_with_clusters['Clusters'])

print('Enter the name of song you like the most: ')
song = input()
clusternum = None
for index, row in data_with_clusters.iterrows():
    if row['song_name'] == song:
        clusternum = row['Clusters']
        break
if clusternum == None:
    print('Song does not exist')
else:
    print('\n\n Other songs you might like are')
    for index, row in data_with_clusters.iterrows():
        if row['Clusters'] == clusternum:
            if random.choice([True]+100*[False]):
                print(row['song_name'])