from __future__ import annotations
import numpy as np

def log_marginal_likelihood(z, R, active, *, sigma2, N, ridge=1e-4) -> float:
    """Transparent Paper A summary-statistic Gaussian marginal likelihood.

    Up to configuration-independent constants:
      -k/2 log(N*sigma2) - 1/2 log|M_C| + 1/2 z_C^T M_C^-1 z_C
    where
      M_C = R_CC + (1/(N*sigma2) + ridge) I.
    """
    z = np.asarray(z, dtype=float)
    R = np.asarray(R, dtype=float)
    active = np.asarray(active, dtype=int)
    if active.size == 0:
        return 0.0
    if sigma2 <= 0 or N <= 0:
        raise ValueError("sigma2 and N must be positive")
    zc = z[active]
    Rcc = R[np.ix_(active, active)]
    k = active.size
    M = Rcc + (1.0/(N*sigma2) + ridge) * np.eye(k)
    sign, logdet = np.linalg.slogdet(M)
    if sign <= 0:
        raise np.linalg.LinAlgError("M_C is not positive definite")
    quad = float(zc @ np.linalg.solve(M, zc))
    return float(-0.5*k*np.log(N*sigma2) - 0.5*logdet + 0.5*quad)

def delta_log_likelihood_for_flip(z, R, x, i, *, sigma2, N, ridge=1e-4) -> float:
    x = np.asarray(x, dtype=int)
    x0 = x.copy(); x0[i] = 0
    x1 = x.copy(); x1[i] = 1
    return (
        log_marginal_likelihood(z, R, np.flatnonzero(x1), sigma2=sigma2, N=N, ridge=ridge)
        - log_marginal_likelihood(z, R, np.flatnonzero(x0), sigma2=sigma2, N=N, ridge=ridge)
    )
