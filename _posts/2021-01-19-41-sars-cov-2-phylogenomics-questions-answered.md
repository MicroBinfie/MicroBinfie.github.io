---
layout: page
title: 'Episode 41: SARS-CoV-2 Phylogenomics questions answered'
date: '2021-01-19 00:00:00'
link: https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered
episode: '41'
soundcloud_track: '967805281'
tags:
- microbinfie
- podcast
description: A January 2021 panel on SARS-CoV-2 outbreak detection, Pangolin lineages, Civet and Llama, contextual genomes and variant-call quality.
excerpt: A January 2021 panel on SARS-CoV-2 outbreak detection, Pangolin lineages, Civet and Llama, contextual genomes and variant-call quality.
headline: 'SARS-CoV-2 phylogenomics: lineages, outbreaks and variant calls'
guests:
- Nick Loman
- Verity Hill
- Andrew Page
- Anna Price
topics:
- sars-cov-2
- phylogenomics
- outbreak detection
- lineage assignment
- phylotypes
- contextual genomes
- variant interpretation
- sequence quality
- vaccine sequences
faq:
- q: What is the difference between COG-UK phylotypes and Pangolin lineages?
  a: Phylotypes describe shared SNP sites at a much finer resolution and are characterised as a textual representation of the tree. Pangolin lineages can contain much larger groups, so sharing a lineage alone does not establish a close epidemiological connection.
- q: Can BLAST find the closest SARS-CoV-2 genomes for an outbreak investigation?
  a: The panel advises against relying on it because the small number of differences between genomes demands finer resolution. They suggest using tools such as Llama to extract relevant parts of a reference tree, and note that a public NCBI search misses genomes outside GenBank.
- q: How does Civet decide which sequences belong in a subtree?
  a: It uses configurable distances above and below the query sequence, together with a radius setting. Verity recalls defaults of two nodes up and two down, but recommends adjusting the settings to obtain useful context without including unmanageable numbers of sequences.
- q: How was pangoLEARN's training dataset manually curated?
  a: The team split a large tree into smaller trees for inspection in FigTree, checked earlier lineage assignments and updated membership or created new lineages. The larger curation exercise was described as roughly a week's work every couple of months.
- q: Do variation databases guarantee reliable SARS-CoV-2 variant calls?
  a: 'No: their results depend on the quality of the submitted consensus genomes, and a FASTA sequence alone does not establish read support. Quality checks can help, but unusual variants may represent either errors or genuine diversity from underrepresented regions.'
---

*SARS-CoV-2 phylogenomics: lineages, outbreaks and variant calls*

Nick Loman, Verity Hill, Andrew Page and Anna Price take part in a SARS-CoV-2 phylogenomics Q&A from the ARTICnetwork and CLIMB-BIG-DATA workshop held on 14–15 January 2021. The discussion covers outbreak detection, lineage assignment, selecting contextual genomes and interpreting variation. It explains why the resolution of a phylogenetic analysis, the quality of its input sequences and the epidemiological context all matter.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 41: SARS-CoV-2 Phylogenomics questions answered" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/967805281&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 41: SARS-CoV-2 Phylogenomics questions answered on SoundCloud](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered)

## In this episode

### Detecting outbreaks with Polecat

Polecat is presented as a systematic way to flag genomic clusters that might otherwise escape notice. Rather than relying only on someone spotting an unusual part of a tree, it summarises the tree into small groups and reports statistics about them. Features of interest include a long branch followed by many sequences, rapid growth, or more sequences than expected within a particular place and time.

Verity explains that the tool was developed largely in response to requests from Public Health England. Its purpose was not originally limited to finding variants of concern: it could also help distinguish outbreaks where high case numbers made epidemiological connections difficult to see. Polecat was available on GitHub, although she could not confirm how well it would work on other datasets.

### Phylotypes, lineages and manual curation

COG-UK phylotypes and Pangolin lineages answer questions at different resolutions. Verity describes phylotypes as a textual codification of the tree based on shared SNP sites. Two sequences with the same phylotype are much more closely connected than two sequences sharing a Pangolin lineage, which can sometimes be very large. Phylotypes therefore support finer-scale questions, including hospital outbreak investigations, while lineages are useful for broader national and international comparisons.

