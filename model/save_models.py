import os
import pandas as pd
import numpy as np
import models
import pickle

rounding = lambda a : 1 if a > 0.5 else 0

xanew_MS = pd.read_csv("./hrXANEW_MS_lem.csv")
xanew_Google = pd.read_csv("./hrXANEW_Google_lem.csv")
emolex = pd.read_csv("./hrEMOLEX_lem.csv")

xanew_MS['Lemmatized'] = xanew_MS['Lemmatized'].str.lower()
ngram_MS = xanew_MS['Lemmatized'].str.split().str.len()
xanew_MS = xanew_MS[ngram_MS == 1]
xanew_Google['Lemmatized'] = xanew_Google['Lemmatized'].str.lower()
ngram_Google = xanew_Google['Lemmatized'].str.split().str.len()
xanew_Google = xanew_Google[ngram_Google == 1]
emolex['Lemmatized'] = emolex['Lemmatized'].str.lower()
ngram = emolex['Lemmatized'].str.split().str.len()
emolex = emolex[ngram == 1]

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rating_dict_xanew_MS = xanew_MS.groupby("Lemmatized").apply(lambda x: np.array([np.mean(x['valence']), np.mean(x['arousal']), np.mean(x['dominance'])])).to_dict()
rating_dict_xanew_Google = xanew_Google.groupby("Lemmatized").apply(lambda x: np.array([np.mean(x['valence']), np.mean(x['arousal']), np.mean(x['dominance'])])).to_dict()
rating_dict_emolex = emolex.groupby("Lemmatized").apply(lambda x: np.array([rounding(np.mean(x['anger'])),
                                                                    rounding(np.mean(x['anticipation'])),
                                                                    rounding(np.mean(x['disgust'])),
                                                                    rounding(np.mean(x['fear'])),
                                                                    rounding(np.mean(x['joy'])),
                                                                    rounding(np.mean(x['sadness'])),
                                                                    rounding(np.mean(x['surprise'])),
                                                                    rounding(np.mean(x['trust']))
                                                                    ])).to_dict()

dim_model_MS = models.DimensionalModel(rating_dict=rating_dict_xanew_MS)
dim_model_Google = models.DimensionalModel(rating_dict=rating_dict_xanew_Google)
disc_model = models.DiscreteModel(rating_dict=rating_dict_emolex)

with open("dim_model_MS.pickle", "wb") as file:
    pickle.dump(dim_model_MS, file)

with open("dim_model_Google.pickle", "wb") as file:
    pickle.dump(dim_model_Google, file)

with open("disc_model.pickle", "wb") as file:
    pickle.dump(disc_model, file)
