---
layout: page
title: 'Episode 29: Mashtree software deep dive'
date: '2020-09-10 00:00:00'
link: https://soundcloud.com/microbinfie/mashtree-software-deep-dive
episode: '29'
soundcloud_track: '877321804'
tags:
- microbinfie
- podcast
description: Lee Katz explains how Mashtree builds rapid genome-comparison trees from Mash sketches, and why they are a first pass rather than a phylogeny.
excerpt: Lee Katz explains how Mashtree builds rapid genome-comparison trees from Mash sketches, and why they are a first pass rather than a phylogeny.
headline: 'Mashtree: fast genome comparison without a full phylogeny'
guests: []
topics:
- whole-genome comparison
- genome sketching
- minhash
- bacterial genomics
- outbreak analysis
- population structure
- software packaging
- open-source software
faq:
- q: Does Mashtree need assembled genomes?
  a: No. Lee explains that it can compare raw sequencing reads as well as assemblies, avoiding assembly when a rapid preliminary comparison is needed.
- q: Does Mashtree produce a phylogeny?
  a: Lee explicitly describes its output as a tree or dendrogram, not a phylogeny. It clusters genomes by similarity without establishing ancestral states, and he recommends more detailed analysis for a final publication.
- q: Why did Lee choose 10,000 k-mers for Mashtree?
  a: The Mash paper showed a good correlation with ANI when retaining a thousand k-mers. Lee chose 10,000 because the comparison remained fast and he wanted to preserve higher resolution.
- q: Had Mashtree been tested for MinION streaming data?
  a: At the time of the episode, Lee said he had not done much testing with MinION data. He wanted separate tests because its error profile differs.
- q: How is Mashtree installed and documented?
  a: Lee says Mashtree can be installed through CPAN and is packaged using MakeMaker. Its documentation consists of a Markdown README and additional Markdown files stored with the repository.
---

*Mashtree: fast genome comparison without a full phylogeny*

Lee Katz takes the hot seat to explain Mashtree, his software for rapidly comparing whole-genome sequence files. The hosts discuss how Mash sketches become a neighbour-joining tree, why that tree should not be treated as a phylogeny, and where it helps with outbreak analysis and population structure. They also cover slower prototypes, Perl multithreading, packaging, documentation and publishing in the Journal of Open Source Software.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 29: Mashtree software deep dive" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/877321804&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 29: Mashtree software deep dive on SoundCloud](https://soundcloud.com/microbinfie/mashtree-software-deep-dive)

## In this episode

### A quick comparison before assembly

Mashtree grew out of repeated requests for rapid genome comparisons during outbreak analyses and investigations of population structure. Lee describes receiving FASTQ files of 50 or 200 megabytes and wanting an answer before spending around an hour per genome on assembly and characterisation with methods such as whole-genome MLST. He had been thinking about the problem between roughly 2014 and 2016.

The initial solution was practical: run Mash on the genomes, compare them, build a neighbour-joining tree, and turn those steps into a pipeline. Mashtree can work with raw reads or assemblies. Lee contrasts a preliminary tree taking about a minute on a laptop with an approximately 90-minute high-quality SNP-based analysis.

### From k-mers to a compact sketch

Mash uses MinHash, an algorithm the discussion traces back to detecting duplicate web pages for the AltaVista search engine. Lee explains the sketching process as converting k-mers into integers, sorting them numerically and retaining a small subset. In his introductory example, keeping the first thousand integers can reduce a 50-megabyte FASTQ file to an approximately eight-kilobyte sketch.

Mashtree compares these sketches using Mash dist and builds a neighbour-joining tree from the resulting distances. Lee initially tried UPGMA, but found neighbour joining a better approximation of the trees he needed. The hosts discuss the relationship between Mash distances and average nucleotide identity, or ANI: comparable, but not equivalent. Lee points to the Mash paper's correlation with ANI using a thousand k-mers, and explains that he chose 10,000 for Mashtree to retain more resolution while remaining fast.

### What the tree can and cannot tell you

Lee stresses that Mashtree produces a tree or dendrogram, not a phylogeny. Its internal nodes should not be read as inferred ancestral states, and the result is intended to cluster genomes by similarity rather than establish their evolutionary history. He recommends it as a first pass before a more detailed analysis, particularly when preparing work for publication.

Useful questions include whether a collection captures enough diversity, whether samples appear related, and whether a sample can be excluded from a possible outbreak before investing in deeper analysis. Lee names E. coli, Shigella, Listeria and Vibrio from his own work, and reports seeing successful use with Legionella outside that enteric focus.

One host asks about streaming long reads from a MinION. Lee says he would like to test that application, but had not done much testing with it. He regards the different error profile as a reason for separate evaluation.

### Slower routes to the same problem

Another host describes Saffron tree, which he made in 2017 and published in JOSS. It collected k-mers from sequence files, compared their intersections and built a tree. It was fast with two or three genomes, but scaled poorly as the collection grew.

