---
layout: page
title: 'Episode 87: Nextstrain, SARSCOV2 and dealing with a data deluge'
date: '2022-07-21 00:00:00'
link: https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge
episode: '87'
soundcloud_track: '1283756557'
tags:
- microbinfie
- podcast
description: Emma Hodcroft and Leonardo de Oliveira Martins discuss Nextstrain, SARS-CoV-2 downsampling, data quality and the CoVariants website.
excerpt: Emma Hodcroft and Leonardo de Oliveira Martins discuss Nextstrain, SARS-CoV-2 downsampling, data quality and the CoVariants website.
headline: Nextstrain, SARS-CoV-2 and the challenge of 10 million genomes
guests:
- Emma Hodcroft
- Leonardo de Oliveira Martins
topics:
- sars-cov-2
- phylogenetics
- genomic surveillance
- downsampling
- sampling bias
- metadata quality
- workflow automation
- variant tracking
- science communication
faq:
- q: Why did Nextstrain limit its SARS-CoV-2 trees to about 5,000 sequences?
  a: Emma describes this as a balance between analysis speed, browser performance and interpretability. Trees with 8,000–10,000 tips could become sluggish, while a tree containing millions of sequences would be difficult to understand even if it could be displayed.
- q: How does Nextstrain select background sequences for a local outbreak?
  a: The proximity function finds sequences similar to a focal set, such as samples from a suspected outbreak. The priority function converts those results into sampling priorities so that relevant background sequences can be preferentially included.
- q: Can outbreak sampling bias a SARS-CoV-2 phylogenetic analysis?
  a: 'Yes: an outbreak investigation can contribute many closely related genomes rather than a representative surveillance sample. Emma says sampling-type metadata is often missing, so detailed local investigations may require checking with the data contributors.'
- q: What information does CoVariants provide?
  a: CoVariants shows the proportions of sequenced SARS-CoV-2 samples belonging to different variants across countries and over time. It also provides mutation comparisons and a simplified Nextstrain tree showing relationships between variants.
---

*Nextstrain, SARS-CoV-2 and the challenge of 10 million genomes*

Emma Hodcroft and Leonardo de Oliveira Martins discuss how SARS-CoV-2 pushed phylogenetic workflows from small, manually managed datasets to millions of sequences. The conversation covers Nextstrain’s daily builds, downsampling and metadata checks, alongside the development of CoVariants. They explain why both the choice of sequences and the way results are displayed matter for researchers and the wider public.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 87: Nextstrain, SARSCOV2 and dealing with a data deluge" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1283756557&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 87: Nextstrain, SARSCOV2 and dealing with a data deluge on SoundCloud](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge)

## In this episode

### Adapting Nextstrain to SARS-CoV-2

Emma explains that Nextstrain’s pre-pandemic development as a modular, flexible pipeline made the initial adaptation to SARS-CoV-2 relatively straightforward. Bioinformatic questions such as choosing a reference sequence and setting or inferring a mutation rate still had to be sorted out, but running the pipeline was not the main obstacle.

A more immediate change concerned presentation. Rather than displaying very small branch-length values, the team showed the number of mutations separating sequences. Emma says that most sequences still had fewer than 100 changes across a roughly 30,000-base genome at the time of recording. Mutation counts offered a more understandable scale for visitors without a phylogenetics background.

### Explaining trees to a much wider audience

Nextstrain attracted scientists and members of the public who were unfamiliar with phylogenetic trees. Emma describes the danger of reading a colourful tree as a definite account of someone travelling between countries and introducing the virus. Such stories could have real-world consequences, especially if a sequence was misplaced.

The team initially previewed every build before publication and paid greater attention to accompanying interpretation. They also produced situation reports using Nextstrain narratives: text alongside an interactive tree that changes as the reader scrolls. These explained how to read a phylogeny and were being translated into more than 20 languages during their early-pandemic peak.

### From copying FASTA files to automated daily builds

Early analyses were strikingly manual: sequences were copied into FASTA files, and team members ran the pipeline on laptops as new data arrived. As datasets grew, work moved to compute clusters. Research assistants Moira Zuber and Eli Harkins helped check and standardise dates, sequence names and geographical labels, with work continuing seven days a week during the first few months.

By this episode, the discussion puts GISAID at around 10 million sequences. Nextstrain restricts its global and continental trees to about 5,000 sequences each. Emma says browser visualisation can be pushed towards 8,000–10,000 tips, but responsiveness deteriorates; displaying millions would also be difficult to interpret.

Data cleaning, daily runs and publication eventually became automated, creating a need for automated quality control rather than relying on someone inspecting every tree. Even compressed file downloads and repeated reading and writing became substantial bottlenecks. Emma notes that limited internet access makes these problems especially difficult for some laboratories.

### Choosing relevant sequences rather than simply fewer

The earliest Nextstrain downsampling aimed for an even spread across geography and time, reducing the imbalance between countries that sequenced heavily and those that sequenced little. Regional builds preferentially included sequences from the focal continent, with a smaller background sample from elsewhere.

