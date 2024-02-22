import numpy as np
import matplotlib.pyplot as plt

def mainFunc(x):
    return 2*x + x**2 - 4

x_values = np.linspace(0 , 20, 200)

y_values = mainFunc(x_values)


plt.figure(figsize=(7, 4))
plt.plot(x_values, y_values, label="f(x) = 2x + x^2 -4",  color='red')
plt.title('Plot of f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()



