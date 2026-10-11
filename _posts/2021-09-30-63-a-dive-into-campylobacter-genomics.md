---
layout: page
title: 'Episode 63: A dive into Campylobacter genomics'
date: '2021-09-30 00:00:00'
link: https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics
episode: '63'
soundcloud_track: '1080404938'
tags:
- microbinfie
- podcast
description: Ozan Gundogdu discusses Campylobacter genomes, phase variation, laboratory passage, plasmids and the case for long-read sequencing.
excerpt: Ozan Gundogdu discusses Campylobacter genomes, phase variation, laboratory passage, plasmids and the case for long-read sequencing.
headline: 'Campylobacter genomics: phase variation, plasmids and poultry'
guests:
- Ozan Gundogdu
topics:
- campylobacter
- reference genome annotation
- phase variation
- homopolymer tracts
- laboratory passage
- plasmids
- secretion systems
- chicken microbiome
- long-read sequencing
- pangenomics
faq:
- q: Why can laboratory passage complicate Campylobacter experiments?
  a: Gundogdu describes sequence variation and plasmid loss during passage, both of which can affect experimental phenotypes. He recommends preparing substantial frozen stocks, working from early passages and using reference assays to monitor unexpected changes.
- q: Which software is discussed for Campylobacter homopolymer tracts?
  a: The episode mentions Tatajuba as software for examining homopolymer tracts in more detail. These regions matter because changes in their lengths can alter reading frames and gene products.
- q: What could long-read sequencing add to Campylobacter research?
  a: The panel discusses using long reads to characterise plasmids and other material that may remain unresolved in short-read analyses, and to improve chicken microbiome studies. Gundogdu stresses that sequencing still needs to be interpreted alongside experimental metadata.
- q: What metadata are useful in chicken microbiome studies?
  a: Gundogdu names environmental factors, chicken weight, feed conversion ratio, histology and immunology. He describes combining these measurements with sequencing to investigate changes associated with feed, farm conditions and Campylobacter detection.
---

*Campylobacter genomics: phase variation, plasmids and poultry*

Dr Ozan Gundogdu of the London School of Hygiene and Tropical Medicine joins the hosts to discuss what bioinformaticians need to understand about Campylobacter. The conversation connects reference-genome annotation, phase variation and plasmids with the practical difficulties of maintaining reproducible laboratory strains. It also examines chicken microbiome studies and why sequencing data need to be interpreted alongside experimental and environmental metadata.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 63: A dive into Campylobacter genomics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1080404938&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 63: A dive into Campylobacter genomics on SoundCloud](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics)

## In this episode

### The reference genome and the value of reannotation

The discussion starts with Campylobacter jejuni NCTC11168, the reference strain whose genome the episode dates to 1999. Gundogdu describes a relatively small genome of 1.64 megabases, approximately 1,654 predicted open reading frames and a GC content of about 30%. Its sequence revealed capsule and lipooligosaccharide structures, numerous homopolymer tracts and an absence of the classical type III and type IV secretion systems in that strain.

Gundogdu also recalls working at the Sanger Institute to update the reference annotation. Within roughly five or six years of the original publication, accumulated experimental research allowed him to update almost 20% of its gene-product functions. CRISPR-associated features were among the additions. His point is that sequencing a reference is not the end of maintaining it.

### Phase variation and changing laboratory stocks

Homopolymer tracts are repeated runs of the same nucleotide. Gundogdu explains how changes in these runs can alter reading frames and gene products, producing phase variation. He discusses their occurrence in genes associated with capsule and lipooligosaccharide structures and their proposed role in helping bacteria evade immune responses.

Asked whether the tracts might simply be sequencing artefacts, he points to their identification through Sanger sequencing and subsequent examination with long reads. He mentions Tatajuba as software for investigating these regions.

The practical concern is that repeated passage can change the organism being studied. Gundogdu describes SNP differences even between stocks of the same strain within a laboratory. His advice is to prepare a substantial frozen stock, use early passages and maintain a few reference assays, such as growth measurements, that can flag unexpected changes. Those checks do not exclude underlying sequence variation.

### Secretion systems and environmental survival

The reference genome did not capture every secretion system subsequently found across Campylobacter. Gundogdu notes later discoveries of type IV systems on plasmids in some strains and estimates that approximately 25–30% of Campylobacter have a type VI secretion system. He frames their possible advantages in bacterial competition, host interactions and particular environments as research questions.

He also describes work showing that flagella can secrete effectors rather than serving only in motility. Another theme is survival under damaging environmental conditions: genome studies identified enzymes involved in breaking down reactive oxygen species, but Gundogdu particularly emphasises the regulators controlling those genes. For him, that regulatory complexity is central to understanding Campylobacter physiology.

### Plasmids, phages and sequencing blind spots

When asked about TraDIS, Gundogdu says published experiments indicate that it works in Campylobacter, while noting that he has not performed it himself. He then discusses strain 81176 and its p-tet plasmid, which carries tetracycline resistance. Plasmids can be lost during passage, changing the material used in an experiment and potentially its phenotype.

The panel also considers DNA that remains unassigned after short-read analysis and the risk of concentrating on the chromosome while overlooking plasmids. Long-read sequencing is presented as a way to characterise that additional material more clearly.

