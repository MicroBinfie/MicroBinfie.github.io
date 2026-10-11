---
layout: page
title: 'Episode 21: Setting up coronavirus sequencing for real-time public health surveillance'
date: '2020-06-16 00:00:00'
link: https://soundcloud.com/microbinfie/coronavirus-sequencing-qib
episode: '21'
soundcloud_track: '839000155'
tags:
- microbinfie
- podcast
description: Justin O'Grady and Andrew Page explain how Quadram set up SARS-CoV-2 sequencing, from ARTIC PCR and contamination to COG-UK data sharing.
excerpt: Justin O'Grady and Andrew Page explain how Quadram set up SARS-CoV-2 sequencing, from ARTIC PCR and contamination to COG-UK data sharing.
headline: Setting up SARS-CoV-2 sequencing for public health surveillance
guests:
- Justin O'Grady
topics:
- sars-cov-2
- covid-19
- cog-uk
- genomic surveillance
- amplicon sequencing
- laboratory contamination
- bioinformatics
- data sharing
- public health
- outbreak investigation
faq:
- q: Why did Quadram use ARTIC PCR rather than metagenomic sequencing?
  a: Justin explains that tiling PCR recovered complete genomes from a wider range of viral loads. Metagenomics could recover genomes from high-viral-load samples but was less sensitive for samples containing less virus.
- q: Did the team reject every SARS-CoV-2 sample above Ct 32?
  a: No. Justin warns that a hard Ct cutoff could bias sample selection and miss biology. He instead suggests considering post-PCR Qubit concentration when deciding whether a sample is worth sequencing.
- q: Why was sharing raw sequencing reads important?
  a: Andrew estimates that only about 20% of genomes submitted to GISAID also reached ENA or SRA at the time. Without underlying reads, researchers could not independently check consensus sequences or perform some forms of reanalysis.
- q: How could SARS-CoV-2 genomes help investigate a care-home or workplace outbreak?
  a: Justin describes using genomes to assess whether multiple cases were consistent with transmission within an institution or separate introductions. That distinction could inform different public health interventions, particularly if sequencing results were available quickly.
---

*Setting up SARS-CoV-2 sequencing for public health surveillance*

Nabil-Fareed Alikhan talks to Andrew Page and Justin O'Grady about establishing SARS-CoV-2 sequencing at the Quadram Institute during the first pandemic wave. Their team generated 1,500 genomes in two months as part of COG-UK. The discussion follows samples from hospital laboratories through amplification, sequencing and bioinformatics, then considers how the resulting genomes could support local outbreak control.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 21: Setting up coronavirus sequencing for real-time public health surveillance" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/839000155&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 21: Setting up coronavirus sequencing for real-time public health surveillance on SoundCloud](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib)

## In this episode

### Building a regional COG-UK effort

COG-UK brought together 16 sequencing sites across England, Scotland, Wales and Northern Ireland, including academic laboratories, public health laboratories and research institutes. Its aim was to build a family tree of SARS-CoV-2: tracing introductions into the UK, spread across the country and outbreaks in settings such as care homes and workplaces.

Andrew received the invitation to participate while on jury service in March. Existing professional connections helped the consortium form unusually quickly, and Justin says sequencing began within about two weeks of the initial contact. Quadram produced 1,500 genomes in two months. Nabil puts that output alongside Norfolk's population of roughly 900,000: one genome for every 600 people.

### Hospital samples, ethics and lockdown staffing

Connections between Quadram, the local medical school and the regional hospital, NNUH, helped the team get started. The NNUH biorepository could collect excess diagnostic samples under its overarching ethical arrangements, allowing work to begin before the study-wide approvals came through COG-UK and Public Health England. It also handled samples, metadata and anonymisation. Justin explains that obtaining patient information required local ethical approval.

Laboratory work depended on volunteers covering sample collection, cDNA production, PCR and sequencing, with bioinformatics following downstream. Andrew recalls about 26 people being involved. Backups mattered because staff could become ill, and the team planned separate laboratory pods so that one group could replace another without everyone being exposed together.

### Why the team chose ARTIC PCR

Justin links the choice of the ARTIC protocol to its sensitivity and specificity, and to the involvement of developers including Josh Quick and Nick Loman in COG-UK. The approach uses 98 primer pairs to generate overlapping amplicons of about 400 bases. He contrasts it with protocols producing 1 kb or 1.2 kb amplicons, which he describes as less sensitive.

Metagenomics had been used to discover the virus, but Justin explains that it would recover fewer complete genomes from low-viral-load samples than tiling PCR. The laboratory workflow took around seven or eight hours from sample to sequencing. Alongside careful sample tracking, contamination control was essential: amplification generated large amounts of coronavirus nucleic acid that then moved through cleanup and library preparation.

### Balancing coverage, sample selection and throughput

Diagnostic qPCR results supplied Ct values as an indication of viral abundance. Justin says ARTIC worked well up to approximately Ct 32–33, which he associates with about 100 viral copies in a sample. Sequencing could still work above that range, but genome coverage declined.

