# TopoFineMap

TopoFineMap is a graph-informed Bayesian fine-mapping framework used to study
representation-induced degree fields in structured Bayesian variable selection.

This public release accompanies the methodological manuscript:

**Degree-induced fields in graph-informed Bayesian fine-mapping**

## Included

- transparent reference implementation of the TopoFineMap prior, likelihood,
  degree correction, and Gibbs sampler;
- matched structural-control utilities;
- canonical Paper A source-data tables;
- scripts for regenerating the principal Paper A display figures;
- provenance manifests and SHA-256 checksums;
- release validation tests.

This release supports the methodological Paper A only and is intentionally
separate from independent disease-mechanism applications.

## Core representation result

For \(x_i\in\{0,1\}\) and \(s_i=2x_i-1\),

\[
\log p_I(s|h,\alpha,G)
= C+\sum_i h_i s_i-\alpha\sum_{\{i,j\}\in E}s_i s_j
\]

is equivalent, up to an additive constant, to

\[
C'+2\sum_i(h_i+\alpha d_i)x_i
-4\alpha\sum_{\{i,j\}\in E}x_i x_j.
\]

The representation-induced unary term is \(+2\alpha d_i\). Under the stated
parameterization,

\[
h_i^{corr}=h_i-\alpha d_i.
\]

This correction is parameterization-specific and is not asserted to be a
universal rule for other Ising sign conventions or graph priors.

## Install

```bash
conda env create -f environment.yml
conda activate topofinemap-public
pip install -e .
```

or

```bash
pip install -r requirements.txt
pip install -e .
```

## Validate the release

```bash
python scripts/reproduce/validate_release.py
pytest -q
```

## Regenerate public Paper A figures

```bash
python scripts/figures/build_all_figures.py
```

Outputs are written to `results/generated_figures/`.

## Small synthetic example

```bash
python scripts/reproduce/run_synthetic_example.py
```

## External raw data

Large externally hosted raw assets are not redistributed. Paper A uses
FinnGen R12 summary statistics, European-reference LD derived from
1000 Genomes, and the GM12878 4DN Hi-C resource (accession
**4DNFIXP4QG5B**). See `reproducibility/DATA_AVAILABILITY.md`.

Canonical source tables required to regenerate the released Paper A display
figures are included in `data/source_tables/`.

## Control terminology

The phase-5 structural randomization is:

**edge-randomized / degree-redistributed control**

It preserves total undirected edge count, not the original node-degree
sequence.

## License

MIT. See `LICENSE`.
