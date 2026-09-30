---
layout: page
title: 'Episode 74: SEPIA With Henk - Soup Or Salad  Yes!'
date: '2022-02-03 00:00:00'
link: https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes
episode: '74'
soundcloud_track: '1128163150'
tags:
- microbinfie
- podcast
description: Henk discusses SEPIA, a Rust read classifier, with batch processing, flexible taxonomies and applications in food safety metagenomics.
excerpt: Henk discusses SEPIA, a Rust read classifier, with batch processing, flexible taxonomies and applications in food safety metagenomics.
headline: 'SEPIA with Henk: read classification, Rust and food safety'
guests:
- Henk
topics:
- metagenomics
- read classification
- taxonomy
- food safety
- rust
- k-mers
- nanopore reads
- classifier benchmarking
faq:
- q: How does SEPIA differ from Kraken2?
  a: Henk describes SEPIA as borrowing Kraken2’s compact hash-table ideas while adding features he wanted, including batch processing, alternative taxonomy handling and a hit-ratio measure. Its taxon summaries do not follow Kraken’s hierarchical report structure.
- q: Can SEPIA run on a laptop?
  a: Memory requirements depend on the reference database. The GTDB example discussed contains about 50,000 references and requires a 98 GB index in RAM, which Henk says would not run on his laptop.
- q: How can SEPIA help assess false-positive species assignments?
  a: Its average k-mer similarity can expose weak matches. Henk is also working on using distinct k-mer estimates to tell broad genome coverage apart from repeated matches to a small shared region. He openly acknowledges that shared genes and reference bias remain problems.
- q: Can SEPIA classify Oxford Nanopore reads?
  a: Henk says he uses it for Nanopore reads and experiments with smaller k-mers, including a size of 21 with a Calamari database. Similarity values are affected by read errors and should not be compared directly with Illumina values.
---

*SEPIA with Henk: read classification, Rust and food safety*

Lee Katz and his co-hosts speak with Henk, an assistant professor at the University of Georgia, about SEPIA, his Rust-based read classifier. They discuss taxonomy choices, database loading, misleading species assignments and food safety applications. The conversation distinguishes working features from experiments, proposed benchmarks and development plans at the time of recording.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 74: SEPIA With Henk - Soup Or Salad  Yes!" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1128163150&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 74: SEPIA With Henk - Soup Or Salad  Yes! on SoundCloud](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes)

## In this episode

### Why build another read classifier?

Henk presents SEPIA as a way to add features he wanted when using other read classifiers. A taxonomist by training, he is interested in how choosing GTDB rather than NCBI taxonomy affects classification, especially for poorly known organisms. SEPIA borrows compact hash-table ideas and classification principles from Kraken2, while also exploring a data structure using a perfect hash function.

He chose Rust for performance-critical work, describing performance comparable to C and C++. SEPIA’s name acknowledges Kraken’s cephalopod theme and the rusty colour of pigment made from sepia ink.

### Batch processing and memory requirements

Repeated database loading was a practical frustration behind SEPIA’s batch mode. Rather than load the index separately for every sample, users can supply a tab-delimited file containing sample names and sequence data. Henk describes loading an 80–90 GB index in about a minute, followed by roughly ten seconds per sample for classification and summaries. These are examples from his use, not a formal benchmark.

For a GTDB R202 database containing about 50,000 bacterial and archaeal references, he gives an index size of 98 GB, all loaded into RAM. That example would not fit on his laptop. He also discusses using 31-base k-mers with 21-base minimisers to reduce database size.

### Shared genes can look like whole organisms

SEPIA does not automatically solve the problem of shared mobile elements or genes producing misleading species assignments. Henk favours representative or centroid strains over indexing every available genome from heavily sequenced populations.

He gives an example of 100,000 reads assigned to Salmonella: if they represent only about 2,000 distinct k-mers rather than the four or five million expected across a genome, the signal may come from a shared gene rather than the organism itself. He says he is currently working on this approach.

SEPIA also reports a hit ratio: an average k-mer similarity estimate based on minimisers. Henk says it correlates well with average nucleotide identity, or ANI. A very low similarity, such as 0.01, can help identify noise caused by a classifier assigning reads to an overly specific taxon.

### Food safety applications and sample limitations

Henk describes projects using metagenomics to identify animal intrusion into farmland and estimate how long ago droppings were deposited. Source attribution becomes harder as the original microbiota changes: typical obligate anaerobes disappear within the first few days, while some Escherichia persist longer.

