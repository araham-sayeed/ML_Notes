import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from scipy.cluster.hierarchy import dendrogram, linkage
from gettext import npgettext
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
## confusion matrix
# actual = np.random.binomial(1, .9, size= 1000)
# predicted = np.random.binomial(1, .9, size= 1000)
# accuracy = metrics.accuracy_score(actual, predicted)
# precision = metrics.precision_score(actual, predicted)
# sensrecall = metrics.recall_score(actual, predicted)
# specify = metrics.recall_score(actual, predicted,pos_label= 0)
# f1score = metrics.f1_score(actual, predicted,pos_label= 0)
# confusion_matrix = metrics.confusion_matrix(actual, predicted)
# cm_display= metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels= [False, True])
# # cm_display.plot()
# # plt.show()

# print("accuracy=",accuracy)
# print("precision=",precision)
# print("sensrecall=",sensrecall)
# print("specify=",specify)
# print("f1score=",f1score)

## heirarical cluster

# x= [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
# y= [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# # plt.scatter(x, y)
# data= list(zip(x,y))
# # linkage_data= linkage(data, method='ward', metric='euclidean') # 1d dendogram
# # dendrogram(linkage_data)

#  # 2 d plot
# hierarchical_cluster= AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
# labels= hierarchical_cluster.fit_predict(data)
# plt.scatter(x, y, c=labels)
# plt.show()

## euclidean 

##  GridSearch

# iris = datasets.load_iris()
# x = iris['data']
# y= iris['target']
# LogisticRegression(max_iter= 10000)
# logit= LogisticRegression(max_iter = 10000)
# print(logit.fit(x, y))


### logistic regression

# x= np.array([ 3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# logr= linear_model.LogisticRegression()
# logr.fit(x, y)

# predicted = logr.predict(np.array([3.46]).reshape(-1,1))
# print(predicted)

# def logit2prob(logr, x):
#     log_odd = logr.coef_*x + logr.intercept_
#     odds = np.exp(log_odd)
#     probability = odds / (1 + odds)
#     return probability

# z= logit2prob(logr, x)
# print(z)


### training the dataset

# np.random.seed(2)
# s1= np.random.normal(3, 1, 100) # no of minute before purchase
# s2= np.random.normal(150, 40, 100)/s1 # amount of money spent on the purchase

# # plt.scatter(s1, s2)
# # plt.show()


# train_x= s1[:80]
# train_y= s2[:80]

# test_x= s1[80:]
# test_y= s2[80:]

# mymodel= np.poly1d(np.polyfit(train_x, train_y, 4))
# myline = np.linspace(0, 6, 100)
# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# # plt.scatter(test_x, test_y)
# plt.show()

## using R-squre method

# np.random.seed(2)
# s1= np.random.normal(3, 1, 100) # no of minute before purchase
# s2= np.random.normal(150, 40, 100)/s1 # amount of money spent on the purchase

# train_x= s1[:80]
# train_y= s2[:80]

# test_x= s1[80:]
# test_y= s2[80:]

# mymodel= np.poly1d(np.polyfit(train_x, train_y, 4))
# # r2= r2_score(train_y,mymodel(train_y))
# print("value: ",mymodel(5))


### Decision Tree

df = pd.read_csv("Comedian.csv")
# print(df)

d =  {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality']= df['Nationality'].map(d)
d= {'YES': 0, 'NO': 1}
df['Go'] = df['Go'].map(d)
# print(df)

features=['Age', 'Experience', 'Rank', 'Nationality']
x = df[features]
y= df['Go']

dtree = DecisionTreeClassifier()
dtree= dtree.fit(x,y)
plot_tree(dtree, feature_names= features)
plt.show()
print(dtree)