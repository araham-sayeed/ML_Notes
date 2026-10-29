### Linear regression
import matplotlib.pyplot as plt 
from scipy import stats  ## scientific python
import numpy as np
from sklearn.metrics import r2_score
from sklearn import linear_model
import pandas as pd

# x= [5,7,8,7,2,17,2,9,4,11,12,9,6]   # x is year of car
# y= [99,86,87,88,11,86,103,87,94,78,77,85,86]  # y is speed of car

# # plt.scatter(x, y)
# # plt.show()

# slope, intercept, r, p, std_err= stats.linregress(x,y)

# def myfunc(x):
#     return slope * x + intercept

# mymodel= list(map(myfunc, x))
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

# ## line to make our compiler able to draw

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


### r for relationship

# x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
# y= [99,86,87,88,11,86,103,87,94,78,77,85,86] 

# slope, intercept, r, p ,std_err = stats.linregress(x, y)

# print(r)

## predicting future values

# x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
# y= [99,86,87,88,11,86,103,87,94,78,77,85,86] 

# slope, intercept, r , p, std_err = stats.linregress(x, y)

# def myFunc(x):
#     return slope*x + intercept

# speed = myFunc(10) # input -> 10 year old car

# print(speed)

## bad fit

# x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5,36, 66, 72, 40]
# y = [21, 46, 3, 36, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# print(r)

# def myFunc(x):
#     return slope*x + intercept

# myModel = list(map(myFunc, x))
# plt.scatter(x, y)
# plt.plot(x, myModel)
# plt.show()


## polynmial regression

# x= [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y= [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99, 100]

# plt.scatter(x, y)

# plt.show()


# x= [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y= [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99, 100]
# myModel= np.poly1d(np.polyfit(x, y, 3))
# print(r2_score(y, myModel(x)))
# speed  = myModel(17)
# print(speed)

# myline = np.linspace(1, 22, 100)
# plt.scatter(x, y)
# plt.plot(myline, myModel(myline))
# plt.show()


## What about the bad fit


# x= [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29,48, 64, 6, 5, 36, 66,72, 40]
# y= [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47,15]
# myModel= np.poly1d(np.polyfit(x, y, 3))
# myLine = np.linspace(2, 95, 100)

# plt.scatter(x, y)
# plt.plot(myLine, myModel(myLine))
# plt.show()

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# scale= StandardScaler()
# df = pd.read_csv("Car.csv")
# x= df[['Weight','Volume']]
# scaledx = scale.fit_transform(x)
# print(scaledx)


# scale= StandardScaler()
# df = pd.read_csv("Car.csv")
# x= df[['Weight','Volume']]
# y= df['CO2']
# x= scale.fit_transform(x)

# regr = linear_model.LinearRegression()
# scaled_input = scale.transform([[2300, 1.3]])

# predictedco2 = regr.predict(scaled_input)
# print(predictedco2)

