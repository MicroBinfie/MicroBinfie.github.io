---
layout: page
title: 'Episode 122: GAMBIT: Genomic Approximation Method for Bacterial Identification and Tracking'
date: '2024-03-09 00:00:00'
link: https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking
episode: '122'
soundcloud_track: '1770012039'
tags:
- microbinfie
- podcast
description: Lee Katz and Andrew Page discuss GAMBIT's targeted k-mers, species calls, reference databases and public health validation.
excerpt: Lee Katz and Andrew Page discuss GAMBIT's targeted k-mers, species calls, reference databases and public health validation.
headline: 'GAMBIT: targeted k-mers for microbial identification'
guests: []
topics:
- microbial identification
- targeted k-mers
- public health validation
- reference databases
- genome taxonomy
- integer encoding
- parallel computing
- fungal genomics
faq:
- q: How does GAMBIT select k-mers for species identification?
  a: Andrew describes searching a genome for a fixed prefix and collecting the suffixes that follow it. His example uses a five-base prefix and an 11-base suffix, producing a targeted signature for comparison with reference genomes.
- q: Does GAMBIT always return a species name?
  a: No. Andrew says it can return a genus-level assignment or decline to make a call when a species assignment is not supported, which he regards as important for public health use.
- q: Was GAMBIT described as clinically validated?
  a: Andrew initially uses clinical-validation language, but clarifies that he means validation for public health use after Lee questions it. The episode explicitly distinguishes the two.
- q: What do I need to try GAMBIT?
  a: Andrew directs listeners to the GAMBIT suite and describes downloading the software plus a reference database made up of two files. Users supply FASTA files and receive results including closest matches and distances.
---

*GAMBIT: targeted k-mers for microbial identification*

Lee Katz talks with Andrew Page about GAMBIT, the Genomic Approximation Method for Bacterial Identification and Tracking. Andrew explains how targeted k-mer signatures support conservative species identification, how reference databases are curated, and why integer-based storage makes comparisons efficient. They also distinguish public health validation from clinical validation and discuss applications beyond bacteria.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 122: GAMBIT: Genomic Approximation Method for Bacterial Identification and Tracking" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1770012039&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 122: GAMBIT: Genomic Approximation Method for Bacterial Identification and Tracking on SoundCloud](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking)

## In this episode

### A targeted signature rather than a random sample

GAMBIT identifies bacteria and eukaryotes using a selected subset of k-mers. Andrew describes looking through a genome for a particular prefix and retaining the bases immediately after it. His example uses a five-base prefix followed by an 11-base suffix. These selected sequences form a signature that can be compared with reference genomes.

Andrew contrasts this targeted selection with the random subsampling he describes for Mash. GAMBIT retains all the k-mers matching its chosen target rather than taking a random sample. He uses Salmonella as an example, estimating around 10,000 selected k-mers from a genome, and says the number collected roughly correlates with genome size. Comparisons within species help describe their diversity and assess whether a query falls within a species.

### Conservative calls and the validation distinction

Andrew's central argument is that identification needs a defensible species call, not just a list of possible matches. He contrasts GAMBIT with Kraken-style results that can contain a dominant species alongside many smaller assignments. His illustrative example includes 80% Salmonella and 10% E. coli, with other assignments contributing bioinformatics noise.

GAMBIT can make a species-level assignment, fall back to the genus level, or decline to call an identity. Andrew presents that conservatism as useful in public health, particularly for closely related organisms. The hosts also correct an important distinction: Andrew initially describes clinical validation, but clarifies that he means validation for public health use after Lee questions the claim. They agree that public health validation remains significant, but is not interchangeable with clinical validation.

### Integer encoding, HDF5 and metadata

Instead of storing every selected sequence as nucleotide text, GAMBIT converts the suffixes into numbers. Andrew describes a numerical space of roughly four million possible values in his example. Each genome's values occupy a chunk of stored data, with offsets allowing the software to retrieve the relevant array directly.

The numerical data are stored in HDF5, while an SQL database holds metadata that links the records together. Andrew does not settle on a particular SQL database system during the discussion. The advantage he emphasises is direct access to arrays and efficient operations on integers, including comparisons and intersections, rather than repeated manipulation of nucleotide strings. Lee asks whether HDF5 makes parsing and parallel access difficult, prompting a discussion of where computation actually needs accelerating.

### Reference databases and taxonomic quality control

GAMBIT's reference collections can be built from RefSeq or from another chosen set of genomes. Andrew describes both existing databases and his work on additional collections. The associated metadata are essential: a reference signature needs a reliable taxonomic label if it is to support identification.

