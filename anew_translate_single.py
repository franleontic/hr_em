import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import translate

anew = pd.read_csv("./anew-1999/all.csv")
anew.set_index("Word No.", inplace=True)
anew.sort_index(inplace=True)

t = translate.BingTranslator_Single()
anew["Translations"] = anew.apply(lambda row : t.translate(row["Description"]), axis=1)
    
# anew["Translations"] = anew.apply(lambda row : t.translate(row["Description"]), axis=1)

# sns.set_palette("husl")
# sns.scatterplot(data=anew, x=anew.columns[3], y=anew.columns[1], s=10)
# plt.xlabel(anew.columns[1])
# plt.ylabel(anew.columns[3])
# plt.show()

anew.to_csv('hrANEW_Bing_single.csv', index=False)