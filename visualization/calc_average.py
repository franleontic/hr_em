import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

xanew = pd.read_csv("./hrXANEW_Bing_single_lem.csv")
xanew_bp = xanew[["valence", "arousal", "dominance"]]
print(np.average(xanew_bp, axis=0))