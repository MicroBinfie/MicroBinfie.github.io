---
layout: page
title: 'Episode 47: SARS-CoV-2 Rapid roundup and questions answered'
date: '2021-02-08 00:00:00'
link: https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered
episode: '47'
soundcloud_track: '981609127'
tags:
- microbinfie
- podcast
description: 'Missing SNPs, E484K, Nanopore basecalling, ARTIC artefacts and genome sharing: practical SARS-CoV-2 analysis advice from February 2021.'
excerpt: 'Missing SNPs, E484K, Nanopore basecalling, ARTIC artefacts and genome sharing: practical SARS-CoV-2 analysis advice from February 2021.'
headline: SARS-CoV-2 lineages, sequencing pitfalls and open data
guests:
- Leonardo de Oliveira Martins
topics:
- sars-cov-2
- lineage assignment
- phylogenetics
- e484k
- sequencing quality control
- nanopore basecalling
- recombination artefacts
- variant annotation
- genomic surveillance
- open data
faq:
- q: Why can one missing SNP change a Pangolin lineage assignment?
  a: 'The episode describes Pangolin’s decision-tree approach at the time: missing an informative SNP can change the route through the classifier. The panel recommends checking the underlying SNPs, missing regions and phylogenetic placement when an assignment looks inconsistent.'
- q: Should I use a GPU for SARS-CoV-2 Nanopore basecalling?
  a: Andrew recommends a compatible NVIDIA GPU to make HAC, high-accuracy basecalling, practical rather than relying on fast mode. He describes CPU processing as slow and notes that cloud processing may be limited by connectivity and cost.
- q: Can ARTIC sequencing reliably establish SARS-CoV-2 recombination?
  a: The panel warns that PCR chimeras in ARTIC data can be mistaken for recombination, especially when interpreting short Illumina fragments. They recommend metagenomics or possibly hybrid capture followed by de novo assembly for that question.
- q: Which tools can annotate SARS-CoV-2 mutations?
  a: The episode suggests CoV-GLUE, Nextclade for FASTA input and SnpEff for VCF input. Ben Jackson’s type_variants script is also mentioned for reporting amino acid replacements from genomes aligned to a reference.
- q: Why share raw reads as well as SARS-CoV-2 consensus genomes?
  a: Raw reads allow analysts to revisit the evidence and processing decisions behind a consensus sequence as methods change. Andrew reports that 15 of 25 papers he examined lacked available raw reads, limiting reproducibility.
---

*SARS-CoV-2 lineages, sequencing pitfalls and open data*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan are joined by Leonardo de Oliveira Martins, head of phylogenomics at the Quadram Institute, for a SARS-CoV-2 analysis roundup recorded on 5 February 2021. They discuss unstable lineage assignments, recurring spike mutations, sequencing artefacts and tools for annotating variants. The conversation also covers practical barriers to sequencing and why sharing consensus genomes alone is insufficient for reproducible analysis.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 47: SARS-CoV-2 Rapid roundup and questions answered" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/981609127&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 47: SARS-CoV-2 Rapid roundup and questions answered on SoundCloud](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered)

## In this episode

### Why one missing SNP can change a lineage

Andrew passes on a question he had been asked: why can losing a single SNP completely change a SARS-CoV-2 lineage assignment? Leonardo explains that Pangolin’s approach at the time uses a decision tree, with SNPs at particular positions acting as features. Missing an informative feature can send a sequence down a different branch of that classifier.

Choosing the closest sequence in a database has limitations too: overall similarity does not necessarily capture phylogenetic position. Leonardo suggests inspecting the sequence’s placement in a tree and mentions llama as a relevant approach. Andrew also describes checking SNPs manually when a cluster contains an unexpected assignment, especially when epidemiological evidence suggests otherwise. The practical message is to investigate important discrepancies rather than treating the lineage label as definitive: missing regions, unusual distances and long branches can all warrant closer inspection.

### E484K, lineage names and repeated mutations

