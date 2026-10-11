---
layout: page
title: 'Episode 68: Bacterial Taxonomy: what is a species, what is a strain? part 2'
date: '2021-12-09 00:00:00'
link: https://soundcloud.com/microbinfie/whats-in-a-name-part-2
episode: '68'
soundcloud_track: '1132643266'
tags:
- microbinfie
- podcast
redirect_from:
- /2021/12/09/68_bacterial_taxonomy_what_i.html
description: How GTDB, ANI and GenomeRxiv classify bacteria, and why species names, strains and lineages matter for diagnostics and public health.
excerpt: How GTDB, ANI and GenomeRxiv classify bacteria, and why species names, strains and lineages matter for diagnostics and public health.
headline: 'Bacterial taxonomy: genomes, strains and public health'
guests:
- Leighton Pritchard
topics:
- bacterial taxonomy
- genome classification
- average nucleotide identity
- species boundaries
- strain terminology
- nomenclature
- public health
- genomic epidemiology
- GenomeRxiv
faq:
- q: What ANI threshold defines a bacterial species?
  a: A guest describes 95% ANI as a common working threshold, with a 94–96% range. The discussion stresses that coverage, the ANI implementation and other biological evidence also matter.
- q: What is the difference between a bacterial strain and an isolate?
  a: The guests offer a working distinction between the physical material obtained from a sample and the cultured material or descendant lineage associated with it. They emphasise that strain and isolate are not used consistently across researchers.
- q: Why can bacterial name changes affect public health?
  a: Diagnostic claims, regulations and legislation may refer to particular organism names. The episode uses the proposed split of mycobacteria into five genera to illustrate how reclassification can create work beyond biological analysis.
- q: What is GenomeRxiv intended to provide?
  a: It is presented as a proposed hierarchical reference framework for locating genomes at different levels of similarity. Multiple names and biological annotations could attach to that framework, helping translate between classification systems.
---

*Bacterial taxonomy: genomes, strains and public health*

