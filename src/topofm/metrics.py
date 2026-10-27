from __future__ import annotations
import numpy as np

def posterior_model_size(pip):
    return float(np.asarray(pip, dtype=float).sum())

def contact_profile_difference_sd(profile_i, profile_j, *, min_valid=5):
    a = np.asarray(profile_i, dtype=float)
    b = np.asarray(profile_j, dtype=float)
    valid = np.isfinite(a) & np.isfinite(b)
    if valid.sum() < min_valid:
        return float("nan")
    return float(np.std(a[valid]-b[valid], ddof=0))
