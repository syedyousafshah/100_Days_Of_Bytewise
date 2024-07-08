# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Importing dataset as dataframe
file_path = r'E:\paython\HousingData.csv'  # Correct file path here
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Replacing '?' with NaN for missing values
df.replace('?', np.nan, inplace=True)

# Checking for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# List of column names to process
columns_to_fill = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'AGE', 'LSTAT']

# Replacing NaN values with the mean of each column
for column in columns_to_fill:
    df[column] = df[column].astype(float).fillna(df[column].astype(float).mean())

# Verifying there are no more missing values in the processed columns
print("Missing values after processing:")
print(df[columns_to_fill].isnull().sum())

# Displaying data types and information about the dataset
print("Dataset information:")
print(df.info())

# Generating and visualizing the correlation matrix
plt.figure(figsize=(12, 10))
correlation_matrix = df.corr()
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Defining features (X) and target (y)
X = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']]
y = df['MEDV']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Displaying the model's coefficients and intercept
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)

# Predicting housing prices on the test set
y_pred = model.predict(X_test)

# Calculating and displaying the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Visualizing the results: Actual vs Predicted housing prices
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r', lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Housing Prices')
plt.show()