Andrew Page asks whether epigenetic modifications prevent some Campylobacter phages from being sequenced with Illumina. Gundogdu says he is unfamiliar with that finding. The episode therefore leaves this as an open question, rather than establishing how often phages are missed.

### Chicken microbiomes need sequencing and metadata

Gundogdu describes moving from laboratory physiology towards understanding Campylobacter in poultry production. His group's chicken microbiome experiments have used 16S studies, which he considers useful but limited. He argues for long-read approaches using PacBio or Oxford Nanopore to improve understanding of these communities.

Their studies found substantial effects of feed changes on microbial community structure. The largest community changes occurred a day or two before Campylobacter was detected, typically at around two weeks. Other experiments examined farm conditions and feed supplements, including omega, alongside Campylobacter numbers.

The accompanying metadata are essential: environmental measurements, chicken weight, feed conversion ratio, histology and immunology can help interpret microbial changes. Andrew also asks whether farms repeatedly acquire Campylobacter from outside or retain it in their infrastructure. He mentions Mark Pallen's long-read chicken microbiome work, but the panel does not establish whether it answers that strain-persistence question.

### Large comparisons and closer links with laboratory science

Gundogdu describes a growing collection of publicly available Campylobacter genomes and a preprint that he recalls analysing more than 50,000 isolates. He sees a need for comprehensive comparisons across locations and phylogenies, alongside software for pangenome analysis. Roary is discussed as an example, not as a demonstrated analysis of all those isolates in the episode.

His central warning for newcomers is that one sequenced strain cannot represent an entire species. Variation occurs between species, between strains and during laboratory maintenance. He also sees a gap between available computational tools and their adoption in pathogenesis and physiology research, and hopes newer researchers will be comfortable connecting bioinformatics with laboratory experiments.

## Highlights

- [00:02:14](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=2:14) — The NCTC11168 reference genome, its size and homopolymer tracts.
- [00:03:55](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=3:55) — Low GC content, natural DNA uptake and variation in secretion systems.
- [00:06:18](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=6:18) — Evidence for homopolymer tracts, passage-related changes and Tatajuba.
- [00:07:43](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=7:43) — TraDIS experiments and plasmid loss during laboratory passage.
- [00:08:26](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=8:26) — Andrew asks whether phage modifications create Illumina sequencing blind spots.
- [00:12:49](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=12:49) — Laboratory models and applying Campylobacter research to poultry settings.
- [00:14:52](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=14:52) — Limits of 16S studies and the importance of chicken microbiome metadata.
- [00:21:14](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=21:14) — Large isolate collections and the need for comprehensive genomic comparisons.
- [00:23:02](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=23:02) — Sequence differences within the same strain and the need for consistent stocks.
- [00:27:41](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=27:41) — Long-read sequencing and overlooked extrachromosomal material.
- [00:30:53](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=30:53) — Why a single Campylobacter strain cannot represent its species.
- [00:31:42](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=31:42) — Pangenome tools and improving connections between computational and laboratory research.

## In their own words

> We're not just talking about, you know, different continents; we're talking potentially the same lab because obviously passages change things.
>
> — Ozan Gundogdu, [00:23:02](https://soundcloud.com/microbinfie/63-a-dive-into-campylobacter-genomics#t=23:02)

## Who is talking

- **Ozan Gundogdu** (guest, London School of Hygiene and Tropical Medicine)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Lee Katz** (host)

Also mentioned: Mark Pallen.

## Tools and resources mentioned

Tatajuba, Roary, TraDIS, Sanger sequencing, 16S sequencing, PacBio, Oxford Nanopore, Illumina.

## Questions this episode answers

### Why can laboratory passage complicate Campylobacter experiments?

Gundogdu describes sequence variation and plasmid loss during passage, both of which can affect experimental phenotypes. He recommends preparing substantial frozen stocks, working from early passages and using reference assays to monitor unexpected changes.

### Which software is discussed for Campylobacter homopolymer tracts?

The episode mentions Tatajuba as software for examining homopolymer tracts in more detail. These regions matter because changes in their lengths can alter reading frames and gene products.

### What could long-read sequencing add to Campylobacter research?

The panel discusses using long reads to characterise plasmids and other material that may remain unresolved in short-read analyses, and to improve chicken microbiome studies. Gundogdu stresses that sequencing still needs to be interpreted alongside experimental metadata.

### What metadata are useful in chicken microbiome studies?

Gundogdu names environmental factors, chicken weight, feed conversion ratio, histology and immunology. He describes combining these measurements with sequencing to investigate changes associated with feed, farm conditions and Campylobacter detection.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Our guest today is Dr Ozan Gundogdu for a deeper dive into the food
borne pathogen Campylobacter and how genomics has informed the field
over the past 20 years since the publication of the first reference
genome in 1999.  Ozan leads the foodborne enteric pathogen group at
the London school of hygiene and tropical medicine. Where they study
the physiology and pathogenesis of Campylobacter and other related
enteric microorganisms like Listeria and Vibrio. His background is in
Molecular Biology and Computer Science and he completed his PhD at
LSHTM (London School of Hygiene & Tropical Medicine) in 2011.
www.lshtm.ac.uk/aboutus/people/gundogdu.ozan
