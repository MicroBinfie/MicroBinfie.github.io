---
layout: page
title: 'Episode 135: Assembling ATCC bacterial strains'
date: '2024-12-19 00:00:00'
link: https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains
episode: '135'
soundcloud_track: '1933458959'
tags:
- microbinfie
- podcast
description: Andrew Page and Nikhita Puthuveetil discuss ATCC genome assembly, repetitive viral genomes, strain provenance and changing taxonomy.
excerpt: Andrew Page and Nikhita Puthuveetil discuss ATCC genome assembly, repetitive viral genomes, strain provenance and changing taxonomy.
headline: Assembling ATCC genomes and tracing strain provenance
guests:
- Nikhita Puthuveetil
topics:
- genome assembly
- bacterial genomes
- herpesviruses
- long-read sequencing
- genome circularisation
- strain provenance
- metadata
- type strains
- microbial taxonomy
faq:
- q: How does ATCC check its genome assemblies?
  a: Puthuveetil describes monthly reviews using measures including N50 and agreement with expected genome lengths. Difficult assemblies may also require manual investigation and literature searches, because subject-matter expertise is hard to find for every organism.
- q: Why are herpesvirus genomes difficult to assemble?
  a: The herpesviruses discussed have GC-rich genomes and extensive repetitive regions, including at their flanks. ATCC uses long reads to help address short-read limitations, although some genomes still need manual assembly work.
- q: Why might a public ATCC-labelled sequence differ from ATCC's assembly?
  a: The comparison described in the episode found substantial differences in some sequences, including an example involving a mutated strain. Missing strain-history metadata can make it difficult to determine whether a public sequence represents the material a researcher expects.
- q: Can a taxonomic name change look like contamination?
  a: Yes. Puthuveetil explains that a mismatch between a deposited name and a current classification can initially trigger a contamination flag. The team investigates whether the discrepancy reflects contamination or a change in taxonomy.
---

*Assembling ATCC genomes and tracing strain provenance*

Andrew Page talks with Nikhita Puthuveetil, Senior Bioinformatician at the American Type Culture Collection (ATCC), about sequencing and assembling organisms from its collection. They discuss repetitive viral genomes, bacterial genome circularisation, assembly checks and the difficulty of applying one pipeline to many organisms. They also explain why strain provenance and changing taxonomy matter when researchers choose reference sequences.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 135: Assembling ATCC bacterial strains" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1933458959&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 135: Assembling ATCC bacterial strains on SoundCloud](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains)

## In this episode

### Sequencing the ATCC collection

Puthuveetil describes her role as lead bioinformatician for the ATCC Genome Portal, after a little over four years at ATCC. The team is working towards sequencing everything in the collection, beginning with bacteria and extending into viruses, fungi and protists. Its laboratory team generates both short- and long-read sequencing data.

The collection's diversity makes a common assembly workflow difficult: organisms span different genome sizes, GC contents and other extremes. Puthuveetil mentions an ASMNGS poster describing the team's assembly approach, but stresses the practical difficulty of custom-assembling every organism. With much of the easier bacterial work completed, the team has been tackling harder organisms, including extremophiles and larger viruses.

### Repetitive genomes, circularisation and assembly checks

Herpesviruses are a particular challenge in Puthuveetil's work. She describes GC-rich genomes with extensive repetitive regions, including repeats at the flanks. These are difficult to sequence with Illumina, so the team uses long reads to address limitations in the short-read data. Some genomes still require manual assembly work and investigation of what is preventing a satisfactory result.

That investigation includes searching the literature for organism-specific problems and examining how other researchers have curated assemblies. Puthuveetil notes the difficulty of finding subject-matter expertise for every organism. Each month, the team reviews pipeline-produced genomes using measures such as N50 and agreement between assembled and expected genome lengths.

For bacterial assemblies, circularity is the publication gold standard she describes. Unicycler can circularise assemblies automatically. The team has also been examining assembly start sites and the need to reposition sequences rather than simply retaining the starting point produced by an assembler.

### Customer feedback and strain provenance

Genome Portal users provide another route into assembly review. A customer may report that a particular gene appears to be missing, prompting the team to revisit a genome and check how it should look. That feedback is useful when a shared pipeline is being applied across such a varied collection.

Puthuveetil recalls a paper from about two years earlier comparing publicly available sequences labelled as ATCC strains with ATCC's own assemblies. Some differed substantially. One example involved a mutated strain whose status was not apparent to people using the sequence. Her point is not that public sequences are necessarily bad, but that supporting metadata may be insufficient to judge their suitability.

ATCC's internal records help it explain the history behind its published genomes. By contrast, reconstructing provenance from public records can require contacting an old submitter or tracing material held in a laboratory for decades. Page describes following strain histories back to papers that identify a source only by a first name.

