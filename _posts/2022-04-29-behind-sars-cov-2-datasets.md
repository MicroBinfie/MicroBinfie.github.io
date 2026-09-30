---
layout: page
title: 'Episode 81: The people behind the benchmark datasets for SARS-CoV-2'
date: '2022-04-29 00:00:00'
link: https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets
episode: '81'
soundcloud_track: '1199120434'
tags:
- microbinfie
- podcast
description: Lingzi Xiaoli and Jill Hagey explain how they mined SARS-CoV-2 data, checked SRA metadata and selected benchmark samples against CDC references.
excerpt: Lingzi Xiaoli and Jill Hagey explain how they mined SARS-CoV-2 data, checked SRA metadata and selected benchmark samples against CDC references.
headline: 'Building SARS-CoV-2 benchmark datasets: mining and QC'
guests:
- Lingzi Xiaoli
- Jill Hagey
topics:
- sars-cov-2
- benchmark datasets
- data mining
- metadata quality
- sequence quality control
- primer schemes
- variant selection
- public health bioinformatics
faq:
- q: Where did the SARS-CoV-2 benchmark sequences and reads come from?
  a: The team searched GISAID assemblies and used a linking table to locate corresponding reads in the SRA. Candidate reads then went through quality-control checks before selection.
- q: How did Selenium help build the benchmark datasets?
  a: Jill Hagey used Selenium to automate browser searches by identifier, then reused it to extract sample metadata from NCBI. This helped filter for Illumina, paired-end samples using ARTIC primers without checking each page manually.
- q: How were representative SARS-CoV-2 variant samples selected?
  a: The team compared candidates with CDC internal lineage references, looking for few SNP differences and few ambiguous Ns. They also checked read quality and required the expected spike mutations for the relevant VOI or VOC.
- q: Why was ARTIC primer metadata difficult to filter?
  a: Submitters used different wording and metadata locations for primer information, including version 3 and v3. The discussion also flags the need to distinguish v3 from v4 as primer schemes change.
---

*Building SARS-CoV-2 benchmark datasets: mining and QC*

Lingzi Xiaoli and Jill Hagey return for the second part of a conversation about building SARS-CoV-2 benchmark datasets. They describe sourcing assemblies and reads, automating metadata checks, and selecting representative sequences using quality-control metrics and CDC internal references. The discussion shows why inconsistent primer labels and sequencing metadata required scrutiny alongside the sequences themselves.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 81: The people behind the benchmark datasets for SARS-CoV-2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1199120434&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 81: The people behind the benchmark datasets for SARS-CoV-2 on SoundCloud](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets)

## In this episode

### Automating searches and metadata checks

Jill describes an early challenge: finding SARS-CoV-2 sequences and downloading them in bulk. Bulk downloading from GISAID was difficult at the time, so she experimented with Selenium, a Python package for interacting with web browsers. She used it to search through a list of identifiers, while a colleague pursued a different download approach. Other participants recognised Selenium from website and continuous integration testing.

Although the team ultimately used the alternative download route, Jill reused Selenium to extract sample information from NCBI. The aim was to give Lingzi a filtered list of samples meeting three requirements: Illumina sequencing, paired-end reads and ARTIC primers. This avoided checking every sample manually.

### Why SRA metadata needed scrutiny

The team initially relied on metadata in the Sequence Read Archive (SRA), but processing exposed oddities. Jill recalls running some data through the wrong pipeline, finding no reads in R2, and questioning why Nanopore data had an R2 file at all. Such cases prompted a closer look at the relationship between the declared sequencing method and the files being processed.

Primer descriptions were another obstacle. Information was not always entered in the same place or expressed consistently: ARTIC v3 could appear as version 3, v3 or other wording. Jill had to inspect what individual pages actually said when automated extraction did not retrieve the expected information. One of the hosts notes that the use of v4 would make distinguishing primer versions even more important.

### Quality control before selection

