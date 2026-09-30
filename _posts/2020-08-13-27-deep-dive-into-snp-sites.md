---
layout: page
title: 'Episode 27: SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments'
date: '2020-08-13 00:00:00'
link: https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites
episode: '27'
soundcloud_track: '844112809'
tags:
- microbinfie
- podcast
description: Andrew Page explains how SNP-sites extracts variants from alignments, why it reads files twice, and how testing and packaging keep it useful.
excerpt: Andrew Page explains how SNP-sites extracts variants from alignments, why it reads files twice, and how testing and packaging keep it useful.
headline: 'SNP-sites: extracting variants from multi-FASTA alignments'
guests: []
topics:
- snp extraction
- multi-fasta alignments
- memory efficiency
- vcf output
- phylogenetics
- distance matrices
- software packaging
- software testing
- feature creep
faq:
- q: What input does SNP-sites need?
  a: It takes a multi-FASTA alignment and extracts variable positions. Page discusses whole-genome alignments, gene alignments and reference-aligned consensus sequences, and confirms that gzipped input is supported.
- q: How does SNP-sites keep memory use low?
  a: It reads the input file twice rather than loading the whole alignment into memory. Page describes thousands of samples using only tens of megabytes of memory, with the trade-off that input cannot simply be streamed through.
- q: Can SNP-sites output be used to build phylogenetic trees?
  a: Page describes using SNP-only alignments to make tree building quicker and obtain an initial view of clustering. He cautions that information is lost and branch lengths will not be as good. The hosts also discuss neighbour joining from pairwise distances produced by snp-dists.
- q: How can SNP-sites be installed?
  a: The episode mentions Debian Med, Homebrew, Conda and Docker. Page also describes a conventional source-build process using Automake and Autoconf, while Katz, who installed it just before the chat, calls it one of the easiest things he has ever run.
---

*SNP-sites: extracting variants from multi-FASTA alignments*

Andrew Page discusses SNP-sites with fellow hosts Lee Katz and Nabil-Fareed Alikhan in a software deep dive. He explains how the tool grew out of Gubbins, extracts variable positions from multi-FASTA alignments, and keeps memory use low by reading the input twice. The conversation also covers compressed inputs, VCF output, tree-building caveats, software packaging and the value of keeping a tool focused.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 27: SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/844112809&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 27: SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments on SoundCloud](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites)

## In this episode

### One task, spun out of Gubbins

SNP-sites takes a multi-FASTA alignment and extracts the positions that vary between sequences. Page describes inputs ranging from reference-aligned consensus sequences to whole-genome and single-gene alignments. The aim is to retain the differences rather than carry every unchanged position into subsequent analysis, such as tree building or investigating recombination.

The tool began as part of Gubbins. During development, Simon R. Harris asked Page to turn the SNP-extraction component into a separate application. Page copied the relevant C code into a new project, with work starting around 2013. He says he still uses it once or twice a month because it performs that narrow task without fuss.

### Low memory use and the cost of writing C

Page contrasts SNP-sites with approaches that load an entire alignment into memory. With tens of thousands of genomes, that can exceed the capacity of a laptop or desktop. SNP-sites instead reads the file twice, trading away streaming input to keep memory overhead low. He describes processing thousands of samples using only tens of megabytes of memory.

The implementation uses C with manually managed memory. Page spent considerable time keeping it fast and finding memory leaks with Valgrind. However, Ben Taylor demonstrated an alternative by producing a fast Cython implementation in a few hours. Page says that approach might have saved him weeks or months, although it had some quirks. The lesson is that developer time matters alongside runtime efficiency.

### Packaging, tests and compressed input

Page emphasises that the C code has tests and uses Automake and Autoconf for a conventional build process. He describes the extra packaging work as worthwhile because it makes the software portable across Linux and Unix-type systems and supports straightforward compilation and installation.

That preparation also helped SNP-sites enter Debian Med. Page values the continuing maintenance available through that route, and mentions availability through Homebrew, Conda and Docker. Katz reports installing it immediately before the conversation and finding it particularly easy to run. Another practical feature is support for gzipped multi-FASTA alignments: users can supply compressed files without first creating an uncompressed copy.

### VCF output, quick trees and distance matrices

