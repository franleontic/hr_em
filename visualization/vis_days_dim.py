import os
import pickle
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

rating_path = ".\\dimensional_ratings_Google"
df = pd.DataFrame(columns=["Day", "Valence", "Arousal", "Dominance"])

threshold = 0.4
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
            df.loc[len(df)] = {"Day" : file_name, "Valence" : mean[0], "Arousal" : mean[1], "Dominance" : mean[2]}


df["Day"] = pd.to_datetime(df["Day"])

if agg_func == "mean":
    df_weekly = df.resample('W-Mon', on='Day', label="left").mean()
    df_monthly = df.resample('M', on='Day', label="left").mean()
elif agg_func == "median":
    df_weekly = df.resample('W-Mon', on='Day').median()
    df_monthly = df.resample('M', on='Day').median()
else:
    df_weekly = df.resample('W-Mon', on='Day').max()
    df_monthly = df.resample('M', on='Day').max()


fig, axes = plt.subplots(3, 3, figsize=(20, 10))
sns.set_color_codes("pastel")

ax = sns.lineplot(data=df, x="Day", y='Valence', color="b", ax=axes[0, 0])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax = sns.lineplot(data=df_weekly, x="Day", y='Valence', color="b", ax=axes[1, 0])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax.set_xlabel("Week")
ax = sns.lineplot(data=df_monthly, x="Day", y='Valence', color="b", ax=axes[2, 0])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax.set_xlabel("Month")

ax = sns.lineplot(data=df, x="Day", y='Arousal', color="orange", ax=axes[0, 1])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax = sns.lineplot(data=df_weekly, x="Day", y='Arousal', color="orange", ax=axes[1, 1])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax.set_xlabel("Week")
ax = sns.lineplot(data=df_monthly, x="Day", y='Arousal', color="orange", ax=axes[2, 1])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax.set_xlabel("Month")

ax = sns.lineplot(data=df, x="Day", y='Dominance', color="g", ax=axes[0, 2])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax = sns.lineplot(data=df_weekly, x="Day", y='Dominance', color="g", ax=axes[1, 2])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax.set_xlabel("Week")
ax = sns.lineplot(data=df_monthly, x="Day", y='Dominance', color="g", ax=axes[2, 2])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
ax.set_xlabel("Month")

for ax in axes.flatten():
    ax.tick_params(axis='x', labelrotation = 60)

plt.tight_layout()
plt.savefig("dim_vis_Google_0.4.png")


df.to_csv('daily_dim.csv')
df_weekly.to_csv('weekly_dim.csv')