### Type strains and changing taxonomy

Page asks about the NCTC sequencing project in the UK. Puthuveetil explains that ATCC and NCTC share some type strains and communicate when changes involving those strains arise. Taxonomy is a recurring issue during publication, and the team uses resources including LPSN to check bacterial names.

A deposited strain may retain a name from the 1990s even though its classification has since changed. ATCC checks deposited identities through classification, but a name mismatch can initially flag a sample as contaminated. Further investigation is needed to distinguish a genuine contamination problem from a taxonomic change.

Page contrasts GTDB's ANI-based taxonomy with the submitter-supplied names in NCBI, drawing on work with NCBI and RefSeq classification databases. Species complexes make these comparisons particularly difficult: classification software may stop at the complex rather than resolve its members. Both speakers emphasise the value of subject-matter expertise and phenotypic evidence when closely related genomes are hard to distinguish.

### Beyond whole-genome sequences

Puthuveetil describes exploratory work on other ways to use ATCC's collection data. The current focus has been whole-genome sequences, but possibilities include RNA-seq using cell-line data and work in proteomics. These are directions the team would like to explore, rather than established services described in the interview.

The question is what additional data customers would find useful. Puthuveetil also values the variety of the work: moving between different organisms means continual learning rather than repeating the same analysis every day.

## Highlights

- [00:00:28](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=0:28) — The ATCC Genome Portal and sequencing bacteria, viruses, fungi and protists
- [00:01:13](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=1:13) — Finding an assembly approach that works across a diverse collection
- [00:02:15](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=2:15) — Repetitive viral regions, long reads and manual assembly investigation
- [00:03:54](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=3:54) — Unicycler and circularity as a bacterial assembly gold standard
- [00:04:16](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=4:16) — Repositioning assembly start sites
- [00:04:34](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=4:34) — Customer reports of missing genes prompt genome checks
- [00:05:38](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=5:38) — Comparing public sequences labelled as ATCC strains with ATCC assemblies
- [00:06:24](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=6:24) — Data provenance and the limits of public sequence metadata
- [00:08:11](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=8:11) — Shared type strains with NCTC and checking changing taxonomic names
- [00:09:45](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=9:45) — Distinguishing contamination flags from taxonomic name changes
- [00:10:22](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=10:22) — Comparing GTDB, NCBI and strain identities in classification databases
- [00:12:01](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=12:01) — Exploring RNA-seq, cell-line data and proteomics

## In their own words

> It's kind of difficult to try to custom assemble every single thing that we have.
>
> — Nikhita Puthuveetil, [00:01:13](https://soundcloud.com/microbinfie/134-assembling-atcc-bacterial-strains#t=1:13)

## Who is talking

- **Andrew Page** (host)
- **Nikhita Puthuveetil** (guest, American Type Culture Collection (ATCC))

## Tools and resources mentioned

ATCC Genome Portal, Unicycler, Illumina, LPSN, NCBI, RefSeq, GTDB, ANI, RNA-seq.

## Questions this episode answers

### How does ATCC check its genome assemblies?

Puthuveetil describes monthly reviews using measures including N50 and agreement with expected genome lengths. Difficult assemblies may also require manual investigation and literature searches, because subject-matter expertise is hard to find for every organism.

### Why are herpesvirus genomes difficult to assemble?

The herpesviruses discussed have GC-rich genomes and extensive repetitive regions, including at their flanks. ATCC uses long reads to help address short-read limitations, although some genomes still need manual assembly work.

### Why might a public ATCC-labelled sequence differ from ATCC's assembly?

The comparison described in the episode found substantial differences in some sequences, including an example involving a mutated strain. Missing strain-history metadata can make it difficult to determine whether a public sequence represents the material a researcher expects.

### Can a taxonomic name change look like contamination?

Yes. Puthuveetil explains that a mismatch between a deposited name and a current classification can initially trigger a contamination flag. The team investigates whether the discrepancy reflects contamination or a change in taxonomy.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie podcast, host Andrew Page is joined by Nikhita Puthuveetil,
Senior Bioinformatician at the American Type Culture Collection (ATCC). They delve into ATCC's
ambitious project of sequencing a vast array of organisms from their renowned collection,
tackling the challenges of assembling complex genomes from bacteria, viruses, fungi, and more.
Discover how Nikhita and her team navigate through genomic roadblocks, leverage cutting-edge
sequencing technologies, and work to ensure accurate data provenance. Whether it's large viral
genomes or evolving taxonomy, this episode offers a deep dive into the fascinating world of
microbial bioinformatics and genomic curation.
