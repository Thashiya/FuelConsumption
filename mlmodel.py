# -*- coding: utf-8 -*-
"""mlmodel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5GcD4zmvyrXZGcva9lBa9e5n1iZBj91
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/MLApp/FuelConsumption.csv")
#use required features
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

#training data and predictor variable
#use all data for training (train-test-split not used)
x = cdf.iloc[:, :3]
y = cdf.iloc[:, -1]
regressor = LinearRegression()

#fitting model with the training data
regressor.fit(x, y)

#saving model to current directory
#pickle serializes objects so they can be saved to a file, and loaded in 

pickle.dump(regressor, open('model.pkl', 'wb'))

#loading model to compare the results

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[2.6, 8, 10.1]]))

import os

# Check if the model file exists
if os.path.exists('model.pkl'):
  print('The model was saved successfully.')
else:
  print('The model was not saved successfully.')

import os

# Get the current working directory
current_directory = os.getcwd()

# Print the path to the model file
print(os.path.join(current_directory, 'model.pkl'))

import os

# Get the path to the model file
model_file_path = '/content/model.pkl'

# Move the model file to your Google Drive
os.system('cp {} /content/drive/MyDrive/MLApp/model.pkl'.format(model_file_path))

import pickle

# Get the path to the model file
model_file_path = '/content/drive/MyDrive/MLApp/model.pkl'

# Load the model file
model = pickle.load(open(model_file_path, 'rb'))

# Print the prediction
print(model.predict([[2.6, 8, 10.1]]))

print(model.predict([[2.6, 8, 10.1]]))

