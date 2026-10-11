---
layout: page
title: 'Episode 131: Bioinformatics Evolution: Torsten Seemann on Snippy, Open-Source Support, and Global Genomics'
date: '2024-11-07 00:00:00'
link: https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics
episode: '131'
soundcloud_track: '1933421819'
tags:
- microbinfie
- podcast
description: Torsten Seemann discusses plans for Snippy NG, Nanopore and assembly support, Australian genomic surveillance and open-source maintenance.
excerpt: Torsten Seemann discusses plans for Snippy NG, Nanopore and assembly support, Australian genomic surveillance and open-source maintenance.
headline: Torsten Seemann on Snippy NG and sustaining genomic tools
guests:
- Torsten Seemann
topics:
- variant calling
- bacterial genomics
- public health genomics
- nanopore sequencing
- genomic surveillance
- open-source software
- software maintenance
- fuzzy core alignments
faq:
- q: Does Snippy support Nanopore reads?
  a: In this episode, Seemann says existing Snippy can sometimes work with Nanopore reads but is not optimised for them. Proper Nanopore support is a planned priority for Snippy NG, informed by benchmarking work with Michael Hall.
- q: How will Snippy NG handle pre-assembled genomes?
  a: Existing Snippy shreds contigs into artificial Illumina reads before processing them. Seemann describes a proof of concept using minimap2 to align contigs directly and call SNPs, with the aim of producing comparable VCF output from assemblies and sequencing reads.
- q: What is AusTrakka used for?
  a: Seemann describes AusTrakka as an online, semi-private surveillance platform developed to help Australian state laboratories share data. An early version was used during the COVID pandemic, and the discussion places it within continuing national genomic surveillance efforts.
- q: Who is funding development of Snippy NG?
  a: The Chan Zuckerberg Initiative awarded Seemann two years of funding through its open-source software scheme. The grant supports maintenance and improvement of existing software, including a postdoc developing Snippy NG.
---

*Torsten Seemann on Snippy NG and sustaining genomic tools*

Andrew Page catches up with Torsten Seemann at the 10th Microbial Bioinformatics Hackathon in Bethesda, Maryland. They discuss the expansion of genomics after COVID, Australian public health laboratories’ work on sharing data, and the difficulty of sustaining bioinformatics software. Seemann outlines two years of Chan Zuckerberg Initiative funding for Snippy’s next generation, including planned support for Nanopore reads, pre-assembled genomes and fuzzy core alignments.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 131: Bioinformatics Evolution: Torsten Seemann on Snippy, Open-Source Support, and Global Genomics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1933421819&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 131: Bioinformatics Evolution: Torsten Seemann on Snippy, Open-Source Support, and Global Genomics on SoundCloud](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics)

## In this episode

### More sequencing, more difficult choices

Andrew Page and Torsten Seemann return to a conversation they began at a hackathon in Norwich around 2019. Meeting again in Bethesda, they reflect on how the pandemic changed microbial bioinformatics: more laboratories have sequencing capacity, but there are also many competing software solutions to navigate.

Seemann describes working with partners across the Asia-Pacific region whose move into genomics was accelerated by COVID. Some lack dedicated bioinformatics personnel or access to dedicated training in their countries. They need practical ways to analyse Nanopore and Illumina data, but explaining the available options—and which suit a particular laboratory—is difficult. His concern is not simply a shortage of tools, but the overwhelming range of choices.

### Connecting Australia’s public health laboratories

Seemann works at Melbourne’s Microbiological Diagnostic Unit, a state public health laboratory. He explains that Australia does not have a national reference laboratory and describes much of his work over the preceding ten years as helping state laboratories collaborate and share data. That work contributed to AusTrakka, an online, semi-private surveillance and data-sharing platform. An immature version was used urgently during the COVID pandemic.

The laboratory is returning to its main work in bacterial genomics, while still dealing with viruses including monkeypox virus and Japanese encephalitis virus. National data sharing remains a priority, alongside interoperability with international platforms, the WHO Berlin hub and regional partners. Seemann attributes the laboratory’s broader reach partly to its position within the University of Melbourne’s microbiology department and the Doherty Institute: those connections allow public health work to sit alongside research, immunology and clinical services.

### Funding maintenance rather than starting again

The post-pandemic funding picture is less favourable. Seemann reports budget cuts, smaller bioinformatics teams and colleagues leaving public health for industry and other roles. Software development has slowed, while his own work has shifted towards management. Page recognises that transition, and a joke about who will do the Perl coding leads Seemann to mention a postdoc who is helping him write the next version of Snippy.

Seemann describes receiving his first grant through the Chan Zuckerberg Initiative’s open-source software scheme. Unlike conventional academic grants focused on research questions, this application asked directly about existing tools, competing software, maintenance problems and planned improvements. He found that a much better fit for his work. The award provides two years of funding and supports a postdoc developing Snippy NG, or Snippy the next generation. Seemann presents it as the opportunity to deliver improvements delayed by software ageing and limited attention during COVID, rather than a fully backward-compatible update.

### Snippy NG: reads and assemblies in one workflow

