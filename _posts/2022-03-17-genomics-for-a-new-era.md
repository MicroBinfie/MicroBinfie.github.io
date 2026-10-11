---
layout: page
title: 'Episode 77: Genomics for a new era'
date: '2022-03-17 00:00:00'
link: https://soundcloud.com/microbinfie/genomics-for-a-new-era
episode: '77'
soundcloud_track: '1131784483'
tags:
- microbinfie
- podcast
description: Zamin Iqbal and Grace Blackwell discuss searchable bacterial assemblies, mobile elements, AMR genes and the biases in public sequencing data.
excerpt: Zamin Iqbal and Grace Blackwell discuss searchable bacterial assemblies, mobile elements, AMR genes and the biases in public sequencing data.
headline: Searching 661,405 bacterial genomes for genes and mobile elements
guests:
- Zamin Iqbal
- Grace Blackwell
topics:
- comparative genomics
- bacterial genome assemblies
- sequence indexing
- mobile genetic elements
- plasmids
- antimicrobial resistance
- sampling bias
- tuberculosis
- protein sequence search
faq:
- q: What bacterial genome dataset is discussed in this episode?
  a: The guests describe a curated collection of 661,405 bacterial assemblies produced with a common assembly and quality-control process. It combines assemblies with sequence-search indexes, genome-distance information and predicted resistance genes.
- q: Can COBS search for an entire plasmid?
  a: Yes. Blackwell describes querying whole plasmids as well as genes and smaller regions; COBS returns samples meeting a specified k-mer matching threshold. It is less effective for divergent sequences because each matching k-mer must be exact.
- q: Do 32–34 resistance genes mean a genome is pan-drug-resistant?
  a: No such conclusion was established. Blackwell stresses that genotype is not phenotype and that some genes provide redundant resistance to the same drug class. Without susceptibility testing she would not call them pan-resistant, although she guesses they are probably close to it.
- q: How representative are the public bacterial genomes in this collection?
  a: 'They are strongly biased: around 90% come from 20 species, and almost 30% are Salmonella enterica. Surveillance priorities, funding, over-represented sequence types and projects targeting resistant isolates also affect the collection.'
- q: Why add protein searches to a bacterial sequence resource?
  a: Iqbal explains that amino acid sequences are more conserved than DNA, allowing searches to reach more evolutionarily divergent relatives. The guests discuss annotation and six-frame translation as possible routes, rather than presenting protein search as an already completed feature.
---

*Searching 661,405 bacterial genomes for genes and mobile elements*

Guests Zamin Iqbal and Grace Blackwell join Andrew Page and Nabil-Fareed Alikhan to discuss a curated, searchable collection of 661,405 bacterial assemblies. They explain how sequence indexes and genome-distance estimates support research into mobile genetic elements and antimicrobial resistance. The conversation also examines sampling bias, the value of continued sequencing and plans for protein-level searches.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 77: Genomics for a new era" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1131784483&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 77: Genomics for a new era on SoundCloud](https://soundcloud.com/microbinfie/genomics-for-a-new-era)

## In this episode

### From archived reads to searchable assemblies

Blackwell and Iqbal discuss their bioRxiv preprint, *Exploring Bacterial Diversity via a Curated and Searchable Snapshot of Archived DNA Sequences*. The project began with questions about the distribution and evolution of mobile genetic elements. The BIGSI demonstration indexed reads available up to the end of 2016, but Blackwell needed assemblies to find out what else each genome contained, such as other plasmid replicons and resistance genes.

After a proposal to assemble everything in early November 2018, Martin Hunt built download and assembly pipelines in about three weeks. Blackwell spent the next six months generating 661,405 bacterial assemblies. Using a uniform assembly and quality-control process helps distinguish biological signals from differences introduced by assemblers. At the time of the discussion, the assemblies were available through an FTP server, with submission to the European Nucleotide Archive (ENA) as third-party assemblies under way.

### What sequence indexes can answer

BIGSI and COBS address a specific question: which samples contain a sequence of interest? COBS splits a query into overlapping k-mers and tests their presence in an index. Users specify the proportion that must match to return a sample. Queries can cover a gene, a region containing a SNP or an entire plasmid. Because individual k-mers require exact matches, the approach works best for closely matching sequences, not distant relatives.

Blackwell reports an index size of 800 GB rather than 80 TB, alongside faster searches. Iqbal explains that COBS accommodates differences in genome size more efficiently than BIGSI’s large rectangular matrix. Searching needs relatively little memory—perhaps one or two gigabytes—but disk speed matters. SSD storage and distributing smaller indexes across servers are possible approaches.

Sequence presence, nearest-genome searches and representative sampling require different indexes. Iqbal argues for an open API through which databases could advertise and answer supported query types, rather than repeatedly aggregating every dataset.

### Genome relationships and mobile elements

The resource also includes sourmash sketches for finding close neighbours of a query genome. The team subsequently used pp-sketchlib to estimate core and accessory genome distances, supporting approximate relationships, trees and identification of closely related clusters or different clades within a species.

Blackwell describes using COBS to retrieve assemblies carrying a small-plasmid replicon across Proteobacteria. The wider discussion covers plasmids moving between species, host ranges that can sometimes cross phyla, and identical plasmid sequences persisting across species and time. Iqbal sees the collection as fertile ground for generating hypotheses about transposons and plasmids: where they occur, how they change and which other genomic features correlate with their presence.

### Resistance genes are not resistance phenotypes

For the resistance analysis, Blackwell ran NCBI’s AMRFinder separately on each genome rather than using COBS. The analysis covered acquired resistance genes, not SNP-mediated resistance. She also warns that some core genes were counted as resistance genes and that predicted genotype does not establish phenotype.

