### k-mean

# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# data = list(zip(x, y))
# inertias = []

# for i in range(1,11):
#     kmeans = KMeans(n_clusters=i)
#     kmeans.fit(data)
#     inertias.append(kmeans.inertia_)

# plt.plot(range(1,11), inertias, marker='o')
# plt.title('Elbow method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()

# kmeans = KMeans(n_clusters=2)
# kmeans.fit(data)

# plt.scatter(x, y, c=kmeans.labels_)
# plt.show()

### pca 

import pandas as pd
import numpy as np

# Here we are using inbuilt dataset of scikit learn
from sklearn.datasets import load_breast_cancer

# instantiating
cancer = load_breast_cancer(as_frame=True)
# creating dataframe
df = cancer.frame

# checking shape
print('Original Dataframe shape :',df.shape)

# Input features
X = df[cancer['feature_names']]
print('Inputs Dataframe shape   :', X.shape)