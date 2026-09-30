---
layout: page
title: 'Episode 36: Roary the pangenome pipeline'
date: '2020-12-10 00:00:00'
link: https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline
episode: '36'
soundcloud_track: '899876332'
tags:
- microbinfie
- podcast
description: Andrew Page explains Roary’s origins, fast pangenome comparisons, annotation requirements and why quality control matters.
excerpt: Andrew Page explains Roary’s origins, fast pangenome comparisons, annotation requirements and why quality control matters.
headline: 'Roary: bacterial pangenomes, scaling and the importance of QC'
guests: []
topics:
- bacterial pangenomes
- core genome
- accessory genome
- gene annotation
- sequence clustering
- high-performance computing
- quality control
- contamination
- bioinformatics software
faq:
- q: What problem does Roary solve?
  a: Roary compares bacterial genomes to identify shared core genes and variable accessory genes. It was developed to make pangenome analysis feasible for thousands or tens of thousands of genomes, rather than the roughly 80–100-genome collections Andrew was seeing in the literature.
- q: How does Roary make large pangenome comparisons faster?
  a: It uses CD-HIT to pre-cluster genes before all-against-all BLAST comparisons, reducing the number of comparisons required. Andrew also describes LSF-based cluster support, although users often preferred running on one machine with many threads.
- q: Why should Roary inputs be annotated consistently?
  a: Different annotation tools and gene predictors can call genes differently, making a mixed collection difficult to compare reliably. Andrew designed Roary around Prokka output and recommends processing the whole collection consistently rather than mixing downloaded annotations.
- q: Why can core-genome size jump every hundred genomes?
  a: Andrew explains that a 99% presence threshold produces steps because the permitted number of missing genomes changes in whole numbers. Requiring genes in every genome removes that threshold effect, but assembly gaps and contig breaks are reasons to allow some tolerance.
- q: What is Scoary used for alongside Roary?
  a: The hosts recommend Scoary for statistical follow-up to Roary output. Andrew describes supplying case and control information to obtain further statistical results.
---

*Roary: bacterial pangenomes, scaling and the importance of QC*

Andrew Page discusses Roary with his co-hosts, explaining why it was developed to compare thousands of bacterial genomes. The conversation covers core and accessory genes, the computational shortcuts that make Roary fast, and the importance of consistent annotation and quality control. It also explores the software’s name, hidden cluster support, unusually candid FAQ and statistical follow-up with Scoary.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 36: Roary the pangenome pipeline" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/899876332&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 36: Roary the pangenome pipeline on SoundCloud](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline)

## In this episode

### The problem Roary was built to solve

Roary creates bacterial pangenomes: comparisons that identify genes shared across a collection and genes that vary between its members. Andrew distinguishes the conserved core genome from accessory variation, including plasmids, phages and integrons. Using Salmonella as an illustration, he asks which collection of genes defines the organism and which additional genes help it survive in particular environments.

The practical motivation came from large sample collections at the Sanger Institute. Researchers wanted to extract core and accessory information, but the literature contained pangenomes of only around 80–100 bacteria. Tools discussed include PanOCT, LS-BSR, GET_HOMOLOGUES and OrthoMCL. An early attempt to adapt OrthoMCL ran into complexity, particularly its MySQL database requirements. Roary’s goal was to make collections of thousands or tens of thousands of bacterial genomes tractable.

### A family name and a short paper

Development began around 2013, with publication following in 2015 as a two-page Bioinformatics application note. Andrew recalls roughly 30 pages of supplementary material. Colleagues within the Sanger Institute were using the software internally, providing rapid feedback about what they needed and which features were unnecessary.

Internally, it was simply the pangenome pipeline, with similarly functional script names. Opening it up to others prompted the search for a distinctive name. Roary references the children’s programme Roary the Racing Car and Andrew’s son, whose name is spelt differently. Lee remembers Andrew showing him a photograph of the original Roary. Andrew stresses the practical benefit of a unique software name that people can find easily.

### Pre-clustering and hidden cluster support

Andrew describes the underlying comparison as an all-against-all BLAST of genes. Roary first uses CD-HIT to pre-cluster the data, greatly reducing the number of comparisons required. Within a bacterial species, repeatedly encountering similar genes means that adding genomes need not produce the same growth in work as comparing every sequence against every other sequence. Andrew also describes memory use as scaling linearly and reports that others have successfully used Roary on about 20,000 genomes.

The software was designed as scripts connected by job runners, allowing work to be distributed across an HPC cluster. That support remains hidden rather than prominently advertised and works with LSF. In practice, users often preferred a single machine with, for example, 64 threads instead of distributing thousands of jobs across a cluster.

### Why annotation consistency matters

Roary was deliberately designed to take output from Prokka rather than accommodate arbitrary GFF or annotation files. Andrew explains that supporting one straightforward annotation tool removed many input-handling problems. Downloading a mixture of genomes from GenBank or EMBL can instead combine annotations made by different tools and gene predictors, which may call genes differently and distort the comparison.

