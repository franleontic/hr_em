import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

emolex = pd.read_csv("./hrEMOLEX_lem.csv")
emolex = emolex[["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]]
print(len(emolex))

cnt_zero = (emolex.eq(0)).all(axis=1).sum()
print(cnt_zero)

cnt_nonzero = (emolex.eq(1)).any(axis=1).sum()
print(cnt_nonzero)