The panel distinguishes a lineage from a mutation appearing within it. E484K, nicknamed “eek” in the discussion, describes a change from E to K at position 484 in the spike protein. Andrew explains why B.1.1.7 plus E484K can be a useful description when that mutation has arisen independently in different parts of the tree, rather than marking one newly spreading lineage.

Leonardo describes repeated appearances as homoplasy, while cautioning that this observation alone does not establish convergent evolution rather than chance or drift. The genetic background matters; looking only for one spike mutation does not identify the whole variant. For proposed new lineages, he points to criteria including a supported cluster in the global tree and epidemiological evidence. The discussion also covers door-to-door surge testing in eight UK areas following community detections of B.1.351.

### Co-infection claims and RNA quality

Andrew questions an unnamed paper reporting infections with two different SARS-CoV-2 lineages. He says controls were not described and roughly 53% of its SNPs were C-to-U changes, raising concerns about degraded RNA and contamination as alternative explanations. These are concerns about interpreting the reported signal, not confirmation that the samples were contaminated.

The panel discusses how delayed freezing can affect RNA quality and whether substitution-bias checks should be built into analysis pipelines. Andrew already uses such checks to identify extreme outliers. C-to-U mutations can be genuine, so the warning concerns unusually high rates rather than the presence of that substitution alone.

### Nanopore accuracy, shipping and ARTIC artefacts

For Nanopore basecalling, Andrew recommends high-accuracy mode, HAC, rather than fast mode because small differences matter for SARS-CoV-2 analysis. A compatible NVIDIA GPU makes this practical; he suggests that a gaming laptop or an older 1080 card may suffice. CPU basecalling is described as slow, while cloud processing can be constrained by cost, electricity and internet access.

A collaboration with Zimbabwe illustrates another bottleneck. Reagents remained at Stansted Airport for two weeks, beyond what their dry ice could sustain, destroying thousands of pounds’ worth of material. Room-temperature equipment could be shipped, but border closures and flight restrictions complicated the cold chain.

The discussion then turns to recombination claims from ARTIC data. PCR chimeras can resemble biological signals, and short Illumina fragments make interpretation particularly difficult. For Nanopore, the panel stresses requiring barcodes at both ends and filtering read lengths. To investigate recombination or structural variation, they recommend metagenomics or possibly hybrid capture with de novo assembly, rather than relying on ARTIC consensus sequences.

### Annotating variants and tracking community spread

The suggested annotation resources are CoV-GLUE, Nextclade for FASTA sequences and SnpEff for VCF files. Leonardo adds Ben Jackson’s type_variants Python script, which takes a genome aligned to the reference and reports amino acid replacements. Its small size makes it a candidate for incorporation into other software or workflows.

The hosts also discuss using Nextstrain maps to recognise community spread and repeated introductions of variants of concern. They emphasise that extensive sequencing can reveal many introductions rather than a single contained event.

At the Quadram Institute, sequencing had passed 10,000 genomes, with another 1,500 added that week. Andrew describes samples from local hospitals, national community testing and the REACT study. Randomly selected households in REACT provide a structured way to examine how much virus is circulating; sequencing positive samples can then help establish which lineages were present and when B.1.1.7 began appearing in those surveys.

### Open genomes need accessible raw reads

The Nature news article “Scientists call for fully open sharing of coronavirus genome data” prompts a discussion of INSDC archives and GISAID. Andrew contrasts open access with protections intended to encourage hesitant contributors to share. He also reports that INSDC turnaround was a limitation for immediate public health surveillance at the time.

The panel considers contributors’ interests, appropriate reuse and the difficulties of establishing shared expectations outside a consortium. It then separates access to consensus genomes from access to the evidence behind them. Andrew says that 15 of 25 papers he recently examined lacked available raw reads. Consensus sequences or assemblies alone do not allow analysts to revisit every processing decision as methods change. He also says that about 20% of studies he has seen did not submit to GISAID, and that some countries that approached his group for help were using others’ public data for context without sharing their own, arguing that participation needs to work in both directions.

## Highlights

