---
layout: page
title: 'Episode 78: StaPH-B: state public health bioinformatics'
date: '2022-03-31 00:00:00'
link: https://soundcloud.com/microbinfie/staph-b-state-public-health
episode: '78'
soundcloud_track: '1232913649'
tags:
- microbinfie
- podcast
description: Erin Young and Kelsey Florek discuss StaPH-B, the Cecret SARS-CoV-2 pipeline and the challenges of scaling public health bioinformatics.
excerpt: Erin Young and Kelsey Florek discuss StaPH-B, the Cecret SARS-CoV-2 pipeline and the challenges of scaling public health bioinformatics.
headline: 'StaPH-B and Cecret: collaboration in public health bioinformatics'
guests:
- Erin Young
- Kelsey Florek
topics:
- public health bioinformatics
- staph-b
- sars-cov-2
- amplicon sequencing
- consensus sequences
- workflow development
- bioinformatics training
- data management
faq:
- q: Who can join StaPH-B?
  a: The guests say membership is open to everyone, not only staff in US state health departments. Its discussions and resources are nevertheless focused on state public health bioinformatics.
- q: What does the Cecret pipeline do?
  a: Cecret maps viral amplicon sequencing reads to a reference, trims primers and produces a consensus sequence. It was developed for Illumina SARS-CoV-2 data and uses BWA as its default aligner.
- q: Can Cecret be used for organisms other than SARS-CoV-2?
  a: Erin says she has tried to make it species-agnostic for viral amplicon sequencing with a reliable reference. Users would need to provide their own reference sequence and primer BED files.
- q: How did COVID-19 sequencing change data management in Wisconsin?
  a: Kelsey describes moving from 50–100 samples for an outbreak to 500–1,000 samples per week. This prompted the laboratory to reconsider how it manages analysis outputs and connects them to public health.
---

*StaPH-B and Cecret: collaboration in public health bioinformatics*

