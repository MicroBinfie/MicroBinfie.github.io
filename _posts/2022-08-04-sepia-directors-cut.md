---
layout: page
title: 'Episode 88: Sepia directors cut'
date: '2022-08-04 00:00:00'
link: https://soundcloud.com/microbinfie/sepia-directors-cut
episode: '88'
soundcloud_track: '1144720606'
tags:
- microbinfie
- podcast
description: Henk den Bakker explains Sepia, a Rust read classifier, covering taxonomy, batch processing, memory use and food-safety metagenomics.
excerpt: Henk den Bakker explains Sepia, a Rust read classifier, covering taxonomy, batch processing, memory use and food-safety metagenomics.
headline: 'Sepia directors’ cut: taxonomy, Rust and read classification'
guests:
- Henk den Bakker
topics:
- read classification
- microbial taxonomy
- metagenomics
- food safety
- k-mers
- reference databases
- rust
- nanopore reads
- benchmarking
faq:
- q: How does Sepia differ from Kraken2?
  a: Sepia uses Kraken2-inspired data structures and classification principles, but den Bakker emphasises flexible taxonomy, batch processing that avoids repeated index loading, and similarity information for interpreting assignments. Its summary is a direct taxon-level report rather than Kraken’s hierarchical report.
- q: Can Sepia run on a laptop?
  a: That depends on the database and parameters. The episode’s GTDB r202 example requires a 98 GB index in RAM, so it is not presented as laptop-friendly; smaller reference collections and different k-mer and minimizer settings reduce the requirement.
- q: How can Sepia help distinguish a shared gene from a whole organism?
  a: The discussion combines average k-mer similarity with evidence about how many distinct k-mers support a taxon. Many assigned reads concentrated in a small set of k-mers can indicate shared sequence rather than genome-wide evidence, although den Bakker does not claim this eliminates false calls.
- q: Does Sepia work with Oxford Nanopore reads?
  a: Den Bakker reports using it for Nanopore read classification and describes useful results with 21-base k-mers in a smaller Kalamari database. He cautions that overly short k-mers match too broadly and that similarity values from noisy reads are not directly comparable with Illumina results.
---

*Sepia directors’ cut: taxonomy, Rust and read classification*

Henk den Bakker joins Lee Katz, Andrew Page and Nabil-Fareed Alikhan for an extended discussion of Sepia, his read classifier written in Rust. They explore how taxonomy, reference databases and k-mer similarity affect microbial read assignments, alongside batch processing and memory use. Food-safety metagenomics provides the practical context, including the problems posed by shared genes, unfamiliar organisms and noisy long reads.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 88: Sepia directors cut" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1144720606&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 88: Sepia directors cut on SoundCloud](https://soundcloud.com/microbinfie/sepia-directors-cut)

## In this episode

### A classifier built around taxonomy

Den Bakker describes Sepia as another read classifier, built to provide features he wanted as both a taxonomist and a regular user of classification tools. It borrows Kraken2’s compact hash table and some classification principles, while providing a way to experiment with alternatives such as GTDB and NCBI taxonomy. A particular interest is how taxonomy changes assignments for organisms that are not well represented or understood.

Sepia stores taxonomy as directed acyclic graphs and uses set operations to find common ancestors. It also checks for inconsistencies, such as a genus name appearing in different lineages. Den Bakker explains that using whole taxonomy strings avoids collisions when combining bacterial, botanical and zoological names. The name Sepia is itself a tribute to Kraken: another cephalopod, with an ink pigment whose colour also recalls Rust.

### Rust, compact indexes and memory

Rust is den Bakker’s choice for performance-critical code; Python remains his usual scripting language. He describes Rust as capable of C- or C++-level performance. Sepia stores sequence-derived information and associated taxon identifiers in unsigned 32-bit integers, and he has experimented with combining compact hash tables with perfect hash functions. He also discusses extending the current 41-base k-mer limit towards 64 bases, without yet knowing the performance consequences.

Memory requirements depend on the reference collection and parameters. For GTDB release r202, den Bakker describes approximately 50,000 bacterial and archaeal references and a 98 GB Sepia index that must be loaded into RAM—not a laptop-sized example. He also reports smaller indexes using a 31-base k-mer and a 21-base minimizer, making parameter choice important when considering memory use and classification accuracy.

### Batch processing and readable results

A central motivation for Sepia was avoiding repeated database loading. Den Bakker describes Kraken2 runs where loading the index takes longer than classifying the reads. Sepia’s batch mode loads the database once, then processes samples supplied through a file containing sequence-data locations and sample names. His example is roughly a minute to load an 80–90 GB index, followed by about ten seconds per sample; these are examples from the discussion, not universal timings.

Sepia produces a summary and per-read classifications. The summary is a direct taxon-level report rather than Kraken’s hierarchical report, giving read counts and average k-mer or minimizer similarity. Optional HyperLogLog output estimates distinct k-mers and supports a coverage-like calculation. A Python script generates Krona input, while a supplementary output records similarity distributions rather than only averages.

### Shared genes and misleading taxonomic calls

The panel asks how a classifier handles sequences shared between species, including mobile genetic elements and antimicrobial-resistance genes. Den Bakker acknowledges that Sepia can suffer the same problems as other classifiers. He favours representative reference strains over indexing every available genome, reducing the influence of heavily sampled populations without claiming to solve shared-sequence ambiguity.

His example is 100,000 reads assigned to Salmonella that cover only about 2,000 distinct k-mers, rather than the four or five million expected across a genome. That concentration could indicate a shared gene rather than the organism itself. Sepia’s hit ratio estimates average k-mer similarity, which he reports correlates well with ANI. Very low similarity, such as 0.01, can help identify noisy assignments. A no-hits category is also available, but the discussion stresses that unfamiliar sequences can still produce misleadingly specific classifications.

