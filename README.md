# Price Prediction for Used Cars

## Project Overview
For this project, a dataset 'Cars.csv' containing sales of second-hand cars was used for the study. Information such as brands, models, prices etc of second-hand cars were available in the dataset. In this project, a linear regression model was selected for building the machine learning model, which was aimed to predict the price of second-hand cars.

## Objectives of the Project
The following are the objectives of the project:
   1.	Create a linear regression model for predicting the price of second-hand cars.
   2.	Deploy the linear regression model for predicting price of second-hand cars based on other dataset using .py module.

## Project Outline
At the beginning of the project, the dataset was first imported into the notebook (Price Prediction for Used Cars.ipynb), and its structure and datatypes were checked. The dataset for this project had 4,345 rows and 9 columns.

The next thing to check was whether any missing values in the dataset. For the dataset of this project, there were some missing values. Several techniques could be used to deal with these missing values, such as dropping those rows with missing values (not recommended if too many rows), or imputing values into those missing fields based on other fields from the same dataset. For this project, these 2 methods were used when dealing with the missing values.

After the missing values of the dataset were handled, the next step was to perform the exploratory data analysis (EDA). The distribution of each variable and how each independent variable related to the dependent variable were checked. At the end of the EDA, some findings from the EDA could be drawn. In addition to the distributions of variables and their relationships with the dependent variable, outliers could also be observed from the EDA. In this project, some thresholds were set for removing outliers.

For this project, those assumptions which should be satisfied for using linear regression model properly were also verified. For handling categorical variables, pandas get_dummied() method was used for creating dummy variables, whereas for numerical variables, StandardScaler from sklearn was used for standardization.

For the machine learning stage, 80% of the dataset was used for training and 20% of the dataset was used for testing since the dataset for this project was not big. Subsequently, the linear regression model was trained, and its performance was evaluated based on several metrics. For model evaluation both train and test data were used since for a good model, it should perform well on both train and test data. 

Once the final linear regression model was obtained, it was saved using pickle library. Once this was done, the second notebook (Price Prediction for Used Cars_For Module.ipynb) was developed, which was used to produce a .py module file (Price_Prediction_for_Used_Cars_Module.py) for model deployment. Finally, the third notebook (Price Prediction for Used Cars_Model Deployment.ipynb) was used for demonstration of model deployment.

Below are the .ipynb files for this project:
1. Price Prediction for Used Cars.ipynb

   For data preprocessing, exploratory data analysis and model building.

2. Price Prediction for Used Cars_For Module.ipynb
   
   For converting into a .py module (Price_Prediction_for_Used_Cars_Module.py) which was used for subsequent model deployment.

3. Price Prediction for Used Cars_Model Deployment.ipynb
   
   For demonstration of model deployment using the .py module.
