from pathlib import Path
import pandas as pd, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S8_LD_contact_overlap.tsv",sep="\t")
out=ROOT/"results/generated_figures"; out.mkdir(parents=True,exist_ok=True)
fig,axes=plt.subplots(1,2,figsize=(9,4))
axes[0].bar(df.locus,df.median_sd_ratio_tied_distant); axes[0].axhline(1,ls="--",lw=.8); axes[0].set_ylabel("Median-SD ratio, LD-tied / LD-distant"); axes[0].set_title("Contact-profile similarity")
axes[1].bar(df.locus,df.same_bin_fraction); axes[1].set_ylabel("Same 5-kb-bin fraction"); axes[1].set_title("LD-tied pairs sharing contact bin")
fig.tight_layout(); fig.savefig(out/"Supplementary_Figure_S9_CANONICAL.png",dpi=300,bbox_inches="tight"); fig.savefig(out/"Supplementary_Figure_S9_CANONICAL.pdf",bbox_inches="tight")
