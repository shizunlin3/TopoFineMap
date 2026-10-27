from pathlib import Path
import sys, numpy as np
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/"src"))
from topofm.priors import spin_prior_log_unnormalized,binary_prior_log_unnormalized
rng=np.random.default_rng(42); p=9; A=np.zeros((p,p))
for i,j in [(0,1),(0,2),(0,5),(2,3),(3,4),(5,6),(6,7),(7,8)]: A[i,j]=A[j,i]=1
h=rng.normal(size=p); alpha=.17; diffs=[]
for _ in range(100):
    x=rng.integers(0,2,size=p); s=2*x-1
    diffs.append(spin_prior_log_unnormalized(s,h,alpha,A)-binary_prior_log_unnormalized(x,h,alpha,A))
assert np.ptp(diffs)<1e-10
print("PASS: representation identity verified up to an additive constant")
