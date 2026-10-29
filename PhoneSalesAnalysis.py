import numpy as np
import pandas as pd
import plotly.express as px

sharadData= pd.read_csv('apple_products.csv')
# print(sharadData.isnull().sum())

# Checking number of reviews

highest_rated = sharadData.sort_values(by=["Star Rating"], ascending= False)
highest_rated= highest_rated.head(10)


print(highest_rated['Product Name'])
iphone = highest_rated['Product Name'].value_counts()
label=iphone.index
counts= highest_rated['Number Of Ratings']
figure= px.bar(highest_rated, x=label, y= counts, title= 'Number of highest rating of iphones')
figure.show()

# checking number of reviews


highest_rated = sharadData.sort_values(by=["Star Rating"], ascending= False)
highest_rated= highest_rated.head(10)


print(highest_rated['Product Name'])
iphone = highest_rated['Product Name'].value_counts()
label=iphone.index
counts= highest_rated['Number Of Reviews']
figure= px.bar(highest_rated, x=label, y= counts, title= 'Number of highest review of iphones')
figure.show()

# checking scatter plot

figure= px.scatter(data_frame=sharadData, x='Number Of Ratings',
                y='Sale Price',
                size='Discount Percentage',
                trendline='ols',
                title='relationship between sale price and number of rating of iphones')
figure.show()

figure= px.scatter(data_frame=sharadData, x='Number Of Ratings',
                y='Discount Percentage',
                size='Sale Price',
                trendline='ols',
                title='relationship between discount percentage and number of rating of iphones')
figure.show()

figure= px.scatter(data_frame=sharadData, x='Number Of Reviews',
                y='Sale Price',
                size='Discount Percentage',
                trendline='ols',
                title='relationship between sale price and number of review of iphones')
figure.show()

figure= px.scatter(data_frame=sharadData, x='Number Of Reviews',
                y='Discount Percentage',
                size='Sale Price',
                trendline='ols',
                title='relationship between Discount Percentage and number of review of iphones')
figure.show()



