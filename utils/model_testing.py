# -*- coding: utf-8 -*-
"""model_testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XLGQpvX8xmhKKedrR8ma_0W2jEdizg_y
"""

# load xgboost model
import xgboost
import numpy as np
model = xgboost.XGBRegressor()
model.load_model(r"./data/xgboost.model")

d = {
    "Age":35,
    "Gender":2,
    "Ethnicity":2,
    "Profession":2,
    "BMI Score":21.6,
    "Salary":2773371,
    "Bed Time":6.75,
    "Mood":1,
    "Average Sleep":6.95,
    "Number of Steps":7506,
    "workspace duration":7,
    "workspace interaction":3,
    "Burnout": 49
}



print(list(d.values()))

query = d.values()

# convert all items in query to float
query = [float(k) for k in d.values()]


print(query)

query = np.array(query).reshape((1,-1))

print(model.predict(query))