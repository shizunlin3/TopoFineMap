from pathlib import Path
import json, numpy as np, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
tn=json.loads((ROOT/"data/source_tables/TNFAIP3_canonical_summary.json").read_text())
out=ROOT/"results/generated_figures"; out.mkdir(parents=True,exist_ok=True)
labels=["rs6927172","rs11154952"]
base=[tn["rs6927172"]["baseline"],tn["rs11154952"]["baseline"]]
unc=[tn["rs6927172"]["uncorrected_alpha_0.1"],tn["rs11154952"]["uncorrected_alpha_0.1"]]
cor=[tn["rs6927172"]["degree_corrected_alpha_0.1"],tn["rs11154952"]["degree_corrected_alpha_0.1"]]
fig,axes=plt.subplots(1,2,figsize=(9,4)); x=np.arange(2); w=.24
axes[0].bar(x-w,base,w,label="α=0 baseline"); axes[0].bar(x,unc,w,label="Uncorrected α=0.1"); axes[0].bar(x+w,cor,w,label="Degree-corrected α=0.1")
axes[0].set_xticks(x,labels); axes[0].set_ylim(0,1.05); axes[0].set_ylabel("PIP"); axes[0].set_title("TNFAIP3 posterior response"); axes[0].legend(frameon=False,fontsize=8)
oe=[tn["contact_context"]["rs6927172_to_IL20RA_TSS_OE"],tn["contact_context"]["rs6927172_to_TNFAIP3_TSS_OE"]]
axes[1].bar(np.arange(2),oe); axes[1].axhline(tn["contact_context"]["graph_edge_threshold_OE"],ls="--",lw=.8,label="Graph-edge threshold")
axes[1].set_xticks(np.arange(2),["IL20RA TSS","TNFAIP3 TSS"]); axes[1].set_ylabel("Hi-C O/E"); axes[1].set_title("Regional 5-kb contact context"); axes[1].legend(frameon=False,fontsize=8)
fig.tight_layout(); fig.savefig(out/"Supplementary_Figure_S10_CANONICAL.png",dpi=300,bbox_inches="tight"); fig.savefig(out/"Supplementary_Figure_S10_CANONICAL.pdf",bbox_inches="tight")
