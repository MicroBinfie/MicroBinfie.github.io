---
layout: page
title: 'Episode 83: A short journey into mobile genetic elements'
date: '2022-05-26 00:00:00'
link: https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements
episode: '83'
soundcloud_track: '1233380629'
tags:
- microbinfie
- podcast
description: Why bacterial mobile genetic elements are hard to assemble and annotate, with examples from Vibrio, E. coli, pertussis and Shigella.
excerpt: Why bacterial mobile genetic elements are hard to assemble and annotate, with examples from Vibrio, E. coli, pertussis and Shigella.
headline: 'Mobile genetic elements: short reads, phages and plasmids'
guests: []
topics:
- mobile genetic elements
- plasmids
- prophages
- insertion sequences
- short-read assembly
- genome annotation
- crispr typing
- genomic surveillance
faq:
- q: Are mobile genetic elements the same as the accessory genome?
  a: No. The hosts explain that the two overlap, but a sequence being part of the accessory genome does not necessarily mean it can move.
- q: Can PlasmidFinder distinguish a standalone plasmid from an integrated element?
  a: A replicon signal alone does not settle that question. The discussion highlights the difficulty of distinguishing genuine integration from misassembly when working with short reads.
- q: How should I start investigating mobile genetic elements from FASTQ files?
  a: The suggested workflow is to assemble the reads, produce a first-pass annotation with Prokka and inspect the genome in Artemis. Read-mapping coverage, GC-content changes and element-specific tools can then help identify regions worth examining.
- q: Which tools are discussed for finding prophages?
  a: PHAST, PHASTER, Phage Finder and PhiSpy are mentioned. The hosts describe their outputs as heuristic predictions that should be checked against the annotated genome rather than accepted without inspection.
- q: What can I try when a phage-associated gene has no useful nr match?
  a: Suggestions include PSI-BLAST, InterProScan, Pfam, more curated phage or plasmid databases, and structural predictions. The hosts caution that these can still fail, leaving experimental microbiology as the route to establishing function.
---

*Mobile genetic elements: short reads, phages and plasmids*

Andrew Page asks Lee Katz and Nabil-Fareed Alikhan what mobile genetic elements are and how to investigate them in bacterial genomes. They discuss repetitive sequences, plasmid typing, prophage detection and CRISPRs, explaining why an assembly or annotation rarely provides the whole answer. The conversation ends early when Lee loses power, with a follow-up discussion promised.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 83: A short journey into mobile genetic elements" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1233380629&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 83: A short journey into mobile genetic elements on SoundCloud](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements)

## In this episode

### What counts as a mobile genetic element?

The discussion covers bacteriophages that integrate as prophages, transposons, plasmids, genomic islands, integrative conjugative elements and integrons. These categories are not tidy: an element can look partly like a phage or plasmid without fitting neatly into either group. Some prophages lack their own complete excision machinery and borrow it from elsewhere.

Mobile genetic elements overlap with the accessory genome, but an accessory gene is not necessarily mobile. The hosts also distinguish recognising phage-like genes from establishing that an element is complete and able to move. Tail and sheath proteins are useful clues, but not every prophage-like region contains the expected set of genes.

### Why short reads leave difficult questions

PlasmidFinder and Inc typing provide evidence about plasmid replicons, but a replicon signal does not necessarily establish whether the sequence belongs to a standalone plasmid. If it appears within a chromosome, the hosts discuss both misassembly and a genuine integrated element, such as an ICE, as possible explanations.

Repeated sequences create another obstacle. One example involves a Vibrio strain with three phages arranged back to back; PacBio becoming available helped resolve the region after about a year of study. Some E. coli genomes are described as having 10–20 prophage or prophage-like repetitive elements, each potentially breaking an assembly. Repeat-rich pertussis and Shigella genomes provide further examples of difficult assemblies and poor N50 values.

### CRISPR defence and organism-dependent typing

CRISPRs are introduced as a bacterial acquired immune system: associated genes act alongside sequences used to recognise foreign DNA and target it for destruction. Conserved associated genes and the distinctive repeat-and-spacer structure make CRISPR regions recognisable. Detection tools mentioned include CRISPRFinder, PILER-CR and CRISPRdb.

Their usefulness for typing depends on the organism. In some Salmonella serovars, particularly Typhimurium, spacer patterns can follow established lineages. Mycobacterium tuberculosis spoligotyping is described as examining the CRISPR panel. However, the hosts caution against assuming that CRISPR patterns always track chromosome evolution, and say CRISPR typing has been less reliable than SNPs or MLST for genomic surveillance.

