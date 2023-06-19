import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(columns=['month', 'total', 'unique'])

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
years = ["2019", "2020", "2021"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for y in years:
    for m in months:
        try:
            path = f"./COVIDdataset/{y}-{m}"
            path_nd = f"./charreplace/{y}-{m}"
            path = os.path.join(script_dir, path)
            path_nd = os.path.join(script_dir, path_nd)

            cnt = 0
            cnt_nd = 0

            for root, directories, files in os.walk(path):
                cnt += len(files)
            for root, directories, files in os.walk(path_nd):
                cnt_nd += len(files)
            
            if cnt != 0:
                df.loc[len(df)] = [f"{y}-{m}", cnt, cnt_nd]
        except FileNotFoundError:
            print(f"{y}-{m} not found")

print(df.head(10))
sns.barplot(x='month', y='total', data=df, color="dimgrey", label='Duplicates')
sns.barplot(x='month', y='unique', data=df, color="cyan", label='Unique files')
plt.xticks(rotation=45)

plt.legend()
plt.ylabel("File count")
plt.tight_layout()
plt.savefig("duplicates.png")
