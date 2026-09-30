---
layout: page
title: 'Episode 72: Bactopia and using workflow managers in bioinformatics  part 1'
date: '2022-01-06 00:00:00'
link: https://soundcloud.com/microbinfie/bactopia-part-1
episode: '72'
soundcloud_track: '1131828346'
tags:
- microbinfie
- podcast
description: Robert Petit explains how Bactopia processes bacterial genomes, separates isolate analysis from comparative genomics, and builds on Nextflow.
excerpt: Robert Petit explains how Bactopia processes bacterial genomes, separates isolate analysis from comparative genomics, and builds on Nextflow.
headline: 'Bactopia: bacterial genome analysis and workflow managers'
guests:
- Robert Petit
topics:
- bacterial genomics
- workflow managers
- quality control
- antimicrobial resistance
- comparative genomics
- phylogenetics
- public sequence data
- genome subsampling
- software development
faq:
- q: What results does Bactopia produce from bacterial sequencing reads?
  a: The episode describes read quality control, genome assembly, annotation, antimicrobial resistance predictions and multilocus sequence typing. Supplementary datasets can support reference-based variant calling and searches against user-supplied sequences.
- q: Does Bactopia build phylogenetic trees?
  a: Yes, through the separate Bactopia tools workflows. Petit keeps comparative analyses separate so users can inspect isolate results, exclude unsuitable samples and choose a relevant dataset before running more demanding analyses.
- q: Can Bactopia download public sequencing data?
  a: Petit explains that users can provide SRA accessions and have the workflow download the reads. He also describes support for public data from GenBank, RefSeq and ENA.
- q: How can researchers request another tool in Bactopia?
  a: Petit recommends opening a GitHub feature request describing the desired tool. His stated requirement is that it be available through Bioconda, and he offers to investigate packaging tools that are not yet on Bioconda.
---

*Bactopia: bacterial genome analysis and workflow managers*

Robert Petit of the Wyoming Public Health Laboratory joins the hosts to explain Bactopia, an all-in-one bacterial genome analysis workflow. He traces its origins in Staphopia and discusses quality control, reference datasets, comparative genomics and Nextflow. The discussion centres on getting usable results quickly while keeping analysis steps understandable and allowing users to choose which samples proceed.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 72: Bactopia and using workflow managers in bioinformatics  part 1" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1131828346&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 72: Bactopia and using workflow managers in bioinformatics  part 1 on SoundCloud](https://soundcloud.com/microbinfie/bactopia-part-1)

## In this episode

### From Staphopia to Bactopia

Bactopia grew out of work that began around 2010, when Petit was a master's student. The initial goal was to download and consistently analyse the hundreds of public Staphylococcus aureus datasets then available through the Sequence Read Archive and European Nucleotide Archive. An early website called Staphopedia accepted FASTQ uploads and launched shell scripts; the project later became Staphopia.

Repeated rewrites took the workflow through Perl, Python, a Python workflow manager and finally Nextflow around 2016–17. Requests to analyse other organisms exposed the limits of a staphylococcal workflow. Processing Haemophilus influenzae required manually removing species-specific steps and changing references. Bactopia became an opportunity to generalise that work and adopt newer workflow and container approaches, rather than asking other users to understand and modify Staphopia's internals.

### What an isolate run produces

Petit describes Bactopia as a way to turn raw sequence data into a broad set of results that researchers are likely to need. A typical example starts with bacterial FASTQ files and a question about antibiotic resistance. The workflow filters poor-quality reads, creates an assembly, annotates the genome and makes antimicrobial resistance predictions. Multilocus sequence typing provides another useful output, allowing users to investigate whether an isolate belongs to a sequence type known to be associated with a certain virulence.

The intended audience includes people who can obtain sequencing data but do not yet know which tools to combine. Petit nevertheless encourages users to learn the command line and understand the analysis. The documentation explains individual steps and identifies the programs responsible, providing a route from running the workflow to investigating its components.

### Reference datasets and public sequence inputs

Bactopia can run without supplementary datasets, or users can build datasets to support species-specific analysis. Examples include Mash's RefSeq sketch and sourmash's GenBank sketch for preliminary checks of sequence identity. A sample expected to be S. aureus but matching E. coli is a reason to investigate, rather than simply continuing with the expected species label.

Users can supply reference genomes for SNP and indel calling, plus genes, proteins or primers for BLAST searches. Public-data support includes GenBank, RefSeq, SRA and ENA; an SRA accession can be supplied as an input for downloading reads. Petit also describes curated Bactopia datasets, with a working S. aureus example, and invites species experts to contribute useful reference selections.

### Checkpoints before comparative genomics

The episode distinguishes Bactopia's isolate workflow from Bactopia tools: separate workflows for comparative genomics, including phylogenetic analysis. This separation lets users process samples first, inspect quality and decide which belong in a comparison. Minimum requirements can stop unsuitable samples before expensive downstream steps—for example, avoiding an assembly attempt with only 2× coverage. Structured output directories and inclusion or exclusion lists support subsequent analyses.

The Bactopia paper provides a practical example. A public collection labelled Lactobacillus contained a yeast sample and some Streptococcus samples. A quick tree exposed conspicuous outliers. To focus on a particular Lactobacillus species, the researchers used FastANI against a reference genome, selected samples within a chosen ANI range, and used that subset for pangenome analysis and a core-genome tree. The paper listed in the show notes is identified by DOI 10.1128/mSystems.00190-20.