Some E. coli and Klebsiella genomes contained 32–34 predicted antimicrobial resistance genes, without strong signs of contamination on inspection. Multiple genes can target the same drug class: Blackwell gives the example of isolates carrying three different sulfonamide resistance genes. Genera prominent in the WHO priority pathogen list also stood out, while others outside that list could warrant investigation as future problems or resistance-gene reservoirs.

### A large collection with substantial sampling bias

Around 90% of the assemblies came from just 20 bacterial species, and almost 30% were Salmonella enterica. Bias persisted within species: E. coli ST11 and ST131 were prominent examples. Just 50 sequencing projects accounted for half the data. Funding, national surveillance programmes and deliberate selection of resistant isolates all shaped what entered the archives.

The collection nevertheless exposed substantial previously unassembled material. Comparing sample accessions with NCBI Assembly and PATRIC, the team found more than 300,000 assemblies absent from NCBI Assembly before this work. Blackwell argues for greater diversity in sampling, including different environments and geographical locations, and for susceptible isolates to accompany resistance-focused collections.

### Why keep sequencing, and what comes next

Asked whether enough tuberculosis genomes have already been sequenced, Iqbal distinguishes historical research from clinical use and ongoing surveillance. Sequencing can inform treatment, while retained data allow newly recognised resistance mutations to be traced retrospectively. He also describes diagnostic-driven selection: resistant variants missed by a targeted test can gain an advantage when treatment is inappropriate. Broader, systematic sampling would answer different questions from repeatedly sequencing familiar pathogens.

Maintaining the resource remains a challenge. The discussion contrasts roughly 660,000 genomes in Blackwell’s dataset with 1.7 million then in the ENA. Future plans include protein searches, which could detect more evolutionarily divergent matches because amino acid sequences are more conserved than DNA. Options include annotation with Prokka or six-frame translation, each with practical drawbacks. Iqbal also discusses pandora for studying SNP variation alongside gene presence, and reiterates the ambition to make the resource searchable through the web.

## Highlights

- [00:04:38](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=4:38) — Different search questions need different indexes and a shared query API
- [00:06:21](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=6:21) — COBS and the reduction from an 80 TB index to 800 GB
- [00:07:00](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=7:00) — How k-mer queries return samples containing genes or plasmids
- [00:08:59](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=8:59) — K-mer lengths, interrupted index updates and growth of the ENA
- [00:12:14](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=12:14) — Mobile-element research motivates assembling 661,405 bacterial datasets
- [00:14:04](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=14:04) — Why assemblies and uniform processing are valuable for comparative analysis
- [00:16:18](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=16:18) — Additional indexes connect sequence hits to genome relationships
- [00:21:30](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=21:30) — Caveats and findings from the antimicrobial resistance gene analysis
- [00:25:59](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=25:59) — Species, sequence-type and resistance-selection biases in public data
- [00:28:13](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=28:13) — Why tuberculosis sequencing remains useful for treatment and surveillance
- [00:33:40](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=33:40) — Catching up with new genomes and developing protein searches
- [00:35:59](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=35:59) — Alignment-based search ambitions and pandora’s study of genomic variation

## In their own words

> So it depends what you're going to do, but there is a real value in having sort of completely uniform system for assembly and QC for the whole thing.
>
> — Zamin Iqbal, [00:14:04](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=14:04)

> Systematic random sampling from across the world would be super valuable.
>
> — Zamin Iqbal, [00:30:26](https://soundcloud.com/microbinfie/genomics-for-a-new-era#t=30:26)

## Who is talking

- **Zamin Iqbal** (guest, European Bioinformatics Institute)
- **Grace Blackwell** (guest, European Bioinformatics Institute; Wellcome Sanger Institute)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Lee Katz** (host)

Also mentioned: Nick Thomson, Martin Hunt.

## Tools and resources mentioned

BIGSI, COBS, European Nucleotide Archive (ENA), NCBI AMRFinder, sourmash, pp-sketchlib, Mash, NCBI Assembly, PATRIC, Prokka, pandora, BLAST, Velvet, Illumina, Nanopore, PCR, Line probe assays, Six-frame translation.

## Questions this episode answers

### What bacterial genome dataset is discussed in this episode?

The guests describe a curated collection of 661,405 bacterial assemblies produced with a common assembly and quality-control process. It combines assemblies with sequence-search indexes, genome-distance information and predicted resistance genes.

### Can COBS search for an entire plasmid?

Yes. Blackwell describes querying whole plasmids as well as genes and smaller regions; COBS returns samples meeting a specified k-mer matching threshold. It is less effective for divergent sequences because each matching k-mer must be exact.

### Do 32–34 resistance genes mean a genome is pan-drug-resistant?

No such conclusion was established. Blackwell stresses that genotype is not phenotype and that some genes provide redundant resistance to the same drug class. Without susceptibility testing she would not call them pan-resistant, although she guesses they are probably close to it.

### How representative are the public bacterial genomes in this collection?

They are strongly biased: around 90% come from 20 species, and almost 30% are Salmonella enterica. Surveillance priorities, funding, over-represented sequence types and projects targeting resistant isolates also affect the collection.

### Why add protein searches to a bacterial sequence resource?

Iqbal explains that amino acid sequences are more conserved than DNA, allowing searches to reach more evolutionarily divergent relatives. The guests discuss annotation and six-frame translation as possible routes, rather than presenting protein search as an already completed feature.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Today we’re talking about some exciting new developments in the area
of comparative genomics. We are joined by Dr. Zamin Iqbal who is a
Research Group Leader at the European Bioinformatics Institute and Dr.
Grace Blackwell who is jointly at the European Bioinformatics
Institute, in Zam’s group and Nick Thomson’s team at Wellcome Sanger
Institute
