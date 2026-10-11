---
layout: page
title: 'Episode 70: Bacterial Taxonomy:  the grand vista is ahead of us'
date: '2021-12-17 00:00:00'
link: https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us
episode: '70'
soundcloud_track: '1178880226'
tags:
- microbinfie
- podcast
description: Phil Hugenholtz, Iain Sutcliffe and Mark Pallen discuss GTDB, evolutionary ranks, 16S limits and classifying uncultured bacteria.
excerpt: Phil Hugenholtz, Iain Sutcliffe and Mark Pallen discuss GTDB, evolutionary ranks, 16S limits and classifying uncultured bacteria.
headline: 'Bacterial taxonomy with GTDB: genomes, ranks and names'
guests:
- Phil Hugenholtz
- Iain Sutcliffe
- Mark Pallen
topics:
- bacterial taxonomy
- genomic classification
- gtdb
- relative evolutionary divergence
- bacterial nomenclature
- uncultured bacteria
- 16s rrna
- phylogenetics
- species descriptions
faq:
- q: How does GTDB turn genome data into a taxonomy?
  a: Hugenholtz describes building conserved-gene trees from NCBI genomes, then overlaying taxonomic ranks using relative evolutionary divergence. Automation supports the process, but substantial manual curation is also required.
- q: Does relative evolutionary divergence tell us how old a bacterial lineage is?
  a: No. It places nodes on a relative scale between a root of zero and tips of one. Absolute dating would require calibration points, and the relative values should not be compared across different trees.
- q: Why do some Mycoplasma species get new genus names?
  a: Sutcliffe explains that the genus containing the type species Mycoplasma mycoides must retain the name Mycoplasma. Phylogenetic evidence places other species elsewhere, prompting proposals for genera such as Mesomycoplasma and Metamycoplasma.
- q: Why might 16S and GTDB classifications disagree?
  a: The panel discusses PCR-generated chimeras, reduced support in very large 16S trees and limitations when applying 16S at higher taxonomic ranks. Both Hugenholtz and Sutcliffe nevertheless defend 16S as an important and successful step in bacterial classification.
---

*Bacterial taxonomy with GTDB: genomes, ranks and names*

Professors Phil Hugenholtz, Iain Sutcliffe and Mark Pallen join hosts Andrew Page and Nabil-Fareed Alikhan for the second part of a bacterial taxonomy discussion. They examine how GTDB turns genome comparisons into a taxonomic framework, why evolutionary rates complicate classification, and why changing bacterial names attracts resistance. The conversation connects these questions to uncultured diversity and the practical challenge of describing hundreds of species together.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 70: Bacterial Taxonomy:  the grand vista is ahead of us" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1178880226&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 70: Bacterial Taxonomy:  the grand vista is ahead of us on SoundCloud](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us)

## In this episode

### How GTDB builds a taxonomy

Phil Hugenholtz describes GTDB as a taxonomy built from genomic comparisons. It takes genomes from NCBI’s Genome Assembly Archive and constructs trees using concatenated single-copy conserved genes, 120 in this case. He stresses that trees from this type of comparison are, for the most part, broadly comparable.

Scale imposes compromises. GTDB uses FastTree because it can handle very large trees; Hugenholtz acknowledges that this heuristic approach is imperfect but considers it adequate for the task. Much of the work then involves overlaying a hierarchical taxonomy on the tree.

This is not simply an automated classification pipeline. Hugenholtz says more than half the team’s time has gone into the taxonomic overlay. At recording, release 207 involved adding 17,000 species, with manual curation already occupying two months.

### Relative divergence, not an absolute clock

GTDB uses relative evolutionary divergence to make ranks more comparable within a tree. The root is assigned zero, the tips one, and internal values are calculated by linear interpolation. Hugenholtz gives approximately 0.85–0.95 as the range in which genera generally fall.

These values are not dates and should not be compared between different trees. Dating would require calibration points, which are difficult to establish for bacteria. GTDB also allows corridors around ranks rather than imposing one rigid boundary. This leaves room for taxonomic opinion: either splitting or lumping Mycobacterium can fit the framework, whereas treating it as a phylum would not.

### Fast evolution and disputed names

Pallen recalls Carl Woese’s review *Bacterial Evolution* while discussing Mycoplasma: organisms once treated as primitive and deeply separate were instead placed within the Firmicutes. Hugenholtz uses this example to explain why flat sequence-identity thresholds can mislead when a group evolves unusually quickly.

The candidate phyla radiation, or CPR, provides another example. Hugenholtz describes evidence supporting a derived, fast-evolving group and a sister relationship to Chloroflexota. Within GTDB’s relative-divergence framework, it is treated as one phylum rather than as many as 100.

Sutcliffe separates these evolutionary questions from nomenclatural rules. The genus containing the type species Mycoplasma mycoides must retain the name Mycoplasma. Reclassifications introducing names such as Mesomycoplasma and Metamycoplasma have met resistance, despite following the naming rules. His broader argument is that classifications and names must be able to respond to new knowledge.

### Uncultured diversity and alternative approaches

Hugenholtz traces his interest in classification to curating Greengenes and encountering large numbers of unclassified environmental sequences in NCBI taxonomy. He sees a major GTDB contribution in providing a complete classification for uncultured taxa. NCBI taxonomy draws on multiple information sources and, unlike GTDB, does not use a rank-normalised approach.

