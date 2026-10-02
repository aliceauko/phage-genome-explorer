# Phage Genome Explorer

## Overview

Phage Genome Explorer is a reproducible computational analysis of complete *Staphylococcus* phage genomes from the NCBI RefSeq database.

The project characterizes genomic variation across a dataset of 176 complete phage genomes, focusing on genome size, GC content, genome topology, coding sequences (CDS), and tRNA content.

## Research Question

What genomic patterns and variation are observed among complete *Staphylococcus* phage genomes?

## Specific Objectives

1. Characterize the distribution of genome sizes.
2. Examine variation in GC content.
3. Describe basic genomic features including CDS, tRNA content, and genome topology.
4. Identify patterns and extreme observations based on genomic characteristics.

## Dataset

The dataset consists of 176 complete *Staphylococcus* phage genome records retrieved from NCBI RefSeq.

Each genome represents one observation.

The metadata table contains:

- Phage name
- NCBI accession
- Genome length
- GC content
- Genome topology
- CDS count
- tRNA count

## Workflow

The analysis follows a reproducible workflow:

1. Retrieve complete *Staphylococcus* phage genomes from NCBI RefSeq.
2. Store the raw GenBank records.
3. Extract genomic metadata using Biopython.
4. Perform quality control.
5. Calculate descriptive statistics.
6. Visualize genome size, GC content, CDS, and tRNA distributions.
7. Examine relationships between genomic features.
8. Identify extreme observations.
9. Interpret genomic patterns.

## Main Findings

Genome sizes ranged from 16,784 to 149,229 bp.

GC content ranged from 27.93% to 36.92%.

The dataset contained 153 linear genomes and 23 circular genomes.

Genome size and CDS count showed a very strong positive correlation (r = 0.99), while genome size and tRNA count showed a moderate positive correlation (r = 0.55).

Genome size showed a moderate negative correlation with GC content (r = -0.48).

These findings describe patterns within the analyzed RefSeq dataset and do not establish causal relationships.

## Project Structure

```text
phage-genome-explorer/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── results.md
│
├── results/
│   ├── figures/
│   └── tables/
│
├── scripts/
│   ├── download_genomes.py
│   ├── build_metadata.py
│   ├── qc_metadata.py
│   ├── analyze_genome_size.py
│   ├── analyze_gc_content.py
│   ├── analyze_size_gc.py
│   ├── analyze_features.py
│   └── find_outliers.py
│
└── requirements.txt