Andrew says he has used GTDB instead of relying solely on NCBI taxonomy. He highlights GTDB's use of ANI to organise species and the availability of quality information, including CheckM results, contamination and completeness. These allow filtering before database construction. His concern is that an incorrectly labelled reference can distort later assignments; he gives the example of an E. coli genome labelled as Salmonella and warns that such errors can persist.

### Parallel comparisons and incremental database building

Andrew reports that GAMBIT's analysis parallelises well: when he has given it 32 threads, it has run close to maxing them out. He distinguishes extracting arrays from HDF5 from comparing their contents, arguing that effort should go into parallelising the slow parts rather than every operation.

Building a large reference database is a different workload. Andrew describes trying to process everything in RefSeq without quality filtering, then stopping the job after about ten days because it was consuming substantial memory. His alternative was incremental construction: process one species at a time and add it to the database. He says this reaches the same result while reducing memory requirements.

### Trying GAMBIT and extending its uses

To get started, Andrew directs listeners to the GAMBIT suite on GitHub. Users download the software and a reference database consisting of two files, then supply FASTA files. Outputs include closest matches and distances. He also describes using GAMBIT as a routing step in a bacterial processing pipeline, deciding which organism-specific tools, such as SISTR or ECTyper, should run next.

Beyond bacterial identification, Andrew mentions identifying Candida species and exploring pangenomic uses. Intersections of shared k-mers can support compact representations of core genome content. He presents these as extensions of the same numerical representation and set operations.

The show notes provide two papers: *GAMBIT (Genomic Approximation Method for Bacterial Identification and Tracking): A methodology to rapidly leverage whole genome sequencing of bacterial isolates for clinical identification* (DOI 10.1371/journal.pone.0277575), and *TheiaEuk: a species-agnostic bioinformatics workflow for fungal genomic characterization*.

## Highlights

- [00:00:00](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=0:00) — Lee introduces Andrew and the discussion of GAMBIT.
- [00:01:15](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=1:15) — Andrew explains targeted k-mer signatures for bacterial and eukaryotic identification.
- [00:06:03](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=6:03) — Lee questions what validation for clinical use would involve.
- [00:06:29](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=6:29) — Andrew clarifies that he means validation for public health use.
- [00:09:36](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=9:36) — Target prefixes, integer-encoded suffixes and offsets make genome signatures efficient to retrieve.
- [00:11:34](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=11:34) — RefSeq collections, GTDB taxonomy and quality filtering underpin reference database construction.
- [00:13:09](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=13:09) — Lee asks about HDF5 parsing, threading and the reasons for choosing the format.
- [00:13:46](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=13:46) — Andrew discusses parallelisation and the cost of building large reference databases.
- [00:15:42](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=15:42) — Lee asks how a new user can get started with GAMBIT.
- [00:15:57](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=15:57) — Andrew describes downloading the suite and databases, supplying FASTA files and reading results.

## In their own words

> You can waste a lot of time parallelizing stuff that doesn't need to be parallelized.
>
> — Andrew Page, [00:13:46](https://soundcloud.com/microbinfie/gambit-genomic-approximation-method-for-bacterial-identification-and-tracking#t=13:46)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)

## Tools and resources mentioned

GAMBIT, GAMBIT suite, Mash, Kraken, RefSeq, NCBI taxonomy, GTDB, ANI, CheckM, SISTR, ECTyper, TheiaEuk.

## Questions this episode answers

### How does GAMBIT select k-mers for species identification?

Andrew describes searching a genome for a fixed prefix and collecting the suffixes that follow it. His example uses a five-base prefix and an 11-base suffix, producing a targeted signature for comparison with reference genomes.

### Does GAMBIT always return a species name?

No. Andrew says it can return a genus-level assignment or decline to make a call when a species assignment is not supported, which he regards as important for public health use.

### Was GAMBIT described as clinically validated?

Andrew initially uses clinical-validation language, but clarifies that he means validation for public health use after Lee questions it. The episode explicitly distinguishes the two.

### What do I need to try GAMBIT?

Andrew directs listeners to the GAMBIT suite and describes downloading the software plus a reference database made up of two files. Users supply FASTA files and receive results including closest matches and distances.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We discuss GAMBIT, software for accurately classifying bacteria and eukaryotes using a targeted
k-mer based approach.

GAMBIT software: <https://github.com/gambit-suite/gambit> GAMBIT suite:
<https://github.com/gambit-suite>

GAMBIT (Genomic Approximation Method for Bacterial Identification and Tracking): A methodology
to rapidly leverage whole genome sequencing of bacterial isolates for clinical identification.
<https://doi.org/10.1371/journal.pone.0277575>

TheiaEuk: a species-agnostic bioinformatics workflow for fungal genomic characterization
<https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2023.1198213/full>
