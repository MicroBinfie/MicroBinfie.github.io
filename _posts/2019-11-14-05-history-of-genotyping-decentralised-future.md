---
layout: page
title: 'Episode 5: History of Genotyping - Decentralised Future'
date: '2019-11-14 00:00:00'
link: https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future
episode: '5'
soundcloud_track: '678649521'
tags:
- microbinfie
- podcast
description: Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss genomic metadata, patient privacy and locally run pipelines for global surveillance.
excerpt: Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss genomic metadata, patient privacy and locally run pipelines for global surveillance.
headline: 'Genotyping''s decentralised future: privacy and shared data'
guests: []
topics:
- microbial genotyping
- genomic epidemiology
- metadata standards
- patient privacy
- public health surveillance
- data sharing
- decentralised analysis
- listeria
- salmonella
faq:
- q: Why can anonymised pathogen genomes still raise privacy concerns?
  a: Dates, locations and other contextual information can be matched with outside knowledge, such as a reported hospital visit or a news story. Lee describes this concern for US Listeria surveillance, where relatively few cases can make individuals easier to identify.
- q: What minimum metadata does EnteroBase request in this episode?
  a: Nabil describes a rough explanation of the host, country and year. The aim is to help users recognise relevant strains and contact their holders, rather than collect every detail in one public repository.
- q: Why might a public sequence record disagree with its paper?
  a: Researchers may discover contamination, species-identification errors or sample-sheet mix-ups after uploading their reads. They may correct those details in the paper without updating the original public record.
- q: What does a centralised, decentralised future mean for genotyping?
  a: Laboratories would run agreed, versioned pipelines locally and submit their results to a shared comparison service. That service would hold limited metadata and help connect people investigating similar isolates, rather than performing all processing centrally.
---

*Genotyping's decentralised future: privacy and shared data*

In this second part of their history of genotyping, Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss how institutions can share and compare whole-genome data without exposing sensitive information. They examine misleading metadata, inconsistencies between public records and publications, and the role of platforms such as EnteroBase. Their proposed direction is a centralised, decentralised future: local analysis using agreed pipelines, with shared results and enough metadata to connect the people investigating related isolates.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 5: History of Genotyping - Decentralised Future" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/678649521&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 5: History of Genotyping - Decentralised Future on SoundCloud](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future)

## In this episode

### Patient privacy and commercial consequences

Removing names does not necessarily make genomic data anonymous. Nabil-Fareed Alikhan explains how hospital attendance, dates or a county containing only two possible farms could help someone identify a source. Lee Katz describes the concern for Listeria surveillance in the United States, where relatively few cases make individual patients easier to distinguish. His hypothetical example pairs a genome labelled New York, June 2010 with a news report about a patient at that time.

The initial approach was to release very little metadata, including the country and an anonymised identifier. The collaboration later decided to update records six months afterwards with information such as serotype, collection period, US region and age bands of around ten years. FDA data raise different concerns: Andrew Page describes a UK company implicated in a fatal hospital Listeria outbreak that went out of business after being shut down for a few weeks.

### Why a location or source field can mislead

Andrew gives two examples of misleading geographic metadata. Many UK samples appear to come from Colindale, London, because that is Public Health England's headquarters and a default location is used for privacy. Food tested and rejected at UK ports can also appear to represent UK pathogens, although the food originated elsewhere. He recommends contacting depositors to check interpretations and request further information where possible.

Even a field called source is ambiguous: it might refer to where an isolate originated or where it was sequenced. The Global Microbial Identifier, GMI, is working towards standardised minimum metadata, but Andrew notes small differences between NCBI's pathogen checklist and EBI's GMI checklist. Such edge cases can disrupt automated processing when datasets contain hundreds of thousands of bacterial isolates.

### EnteroBase needs enough metadata to start a conversation

Nabil describes discrepancies between public sequence records and their associated papers. Researchers may upload reads immediately, then discover contamination, incorrect species identification or sample-sheet errors during analysis. They correct the publication without correcting the deposited record. With about 200,000 Salmonella SRA records under discussion, checking every associated paper is not a practical solution.

EnteroBase therefore asks for only a rough description of the host, country and year. Its purpose is not to become the primary repository for every piece of metadata. Instead, those fields should let a researcher recognise a related strain, understand its broad sampling context and contact the person holding it. Nabil presents this as a way to enable collaboration while acknowledging privacy restrictions and academic concerns about being scooped.

