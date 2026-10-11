---
layout: page
title: 'Episode 103: Release the Kraken'
date: '2023-03-23 00:00:00'
link: https://soundcloud.com/microbinfie/release-the-kraken
episode: '103'
soundcloud_track: '1406671645'
tags:
- microbinfie
- podcast
description: Jennifer Lu and Natalia Rincon explain Kraken classification, database choices, memory needs, abundance estimation and low-read pathogen detection.
excerpt: Jennifer Lu and Natalia Rincon explain Kraken classification, database choices, memory needs, abundance estimation and low-read pathogen detection.
headline: 'Kraken: databases, read classification and pathogen detection'
guests:
- Jennifer Lu
- Natalia Rincon
topics:
- taxonomic classification
- metagenomics
- reference databases
- k-mer matching
- abundance estimation
- microbial diversity
- pathogen detection
- nanopore sequencing
- contamination
faq:
- q: What is the difference between Kraken and Bracken?
  a: Kraken classifies sequencing reads into taxonomic groups. Bracken, developed by Jennifer Lu, uses Kraken output for abundance estimation.
- q: How much RAM does Kraken need?
  a: The guests describe Kraken2 databases requiring roughly 30–50 GB of RAM at the time of recording, with requirements changing as reference collections grow. Mini Kraken databases can target sizes such as 8 or 16 GB, at the cost of sensitivity and more unclassified reads.
- q: How many Kraken reads are enough to identify a pathogen?
  a: The guests do not give a universal threshold. They describe a brain-sample investigation where roughly a dozen reads led to a genuine pathogen finding, and recommend considering sample context and unique k-mer or minimiser support.
- q: Can Kraken classify Nanopore reads?
  a: Yes, although the guests warn that higher error rates can affect accuracy because Kraken was developed with Illumina reads in mind. They describe using the same database as acceptable with that caveat, while noting that an optimal Nanopore-specific k-mer size had not been established.
---

*Kraken: databases, read classification and pathogen detection*

Jennifer Lu and Natalia Rincon join the hosts to discuss Kraken, its taxonomic classification algorithm and the wider software suite. They explain database choices, memory requirements, abundance estimation and diversity analysis, then explore how to interpret small numbers of pathogen reads and handle Nanopore data.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 103: Release the Kraken" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1406671645&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 103: Release the Kraken on SoundCloud](https://soundcloud.com/microbinfie/release-the-kraken)

## In this episode

### What Kraken classifies

Developed in 2013–2014, Kraken assigns sequencing reads to taxonomic groups as specifically as the evidence allows. A read may be assigned to a species, a genus or a broader bacterial group when its sequence is shared across genomes. The guests describe exact k-mer matching as central to its speed, particularly when processing millions or billions of reads rather than searching reads with BLAST.

Comparison tools discussed include MetaPhlAn, megablast and Centrifuge. The guests caution that comparison papers reach different conclusions. They also identify Emu as a useful approach for 16S classification, while stressing that database structure makes 16S a distinct problem.

### Database choices and memory requirements

The standard database described uses complete bacterial, archaeal and viral genomes from NCBI RefSeq, plus the human reference GRCh38. Its size changes as more genomes become available. The guests report that Kraken 1 databases had reached around 300 GB, whereas Kraken2 brought requirements down to roughly 30–50 GB of RAM at the time of recording.

For smaller machines, mini Kraken databases can be built to a specified size, such as 8 or 16 GB. This sacrifices sensitivity: less reference information means more unclassified reads. The guests generally use NCBI RefSeq, while one host uses GTDB taxonomy. Pre-built databases, including those provided through Ben Langmead's lab and available GTDB Kraken databases, let users avoid downloading genomes and building everything themselves.

### The wider Kraken software family

Derek Wood and Steven Salzberg created the original Kraken. Florian Breitweiser developed KrakenUniq to provide additional information, while Ben Langmead and Derek worked together on Kraken2. Jennifer Lu developed Bracken for abundance estimation. Natalia Rincon contributes diversity tools: alpha diversity describes richness within a community, while beta diversity compares communities.

A recent Nature Protocols paper describes metagenomic analysis using the Kraken software suite. Jennifer, Natalia and Martin Steinegger are among its co-authors. The conversation also covers a 2021 paper by Derek and Steven about developing Kraken.

