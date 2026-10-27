from pathlib import Path
import sys, numpy as np
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/"src"))
from topofm.sampler import run_posterior_gibbs, posterior_pip

p=8
R=np.eye(p)
for i in range(p-1): R[i,i+1]=R[i+1,i]=0.15
z=np.array([4.5,1.0,0.2,0.1,-0.3,0.4,0.0,-0.2])
A=np.zeros((p,p))
for i,j in [(0,1),(0,2),(0,3),(0,4),(4,5),(5,6)]: A[i,j]=A[j,i]=1
p0=1/p; h=np.full(p,0.5*np.log(p0/(1-p0)))
def fit(alpha,corrected):
    s=run_posterior_gibbs(h,A,z,R,1e-3,100000,alpha=alpha,corrected=corrected,n_chains=2,n_burn=30,n_samples=50,seed=42)
    return posterior_pip(s)
base,unc,cor=fit(0,False),fit(.08,False),fit(.08,True)
print("variant\tbaseline\tuncorrected\tcorrected")
for i in range(p): print(f"v{i}\t{base[i]:.3f}\t{unc[i]:.3f}\t{cor[i]:.3f}")
