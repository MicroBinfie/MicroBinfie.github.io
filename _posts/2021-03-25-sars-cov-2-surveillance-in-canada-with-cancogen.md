---
layout: page
title: 'Episode 53: SARS-CoV-2 surveillance in Canada with CANCOGEN'
date: '2021-03-25 00:00:00'
link: https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen
episode: '53'
soundcloud_track: '1016044426'
tags:
- microbinfie
- podcast
description: Emma Griffiths, William Hsiao and Finlay McGuire discuss Canada's SARS-CoV-2 sequencing, data sharing, analysis workflows and variant surveillance.
excerpt: Emma Griffiths, William Hsiao and Finlay McGuire discuss Canada's SARS-CoV-2 sequencing, data sharing, analysis workflows and variant surveillance.
headline: SARS-CoV-2 surveillance in Canada with CANCOGEN
guests:
- William Hsiao
- Finlay McGuire
topics:
- sars-cov-2
- canada
- cancogen
- genomic surveillance
- public health
- data sharing
- quality control
- de-hosting
- variant calling
- variant nomenclature
faq:
- q: What is CANCOGEN's role in Canadian SARS-CoV-2 surveillance?
  a: CANCOGEN coordinates sequencing, data collection and analysis across public health, academic and healthcare partners. Its working groups address areas including metadata, quality control and data analysis, and the network also includes host genome sequencing.
- q: Why was a complete national SARS-CoV-2 database difficult to assemble?
  a: Provinces had separate health informatics systems and authority over their data. Although national database infrastructure existed, agreements to share provincial sequences were still being established.
- q: How did the SIGNAL workflow remove human reads without losing viral reads?
  a: McGuire describes competitive mapping against both human and viral references. Reads matching both could be retained when their viral alignment was better, rather than automatically discarding every read that aligned to the human reference.
- q: How were SARS-CoV-2 variants named in Canada at the time?
  a: The episode describes adoption of Pango lineage names for reporting, with many provinces using Pangolin. The panellists also wanted consistent tracking of individual mutations and their functional evidence, not just lineage labels.
---

*SARS-CoV-2 surveillance in Canada with CANCOGEN*

Guest host Emma Griffiths joins William Hsiao and Finlay McGuire to explain how CANCOGEN coordinates SARS-CoV-2 genomics across Canada's decentralised public health system. They discuss uneven sequencing coverage, national data-sharing barriers, laboratory and bioinformatics workflows, and emerging variants. The conversation captures the surveillance situation around the episode's March 2021 release, including efforts to standardise quality control and variant naming.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 53: SARS-CoV-2 surveillance in Canada with CANCOGEN" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1016044426&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 53: SARS-CoV-2 surveillance in Canada with CANCOGEN on SoundCloud](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen)

## In this episode

### Different provinces, different surveillance coverage

Canada's geography and provincial health systems shape both the pandemic and genomic surveillance. Finlay McGuire reports about 900,000 cases nationally, with substantial burdens in Quebec, Ontario, British Columbia and Alberta. Atlantic provinces had generally experienced far fewer cases, while restrictions varied from limited pub attendance in Halifax to stringent gathering restrictions in Toronto.

The sequencing figures illustrate that unevenness. Ontario had more than 320,000 confirmed cases and about 6,000 publicly available genomes, representing roughly 1.9% of cases. Nova Scotia had about 1,600 confirmed cases and 772 public genomes, with coverage described as 46% and additional sequencing not yet public. These are figures reported during the conversation, not current surveillance totals. Comparisons between provinces therefore require attention to how deeply each population has been sampled.

### What CANCOGEN coordinates

The Genome Canada-funded Canadian COVID Genomics Network, CANCOGEN, brings together public health laboratories, academic genomics groups and healthcare partners. Many participants already collaborated through IRIDA, the Integrated Rapid Infectious Disease Analysis Platform. The Canadian Public Health Laboratory Network provides another route for communication between provincial, territorial and federal laboratories.

Sequencing is distributed rather than performed by one laboratory. Nova Scotia sends samples to the National Microbiology Laboratory in Winnipeg for sequencing and analysis, while larger provinces have substantial local capacity. Academic partners, including OICR and McMaster University, also contribute. Working groups address data analysis, metadata and quality control. CANCOGEN additionally includes human genome sequencing of infected people, connecting questions about the host with those about the pathogen and disease outcomes.

### A national database needs more than infrastructure

William Hsiao explains that provincial authority over healthcare extends, in practice, to control over health data. Separate informatics systems make sharing between provinces, territories and the Public Health Agency of Canada difficult. Collaboration exists, but information can still move through paper forms, spreadsheets and other ad hoc arrangements.

A national database at the National Microbiology Laboratory is intended to aggregate sequences for surveillance. Its technical infrastructure was in place, but data-sharing agreements remained an obstacle to complete provincial submissions. A public Canadian data portal was also being planned, drawing on the COG-UK example and considering integration with Microreact. Existing services included private provincial Nextstrain instances at the national laboratory and public views for Ontario and Canada.

### Shared quality standards, varied workflows

Laboratories retain flexibility over their analysis methods, while a CANCOGEN quality-control working group led by Jared Simpson at OICR developed baseline requirements. These cover sample preparation, controls, RNA extraction, bioinformatics and removal of human sequence data. Supply-chain disruptions, equipment and local expertise also influence laboratory choices.