### Choosing representatives from thousands of genomes

One host asks how to reduce 67,000 S. aureus genomes to roughly 1,000 useful tree tips. Petit does not offer a universal solution. For S. aureus, the team created a non-redundant dataset, nicknamed the nerd set, by choosing one high-quality genome per sequence type. At that point, this reduced about 40,000 genomes to roughly 400 representatives, which could help guide further selection.

A host describes selecting one representative per rMLST type as another practical approach, although it requires assemblies and typing results already to exist. The discussion distinguishes subsampling an analysed collection from searching public data for relevant neighbours. Species-specific population structure remains an important complication.

### Contributing tools and moving to modular workflows

Petit welcomes GitHub feature requests for tools used by other bacterial research communities. His stated requirement is availability through Bioconda, because installation and supporting container infrastructure are already addressed. If a requested tool is not packaged there, he is willing to investigate adding it. He also emphasises responding promptly to issues so that installation or analysis problems do not cause users to abandon the workflow.

Contributors helped move Bactopia from Nextflow DSL1 to DSL2, enabling reusable modules, subworkflows and workflows. Petit describes incorporating Staphopia-specific analyses into this structure. He also discusses planned integration with nf-core modules and contributing individual tool modules back, so that people building other workflows can reuse the same components without adopting Bactopia itself.

## Highlights

- [00:02:18](https://soundcloud.com/microbinfie/bactopia-part-1#t=2:18) — Petit introduces Bactopia and thanks the developers of the tools it uses.
- [00:03:03](https://soundcloud.com/microbinfie/bactopia-part-1#t=3:03) — The master's project and repeated Staphopia rewrites that led to Bactopia.
- [00:13:27](https://soundcloud.com/microbinfie/bactopia-part-1#t=13:27) — Getting from raw sequences to useful results, with documentation for learners.
- [00:16:19](https://soundcloud.com/microbinfie/bactopia-part-1#t=16:19) — A resistance-analysis use case, isolate outputs and supplementary datasets.
- [00:18:14](https://soundcloud.com/microbinfie/bactopia-part-1#t=18:14) — Why comparative genomics sits in separate Bactopia tools workflows.
- [00:22:52](https://soundcloud.com/microbinfie/bactopia-part-1#t=22:52) — Public Lactobacillus data reveal mislabelled samples and motivate ANI-based selection.
- [00:25:31](https://soundcloud.com/microbinfie/bactopia-part-1#t=25:31) — How could 67,000 S. aureus genomes become a manageable phylogenetic dataset?
- [00:26:06](https://soundcloud.com/microbinfie/bactopia-part-1#t=26:06) — Staphopia's non-redundant set selects one high-quality genome per sequence type.
- [00:28:58](https://soundcloud.com/microbinfie/bactopia-part-1#t=28:58) — Species expertise and curated reference datasets for Bactopia.
- [00:30:20](https://soundcloud.com/microbinfie/bactopia-part-1#t=30:20) — Requesting new tools through GitHub and the Bioconda packaging requirement.
- [00:32:24](https://soundcloud.com/microbinfie/bactopia-part-1#t=32:24) — A contributor pull request leads into DSL2 modularity and nf-core reuse.

## In their own words

> The only requirement is it has to be on Bioconda just because I think that's a good starting point.
>
> — Robert Petit, [00:30:20](https://soundcloud.com/microbinfie/bactopia-part-1#t=30:20)

## Who is talking

- **Robert Petit** (guest, Wyoming Public Health Laboratory)
- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Bactopia, Staphopia, Staphopedia, Nextflow, Nextflow DSL1, Nextflow DSL2, nf-core modules, Bioconda, BioContainers, Docker, Singularity, GitHub, Mash, sourmash, FastANI, BLAST, MLST, rMLST, GenBank, RefSeq, Sequence Read Archive, European Nucleotide Archive.

## Questions this episode answers

### What results does Bactopia produce from bacterial sequencing reads?

The episode describes read quality control, genome assembly, annotation, antimicrobial resistance predictions and multilocus sequence typing. Supplementary datasets can support reference-based variant calling and searches against user-supplied sequences.

### Does Bactopia build phylogenetic trees?

Yes, through the separate Bactopia tools workflows. Petit keeps comparative analyses separate so users can inspect isolate results, exclude unsuitable samples and choose a relevant dataset before running more demanding analyses.

### Can Bactopia download public sequencing data?

Petit explains that users can provide SRA accessions and have the workflow download the reads. He also describes support for public data from GenBank, RefSeq and ENA.

### How can researchers request another tool in Bactopia?

Petit recommends opening a GitHub feature request describing the desired tool. His stated requirement is that it be available through Bioconda, and he offers to investigate packaging tools that are not yet on Bioconda.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We are joined by Dr Robert Petit from the Wyoming Public Health
Laboratory who is talking to us about BACTOPIA, a bioinformatics
workflow specifically for bacterial genomes.

- Docs: https://bactopia.github.io/
- Repo: https://github.com/bactopia/bactopia/
- Pub: https://doi.org/10.1128/mSystems.00190-20