Pallen celebrates a framework that can extend beyond the roughly 2% of bacteria described in the discussion as culturable. Hugenholtz is more cautious, calling GTDB a prototype rather than a final answer. Alternatives mentioned include PhyloPhlAn for phylogenetic analysis and TYGS, the Type Strain Genome Server associated with DSMZ and LPSN.

### What 16S gets right—and misses

A host reports conflicting high-level classifications after comparing long-read metagenomic data against an unnamed 16S database and GTDB. Hugenholtz rejects the suggestion that 16S was a wasted effort, but explains how PCR-generated chimeras can distort trees. He recalls estimating that at least 4% of 16S sequences were chimeric to some degree, with some chimeras recurring reproducibly.

He also describes reduced bootstrap support in very large 16S trees. Sutcliffe regards 16S as a major historical advance, while noting problems at higher taxonomic ranks. Average nucleotide identity and digital DNA–DNA hybridisation now provide useful species-level metrics; grouping species into genera and families remains an important focus of genomic classification.

### Naming hundreds of species together

The panel challenges the one-colony, one-species, one-paper model. Pallen describes a chicken gut microbiome study that named more than 600 species in one paper. The team initially prepared names and protologues in a spreadsheet, then moved them into the manuscript because of concerns about acceptance as supplementary information. That added more than 100 pages and over $1,000 in publication costs.

Sutcliffe argues for separating classification from exhaustive characterisation. A genome-based framework can identify interesting groups for later investigation—for example, examining biosynthetic gene clusters in taxa that might produce useful metabolites. Pallen argues along similar lines that the code requires only a description and a circumscription and does not prescribe methods, so robust phylogenetic placement and clear circumscription should not be held up by reviewers who insist on particular methods.

## Highlights

- [00:01:28](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=1:28) — Hugenholtz explains GTDB’s genome sources, conserved-gene trees and manual curation.
- [00:05:05](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=5:05) — Relative evolutionary divergence assigns ranks without dating the tree.
- [00:07:47](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=7:47) — Mycoplasma illustrates how molecular evidence overturned older classifications.
- [00:08:48](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=8:48) — Fast evolutionary rates complicate sequence thresholds for Mycoplasma and CPR.
- [00:10:42](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=10:42) — Sutcliffe explains type species and resistance to Mycoplasma renaming.
- [00:15:25](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=15:25) — Pallen argues that a broad genomic framework for bacterial taxonomy is worth celebrating.
- [00:16:46](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=16:46) — Hugenholtz cautions that GTDB should be considered a prototype.
- [00:17:35](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=17:35) — NCBI taxonomy and GTDB differ in rank normalisation and uncultured-taxon coverage.
- [00:19:35](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=19:35) — PCR chimeras and large-tree limitations complicate 16S-based classification.
- [00:22:59](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=22:59) — TYGS provides another approach as taxonomy moves from phenotype to genotype.
- [00:24:25](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=24:25) — Pallen describes naming more than 600 chicken gut species in one paper.
- [00:25:20](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=25:20) — Sutcliffe distinguishes genome-based classification from detailed downstream characterisation.

## In their own words

> the grand vista is ahead of us now and this is something to celebrate
>
> — Mark Pallen, [00:15:25](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=15:25)

> let's consider it more a prototype to show that it's possible
>
> — Phil Hugenholtz, [00:16:46](https://soundcloud.com/microbinfie/bacterial-taxonomy-the-grand-vista-is-ahead-of-us#t=16:46)

## Who is talking

- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Lee Katz** (host)
- **Phil Hugenholtz** (guest)
- **Iain Sutcliffe** (guest)
- **Mark Pallen** (guest)

Also mentioned: Carl Woese.

## Tools and resources mentioned

GTDB, NCBI Genome Assembly Archive, NCBI Taxonomy, FastTree, Greengenes, PhyloPhlAn, TYGS, LPSN, Relative evolutionary divergence, 16S rRNA analysis, PCR, Average nucleotide identity, Digital DNA–DNA hybridisation, DNA–DNA hybridisation.

## Questions this episode answers

### How does GTDB turn genome data into a taxonomy?

Hugenholtz describes building conserved-gene trees from NCBI genomes, then overlaying taxonomic ranks using relative evolutionary divergence. Automation supports the process, but substantial manual curation is also required.

### Does relative evolutionary divergence tell us how old a bacterial lineage is?

No. It places nodes on a relative scale between a root of zero and tips of one. Absolute dating would require calibration points, and the relative values should not be compared across different trees.

### Why do some Mycoplasma species get new genus names?

Sutcliffe explains that the genus containing the type species Mycoplasma mycoides must retain the name Mycoplasma. Phylogenetic evidence places other species elsewhere, prompting proposals for genera such as Mesomycoplasma and Metamycoplasma.

### Why might 16S and GTDB classifications disagree?

The panel discusses PCR-generated chimeras, reduced support in very large 16S trees and limitations when applying 16S at higher taxonomic ranks. Both Hugenholtz and Sutcliffe nevertheless defend 16S as an important and successful step in bacterial classification.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We continue our discussion on bacterial taxonomy, this time looking at
how genomics has changed taxonomy with: Professor Phil Hugenholtz,
Professor Iain Sutcliffe and Professor Mark Pallen.

Selective
bibliography: https://github.com/MicroBinfie/MicroBinfie.github.io/bl
ob/45db8eb57d732176449073065dbdacc88a288fe9/assets/Taxonomy*Selective*
bibliography.pdf
