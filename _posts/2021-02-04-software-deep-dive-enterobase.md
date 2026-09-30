---
layout: page
title: 'Episode 45: Software deep dive: Enterobase'
date: '2021-02-04 00:00:00'
link: https://soundcloud.com/microbinfie/software-deep-dive-enterobase
episode: '45'
soundcloud_track: '911118157'
tags:
- microbinfie
- podcast
description: How EnteroBase combines bacterial genomes, curated metadata and cgMLST, with lessons on Salmonella sampling bias and finding related isolates.
excerpt: How EnteroBase combines bacterial genomes, curated metadata and cgMLST, with lessons on Salmonella sampling bias and finding related isolates.
headline: 'EnteroBase: genome fishing, cgMLST and population structure'
guests: []
topics:
- microbial bioinformatics
- bacterial population structure
- salmonella
- cgmlst
- metadata curation
- sampling bias
- genomic surveillance
- public sequencing data
faq:
- q: What does EnteroBase provide beyond a traditional MLST database?
  a: The episode describes EnteroBase as combining legacy typing records with processed public sequencing data, assemblies, multiple typing schemes, cleaned metadata and web-based analysis. It also provides a framework for interpreting bacterial population structure.
- q: How can EnteroBase help find isolates related to a sample?
  a: Andrew describes searching by cgMLST similarity and choosing an allowed number of allelic mismatches, such as five or ten. These searches can identify additional public samples to include in an analysis.
- q: How were genes selected for the Salmonella cgMLST scheme?
  a: The team began with curated annotations, expanded the pangenome panel and tested gene conservation across reference and assembled genomes. They used an approximately 98% presence threshold and removed problematic loci, arriving at the 3,002-gene scheme discussed in the episode.
- q: Is the whole EnteroBase Salmonella collection a representative sample?
  a: Not automatically. Nabil warns that clinical and food-production sampling biases remain even in a collection containing hundreds of thousands of genomes, so users need to consider which isolates they select.
---

*EnteroBase: genome fishing, cgMLST and population structure*

Lee Katz and Andrew Page talk with co-host Nabil-Fareed Alikhan about building EnteroBase, from legacy MLST catalogues to searchable bacterial genomes and cleaned metadata. They discuss how the Salmonella cgMLST scheme was developed and how users can find related isolates across public datasets. The conversation also covers sampling bias, errors in older records and uncertainty over the project's future.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 45: Software deep dive: Enterobase" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/911118157&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 45: Software deep dive: Enterobase on SoundCloud](https://soundcloud.com/microbinfie/software-deep-dive-enterobase)

## In this episode

### From MLST catalogues to EnteroBase

Nabil joined EnteroBase roughly a year after its grant was awarded. He describes the project as bringing together ideas from X-Base, a comparative-genomics website with precomputed analyses, and existing MLST databases for Escherichia, Salmonella, Moraxella and Yersinia. The aim was to combine genotyping, population structure, visualisation and genome comparisons through a web interface. Moraxella catarrhalis was an unusual inclusion: a respiratory pathogen in a database named for enteric organisms.

The old MLST sites held allele sequences, sequence-type profiles and sample information. EnteroBase retained those historical records as searchable legacy data, even where no whole-genome sequencing was available. Beyond that inheritance, the software was rebuilt from the ground up in Python, using Flask and Postgres.

### Public sequencing data and cleaned metadata

Nabil recalls initially running an hourly scheduled job to retrieve newly released sequencing data from the SRA. Processing included quality control with Kraken, assembly through a workflow he compares with Shovill, annotation and typing with MLST, rMLST and cgMLST schemes. Users could then search the results and choose which information to display, rather than running those analyses themselves.

Metadata cleaning was a substantial part of the work. Automated scripts interpreted free-text submissions and assigned more consistent categories, supplemented by manual curation. The team initially worked through around 30,000 Salmonella records, including looking up animal scientific names to classify hosts. The hosts explain why this is difficult: a live chicken, packaged chicken breast and chicken Kiev may all involve chicken, but represent different sampling contexts. Nabil notes that users also take the cleaned metadata and assemblies into machine-learning analyses.

### Building the Salmonella cgMLST scheme

The initial gene set came from a Salmonella annotation curated by Jay Hinton's group, with transcriptional evidence used to refine gene starts and stops. Other hand-annotated genomes expanded the preliminary pangenome. The show notes correct the strain discussed here to **ST313 (D23580), not ST131**.

The team checked the gene panel against reference genomes, including PacBio NCTC genomes from Sanger and PHE, then assessed assembled Salmonella genomes selected one per ribosomal sequence type. They used a presence threshold of about 98%, rather than requiring every gene in every assembly: poor assemblies could otherwise make conserved genes appear absent. Genes with frequent truncations, pseudogenes, low complexity or alignment problems were excluded, producing the 3,002-gene scheme discussed in the episode.

Version two revisited the selection after the database grew from roughly 30,000 to more than 70,000 Salmonella genomes. Nabil connects this reassessment to Alikhan et al. (2018), *A genomic overview of the population structure of Salmonella*, in PLOS Genetics.

### Finding related isolates through genome fishing

Andrew describes using EnteroBase while working at the Sanger Institute to find additional samples related to an isolate of interest. A cgMLST search could allow, for example, five or ten allelic mismatches, letting the user control how close a match needed to be. Starting from a single sample, this often turned up other nearby or similar samples that could then be included in an analysis.

These genome-fishing exercises feature in Zhou et al. (2020), *The EnteroBase user's guide*, in Genome Research. Its case studies cover Salmonella transmissions, Yersinia pestis phylogeny and Escherichia core genomic diversity. Nabil specifically mentions the paper's investigation of Salmonella in badgers.