At the time of recording, the team was preparing a community user survey to send out before the end of 2024. Nanopore support was already a prominent request. Seemann says existing Snippy can sometimes work with Nanopore reads, but is not optimised for them. The next version is intended to retain Illumina support while adding a better-supported Nanopore workflow.

A Nanopore benchmarking paper developed with Michael Hall is informing those plans. Seemann describes it as awaiting publication and says the team has gained insight into efficient Nanopore variant calling. He also wants Snippy to accept pre-assembled genomes alongside read data, rather than forcing every input through the same read-based route.

Existing Snippy can accept contigs by shredding them into artificial Illumina reads. Seemann instead describes a working proof of concept using minimap2 to align contigs against contigs and call SNPs directly, which he reports is very fast. The goal is a uniform route from assemblies, Nanopore reads and Illumina reads to comparable VCF output, followed by core-genome alignments.

### Fuzzy alignments and software survival

Another planned change is support for fuzzy core alignments. Seemann points to research by Ryan Wick, known for Unicycler, into how far alignments can be relaxed before their signal is corrupted. He sees a fuzzy core approach as the direction Snippy should take, while presenting this as work for the next version rather than an already delivered feature.

Page connects these plans to a wider maintenance problem: useful tools can disappear when their developers finish a PhD, postdoc or grant, or when dependencies stop being updated. Seemann describes meeting other Chan Zuckerberg Initiative award recipients, including projects such as Bioconductor. Both emphasise the value of funding continued support for established software, rather than treating initial development as the end of the work.

## Highlights

- [00:00:48](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=0:48) — Andrew Page reunites with Torsten Seemann at the Bethesda hackathon.
- [00:01:45](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=1:45) — Seemann reflects on the expansion of sequencing capacity after COVID.
- [00:01:57](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=1:57) — Asia-Pacific partners face an overwhelming choice of bioinformatics tools.
- [00:03:00](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=3:00) — Australia’s state laboratory structure and efforts to coordinate data sharing.
- [00:05:44](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=5:44) — The transition from writing code to managing bioinformatics teams.
- [00:06:01](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=6:01) — Perl maintenance and the developer helping write Snippy’s next version.
- [00:06:33](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=6:33) — Seemann’s first grant and the Chan Zuckerberg Initiative’s maintenance funding.
- [00:08:16](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=8:16) — The Snippy postdoc’s experience in AI, phylogenetics and software engineering.
- [00:11:07](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=11:07) — Why useful bioinformatics tools disappear when maintenance stops.
- [00:11:42](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=11:42) — Support for established open-source projects, including Bioconductor.

## In their own words

> They say diversity is a good thing. I think we probably have a bit too much diversity in the bioinformatics space. It's quite overwhelming.
>
> — Torsten Seemann, [00:01:57](https://soundcloud.com/microbinfie/131-bioinformatics-evolution-torsten-seemann-on-snippy-open-source-support-and-global-genomics#t=1:57)

## Who is talking

- **Andrew Page** (host)
- **Torsten Seemann** (guest, Microbiological Diagnostic Unit (MDU), University of Melbourne; Doherty Institute)

Also mentioned: Michael Hall, Ryan Wick.

## Tools and resources mentioned

Snippy, Snippy NG, AusTrakka, Nanopore, Illumina, minimap2, BEAST, Unicycler, Bioconductor, Perl, fuzzy core alignments.

## Questions this episode answers

### Does Snippy support Nanopore reads?

In this episode, Seemann says existing Snippy can sometimes work with Nanopore reads but is not optimised for them. Proper Nanopore support is a planned priority for Snippy NG, informed by benchmarking work with Michael Hall.

### How will Snippy NG handle pre-assembled genomes?

Existing Snippy shreds contigs into artificial Illumina reads before processing them. Seemann describes a proof of concept using minimap2 to align contigs directly and call SNPs, with the aim of producing comparable VCF output from assemblies and sequencing reads.

### What is AusTrakka used for?

Seemann describes AusTrakka as an online, semi-private surveillance platform developed to help Australian state laboratories share data. An early version was used during the COVID pandemic, and the discussion places it within continuing national genomic surveillance efforts.

### Who is funding development of Snippy NG?

The Chan Zuckerberg Initiative awarded Seemann two years of funding through its open-source software scheme. The grant supports maintenance and improvement of existing software, including a postdoc developing Snippy NG.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie Podcast, host Andrew Page catches up with Torsten Seemann
at the 10th Microbial Bioinformatics Hackathon in Bethesda, Maryland. They discuss the rapid
evolution of bioinformatics, the challenges faced by labs worldwide, and the explosion of tools
post-COVID. Torsten shares insights into his work at Melbourne’s Microbiological Diagnostic
Unit (MDU), the development of platforms like OzTracker for bacterial genomics, and how his lab
plays a national and international role in data sharing.

The conversation dives into the future of the widely-used variant calling tool Snippy, as
Torsten reveals exciting updates funded by the Chan Zuckerberg Initiative, including nanopore
read support and the ability to process pre-assembled genomes. They also explore the importance
of maintaining open-source bioinformatics tools to prevent them from becoming obsolete. Tune in
for an in-depth discussion on the state of genomics, software development, and the challenges
and rewards of open-source collaboration.