### From reads to an inspectable genome

Starting with FASTQ files, the proposed first step is assembly, whether the reads are short or long. Gene order and neighbourhood matter: finding a single transposon-related feature without genomic context tells the analyst much less. A first-pass Prokka annotation provides something to inspect in Artemis, followed by more specialised annotation for the elements that appear to be present.

Mapping reads back to the assembly adds another clue. A large coverage spike can indicate a collapsed repeat. A change in GC content relative to the chromosome may also flag an unusual region; many phages are described as AT-rich. These signals guide investigation rather than replacing visual inspection.

### Prophage predictions need checking

For an initial prophage search, the hosts suggest PHAST or PHASTER. These assess candidate regions using a collection of criteria, including structural proteins and sequence-composition signals. Phage Finder and PhiSpy are also mentioned as options that may return different results.

The important limitation is that these are heuristic predictions, not complete answers. The suggested next step is to return to Artemis and check whether the proposed regions make biological sense. More broadly, the hosts argue that mobile genetic elements remain difficult enough that no single tool should be trusted to settle every case.

### When annotation finds no useful match

An annotated phage tail gene may sit beside genes for which an NCBI nr search gives no useful result. Suggested next steps include more sensitive searches with PSI-BLAST, domain analysis with InterProScan or Pfam, searches against more curated phage or plasmid databases, and structural predictions. The discussion also stresses searching in amino-acid space rather than relying only on nucleotide comparisons.

None of these approaches is guaranteed to identify a function. Some sequences remain unknown despite repeated computational searches, and resolving their biology may require collaborators in the wet lab. The episode closes before the discussion can continue because Lee has lost power.

## Highlights

- [00:01:23](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=1:23) — Defining mobile genetic elements and explaining why their categories overlap.
- [00:04:34](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=4:34) — What PlasmidFinder and replicon typing can tell an analyst.
- [00:05:55](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=5:55) — Short-read limitations and a Vibrio strain with three tandem phages.
- [00:08:01](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=8:01) — CRISPR defence, repeat-and-spacer structures and detection tools.
- [00:09:37](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=9:37) — CRISPR typing in Salmonella and Mycobacterium tuberculosis.
- [00:11:17](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=11:17) — Assembly, gene context and first-pass annotation with Prokka and Artemis.
- [00:12:18](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=12:18) — Mapping reads back to an assembly to spot collapsed repeats through coverage.
- [00:13:46](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=13:46) — Using prophage prediction tools and checking their heuristic results.
- [00:15:10](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=15:10) — Options when nr searches fail, including sensitive alignments and wet-lab work.
- [00:16:56](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=16:56) — Lee's power cut brings the discussion to an early close.

## In their own words

> As long as there's some sort of mechanism for it to transfer, then it's a mobile genetic element.
>
> — one of the hosts, [00:01:23](https://soundcloud.com/microbinfie/a-short-journey-into-mobile-genetic-elements#t=1:23)

## Who is talking

- **Andrew Page** (host)
- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

PlasmidFinder, Inc typing, PacBio, CRISPRFinder, PILER-CR, CRISPRdb, CRISPR typing, Spoligotyping, MLST, Prokka, Artemis, PHAST, PHASTER, Phage Finder, PhiSpy, NCBI nr, PSI-BLAST, InterProScan, Pfam.

## Questions this episode answers

### Are mobile genetic elements the same as the accessory genome?

No. The hosts explain that the two overlap, but a sequence being part of the accessory genome does not necessarily mean it can move.

### Can PlasmidFinder distinguish a standalone plasmid from an integrated element?

A replicon signal alone does not settle that question. The discussion highlights the difficulty of distinguishing genuine integration from misassembly when working with short reads.

### How should I start investigating mobile genetic elements from FASTQ files?

The suggested workflow is to assemble the reads, produce a first-pass annotation with Prokka and inspect the genome in Artemis. Read-mapping coverage, GC-content changes and element-specific tools can then help identify regions worth examining.

### Which tools are discussed for finding prophages?

PHAST, PHASTER, Phage Finder and PhiSpy are mentioned. The hosts describe their outputs as heuristic predictions that should be checked against the annotated genome rather than accepted without inspection.

### What can I try when a phage-associated gene has no useful nr match?

Suggestions include PSI-BLAST, InterProScan, Pfam, more curated phage or plasmid databases, and structural predictions. The hosts caution that these can still fail, leaving experimental microbiology as the route to establishing function.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We discuss mobile genetic elements in bacteria and find, its really
hard. Its just a short chat as Lee lost power, but we will be back
with a part 2 sometime soon.