The name is not presented as an acronym. According to the account shared by the guest, Kraken followed the sea-creature theme of Jellyfish, the k-mer counting tool used to build the original databases.

### Reading the outputs

Kraken produces a per-read text file containing the read identifier, classification status, taxonomy ID and a breakdown of k-mer matches. Its summary report gives counts for each taxonomic group, distinguishing reads assigned directly to that group from reads assigned anywhere in its subtree.

The example is a genus with 100 reads assigned directly to it and another 50 assigned to species within it: the subtree total is 150. Those columns answer different questions and should not be confused.

Unclassified reads have no database hits. Reads assigned to the root have matches that do not support a more specific placement. Unclassified reads may warrant further investigation because the standard database described does not cover all possible sources, such as plant or other vertebrate DNA.

### When a few reads matter

There is no universal minimum read count for a meaningful finding. In a brain-sample investigation, roughly a dozen reads assigned to a species absent from the other samples prompted further investigation. The guests report that this proved to be a genuine pathogen. Brain and corneal samples illustrate why filtering out every low-count result can lose useful candidates.

KrakenUniq adds evidence by counting unique k-mers. The guests also describe unique-count reporting in Kraken2, which uses minimisers. Many reads supported by very few distinct k-mers or minimisers can indicate contamination in the sample or database. These counts help validate a result rather than making the read total alone decisive. For broader diversity analysis, the guests highlight Kraken2's speed.

### Nanopore reads and implementation

Kraken was designed with Illumina reads and their error rate in mind. The guests say Nanopore reads can be classified, but higher error rates can reduce classification accuracy. Smaller k-mers might help when building a database for Nanopore data, although they do not offer a settled optimal size. Longer reads also provide more k-mers, creating a trade-off.

Rapidly changing Nanopore chemistries make parameter tuning difficult. Using the same database for Illumina and Nanopore is described as acceptable, provided users recognise possible differences in classification.

Vector sequences are included in the databases and assigned a synthetic-sequences taxonomy ID. Kraken combines Perl for some input processing with C++ for database construction, compact storage, memory management and classification. The guests say newer tools are increasingly written in Python.

## Highlights

