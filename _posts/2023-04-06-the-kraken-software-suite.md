---
layout: page
title: 'Episode 104: The Kraken software suite'
date: '2023-04-06 00:00:00'
link: https://soundcloud.com/microbinfie/the-kraken-software-suite
episode: '104'
soundcloud_track: '1407306292'
tags:
- microbinfie
- podcast
description: Jennifer Lu and Natalia Rincon explain Kraken's tools, database trade-offs, pathogen detection and contamination checks.
excerpt: Jennifer Lu and Natalia Rincon explain Kraken's tools, database trade-offs, pathogen detection and contamination checks.
headline: 'Kraken, KrakenUniq and Bracken: classification and contamination'
guests:
- Jennifer Lu
- Natalia Rincon
topics:
- taxonomic classification
- metagenomics
- pathogen detection
- microbiome analysis
- reference databases
- contamination detection
- abundance estimation
- k-mers
- minimisers
faq:
- q: What is the difference between Kraken and Bracken?
  a: Kraken classifies reads at the most specific taxonomic level supported by their sequence evidence, so some reads are assigned only at genus or family level. Bracken uses a Bayesian algorithm to re-estimate read counts and abundances at a selected level, such as species or genus.
- q: Why do the guests prefer KrakenUniq for clinical pathogen detection?
  a: Their laboratory is concerned about Kraken 2's small false-positive rate when looking for rare pathogen evidence, so it generally uses KrakenUniq for infectious pathogen detection. They favour Kraken 2's speed and smaller storage requirements for diversity and abundance analyses.
- q: Can KrakenUniq run when its database is larger than available RAM?
  a: The guests describe an option that lets users specify available RAM and compare reads against portions of the database in turn. This avoids loading the whole database at once, at some cost in speed.
- q: Can Kraken check contamination in isolate sequencing data?
  a: Yes. Katz describes treating an expected single-genome sample as a metagenome and looking for conflicting taxonomic assignments, such as Listeria in an E. coli sample. The guests also use Kraken to identify host contamination in draft eukaryotic pathogen genomes.
---

*Kraken, KrakenUniq and Bracken: classification and contamination*

Jennifer Lu and Natalia Rincon from Johns Hopkins University join the hosts to explain the Kraken software suite, from taxonomic classification to abundance estimation and visualisation. They compare Kraken 1, KrakenUniq and Kraken 2, including their memory requirements and approaches to counting sequence evidence. Clinical examples and contamination checks show why database composition matters as much as the choice of software.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 104: The Kraken software suite" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1407306292&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 104: The Kraken software suite on SoundCloud](https://soundcloud.com/microbinfie/the-kraken-software-suite)

## In this episode

### From Kraken 1 to Kraken 2

The guests trace the suite back to the original Kraken, developed in 2013–2014. They describe its exact k-mer matching, a k-mer size of 31 and the use of Jellyfish. KrakenUniq retains Kraken 1's database structure and classification approach while adding unique k-mer counts. The rationale is that evidence for a species should be spread across its genome, rather than consist of repeated matches to the same sequence.

Kraken 2 addresses the growing size of reference databases through a probabilistic data structure and minimisers. The example given is a reduction from a roughly 300 GB database to about 30–50 GB, with a small accuracy trade-off and faster classification. The algorithm discussion also covers shorter sequence representations and caching: nearby k-mers can share a minimiser, reducing repeated lookup work.

### Unique counts, limited RAM and abundance estimates

The episode describes the incorporation of KrakenUniq-style counting into Kraken 2, with an important distinction: Kraken 2 counts unique minimisers rather than unique k-mers. KrakenUniq also has an option to process a large database in portions, allowing users to specify their available RAM instead of loading everything at once. This reduces memory requirements at some cost in speed.

Bracken answers a different question from Kraken. Kraken classifies reads as specifically as their evidence permits, so assignments may stop at genus or family rather than species. Bracken uses a Bayesian algorithm to re-estimate read counts and abundances at a chosen level, such as species or genus. The guests also explain that KrakenUniq and Kraken 2 databases can coexist in one folder without duplicating the library and taxonomy files.

### Making classification reports usable