The sequence-to-lineage dataset used to train pangoLEARN requires substantial manual curation. The team divides a large tree into smaller trees that can be inspected comfortably in FigTree, compares previous assignments with the updated tree, adds sequences to existing lineages and assigns new lineage numbers where needed. At the time, this larger curation exercise took roughly a week and happened every couple of months. Researchers could also propose epidemiologically or biologically interesting groups for lineage assignment, and volunteers were invited to help inspect trees.

### Civet, Llama and finding contextual genomes

Llama was developed for global use and broader lineage-level investigations, while Civet initially targeted UK cluster investigations. They share substantial code, but Civet includes spatial analysis and mapping features that depend on carefully curated metadata. The tools were becoming more similar as work progressed towards making Civet usable outside the UK.

For finding relatives of a query genome, the panel advises against relying on BLAST. SARS-CoV-2 genomes can differ by very few mutations, and the speakers argue that BLAST does not provide the resolution needed here. Searching the public NCBI database would also miss many genomes not held in GenBank.

The alternative described is to locate the relevant region of an existing reference tree, extract contextual sequences and rebuild a smaller tree with new queries. This avoids rebuilding a tree of perhaps 400,000 sequences whenever another genome is added. Even then, a broad lineage such as B.1 may say little about a genome's closest relatives. The discussion of B.1.1.7 stresses that distinguishing importation from local transmission also requires epidemiology.

### Choosing subtrees and adapting to other viruses

Civet's subtree selection can be adjusted through its configuration file or command line. Verity recalls defaults of two nodes above and two nodes below a sequence of interest, alongside a radius setting. Increasing these distances can supply missing context; reducing them can prevent an investigation from pulling in overwhelming numbers of sequences.

This matters because densely sampled UK data can contain polytomies involving hundreds or thousands of sequences, which are difficult to display. The panel cautions against transferring settings directly to HIV or another virus. HIV's faster evolution changes how separation between subtrees should be interpreted, while infections involving multiple variants or strains may not be represented adequately by a simple tree. A setting useful for excluding SARS-CoV-2 transmission need not support the same conclusion for HIV.

### Sharing vaccine sequences

A question asks whether sequences for mRNA and adenoviral-vector vaccines are available. One panellist recalls seeing a sequence for an mRNA vaccine, including notation for modified RNA bases, but does not think the sequences of all vaccines are available.

The response favours sharing these sequences and argues that they may become known through laboratory sequencing or incidental detection anyway. This is a discussion of availability and openness as understood in January 2021, rather than a catalogue of vaccine sequences.

### Variation databases and the limits of quality checks

The panel compares CoV-GLUE, Nextstrain and the Nextstrain Clades sequence-analysis site. CoV-GLUE is described as a catalogue of mutations, insertions and deletions, useful for investigating their frequency. Nextstrain places changes on a phylogenetic tree through ancestral state reconstruction, helping users examine lineage-defining or recurrent mutations such as N501Y and E484K. These are complementary views, not interchangeable outputs; gene naming and filtering can differ between tools.

Variant-call quality ultimately depends on the consensus genomes supplied. A base in a FASTA file does not reveal whether the underlying reads adequately support it. Curation and automated checks can flag suspicious sequences, but their results need interpretation: private variants might indicate poor data, or genuinely reflect sampling from an underrepresented region. The panel also notes CoV-GLUE checks against ARTIC amplicon regions that can highlight potentially problematic SNP positions. Database reports and quality flags cannot remove the need to consider the input data.

## Highlights

