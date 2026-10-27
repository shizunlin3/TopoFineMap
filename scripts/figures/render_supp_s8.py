from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S6A_canonical_28_primary.tsv",sep="\t").sort_values("fold_uncorrected").reset_index(drop=True)
out=ROOT/"results/generated_figures"; out.mkdir(parents=True,exist_ok=True)
labels=(df.locus+" | "+df.endpoint).tolist()
fig,ax=plt.subplots(figsize=(11,5)); ax.scatter(np.arange(len(df)),df.fold_uncorrected,label="Coordinate-only primary")
ax.set_yscale("log"); ax.axhline(36.316,ls="--",lw=.8); ax.set_xticks(np.arange(len(df)),labels,rotation=90,fontsize=6)
ax.set_ylabel("Uncorrected posterior-model-size fold expansion"); ax.set_xlabel("Held-out configurations sorted by primary fold expansion"); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(out/"Supplementary_Figure_S8_CANONICAL.png",dpi=300,bbox_inches="tight"); fig.savefig(out/"Supplementary_Figure_S8_CANONICAL.pdf",bbox_inches="tight")
