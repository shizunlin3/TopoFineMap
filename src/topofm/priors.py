from __future__ import annotations
import numpy as np

def degrees_from_adjacency(adjacency: np.ndarray) -> np.ndarray:
    adjacency = np.asarray(adjacency, dtype=float)
    if adjacency.ndim != 2 or adjacency.shape[0] != adjacency.shape[1]:
        raise ValueError("adjacency must be square")
    if not np.allclose(adjacency, adjacency.T):
        raise ValueError("adjacency must be symmetric")
    return adjacency.sum(axis=1)

def spin_prior_log_unnormalized(s, h, alpha, adjacency) -> float:
    """Competitive uncentered Ising prior, omitting the normalizer."""
    s = np.asarray(s, dtype=float)
    h = np.asarray(h, dtype=float)
    A = np.asarray(adjacency, dtype=float)
    upper = np.triu(A, 1)
    return float(h @ s - alpha * np.sum(upper * np.outer(s, s)))

def binary_prior_log_unnormalized(x, h, alpha, adjacency) -> float:
    """Binary-space representation of the same prior, up to a constant."""
    x = np.asarray(x, dtype=float)
    h = np.asarray(h, dtype=float)
    A = np.asarray(adjacency, dtype=float)
    d = degrees_from_adjacency(A)
    unary = 2.0 * np.sum((h + alpha * d) * x)
    pairwise = -4.0 * alpha * np.sum(np.triu(A, 1) * np.outer(x, x))
    return float(unary + pairwise)

def degree_corrected_fields(h, alpha, adjacency) -> np.ndarray:
    """h_corr = h - alpha * degree."""
    h = np.asarray(h, dtype=float)
    d = degrees_from_adjacency(adjacency)
    return h - alpha * d

def conditional_prior_log_odds(x, i, h, alpha, adjacency, corrected=False) -> float:
    x = np.asarray(x, dtype=int)
    h = np.asarray(h, dtype=float)
    A = np.asarray(adjacency, dtype=float)
    d_i = float(A[i].sum())
    m_i = float(A[i] @ x)
    if corrected:
        return float(2.0 * h[i] - 4.0 * alpha * m_i)
    return float(2.0 * h[i] + 2.0 * alpha * d_i - 4.0 * alpha * m_i)