### Co-ordinating surveillance platforms across borders

Lee describes PulseNet's US role and PulseNet International's collaborations, alongside GMI meetings representing roughly 40–50 nations. The US collaboration GenFS brings together CDC, FDA, agencies under USDA and NCBI around whole-genome sequencing. At the time of recording, Lee anticipated a paper describing GenFS that year or the next; he emphasised its complexity and many authors rather than giving a published citation.

Other platforms and projects include IRIDA and INNUENDO, which Lee believes serves 12 European countries. Andrew describes COMPARE as another European project, bringing tools such as ResFinder and PlasmidFinder together with EBI pipelines and systems. Lee also names GalaxyTrakr as the platform over GenomeTrakr. BIGSdb and EnteroBase support genomic epidemiology as well as broader population-genomics work. Nabil notes that both can support surveillance and institutional communication, while being available online and free to use.

### Local analysis with a shared place to compare results

Nabil questions whether monolithic databases can continue handling requests from the whole world. Earlier approaches such as PCR allowed laboratories with fewer resources to generate comparable results; moving to whole-genome sequencing also introduces bandwidth and submission demands. Local analysis could reduce those barriers. It could also keep analysis closer to the people who collected samples, rather than leaving enquiries with a sequencing-data submitter who knows little about the original sampling. Nanopore sequencing is discussed as an opportunity to process data in the field.

The proposed architecture uses transparent, locally installable pipelines with agreed, fixed versions, probably distributed in containers. Each laboratory would process its own data before submitting results for comparison, distributing the computational workload. Nabil uses the prospect of half a million or a million Salmonella genomes to illustrate the scaling problem. A shared service would retain minimum metadata and direct researchers towards conversations with others who had seen similar isolates.

## Highlights

- [00:01:08](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=1:08) — How genomic data and metadata can identify patients or farms despite anonymisation
- [00:02:40](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=2:40) — Why Colindale locations and food tested at UK ports can produce misleading interpretations
- [00:04:12](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=4:12) — GMI metadata standards and differences between NCBI and EBI checklists
- [00:04:59](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=4:59) — Listeria surveillance, minimal public metadata and updates six months later
- [00:07:11](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=7:11) — Commercial consequences of identifying an outbreak-associated company
- [00:09:28](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=9:28) — EnteroBase's handling of inconsistent metadata in public records and papers
- [00:12:13](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=12:13) — Co-ordinating surveillance platforms through GMI and the US GenFS collaboration
- [00:14:54](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=14:54) — COMPARE and the integration of ResFinder, PlasmidFinder and EBI systems
- [00:15:23](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=15:23) — GalaxyTrakr over GenomeTrakr, followed by BIGSdb and EnteroBase
- [00:17:16](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=17:16) — The limits of monolithic central databases and the case for local processing
- [00:20:58](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=20:58) — Locally installable pipelines and distributed processing before sharing results

## In their own words

> And for me, that's the main thing is facilitating that conversation, those collaborations.
>
> — Nabil-Fareed Alikhan, [00:09:28](https://soundcloud.com/microbinfie/05-history-of-genotyping-decentralised-future#t=9:28)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

EnteroBase, BIGSdb, IRIDA, INNUENDO, GalaxyTrakr, GenomeTrakr, ResFinder, PlasmidFinder, NCBI BioSample, SRA, MLST, PCR.

## Questions this episode answers

### Why can anonymised pathogen genomes still raise privacy concerns?

Dates, locations and other contextual information can be matched with outside knowledge, such as a reported hospital visit or a news story. Lee describes this concern for US Listeria surveillance, where relatively few cases can make individuals easier to identify.

### What minimum metadata does EnteroBase request in this episode?

Nabil describes a rough explanation of the host, country and year. The aim is to help users recognise relevant strains and contact their holders, rather than collect every detail in one public repository.

### Why might a public sequence record disagree with its paper?

Researchers may discover contamination, species-identification errors or sample-sheet mix-ups after uploading their reads. They may correct those details in the paper without updating the original public record.

### What does a centralised, decentralised future mean for genotyping?

Laboratories would run agreed, versioned pipelines locally and submit their results to a shared comparison service. That service would hold limited metadata and help connect people investigating similar isolates, rather than performing all processing centrally.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Modern genotyping is discussed in this second part.
