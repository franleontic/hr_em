import pandas as pd
from scipy.stats import zscore

df_weekly = pd.read_csv("./daily_disc.csv")

df_zscores = df_weekly[df_weekly.columns[2:]].transform(zscore)
df_zscores = pd.concat([df_weekly["Day"], df_zscores], axis=1)

for dim in ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]:
    df_sorted = df_zscores.sort_values(by=dim, ascending=False)
    print(f'{dim} sort')
    print(df_sorted)