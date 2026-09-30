---
layout: page
title: 'Episode 65: Genomics of Mycobacterium tuberculosis'
date: '2021-10-28 00:00:00'
link: https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis
episode: '65'
soundcloud_track: '1095637423'
tags:
- microbinfie
- podcast
description: 'TB genomics, drug resistance and transmission: tools, slow mutation rates, spoligotyping and biological questions sequencing cannot yet answer.'
excerpt: 'TB genomics, drug resistance and transmission: tools, slow mutation rates, spoligotyping and biological questions sequencing cannot yet answer.'
headline: 'Tuberculosis genomics: tools, transmission and missing biology'
guests:
- Suzie Hingley-Wilson
- Dany Beste
- Conor Meehan
topics:
- mycobacterium tuberculosis
- tuberculosis genomics
- drug resistance
- drug tolerance
- transmission analysis
- spoligotyping
- microbial metabolism
- long-read sequencing
- single-cell genomics
faq:
- q: Why is TB transmission difficult to reconstruct from genome sequences?
  a: TB evolves slowly, so several patients can carry isolates with no SNP differences. The panel explains that SNP distances help identify circulating clusters but do not necessarily establish who infected whom.
- q: Which long-read TB bioinformatics tools are discussed?
  a: Andrew Page introduces Galru for spoligotyping long reads. Conor Meehan also discusses TB Profiler's support for Nanopore reads and the broader challenge of adapting tools originally built for short reads.
- q: Can matching spoligotypes prove a TB transmission cluster?
  a: No. Meehan describes spoligotyping as useful for broad lineage identification and choosing samples for further investigation, but convergent patterns mean matching results do not establish transmission.
- q: Why does TB genomics still need laboratory experiments?
  a: The presence of metabolic genes does not always explain the organism's behaviour, as illustrated by BCG comparisons and the discussion of vitamin B12. Experiments are also needed to establish growth requirements, drug tolerance and generation times under conditions relevant to infection.
---

*Tuberculosis genomics: tools, transmission and missing biology*

Suzie Hingley-Wilson, Dany Beste and Conor Meehan join the hosts to discuss bioinformatics and genomics of Mycobacterium tuberculosis. They cover long-read tools, drug-resistance prediction, transmission analysis and the limits of older typing methods. The discussion connects these approaches to unresolved questions about TB metabolism, mutation rates and variation between individual bacterial cells.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 65: Genomics of Mycobacterium tuberculosis" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1095637423&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 65: Genomics of Mycobacterium tuberculosis on SoundCloud](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis)

## In this episode

### Adapting TB tools to long reads

Andrew Page introduces Galru, a tool for spoligotyping from long reads, developed by repurposing code from a project that had not worked as intended. Spoligotyping measures the presence or absence of CRISPR spacers. Conor Meehan places it within a wider effort to recover familiar clinical typing and resistance information from genome data. TB Profiler is discussed as a resistance tool that now also accepts Nanopore reads.

Meehan describes a 40-author review he coordinated to define what TB bioinformatics tools should deliver. Standards matter: tools differ in their SNP databases, supported technologies and variant thresholds. He gives examples of 90% versus 70% read support for a majority call, and two versus five supporting reads for a minority variant. Similar-looking outputs can therefore rest on different analytical decisions.

### Drug resistance, tolerance and essential genes

Dany Beste wants to understand how metabolic environments influence the evolution of drug resistance. Work in E. coli provides a comparison, but the conditions experienced by TB inside a person are harder to establish. She also distinguishes resistance from tolerance: mutations that help bacteria survive longer during drug exposure may give them an opportunity to become resistant later.

The panel discusses TraDIS and other transposon-library screens for identifying genes needed under particular conditions. Examples include studies involving M. tuberculosis, M. bovis, macrophages and macaque models. One of the guests questions whether an essential gene automatically makes a good drug target: essentiality depends on the environment, and laboratory growth requirements need not match those inside a host.

### Slow evolution complicates transmission analysis

Meehan describes an expanding picture of TB diversity, with lineages numbered one to nine. He gives an approximate pace of one SNP every three years, explaining why genetically identical isolates do not establish who infected whom. Mutation-rate estimates also depend on assumptions about generation time, which Beste challenges. Meehan notes that roughly 10% of the genome is excluded from analyses because of repetitive regions, potentially hiding additional variation.

For transmission analysis, the usual approach is to call SNPs against H37Rv and compare distances, using thresholds such as five or 12 SNPs. A Rwandan cluster discussed in the episode had persisted since the 1990s, with around 12 SNPs separating many isolates. Core-genome MLST and Bayesian transmission approaches offer alternatives, but better models still require biological information about generation times and infectious periods.

### What the genome cannot explain about metabolism

Beste describes TB living inside a macrophage phagosome, where sterols, fatty acids and some amino acids are available. Disrupting fatty-acid utilisation reduces its ability to survive there. Comparisons with Rhodococcus helped establish TB's ability to metabolise cholesterol, while comparisons within Mycobacterium are constrained by limited experimental knowledge of neighbouring species.

