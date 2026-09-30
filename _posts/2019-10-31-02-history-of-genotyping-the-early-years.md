---
layout: page
title: 'Episode 4: History of Genotyping - The early years'
date: '2019-10-31 00:00:00'
link: https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years
episode: '4'
soundcloud_track: '678648705'
tags:
- microbinfie
- podcast
description: How PFGE, MLST, MLVA and older typing methods shaped outbreak surveillance, and how PulseNet, GenomeTrakr and Galaxy support shared analysis.
excerpt: How PFGE, MLST, MLVA and older typing methods shaped outbreak surveillance, and how PulseNet, GenomeTrakr and Galaxy support shared analysis.
headline: 'Before whole genomes: the early years of microbial typing'
guests: []
topics:
- microbial genotyping
- pfge
- mlst
- mlva
- outbreak surveillance
- genomic epidemiology
- data sharing
- workflow sharing
faq:
- q: Can a complete genome predict a PFGE banding pattern?
  a: Lee explains that it cannot necessarily do so, because methylation can block restriction-enzyme cutting. He also describes cases where PFGE groupings split into several WGS clades, or different PFGE profiles collapse into one WGS type.
- q: Why use older typing methods when whole-genome sequencing is available?
  a: The hosts describe their continuing value for outbreak discrimination and for interpreting historical associations with geography, hosts and environments. In the Haiti cholera investigation, PFGE and MLVA also helped select diverse samples for sequencing when resources were limited.
- q: What is the difference between PulseNet and GenomeTrakr?
  a: In the episode, PulseNet is described as a pre-genomics surveillance platform historically coordinating PFGE and MLVA results, then moving towards WGS workflows. GenomeTrakr is described as the FDA's WGS-based initiative for laboratory submissions, central analysis and sharing through NCBI.
- q: How are IRIDA and Galaxy used together at Quadram?
  a: Nabil describes IRIDA as handling data management and simpler, standardised pipelines. Data can then be linked into Galaxy for more complex, user-built workflows and bespoke follow-up analyses.
---

*Before whole genomes: the early years of microbial typing*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss microbial typing before routine whole-genome sequencing, from phage and plasmid typing to PFGE, MLVA and MLST. They explain what these methods reveal, where their results differ from whole-genome comparisons, and why older outbreak evidence still matters. The conversation then follows the transition towards shared genomic surveillance and reusable analysis workflows.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 4: History of Genotyping - The early years" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/678648705&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 4: History of Genotyping - The early years on SoundCloud](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years)

## In this episode

### What older typing methods measure

The hosts survey plasmid typing, phage typing, serotyping, PFGE, MLVA and MLST as ways of describing microbes before routine whole-genome sequencing (WGS). These methods measure different features rather than necessarily reproducing a whole-genome phylogeny. Phage typing, for example, tests how bacteria respond to different phages; MLVA examines microsatellites, while MLST compares housekeeping genes.

Nabil-Fareed Alikhan describes serotyping as a continuing reporting standard for Salmonella and recalls MLVA being used for reporting between countries through the ECDC. The hosts also discuss hospital antibiograms: comparing antibiotic resistance profiles can help distinguish groups of infections and decide which cases belong in an outbreak.

### Why PFGE trees can differ from genome trees

Lee Katz explains that PFGE is difficult to translate directly into WGS results. Restriction enzymes generate a banding pattern, but methylation can block cutting, so even a complete genome does not necessarily predict the observed bands. He describes enzymes chosen to produce about 15 bands and a simple distance matrix based on band differences, which can then become a tree.

Those trees may agree with WGS trees, but not always. Lee gives Salmonella Newport as an example that can separate into roughly three WGS clades. Different PFGE profiles can also collapse into one WGS type. Nabil notes that phage-derived genomic content can change a banding pattern and distort the apparent relationship between strains.

### The value of older outbreak evidence

Typing results help define outbreaks, but they must be combined with context. Lee's deliberately fictitious example is a meningitis outbreak involving sequence type 11 in a boarding school: both the seven-gene MLST result and the shared setting matter. He also recalls meningococcal sequence type 32 being strongly associated with the north-western United States in his earlier work.

The discussion argues against dismissing older literature simply because WGS is now available. Serotypes and other typing results can retain useful associations with geography, animal hosts or environments. Lee recounts the Rajneeshi food-poisoning investigation as an example of plasmid typing: investigators compared a distinctive plasmid from the outbreak with an ATCC strain purchased by the group. The story illustrates the investigative value of a method that does not require whole-genome data.

### Choosing samples and moving to routine WGS

For the Haiti cholera investigation, Lee describes using PFGE followed by MLVA to choose a diversity of samples for WGS in the early 2010s. With sequencing resources limited, investigators needed an initial estimate of diversity before selecting genomes: a practical chicken-and-egg problem.

