---
layout: page
title: 'Episode 22: Assembly after party'
date: '2020-06-25 00:00:00'
link: https://soundcloud.com/microbinfie/22-assembly-after-party
episode: '22'
soundcloud_track: '770093671'
tags:
- microbinfie
- podcast
description: Checking microbial genome assemblies with read mapping, polishing, QUAST, socru and genome viewers—and why N50 alone is not enough.
excerpt: Checking microbial genome assemblies with read mapping, polishing, QUAST, socru and genome viewers—and why N50 alone is not enough.
headline: 'After assembly: polishing, quality checks and genome viewers'
guests: []
topics:
- microbial genome assembly
- scaffolding
- gap filling
- assembly polishing
- assembly quality control
- n50
- contamination detection
- genome completeness
- chromosome structure
- genome visualisation
faq:
- q: Is a high N50 enough to trust a bacterial genome assembly?
  a: No. The hosts explain that aggressive scaffolding or concatenating contigs can inflate N50 without making the sequence correct. They recommend checking read mapping, total assembly length, taxonomic assignments, marker genes and chromosome structure as well.
- q: How many rounds of Pilon polishing do the hosts use?
  a: Lee describes running Pilon four times through a wrapper and checking whether further differences remain. He does not present four rounds as a guarantee of correctness, and the discussion notes that polishing can reinforce errors.
- q: What does socru check in a complete bacterial chromosome?
  a: It checks the order and orientation of ribosomal operons against a species-specific reference framework. The output can distinguish known patterns, novel but biologically plausible arrangements, and improbable arrangements that may indicate a misassembly.
- q: Why can a Shigella assembly have a low N50?
  a: The hosts attribute the fragmentation of short-read Shigella assemblies to numerous insertion sequence elements. They give N50 values of 30,000–40,000 as examples and stress that quality expectations must be tailored to the organism.
---

*After assembly: polishing, quality checks and genome viewers*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss what happens after a microbial genome assembly is produced: scaffolding, gap filling, polishing and quality control. They explain why contiguity statistics need to be considered alongside read mapping, contamination, completeness and chromosome structure. Examples from Salmonella, E. coli and Shigella show why a useful quality threshold depends on the organism.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 22: Assembly after party" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/770093671&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 22: Assembly after party on SoundCloud](https://soundcloud.com/microbinfie/22-assembly-after-party)

## In this episode

### Map the reads back and inspect the joins

A basic sanity check is to map the input reads back against the assembly. Nabil-Fareed Alikhan recommends looking for unexpected mapping patterns, large insertions or deletions, and concentrations of sequence differences. Because these are the reads used to build the assembly, substantial disagreement deserves investigation.

The hosts distinguish contig construction from scaffolding. Contigs join overlapping sequence; scaffolding uses additional evidence, such as paired-end or mate-pair information, to connect them. Unsequenced intervals are represented by Ns. Gap filling returns to the reads to recover sequence within those intervals, sometimes extending from overhanging reads. Lee recalls using IMAGE 2 to combine scaffolding and gap filling.

### Polishing is useful, but repetition is not a guarantee

Lee describes a wrapper around Pilon that runs four rounds of polishing and checks for no, or few, new differences. He presents four rounds as a community convention rather than a proven stopping rule. The hosts question whether additional rounds, or combinations of different polishers, keep improving an assembly: polishing can also reinforce errors.

Nanopolish is discussed as working with Nanopore’s raw signal, or “squiggle space”, rather than just called bases. One host recalls its runtime for an E. coli genome dropping from about 4,000 hours to a handful of hours as the software developed. The broader recommendation is to cross-check with a different source of sequence information, such as Illumina reads alongside Nanopore data.

### Use N50 as one measurement, not a verdict

QUAST provides assembly statistics through command-line and graphical interfaces, with a web portal also mentioned. The hosts compare it with simpler reporting scripts, including run assembly metrics and assembly-stats, which quickly report values such as N50 and the longest contig.

The N50 discussion works towards a length-based definition: sort the contigs by length, calculate half the total assembled sequence, and identify the contig spanning that cumulative position. Its length is the N50. However, aggressive scaffolding—or simply concatenating contigs—can inflate this number without producing a correct genome. The hosts therefore favour several complementary checks rather than treating a high N50 as proof of quality.

### Check contamination, completeness and chromosome structure

Classifying contigs with Kraken or Centrifuge can quickly expose unexpected sequence. A Salmonella assembly containing contigs classified as Klebsiella needs investigation, although plasmids complicate interpretation. Another suggestion is to assemble reads left over after mapping, to see what the main assembly missed.

Single-copy marker genes provide another check: extra copies can indicate a problem. BUSCO and CheckM are discussed for marker-based assessment and estimated completeness, including applications to metagenomic and isolate assemblies.

For complete bacterial chromosomes, socru examines the order and orientation of ribosomal operons. Salmonella normally has seven in the example given; finding one or 15 would raise questions. The tool distinguishes known arrangements, novel but biologically plausible arrangements, and improbable patterns that may indicate misassembly. Its database is described as covering 433 species.

### Set expectations for the organism

