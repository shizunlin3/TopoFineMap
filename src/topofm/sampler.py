from __future__ import annotations
import numpy as np
from .likelihood import delta_log_likelihood_for_flip
from .priors import conditional_prior_log_odds

def _expit(x):
    if x >= 0:
        e = np.exp(-x)
        return float(1.0/(1.0+e))
    e = np.exp(x)
    return float(e/(1.0+e))

def run_posterior_gibbs(
    h, adjacency, z, R, sigma2, N, *,
    alpha=0.0, corrected=False,
    n_chains=4, n_burn=100, n_samples=250,
    seed=42, ridge=1e-4, init_state=None,
):
    """Transparent reference Gibbs sampler.

    Returns shape (chains, retained_samples, p).

    This public implementation prioritizes auditability. Full Paper A production
    runs used an optimized implementation under the same posterior contract.
    """
    h = np.asarray(h, dtype=float)
    z = np.asarray(z, dtype=float)
    R = np.asarray(R, dtype=float)
    p = z.size
    if adjacency is None:
        A = np.zeros((p,p), dtype=float)
    else:
        A = np.asarray(adjacency, dtype=float)
    if h.shape != (p,) or R.shape != (p,p) or A.shape != (p,p):
        raise ValueError("dimension mismatch")

    out = np.zeros((n_chains, n_samples, p), dtype=np.int8)
    for chain in range(n_chains):
        rng = np.random.default_rng(seed + chain)
        x = np.zeros(p, dtype=np.int8) if init_state is None else np.asarray(init_state, dtype=np.int8).copy()
        keep = 0
        for sweep in range(n_burn + n_samples):
            for i in range(p):
                dll = delta_log_likelihood_for_flip(
                    z, R, x, i, sigma2=sigma2, N=N, ridge=ridge
                )
                prior = conditional_prior_log_odds(
                    x, i, h, alpha, A, corrected=corrected
                )
                x[i] = rng.random() < _expit(dll + prior)
            if sweep >= n_burn:
                out[chain, keep] = x
                keep += 1
    return out

def posterior_pip(samples):
    samples = np.asarray(samples)
    if samples.ndim != 3:
        raise ValueError("samples must be (chains, samples, p)")
    return (samples > 0).mean(axis=(0,1))