He then outlines the US transition to routine WGS surveillance as it stood in 2019. Listeria was the starting point in 2013, with an expectation of about 1,600 isolates per year from participating agencies. Salmonella was a larger undertaking, running into tens of thousands of isolates. Lee says WGS had overtaken PFGE submissions the previous year and that coordination was now centred on WGS, although laboratories were not being prevented from continuing PFGE.

### PulseNet, GenomeTrakr and public data

Lee traces PulseNet's origins to a 1993 western US E. coli outbreak linked to undercooked hamburgers, followed by its official launch in 1996. He describes more than 80 US laboratories and the wider PulseNet International consortium. Historically, PFGE and MLVA supplied standard reporting results, with BioNumerics used to coordinate them.

The contrast is with the FDA's GenomeTrakr initiative, built around WGS submissions, central analysis and NCBI as its platform. Lee says the laboratories in his own US surveillance network now submit directly to NCBI; BioProjects and contributor listings make their data discoverable. Some information is masked for patient confidentiality, allowing surveillance without tracing records back to individuals. He also describes synchronisation between NCBI and ENA, so genomes can be downloaded from either database. These arrangements connect laboratory characterisation with surveillance across institutions and borders.

### Galaxy, IRIDA and shareable workflows

The conversation moves to GenomeTrakr's expansion into GalaxyTrakr and Quadram's use of Galaxy with IRIDA, a Canadian system. Nabil explains that IRIDA manages data and launches simpler, standardised pipelines, while Galaxy supports more complex workflows built by users. This gives laboratories a route from routine results to bespoke follow-up analysis.

The hosts discuss putting pipelines on GitHub so other laboratories can download and reuse the same analyses rather than reinventing them. Galaxy is described as supporting point-and-click workflows on cloud infrastructure or a local high-performance computing cluster. One host reports on a meeting of about 25 Galaxy principal investigators, with Penn State, Johns Hopkins and Freiburg University named as major centres. Sharing validated or published workflows is presented as a practical way for laboratories to exchange methods and bioinformatics knowledge.

## Highlights

- [00:01:19](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=1:19) — An overview of plasmid typing, phage typing, serotyping, PFGE, MLVA and MLST.
- [00:05:15](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=5:15) — Why PFGE banding patterns and trees do not map directly onto WGS results.
- [00:08:47](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=8:47) — Using PFGE and MLVA to select genomes for the Haiti cholera investigation.
- [00:10:02](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=10:02) — Scaling US WGS surveillance from Listeria to much larger Salmonella collections.
- [00:10:58](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=10:58) — Direct NCBI submissions, patient confidentiality and synchronisation with ENA.
- [00:11:57](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=11:57) — Combining typing results with epidemiological context to define an outbreak.
- [00:14:42](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=14:42) — The usefulness of older typing literature and the Rajneeshi plasmid-typing story.
- [00:17:33](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=17:33) — Using antibiotic resistance profiles to distinguish hospital outbreaks.
- [00:18:25](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=18:25) — Coordinating laboratories through PulseNet and PulseNet International.
- [00:20:40](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=20:40) — How the FDA's GenomeTrakr initiative differs from PulseNet.
- [00:22:11](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=22:11) — Combining IRIDA data management and standard pipelines with flexible Galaxy workflows.
- [00:23:54](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=23:54) — The Galaxy principal investigators' meeting and the wider Galaxy community.

## In their own words

> We want to do everything WGS, but we have to understand that these classic methods really were very useful.
>
> — Lee Katz, [00:16:25](https://soundcloud.com/microbinfie/02-history-of-genotyping-the-early-years#t=16:25)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

PFGE, MLVA, MLST, Serotyping, Phage typing, Plasmid typing, Antibiograms, BioNumerics, NCBI, ENA, GalaxyTrakr, Galaxy, IRIDA, GitHub.

## Questions this episode answers

### Can a complete genome predict a PFGE banding pattern?

Lee explains that it cannot necessarily do so, because methylation can block restriction-enzyme cutting. He also describes cases where PFGE groupings split into several WGS clades, or different PFGE profiles collapse into one WGS type.

### Why use older typing methods when whole-genome sequencing is available?

The hosts describe their continuing value for outbreak discrimination and for interpreting historical associations with geography, hosts and environments. In the Haiti cholera investigation, PFGE and MLVA also helped select diverse samples for sequencing when resources were limited.

### What is the difference between PulseNet and GenomeTrakr?

In the episode, PulseNet is described as a pre-genomics surveillance platform historically coordinating PFGE and MLVA results, then moving towards WGS workflows. GenomeTrakr is described as the FDA's WGS-based initiative for laboratory submissions, central analysis and sharing through NCBI.

### How are IRIDA and Galaxy used together at Quadram?

Nabil describes IRIDA as handling data management and simpler, standardised pipelines. Data can then be linked into Galaxy for more complex, user-built workflows and bespoke follow-up analyses.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Genotyping is at the foundation of modern microbiology. We discuss all
of the techniques used in the preNGS era.
