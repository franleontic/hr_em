import pandas as pd
import classla

anew = pd.read_csv("./hrXANEW_Google.csv")
anew["Translations"] = anew["Translations"].replace('', "no_translation")

lem = classla.Pipeline("hr", processors='tokenize, pos, lemma', tokenize_no_ssplit=True)
lemmatized = lem(anew["Translations"].to_list())
lemmas = [sent.words[0].lemma if len(sent.words) == 1 else ' '.join([word.text for word in sent.words]) for sent in lemmatized.sentences]
anew["Lemmatized"] = lemmas
anew["Lemmatized"]  = anew["Lemmatized"] .replace('null', '')
    
anew.to_csv('hrXANEW_Google_lem.csv', index=False)