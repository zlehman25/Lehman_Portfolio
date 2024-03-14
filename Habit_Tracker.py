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

    #Creating a pie chart - 
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

def spend_charter():
    
    #Path of the file to read, reading the file into a variable
    filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Habit_Tracker\\habit_tracker.csv"
    habit_data = pd.read_csv(filepath)
    
    #Converting the date from the habit_data data frame into a full date and adding the day of the week and month based on the full date
    habit_data['date'] = pd.to_datetime(habit_data['date'])
    habit_data['day_of_week'] = habit_data['date'].dt.day_name()
    habit_data['month'] = habit_data['date'].dt.month_name()

    #Creating a pie chart - 
    labels = sorted((set(habit_data['spending'])))
    plt.pie(habit_data.groupby('spending')['spending'].count(), autopct='%1.1f%%')
    plt.figure(1, figsize=(6,6))
    plt.legend(labels=labels, loc='best')
    plt.title('Spending Habit Breakdown YTD')
    plt.show()

    #Creating a bar chart with outcome by day of the week
    sns.set(style='white')
    sns.countplot(habit_data, x="day_of_week", hue="spending", palette='deep')
    plt.title('Spending Habits by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week')
    plt.ylabel('Count of Spending Habit')
    plt.show()

    #Creating a bar chart with outcome by month
    sns.set(style='white')
    sns.countplot(habit_data, x="month", hue="spending", palette='deep')
    plt.title('Spending Habits by Month', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Count of Spending Habit')
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

def yoga_charter():
    
    #Path of the file to read, reading the file into a variable
    filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Habit_Tracker\\habit_tracker.csv"
    habit_data = pd.read_csv(filepath)
    
    #Converting the date from the habit_data data frame into a full date and adding the day of the week and month based on the full date
    habit_data['date'] = pd.to_datetime(habit_data['date'])
    habit_data['day_of_week'] = habit_data['date'].dt.day_name()
    habit_data['month'] = habit_data['date'].dt.month_name()

    #Creating a pie chart - 
    labels = sorted((set(habit_data['yoga'])))
    plt.pie(habit_data.groupby('yoga')['yoga'].count(), autopct='%1.1f%%')
    plt.figure(1, figsize=(6,6))
    plt.legend(labels=labels, loc='best')
    plt.title('Yoga Habit Breakdown YTD')
    plt.show()

    #Creating a bar chart with outcome by day of the week
    sns.set(style='white')
    sns.countplot(habit_data, x="day_of_week", hue="yoga", palette='deep')
    plt.title('Yoga Habits by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week')
    plt.ylabel('Count of Yoga Habit')
    plt.show()

    #Creating a bar chart with outcome by month
    sns.set(style='white')
    sns.countplot(habit_data, x="month", hue="yoga", palette='deep')
    plt.title('Yoga Habits by Month', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Count of Yoga Habit')
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

def gym_charter():
    
    #Path of the file to read, reading the file into a variable
    filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Habit_Tracker\\habit_tracker.csv"
    habit_data = pd.read_csv(filepath)
    
    #Converting the date from the habit_data data frame into a full date and adding the day of the week and month based on the full date
    habit_data['date'] = pd.to_datetime(habit_data['date'])
    habit_data['day_of_week'] = habit_data['date'].dt.day_name()
    habit_data['month'] = habit_data['date'].dt.month_name()

    #Creating a pie chart - 
    labels = sorted((set(habit_data['gym'])))
    plt.pie(habit_data.groupby('gym')['gym'].count(), autopct='%1.1f%%')
    plt.figure(1, figsize=(6,6))
    plt.legend(labels=labels, loc='best')
    plt.title('Gym Habit Breakdown YTD')
    plt.show()

    #Creating a bar chart with outcome by day of the week
    sns.set(style='white')
    sns.countplot(habit_data, x="day_of_week", hue="gym", palette='deep')
    plt.title('Gym Habits by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week')
    plt.ylabel('Count of Gym Habit')
    plt.show()

    #Creating a bar chart with outcome by month
    sns.set(style='white')
    sns.countplot(habit_data, x="month", hue="gym", palette='deep')
    plt.title('Gym Habits by Month', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Count of Gym Habit')
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

def learn_charter():
    
    #Path of the file to read, reading the file into a variable
    filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Habit_Tracker\\habit_tracker.csv"
    habit_data = pd.read_csv(filepath)
    
    #Converting the date from the habit_data data frame into a full date and adding the day of the week and month based on the full date
    habit_data['date'] = pd.to_datetime(habit_data['date'])
    habit_data['day_of_week'] = habit_data['date'].dt.day_name()
    habit_data['month'] = habit_data['date'].dt.month_name()

    #Creating a pie chart - 
    labels = sorted((set(habit_data['learning'])))
    plt.pie(habit_data.groupby('learning')['learning'].count(), autopct='%1.1f%%')
    plt.figure(1, figsize=(6,6))
    plt.legend(labels=labels, loc='best')
    plt.title('Learning Habit Breakdown YTD')
    plt.show()

    #Creating a bar chart with outcome by day of the week
    sns.set(style='white')
    sns.countplot(habit_data, x="day_of_week", hue="learning", palette='deep')
    plt.title('Learning Habits by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week')
    plt.ylabel('Count of learn Habit')
    plt.show()

    #Creating a bar chart with outcome by month
    sns.set(style='white')
    sns.countplot(habit_data, x="month", hue="learning", palette='deep')
    plt.title('Learning Habits by Month', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Count of Learning Habit')
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

def read_charter():
    
    #Path of the file to read, reading the file into a variable
    filepath = "C:\\Users\\Zach\\python\\Lehman_Portfolio\\Habit_Tracker\\habit_tracker.csv"
    habit_data = pd.read_csv(filepath)
    
    #Converting the date from the habit_data data frame into a full date and adding the day of the week and month based on the full date
    habit_data['date'] = pd.to_datetime(habit_data['date'])
    habit_data['day_of_week'] = habit_data['date'].dt.day_name()
    habit_data['month'] = habit_data['date'].dt.month_name()

    #Creating a pie chart - 
    labels = sorted((set(habit_data['reading'])))
    plt.pie(habit_data.groupby('reading')['reading'].count(), autopct='%1.1f%%')
    plt.figure(1, figsize=(6,6))
    plt.legend(labels=labels, loc='best')
    plt.title('Reading Habit Breakdown YTD')
    plt.show()

    #Creating a bar chart with outcome by day of the week
    sns.set(style='white')
    sns.countplot(habit_data, x="day_of_week", hue="reading", palette='deep')
    plt.title('Reading Habits by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week')
    plt.ylabel('Count of reading Habit')
    plt.show()

    #Creating a bar chart with outcome by month
    sns.set(style='white')
    sns.countplot(habit_data, x="month", hue="reading", palette='deep')
    plt.title('Reading Habits by Month', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Count of reading Habit')
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
