import os
import pickle
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

rating_path = ".\\discrete_ratings"
df = pd.DataFrame(columns=["Day", "anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"])

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
            df.loc[len(df)] = {"Day" : file_name,
                                "anger" : mean[0],
                                "anticipation" : mean[1],
                                "disgust" : mean[2],
                                "fear" : mean[3],
                                "joy" : mean[4],
                                "sadness" : mean[5],
                                "surprise" : mean[6],
                                "trust" : mean[7]}


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


fig, axes = plt.subplots(3, 4, figsize=(28, 10))
sns.set_color_codes("pastel")
colors1 = ["red", "orange", "chartreuse", "darkred"]
colors2 = ["cyan", "dimgrey", "magenta", "gold"]
cols1 = ["anger", "anticipation", "disgust", "fear"]
cols2 = ["joy", "sadness", "surprise", "trust"]

for i in range(4):
    ax = sns.lineplot(data=df, x="Day", y=cols1[i], color=colors1[i], ax=axes[0, i])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
    ax = sns.lineplot(data=df_weekly, x="Day", y=cols1[i], color=colors1[i], ax=axes[1, i])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
    ax.set_xlabel("Week")
    ax = sns.lineplot(data=df_monthly, x="Day", y=cols1[i], color=colors1[i], ax=axes[2, i])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
    ax.set_xlabel("Month")

for ax in axes.flatten():
    ax.tick_params(axis='x', labelrotation = 60)

plt.tight_layout()
plt.savefig("disc_1_0.4.png")


fig, axes = plt.subplots(3, 4, figsize=(28, 10))
for i in range(4):
    ax = sns.lineplot(data=df, x="Day", y=cols2[i], color=colors2[i], ax=axes[0, i])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
    ax = sns.lineplot(data=df_weekly, x="Day", y=cols2[i], color=colors2[i], ax=axes[1, i])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
    ax.set_xlabel("Week")
    ax = sns.lineplot(data=df_monthly, x="Day", y=cols2[i], color=colors2[i], ax=axes[2, i])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 
    ax.set_xlabel("Month")

for ax in axes.flatten():
    ax.tick_params(axis='x', labelrotation = 60)

plt.tight_layout()
plt.savefig("disc_2_0.4.png")

df.to_csv('daily_disc.csv')
df_weekly.to_csv('weekly_disc.csv')
