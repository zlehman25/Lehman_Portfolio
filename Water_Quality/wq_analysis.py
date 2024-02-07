#questions to answer:
#what regions, cities, etc have the highest/lowest air pollution and water quality?

#importing analysis tools
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Path of the file to read, reading the file into a variable
filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Water_Quality\\Cities1.csv"
city_data = pd.read_csv(filepath)


#Creating data frames for graphing
avg_df = city_data.groupby('Country')[['WaterPollution', 'AirQuality']].mean()
water_df = city_data.groupby('Country')[['WaterPollution']].mean()
air_df = city_data.groupby('Country')[['AirQuality']].mean()

#Creating a plot to show air quality and water pollution correlation
g1 = sns.lmplot(data=avg_df, 
                x='AirQuality', 
                y='WaterPollution'
                )

g1.fig.set_figwidth(16)
g1.fig.set_figheight(10)
plt.title('Relation of Air Quality and Water Pollution by Country')
plt.ylabel('Water Pollution')
plt.xlabel('Air Quality')
plt.show()


#Creating plots to show the countries with the worst and best air quality

#Best air
g2 = sns.barplot(data=air_df.sort_values(by=['AirQuality', 'Country'], ascending = False).head(10),
                 x='Country',
                 y='AirQuality',
                 hue = 'Country'
                 )
plt.show()

#Worst air
g3 = sns.barplot(data=air_df.sort_values(by=['AirQuality', 'Country'], ascending = False).tail(10),
                 x='Country',
                 y='AirQuality',
                 hue = 'Country'
                 )
plt.show()
#Creating a plot to show the countries with the worst water pollution

#Worst water
g4 = sns.barplot(data=water_df.sort_values(by=['WaterPollution', 'Country'], ascending = False).head(10),
                 x='Country',
                 y='WaterPollution',
                 hue = 'Country'
                 )
plt.show()

#Best water
g4 = sns.barplot(data=water_df.sort_values(by=['WaterPollution', 'Country'], ascending = False).tail(10),
                 x='Country',
                 y='WaterPollution',
                 hue = 'Country'
                 )
plt.show()