from __future__ import annotations
import numpy as np
from .graph_utils import edge_randomized_control, k_regular_control
from .priors import degree_corrected_fields

def make_structural_controls(adjacency, h, alpha, *, seed=42):
    A = np.asarray(adjacency, dtype=float)
    p = A.shape[0]
    k = int(round(A.sum(axis=1).mean()))
    if (p*k) % 2:
        k = max(0, k-1)
    return {
        "native": A,
        "edge_randomized_degree_redistributed": edge_randomized_control(A, seed=seed),
        "k_regular": k_regular_control(p, k, seed=seed) if k > 0 else np.zeros_like(A),
        "h_degree_corrected": degree_corrected_fields(h, alpha, A),
    }
