import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

emolex = pd.read_csv("./hrEMOLEX_lem.csv")
emolex = emolex[["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]]
counts = emolex.eq(1).sum()
counts = counts.sort_values(ascending=False)
sns.set_style("whitegrid")
sns.barplot(x=counts.index, y=counts.values, palette=["darkred", "red", "gold", "dimgrey", "chartreuse", "orange", "cyan", "magenta"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("emolex_bar.png")