A strict Ct cutoff risked biasing which patients were represented. Instead, Justin suggests measuring nucleic acid concentration with Qubit after ARTIC PCR: samples below about 2 ng/µl might be excluded because they were likely to fail sequencing quality thresholds. This is presented as a practical recommendation, not an absolute rule.

Throughput drove the preference for Illumina over Nanopore. During the April–May peak, the team needed hundreds of samples per week; Andrew reports a largest run of 384 samples.

### From reads to shared consensus genomes

The team coordinated through Discord. Andrew describes Guppy basecalling for Nanopore data and bcl2fastq processing for Illumina data. For Illumina, iVar handled synthetic ARTIC primer sequence so that it would not be mistaken for genuine viral variation. A slightly modified Nextflow pipeline from Tom Connor's laboratory produced consensus sequences and BAM files, followed by checks on genome recovery and coverage.

Amplicon coverage was highly uneven, and genome ends were generally missing. Andrew warns against treating these reads like ordinary sequencing data without accounting for the amplification protocol.

Nabil checked run quality and submitted sequences and metadata to COG-UK, with consensus data subsequently reaching GISAID. The thresholds described in the episode were 90% genome recovery for GISAID and 50% within COG-UK, although the team submitted poorer results too, alongside Ct values. ENA and SRA submission mattered because consensus sequences alone did not allow others to inspect and reanalyse the underlying reads.

### Turning genomes into public health evidence

Justin stresses that producing 1,500 genomes was not enough without using the data. He cites work involving Oliver Pybus that estimated around 1,350 separate introductions into the UK, described as likely to be an underestimate.

Looking ahead from June 2020, the next goal was to work with local county councils and Public Health England on outbreak control. Sequencing could help assess whether cases in a school, care home or factory were consistent with transmission within that setting or with separate introductions. Those interpretations could support different interventions. The team therefore wanted results available as close to real time as possible, backed by accurate patient metadata and reporting.

## Highlights

- [00:00:07](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=0:07) — Introducing the Quadram sequencing effort and its first 1,500 SARS-CoV-2 genomes
- [00:02:08](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=2:08) — COG-UK's 16 sites and the aim of reconstructing viral introductions and spread
- [00:03:13](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=3:13) — How existing connections helped the consortium come together rapidly
- [00:06:21](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=6:21) — How the NNUH biorepository enabled access to excess diagnostic samples
- [00:07:10](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=7:10) — Recruiting laboratory volunteers and organising the sample-to-sequence workflow
- [00:09:59](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=9:59) — Choosing ARTIC and its 98-primer-pair tiling PCR approach
- [00:12:18](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=12:18) — Laboratory processing time, sample tracking and contamination risks
- [00:14:44](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=14:44) — Avoiding Ct-based sampling bias and considering post-PCR Qubit measurements
- [00:16:22](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=16:22) — Why high sample throughput favoured Illumina over Nanopore
- [00:17:33](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=17:33) — Processing reads with Guppy, bcl2fastq, iVar and a Nextflow pipeline
- [00:19:51](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=19:51) — Quality checks, COG-UK submission and onward sharing through GISAID
- [00:25:53](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=25:53) — Using the genomes to study UK introductions and support local outbreak control

## In their own words

> So the tiling PCR approach gives you more complete genomes from more patients.
>
> — Justin O'Grady, [00:11:18](https://soundcloud.com/microbinfie/coronavirus-sequencing-qib#t=11:18)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)
- **Justin O'Grady** (guest, Quadram Institute; University of East Anglia)

Also mentioned: Josh Quick, Nick Loman, Tom Connor, Oliver Pybus.

## Tools and resources mentioned

ARTIC protocol, Qubit, Illumina, Nanopore, Guppy, bcl2fastq, iVar, Nextflow, Discord, GISAID, ENA, SRA.

## Questions this episode answers

### Why did Quadram use ARTIC PCR rather than metagenomic sequencing?

Justin explains that tiling PCR recovered complete genomes from a wider range of viral loads. Metagenomics could recover genomes from high-viral-load samples but was less sensitive for samples containing less virus.

### Did the team reject every SARS-CoV-2 sample above Ct 32?

No. Justin warns that a hard Ct cutoff could bias sample selection and miss biology. He instead suggests considering post-PCR Qubit concentration when deciding whether a sample is worth sequencing.

### Why was sharing raw sequencing reads important?

Andrew estimates that only about 20% of genomes submitted to GISAID also reached ENA or SRA at the time. Without underlying reads, researchers could not independently check consensus sequences or perform some forms of reanalysis.

### How could SARS-CoV-2 genomes help investigate a care-home or workplace outbreak?

Justin describes using genomes to assess whether multiple cases were consistent with transmission within an institution or separate introductions. That distinction could inform different public health interventions, particularly if sequencing results were available quickly.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat to Justin O'Grady and Andrew Page on how to get a SARS-CoV-2
sequencing effort off the ground in the middle of a pandemic and go on
to sequence 1,500 genomes in 2 months. The Quadram institute is one of
16 sequencing centres in the UK which are part of the COVID-19 genome
sequencing consortium. Things we touch off include COG, contamination
issues, the people, and bioinformatics.

Further information from:
https://www.cogconsortium.uk/

If you want to access the sequencing
data produced by Quadram, please checkout the ENA and GISAID.
