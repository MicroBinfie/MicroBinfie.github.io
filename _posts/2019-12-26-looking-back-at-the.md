---
layout: page
title: 'Episode 8: Looking back at 2019'
date: '2019-12-26 00:00:00'
link: https://soundcloud.com/microbinfie/looking-back-at-the
episode: '8'
soundcloud_track: '732647680'
tags:
- microbinfie
- podcast
description: A review of 2019’s microbial bioinformatics tools, from Kraken2 and GTDB to long-read assembly, containers and browser-based analysis.
excerpt: A review of 2019’s microbial bioinformatics tools, from Kraken2 and GTDB to long-read assembly, containers and browser-based analysis.
headline: 'Looking back at 2019: long reads, Kraken2 and reproducibility'
guests: []
topics:
- microbial bioinformatics
- long-read sequencing
- metagenomics
- taxonomic classification
- reproducible workflows
- phylogenetics
- public health genomics
- webassembly
faq:
- q: What is the difference between Kraken2 and Bracken?
  a: The hosts describe Kraken2 as classifying reads within a taxonomic tree. Bracken uses those classification results to estimate organism abundance, producing a more direct account of which species are present and in what proportions.
- q: Why do the hosts use Singularity rather than Docker on shared HPC systems?
  a: Andrew describes using Singularity on the institute’s cluster and Galaxy system, while Lee says Docker is less suitable for CDC’s environment shared by hundreds of scientists. The episode reports their practical choices without giving a detailed technical comparison.
- q: How were long reads changing antimicrobial resistance research?
  a: The hosts describe researchers increasingly recovering complete plasmids and chromosomes rather than leaving their structure unresolved. This helps investigate mobile genetic elements and their placement in studies of antimicrobial resistance.
- q: Why might WebAssembly be useful for bioinformatics?
  a: It could make adapted analysis tools available through a browser while running calculations on the user’s computer rather than a central server. The hosts see benefits for access and scalability, but stress that code adaptation and a usable front end still require work.
---

*Looking back at 2019: long reads, Kraken2 and reproducibility*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan review the tools, papers and working practices that shaped their microbial bioinformatics in 2019. They discuss taxonomic classification, reproducible workflows, long-read sequencing and phylogenetic methods, before looking towards browser-based analysis and public health standards. Throughout, they ask how improving software and sequencing technology can make reliable analysis easier to share.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 8: Looking back at 2019" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/732647680&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 8: Looking back at 2019 on SoundCloud](https://soundcloud.com/microbinfie/looking-back-at-the)

## In this episode

### Galaxy, Kraken2 and Bracken

Andrew’s practical discovery of 2019 was Galaxy: a point-and-click environment that saved him work and made analyses easier to share with researchers who do not program. Lee describes the FDA’s use of a Galaxy interface to support state and local partners in the US.

Kraken2 is Nabil’s bioinformatics tool of the year. The hosts report lower memory requirements, faster operation and cleaner classification results than with Kraken 1, with applications ranging from quality control of cultured isolates to microbial ecology. Nabil pairs it with Bracken, whose paper appeared in 2017 but which continued improving. Kraken classifies reads within a taxonomic tree; Bracken adds abundance estimates, helping answer questions such as how much E. coli is in a sample.

### Reference databases and chromosome structure

GTDB is another favourite, particularly for classifying metagenomic data. Nabil describes its reference phylogeny as using 120 ubiquitous single-copy proteins across about 94,000 bacterial genomes, including roughly 14,000 from uncultured organisms. He values its systematic classification scheme and inclusion of genomes recovered through metagenomic assembly, even where its definitions challenge existing taxonomy. The hosts also acknowledge its substantial storage and runtime requirements.

Lee discusses making a Kraken database from GTDB and developing his own database, Calamari. Rather than competing on comprehensiveness, he considers a narrower public health collection, potentially restricted to completed genomes to reduce contamination. When Lee raises socru, Andrew explains that it examines large structural rearrangements between rRNA operons in circular bacterial assemblies. He discusses Typhi as an example and raises niche adaptation as a possible explanation, not an established conclusion.

### Containers, testing and workflow managers

Docker and Singularity have become routine parts of the hosts’ work. Andrew uses Singularity on the institute’s cluster and Galaxy system, while finding Docker convenient on his laptop. Lee says Docker is less suitable for CDC’s shared HPC environment, where hundreds of scientists work, and describes increased reliance on Singularity. Containers save time resolving dependencies, although Nabil cautions that underlying hardware can still affect results.

Andrew connects Docker Hub distribution with Travis testing: the container users receive can also be the environment tested during development. Lee credits state health bioinformaticians with containerising tools, while Nabil recalls community help putting GrapeTree into Bioconda.

Snakemake, Nextflow and Flowcraft similarly reduce infrastructure work. Nabil contrasts a Nextflow workflow written in a few hours with comparable job-management code that took months during his PhD. Andrew warns that numerous incompatible workflow managers, without full CWL support, could create new barriers.

### Long reads, complete genomes and portable sequencing

Andrew says most of his current work involves PacBio or Nanopore long reads. Looking ahead from late 2019, he anticipates multiplexing 96 bacterial isolates on one flow cell or 384 on a PacBio cell, making complete assemblies cheaper. These are expectations for the coming year or so, rather than results presented in the episode.

The hosts connect complete chromosomes and plasmids with better investigation of antimicrobial resistance and mobile genetic elements. They discuss improving assemblers, including Flye, Redbean, Canu and Unicycler, and Andrew reports recovering complete circular bacterial genomes from a metagenomic dataset with little manual intervention. Lee describes a modular Nanopore Workflow being developed in his lab, with separate components for tasks such as cleaning and basecalling.

