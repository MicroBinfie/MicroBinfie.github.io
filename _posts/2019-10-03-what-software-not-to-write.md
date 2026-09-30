---
layout: page
title: 'Episode 2: What bioinformatics software not to write part 2'
date: '2019-10-03 00:00:00'
link: https://soundcloud.com/microbinfie/what-software-not-to-write
episode: '2'
soundcloud_track: '679961924'
tags:
- microbinfie
- podcast
description: The hosts question new metagenomics and AMR tools, arguing for better databases, long-read methods, useful visualisation and easier installation.
excerpt: The hosts question new metagenomics and AMR tools, arguing for better databases, long-read methods, useful visualisation and easier installation.
headline: 'What not to write: metagenomics and AMR software'
guests: []
topics:
- metagenomics
- 16s
- taxonomic classification
- reference databases
- antimicrobial resistance
- database curation
- long reads
- population genomics
- data visualisation
- software usability
faq:
- q: Why do the hosts argue against writing another metagenomics tool?
  a: They describe an established field with many classifiers and assemblers already using different approaches. Their preference is to improve reference databases, data quality or existing implementations unless a new tool addresses a genuinely different need.
- q: What does the episode say about 16S versus shotgun metagenomics?
  a: One host strongly discourages further 16S tool development because of the limited biological information recovered. Another notes that amplification can allow 16S to recover more OTUs than shotgun sequencing, so the discussion includes a qualification rather than a unanimous dismissal.
- q: Should researchers build another AMR database?
  a: The hosts recommend contributing to an existing repository instead. They identify inconsistent naming, uneven curation, missing laboratory validation and disagreement over resistance definitions as priorities that another competing database would not necessarily solve.
- q: Where do the hosts see opportunities for new bioinformatics software?
  a: They point to long reads, complete genomes, mobile genetic elements, epigenetic information, GPU or FPGA implementations and population-scale comparisons. They also value visualisation for large datasets and tools that are easier to install, document and maintain.
---

