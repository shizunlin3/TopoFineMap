from __future__ import annotations
import numpy as np
import networkx as nx

def adjacency_from_edges(p, edges):
    A = np.zeros((p,p), dtype=float)
    for i,j in edges:
        if i == j:
            continue
        A[i,j] = A[j,i] = 1.0
    return A

def edge_randomized_control(adjacency, *, seed=42):
    """Preserve edge count, but not the original node-degree sequence."""
    A = np.asarray(adjacency, dtype=float)
    p = A.shape[0]
    n_edges = int(np.triu(A,1).sum())
    pairs = np.array([(i,j) for i in range(p) for j in range(i+1,p)])
    rng = np.random.default_rng(seed)
    chosen = pairs[rng.choice(len(pairs), size=n_edges, replace=False)]
    return adjacency_from_edges(p, chosen)

def k_regular_control(p, k, *, seed=42):
    if k >= p or (p*k) % 2:
        raise ValueError("invalid k-regular graph dimensions")
    G = nx.random_regular_graph(k, p, seed=seed)
    return adjacency_from_edges(p, G.edges())
