---
layout: page
title: 'Episode 86: What''s next for nextstrain?'
date: '2022-07-07 00:00:00'
link: https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain
episode: '86'
soundcloud_track: '1283726296'
tags:
- microbinfie
- podcast
description: Emma Hodcroft explains Nextstrain, Augur, Auspice and the challenges of adapting viral phylogenetic tools to bacterial genomes.
excerpt: Emma Hodcroft explains Nextstrain, Augur, Auspice and the challenges of adapting viral phylogenetic tools to bacterial genomes.
headline: 'Nextstrain: from flu trees to bacterial genomes'
guests:
- Emma Hodcroft
- Leonardo de Oliveira Martins
topics:
- nextstrain
- phylogenetics
- pathogen evolution
- interactive visualisation
- bacterial genomics
- tuberculosis
- influenza
- sars-cov-2
- sequence alignment
- software testing
faq:
- q: What is the difference between Augur and Auspice?
  a: Augur performs the bioinformatics analysis and writes files containing the results. Auspice reads those files to create the interactive trees and other visualisations.
- q: Can Nextstrain be used for bacteria?
  a: Yes. Hodcroft describes adapting it for tuberculosis and using it for bacterial outbreak analysis. Researchers still need to choose appropriate genomic regions and account for recombination and differences in gene content when interpreting trees.
- q: What do Nextalign and Nextclade add to Nextstrain?
  a: Nextalign was developed to make alignment more efficient when SARS-CoV-2 sequence volumes became a bottleneck. Nextclade builds on fast alignment to provide clade assignments and quality-control information through a browser interface.
- q: Does the Nextclade browser interface send sequences to the Nextstrain team?
  a: Hodcroft says the analysis happens in the user’s browser and the sequences do not come to the team. The interface provides alignment, clade information and checks such as coverage and unusual mutations.
---

*Nextstrain: from flu trees to bacterial genomes*

Emma Hodcroft joins the podcast team and guest Leonardo de Oliveira Martins to explain how Nextstrain combines phylogenetic analysis with interactive visualisation. The discussion covers its influenza origins, adaptation to bacteria, distributed development team and related tools Nextalign and Nextclade. For researchers investigating outbreaks, it explains both what the software provides and why bacterial trees need careful interpretation.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 86: What's next for nextstrain?" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1283726296&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 86: What's next for nextstrain? on SoundCloud](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain)

## In this episode

### A website and an analysis package

Nextstrain is both a website for exploring pathogen evolution and software that researchers can download to produce their own analyses. Hodcroft explains that it compares pathogen genomes, mostly viruses but also bacteria, to reconstruct relationships between sequences. Sample dates and locations add information that can help infer when and where pathogens have moved.

The project began in late 2014 or early 2015 as Next Flu, focused on influenza evolution and understanding the next circulating strain. Hodcroft’s interest in visualisation grew while sharing an office with Trevor Bedford in Edinburgh, before Nextstrain existed. His graphics brought together antigenic and phylogenetic evolution in ways she found unusually intuitive. Following that work eventually led her to a Nextstrain position in Switzerland.

### What Augur and Auspice each do

The software has two main parts. **Augur** is the bioinformatics pipeline: it takes sequences through analysis and produces files containing the inferred results. **Auspice** reads those results and turns them into interactive visualisations. The pipeline does not directly produce the finished pictures or movies; Hodcroft calls that a common misconception, and links the two-part split to Nextstrain being both software and a website.

Augur is written in Python and calls existing programs rather than replacing every component of an analysis. Hodcroft names FastTree and IQ-TREE as options for phylogenetic reconstruction. TreeTime is used to make time-resolved phylogenies. On the visualisation side, Auspice uses React and JavaScript. Hodcroft describes Python as accessible to collaborators, while the web interface requires a broader mixture of technical skills.

### Making room for bacterial genomes

After several years working on HIV, Hodcroft began exploring other pathogens. Tuberculosis offered an appealing bacterial test case because of its limited recombination and the absence of the gene loss and gain she describes as complicating work on other bacteria. Even so, the much larger genomes created substantial computational and data-handling challenges.

Her work involved making the algorithms more efficient, handling file formats researchers already used, and avoiding an unfamiliar new output format. She also considered how to separate invariant bases from changing sites while retaining the information needed for analysis. The changes extended into Auspice, including displaying genes on both strands and improving zooming. She remains particularly proud of this work because it connected underlying TreeTime algorithms, the Augur pipeline and the final visualisation.

### A small team working across time zones

Hodcroft estimates that roughly 10–12 people work on Nextstrain day to day. Many are researchers contributing alongside their scientific work rather than full-time software developers. Team members are spread across Switzerland, Seattle and New Zealand. They meet every two weeks and rely heavily on Slack, GitHub issues and written records so colleagues can follow decisions made while they were asleep.

