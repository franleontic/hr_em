import pandas as pd
import translate
import os

def load_xanew():
      
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    print(script_dir)
    csv = os.path.join(script_dir, "xanew\\Ratings_Warriner_et_al.csv")
    df = pd.read_csv(csv, index_col=0)
    df=df[['Word','V.Mean.Sum', 'A.Mean.Sum', 'D.Mean.Sum']]
    df.columns=['word', 'valence', 'arousal', 'dominance']

    print(df.shape)
    print(df.columns)
    print(df.head())
    return df


xanew = load_xanew()
xanew.at[8290, "word"] = "null"
t = translate.GoogleTranslator()
xanew["Translations"] = xanew.apply(lambda row : t.translate(row["word"]), axis=1)
xanew.to_csv('hrXANEW_Google.csv', index=False)