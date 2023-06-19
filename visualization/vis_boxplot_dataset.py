import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

anew = pd.read_csv("./hrXANEW_MS_lem.csv")
anew_bp = anew[["valence", "arousal", "dominance"]]
anew_bp = anew_bp.rename(columns={"valence": "Valence", "arousal": "Arousal", "dominance": "Dominance"})
sns.boxplot(data=anew_bp, showfliers=True, whis=100)

plt.savefig("XANEW boxplot.png")