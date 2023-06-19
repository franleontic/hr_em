import phunspell
import pandas as pd

ms = pd.read_csv("./hrXANEW_MS_single_lem.csv")
google = pd.read_csv("./hrXANEW_Google_single_lem.csv")

hrvdict = phunspell.Phunspell("hr_HR")

count_ms = ms['Lemmatized'].apply(hrvdict.lookup).sum()
count_google = google['Lemmatized'].apply(hrvdict.lookup).sum()

print(count_ms)
print(count_google)