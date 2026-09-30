---
layout: page
title: 'Episode 10: History of file formats'
date: '2020-01-23 00:00:00'
link: https://soundcloud.com/microbinfie/10-history-of-file-formats
episode: '10'
soundcloud_track: '719278054'
tags:
- microbinfie
- podcast
description: 'Why bioinformatics has so many file formats: FASTQ, BAM, genome annotation, BLAST outputs and the practical headaches of parsing and conversion.'
excerpt: 'Why bioinformatics has so many file formats: FASTQ, BAM, genome annotation, BLAST outputs and the practical headaches of parsing and conversion.'
headline: 'A history of bioinformatics file formats: FASTQ to BLAST'
guests: []
topics:
- bioinformatics file formats
- sequencing data
- data interoperability
- genome annotation
- sequence alignment
- file parsing
- data standards
- microbial bioinformatics
faq:
- q: Why do bioinformaticians convert sequencing data to FASTQ or BAM?
  a: The hosts emphasise the existing tools and pipelines built around these formats. Conversion lets users work with sequencing data without depending entirely on bespoke tools for an instrument’s proprietary output.
- q: Why are genome annotation files difficult to parse consistently?
  a: The episode identifies incompatible format versions, differing sequence separators, coordinate conventions and competing feature hierarchies. Even bacterial annotations can differ over whether they include gene features, CDS features or both.
- q: Why was XML chosen for BLAST output in BRIG?
  a: Nabil-Fareed Alikhan says the documentation at the time recommended XML as an output that would not change between versions. That reduced the risk of having to rewrite BRIG’s parser after a BLAST update.
- q: What is Boulder IO used for in this episode?
  a: The hosts discuss it as Primer3’s straightforward key–value format. They find its equals-sign delimiters convenient for parsing individual records and using the output in pipelines.
---

*A history of bioinformatics file formats: FASTQ to BLAST*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan trace bioinformatics file formats through sequencing, genome annotation and sequence alignment. They compare proprietary outputs with community-supported formats, revisit awkward legacy files and explain why apparently small differences can break analysis pipelines. The recurring question is whether formats serve people reading results, software parsing them, or both.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 10: History of file formats" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/719278054&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 10: History of file formats on SoundCloud](https://soundcloud.com/microbinfie/10-history-of-file-formats)

## In this episode

### Raw sequencing data and common formats

FASTQ is presented as the de facto standard for sharing raw sequencing reads, even when instruments initially produce something proprietary. The hosts recall Sanger chromatograms before discussing PacBio’s use of HDF5 containers and its move to BAM. BAM makes existing tools such as samtools available; methylation information can be retained through additional key–value fields in the SAM representation.

Nanopore’s FAST5 files store raw signals, which base callers and tools such as Nanopolish can interrogate. The conversation also covers the term squiggles for those signals. Direct FASTQ output is welcomed because it lets users move into established pipelines without repeatedly handling instrument-specific formats.

### Legacy sequencers and difficult conversions

The hosts remember working with 454 SFF files and ACE assemblies. ACE could describe assembled contigs and their underlying reads, but extracting that information from its multi-line structure was awkward. Lee Katz recalls asking how to convert between formats before discovering SAM as a more practical alternative.

For Illumina data, the familiar route is BCL to FASTQ using bcl2fastq. Revisiting BCL files is discussed mainly in connection with indexes, barcode bleed-through or an especially important run. The broader point is practical inertia: once good tools exist around a shared format, rebuilding them for another proprietary output is difficult to justify.

### Annotation formats and competing gene models

GenBank and EMBL illustrate different approaches to presenting annotation. EMBL’s two-letter line codes identify record types, while fixed-width lines and wrapping recall older terminals. GFF introduces another compatibility problem: versions are not necessarily interchangeable. The hosts discuss Prokka’s GFF3 output with an appended FASTA sequence and the extra checks needed when other producers handle separators differently.

Content can be harder than syntax. Zero-based versus one-based coordinates cause confusion, while gene, exon, CDS, mRNA and polypeptide features can form different hierarchies. E. coli K-12 is cited as an older complete genome with both gene and CDS features. The discussion distinguishes open reading frames from predicted coding sequences, particularly the difficulty of locating a start, and notes that choosing the wrong translation table can disrupt interpretation.

### BLAST’s many outputs

