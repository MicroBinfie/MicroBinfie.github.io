---
layout: page
title: 'Episode 99: Stories from the frontlines of bioinformatics'
date: '2023-01-26 00:00:00'
link: https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics
episode: '99'
soundcloud_track: '1405781155'
tags:
- microbinfie
- podcast
description: 'PDFs, Excel errors, COVID lab workflows and bacterial quirks: a live panel on the practical problems of microbial bioinformatics.'
excerpt: 'PDFs, Excel errors, COVID lab workflows and bacterial quirks: a live panel on the practical problems of microbial bioinformatics.'
headline: 'Bioinformatics frontlines: PDFs, metadata and bacterial quirks'
guests:
- Kristy Horan
- Torsten Seemann
- Finlay Maguire
topics:
- microbial bioinformatics
- metadata quality
- spreadsheet errors
- public health genomics
- laboratory workflows
- contamination
- reproducibility
- browser-based bioinformatics
- antimicrobial resistance
- genome diversity
faq:
- q: Why are PDF reports a problem for bioinformatics workflows?
  a: Kristy needed phenotypic metadata for 10,000 samples but could obtain them only from a PDF, adding an extraction step before analysis. Finlay describes both inconsistently formatted susceptibility tables and staff manually retyping printed reports, showing how PDFs can obstruct automated data transfer.
- q: How can Excel damage sample identifiers?
  a: Torsten describes numeric hospital identifiers being converted to scientific notation and rounded until different patients appeared to share the same identifier. He discusses entering identifiers as text, prefixing entries with a single quote, and starting identifier codes with a letter.
- q: What made COVID genomics papers difficult to reproduce?
  a: Andrew encountered missing accession numbers, raw reads, metadata and analysis pipelines when reviewing papers. Finlay also reports sequence-versioning problems in GISAID, where changed sequences could retain the same accession.
- q: Why might resistance analysis need reads rather than an assembly?
  a: Torsten’s Neisseria gonorrhoeae example involves multiple copies of the 23S ribosomal gene, with only some carrying a resistance-associated SNP. He argues that read-level information is needed to estimate that allele fraction; the panel discusses ARIBA but does not establish that it provides the complete answer.
---

*Bioinformatics frontlines: PDFs, metadata and bacterial quirks*

At the 8th Microbial Bioinformatics Hackathon in Bath, Andrew Page talks with Kristy Horan, Torsten Seemann and Finlay Maguire about practical problems behind bioinformatics analyses. Their stories cover extracting data from PDFs, repairing metadata, understanding laboratory workloads and spotting biological assumptions that break software. The discussion connects everyday frustrations with larger questions about reproducibility, accessible tools and antimicrobial resistance analysis.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 99: Stories from the frontlines of bioinformatics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1405781155&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 99: Stories from the frontlines of bioinformatics on SoundCloud](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics)

## In this episode

### When the data arrive as a PDF

Kristy describes an early project validating antimicrobial resistance predictions against phenotypic results. The useful metadata for 10,000 samples were available only in a PDF, requiring extraction into a spreadsheet before comparison with the genomic results. Finlay recalls antibiotic susceptibility breakpoint tables distributed as PDFs with inconsistent formatting, making automated extraction difficult.

Finlay also discovered that a spreadsheet report was not being automatically imported into a medical record system. Instead, staff printed the accompanying PDF and retyped its summary table, using a ruler to follow rows. Increasing the font size reduced data-entry errors. Andrew recalls printing a tree of 2,000 strains several metres long; Torsten remembers an all-against-all Salmonella dot plot assembled from taped-together A4 sheets.

Manual work reaches an extreme in Torsten’s Roche 454 story: someone spent Fridays for six months inspecting reads and quality values in a spreadsheet, entering trimmed sequences in another column. He contrasts that effort with a simple tool taking five minutes; the manually processed reads still had homopolymer errors.