Portable sequencing also offers local capacity building. Andrew describes plans to send a team to Bangladesh to establish MinION sequencing locally. School outreach and low-equipment demonstrations illustrate how sequencing can move beyond conventional laboratory settings.

### Phylogenetic methods and machine-learning expectations

Lee highlights the 2018 paper *Renewing Felsenstein’s phylogenetic bootstrap in the era of big data*. Its transfer bootstrap expectation method interests him because support need not depend only on whether exactly the same clade appears in a bootstrap tree: partial agreement among descendants can contribute to the assessment.

Nabil’s paper choice is BactDating, describing Bayesian inference of ancestral dates on bacterial phylogenies. He appreciates the accompanying checks for convergence, support and temporal signal.

Machine learning receives a more cautious assessment. Andrew sees the term throughout CVs and funding applications, sometimes attached to ordinary statistical work. Nabil has seen promising, tightly targeted studies, but the hosts distinguish those results from broad claims and expect practical progress to take longer than the funding buzz.

### Browser-based analysis and public health standards

Nabil introduces WebAssembly as a way to adapt compiled software for execution in a browser. He describes browser-based examples involving MinHash and SAMtools, while noting that he had not found a comparable local-alignment tool. Lee sees potential for making command-line bioinformatics accessible to people whose expertise is sequencing rather than Linux.

Nabil stresses a different advantage: the user’s own computer performs the calculations, reducing the computational burden on a central service. Major-browser support could help portability, but developers still need a front end and must adapt their code; conversion is not automatic.

The conversation closes with the Public Health Alliance for Genomic Epidemiology. Nabil notes that all three hosts are involved in its working groups. Lee emphasises less conspicuous but essential work, including standardising metadata and communication between platforms so that independently operating public health groups can work together.

## Highlights

- [00:00:59](https://soundcloud.com/microbinfie/looking-back-at-the#t=0:59) — Andrew explains how Galaxy made analysis and sharing easier.
- [00:01:48](https://soundcloud.com/microbinfie/looking-back-at-the#t=1:48) — Kraken2’s memory use and performance lead into Bracken abundance estimates.
- [00:03:45](https://soundcloud.com/microbinfie/looking-back-at-the#t=3:45) — GTDB becomes a favourite reference database for Kraken2.
- [00:07:05](https://soundcloud.com/microbinfie/looking-back-at-the#t=7:05) — Publication challenges and the purpose of socru’s chromosome-structure analysis.
- [00:08:33](https://soundcloud.com/microbinfie/looking-back-at-the#t=8:33) — Singularity and Docker across clusters, Galaxy and laptops.
- [00:14:09](https://soundcloud.com/microbinfie/looking-back-at-the#t=14:09) — Snakemake and Nextflow reduce the work of building analysis workflows.
- [00:15:50](https://soundcloud.com/microbinfie/looking-back-at-the#t=15:50) — Machine-learning enthusiasm in recruitment and research funding.
- [00:17:49](https://soundcloud.com/microbinfie/looking-back-at-the#t=17:49) — Long-read analysis and expectations for greater bacterial multiplexing.
- [00:22:37](https://soundcloud.com/microbinfie/looking-back-at-the#t=22:37) — Transfer bootstrap expectation as an alternative assessment of phylogenetic support.
- [00:24:03](https://soundcloud.com/microbinfie/looking-back-at-the#t=24:03) — Bayesian dating of bacterial phylogenies with BactDating.
- [00:30:05](https://soundcloud.com/microbinfie/looking-back-at-the#t=30:05) — How WebAssembly differs from writing analysis software in JavaScript.
- [00:34:04](https://soundcloud.com/microbinfie/looking-back-at-the#t=34:04) — The Public Health Alliance for Genomic Epidemiology and shared standards.

## In their own words

> Don't get too excited. It's not as easy as just copying a code in one thing, compiling it, and getting out the product.
>
> — Nabil-Fareed Alikhan, [00:33:45](https://soundcloud.com/microbinfie/looking-back-at-the#t=33:45)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Galaxy, Kraken2, Bracken, GTDB, Calamari, socru, Docker, Docker Hub, Singularity, Travis, GrapeTree, pip, Conda, Bioconda, Snakemake, Nextflow, Flowcraft, CWL, MinION, Flye, Redbean, Canu, Unicycler, minimap2, Krocus, Tiptoft, MLST, Nanopore Workflow, transfer bootstrap expectation, BactDating, WebAssembly, MinHash, SAMtools.

## Questions this episode answers

### What is the difference between Kraken2 and Bracken?

The hosts describe Kraken2 as classifying reads within a taxonomic tree. Bracken uses those classification results to estimate organism abundance, producing a more direct account of which species are present and in what proportions.

### Why do the hosts use Singularity rather than Docker on shared HPC systems?

Andrew describes using Singularity on the institute’s cluster and Galaxy system, while Lee says Docker is less suitable for CDC’s environment shared by hundreds of scientists. The episode reports their practical choices without giving a detailed technical comparison.

### How were long reads changing antimicrobial resistance research?

The hosts describe researchers increasingly recovering complete plasmids and chromosomes rather than leaving their structure unresolved. This helps investigate mobile genetic elements and their placement in studies of antimicrobial resistance.

### Why might WebAssembly be useful for bioinformatics?

It could make adapted analysis tools available through a browser while running calculations on the user’s computer rather than a central server. The hosts see benefits for access and scalability, but stress that code adaptation and a usable front end still require work.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

So it's the end of 2019 and we thought we'd like to pause and look
back at what we were working on . What resonated  with us and where we
think the micro binfie field will go in the new year.