BLAST offers 19 output formats in the discussion, although the hosts commonly use tabular format 6, formerly M8. Nabil-Fareed Alikhan describes choosing XML while developing BRIG because the documentation then recommended it as stable between versions. They also discuss customisable tabular columns, human-readable output, JSON and SAM.

The move from legacy BLAST to BLAST+ raises a separate reproducibility concern: changed matching behaviour could shift alignment coordinates and complicate comparisons with earlier analyses. There is also a complaint about BLAST’s single-dash options for full words. Despite these frustrations, the hosts praise the NCBI teams for maintaining the software over such a long period.

### Multiple alignments and restrictive names

Andrew Page discusses Gubbins, which accepts a multiple-FASTA alignment, and Roary, which produces multiple sequence alignments. Mauve’s XMFA output provides another example of the formats users must accommodate.

The hosts recall strict ten-character taxon-name limits, relaxed variants and interleaved sequence layouts. PHYLIP remains relevant through programs such as RAxML and QuickTree, with Lee Katz mentioning its use for Mashtree. They trace PHYLIP back to 1980. Andrew favours multiple-FASTA alignments for their straightforward structure: they are simply FASTA files with multiple sequence entries, all aligned to the same length.

### Simple records and evolving standards

Boulder IO, encountered through Primer3, receives a favourable assessment. Its key–value fields and equals-sign record delimiters make it straightforward to parse one entry at a time. Lee notes a 1996 copyright date in the Primer3 manual. PrimerSearch provides a contrasting example of multi-line output that Andrew finds awkward to process.

The conclusion is that formats are shaped by the software that reads and writes them, not just by specifications. GA4GH’s work on formats including VCF, SAM, BAM and CRAM is discussed as an attempt to formalise standards. The hope for fewer universal formats ends with a reference to the xkcd standards comic.

## Highlights

- [00:00:04](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=0:04) — Why converting between file formats occupies so much bioinformatics work
- [00:03:34](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=3:34) — PacBio’s HDF5 files, BAM and the benefits of community-supported tools
- [00:04:48](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=4:48) — SAM key–value fields for methylation data, followed by Nanopore FAST5
- [00:06:53](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=6:53) — Falling back on established standards and memories of 454 SFF and ACE
- [00:12:12](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=12:12) — Illumina BCL output and immediate conversion to FASTQ
- [00:15:13](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=15:13) — Genome annotation in GenBank and EMBL formats
- [00:17:10](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=17:10) — GFF versions and compatibility between annotation parsers
- [00:23:04](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=23:04) — Distinguishing open reading frames from coding sequences
- [00:25:13](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=25:13) — BLAST output as a software-defined family of 19 formats
- [00:28:26](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=28:26) — Choosing XML for BRIG to avoid changing BLAST output conventions
- [00:32:34](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=32:34) — Multiple sequence alignments and their competing file formats
- [00:35:54](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=35:54) — Boulder IO records and their usefulness for parsing and pipelines

## In their own words

> Just like language, which is continuously evolving, if a popular software application introduces a variant of a format, then realistically, it is in common usage and is part of an unofficial format standard.
>
> — Lee Katz, [00:38:11](https://soundcloud.com/microbinfie/10-history-of-file-formats#t=38:11)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

samtools, Nanopolish, bcl2fastq, GenBank, Artemis, Prokka, BLAST, BLAST+, BRIG, Biopython, BioPerl, Gubbins, Roary, Mauve, RAxML, PHYLIP, QuickTree, Mashtree, Primer3, PrimerSearch.

## Questions this episode answers

### Why do bioinformaticians convert sequencing data to FASTQ or BAM?

The hosts emphasise the existing tools and pipelines built around these formats. Conversion lets users work with sequencing data without depending entirely on bespoke tools for an instrument’s proprietary output.

### Why are genome annotation files difficult to parse consistently?

The episode identifies incompatible format versions, differing sequence separators, coordinate conventions and competing feature hierarchies. Even bacterial annotations can differ over whether they include gene features, CDS features or both.

### Why was XML chosen for BLAST output in BRIG?

Nabil-Fareed Alikhan says the documentation at the time recommended XML as an output that would not change between versions. That reduced the risk of having to rewrite BRIG’s parser after a BLAST update.

### What is Boulder IO used for in this episode?

The hosts discuss it as Primer3’s straightforward key–value format. They find its equals-sign delimiters convenient for parsing individual records and using the output in pipelines.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

10 History of file formats by Microbial Bioinformatics
