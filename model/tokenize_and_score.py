from model import Model
import pandas as pd
import numpy as np
import os
import pickle


anew = pd.read_csv("./hrXANEW_Bing_single_lem.csv")
years = ["2020"]
months = ["02"]

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rating_dict = anew.groupby("Lemmatized").apply(lambda x: np.array([np.mean(x['valence']), np.mean(x['arousal'])])).to_dict()
model = Model(rating_dict=rating_dict)

for y in years:
    for m in months:
        try:
            path = f"./charreplace/{y}-{m}"
            path_result = f"./ratings/{y}-{m}"
            path = os.path.join(script_dir, path)
            os.chdir(path)
            path_result = os.path.join(script_dir, path_result)
            for date in os.listdir():
                os.makedirs(path_result, exist_ok=True)
                curr_path = os.path.join(path, date)
                curr_path_result = os.path.join(path_result, date)
                os.chdir(curr_path)
                ratings = []
                confidences = []

                base_path, ext = os.path.splitext(curr_path_result)
                curr_path_result = base_path + ".pickle"

                for file in os.listdir():
                    file_path = os.path.join(curr_path, file)
                    with open(file_path, 'r', errors="ignore") as f2:
                        for line in f2:
                            rating, confidence = model.tokenize_and_score(line)
                            ratings.append(rating)
                            confidences.append(confidence)

                print("Saving to " + curr_path_result)
                with open(curr_path_result, 'wb') as f:
                    pickle.dump((ratings, confidences), f)

        except FileNotFoundError:
            print(f"{y}-{m} not found")
            