Total assembly length can be more informative than N50. An unusually small or large Salmonella assembly should prompt investigation, but Lee notes that large plasmids can bring some examples to 5.5–6 megabases. The discussion also mentions extreme E. coli records in RefSeq, from 150 kilobases to 10 megabases, as reasons to scrutinise deposited genomes.

Shigella illustrates why fragmentation thresholds cannot simply transfer between closely related organisms. Short-read assemblies can have N50 values of 30,000–40,000 because of numerous insertion sequence elements. The hosts point to ranges distributed through PulseNet and GenomeTrakr, and average values in EnteroBase documentation for Salmonella, E. coli, Yersinia and Clostridioides, as practical reference points.

### Look at the reads as well as the finished sequence

The visualisation discussion starts with Consed, particularly its ability to show which contig contains a read’s mate. Gap5 is remembered as a powerful finishing tool, though one that benefits from hands-on instruction. Artemis remains useful for inspecting read pileups, annotations, insert-size patterns and GC content. A practical tip is to turn off stop-codon display when repeatedly zooming or preparing figures.

Different viewers answer different questions. IGV makes it convenient to display many tracks together, while Bandage shows connections in the assembly graph and can help investigate why a long-read assembly failed to circularise. Hawkeye and Tablet also feature in the discussion. For a lightweight terminal view, the hosts recommend SAMtools’ ASCII read-pileup viewer, navigated with arrow keys.

## Highlights

- [00:01:39](https://soundcloud.com/microbinfie/22-assembly-after-party#t=1:39) — Mapping input reads back to the assembly as a sanity check
- [00:03:55](https://soundcloud.com/microbinfie/22-assembly-after-party#t=3:55) — Gap filling: recovering missing sequence between scaffolded contigs
- [00:05:41](https://soundcloud.com/microbinfie/22-assembly-after-party#t=5:41) — Lee’s IMAGE 2 workflow, followed by repeated Pilon polishing
- [00:07:26](https://soundcloud.com/microbinfie/22-assembly-after-party#t=7:26) — Questions about combining polishers and an introduction to Nanopolish
- [00:09:59](https://soundcloud.com/microbinfie/22-assembly-after-party#t=9:59) — Using QUAST to report and explore assembly metrics
- [00:12:08](https://soundcloud.com/microbinfie/22-assembly-after-party#t=12:08) — An attempt to explain N50 in a sentence
- [00:14:40](https://soundcloud.com/microbinfie/22-assembly-after-party#t=14:40) — Taxonomic classification of contigs and single-copy marker checks
- [00:17:05](https://soundcloud.com/microbinfie/22-assembly-after-party#t=17:05) — Using socru to assess ribosomal operon arrangements in complete chromosomes
- [00:18:07](https://soundcloud.com/microbinfie/22-assembly-after-party#t=18:07) — Why total assembly length can be more useful than N50
- [00:21:13](https://soundcloud.com/microbinfie/22-assembly-after-party#t=21:13) — Why short-read Shigella assemblies are more fragmented than E. coli assemblies
- [00:23:26](https://soundcloud.com/microbinfie/22-assembly-after-party#t=23:26) — Eyeballing assemblies, beginning with Consed
- [00:28:33](https://soundcloud.com/microbinfie/22-assembly-after-party#t=28:33) — Comparing genome viewers, including IGV, Tablet and Bandage

## In their own words

> Like, the N50 is actually quite low down on my list these days to check.
>
> — Nabil-Fareed Alikhan, [00:16:44](https://soundcloud.com/microbinfie/22-assembly-after-party#t=16:44)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

IMAGE 2, Pilon, Nanopolish, QUAST, SPAdes, run assembly metrics, assembly-stats, Kraken, Centrifuge, BUSCO, CheckM, socru, RefSeq, EnteroBase, Consed, Hawkeye, AMOS, Gap4, Gap5, Artemis, IGV, JBrowse, Biodalliance, Tablet, Bandage, SAMtools, Chado, GMOD, WebApollo.

## Questions this episode answers

### Is a high N50 enough to trust a bacterial genome assembly?

No. The hosts explain that aggressive scaffolding or concatenating contigs can inflate N50 without making the sequence correct. They recommend checking read mapping, total assembly length, taxonomic assignments, marker genes and chromosome structure as well.

### How many rounds of Pilon polishing do the hosts use?

Lee describes running Pilon four times through a wrapper and checking whether further differences remain. He does not present four rounds as a guarantee of correctness, and the discussion notes that polishing can reinforce errors.

### What does socru check in a complete bacterial chromosome?

It checks the order and orientation of ribosomal operons against a species-specific reference framework. The output can distinguish known patterns, novel but biologically plausible arrangements, and improbable arrangements that may indicate a misassembly.

### Why can a Shigella assembly have a low N50?

The hosts attribute the fragmentation of short-read Shigella assemblies to numerous insertion sequence elements. They give N50 values of 30,000–40,000 as examples and stress that quality expectations must be tailored to the organism.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

When you get an assembly the fun doesnt stop there. You then have to
fix it up and see how good it is. In this episode we discuss
scaffolding, gapfilling, polishing, assembly metrics, quality control,
genome structure, and visualisation tools.  Tools and papers
mentioned: https://github.com/quadram-institute-bioscience/socru https
://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0004446
