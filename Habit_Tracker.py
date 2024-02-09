#importing analysis tools
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#function plotter - create function for each habit that returns a variety of graphs
def diet_charter():
    
    #Path of the file to read, reading the file into a variable
    filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Habit_Tracker\\habit_tracker.csv"
    habit_data = pd.read_csv(filepath)
    
    #Converting the date from the habit_data data frame into a full date and adding the day of the week and month based on the full date
    habit_data['date'] = pd.to_datetime(habit_data['date'])
    habit_data['day_of_week'] = habit_data['date'].dt.day_name()
    habit_data['month'] = habit_data['date'].dt.month_name()

    #Creating a pie chart - group is not working correctly
    labels = sorted((set(habit_data['diet'])))
    plt.pie(habit_data.groupby('diet')['diet'].count(), autopct='%1.1f%%')
    plt.figure(1, figsize=(6,6))
    plt.legend(labels=labels, loc='best')
    plt.title('Diet Habit Breakdown YTD')
    plt.show()

    #Creating a bar chart with outcome by day of the week
    sns.set(style='white')
    sns.countplot(habit_data, x="day_of_week", hue="diet", palette='deep')
    plt.title('Diet Habits by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week')
    plt.ylabel('Count of Diet Habit')
    plt.show()

    #Creating a bar chart with outcome by month
    sns.set(style='white')
    sns.countplot(habit_data, x="month", hue="diet", palette='deep')
    plt.title('Diet Habits by Month', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Count of Diet Habit')
    plt.show()

    #Creating a chart to see if falloff follows a pattern
    def count_bads(series, habit):
        return (series == habit).sum()

    habit = 'bad'

    habit_data["falloff"] = habit_data.apply(func=lambda row: count_bads(row, habit), axis=1)
    sns.set_theme(style="darkgrid")
    sns.lineplot(data=habit_data, x="date", y="falloff")
    plt.title('Habit Falloff Over Time', fontsize=16)
    plt.xlabel('Day')
    plt.ylabel('Falloff (count of habits recorded as "bad")')
    plt.show()

