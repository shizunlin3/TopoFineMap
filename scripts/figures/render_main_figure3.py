from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/"data/source_tables/Figure3_matched_controls.tsv", sep="\t")
out=ROOT/"results/generated_figures"; out.mkdir(parents=True, exist_ok=True)

g=df[df.control_family=="graph structure"]
p=df[df.control_family=="parameterization"]
native=g[g.configuration=="native"]
edge=g[g.configuration=="edge-randomized"]
kreg=g[g.configuration=="k-regular"]
unc=p[p.configuration=="uncentered Ising"]
corr=p[p.configuration=="degree-corrected Ising"]
bern=p[p.configuration=="Bernoulli-state"]

fig,axes=plt.subplots(2,2,figsize=(10,8))

ax=axes[0,0]
ax.plot(native.alpha,native.kpost,marker="o",label="Native graph")
ax.plot(edge.alpha,edge.kpost,marker="o",label="Edge-randomized")
ax.set_xscale("symlog",linthresh=0.02); ax.set_yscale("log")
ax.set_xlabel("Coupling strength α"); ax.set_ylabel("Expected posterior model size")
ax.set_title("a  Edge randomization shifts mass expansion"); ax.legend(frameon=False)

ax=axes[0,1]
ax.plot(native.alpha,native.kpost,marker="o",label="Native graph")
ax.plot(kreg.alpha,kreg.kpost,marker="o",label="Degree-regular")
ax.set_xscale("symlog",linthresh=0.02); ax.set_yscale("log")
ax.set_xlabel("Coupling strength α"); ax.set_ylabel("Expected posterior model size")
ax.set_title("b  Degree regularization attenuates early expansion"); ax.legend(frameon=False)

ax=axes[1,0]
ax.plot(unc.alpha,unc.kpost,marker="o",label="Uncentered Ising")
ax.plot(bern.alpha,bern.kpost,marker="o",label="Bernoulli-state")
ax.set_xscale("symlog",linthresh=0.02); ax.set_yscale("log")
ax.set_xlabel("Coupling strength α"); ax.set_ylabel("Expected posterior model size")
ax.set_title("c  State parameterization changes the transition"); ax.legend(frameon=False)

ax=axes[1,1]
ax.plot(unc.alpha,unc.proxy_pip,marker="o",label="Uncentered Ising")
ax.plot(corr.alpha,corr.proxy_pip,marker="o",label="Degree-corrected Ising")
ax.plot(bern.alpha,bern.proxy_pip,marker="o",label="Bernoulli-state")
ax.set_xscale("symlog",linthresh=0.02)
ax.set_xlabel("Coupling strength α"); ax.set_ylabel("PIP at rs10889669")
ax.set_ylim(-0.02,1.05); ax.set_title("d  Correction matches the Bernoulli reference")
ax.legend(frameon=False)

fig.tight_layout()
fig.savefig(out/"Main_Figure_3_CANONICAL.png",dpi=300,bbox_inches="tight")
fig.savefig(out/"Main_Figure_3_CANONICAL.pdf",bbox_inches="tight")
