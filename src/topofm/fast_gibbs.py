"""Public compatibility entry point.

The historical Paper A workflow used an optimized vectorized implementation.
This release exposes the same high-level posterior contract through the
transparent reference sampler.
"""
from .sampler import run_posterior_gibbs, posterior_pip
run_posterior_gibbs_fast = run_posterior_gibbs
