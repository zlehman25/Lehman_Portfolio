# Habit Tracker Analysis
  This project was an continuation of data analysis and visualization using python and the libraries within it. The data comes from personal data related to the habits I wanted to track and improve on during 2024. The following are the habits/activities and the basis for tracking them:
  - Diet - Diet was tracked with 3 categories: good, neutral, and bad. A 'good' day consists of all homecooked meals with a focus on healthier or plant-based eating. A 'bad' day was a day with unhealthy eating or too much snacking. A 'neutral' day falls somewhere in between (a bit too arbitrary so this may be changed in the future)
  - Spending - Spending was also tracked with 3 categories: good, neutral, and bad. A 'good' day consists of no spending at all. A 'bad' day was a day with money spent on unnecessary things. A 'neutral' day was when money was only spent on necessities like groceries, gas, or bills.
  - Yoga - Very simple; good for yoga done that day and bad for no yoga
  - Gym - Tracked the same way as yoga, looking at days where I either went to the gym for weight training or another physical activity
  - Learning - Tracked the same way as yoga, looking at days where I did some kind of online learning, training, or project
  - Reading - Tracked the same way as yoga, looking at days where I either read or did not read

### Included:
  - pandas library
  - seaborn library
  - matplotlib library
  - datetime library
  
### Features:
  - Adds csv file data into the function by saving it into a variable
  - Massages the data into a more 'usable' format for analysis
  - Creates a variety of graphs to better understand the data including pie charts, column charts, and line plots

### Process:
I started by giving myself about a month's worth of data related to the habits mentioned above, making sure to not miss any days. After gathering enough data I loaded the csv file used to track the habits into Python using the pandas library. The main ideas I had when thinking of how to view this data were what habits I do the best at, what days and months I do the best and worst at, and how a 'bad' day for one habit relates to how I score on the other habits. I took a few steps to use the recorded date from the csv file to add new columns into the data frame for analysis (long date, day of the week, month). The data frames were then used to create graphs that answer all of the inital questions that were mentioned earlier.

### Learnings:
- Using the pandas library
- Using the seaborn library
- Using the matplotlib library
- massaging data within dataframes
- nested functions
- applying functions accross rows and columns of data

### Improvement:
- Create more graphs
- Expand on the graphs that were already created - explore more customization options with the libraries that were used
- Look at the data from a different lens - how else can I analyze my habits?
- Expand the habits I track
- Continue the analysis for the entire year (or more?)
- Try to implement some kind of machine learning to predict when I may have a good or bad day for certain habits