### Sampling bias and historical errors

At the time of recording, Nabil reports 267,000 Salmonella genomes in EnteroBase. That scale does not make the collection random or representative. Clinical isolates and samples from food production are heavily represented, while other serovars and sources remain poorly covered. The hosts warn against treating an entire public database as an unbiased sample simply because it contains many records.

Historical MLST data present a different problem. Some legacy sequence types had still not appeared among sequenced genomes. Nabil suggests that genuinely rare historical or environmental isolates may explain some cases, while manual errors in Sanger-trace interpretation or submission may explain others. He presents those explanations as possibilities, not confirmed findings. EnteroBase therefore requires whole-genome sequencing for new sequence types rather than accepting Sanger traces, while retaining the useful historical records and nomenclature.

### Population interpretation and future support

The discussion compares EnteroBase with PubMLST, BIGSdb and NCBI's pathogen browser. For Nabil, EnteroBase's distinctive contribution is not simply returning typing results: it offers a framework for describing bacterial populations. Thresholds help users discuss what constitutes a strain, sequence type, clonal complex or species, rather than leaving them with an unexplained collection of numbers.

Asked about the project's future, Nabil says he does not know the plans and hopes someone will continue it. The hosts describe why continuity matters to existing users. Lee reports that PulseNet uses the cgMLST developed by the EnteroBase team as its backbone, while Andrew emphasises the time saved when finding related samples. These are comments about use and support at the time of recording, not an announcement of future arrangements.

## Highlights

- [00:01:11](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=1:11) — EnteroBase's origins in X-Base and legacy MLST databases
- [00:03:12](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=3:12) — Carrying over historical records and rebuilding with Flask and Postgres
- [00:04:36](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=4:36) — Retrieving public sequencing data and running automated processing
- [00:06:14](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=6:14) — Using cgMLST mismatch thresholds to find related samples
- [00:07:17](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=7:17) — Starting the Salmonella scheme from curated annotations
- [00:08:15](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=8:15) — Selecting conserved loci and reassessing the scheme as the database grew
- [00:10:57](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=10:57) — Why a large Salmonella collection is not necessarily representative
- [00:12:41](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=12:41) — Why EnteroBase requires whole-genome data for new sequence types
- [00:14:50](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=14:50) — Interpreting population structure rather than only returning typing results
- [00:15:53](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=15:53) — Classifying free-text metadata through automation and manual curation
- [00:18:31](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=18:31) — Uncertainty about future plans and the importance of continued support
- [00:19:34](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=19:34) — Genome-fishing case studies involving Salmonella in badgers

## In their own words

> Just because there's 100,000 data points doesn't mean it's random or there's no bias.
>
> — Nabil-Fareed Alikhan, [00:10:57](https://soundcloud.com/microbinfie/software-deep-dive-enterobase#t=10:57)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Jay Hinton.

## Tools and resources mentioned

EnteroBase, X-Base, PubMLST, BIGSdb, SRA, Kraken, Shovill, Flask, Postgres, MLST, rMLST, cgMLST, PacBio, EToKi.

## Questions this episode answers

### What does EnteroBase provide beyond a traditional MLST database?

The episode describes EnteroBase as combining legacy typing records with processed public sequencing data, assemblies, multiple typing schemes, cleaned metadata and web-based analysis. It also provides a framework for interpreting bacterial population structure.

### How can EnteroBase help find isolates related to a sample?

Andrew describes searching by cgMLST similarity and choosing an allowed number of allelic mismatches, such as five or ten. These searches can identify additional public samples to include in an analysis.

### How were genes selected for the Salmonella cgMLST scheme?

The team began with curated annotations, expanded the pangenome panel and tested gene conservation across reference and assembled genomes. They used an approximately 98% presence threshold and removed problematic loci, arriving at the 3,002-gene scheme discussed in the episode.

### Is the whole EnteroBase Salmonella collection a representative sample?

Not automatically. Nabil warns that clinical and food-production sampling biases remain even in a collection containing hundreds of thousands of genomes, so users need to consider which isolates they select.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat with Nabil about EnteroBase, and learn about the background to
the project, the general benefits of the platforms and some of the
strange quirks users might encounter. EnteroBase is an integrated
software environment that supports the identification of global
population structures within several bacterial genera that include
pathogens.   Papers: Mentioned PLOS genetics paper: Alikhan et al.
(2018) A genomic overview of the population structure of Salmonella.
PLoS Genet 14 (4): e1007261
https://doi.org/10.1371/journal.pgen.1007261 Paper describing
Enterobase and the genome fishing expeditions: Zhou et al. (2020) The
EnteroBase user's guide, with case studies on Salmonella
transmissions, Yersinia pestis phylogeny and Escherichia core genomic
diversity. Genome Res. 30:138-152.
https://doi.org/10.1101/gr.251678.119  rMLST is described in: Jolley
et al. 2012 Microbiology 158:1005-15.
https://doi.org/10.1099/mic.0.055459-0 Resources Enterobase:
http://enterobase.warwick.ac.uk/ PubMLST https://pubmlst.org/  About
EnteroBase schemes:
https://enterobase.readthedocs.io/en/latest/enterobase-
tutorials/deeper-lineages.html Software: Enterobase toolkit and
background software: https://github.com/zheminzhou/EToKi   Errata.
Jay Hinton’s Salmonella is a ST313 (D23580), not ST131 (I always mix
the numbers up -- Nabil)
