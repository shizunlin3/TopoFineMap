import numpy as np
from topofm.priors import spin_prior_log_unnormalized,binary_prior_log_unnormalized,degree_corrected_fields,conditional_prior_log_odds

def test_spin_binary_equivalence_up_to_constant():
    rng=np.random.default_rng(1); p=7; A=np.zeros((p,p))
    for i,j in [(0,1),(0,2),(2,3),(3,4),(4,5),(5,6)]: A[i,j]=A[j,i]=1
    h=rng.normal(size=p); alpha=.23; diffs=[]
    for _ in range(50):
        x=rng.integers(0,2,size=p); s=2*x-1
        diffs.append(spin_prior_log_unnormalized(s,h,alpha,A)-binary_prior_log_unnormalized(x,h,alpha,A))
    assert np.ptp(diffs)<1e-10

def test_degree_correction_sign():
    A=np.array([[0,1,1],[1,0,0],[1,0,0]],float); h=np.array([.2,.2,.2])
    assert np.allclose(degree_corrected_fields(h,.3,A),[-.4,-.1,-.1])

def test_corrected_conditional():
    A=np.array([[0,1,1],[1,0,0],[1,0,0]],float); x=np.array([0,1,0]); h=np.array([.2,.2,.2])
    got=conditional_prior_log_odds(x,0,h,.3,A,corrected=True)
    assert abs(got-(2*.2-4*.3))<1e-12