Page frequently uses SNP-sites to create VCF files containing SNP coordinates and a matrix of variant calls across samples. The discussion also covers PHYLIP format and feeding SNP-only alignments into tree-building software such as RAxML. Reducing a large alignment to variable sites can make an otherwise slow analysis much quicker; Page uses a one-gigabyte input as an example of a file that may cause difficulties for tree-building programs.

He cautions that removing information has consequences: branch lengths will not be as good, even if the result gives a quick view of clustering. Torsten Seemann's snp-dists is discussed as a companion tool that produces pairwise distance matrices from SNP-sites output. One of the hosts notes that such a matrix could be used for neighbour joining.

### A publishable building block, not an expanding pipeline

The accompanying paper, *SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments*, appeared in Microbial Genomics 2(4) in 2016. Page initially treated publication as an experiment in whether such a small tool could justify a paper. The team carried out performance comparisons and wrote it up; at the time of recording, he says it was the journal's highest-cited paper.

The hosts connect its usefulness to the Unix approach of combining small programs. Page has seen SNP-sites adopted in many pipelines through papers citing it. They also discuss feature creep: apparently minor requests can greatly expand a codebase. Page does not anticipate major additions to SNP-sites, beyond possible output formats and bug fixes.

## Highlights

- [00:01:14](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=1:14) — What SNP-sites extracts from a multi-FASTA alignment
- [00:02:05](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=2:05) — How the SNP-extraction component became a separate tool from Gubbins
- [00:03:20](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=3:20) — Reading the input twice to keep memory use low
- [00:04:45](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=4:45) — Why Page chose C for efficient implementation
- [00:07:33](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=7:33) — Reading gzipped alignments directly
- [00:08:17](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=8:17) — Creating VCF files with SNP coordinates and variant calls
- [00:09:41](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=9:41) — Testing whether a small, focused tool could become a journal paper
- [00:10:19](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=10:19) — Minimising memory use and tracking leaks with Valgrind
- [00:10:55](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=10:55) — The Unix approach of combining small tools into pipelines
- [00:11:52](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=11:52) — Keeping future SNP-sites development limited in scope
- [00:12:45](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=12:45) — Using a pairwise distance matrix for neighbour joining

## In their own words

> It's not trying to do every possible different thing.
>
> — Andrew Page, [00:02:16](https://soundcloud.com/microbinfie/27-deep-dive-into-snp-sites#t=2:16)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Ben Taylor, Simon R. Harris, Torsten Seemann, Nick Waters.

## Tools and resources mentioned

SNP-sites, Gubbins, Cython, Valgrind, Automake, Autoconf, Debian Med, Homebrew, Conda, Docker, RAxML, snp-dists, neighbour joining.

## Questions this episode answers

### What input does SNP-sites need?

It takes a multi-FASTA alignment and extracts variable positions. Page discusses whole-genome alignments, gene alignments and reference-aligned consensus sequences, and confirms that gzipped input is supported.

### How does SNP-sites keep memory use low?

It reads the input file twice rather than loading the whole alignment into memory. Page describes thousands of samples using only tens of megabytes of memory, with the trade-off that input cannot simply be streamed through.

### Can SNP-sites output be used to build phylogenetic trees?

Page describes using SNP-only alignments to make tree building quicker and obtain an initial view of clustering. He cautions that information is lost and branch lengths will not be as good. The hosts also discuss neighbour joining from pairwise distances produced by snp-dists.

### How can SNP-sites be installed?

The episode mentions Debian Med, Homebrew, Conda and Docker. Page also describes a conventional source-build process using Automake and Autoconf, while Katz, who installed it just before the chat, calls it one of the easiest things he has ever run.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat to the author of SNP-sites, bioinformatics software for
extracting SNPs from a multi-FASTA alignment. Sounds simple but behind
all of our software are quirky details that never make it into the
final paper.  Software: https://github.com/sanger-pathogens/snp-sites
Paper: https://www.microbiologyresearch.org/content/journal/mgen/10.10
99/mgen.0.000056   "SNP-sites: rapid efficient extraction of SNPs from
multi-FASTA alignments", Andrew J. Page, Ben Taylor, Aidan J. Delaney,
Jorge Soares, Torsten Seemann, Jacqueline A. Keane, Simon R. Harris,
Microbial Genomics 2(4), (2016)