Lee had also tried a slow approach based on Jaccard distances between k-mer collections and abandoned it. Another prototype used MUMmer-based ANI, but that route still required genome assembly and therefore did not meet the same need for speed. These comparisons explain why Mash became the foundation: it offered compact comparisons and could accept either assemblies or raw sequencing reads.

### Perl, packaging and documentation

Mashtree is written in Perl. Lee defends that choice in terms of his familiarity with Perl multithreading when development began, rather than claiming other languages lacked suitable facilities. The package has a main script and supporting library files, and can be installed through CPAN.

Torsten's prodding about packaging on GitHub helped motivate the CPAN approach. Lee used MakeMaker to generate the makefile for installation, and added unit tests covering major functions and several smaller ones. He values the resulting standard installation and testing conventions.

Documentation is deliberately straightforward: a Markdown README links to additional Markdown files in a docs subdirectory. Lee sees advantages in documentation travelling with a cloned repository and remaining readable at the command line without opening a browser.

### Open review and a stable program

The paper is Katz et al. (2019), “Mashtree: a rapid comparison of whole genome sequence files”, published in the Journal of Open Source Software, volume 4, issue 44, article 1762. Lee initially found the idea of a free journal suspicious. Seeing a paper by Steve Davis at the FDA helped reassure him, and he became enthusiastic about JOSS's transparent peer review through GitHub.

At the time of recording, Lee's plan was largely to leave Mashtree stable and respond to bug reports. He discusses Torsten's suggestion to make the tree-building pipeline more general: users could supply distances from another comparison method, such as ANI, rather than relying on Mash. Lee wishes he had designed that flexibility in earlier, but says he does not have time to implement it.

## Highlights

- [00:00:02](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=0:02) — Introducing the software deep dive and Lee's turn in the hot seat.
- [00:00:25](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=0:25) — The need for rapid trees from large whole-genome sequencing files.
- [00:01:04](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=1:04) — Saffron tree as an earlier approach that struggled with scaling.
- [00:02:17](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=2:17) — The Mash name, MinHash and the connection to AltaVista.
- [00:03:08](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=3:08) — How hashing k-mers produces compact sketches for genome comparison.
- [00:05:36](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=5:36) — Whether Mashtree could work with long reads streamed from a MinION.
- [00:06:45](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=6:45) — Lee's early, slow prototype using Jaccard distances between k-mer collections.
- [00:09:16](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=9:16) — Correlation with ANI and the decision to retain 10,000 k-mers.
- [00:10:42](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=10:42) — Mashtree's role as a fast, approximate first-round analysis.
- [00:12:06](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=12:06) — Why familiarity with Perl multithreading shaped the implementation.
- [00:14:00](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=14:00) — Keeping documentation in Markdown alongside the code.
- [00:17:39](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=17:39) — A proposed interface for alternative distance methods and plans for maintenance.

## In their own words

> MashTree creates trees, dendrograms, but it does not create a phylogeny.
>
> — Lee Katz, [00:03:08](https://soundcloud.com/microbinfie/mashtree-software-deep-dive#t=3:08)

## Who is talking

- **Lee Katz** (host)

Also mentioned: Torsten, Steve Davis.

## Tools and resources mentioned

Mashtree, Mash, MinHash, UPGMA, neighbour joining, average nucleotide identity (ANI), whole-genome MLST (wgMLST), Jaccard distance, MUMmer, Saffron tree, MinION, Perl, CPAN, MakeMaker, GitHub, AltaVista.

## Questions this episode answers

### Does Mashtree need assembled genomes?

No. Lee explains that it can compare raw sequencing reads as well as assemblies, avoiding assembly when a rapid preliminary comparison is needed.

### Does Mashtree produce a phylogeny?

Lee explicitly describes its output as a tree or dendrogram, not a phylogeny. It clusters genomes by similarity without establishing ancestral states, and he recommends more detailed analysis for a final publication.

### Why did Lee choose 10,000 k-mers for Mashtree?

The Mash paper showed a good correlation with ANI when retaining a thousand k-mers. Lee chose 10,000 because the comparison remained fast and he wanted to preserve higher resolution.

### Had Mashtree been tested for MinION streaming data?

At the time of the episode, Lee said he had not done much testing with MinION data. He wanted separate tests because its error profile differs.

### How is Mashtree installed and documented?

Lee says Mashtree can be installed through CPAN and is packaged using MakeMaker. Its documentation consists of a Markdown README and additional Markdown files stored with the repository.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Paper: https://joss.theoj.org/papers/10.21105/joss.01762 Repository:
https://github.com/lskatz/mashtree  We chat to the author of Mashtree,
bioinformatics software for creating a very fast tree from genomes.
Citation Katz et al., (2019). Mashtree: a rapid comparison of whole
genome sequence files. Journal of Open Source Software, 4(44), 1762,
https://doi.org/10.21105/joss.01762