Pavian provides an R/Shiny graphical interface for inspecting Kraken reports. It helps users compare read counts across species and see graphical representations of what is present in a sample. Lu, who is not its author, calls it near and dear to her heart and says it makes analysing Kraken reports far easier.

KrakenTools is their ongoing collection of scripts for downstream work, including extracting reads, producing visualisations and calculating statistical metrics. Rather than being another classifier, it supports different uses of Kraken's output. Both guests also co-authored the Nature Protocols paper introduced in the episode, which covers metagenomic analysis using the Kraken software suite.

### Microbiomes and clinical pathogen detection

The discussion covers microbiome analysis in drinking water, waterways and the human gut, including interest in microbes in Baltimore's Inner Harbor. The guests' own laboratory places more emphasis on pathogen detection. Working with Johns Hopkins Hospital clinicians, they analyse sequencing data from samples such as cerebrospinal fluid and brain biopsies. Many analyses do not identify a pathogen, but published examples include detecting tuberculosis and a viral infection using Kraken and Pavian.

Rincon describes an early PhD project involving an ocular sarcoidosis dataset with patient and control whole-genome sequencing. It introduced her directly to the infectious pathogen detection pipeline, with Lu providing support.

For these investigations, the laboratory generally prefers the Kraken 1-based KrakenUniq because of concerns about Kraken 2's small false-positive rate when searching for rare pathogen evidence. Kraken 2 is useful for diversity and abundance work where its speed and smaller database are advantages. Clinical interpretation focuses on presence or absence rather than quantifying an infection, and relies on doctors and pathological verification.

### Reference coverage and contamination checks

A host asks how pathogen-heavy reference collections affect microbiome analysis, using Salmonella as an example. The guests emphasise that results depend on what has been sequenced and included in the database. They describe NCBI RefSeq Complete as strongly weighted towards bacterial and viral genomes, with fewer eukaryotic pathogen genomes. Bracken can adjust read-count estimates, but users still need to understand their reference collection.

Lee Katz describes treating an expected single-genome sample as a metagenome for quality control. Conflicting assignments, such as Listeria reads in an E. coli sample, can flag contamination. Another host runs Kraken on isolate data and describes EnteroBase checks that expect about 90% of genomic content to match the intended species.

The guests also use Kraken to screen draft eukaryotic pathogen genomes against bacteria, human sequences, vertebrates and plants. This has exposed contamination from hosts: for forms of malaria found in hosts such as chicken or cow, they found a lot of chicken DNA in the draft genomes. Contaminating regions can then be masked. They also mention adding the T2T consortium's complete human genome to their databases, which has produced further contamination findings.

### Keeping the suite practical as databases grow

The team plans to maintain the Kraken GitHub repositories and continue improving accuracy, speed and usefulness. KrakenTools will gain scripts and downstream analyses as new needs arise.

Database growth remains a central challenge. Rincon identifies smaller databases as necessary for keeping Kraken usable as more genomes become available. The possibilities under discussion include different indexing and sketching approaches, as well as hosting on a compute resource; these are directions being explored rather than announced solutions.

## Highlights

- [00:02:00](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=2:00) — Kraken 1's exact k-mer matching and the development of KrakenUniq and Kraken 2
- [00:04:50](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=4:50) — How minimisers help reduce Kraken 2's database size
- [00:05:30](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=5:30) — Caching and shared minimisers as an explanation for faster lookups
- [00:06:03](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=6:03) — Unique-minimiser counting brings KrakenUniq-style functionality into Kraken 2
- [00:10:20](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=10:20) — Rincon's early PhD work with an ocular sarcoidosis sequencing dataset
- [00:11:22](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=11:22) — Microbiome applications and the laboratory's clinical pathogen detection work
- [00:13:07](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=13:07) — Why the laboratory favours KrakenUniq for infectious pathogen detection
- [00:14:32](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=14:32) — Database dependence and the limited representation of eukaryotic pathogens
- [00:16:23](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=16:23) — Treating a single-genome sample as a metagenome for contamination checks
- [00:17:21](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=17:21) — Screening draft eukaryotic pathogen genomes for host and other contamination
- [00:19:07](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=19:07) — Routine isolate checks and EnteroBase's expected-species threshold
- [00:20:40](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=20:40) — Smaller databases through indexing, sketching and possible hosted computing