### Food safety and environmental samples

Applications include using metagenomics to identify animals entering farmland and estimate how long ago they deposited faeces. Den Bakker describes changes in the native microbiota of animal droppings: the typical obligate anaerobes, which he considers the most indicative, disappear within the first few days, so what can be seen depends on how long ago the contamination occurred. Escherichia signals were among the longest-lasting in the dataset he discusses.

Other projects map retail-environment microbiomes and examine their relationship to Listeria and Salmonella occurrence. Sepia can quickly scan 16S datasets for reads of interest, especially with an amplicon database. The conversation also explains why recovering Listeria often involves culture enrichment. This selectively favours organisms of interest and takes at least a couple of days from a soil sample to Listeria cultures, rather than simply an overnight incubation.

### Long reads, benchmarks and unfinished work

Den Bakker also uses Sepia with Oxford Nanopore reads, adjusting parameters for noisy sequences. With a smaller Kalamari database, he reports useful results using 21-base k-mers, while warning that excessively short k-mers match too broadly. Average similarity values from Nanopore data are not directly comparable with those from Illumina data. Lee Katz describes Kalamari as a curated reference-genome collection, mostly bacterial and foodborne, distributed as accessions, download scripts and database-building documentation.

Suggested benchmarks include Zymo mock communities, CAMI from Nature Methods in 2017, and a 2017 Genome Biology comparison by McIntyre and colleagues. These are proposed tests, not reported Sepia results. At recording, the HyperLogLog implementation was described as slow, a read-filtering function was planned, documentation was being expanded and a paper remained unwritten. Den Bakker credits the Rust clap crate with helping him write good command-line help.

## Highlights

- [00:01:42](https://soundcloud.com/microbinfie/sepia-directors-cut#t=1:42) — Why Sepia exists: taxonomy choices, Kraken2 principles and compact data structures
- [00:06:17](https://soundcloud.com/microbinfie/sepia-directors-cut#t=6:17) — Choosing Rust for performance-critical classification while retaining Python for scripting
- [00:09:22](https://soundcloud.com/microbinfie/sepia-directors-cut#t=9:22) — Database-loading overhead as a motivation for batch processing
- [00:11:18](https://soundcloud.com/microbinfie/sepia-directors-cut#t=11:18) — Representative reference strains, shared genes and k-mer evidence for taxonomic calls
- [00:14:55](https://soundcloud.com/microbinfie/sepia-directors-cut#t=14:55) — Animal droppings, farmland intrusion and retail-environment microbiomes
- [00:22:24](https://soundcloud.com/microbinfie/sepia-directors-cut#t=22:24) — The GTDB r202 example: approximately 50,000 references and a 98 GB index
- [00:34:45](https://soundcloud.com/microbinfie/sepia-directors-cut#t=34:45) — Storing taxonomy as directed acyclic graphs and finding common ancestors
- [00:36:15](https://soundcloud.com/microbinfie/sepia-directors-cut#t=36:15) — Sepia’s summary output and its departure from Kraken’s hierarchical report
- [00:40:00](https://soundcloud.com/microbinfie/sepia-directors-cut#t=40:00) — Low-similarity assignments, no-hits results and the danger of false classifications
- [00:42:35](https://soundcloud.com/microbinfie/sepia-directors-cut#t=42:35) — HyperLogLog overhead, followed by parameter tuning for Oxford Nanopore reads
- [00:45:17](https://soundcloud.com/microbinfie/sepia-directors-cut#t=45:17) — CAMI and other benchmark datasets for testing read classifiers
- [00:51:23](https://soundcloud.com/microbinfie/sepia-directors-cut#t=51:23) — The Sepia name: a cephalopod tribute to Kraken and a reference to Rust

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Henk den Bakker** (guest, University of Georgia)

## Tools and resources mentioned

Sepia, Kraken2, GTDB, NCBI taxonomy, Rust, Python, Perl, HyperLogLog, ANI, Krona, Kalamari, CAMI, clap, Redis, Bracken, UniFrac, Plasmidtron, minimap2, Oxford Nanopore, Illumina, Zymo mock communities.

## Questions this episode answers

### How does Sepia differ from Kraken2?

Sepia uses Kraken2-inspired data structures and classification principles, but den Bakker emphasises flexible taxonomy, batch processing that avoids repeated index loading, and similarity information for interpreting assignments. Its summary is a direct taxon-level report rather than Kraken’s hierarchical report.

### Can Sepia run on a laptop?

That depends on the database and parameters. The episode’s GTDB r202 example requires a 98 GB index in RAM, so it is not presented as laptop-friendly; smaller reference collections and different k-mer and minimizer settings reduce the requirement.

### How can Sepia help distinguish a shared gene from a whole organism?

The discussion combines average k-mer similarity with evidence about how many distinct k-mers support a taxon. Many assigned reads concentrated in a small set of k-mers can indicate shared sequence rather than genome-wide evidence, although den Bakker does not claim this eliminates false calls.

### Does Sepia work with Oxford Nanopore reads?

Den Bakker reports using it for Nanopore read classification and describes useful results with 21-base k-mers in a smaller Kalamari database. He cautions that overly short k-mers match too broadly and that similarity values from noisy reads are not directly comparable with Illumina results.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

This is an extended directors cut of our chat with Dr Henk den Bakker about Sepia. Its a summer
holiday bonus.

Some URLs Get Sepia here: <https://github.com/hcdenbakker/sepia> Some information on the food
safety informatics group at UGA: <https://www.denglab.site/> Rust: <https://www.rust-lang.org/>
Kalamari: <https://github.com/lskatz/kalamari> CAMI:
<https://www.nature.com/articles/nmeth.4458>
