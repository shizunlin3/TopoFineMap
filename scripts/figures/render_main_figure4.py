from pathlib import Path
import json, numpy as np, pandas as pd, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Supplementary_Table_S6A_canonical_28_primary.tsv",sep="\t")
tn=json.loads((ROOT/"data/source_tables/TNFAIP3_canonical_summary.json").read_text())
out=ROOT/"results/generated_figures"; out.mkdir(parents=True,exist_ok=True)
mst=df[df.locus=="mst1_3p21"].iloc[0]; atg=df[df.locus=="atg16l1"].iloc[0]

fig,axes=plt.subplots(2,2,figsize=(10.5,8.5))
ax=axes[0,0]; ax.scatter(df.pip_baseline,df.pip_uncorrected); ax.plot([0,1],[0,1],ls="--",lw=1)
ax.set(xlim=(-.02,1.02),ylim=(-.02,1.02),xlabel="Baseline focal PIP",ylabel="Uncorrected focal PIP"); ax.set_title("a  Uncorrected graph prior")

ax=axes[0,1]; ax.scatter(df.pip_baseline,df.pip_corrected); grid=np.linspace(0,1,200)
ax.plot(grid,grid,lw=1); ax.plot(grid,np.clip(grid+.005,0,1),ls="--",lw=.8); ax.plot(grid,np.clip(grid-.005,0,1),ls="--",lw=.8)
ax.annotate("MST1",(mst.pip_baseline,mst.pip_corrected),xytext=(7,-12),textcoords="offset points")
ax.set(xlim=(-.02,1.02),ylim=(-.02,1.02),xlabel="Baseline focal PIP",ylabel="Degree-corrected focal PIP"); ax.set_title("b  Representation-matched correction")

ax=axes[1,0]; x=np.arange(3)
examples={"MST1/3p21":[mst.pip_baseline,mst.pip_uncorrected,mst.pip_corrected],
"ATG16L1":[atg.pip_baseline,atg.pip_uncorrected,atg.pip_corrected],
"TNFAIP3":[tn["rs6927172"]["baseline"],tn["rs6927172"]["uncorrected_alpha_0.1"],tn["rs6927172"]["degree_corrected_alpha_0.1"]]}
for name,vals in examples.items(): ax.plot(x,vals,marker="o",label=name)
ax.set_xticks(x,["Baseline","Uncorrected","Corrected"]); ax.set_ylim(-.02,1.02); ax.set_ylabel("Focal PIP"); ax.set_title("c  Distinct posterior-response regimes"); ax.legend(frameon=False)

ax=axes[1,1]; fold=np.sort(df.fold_uncorrected.values); ax.scatter(np.arange(len(fold)),fold); ax.set_yscale("log")
ax.set_xlabel("28 held-out configurations (sorted)"); ax.set_ylabel("Uncorrected model-size fold expansion"); ax.set_title("d  Posterior-model-size expansion")

fig.tight_layout(); fig.savefig(out/"Main_Figure_4_CANONICAL.png",dpi=300,bbox_inches="tight"); fig.savefig(out/"Main_Figure_4_CANONICAL.pdf",bbox_inches="tight")
