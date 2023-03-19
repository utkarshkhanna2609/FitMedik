# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H46lMmB003FkMIUntw92OEnDShLQYb3l
"""

!pip install flask-ngrok

!pip install pyngrok

!ngrok authtoken 2NBunSFGRLRluBNplDOIq5HIctl_5z2pNzUom2rHxwNuh2e7k

from flask import Flask, jsonify, request
import xgboost
import numpy as np

from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/predict', methods=['POST'])
def predict():
  # Get the data from the POST request.
  data = request.get_json(force=True)

# load xgboost model
  model = xgboost.XGBRegressor()
  model.load_model(r"./xgboost.model")

  try:
# convert all elements in data.values to float
    query = [float(k) for k in data.values()]

    query = np.array(list(query)).reshape((1, -1))
    result = model.predict(query)
    return jsonify({'vulnerability': str(result[0]), 'status': 'success'})

  except:
    return jsonify({'status': 'Error occured'})

# if __name__ == '__main__':
#   app.run(debug=True, host='0.0.0.0')
app.run()

