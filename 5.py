  
# Jessica Chouhan 0827CI201087
import pandas as pd  
  
# Load data from CSV file data 
= pd.read_csv('data.csv')  
  
# Print first 5 rows of the data print(data.head())  
  
# Jessica Chouhan 0827CI201087  
from sklearn.model_selection import train_test_split   
# Split the data into features (X) and target variable 
(y) X = data.iloc[:, :-1].values y = data.iloc[:, 1].values  
  
# Split the data into training and testing sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  

# Jessica Chouhan 0827CI201087 class LinearRegression:           def __init__(self):          self.coefficients = None  
    def fit(self, X, y):  
        # Add a column of ones to X for the bias term  
        X = np.hstack((np.ones((X.shape[0], 1)), X))           
        # Calculate the coefficients using the normal equation         self.coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)          
def predict(self, X):  
        # Add a column of ones to X for the bias term  
        X = np.hstack((np.ones((X.shape[0], 1)), X))  
          
        # Make predictions using the coefficients         y_pred = X.dot(self.coefficients)  
                 return y_pred  
  
# Jessica Chouhan 0827CI201087
import numpy as np  
  
# Create an instance of the Linear Regression model lr 
= LinearRegression()  
  
# Train the model on the training data lr.fit(X_train, y_train)

# Jessica Chouhan 0827CI201087   
# Make predictions on the testing data y_pred 
= lr.predict(X_test)   # Print the predictions  print(y_pred)

# Jessica Chouhan 0827CI201087  
import pandas as pd import numpy as np from sklearn.model_selection import train_test_split   class 
LinearRegression:  
         def __init__(self):          self.coefficients = None           def fit(self, X, y):  
        # Add a column of ones to X for the bias term  
        X = np.hstack((np.ones((X.shape[0], 1)), X))           
        # Calculate the coefficients using the normal equation         self.coefficients = np.linalg.inv(X.T)  

# Jessica Chouhan 0827CI201087 
import numpy as np import 
matplotlib.pyplot as plt  
   def estimate_coef(x, y):  
    # number of observations/points     n = np.size(x)  
    
    # mean of x and y vector     m_x = np.mean(x)     m_y = np.mean(y)      
    # calculating cross-deviation and deviation about x  
    SS_xy = np.sum(y*x) - n*m_y*m_x  
    SS_xx = np.sum(x*x) - n*m_x*m_x  
    
    # calculating regression coefficients     b_1 = SS_xy / SS_xx     b_0 = m_y - b_1*m_x          return (b_0, b_1)     def plot_regression_line(x, y, b):  
    # plotting the actual points as scatter plot     plt.scatter(x, y, color = "m",                marker = "o", s = 30)  
    
    # predicted response vector      y_pred = b[0] + b[1]*x  
    
    # plotting the regression line     plt.plot(x, y_pred, color = "g")  
    
    # putting labels     plt.xlabel('x')     plt.ylabel('y')  
    
    # function to show plot     plt.show()    def main():  
    # observations / data     x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])     y = np.array([1, 3, 2, 
5, 7, 8, 8, 9, 10, 12])  
    
    # estimating coefficients     b = estimate_coef(x, y)     print("Estimated coefficients:\nb_0 = {}  \  
          \nb_1 = {}".format(b[0], b[1]))  
    
    # plotting regression line     plot_regression_line(x, y, b)     if __name__ == "__main__":     main()  