### Dates and identifiers that cannot be trusted

During COVID, Andrew encountered many incompatible date formats, recycled hospital identifiers and identifiers that were not unique across hospitals using the same systems. These problems could associate metadata with the wrong samples. Sometimes the mistakes were only noticed when variants turned up at dates when they could not have existed.

Torsten describes hospital identifiers collapsing into repeated scientific-notation values through Excel conversion and rounding. He discusses treating identifiers as text, using a leading single quote during entry, and putting a letter at the start of identifier codes. Kristy adds an unresolved problem: dates in a tool’s output appeared wrong on only one person’s computer. The panel suggests checking regional settings, language settings and software versions, without establishing a definitive cause.

### The laboratory work behind a sequence file

Finlay recalls eight to ten people working full-time replacing sample-container caps at the Shared Hospital Lab during the pandemic. Such labour was easy to overlook when working downstream with sequence data. He also describes how, beyond a certain number of failures, resequencing an entire plate could be less work than selecting individual samples. Andrew contrasts strict contamination thresholds with academic practice and notes that samples could already have been discarded because freezer space was unavailable.

The panel discusses persistent coronavirus amplicon contamination, including recognisable 400-base fragments. Finlay explicitly distinguishes these sequences from functional viruses. Their broader warning concerns interpreting low-level signals: apparent microbiomes in low-biomass samples, or Malassezia in environmental surveys, need consideration of contamination, including material introduced by people.

### Metadata, accessions and reproducibility

Torsten describes cleaning GISAID metadata containing gender labels in different languages and ages recorded in inconsistent units. Finlay notes that unfamiliar sequencer names could reflect rebadged instruments, including Ion Torrent systems. Andrew raises another interpretive problem: a sample’s listed country may not reveal that the patient was travelling.

Andrew describes reviewing COVID papers with missing accession numbers, raw reads, metadata or analysis pipelines. Finlay reports encountering updated GISAID sequences whose accessions did not change, while Torsten encountered duplicated records; neither presents these observations as a verified account of the database’s current behaviour.

The panel contrasts GISAID’s simple spreadsheet-and-sequence submission model with the linked BioProject, BioSample and SRA records used in more structured repositories. Finlay argues that the additional complexity reflects the complexity of the underlying data, rather than being merely an administrative obstacle.

### Web tools have a substantial audience

Andrew describes Galaxy enabling wet-lab colleagues to perform assemblies and investigate resistance genes and plasmids without relying on his team for every analysis. He also uses NCBI BLAST against nr for straightforward searches. Finlay points to heavy use of the CARD RGI portal, while Torsten highlights the Danish Centre for Genomic Epidemiology’s online tools. Access to command-line environments and high-performance computing is not universal.

The discussion turns to computation inside the browser. Torsten expects client-side bioinformatics to grow, mentioning Wasm, Web Workers and Rust cross-compilation. Finlay adds a practical caution: failures on someone else’s individual computer can be difficult to reproduce and debug.

### Biological assumptions that break analyses

Torsten recounts an in silico PCR tool that missed results because it searched only one DNA strand. He wonders how many similar strand bugs, off-by-one errors and mix-ups between BED and GFF coordinate conventions remain in software. Andrew recalls assuming that bacteria always had one circular chromosome; Torsten’s first bacterial project involved Leptospira with two chromosomes. Finlay describes a Paramecium with separate somatic and germline nuclei, including a somatic nucleus at roughly 800-fold ploidy.

Torsten then uses Neisseria gonorrhoeae to illustrate resistance-associated allele dosage. His example counts 25 copies of the 23S ribosomal gene across multiple genome copies, with resistance depending on how many carry a particular SNP. He argues that estimating the fraction requires returning to reads rather than relying on an assembly. ARIBA is discussed as a possible source of useful alignment information, not a confirmed complete solution. Andrew closes by warning that variation among 16S copies within a bacterium can exceed differences between species, complicating species identification.

