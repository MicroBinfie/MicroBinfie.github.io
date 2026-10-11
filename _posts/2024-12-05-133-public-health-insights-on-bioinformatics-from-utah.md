---
layout: page
title: 'Episode 133: The Role of Bioinformatics in Public Health and Disease Outbreaks'
date: '2024-12-05 00:00:00'
link: https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah
episode: '133'
soundcloud_track: '1933430264'
tags:
- microbinfie
- podcast
description: Erin Young discusses bacterial species typing in Utah public health and testing Nanopore reads for antimicrobial resistance gene detection.
excerpt: Erin Young discusses bacterial species typing in Utah public health and testing Nanopore reads for antimicrobial resistance gene detection.
headline: Klebsiella typing and Nanopore AMR detection in public health
guests:
- Erin Young
topics:
- public health bioinformatics
- antimicrobial resistance
- klebsiella
- bacterial species identification
- outbreak analysis
- nanopore sequencing
- long reads
- sequencing coverage
- bioinformatics careers
faq:
- q: How did Erin Young move from cancer research into public health bioinformatics?
  a: After research on hereditary breast and ovarian cancer and a postdoc involving paediatric cancers, Erin sought work outside academia. A CDC and APHL bioinformatics fellowship helped her transition to the Utah Public Health Laboratory.
- q: Which tools does Erin use for bacterial species identification?
  a: She names MASH, FastANI and skani. She updates her MASH reference using representative genomes and says the default sketch size works for her.
- q: Can AMR genes be detected directly from Nanopore reads?
  a: Erin describes testing this by converting FASTQ reads to FASTA, analysing them with NCBI’s AMRFinderPlus and comparing the results with corresponding Illumina assemblies. She sees promise when enough reads support a call, but remains cautious about read errors.
- q: What Nanopore coverage is needed for reliable AMR gene detection?
  a: 'The episode does not establish a threshold: Erin says coverage analysis is work for a later poster. Andrew’s references to 10×, 20× and COVID sequencing protocols are not recommendations validated for her workflow.'
---

*Klebsiella typing and Nanopore AMR detection in public health*

Andrew Page interviews Dr. Erin Young of the Utah Public Health Laboratory at the 10th Microbial Bioinformatics Hackathon in Bethesda, Maryland. They discuss her move from cancer research into public health, the practical difficulties of identifying closely related Klebsiella species, and tools for comparing bacterial genomes. Erin also describes research into detecting antimicrobial resistance genes directly from Nanopore reads, including the unresolved question of how much coverage is enough.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 133: The Role of Bioinformatics in Public Health and Disease Outbreaks" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1933430264&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 133: The Role of Bioinformatics in Public Health and Disease Outbreaks on SoundCloud](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah)

## In this episode

### From cancer research to public health

Erin Young began learning bioinformatics while researching inherited predisposition to cancer. Her laboratory shared a bioinformatician with another group, and she did not want to wait for her analyses. Her PhD concerned hereditary breast and ovarian cancer; a short postdoctoral position extended that interest to different diseases and a paediatric cancer cohort.

During her postdoc at the University of Utah, she decided academia was not the right fit and looked for another setting where she could apply her skills to interesting work. A CDC and APHL bioinformatics fellowship provided the route into public health. She has worked at the Utah Public Health Laboratory since 2018.

### Bacterial genomes and outbreak analysis

Erin’s main responsibility is bacterial sequence analysis. Her current focus includes antimicrobial-resistant organisms and completing their genomes as far as possible, with the aim of supporting robust outbreak studies. She describes a broad public health workload, with more questions to investigate than she has time to pursue.

Andrew asks whether Utah encounters C. auris or other particular challenges. Erin confirms that C. auris and COVID are both present in Utah, but stresses that she is not the bioinformatician responsible for either. Her answers therefore centre on the bacterial work she handles directly.

### Why Klebsiella species labels matter

Klebsiella subtyping takes more of Erin’s time than she thinks anyone intended. The difficulty she describes is distinguishing closely related Klebsiella species and related organisms, rather than identifying one particularly prevalent sequence type.

That distinction matters beyond the analysis itself. Erin explains that once an organism name enters an epidemiological report, changing it can be difficult. Subsequent analyses linking organisms in an outbreak are then expected to use the original species designation. The conversation highlights a practical tension: improving a species assignment does not necessarily mean that the corresponding reporting process can readily accommodate the change.

### MASH, FastANI and skani

For species identification, Erin uses MASH with a reference built from representative genomes. She rebuilds that reference when the underlying genome resource is updated. Keeping the reference current can help identification, but it also creates a choice between being comprehensive and keeping results consistent over time.

Andrew asks about sketch size, saying he tends to choose either 1,000 or 10,000 without a firm basis. Erin says the default size works for her; she does not present a comparison establishing an optimum. Her laboratory also uses FastANI with representative genomes and skani, which she explicitly spells out. She describes skani as faster, although she finds its inputs more cumbersome than those of the other tools.

### Testing AMR detection directly from Nanopore reads

