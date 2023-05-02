import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import translate
import classla

anew = pd.read_csv("./hrANEW_Bing_single.csv")
anew["Translations"] = anew["Translations"].fillna('null')

lem = classla.Pipeline("hr", processors='tokenize, pos, lemma', tokenize_no_ssplit=True)
lemmatized = lem(anew["Translations"].to_list())
lemmas = [sent.words[0].lemma if len(sent.words) == 1 else ' '.join([word.text for word in sent.words]) for sent in lemmatized.sentences]
anew["Lemmatized"] = lemmas
anew["Lemmatized"]  = anew["Lemmatized"] .replace('null', '')
    
# anew["Translations"] = anew.apply(lambda row : t.translate(row["Description"]), axis=1)

# sns.set_palette("husl")
# sns.scatterplot(data=anew, x=anew.columns[3], y=anew.columns[1], s=10)
# plt.xlabel(anew.columns[1])
# plt.ylabel(anew.columns[3])
# plt.show()

anew.to_csv('hrANEW_Bing_single_lem.csv', index=False)