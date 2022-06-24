import numpy as np
import matplotlib.pyplot as plt

prediction = np.random.rand(10)

real_value = np.random.rand(10)

prediction1 = np.random.rand(10)


plt.scatter(prediction,real_value)
plt.scatter(prediction1,real_value)
plt.plot(real_value,1)
plt.show()
mse_ = (real_value[0] - prediction[0]) ** 2

def mse(prediction, real_value):
    mse_ = (real_value - prediction) ** 2
    return mse_.sum()/len(real_value)

def mse(prediction, real_value):
    return ((real_value - prediction) ** 2).mean()
mse(prediction,real_value)
mse(prediction1,real_value)