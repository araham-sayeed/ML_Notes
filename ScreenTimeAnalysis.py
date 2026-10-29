import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime.csv")

# print(data.describe())

figure = px.bar(data_frame=data, x='Date', y='Usage', color='App',
                title='Usage Graph')
figure.show()


figure = px.bar(data_frame=data, x='Date', y='Notifications', color='App',
                title='Notification Graph')
figure.show()


figure = px.bar(data_frame=data, x='Date', y='Times opened', color='App',
                title='number of time opened Graph')
figure.show()


figure= px.scatter(data_frame=data, x='Notifications', y= 'Usage', size='Notifications',
                   trendline='ols', title='relationship between number of notification and amount of usage')
figure.show()

