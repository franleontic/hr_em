import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

xanew = pd.read_csv("./hrXANEW_Bing_single_lem.csv")
xanew_dims = xanew[["valence", "arousal", "dominance"]]

arr = []
for i in range(1, 10):
    fit = np.polyfit(xanew_dims["valence"], xanew_dims["arousal"], i)
    v1 = np.polyval(fit, xanew_dims["valence"])
    mse = np.mean(np.square(xanew_dims["arousal"] - v1))
    arr.append(mse)
plt.xlabel("Polynomial degree")
plt.ylabel("MSE")
plt.plot(range(1, 10), arr)
plt.savefig("MSE-VA_XANEW.png")

print("---")
for i in range(1, 10):
    fit = np.polyfit(xanew_dims["arousal"], xanew_dims["dominance"], i)
    v1 = np.polyval(fit, xanew_dims["arousal"])
    mse = np.mean(np.square(xanew_dims["dominance"] - v1))
    print(mse)
print("---")
for i in range(1, 10):
    fit = np.polyfit(xanew_dims["valence"], xanew_dims["dominance"], i)
    v1 = np.polyval(fit, xanew_dims["valence"])
    mse = np.mean(np.square(xanew_dims["dominance"] - v1))
    print(mse)

print(xanew_dims.corr())