*What not to write: metagenomics and AMR software*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan continue their discussion of crowded areas in bioinformatics software, focusing on metagenomics and antimicrobial resistance. They argue that database curation, experimental validation and improvements to existing tools can be more valuable than another competing implementation. Long reads, population-scale comparisons, visualisation and accessible software remain areas where they see useful work to do.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 2: What bioinformatics software not to write part 2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/679961924&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 2: What bioinformatics software not to write part 2 on SoundCloud](https://soundcloud.com/microbinfie/what-software-not-to-write)

## In this episode

### 16S and a crowded classification field

The hosts question whether another tool is justified when many implementations already exist, a problem is effectively solved or unsolvable, or the technology has been superseded. One host takes a particularly strong position against developing more 16S tools, discussing V1, V2 and V4 and favouring approaches that reveal more about an organism’s genes and biology. Another offers a qualification: amplification can give 16S an advantage in the number of OTUs recovered compared with shotgun sequencing.

For shotgun taxonomic classification, they name MEGAN, Kraken, SIGMA, MIDAS, MetaPhlAn and mOTUs. These use different approaches, including conserved housekeeping genes, unique markers and whole-genome reference databases. The hosts acknowledge that classifiers give different answers, but argue that entering this established field requires substantial work. Shotgun data can also provide context beyond an unfamiliar OTU—for example, suggesting that something resembles Salmonella without being Salmonella.

### Improve databases and assembly inputs

Lee describes his Kalamari work as an effort to improve the databases used for metagenomic classification. He emphasises specificity and fewer false hits, accepting that more reads may remain unclassified. He also describes a reported Kraken problem: adding multiple assemblies per species can make assignments less species-specific, shifting results towards the genus level. Another host highlights database sampling bias and favours Bracken’s Bayesian adjustment of Kraken reports, alongside changes introduced in Kraken2.

The assembly discussion similarly favours better inputs over another similar algorithm. Higher sequencing depth, better-quality DNA and better binning can improve assemblies. The show notes list MetaSPAdes, metaFlye, MEGAHIT and MetaVelvet, alongside adaptations of single-isolate assemblers. Long reads are especially attractive to the hosts because they can produce larger pieces, complete chromosomes and full plasmids.

### AMR databases need curation and agreement

For antimicrobial resistance, the concern is not simply a shortage of databases. The hosts describe competing resources with different formats, inconsistent naming, uneven curation and, in some cases, abandonment. They question entries whose resistance claims have not been validated in the laboratory. Lee recalls a hackathon on 1 June that compared genes across databases and worked towards more consistent naming.

The discussion includes the Global Microbial Identifier, GenFS and NARMS as examples of collaborative efforts. Another host describes a consensus initiative involving NCBI, Public Health Agency Canada, ResFinder contributors and other database groups, while expressing uncertainty about who initiated it. Even antibiotic names, abbreviations, MIC values and the meaning of intermediate resistance are presented as sources of disagreement. Their recommendation is to contribute to existing repositories and curation efforts rather than establish another rival database.

### Finding a gene is not the whole resistance question

The hosts contrast ABRICATE, which works from assemblies, with ARIBA, which works from raw reads. They note that detection tools differ in scope: some scan for genes without finding resistance-associated point mutations, with gyrA given as an example. Finding 90% of a resistance gene raises another unresolved question: does that establish resistance, especially without empirical testing?

Asked about public-health practice, Lee avoids speaking for colleagues or declaring a best tool. He names AMRFinder and ResFinder among tools used, and discusses NCBI making genotype analyses available online using NARMS annotations. He explicitly stops short of assessing the quality of those analyses himself.

### Long reads and population-scale questions

The hosts make an exception to their argument against rewriting software: adapting methods for long reads and fully complete assembled genomes. They discuss opportunities to locate mobile genetic element insertion sites and study prophages and the mobilome. Methylation patterns and Hi-C are mentioned as approaches to assembling or organising metagenomic data, while epigenetic methods from human and other eukaryote research offer ideas for microbial work.

They also discuss moving algorithms to GPUs or FPGAs, stressing that this requires different programming rather than simply transferring an existing script. At a larger scale, datasets are moving beyond tens or hundreds of genomes to thousands or tens of thousands. The proposed challenge is whole-population comparison: identifying what is conserved, variable, rearranged or inserted across a species. Graph-based approaches are discussed as promising but complicated by messy biological data.

### Visualisation, maintenance and installation

Useful visualisation is another priority, particularly for large datasets, mixed populations and metagenomics. The hosts want more than progressively larger versions of existing comparison displays. They also criticise web services that disappear after a PhD or postdoctoral project ends, especially when the source code has not been released.

Machine learning enters the discussion with a warning about input quality: finding a signal does not establish that it is real. The closing qualification is practical. Even in a crowded field, software can be valuable if it is easy to install, well documented and maintainable. Conda and Docker are offered as preferable routes to installation compared with editing makefiles, navigating scattered documentation and installing out-of-date dependencies.

## Highlights

- [00:01:08](https://soundcloud.com/microbinfie/what-software-not-to-write#t=1:08) — A strong critique of developing more 16S tools, including V1, V2 and V4 approaches
- [00:02:47](https://soundcloud.com/microbinfie/what-software-not-to-write#t=2:47) — Shotgun taxonomic classifiers and their different reference strategies
- [00:04:02](https://soundcloud.com/microbinfie/what-software-not-to-write#t=4:02) — Lee’s Kalamari work and the trade-off between specificity and unclassified reads
- [00:05:53](https://soundcloud.com/microbinfie/what-software-not-to-write#t=5:53) — Metagenomic assemblers, better input data and opportunities from long reads
- [00:07:32](https://soundcloud.com/microbinfie/what-software-not-to-write#t=7:32) — AMR database proliferation and a hackathon on harmonising gene names
- [00:10:43](https://soundcloud.com/microbinfie/what-software-not-to-write#t=10:43) — Seeking consensus on AMR definitions and contributing to existing repositories
- [00:11:53](https://soundcloud.com/microbinfie/what-software-not-to-write#t=11:53) — ABRICATE, ARIBA and the limits of resistance-gene detection
- [00:15:05](https://soundcloud.com/microbinfie/what-software-not-to-write#t=15:05) — Long reads and complete genomes as reasons to revisit existing software
- [00:15:18](https://soundcloud.com/microbinfie/what-software-not-to-write#t=15:18) — Why GPU and FPGA implementations require a different programming approach
- [00:16:42](https://soundcloud.com/microbinfie/what-software-not-to-write#t=16:42) — Borrowing epigenetic approaches from eukaryote and human research
- [00:18:10](https://soundcloud.com/microbinfie/what-software-not-to-write#t=18:10) — The problem of unmaintained visualisation websites without released source code
- [00:19:59](https://soundcloud.com/microbinfie/what-software-not-to-write#t=19:59) — Easy installation, documentation and maintenance as reasons to build a tool

## In their own words

> But it turns out that the databases can definitely use a lot of fixing.
>
> — Lee Katz, [00:04:02](https://soundcloud.com/microbinfie/what-software-not-to-write#t=4:02)

> I think we have to fundamentally change the way we think about our data and the way we look at our data.
>
> — one of the hosts, [00:18:36](https://soundcloud.com/microbinfie/what-software-not-to-write#t=18:36)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

MEGAN, Kraken, Kraken2, Bracken, SIGMA, MIDAS, MetaPhlAn, MetaPhlAn2, mOTUs, Kalamari, MetaSPAdes, metaFlye, MEGAHIT, MetaVelvet, CARD, ResFinder, ABRICATE, ARIBA, AMRFinder, Hi-C, Conda, Docker.

## Questions this episode answers

### Why do the hosts argue against writing another metagenomics tool?

They describe an established field with many classifiers and assemblers already using different approaches. Their preference is to improve reference databases, data quality or existing implementations unless a new tool addresses a genuinely different need.

### What does the episode say about 16S versus shotgun metagenomics?

One host strongly discourages further 16S tool development because of the limited biological information recovered. Another notes that amplification can allow 16S to recover more OTUs than shotgun sequencing, so the discussion includes a qualification rather than a unanimous dismissal.

### Should researchers build another AMR database?

The hosts recommend contributing to an existing repository instead. They identify inconsistent naming, uneven curation, missing laboratory validation and disagreement over resistance definitions as priorities that another competing database would not necessarily solve.

### Where do the hosts see opportunities for new bioinformatics software?

They point to long reads, complete genomes, mobile genetic elements, epigenetic information, GPU or FPGA implementations and population-scale comparisons. They also value visualisation for large datasets and tools that are easier to install, document and maintain.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode we identify areas of “Peak-bioinformatics”. There are a lot of existing bioinformatics software out there - more often than not the new tool you want to write already exists or a new tool cannot effectively improve. We discuss this in terms of metagenomics and anti microbial resistance.

Question and comments? microbinfie@gmail.com

SHOW NOTES
Generally, novel software is not needed if:
There are a plethora of existing tools
The problem is more or less solved or its been shown to be unsolvable
The underlying technology or problem is now obsolete and/or superceded by other methods.
Metagenomics
Taxonomic classification: Megan, Kraken, SIGMA, MIDAS, metaphlan2, mOTUs.
Assemblers: MetaSpades, metaflye,MEGAHIT, MetaVelvet, a lot of single isolate assemblers have been tweaked to run on metagenomes.
https://github.com/lskatz/Kalamari
AMR
https://github.com/arpcard/amr_curation
https://food-safety-bioinformatics-hackathon.github.io/AMR-protocols/
ABRICATE https://github.com/tseemann/abricate
ARIBA https://www.sanger.ac.uk/science/tools/ariba
Too many detection tools:
https://docs.google.com/spreadsheets/d/18XGWpDiaE249qQKDAL7gdBCka0Z1drpA_s3FElfMJe0/edit#gid=0

Microbial Bioinformatics is a rapidly changing field marrying computer science and microbiology. Join us as we share some tips and tricks we've learnt over the years. If you're student just getting to grips to the field, or someone who just wants to keep tabs on the latest and greatest - this podcast is for you.

The hosts are Dr. Lee Katz from the Centres for Disease Control and Prevention (US), Dr. Nabil-Fareed Alikhan and Dr. Andrew Page both from Quadram Institute Bioscience (UK) and bring together years of experience in microbial bioinformatics.

The opinions expressed here are our own and do not necessarily reflect the views of Centres for Disease Control and Prevention or Quadram Institute Bioscience.

Intro music : Werq - Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 3.0 License
http://creativecommons.org/licenses/by/3.0/

Outro music : Scheming Weasel (faster version) - Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 3.0 License
http://creativecommons.org/licenses/by/3.0/
