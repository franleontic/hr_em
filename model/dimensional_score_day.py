import pandas as pd
import os
import pickle

def score(file_path, dest_path, model):
    print("Rating " + file_path)
    ratings = []
    confidences = []
    with open(file_path, errors="ignore", encoding="UTF-8") as f:
        lines = [line for line in f]

    ctr = 0
    for line in lines:
        print("Scored " + str(ctr))
        ctr += 1       
        rating, confidence = model.score(line)
        ratings.append(rating)
        confidences.append(confidence)

    print("Saving to " + dest_path)
    with open(dest_path, 'wb') as f:
        pickle.dump((ratings, confidences), f)



years = ["2019", "2020", "2021"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

with open('./model/dim_model_Google.pickle', 'rb') as f:
    model = pickle.load(f)
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for y in years:
    for m in months:
        try:
            path = f"./tokenized/{y}-{m}"
            path_result = f"./dimensional_ratings_Google/{y}-{m}"
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

os.chdir(script_dir)
df_count = pd.DataFrame(list(model.counter.items()), columns=["Key", "Count"])
df_count.to_csv("word_count.csv")   
