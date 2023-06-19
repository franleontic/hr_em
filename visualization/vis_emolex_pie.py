import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def sent(row):
    if row["positive"] == 1 and row["negative"] == 0:
        return "positive"
    elif row["positive"] == 0 and row["negative"] == 1:
        return "negative"
    elif row["positive"] == 0 and row["negative"] == 0:
        return "neutral"
    else:
        return "both"

emolex = pd.read_csv("./hrEMOLEX_lem.csv")
emolex = emolex[["positive", "negative"]]
emolex["label"] = emolex.apply(lambda x: sent(x), axis=1)
counts = emolex["label"].value_counts()

plt.pie(counts, labels=counts.index, autopct="%1.1f%%", pctdistance=0.8, colors=["dodgerblue", "crimson", "palegreen", "mistyrose"])
plt.savefig("emolex_pie.png")