Lee Katz, a fellow host and two returning guests, including Leighton Pritchard, examine the practical problems of bacterial taxonomy. They compare genome-based classification with the names used in laboratories, epidemiology and public health, asking how better biological definitions can support rather than disrupt practical decisions.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 68: Bacterial Taxonomy: what is a species, what is a strain? part 2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1132643266&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 68: Bacterial Taxonomy: what is a species, what is a strain? part 2 on SoundCloud](https://soundcloud.com/microbinfie/whats-in-a-name-part-2)

## In this episode

### GTDB and genome-based ranks

The Genome Taxonomy Database, GTDB, provides a working example of classification built around genomes rather than biochemical characteristics. A guest describes constructing a tree from shared core proteins, then normalising taxonomic ranks using positions within that tree. Many existing genera and families fit this framework, suggesting that earlier classifications often captured genuine phylogenetic structure.

Classification and nomenclature are not the same problem. One guest reports that about 80% of GTDB taxa lack valid names and argues that naming rules should not govern which classifications are useful. The panel also questions whether traditional ranks capture natural biological divisions: the formal definition of genus places it between species and family without specifying a universal biological criterion.

### ANI thresholds need coverage and context

Average nucleotide identity, ANI, is presented as a common starting point for comparing a new genome with existing species. One guest gives 95% as a usual species threshold, with a working range of 94–96%, and mentions 98% for subspecies while noting that this is not consistently applied. These are practical conventions, not a complete account of species boundaries.

Coverage matters alongside identity. Two genomes can have high ANI across the regions that align while sharing relatively little aligned sequence overall. A guest discusses group-dependent coverage values around 30–50% for distinguishing same-genus from same-species comparisons, and uses 50% as a conservative rule of thumb. The same guest favours combining evidence, including alignment fraction, biological characteristics and agreement among individual gene trees, rather than relying on one numerical cutoff.

### Strains, isolates, variants and lineages

The guests describe inconsistent usage below species level, distinguishing formal species and subspecies ranks from informal terms such as variant and lineage. Their working distinction treats an isolate as the physical material obtained from a sample, and a strain as the cultured material or descendant lineage associated with it. They explicitly acknowledge that other researchers use these words differently.

Variant is particularly troublesome because it can refer both to a mutation and to an organism carrying changes. COVID-19 illustrates how variants of interest, variants of concern and named lineages acquire different meanings for researchers and the public. One guest prefers a lineage to have a monophyletic grouping plus a relevant biological distinction, such as virulence, host range or environment, rather than merely a list of SNPs.

### When classification meets regulation

The split of mycobacteria into five genera provides a concrete example of taxonomic change with practical consequences. A guest describes challenging that split, noting that GTDB retained one genus. The discussion includes a genus-boundary method combining ANI and alignment fraction for bidirectional best hits, with comparisons against type species. Renaming also raises questions about diagnostic product claims and regulatory documentation.

Lee Katz describes Listeria as having about 92% ANI across four lineages, with lineages one and two more associated with human disease and three and four with animals. His example contrasts numerical species thresholds with the practical aim of keeping disease-causing organisms out of food. A guest extends this concern to plant pathovars and legislation: distinctions important for disease control may not coincide with large genomic differences.

### Choosing comparison and identification tools

Different ANI implementations can place a comparison on opposite sides of a threshold. The guest contrasts BLAST-based ANIB, which fragments genomes into sections of roughly 1,000 nucleotides, with ANIM, which identifies maximal homologous regions. Differences become more important below the high-identity range commonly used for species comparisons.

Digital DNA–DNA hybridisation models laboratory hybridisation measurements, but the guest cautions that the relationship between those measurements and genome identity contains substantial variation. FastANI offers rapid approximation using k-mer approaches and MinHash, while retaining inspectable alignments can be valuable for smaller studies.

For routine work, the question is often simpler: which existing label belongs to this sample? Centrifuge, Mash and MLST are discussed in that context. Reliable identification depends on the quality of the classifications and labels supplied upstream.

### GenomeRxiv as a shared reference

The discussion connects taxonomy with epidemiological clustering, including SNP addresses and cgMLST. Both organise samples into groups whose definitions need to be consistent and useful for decisions.

The proposed GenomeRxiv framework would provide hierarchical identifiers for genome space, compared with map grid references. Increasingly detailed identifiers would locate increasingly similar groups. Multiple nomenclatures and biological annotations could attach to the same reference framework, allowing different definitions to coexist without requiring one naming system to replace every other system.

A technical challenge is spanning the whole range of relatedness. The project aims to combine measures such as AAI for deeper divisions and split k-mer comparisons near outbreak-level resolution. It also aims to support local browser processing rather than requiring exact genome uploads, with privacy, intellectual property and indigenous rights among the considerations.

## Highlights

- [00:03:01](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=3:01) — How GTDB uses core-protein trees and rank normalisation
- [00:07:59](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=7:59) — ANI thresholds for species and subspecies, and their limitations
- [00:09:13](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=9:13) — Why alignment coverage matters alongside ANI
- [00:10:32](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=10:32) — Testing genus boundaries through the mycobacterial split
- [00:13:38](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=13:38) — Working definitions of strain, isolate, variant and lineage
- [00:19:47](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=19:47) — Listeria lineages and the public-health case for pragmatic grouping
- [00:21:59](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=21:59) — Classification, nomenclature and identification meet legislation
- [00:25:41](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=25:41) — Differences between ANI implementations and digital DNA–DNA hybridisation
- [00:28:42](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=28:42) — Practical taxonomy as applying existing labels to samples
- [00:31:00](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=31:00) — Epidemiological clusters, SNP addresses and cgMLST as classification systems
- [00:32:40](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=32:40) — GenomeRxiv and hierarchical identifiers for genome space

## In their own words

> But epidemiology is just a public health version of taxonomy.
>
> — a guest, [00:31:00](https://soundcloud.com/microbinfie/whats-in-a-name-part-2#t=31:00)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Leighton Pritchard** (guest)

## Tools and resources mentioned

GTDB, average nucleotide identity (ANI), average amino acid identity (AAI), FastANI, ANIB, ANIM, BLAST, digital DNA–DNA hybridisation, MinHash, Centrifuge, Mash, MLST, cgMLST, SNP address system, GenomeRxiv, split k-mer comparisons.

## Questions this episode answers

### What ANI threshold defines a bacterial species?

A guest describes 95% ANI as a common working threshold, with a 94–96% range. The discussion stresses that coverage, the ANI implementation and other biological evidence also matter.

### What is the difference between a bacterial strain and an isolate?

The guests offer a working distinction between the physical material obtained from a sample and the cultured material or descendant lineage associated with it. They emphasise that strain and isolate are not used consistently across researchers.

### Why can bacterial name changes affect public health?

Diagnostic claims, regulations and legislation may refer to particular organism names. The episode uses the proposed split of mycobacteria into five genera to illustrate how reclassification can create work beyond biological analysis.

### What is GenomeRxiv intended to provide?

It is presented as a proposed hierarchical reference framework for locating genomes at different levels of similarity. Multiple names and biological annotations could attach to that framework, helping translate between classification systems.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We’re navigating the twisted world of bacterial taxonomy. We have some excellent guides to help us!

See [part 1 here]({% post_url 2021-11-25-whats-in-a-name-part-1 %}).