Most sequencing uses amplicon approaches, particularly the ARTIC protocol, with Illumina and Nanopore platforms and differing primer schemes or kits, including Illumina COVIDSeq. Many analysis workflows converged on a BWA and iVar core for variant calling and consensus generation. The Connor lab Nextflow workflow and the Snakemake-based SIGNAL workflow provide different infrastructure around that core.

De-hosting receives particular attention. McGuire describes competitive mapping against human and viral references, retaining ambiguous reads when they map better to the virus. He also mentions nanostripper for Nanopore data and SIGNAL's interactive reports for individual sequencing runs.

### Checking variant calls around indels

McGuire describes an analysis problem that could affect the mutations reported in a genome: poor read alignment around insertions and deletions can produce spurious iVar variant calls. Alignment scoring may favour an incorrect alignment over introducing a large gap, leaving misleading differences near the indel.

Jared Simpson developed an OICR fork of the Connor lab Nextflow workflow using a FreeBayes alternative, while retaining comparable masking rules and thresholds. McGuire had also implemented this approach in SIGNAL's development branch. These checks were being evaluated alongside iVar, rather than presented as a settled replacement, to help investigate suspicious mutations around indels.

### Tracking variants and their mutations

B.1.1.7 dominates the variants of concern discussed, with smaller numbers of B.1.351 and P.1. A rapidly spreading B.1.1.7 outbreak in Newfoundland illustrates the vulnerability of places that had previously experienced little transmission. Sequencing also supports higher-throughput PCR screens for mutations such as N501Y and E484K.

Hsiao describes an aim to sequence 5–10% of samples. Although rare variants may be harder to detect at that level, increasing variants should become visible; national aggregation would strengthen detection further. For reporting, Canada adopted Pango lineage names, with many provinces using Pangolin to assign them.

The panellists argue for tracking individual mutations and combinations of mutations alongside lineage labels. They discuss linking changes to functional evidence and prioritising follow-up, while acknowledging that a formal route from variant of interest to variant of concern was not yet established.

## Highlights

- [00:00:47](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=0:47) — Emma Griffiths introduces the Canadian takeover and CANCOGEN.
- [00:03:42](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=3:42) — Provincial differences in cases, sequencing coverage and restrictions.
- [00:06:17](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=6:17) — How Canada's federated healthcare system complicates data sharing.
- [00:10:01](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=10:01) — CANCOGEN coordinates national, provincial and academic sequencing partners.
- [00:14:01](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=14:01) — Distributed sequencing feeds a national database still facing sharing barriers.
- [00:16:26](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=16:26) — Common quality-control requirements and approaches to de-hosting.
- [00:18:39](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=18:39) — Amplicon methods, sequencing platforms and the SIGNAL workflow.
- [00:21:59](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=21:59) — Investigating spurious variant calls around indels.
- [00:24:05](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=24:05) — Increasing B.1.1.7 prevalence and the Newfoundland outbreak.
- [00:26:04](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=26:04) — Mutation screening and coordination to investigate newly detected variants.
- [00:29:15](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=29:15) — Consistent variant names and links between lineages, mutations and function.

## In their own words

> So the power of aggregation then would allow us to detect the low and rare mutations in the population before it becomes a problem.
>
> — William Hsiao, [00:27:51](https://soundcloud.com/microbinfie/sars-cov-2-surveillance-in-canada-with-cancogen#t=27:51)

## Who is talking

- **Emma Griffiths** (host)
- **William Hsiao** (guest, Faculty of Health Sciences, Simon Fraser University)
- **Finlay McGuire** (guest, Dalhousie University)
- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

IRIDA, Nextstrain, Microreact, Nextflow, Connor lab Nextflow workflow, Snakemake, SIGNAL, BWA, iVar, FreeBayes, nanostripper, ARTIC protocol, Illumina COVIDSeq, Illumina, Nanopore, Pangolin, Pango lineage nomenclature.

## Questions this episode answers

### What is CANCOGEN's role in Canadian SARS-CoV-2 surveillance?

CANCOGEN coordinates sequencing, data collection and analysis across public health, academic and healthcare partners. Its working groups address areas including metadata, quality control and data analysis, and the network also includes host genome sequencing.

### Why was a complete national SARS-CoV-2 database difficult to assemble?

Provinces had separate health informatics systems and authority over their data. Although national database infrastructure existed, agreements to share provincial sequences were still being established.

### How did the SIGNAL workflow remove human reads without losing viral reads?

McGuire describes competitive mapping against both human and viral references. Reads matching both could be retained when their viral alignment was better, rather than automatically discarding every read that aligned to the human reference.

### How were SARS-CoV-2 variants named in Canada at the time?

The episode describes adoption of Pango lineage names for reporting, with many provinces using Pangolin. The panellists also wanted consistent tracking of individual mutations and their functional evidence, not just lineage labels.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

The Canadians have taken over the podcast !   Join guest host Dr. Emma
Griffiths, as she talks with Dr. Finlay McGuire and Dr. William Hsiao
about the SARS-CoV-2 genomics epidemiology efforts in Canada.
Cancogen website : https://www.genomecanada.ca/en/cancogen