She credits James Hadfield with Auspice and much of its interactivity, John Huddleston with pipeline efficiency and usability, and Tom Sibley with back-end organisation and databases. She also describes a major move away from early, flu-specific assumptions towards modular analysis steps. Researchers can run the stages they need and omit others, such as antigenic-data analysis when those data are unavailable. Unit tests and small test runs help catch problems when code changes, although she stresses that testing cannot guarantee perfection.

### Nextalign and Nextclade during the pandemic

The volume of SARS-CoV-2 data made sequence alignment a bottleneck before the main Nextstrain analysis. Because those sequences were relatively similar compared with many other pathogens, the team developed Nextalign to perform alignment more efficiently. Hodcroft says it became the aligner used for SARS-CoV-2 in Nextstrain and could also be used for other pathogens.

Nextclade built on that fast alignment work to offer a browser interface for aligning sequences, identifying their clades and inspecting quality-control information. Examples include coverage, unusual mutations and mutations that might affect primer sites. Hodcroft emphasises that processing happens in the browser: the sequences do not come to the Nextstrain team. These tools are connected to Nextstrain through its developers and pipeline, but sit somewhat outside the core Augur–Auspice pair.

### What a bacterial tree can tell you

Hodcroft hopes more researchers will use Nextstrain for bacteria, but argues that the biological question must guide the analysis. Bacterial samples may not share the same genes, so researchers must decide whether to analyse a genome, a gene or a selected genomic region. Recombination and gene exchange also affect how a tree should be interpreted.

Short, local outbreaks can be more straightforward because there has been less opportunity for recombination or gene loss and gain. She describes Nextstrain as useful for investigating outbreaks at scales such as a town or building, while urging greater care with broader bacterial analyses. The episode closes before a fuller discussion of SARS-CoV-2, which the hosts reserve for the next instalment.

## Highlights

- [00:00:47](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=0:47) — Introducing Emma Hodcroft and Leonardo de Oliveira Martins
- [00:02:05](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=2:05) — Nextstrain as both a website and downloadable analysis software
- [00:03:17](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=3:17) — Separating Augur’s analysis from Auspice’s interactive visualisation
- [00:04:30](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=4:30) — Next Flu’s origins and how Hodcroft became involved
- [00:08:05](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=8:05) — Adapting Nextstrain to tuberculosis and larger bacterial genomes
- [00:10:13](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=10:13) — Python, web technologies and external phylogenetic programs
- [00:11:27](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=11:27) — Coordinating a small development team across three time zones
- [00:13:57](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=13:57) — Improving testing and moving beyond flu-specific code
- [00:18:46](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=18:46) — Hodcroft’s development work before and during the pandemic
- [00:20:23](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=20:23) — Choosing bacterial phylogenetic questions and interpreting recombination
- [00:22:08](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=22:08) — Saving the fuller SARS-CoV-2 discussion for the next episode

## In their own words

> I think probably no piece of code that's more than five lines is going to be absolutely perfect and something will catch you out.
>
> — Emma Hodcroft, [00:13:57](https://soundcloud.com/microbinfie/85-whats-next-for-nextstrain#t=13:57)

## Who is talking

- **Emma Hodcroft** (guest, ISPM, University of Bern, Switzerland; Swiss Institute of Bioinformatics (SIB))
- **Leonardo de Oliveira Martins** (guest, QIB)
- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Andrew Page, Trevor Bedford, James Hadfield, John Huddleston, Tom Sibley.

## Tools and resources mentioned

Nextstrain, Augur, Auspice, Nextalign, Nextclade, TreeTime, FastTree, IQ-TREE, React, Slack, GitHub.

## Questions this episode answers

### What is the difference between Augur and Auspice?

Augur performs the bioinformatics analysis and writes files containing the results. Auspice reads those files to create the interactive trees and other visualisations.

### Can Nextstrain be used for bacteria?

Yes. Hodcroft describes adapting it for tuberculosis and using it for bacterial outbreak analysis. Researchers still need to choose appropriate genomic regions and account for recombination and differences in gene content when interpreting trees.

### What do Nextalign and Nextclade add to Nextstrain?

Nextalign was developed to make alignment more efficient when SARS-CoV-2 sequence volumes became a bottleneck. Nextclade builds on fast alignment to provide clade assignments and quality-control information through a browser interface.

### Does the Nextclade browser interface send sequences to the Nextstrain team?

Hodcroft says the analysis happens in the user’s browser and the sequences do not come to the team. The interface provides alignment, clade information and checks such as coverage and unusual mutations.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

86 What's next for nextstrain? by Microbial Bioinformatics