Jill outlines a workflow combining FastQC, SAMtools and the TITAN pipeline. FastQC provided basic quality information. SAMtools was used to examine coverage at nucleotide positions, including average depth and standard deviation. TITAN supplied further metrics, including the number of Ns, Pangolin lineage assignments, amino-acid insertions, deletions and substitutions, and sequencing depth across the assembly.

These checks determined whether candidate samples met the team's quality criteria. Sequence similarity alone was not enough: the associated reads also had to pass quality control, and the spike mutations needed to agree with the expected lineage profile.

### Choosing representative variants

Lingzi explains that CDC internal references provided the starting point for each lineage. The team searched available GISAID assemblies for candidates with few SNP differences and few ambiguous Ns, then used a linking table to find their corresponding SRA data. Those reads went through the quality-control workflow. Jill also describes using Snippy to compare SNPs against the internal references and checking spike mutations separately.

For variants of interest (VOIs) and variants of concern (VOCs), the team required the spike mutations described on the CDC website. Asked whose variant definitions guided inclusion, Lingzi says they used the CDC-defined VOIs and VOCs available when the project began; WHO naming was not yet available at that point.

The show notes identify the project repository as CDCgov/datasets-sars-cov-2 and point listeners to an earlier paper on bacterial benchmark datasets and the preceding episode for part one of the conversation.

## Highlights

- [00:00:47](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=0:47) — Introducing part two: how the SARS-CoV-2 benchmark datasets were assembled
- [00:01:25](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=1:25) — Finding sequences, bulk-download difficulties and experimenting with Selenium
- [00:02:11](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=2:11) — Using Selenium to automate searches through a list of sample identifiers
- [00:04:38](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=4:38) — Distinguishing ARTIC primer versions as v4 comes into use
- [00:05:20](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=5:20) — Checking candidate sequences with FastQC, SAMtools and TITAN
- [00:06:56](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=6:56) — Starting from CDC internal references and linking GISAID assemblies to SRA reads
- [00:07:52](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=7:52) — Deciding which lineages and variant definitions to include
- [00:08:28](https://soundcloud.com/microbinfie/behind-sars-cov-2-datasets#t=8:28) — Using the CDC-defined VOIs and VOCs available when the project began

## Who is talking

- **Lingzi Xiaoli** (guest)
- **Jill Hagey** (guest)
- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Selenium, GISAID, NCBI Sequence Read Archive (SRA), FastQC, SAMtools, TITAN, Snippy, Pangolin, ARTIC primer schemes (v3 and v4).

## Questions this episode answers

### Where did the SARS-CoV-2 benchmark sequences and reads come from?

The team searched GISAID assemblies and used a linking table to locate corresponding reads in the SRA. Candidate reads then went through quality-control checks before selection.

### How did Selenium help build the benchmark datasets?

Jill Hagey used Selenium to automate browser searches by identifier, then reused it to extract sample metadata from NCBI. This helped filter for Illumina, paired-end samples using ARTIC primers without checking each page manually.

### How were representative SARS-CoV-2 variant samples selected?

The team compared candidates with CDC internal lineage references, looking for few SNP differences and few ambiguous Ns. They also checked read quality and required the expected spike mutations for the relevant VOI or VOC.

### Why was ARTIC primer metadata difficult to filter?

Submitters used different wording and metadata locations for primer information, including version 3 and v3. The discussion also flags the need to distinguish v3 from v4 as primer schemes change.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We bring on Lingzi Xiaoli and Jill Hagey to talk about their benchmark
datasets for SARS-CoV-2. See our previous episode for part 1 of the conversation.

Find out more at https://github.com/CDCgov/datasets-sars-cov-2

- Previous paper for bacterial datasets can be found at https://peerj.com/articles/3893/
- Jill can be found on Twitter at @JillHagey and jvhagey.github.io
- Lingzi can be found on LinkedIn at https://www.linkedin.com/in/lingzi-xiaoli-27b87174/