Erin previews a poster for ASM NGS about the effect of Nanopore read errors on antimicrobial resistance gene detection. Rather than comparing assemblies or a range of assembly-based methods, she asks whether the raw reads themselves can identify AMR genes accurately. The rationale is that a long read can contain an entire resistance gene.

Her workflow converts FASTQ reads to FASTA, runs them through NCBI’s AMRFinderPlus, and compares the Nanopore results with corresponding Illumina assemblies. Andrew sees potential relevance to directly sequenced metagenomic samples, where long reads might reveal useful resistance information. That is an application he raises in discussion, rather than a validation study Erin reports.

### Read errors and the unanswered coverage question

Erin remains cautious about Nanopore accuracy. SNPs are still present, but she explains that errors at different positions across reads can be overcome when enough reads support a result. Andrew distinguishes detecting a whole gene from identifying a particular point mutation, which he expects to be harder.

How many reads are enough remains unanswered. When Andrew asks whether she has examined coverage or established a threshold, Erin says that will require a later poster. Andrew mentions 10× and 20× as examples of numbers people choose, and recalls a 20× minimum used for ARTIC during COVID work. He explicitly notes that these involve different protocols. None of those numbers is presented as a validated threshold for Erin’s Nanopore AMR workflow.

## Highlights

- [00:00:48](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=0:48) — Andrew introduces the interview with Erin Young at the Bethesda hackathon.
- [00:01:11](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=1:11) — Erin explains why waiting for shared bioinformatics support prompted her to learn the subject.
- [00:02:17](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=2:17) — A CDC and APHL fellowship provides a route from cancer research into public health.
- [00:03:42](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=3:42) — Erin describes laboratory priorities, including AMR organisms and complete genomes for outbreak analysis.
- [00:05:29](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=5:29) — Klebsiella subtyping reveals difficulties with closely related species and fixed reporting labels.
- [00:07:12](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=7:12) — MASH reference updates create a trade-off between comprehensive and consistent species identification.
- [00:07:59](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=7:59) — Erin discusses MASH defaults, FastANI and skani.
- [00:08:38](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=8:38) — An ASM NGS poster investigates AMR gene detection directly from Nanopore reads.
- [00:10:24](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=10:24) — The workflow converts FASTQ to FASTA, runs AMRFinderPlus and compares against Illumina assemblies.
- [00:11:23](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=11:23) — Erin explains how differing SNP positions across reads affect confidence in AMR calls.
- [00:11:39](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=11:39) — A minimum coverage threshold remains a question for future work.

## In their own words

> So if you have enough reads, then the noise cancels out.
>
> — Erin Young, [00:11:23](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=11:23)

> Alas, that will have to be a later poster.
>
> — Erin Young, [00:11:39](https://soundcloud.com/microbinfie/133-public-health-insights-on-bioinformatics-from-utah#t=11:39)

## Who is talking

- **Andrew Page** (host)
- **Erin Young** (guest, Utah Public Health Laboratory)
- **Lee Katz** (host)

## Tools and resources mentioned

MASH, FastANI, skani, Nanopore, Illumina, NCBI AMRFinderPlus, ARTIC.

## Questions this episode answers

### How did Erin Young move from cancer research into public health bioinformatics?

After research on hereditary breast and ovarian cancer and a postdoc involving paediatric cancers, Erin sought work outside academia. A CDC and APHL bioinformatics fellowship helped her transition to the Utah Public Health Laboratory.

### Which tools does Erin use for bacterial species identification?

She names MASH, FastANI and skani. She updates her MASH reference using representative genomes and says the default sketch size works for her.

### Can AMR genes be detected directly from Nanopore reads?

Erin describes testing this by converting FASTQ reads to FASTA, analysing them with NCBI’s AMRFinderPlus and comparing the results with corresponding Illumina assemblies. She sees promise when enough reads support a call, but remains cautious about read errors.

### What Nanopore coverage is needed for reliable AMR gene detection?

The episode does not establish a threshold: Erin says coverage analysis is work for a later poster. Andrew’s references to 10×, 20× and COVID sequencing protocols are not recommendations validated for her workflow.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie podcast, host Andrew Page talks with Dr. Erin Young, a
bioinformatician at the Utah Public Health Laboratory, recorded during the 10th Microbial
Bioinformatics Hackathon in Bethesda, Maryland. Erin shares her journey from researching
hereditary cancer predisposition to her current role in public health bioinformatics, which she
entered through a prestigious CDC and APHL fellowship. The conversation delves into her work
with bacterial pathogens, particularly in tracking antimicrobial resistance in organisms like
Klebsiella. Erin discusses the tools she uses for genome typing, such as MASH, FastANI, and
SKA, and her innovative research on the accuracy of long-read sequencing technologies like
Nanopore for detecting antimicrobial resistance genes. She also provides a preview of her
upcoming poster for ASM, where she examines how Nanopore reads can be used effectively in
public health microbiology. This episode offers a fascinating look at how bioinformatics and
genomics are advancing the fight against infectious diseases.