Other work maps retail-environment microbiomes and examines relationships with Listeria and Salmonella. Henk explains that Listeria can occur in small numbers in unenriched sequencing datasets, but recovering cultures commonly involves selective enrichment and takes at least a couple of days, rather than simply an overnight culture.

He also uses SEPIA to scan 16S amplicon datasets quickly and select reads of interest, describing an amplicon database as fast enough that batch mode is unnecessary.

### Taxonomy handling and readable results

SEPIA stores taxonomy as directed acyclic graphs and uses set operations to find common ancestors. Full lineage strings distinguish identical genus names occurring in different lineages, including across plant, bacterial and zoological taxonomies. The software can flag genus names appearing in multiple lineages for inspection.

Outputs include human-readable per-read classifications and taxon summaries, rather than Kraken’s hierarchical report. Summaries contain read counts and average k-mer or minimiser similarity. Optional HyperLogLog calculations estimate distinct k-mers and support a coverage-like measure based on total hits divided by that estimate.

A separate plus file records similarity distributions, not just averages. Henk created this output to explore whether machine learning could separate noise from genuine hits.

### Nanopore reads and benchmarks still to try

Henk also uses SEPIA with Oxford Nanopore reads. Their average k-mer similarity values are affected by sequencing errors and are not directly comparable with Illumina results. He describes useful results with 21-base k-mers and a smaller Calamari reference database, while warning that excessively short k-mers match too broadly. A host raises minimap2’s error models as something worth investigating, not as an existing SEPIA feature.

Henk warns that the HyperLogLog implementation is slow at the time of recording. The hosts suggest testing with Zymo mock communities and challenging classifier datasets. They identify CAMI and discuss a 2017 Nature Methods paper alongside a McIntyre paper from 2017 in Genome Biology. These are proposed tests, not evidence that SEPIA has outperformed other classifiers.

## Highlights

- [00:00:00](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=0:00) — Lee introduces the software deep dive and Henk’s food safety bioinformatics background
- [00:01:34](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=1:34) — Why SEPIA exists: taxonomy choices and compact classification data structures
- [00:04:57](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=4:57) — Choosing Rust for performance-critical read classification
- [00:07:39](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=7:39) — Batch mode avoids repeatedly loading a large reference index
- [00:09:24](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=9:24) — Representative strains, shared-gene matches and the hit ratio
- [00:12:46](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=12:46) — Animal droppings, retail microbiomes and rapid screening of 16S datasets
- [00:18:59](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=18:59) — A roughly 50,000-reference GTDB database requires a 98 GB index in RAM
- [00:25:23](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=25:23) — Representing taxonomy with directed acyclic graphs
- [00:26:29](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=26:29) — Taxon summaries differ from Kraken’s hierarchical reporting
- [00:32:11](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=32:11) — Trying SEPIA, the slow HyperLogLog implementation and Nanopore classification
- [00:34:28](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=34:28) — CAMI and published datasets suggested for classifier benchmarking
- [00:36:24](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=36:24) — The SEPIA name connects Kraken, cephalopods and Rust

## In their own words

> Just give the software a run and see what you can do with it.
>
> — Henk, [00:32:11](https://soundcloud.com/microbinfie/sepia-with-henk-soup-or-salad-yes#t=32:11)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Henk** (guest, University of Georgia)

## Tools and resources mentioned

SEPIA, Kraken2, Rust, GTDB, NCBI taxonomy, HyperLogLog, Average nucleotide identity (ANI), Calamari, minimap2.

## Questions this episode answers

### How does SEPIA differ from Kraken2?

Henk describes SEPIA as borrowing Kraken2’s compact hash-table ideas while adding features he wanted, including batch processing, alternative taxonomy handling and a hit-ratio measure. Its taxon summaries do not follow Kraken’s hierarchical report structure.

### Can SEPIA run on a laptop?

Memory requirements depend on the reference database. The GTDB example discussed contains about 50,000 references and requires a 98 GB index in RAM, which Henk says would not run on his laptop.

### How can SEPIA help assess false-positive species assignments?

Its average k-mer similarity can expose weak matches. Henk is also working on using distinct k-mer estimates to tell broad genome coverage apart from repeated matches to a small shared region. He openly acknowledges that shared genes and reference bias remain problems.

### Can SEPIA classify Oxford Nanopore reads?

Henk says he uses it for Nanopore reads and experiments with smaller k-mers, including a size of 21 with a Calamari database. Similarity values are affected by read errors and should not be compared directly with Illumina values.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

74 SEPIA With Henk - Soup Or Salad  Yes! by Microbial Bioinformatics