- [00:00:16](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=0:16) — Introducing Polecat for investigating genomically defined clusters
- [00:03:54](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=3:54) — COG-UK phylotypes versus Pangolin lineages
- [00:06:11](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=6:11) — How Civet and Llama differ in scope and metadata requirements
- [00:07:22](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=7:22) — Finding related international genomes and whether BLAST is suitable
- [00:10:43](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=10:43) — Using reference trees rather than rebuilding a tree of 400,000 genomes
- [00:11:48](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=11:48) — Manually curating sequence-to-lineage assignments for pangoLEARN
- [00:14:47](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=14:47) — Adjusting Civet's node distances and radius to select subtrees
- [00:16:56](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=16:56) — Why tools built for SARS-CoV-2 need caution when applied to HIV
- [00:18:12](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=18:12) — Availability and sharing of vaccine sequences
- [00:19:24](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=19:24) — Comparing CoV-GLUE and Nextstrain variation reports
- [00:22:55](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=22:55) — Why variant-call quality depends on consensus genomes and read support
- [00:23:55](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=23:55) — Why private variants are not necessarily evidence of poor sequence quality

## In their own words

> So it depends on the resolution of the question you're asking really.
>
> — Verity Hill, [00:04:11](https://soundcloud.com/microbinfie/41-sars-cov-2-phylogenomics-questions-answered#t=4:11)

## Who is talking

- **Nick Loman** (panellist, University of Birmingham)
- **Verity Hill** (panellist, University of Edinburgh)
- **Andrew Page** (panellist, Quadram Institute)
- **Anna Price** (panellist, MRC CLIMB and Cardiff University)

## Tools and resources mentioned

Polecat, Pangolin, pangoLEARN, Civet, Llama, BLAST, GenBank, FigTree, Nextstrain, Nextstrain Clades, CoV-GLUE.

## Questions this episode answers

### What is the difference between COG-UK phylotypes and Pangolin lineages?

Phylotypes describe shared SNP sites at a much finer resolution and are characterised as a textual representation of the tree. Pangolin lineages can contain much larger groups, so sharing a lineage alone does not establish a close epidemiological connection.

### Can BLAST find the closest SARS-CoV-2 genomes for an outbreak investigation?

The panel advises against relying on it because the small number of differences between genomes demands finer resolution. They suggest using tools such as Llama to extract relevant parts of a reference tree, and note that a public NCBI search misses genomes outside GenBank.

### How does Civet decide which sequences belong in a subtree?

It uses configurable distances above and below the query sequence, together with a radius setting. Verity recalls defaults of two nodes up and two down, but recommends adjusting the settings to obtain useful context without including unmanageable numbers of sequences.

### How was pangoLEARN's training dataset manually curated?

The team split a large tree into smaller trees for inspection in FigTree, checked earlier lineage assignments and updated membership or created new lineages. The larger curation exercise was described as roughly a week's work every couple of months.

### Do variation databases guarantee reliable SARS-CoV-2 variant calls?

No: their results depend on the quality of the submitted consensus genomes, and a FASTA sequence alone does not establish read support. Quality checks can help, but unusual variants may represent either errors or genuine diversity from underrepresented regions.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

ARTICnetwork & CLIMB-BIG-DATA present a panel discussion on SARS-CoV-2
phylogenomics with Nick Loman from the University of Birmingham,
Verity Hill from the University of Edinburgh, Andrew Page from the
Quadram Institute and Anna Price from MRC CLIMB and Cardiff
University. This was part of a workshop on COVID-19 data analysis.
The topics covered are: More about Polecat  Whats the difference
between COG-UK Phylotypes and Pangolin lineages? What is the
difference between Civet and Llama Can you use BLAST to find similar
SARS-CoV-2 genomes? How do you find similar sequences in the public
repositories to give your samples context? How do you manually curate
the dataset for PangoLEARN? How does Civet choose what constitutes a
subtree? Can Civet be adapted to other viruses? Are the vaccine
sequences available? Databases that report variation Quality of
variant calls?  Groups: https://www.climb.ac.uk/artic-and-climb-big-
data-joint-workshop/ https://www.climb.ac.uk/ https://artic.network/
https://cogconsortium.uk/  Software: https://github.com/COG-UK/polecat
https://github.com/cov-lineages/pangolin https://github.com/cov-
lineages/llama https://github.com/artic-network/civet
https://github.com/cov-lineages/pangoLEARN
http://tree.bio.ed.ac.uk/software/figtree/  Analysis websites:
https://cov-lineages.org/ https://clades.nextstrain.org/
https://pangolin.cog-uk.io/ http://cov-glue.cvr.gla.ac.uk/
