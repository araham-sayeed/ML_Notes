import numpy as np
import matplotlib.pyplot as plt

# speed=[96, 94, 99, 101, 118, 87, 90, 94, 98, 91, 100]
# sharad= np.mean(speed)
# print("mean: ",sharad)
# sharad2= np.median(speed)
# print("median: ",sharad2)

# from scipy import stats
# sharad3= stats.mode(speed)
# print("mode: ",sharad3)

# speed2= [86,87,88,87,85,86]
# sharad4= np.std(speed2)
# print(sharad4)

# speed3= [32, 111, 138, 28, 59, 77, 97]
# sharad5= np.std(speed3)
# sharad6= np.
# print(sharad5)

# ages= [5,31,43,47,7,11,39,80,82,32,2,8,6,25,36,27,61,31,30]
# sharad= np.percentile(ages, 90)
# print(sharad)


### data distribution

# sharad= np.random.uniform(0.0, 5.0, 250)
# print(sharad)
# plt.hist(sharad, 5)
# plt.show()

## Big Data distribution

# sharad= np.random.uniform(0.0, 5.0, 100000)
# print(sharad)
# plt.hist(sharad,100)
# plt.show()

## normal data distribution

# sharad= np.random.normal(5.0, 1.0, 100000)
# plt.hist(sharad, 100)
# plt.show()

## scatter plot 

# x= [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y= [99,86,87,88,11,86,103,87,94,78,77,85,86]
# plt.scatter(x,y)
# plt.show()

# using random distribution

# x= np.random.normal(5.0, 2.0, 1000)
# y= np.random.normal(10.0, 3.0, 1000)

# plt.scatter(x, y)
# plt.show()

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

