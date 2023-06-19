import os
import pickle
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rating_path = ".\\dimensional_ratings_Google"
df = pd.DataFrame(columns=["Day", "Valence", "Arousal", "Dominance"])

all_ratings = []
all_confidences = []

for folder in os.listdir(rating_path):
    folder_path = os.path.join(rating_path, folder)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        file_name = os.path.splitext(file_name)[0]

        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
            ratings = obj[0]
            confidences = obj[1]

            all_ratings.extend(ratings)
            all_confidences.extend(confidences)

all_ratings = np.array(all_ratings)
all_confidences = np.array(all_confidences)

c = 0

for i in range(9):
    c += 0.1
    filtered_ratings = all_ratings[all_confidences >= c]
    std = np.std(filtered_ratings, axis = 0)
    print(f"{c}: {std}")