Emma describes adding a proximity function to find sequences similar to a focal set, such as North American samples or a suspected outbreak. This makes the background more relevant than a random worldwide sample. Within Nextstrain Augur, proximity calculates similarity to the focal sequences, while the priority function turns that information into values used for sampling. Both can be used in other pipelines, and the code is open source.

Leonardo describes another objective: selecting fewer leaves from an existing tree while preserving its phylogenetic diversity. For local investigations, he discusses Uvaia, developed at the Quadram, which scans a database for sequences closest to a query and returns matches with statistics.

### Sampling bias and unreliable metadata

A large sequence collection is not necessarily a random survey. An outbreak investigation may contribute many closely related genomes, distorting the broader picture. GISAID has a field for sampling type, but Emma says Nextstrain does not currently receive it automatically, and submitters often leave it unfilled. The person uploading sequences may also be far removed from the person who collected the samples.

Earlier in the pandemic, the team sometimes contacted contributors about suspicious clusters of similar dates and locations. That became impractical at scale. Emma considers the issue less influential in heavily downsampled global views, but important for local investigations. Date errors remain another recurring problem, including Omicron sequences labelled January 2021, inconsistent day/month ordering and Excel-altered date fields.

### CoVariants and accessible variant information

CoVariants grew out of Emma’s work on EU1, a variant that circulated widely in Europe during summer 2020. She had made graphs showing its spread and the other variants present in different countries. Alpha’s emergence added urgency to sharing those plots, initially through a GitHub repository and then a full website launched shortly before the end of 2020.

The site shows the proportions of sequences assigned to different variants by country and over time, and lets visitors compare mutations between variants. A simplified tree showing relationships between variants comes from Nextstrain. One of the hosts describes using the site to help answer family members’ questions.

Emma’s advice for similar projects is to identify the audience and the information they need. A useful website need not expose every detail: simplifying the presentation can make existing scientific information accessible while keeping it accurate.

## Highlights

- [00:01:58](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=1:58) — Adapting Nextstrain’s existing pipeline to SARS-CoV-2 and changing how trees were presented
- [00:06:59](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=6:59) — Moving from manually collected sequences to automated, downsampled daily analyses
- [00:12:15](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=12:15) — Sampling across geography and time, then choosing relevant background sequences
- [00:15:09](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=15:09) — How the proximity and priority functions work within Nextstrain Augur
- [00:16:08](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=16:08) — Leonardo’s approaches to preserving phylogenetic diversity and finding close matches with Uvaia
- [00:18:10](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=18:10) — Distinguishing surveillance samples from outbreak investigations when metadata is incomplete
- [00:20:31](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=20:31) — Date mix-ups, Excel problems and Omicron sequences assigned to the wrong year
- [00:21:39](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=21:39) — The origins of CoVariants and its country-level variant and mutation displays
- [00:24:56](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=24:56) — A simplified tree showing how SARS-CoV-2 variants are related
- [00:25:55](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=25:55) — Designing scientific websites around their audience rather than including every detail

## In their own words

> Nextstrain is now flexible enough that if you have a virus you want to run it on, the pipeline essentially will usually work just fine.
>
> — Emma Hodcroft, [00:01:58](https://soundcloud.com/microbinfie/nextstrain-sarscov2-and-dealing-with-a-data-deluge#t=1:58)

## Who is talking

- **Emma Hodcroft** (guest, ISPM, University of Bern; Swiss Institute of Bioinformatics (SIB))
- **Leonardo de Oliveira Martins** (guest, Quadram Institute)
- **Nabil-Fareed Alikhan** (host)
- **Lee Katz** (host)
- **Andrew Page** (host)

Also mentioned: Moira Zuber, Eli Harkins.

## Tools and resources mentioned

Nextstrain, Nextstrain narratives, Nextstrain Augur, Nextstrain proximity function, Nextstrain priority function, GISAID, Uvaia, CoVariants, GitHub, Excel.

## Questions this episode answers

### Why did Nextstrain limit its SARS-CoV-2 trees to about 5,000 sequences?

Emma describes this as a balance between analysis speed, browser performance and interpretability. Trees with 8,000–10,000 tips could become sluggish, while a tree containing millions of sequences would be difficult to understand even if it could be displayed.

### How does Nextstrain select background sequences for a local outbreak?

The proximity function finds sequences similar to a focal set, such as samples from a suspected outbreak. The priority function converts those results into sampling priorities so that relevant background sequences can be preferentially included.

### Can outbreak sampling bias a SARS-CoV-2 phylogenetic analysis?

Yes: an outbreak investigation can contribute many closely related genomes rather than a representative surveillance sample. Emma says sampling-type metadata is often missing, so detailed local investigations may require checking with the data contributors.

### What information does CoVariants provide?

CoVariants shows the proportions of sequenced SARS-CoV-2 samples belonging to different variants across countries and over time. It also provides mutation comparisons and a simplified Nextstrain tree showing relationships between variants.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

87 Nextstrain, SARSCOV2 and dealing with a data deluge by Microbial Bioinformatics
