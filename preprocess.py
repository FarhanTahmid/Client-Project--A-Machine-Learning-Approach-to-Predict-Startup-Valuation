import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
dataset = pd.read_csv('Dataset-for-498-V4.csv')


# Data preprocessing
# Remove any irrelevant columns
dataset = dataset[['Duration','Operational Cost', 'Total Fund', 'Revenue', 'Profit','Net Profit Margin', 'Valuation','Userbase','Daily Active User']]
# Handling missing values (if any)
dataset = dataset.dropna()

def removePercentage(value):
    decimal_value=value[:-1]
    decimal_value=(int(decimal_value)/100)
    return decimal_value

dataset['Net Profit Margin'] = dataset['Net Profit Margin'].apply(lambda x: removePercentage(x))
dataset.head()

# Split the dataset into features (X) and target variable (y)
X = dataset.drop('Valuation', axis=1)
y = dataset['Valuation']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
