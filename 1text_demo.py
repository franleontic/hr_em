from model import Model
import pandas as pd
import numpy as np

text1 = "Razvoj hrvatskog jezika se uglavnom rekonstruira na temelju starih natpisa tekstova i imena Rekonstrukcija počinje od zajedničkog praslavenskog jezika U odnosu na druge slavenske jezike južni slavenski jezici pokazuju neke zajedničke osobine"

anew = pd.read_csv("./hrANEW_Bing_single_lem.csv")

rating_dict = anew.groupby("Lemmatized").apply(lambda x: np.array([x["Valence Mean"], x["Arousal Mean"]]))
m = Model(rating_dict=rating_dict)

rating, confidence = m.score(text1.split())
print(rating)
print(confidence)