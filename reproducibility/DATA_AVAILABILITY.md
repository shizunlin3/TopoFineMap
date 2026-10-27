# Data availability and external assets

This repository does not redistribute externally hosted raw datasets.

## FinnGen
Paper A uses FinnGen R12 summary statistics.

## LD
European-reference LD is derived from 1000 Genomes with ALT-allele
orientation. Strand-ambiguous A/T and C/G variants are removed unless a
predefined reference variant is explicitly retained.

## 3D genome
GM12878 in situ Hi-C:
- 4DN accession: `4DNFIXP4QG5B`
- resolution: 5 kb

For benchmark-locus graphs, balanced contact values are transformed to O/E
and undirected edges are retained at O/E > 2.0, excluding self-edges.

## Canonical hold-out lineage
For the 28-configuration hold-out:
- POS1 is converted to POS0;
- variants are mapped through actual cooler-bin intervals;
- the coordinate-only repaired lineage retains the historical phase-6 O/E
  transformation and is the primary analysis;
- a later-audited O/E transformation is retained as robustness analysis.

## TNFAIP3
TNFAIP3 is a separate resolution-boundary analysis and is not one of the
28 held-out configurations.
