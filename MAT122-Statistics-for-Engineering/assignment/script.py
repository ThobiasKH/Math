import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.array([8, 7, 13, 9, 6, 5, 11, 9, 14, 13, 6, 10, 12, 13, 12, 10, 7, 8, 12, 10]).reshape(-1, 1)  
Y = np.array([27, 30, 26, 32, 26, 18, 36, 27, 36, 31, 34, 29, 21, 25, 35, 26, 19, 22, 37, 25])        


model = LinearRegression()
model.fit(X, Y)

alpha = model.intercept_   
beta = model.coef_[0]      
print(f"α : {alpha:.2f}")
print(f"β : {beta:.2f}")


Y_pred = model.predict(X)

plt.scatter(X, Y, color='blue', label='Data punkt')

plt.plot(X, Y_pred, color='red', label=f'Y = {alpha:.2f} + {beta:.2f}X')

plt.xlabel('X (gjødsel)')
plt.ylabel('Y (avling)')
plt.title('Y = α + βX + e')
plt.legend()
plt.show()