Erin Young and Kelsey Florek join Lee Katz and Nabil-Fareed Alikhan to discuss how StaPH-B connects bioinformaticians across state public health laboratories. They describe its Slack community, shared software and training, before exploring why Erin developed Cecret for SARS-CoV-2 amplicon sequencing. The conversation links workflow development to practical problems: isolated staff, changing analysis requirements and rapidly increasing sample volumes.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 78: StaPH-B: state public health bioinformatics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1232913649&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 78: StaPH-B: state public health bioinformatics on SoundCloud](https://soundcloud.com/microbinfie/staph-b-state-public-health)

## In this episode

### Connecting state public health laboratories

Kelsey describes StaPH-B as a way to connect bioinformaticians working in state public health laboratories, particularly when there were few people in these roles and limited communication between laboratories. At the time of the episode, its Slack workspace was approaching 400 members, with more than 50 channels covering different activities. Erin recalls being the only bioinformatician in her laboratory and valuing access to people facing similar problems.

Membership is open to everyone, although the discussion and resources focus on state public health. Kelsey explains how shared experience helps laboratories adapt CDC methods to their own computing environments and supports projects funded through the NIH, CDC and other agencies.

### Shared software and practical training

For Kelsey, the Slack workspace is StaPH-B's biggest achievement: a place where questions generate conversations and collaborations. GitHub workflows and the Docker project are further examples of laboratories developing shared resources rather than working separately.

Erin stresses that these resources also depend on training. Some contributors made their first Docker image through the community, while the StaPH-B Toolkit and related sessions help people use command-line tools. Monthly videos cover state laboratory projects. Examples discussed include SARS-CoV-2 data submissions, sequence similarity searching and antimicrobial resistance detection. Kelsey identifies accessible communication, contribution guidelines, examples and tutorials as foundations for continuing this work.

### Why Erin built Cecret

Cecret began with a practical need in spring 2020. Erin's laboratory wanted to sequence SARS-CoV-2 using the ARTIC group's primers, but its setup made an Illumina MiSeq approach easier than Nanopore sequencing. The laboratory adapted the sequencing protocol and needed an Illumina-based analysis workflow.

Early tool testing exposed a consensus-generation problem: some approaches inserted detected SNPs but otherwise retained the reference sequence. Erin highlights the value of N bases in consensus sequences. Cecret maps amplicon reads to a reference, trims primers and generates a consensus, using BWA as its default aligner.

Erin has tried to make the workflow species-agnostic. Its intended use is viral amplicon sequencing with a reliable reference; users applying it to another organism would need to supply a reference sequence and primer BED files.

### Why optional features remain

Cecret retains features added when laboratories were still deciding which quality-control metrics and analysis approaches they needed. These include samtools flagstat output and a choice between BWA and minimap2. Erin explains that checking an alternative alignment could provide supporting evidence when a consensus containing a frameshift was rejected during submission to GenBank or GISAID.

The workflow also offers iVar trim or samtools ampliconclip for primer trimming. Erin suspects many users now run the defaults, but has avoided removing options because an unknown user may still depend on them. She describes gradual changes and fewer bugs rather than a dramatic redesign: the core workflow and use case remain similar to summer 2020.

### Other workflows and much larger datasets

Erin discusses alternatives including nf-core's viralrecon and Monroe, a minimap2-based workflow that later became part of Titan. One of the hosts describes using a Nextflow ARTIC pipeline in the UK and recalls the difficulty of building analyses while requirements were still changing. Outputs became more structured as lineage and variant analysis tools were added.

Kelsey identifies a separate challenge in Wisconsin: moving from sequencing 50–100 samples for an outbreak to 500–1,000 samples per week. That shift requires reconsidering not only analysis tools, but also how laboratories manage workflow outputs and connect those data to public health.

### Publishing a workflow and naming it

Erin describes feeling anxious when she made Cecret public on GitHub. She followed repository forks to understand other people's changes, seeking more insight than reports that something was not working. Her aim was a workflow that was both usable and scientifically meaningful. She cannot give a reliable user count and notes that other workflows appear more popular.

The name Cecret came from an acronym associated with a hiking landmark in northern Utah. Erin remembers that the expansion involved COVID and enriched, but could not find where she had written it down after maternity leave. The name remained even though the full expansion was lost.

## Highlights

- [00:01:15](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=1:15) — Why StaPH-B formed and how its Slack community grew
- [00:03:45](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=3:45) — Who can join a community focused on state public health
- [00:07:54](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=7:54) — Slack, GitHub collaborations and the Docker project
- [00:08:54](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=8:54) — Training contributors and sharing command-line skills
- [00:09:51](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=9:51) — Monthly videos and making expertise accessible across laboratories
- [00:12:13](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=12:13) — The Illumina sequencing need that led to Cecret
- [00:15:32](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=15:32) — Retained QC metrics, alternative aligners and primer-trimming options
- [00:17:21](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=17:21) — Cecret usage and alternatives including viralrecon and Titan
- [00:18:09](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=18:09) — A UK Nextflow ARTIC pipeline and rapidly changing requirements
- [00:20:13](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=20:13) — Wisconsin's shift to analysing 500–1,000 samples per week
- [00:21:11](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=21:11) — Publishing Cecret, following forks and responding to feedback
- [00:23:49](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=23:49) — The Utah hiking landmark and forgotten acronym behind Cecret

## In their own words

> I wanted to create something that was usable for everybody, but also something that made sense scientifically and analytically
>
> — Erin Young, [00:21:11](https://soundcloud.com/microbinfie/staph-b-state-public-health#t=21:11)

## Who is talking

- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)
- **Erin Young** (guest, Utah Department of Health)
- **Kelsey Florek** (guest, Wisconsin State Laboratory of Hygiene)

## Tools and resources mentioned

Slack, GitHub, Docker, StaPH-B Toolkit, Cecret, ARTIC protocol, Illumina MiSeq, Nanopore sequencing platform, BWA, minimap2, samtools flagstat, iVar trim, samtools ampliconclip, GenBank, GISAID, nf-core viralrecon, Monroe, Titan, Nextflow, Nextflow ARTIC pipeline.

## Questions this episode answers

### Who can join StaPH-B?

The guests say membership is open to everyone, not only staff in US state health departments. Its discussions and resources are nevertheless focused on state public health bioinformatics.

### What does the Cecret pipeline do?

Cecret maps viral amplicon sequencing reads to a reference, trims primers and produces a consensus sequence. It was developed for Illumina SARS-CoV-2 data and uses BWA as its default aligner.

### Can Cecret be used for organisms other than SARS-CoV-2?

Erin says she has tried to make it species-agnostic for viral amplicon sequencing with a reliable reference. Users would need to provide their own reference sequence and primer BED files.

### How did COVID-19 sequencing change data management in Wisconsin?

Kelsey describes moving from 50–100 samples for an outbreak to 500–1,000 samples per week. This prompted the laboratory to reconsider how it manages analysis outputs and connects them to public health.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Dr. Erin Young and Dr Kelsey Florek join us to talk about StaPH-B, a
US state public health bioinformatics group. They also give some
insights into the popular SARS-CoV-2 pipeline cecret.

- Website: https://staphb.org/
- Cecret Pipeline: https://github.com/CDCgov/SC2CLIA
