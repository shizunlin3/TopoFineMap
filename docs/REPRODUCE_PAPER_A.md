# Reproduce Paper A public displays

```bash
conda env create -f environment.yml
conda activate topofinemap-public
pip install -e .
python scripts/reproduce/validate_release.py
python scripts/figures/build_all_figures.py
pytest -q
```

Full production-scale posterior reruns additionally require the external raw
GWAS, LD and contact-map inputs described in
`reproducibility/DATA_AVAILABILITY.md`.

The included canonical source tables are the numerical source for the public
Paper A display reproduction.
