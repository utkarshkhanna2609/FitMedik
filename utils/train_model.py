# -*- coding: utf-8 -*-
"""Training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dvdz7vTIBXlvb8XRNaLAMoCpSynbcazo
"""

from sklearn.metrics import r2_score
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import xgboost
import pandas as pd

df = pd.read_csv(r'./encoded_data.csv')

# Create XGboost regression model for Burnout prediction
df.drop('Name', axis=1, inplace=True)

X = df.drop(['Burnout'], axis=1)
y = df['Burnout']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


model = XGBRegressor(n_estimators=1000, max_depth=7, eta=0.1, subsample=0.7, colsample_bytree=0.8 )

model.fit(X_train, y_train)

predictions = model.predict(X_test)


print('R^2 Training: ', r2_score(y_train, model.predict(X_train)))

print('R^2 Test: ', r2_score(y_test, model.predict(X_test)))


# print the root mean squared error on the testing data
print('RMSE: \n', np.sqrt(mean_squared_error(y_test, model.predict(X_test))))


# save model to file
model.save_model(r"sample_data")

# # load model from file
# loaded_model = XGBRegressor()
# loaded_model.load_model("xgboost.model")


print('Model Successfully Trained and Saved')

#Gender -
#0- Female
#1- Male
#2- Non Binary
#3- Others
#4- Transgender

#Ethnicity-
#0-american native
#1-Asian
#2-Coloured
#3-Others
#4-White


#Profession-
#0-Doctor
#1-IT
#2-Nurse
#3-Staff
#4-Student


#Mood -
#0-Anger
#-Fear
#2-Joy
#3-Neutral
#4-Sadness
