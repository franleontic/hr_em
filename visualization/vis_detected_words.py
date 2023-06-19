import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("new_wc09.csv", delimiter="\t", names=["Index", "Word", "Count"])
df["Count"] = df["Count"] - 1

df = df.sort_values("Count", ascending=False)
print(df.head())

ranking = np.arange(1, len(df["Count"]) + 1)

plt.figure(figsize=(10, 6))
plt.plot(ranking, df["Count"])

plt.xlabel('Ranking')
plt.ylabel('Detections')
plt.tight_layout()


plt.savefig("word_detections.png")