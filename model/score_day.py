from model import Model
import pandas as pd
import numpy as np
import os
import pickle
import torch

def score(file_path, dest_path, model):
    print("Rating " + file_path)
    ratings = []
    confidences = []
    with open(file_path, errors="ignore") as f:
        lines = [line for line in f]

    ctr = 0
    for line in lines:
        print("Scored " + str(ctr))
        ctr += 1
        rating, confidence = model.score_all(line)
        ratings.append(rating)
        confidences.append(confidence)

    print("Saving to " + dest_path)
    with open(dest_path, 'wb') as f:
        pickle.dump((ratings, confidences), f)



anew = pd.read_csv("./hrXANEW_Bing_single_lem.csv")
years = ["2020"]
months = ["01", "02"]

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rating_dict = anew.groupby("Lemmatized").apply(lambda x: np.array([np.mean(x['valence']), np.mean(x['arousal'])])).to_dict()
model = Model(rating_dict=rating_dict)

for y in years:
    for m in months:
        try:
            path = f"./tokenized/{y}-{m}"
            path_result = f"./ratings/{y}-{m}"
            path = os.path.join(script_dir, path)
            os.chdir(path)
            path_result = os.path.join(script_dir, path_result)
            
            for date in os.listdir():
                os.makedirs(path_result, exist_ok=True)
                curr_path = os.path.join(path, date)
                curr_path_result = os.path.join(path_result, date)
                base_path, ext = os.path.splitext(curr_path_result)
                curr_path_result = base_path + ".pickle"
                score(curr_path, curr_path_result, model)
        except FileNotFoundError:
            print(f"{y}-{m} not found")
            