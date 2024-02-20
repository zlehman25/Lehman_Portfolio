# EPL Predictor
This project was an introduction to the machine learning capabilities within python. The project can also be found with step-by-step instructions at the following locations: [github](https://github.com/dataquestio/project-walkthroughs/tree/master/football_matches) and
[youtube](https://github.com/dataquestio/project-walkthroughs/tree/master/football_matches). This Jupyter Notebook walks through steps to use match results and data from soccer/football games in the English Premier League to predict future results. The data is cleaned,
transformed, and analyzed with machine learning models that are adjusted throughout the project to improve theur accuracy.

### Included:
  - pandas library
  - sklearn library
  - RandomForestClassifier
  - accuracy_score
  - precision_score
  
### Features:
  - Adds csv file data into the function by saving it into a variable
  - Massages the data into a more 'usable' format for analysis
  - Creates targets and predictors to train a random forest machine learning model
  - Calculates the accuracy and precision of the model
  - Normalizes data with a dictionary

### Process:
Like mentioned above, the data comes from match results from the English Premier League. Various statistics such as goals for, home/away, opponent, and day of the week are turned into predictors that are then used to train the machine learning model using a training data set. The test data set is then used to check the accuracy of the model's predictions.

### Learnings:
- Using the pandas library for machine learning
- Massaging data within dataframes
- Using the sklearn library (accuracy_score and precision_score)
- Using random forests for machine learning
- Training and testing machine learning models
- Creating a python dictionary

### Improvement:
- Use a larger dataset
- Choose a different type of data to predict without following along with another project
- Look into different machine learning models
- Look into different ways to determine the accuracy of my model
- Tweak the current model to see if changes to things like the random forest estimators or splits improves the accruacy
