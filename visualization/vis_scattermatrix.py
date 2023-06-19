import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

anew = pd.read_csv("./hrXANEW_Bing_single_lem.csv")
anew_bp = anew[["valence", "arousal", "dominance"]]
anew_bp = anew_bp.rename(columns={"valence": "Valence", "arousal": "Arousal", "dominance": "Dominance"})
bins = np.arange(1, 10)
pl = sns.pairplot(data=anew_bp, plot_kws={'s': 10}, diag_kws={'bins': bins})
pl.set(xlim=(1, 9), ylim=(1, 9))

plt.savefig("XANEW scattermatrix")