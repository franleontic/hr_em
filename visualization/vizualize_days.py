import os
import pickle
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rating_path = ".\\ratings"
df = pd.DataFrame(columns=["Day", "Valence", "Arousal"])

threshold = 0.2
agg_func = "mean"

for folder in os.listdir(rating_path):
    folder_path = os.path.join(rating_path, folder)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        file_name = os.path.splitext(file_name)[0]

        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
            ratings = obj[0]
            confidences = obj[1]

            filtered_ratings = [x for x, y in zip(ratings, confidences) if y >= threshold]
            mean = np.mean(filtered_ratings, axis=0)
            df.loc[len(df)] = {"Day" : file_name, "Valence" : mean[0], "Arousal" : mean[1]}
            # df = df.append({"Day" : file_name, "Valence" : mean[0], "Arousal" : mean[1]}, ignore_index=True)


df["Day"] = pd.to_datetime(df["Day"])
print(type(df.resample('M', on='Day')))

if agg_func == "mean":
    df_weekly = df.resample('W-Mon', on='Day').mean()
    df_monthly = df.resample('M', on='Day').mean()
elif agg_func == "median":
    df_weekly = df.resample('W-Mon', on='Day').median()
    df_monthly = df.resample('M', on='Day').median()
else:
    df_weekly = df.resample('W-Mon', on='Day').max()
    df_monthly = df.resample('M', on='Day').max()

fig, axes = plt.subplots(3, 2, figsize=(14, 8))
sns.set_color_codes("pastel")

sns.lineplot(data=df, x="Day", y='Valence', color="b", ax=axes[0, 0])

sns.lineplot(data=df_weekly, x="Day", y='Valence', color="b", ax=axes[1, 0])

sns.lineplot(data=df_monthly, x="Day", y='Valence', color="b", ax=axes[2, 0])

sns.lineplot(data=df, x="Day", y='Arousal', color="r", ax=axes[0, 1])

sns.lineplot(data=df_weekly, x="Day", y='Arousal', color="r", ax=axes[1, 1])

sns.lineplot(data=df_monthly, x="Day", y='Arousal', color="r", ax=axes[2, 1])


plt.tight_layout()
plt.show()
