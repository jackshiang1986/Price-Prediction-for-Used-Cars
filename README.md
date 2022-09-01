# Price Prediction for Used Cars

## Project Overview
For this project, a dataset 'Cars.csv' which contains sales of second-hand cars is used. The dataset contains information for brands, models, prices etc of second-hand cars. In this project, a linear regression model is selected for building the machine learning model, which is aimed to predict the price of second-hand cars.

## Project Outline
At the beginning of the project, the dataset is first imported into the notebook (Price Prediction for Used Cars.ipynb), and its structure and datatypes shall be checked. The dataset for this project has 4,345 rows and 9 columns.

The next thing to check is whether there are any missing values in the dataset. For the dataset of this project, there are some missing values. Several techniques can be used to deal with these missing values, such as dropping those rows with missing values (not recommended if the number of rows is too many), or imputing values into those missing fields based on other fields from the same dataset. For this project, these 2 methods are used when dealing with the missing values.

After the missing values of the dataset are handled, the exploratory data analysis (EDA) for the dataset can be performed. The distribution of each variable and how each independent variable relates to the dependent variable are checked. At the end of the EDA, some findings from the EDA can be drawn. In addition to the distributions of variables and their relationships with the dependent variable, outliers can also be observed from the EDA. In this project, some thresholds are set for removing outliers.

For this project, those assumptions which should be satisfied for using linear regression model properly are checked. For handling categorical variables, pandas get_dummied() method is used for creating dummy variables, whereas for numerical variables, StandardScaler from sklearn is used for standardization.

For the machine learning stage, 80% of the dataset is used for training and 20% of the dataset is used for testing since the dataset for this project is not big. Subsequently, the linear regression model can be created, and its performance are evaluated based on several metrics. For model evaluation both train and test data are used since for a good model, it should perform well on both train and test data. 

Once the final linear regression model is obtained, it is saved using pickle library. Once this is done, the second notebook (Price Prediction for Used Cars_For Module.ipynb) can be developed, which is used to produce a .py module file (Price_Prediction_for_Used_Cars_Module.py) for model deployment. Finally, the third notebook (Price Prediction for Used Cars_Model Deployment.ipynb) is used for demonstration of model deployment.

Below are the .ipynb files for this project:
1. Price Prediction for Used Cars.ipynb

   For data preprocessing, exploratory data analysis and model building.

2. Price Prediction for Used Cars_For Module.ipynb
   
   For converting into a .py module (Price_Prediction_for_Used_Cars_Module.py) which will be used for subsequent model deployment.

3. Price Prediction for Used Cars_Model Deployment.ipynb
   
   Demonstration for model deployment using the .py module.