Gene content does not always predict behaviour. Beste describes metabolic differences between BCG and TB that are not explained simply by whether the relevant genes are present. Vitamin B12 is another puzzle: a study discussed found that TB did not make it despite retaining the pathway's genes, while supplying B12 improved the behaviour of a genome-scale metabolic model. The panel argues for transcriptomic and proteomic work; Meehan recalls finding very little public transcriptome data for a particular TB project.

### Where older typing and diagnostic methods still help

Spoligotyping persists because it is inexpensive and practical: Meehan puts the cost below £1 per test and says 40 can be processed together. It can indicate broad lineages, but convergent patterns make it unsuitable for establishing transmission clusters. An unusual spoligotype nevertheless prompted sequencing that revealed lineage eight. His recommendation is to use older tests to guide further investigation, rather than discard them or treat them as definitive.

Beste recalls distinguishing M. bovis from M. tuberculosis using LJ slopes with and without pyruvate. That cheap growth test informed treatment, alongside the discussion of intrinsic pyrazinamide resistance in M. bovis. Hingley-Wilson stresses the delay: growth on slopes takes about a month, so faster genetic information is needed before patients spend that time receiving an unsuitable drug.

### Single cells and sustained research funding

Hingley-Wilson's wish list centres on single-cell genomics and transcriptomics. Population-level measurements can miss unusual individual cells and subpopulations that she considers really important. The panel also identifies culture bias, obtaining complete genomes and making clinical bioinformatics usable by non-specialists as continuing challenges.

The closing discussion returns to funding. Beste warns that directing resources towards COVID must not mean forgetting TB and other ongoing pandemics, and argues for a broad research base. Meehan and Hingley-Wilson describe how TB's treatment outside the main WHO pathogen and AMR lists can be misunderstood by funders. Their shared concern is that genomic progress needs sustained support for the underlying experimental biology.

## Highlights

- [00:01:55](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=1:55) — Andrew Page introduces Galru for spoligotyping long reads.
- [00:02:54](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=2:54) — Conor Meehan discusses the TB tools review, long-read support and variant-calling standards.
- [00:05:50](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=5:50) — Dany Beste asks how metabolic conditions influence resistance and drug tolerance.
- [00:07:40](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=7:40) — TraDIS studies investigate genes needed for mycobacterial survival.
- [00:09:29](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=9:29) — TB lineage diversity introduces questions about mutation rates and excluded genomic regions.
- [00:13:33](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=13:33) — TB nutrition inside the phagosome includes sterols, fatty acids and amino acids.
- [00:16:00](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=16:00) — Metabolic differences between BCG and TB expose limits of gene-content comparisons.
- [00:22:01](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=22:01) — Suzie Hingley-Wilson calls for single-cell genomics and transcriptomics.
- [00:23:19](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=23:19) — Transmission typing progresses from insertion patterns to whole-genome SNP comparisons.
- [00:26:40](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=26:40) — Spoligotyping remains useful for low-cost lineage surveys, but not transmission proof.
- [00:30:01](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=30:01) — Pyruvate-dependent growth on LJ slopes provides a historical diagnostic example.
- [00:31:26](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=31:26) — The panel calls for broad research funding alongside the response to COVID.

## In their own words

> we don't know as much of the fundamental biology as I think people assume we do
>
> — Conor Meehan, [00:11:46](https://soundcloud.com/microbinfie/65-genomics-of-mycobacterium-tuberculosis#t=11:46)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Suzie Hingley-Wilson** (guest, University of Surrey)
- **Dany Beste** (guest, University of Surrey)
- **Conor Meehan** (guest, University of Bradford)

## Tools and resources mentioned

Galru, TB Profiler, Nanopore sequencing, spoligotyping, TraDIS, MIRU-VNTR, core-genome MLST, genome-scale metabolic modelling.

## Questions this episode answers

### Why is TB transmission difficult to reconstruct from genome sequences?

TB evolves slowly, so several patients can carry isolates with no SNP differences. The panel explains that SNP distances help identify circulating clusters but do not necessarily establish who infected whom.

### Which long-read TB bioinformatics tools are discussed?

Andrew Page introduces Galru for spoligotyping long reads. Conor Meehan also discusses TB Profiler's support for Nanopore reads and the broader challenge of adapting tools originally built for short reads.

### Can matching spoligotypes prove a TB transmission cluster?

No. Meehan describes spoligotyping as useful for broad lineage identification and choosing samples for further investigation, but convergent patterns mean matching results do not establish transmission.

### Why does TB genomics still need laboratory experiments?

The presence of metabolic genes does not always explain the organism's behaviour, as illustrated by BCG comparisons and the discussion of vitamin B12. Experiments are also needed to establish growth requirements, drug tolerance and generation times under conditions relevant to infection.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We’re continuing our series where we examine a particular microbial
species in some depth. We’re continuing our look at Mycobacterium
tuberculosis, focusing more on bioinformatics, genomics and typing.
Our guests are Dr. Suzie Hingley-Wilson Lecturer in Bacteriology at
the University of Surrey, Dr. Dany Beste Senior Lecturer in Microbial
Metabolism at the University of Surrey and Dr. Conor Meehan assistant
professor in molecular microbiology at the University of Bradford.