## In their own words

> We need to figure out how to make the database smaller.
>
> — Natalia Rincon, [00:20:40](https://soundcloud.com/microbinfie/the-kraken-software-suite#t=20:40)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Jennifer Lu** (guest, Johns Hopkins University Center for Computational Biology)
- **Natalia Rincon** (guest, Johns Hopkins University Center for Computational Biology)

## Tools and resources mentioned

Kraken 1, KrakenUniq, Kraken 2, Bracken, Pavian, KrakenTools, Jellyfish, R, Shiny, NCBI RefSeq Complete, EnteroBase, T2T consortium human genome.

## Questions this episode answers

### What is the difference between Kraken and Bracken?

Kraken classifies reads at the most specific taxonomic level supported by their sequence evidence, so some reads are assigned only at genus or family level. Bracken uses a Bayesian algorithm to re-estimate read counts and abundances at a selected level, such as species or genus.

### Why do the guests prefer KrakenUniq for clinical pathogen detection?

Their laboratory is concerned about Kraken 2's small false-positive rate when looking for rare pathogen evidence, so it generally uses KrakenUniq for infectious pathogen detection. They favour Kraken 2's speed and smaller storage requirements for diversity and abundance analyses.

### Can KrakenUniq run when its database is larger than available RAM?

The guests describe an option that lets users specify available RAM and compare reads against portions of the database in turn. This avoids loading the whole database at once, at some cost in speed.

### Can Kraken check contamination in isolate sequencing data?

Yes. Katz describes treating an expected single-genome sample as a metagenome and looking for conflicting taxonomic assignments, such as Listeria in an E. coli sample. The guests also use Kraken to identify host contamination in draft eukaryotic pathogen genomes.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We talk about KRAKEN the taxonomic classification software and the software suite around it and
are joined by Jennifer Lu and Natalia Rincon from Johns Hopkins University Center for
Computational Biology.

Dr. Jennifer Lu and Natalia Rincon from the Kraken software development team were interviewed
on the MicroBinfie podcast. They discussed the various versions of Kraken and the tools
developed around it. They began by explaining the original Kraken, which uses an exact camera
matching process and a camera size of 31 based on jellyfish. Kraken Unique is an additional
version of Kraken that includes an additional column called unique camera counting, which
determines how many unique cameras are covered by each read, providing an additional way to
verify microbial identification. Kraken two was developed to accommodate larger databases by
using a probabilistic data structure and minimizers to map cameras to a shorter sequence size.

They then talked about how Kraken is useful for microbiome analysis, including detecting
pathogens. However, the accuracy of the results depends heavily on the availability of genomic
data in the database, which emphasizes bacterial and viral data. For infectious pathogen
detection, Kraken one unique is combined with Bracken to approximate the abundance of species
present.

The developers emphasized the importance of users being aware of available genomic data in the
database because the results can only be as accurate as the data. They also talked about how
Kraken is used widely in bioinformatics and can be used for various scenarios beyond
metagenomics. For example, they use Kraken to treat a single genome as a metagenome as part of
quality control analysis. In cases where there are conflicting taxa in the reads, Kraken
results show it, making it useful in determining the presence of contamination in samples.

The Kraken team also talked about how they use Kraken for contamination work to detect
contamination in pathogen genomes. They compare all eukaryotic pathogen genomes against
bacteria, human genomes, and databases of vertebrates and plants to filter out any
contaminants. They have found in some instances where contaminating sequences from hosts such
as chicken or cow were present in eukaryotic pathogen genomes.

Moving forward, the Kraken team intends to maintain all Kraken repositories, enhance its
accuracy, speed, and usefulness, and develop new scripts and downstream analysis for the Kraken
Tools suite. They acknowledge the need to make the database smaller as more genomes become
available and are exploring ways of indexing and sketching to achieve this.

In conclusion, Kraken has been an essential software for metagenomic analysis, and it remains a
continually improving tool for pathogen detection and classification. The Kraken team advises
users to keep in mind the importance of accurate data for effective pathogen detection and
classification.