- [00:01:41](https://soundcloud.com/microbinfie/release-the-kraken#t=1:41) — What Kraken does: assigning sequencing reads to species, genera or broader taxonomic groups.
- [00:06:33](https://soundcloud.com/microbinfie/release-the-kraken#t=6:33) — Database growth, Kraken2 memory requirements and smaller mini Kraken databases.
- [00:08:53](https://soundcloud.com/microbinfie/release-the-kraken#t=8:53) — NCBI RefSeq, GTDB taxonomy and pre-built Kraken databases.
- [00:09:41](https://soundcloud.com/microbinfie/release-the-kraken#t=9:41) — The developers behind Kraken, KrakenUniq and Kraken2.
- [00:11:27](https://soundcloud.com/microbinfie/release-the-kraken#t=11:27) — Bracken abundance estimation and Natalia Rincon's diversity tools.
- [00:12:46](https://soundcloud.com/microbinfie/release-the-kraken#t=12:46) — The Kraken name, its Jellyfish connection and the paper about its development.
- [00:14:02](https://soundcloud.com/microbinfie/release-the-kraken#t=14:02) — Per-read output and the distinction between direct and subtree counts in Kraken reports.
- [00:16:10](https://soundcloud.com/microbinfie/release-the-kraken#t=16:10) — Why roughly a dozen pathogen reads in a brain sample were worth investigating.
- [00:18:24](https://soundcloud.com/microbinfie/release-the-kraken#t=18:24) — Unique k-mer and minimiser counts as supporting evidence for classifications.
- [00:19:29](https://soundcloud.com/microbinfie/release-the-kraken#t=19:29) — Using Kraken with Nanopore reads and the trade-offs around errors and k-mer size.
- [00:21:35](https://soundcloud.com/microbinfie/release-the-kraken#t=21:35) — The difference between unclassified reads and reads assigned to the root.
- [00:23:33](https://soundcloud.com/microbinfie/release-the-kraken#t=23:33) — Synthetic-sequence taxonomy IDs, followed by Kraken's Perl and C++ implementation.

## In their own words

> So if you're really doing like an in-depth analysis, you'll probably need some external compute resources, but you can potentially run it like on your laptop or with limited resources.
>
> — Natalia Rincon, [00:08:17](https://soundcloud.com/microbinfie/release-the-kraken#t=8:17)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Jennifer Lu** (guest, Johns Hopkins University Center for Computational Biology, Steven Salzberg's lab)
- **Natalia Rincon** (guest, Johns Hopkins University Center for Computational Biology, Steven Salzberg's lab)

Also mentioned: Derek Wood, Steven Salzberg, Florian Breitweiser, Ben Langmead, Martin Steinegger.

## Tools and resources mentioned

Kraken, Kraken 1, Kraken2, KrakenUniq, mini Kraken, Bracken, BLAST, MetaPhlAn, megablast, Centrifuge, Emu, Jellyfish, NCBI RefSeq, GTDB, GRCh38.

## Questions this episode answers

### What is the difference between Kraken and Bracken?

Kraken classifies sequencing reads into taxonomic groups. Bracken, developed by Jennifer Lu, uses Kraken output for abundance estimation.

### How much RAM does Kraken need?

The guests describe Kraken2 databases requiring roughly 30–50 GB of RAM at the time of recording, with requirements changing as reference collections grow. Mini Kraken databases can target sizes such as 8 or 16 GB, at the cost of sensitivity and more unclassified reads.

### How many Kraken reads are enough to identify a pathogen?

The guests do not give a universal threshold. They describe a brain-sample investigation where roughly a dozen reads led to a genuine pathogen finding, and recommend considering sample context and unique k-mer or minimiser support.

### Can Kraken classify Nanopore reads?

Yes, although the guests warn that higher error rates can affect accuracy because Kraken was developed with Illumina reads in mind. They describe using the same database as acceptable with that caveat, while noting that an optimal Nanopore-specific k-mer size had not been established.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We are talking about KRAKEN - the taxonomic classification software and in the hot seat are Dr
Jennifer Lu and Natalia Rincon from Johns Hopkins University Center for Computational Biology.

The MicroBinfie podcast welcomed Dr. Jennifer Lu and Natalia Rincon to discuss Kraken, a
taxonomic classification software. Developed in 2013-2014, Kraken easily identifies and assigns
sequencing reads to a specific species, genus, or general bacteria. Its efficiency in
classifying millions or billions of reads puts it ahead of other classification methods such as
Melan, Mega Blast, and Chime. The tool is known for its ease of use and accuracy.

Following the success of Kraken's metagenomic analysis, Florian Breitweiser developed Kraken
Unique, which provides more information than the standard Kraken. C Another edition to the
Kraken family is Bracken, developed by Jennifer Lu, which estimates abundance, and Nat Rincon
contributes to the newest editions, which analyze diversity metrics.

Kraken's exact camera matching technology identifies reads and classifies taxonomy IDs, with
two outputs: a long text file for every read and a Kraken report that provides a breakdown of
reads for each taxonomy ID. The interpretation of the Kraken report relies on the sample and
its taxon. Even if there are few reads available, taxons can still be meaningful. For
beginners, Kraken simplifies the classification process by providing pre-built databases.

There was an interesting discussion about the origin of the Kraken name. It is derived from a
mythological creature that relied on Jellyfish, a camera counting tool used to build the Kraken
databases. Derek Wood developed the original concept of Kraken.

The hosts found a true pathogen in a sample, which was significant for downstream analysis. The
number of reads in some samples was very few, and some unclassified reads could also be
uninformative or indicate contamination. Being developed for Illumina reads, Kraken's accuracy
in classifying Nanopore reads is likely to be affected due to the higher error rate. The Kraken
database achieves exact matching of k-mers and fits all genome information into a small space.
Tools spawned out of the Kraken world are widely used due to their high accuracy, speed, and
simplicity in the classification of taxonomy.

Kraken provides an additional column in the report to count the number of unique k-mers to
validate the results. The developers worked closely with others to test new Nanopore
chemistries due to the frequent changes in the chemistry that affected the accuracy of the
reads.

Kraken databases contain vector sequence information, and vectors are given their taxonomy ID
as "synthetic sequences." The software mixes Pearl and C++, with Pearl processing inputs and
C++ managing heavy memory stuff by building and compacting sequences and writing bytes. Dr.
Jennifer Lu appreciates the simplicity and accuracy of the classification algorithm, and Nat
Rincon takes pride in being part of the Kraken community.
