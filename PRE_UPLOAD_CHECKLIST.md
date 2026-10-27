# Pre-upload checklist

- [ ] Repository name is exactly `TopoFineMap`.
- [ ] Repository visibility will be Public.
- [ ] `python scripts/reproduce/validate_release.py` returns PASS.
- [ ] `pytest -q` passes.
- [ ] `python scripts/figures/build_all_figures.py` completes.
- [ ] No private raw data are present.
- [ ] No passwords, tokens, cookies, PATs, or SSH keys are present.
- [ ] No personal absolute local paths are present.
- [ ] Create tag `v1.0.0-paperA`.
- [ ] Insert the final public repository URL into the manuscript.
