#  step 1 :import libraries 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# step 2:  prepare the data 
data = {
    'Hours_studied': [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10],
    'score': [12, 25, 30, 45, 50, 55, 60, 73, 82, 90]
}
df = pd.DataFrame(data)

# Features and  target 
X = df[['Hours_studied']]
y = df['score']

# step 3 : split the data 
X_train , X_test , y_train , y_test  = train_test_split(X, y , test_size = 0.2 , random_state = 42)

# step 4 : train  the model 
model = LinearRegression()
model.fit(X_train , y_train)

# step 5 : make predictions 
y_pred = model.predict(X_test)
print("predicitons:", y_pred)


# step 6 : Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error ", mse)

# step 7 : visualize results 
# Convert X to 1D array for plotting 
X_1d  = X['Hours_studied'].values
y_pred_full = model.predict(X)  # .flatten() isn’t needed for model.predict(X) — it already gives a 1D array.

plt.scatter(X_1d , y, color='blue', label = 'Actual score')
plt.plot(X_1d , y_pred_full , color = 'red', label = 'predicted Line')
plt.xlabel('Hours Studied')
plt.ylabel('score')
plt.title('Hours Studied vs score Prediction')
plt.legend()
plt.show()