- [00:01:21](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=1:21) — Why one missing SNP can change a SARS-CoV-2 lineage assignment
- [00:05:54](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=5:54) — Choosing lineage names and describing B.1.1.7 with additional mutations
- [00:08:59](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=8:59) — Does repeated E484K indicate convergent evolution?
- [00:14:19](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=14:19) — Questioning co-infection reports: controls, substitution bias and contamination
- [00:16:51](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=16:51) — HAC basecalling, NVIDIA GPUs and resource constraints
- [00:19:03](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=19:03) — Cold-chain failures when shipping Nanopore reagents to Zimbabwe
- [00:21:56](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=21:56) — Requiring Nanopore barcodes at both ends to filter artefacts
- [00:22:40](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=22:40) — Annotating variants with CoV-GLUE, Nextclade and SnpEff
- [00:24:26](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=24:26) — Recognising community spread and multiple introductions in Nextstrain
- [00:25:29](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=25:29) — Quadram sequencing totals and hospital, community and REACT samples
- [00:28:05](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=28:05) — INSDC and GISAID: openness, contributor protections and turnaround
- [00:30:36](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=30:36) — Missing raw reads and the limits of reproducibility

## In their own words

> So make sure you use the right technology to answer the question that you're asking.
>
> — Andrew Page, [00:19:03](https://soundcloud.com/microbinfie/47-sars-cov-2-rapid-roundup-and-questions-answered#t=19:03)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Leonardo de Oliveira Martins** (guest, Quadram Institute)

Also mentioned: Ben Jackson.

## Tools and resources mentioned

Pangolin, llama, ARTIC protocol, Oxford Nanopore, Illumina, HAC basecalling, CoV-GLUE, Nextclade, SnpEff, type_variants, Nextflow, Nextstrain, GISAID, INSDC, NCBI, EBI, DDBJ.

## Questions this episode answers

### Why can one missing SNP change a Pangolin lineage assignment?

The episode describes Pangolin’s decision-tree approach at the time: missing an informative SNP can change the route through the classifier. The panel recommends checking the underlying SNPs, missing regions and phylogenetic placement when an assignment looks inconsistent.

### Should I use a GPU for SARS-CoV-2 Nanopore basecalling?

Andrew recommends a compatible NVIDIA GPU to make HAC, high-accuracy basecalling, practical rather than relying on fast mode. He describes CPU processing as slow and notes that cloud processing may be limited by connectivity and cost.

### Can ARTIC sequencing reliably establish SARS-CoV-2 recombination?

The panel warns that PCR chimeras in ARTIC data can be mistaken for recombination, especially when interpreting short Illumina fragments. They recommend metagenomics or possibly hybrid capture followed by de novo assembly for that question.

### Which tools can annotate SARS-CoV-2 mutations?

The episode suggests CoV-GLUE, Nextclade for FASTA input and SnpEff for VCF input. Ben Jackson’s type_variants script is also mentioned for reporting amino acid replacements from genomes aligned to a reference.

### Why share raw reads as well as SARS-CoV-2 consensus genomes?

Raw reads allow analysts to revisit the evidence and processing decisions behind a consensus sequence as methods change. Andrew reports that 15 of 25 papers he examined lacked available raw reads, limiting reproducibility.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We present a rapid round up of SARS-CoV-2 questions and issues,
hopefully with some answers, so that you can stay on top of the latest
in SARS-CoV-2 genomics. Recorded 5 February 2021.  Topics covered: Why
missing 1 SNP can cause lineage assignment to break and how it works?
How do we describe lineages with a chain of mutation events? Are we
seeing convergent evolution? Co-infections of different lineages
discovered? For nanopore basecalling do use HAC & should you get a
GPU? Basic logistics difficult for sequencing in many parts of world.
Can I look at recombination with ARTIC on Illumina?  How do you
annotate a SARS-CoV-2 sequence?  http://cov-glue.cvr.gla.ac.uk/#/home
FASTA > nextclade   VCF > snpeff  https://github.com/cov-
ert/type_variants   Spotting community spread from NextStrain?
Scientists call for fully open sharing of coronavirus genome data:
https://www.nature.com/articles/d41586-021-00305-7