One of the hosts points out the trade-off: painstakingly curated GenBank annotations may be discarded in favour of consistent automated annotations from Prokka or RefSeq. Useful detail can disappear, but consistency is particularly important for analysis at scale. Andrew’s advice is to process the bacterial collection consistently from the outset and analyse it together, rather than combine independently prepared inputs and assume they are equivalent.

### Core-gene thresholds and quality control

The FAQ grew out of real support requests, ranging from attempts to run Perl scripts with Python to requests for someone else to analyse the data. It also explains substantive issues. A core-gene threshold allowing presence in 99% of genomes produces step changes at each hundred genomes because gene presence is counted in whole numbers. Requiring presence in every genome avoids that particular threshold effect, but incomplete assemblies and contig breaks make some tolerance useful.

Andrew repeatedly returns to quality control. A result containing only about 150 core genes could reflect contamination or an excessively broad comparison, such as trying to build a pangenome of everything Gram-negative. He uses Roary as a quick contamination check himself. His wider warning is that running complex analytical software without understanding the inputs and methods leaves users unable to interpret the results reliably.

### Packaging, maintenance and follow-up analysis

Roary’s availability through Debian and Ubuntu, Homebrew and Conda is another practical advantage discussed. Andrew describes a Perl codebase using Moose, with extensive automated unit tests and a structure intended to be readable by other Perl programmers. The hosts briefly compare their experiences of Perl and Python.

At the time of recording, Andrew reports well over 1,000 citations and use in public health laboratories and analysis pipelines. He says he has not updated Roary for years after moving jobs and projects, but welcomes changes and additions through GitHub. PopPUNK and Panaroo are mentioned as newer alternatives to investigate if Roary does not meet a user’s needs; the discussion does not establish a single best tool.

Scoary is recommended for statistical follow-up to Roary output, using information such as case and control labels. The episode closes by returning to the same practical priority: quality-control the data before trusting the pangenome.

## Highlights

- [00:01:15](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=1:15) — What bacterial pangenomes capture, and why Sanger needed larger analyses
- [00:06:02](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=6:02) — Roary’s spelling, racing-car connection and distinctive software name
- [00:06:48](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=6:48) — Development around 2013, publication in 2015 and the original HPC design
- [00:08:23](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=8:23) — LSF cluster support and CD-HIT pre-clustering to reduce BLAST comparisons
- [00:09:47](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=9:47) — Why Roary was designed around Prokka rather than arbitrary annotations
- [00:11:01](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=11:01) — The trade-off between consistent annotation and detailed GenBank curation
- [00:14:37](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=14:37) — The FAQ’s warning about pangenomes generated without sequencing QC
- [00:15:41](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=15:41) — Why a 99% core-gene threshold creates steps every hundred genomes
- [00:17:22](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=17:22) — Community uptake, maintenance and newer tools including PopPUNK and Panaroo
- [00:18:50](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=18:50) — Scoary for statistical analysis of Roary output using cases and controls
- [00:19:41](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=19:41) — Over-broad pangenomes, contamination and the need to check input data

## In their own words

> And I would expect people to have a baseline knowledge and not just try and randomly run pieces of complex analytical software because they won't be able to interpret the results properly.
>
> — Andrew Page, [00:14:50](https://soundcloud.com/microbinfie/roary-the-pangenome-pipeline#t=14:50)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Roary, PanOCT, LS-BSR, GET_HOMOLOGUES, OrthoMCL, MySQL, CD-HIT, BLAST, LSF, Prokka, GenBank, EMBL, RefSeq, Perl, Moose, Python, Debian, Ubuntu, Homebrew, Conda, GitHub, PopPUNK, Panaroo, Scoary.

## Questions this episode answers

### What problem does Roary solve?

Roary compares bacterial genomes to identify shared core genes and variable accessory genes. It was developed to make pangenome analysis feasible for thousands or tens of thousands of genomes, rather than the roughly 80–100-genome collections Andrew was seeing in the literature.

### How does Roary make large pangenome comparisons faster?

It uses CD-HIT to pre-cluster genes before all-against-all BLAST comparisons, reducing the number of comparisons required. Andrew also describes LSF-based cluster support, although users often preferred running on one machine with many threads.

### Why should Roary inputs be annotated consistently?

Different annotation tools and gene predictors can call genes differently, making a mixed collection difficult to compare reliably. Andrew designed Roary around Prokka output and recommends processing the whole collection consistently rather than mixing downloaded annotations.

### Why can core-genome size jump every hundred genomes?

Andrew explains that a 99% presence threshold produces steps because the permitted number of missing genomes changes in whole numbers. Requiring genes in every genome removes that threshold effect, but assembly gaps and contig breaks are reasons to allow some tolerance.

### What is Scoary used for alongside Roary?

The hosts recommend Scoary for statistical follow-up to Roary output. Andrew describes supplying case and control information to obtain further statistical results.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat with Andrew about Roary, software for generating a pangenome,
and learn about the background to the project, where the name comes
from, hidden features and the light hearted FAQ.  Paper:
https://academic.oup.com/bioinformatics/article/31/22/3691/240757
Software: https://github.com/sanger-pathogens/Roary Documentation:
https://sanger-pathogens.github.io/Roary/
