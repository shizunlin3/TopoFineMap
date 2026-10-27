from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S6A_canonical_28_primary.tsv",sep="\t")
out=ROOT/"results/generated_figures"; out.mkdir(parents=True,exist_ok=True)
labels=(df.locus+" | "+df.endpoint).tolist(); y=np.arange(len(df))
du=df.pip_uncorrected-df.pip_baseline; dc=df.pip_corrected-df.pip_baseline
fig,ax=plt.subplots(figsize=(8,10)); ax.scatter(du,y,label="Uncorrected − baseline"); ax.scatter(dc,y,marker="x",label="Corrected − baseline")
ax.axvline(0,lw=1); ax.axvline(.005,ls="--",lw=.8); ax.axvline(-.005,ls="--",lw=.8)
ax.set_yticks(y,labels); ax.set_xlabel("Focal-PIP change relative to α=0 baseline"); ax.set_ylabel("Held-out configuration"); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(out/"Supplementary_Figure_S7_CANONICAL.png",dpi=300,bbox_inches="tight"); fig.savefig(out/"Supplementary_Figure_S7_CANONICAL.pdf",bbox_inches="tight")