## Highlights

- [00:01:19](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=1:19) — Kristy’s phenotypic metadata for 10,000 samples were available only as a PDF.
- [00:03:25](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=3:25) — Finlay discovers that staff print a PDF report and manually retype its results.
- [00:08:59](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=8:59) — Excel converts hospital identifiers into repeated scientific-notation values.
- [00:12:17](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=12:17) — Pandemic laboratory workloads include full-time work replacing sample-container caps.
- [00:14:38](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=14:38) — Finlay clarifies that contaminating COVID amplicons are sequences, not functional viruses.
- [00:17:58](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=17:58) — GISAID metadata cleaning reveals multilingual labels and inconsistent age formats.
- [00:21:59](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=21:59) — Sequence updates without changed accessions create versioning problems.
- [00:26:42](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=26:42) — Torsten discusses browser-based computation using Wasm and Web Workers.
- [00:28:18](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=28:18) — A researcher spends six months manually trimming Roche 454 reads in a spreadsheet.
- [00:30:47](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=30:47) — An in silico PCR tool misses matches because it checks only one DNA strand.
- [00:33:00](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=33:00) — Finlay describes microbial eukaryotes with separate nuclei and unusual genome organisation.
- [00:36:26](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=36:26) — The panel considers estimating a resistance-associated 23S allele fraction from reads.

## In their own words

> So always put a letter at the start of your ID codes to avoid this problem.
>
> — Torsten Seemann, [00:10:34](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=10:34)

> Probably should reassure that these are COVID amplicons, they're not functional viruses, these are just sequences.
>
> — Finlay Maguire, [00:14:38](https://soundcloud.com/microbinfie/99-stories-from-the-frontlines-of-bioinformatics#t=14:38)

## Who is talking

- **Andrew Page** (host)
- **Kristy Horan** (panellist, MDU, Victoria, Australia)
- **Torsten Seemann** (panellist, Doherty Institute, Melbourne, Australia)
- **Finlay Maguire** (panellist, Dalhousie University, Canada; Shared Hospital Lab, Toronto)
- **Lee Katz** (host)

## Tools and resources mentioned

Excel, Artemis, GISAID, NCBI, EBI, BioProject, BioSample, SRA, Galaxy, NCBI BLAST, nr, CARD RGI, UShER, ARIBA, Roche 454, Ion Torrent, Ion Chef.

## Questions this episode answers

### Why are PDF reports a problem for bioinformatics workflows?

Kristy needed phenotypic metadata for 10,000 samples but could obtain them only from a PDF, adding an extraction step before analysis. Finlay describes both inconsistently formatted susceptibility tables and staff manually retyping printed reports, showing how PDFs can obstruct automated data transfer.

### How can Excel damage sample identifiers?

Torsten describes numeric hospital identifiers being converted to scientific notation and rounded until different patients appeared to share the same identifier. He discusses entering identifiers as text, prefixing entries with a single quote, and starting identifier codes with a letter.

### What made COVID genomics papers difficult to reproduce?

Andrew encountered missing accession numbers, raw reads, metadata and analysis pipelines when reviewing papers. Finlay also reports sequence-versioning problems in GISAID, where changed sequences could retain the same accession.

### Why might resistance analysis need reads rather than an assembly?

Torsten’s Neisseria gonorrhoeae example involves multiple copies of the 23S ribosomal gene, with only some carrying a resistance-associated SNP. He argues that read-level information is needed to estimate that allele fraction; the panel discusses ARIBA but does not establish that it provides the complete answer.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

At the 8th Microbial Bioinformatics Hackathon in Bath we talked to a live panel with Kristy
Horan, Torsten Seemann, Finlay Maguire and Andrew Page about bioinformatics from the
frontlines.

We apologise for the poor audio quality, it was recorded in a room with 20 people in the
background so at points it got a bit loud, however we felt you might enjoy the discussion
regardless.
