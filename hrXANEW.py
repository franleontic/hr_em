from git import Repo
from pathlib import Path
import pandas as pd
import translate

def load_anew(split='train', 
              root=Path.home()/'xanew'):
    
    assert split in ['train', 'dev', 'test'], 'split must be "train", "dev", or "test".'
   
      
    csv = str(root / 'Ratings_Warriner_et_al.csv')
    df = pd.read_csv(csv, index_col=0)
    df=df[['Word','V.Mean.Sum', 'A.Mean.Sum', 'D.Mean.Sum']]
    df.columns=['word', 'valence', 'arousal', 'dominance']

    print(df.shape)
    print(df.columns)
    print(df.head())
    return df


xanew = load_anew('train')
xanew.at[8290, "word"] = "null"
t = translate.BingTranslator_Single()
xanew["Translations"] = xanew.apply(lambda row : t.translate(row["word"]), axis=1)
xanew.to_csv('hrXANEW_Bing_single.csv', index=False)