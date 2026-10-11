---
layout: page
title: 'Episode 42: Overcoming barriers to SARS-CoV-2 data analysis'
date: '2021-01-20 00:00:00'
link: https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis
episode: '42'
soundcloud_track: '968019349'
tags:
- microbinfie
- podcast
description: A panel on SARS-CoV-2 metadata, within-host variation, public health sequencing and validation of ARTIC, Pangolin and Civet workflows.
excerpt: A panel on SARS-CoV-2 metadata, within-host variation, public health sequencing and validation of ARTIC, Pangolin and Civet workflows.
headline: 'SARS-CoV-2 analysis: metadata, training and validation'
guests:
- Nick Loman
- Andrew Page
- Áine O'Toole
- Will Rowe
- Anna Price
topics:
- sars-cov-2
- genomic surveillance
- sample metadata
- within-host variation
- public health policy
- data sharing
- bioinformatics training
- pipeline validation
- reproducibility
- lineage assignment
faq:
- q: What metadata should a SARS-CoV-2 sequencing programme collect?
  a: The panel recommends collecting the minimum needed for the intended investigation, particularly collection date and location, with other fields chosen for the question being asked. PHA4GE and MAJORA provide specifications to consult rather than reinventing everything locally.
- q: Can ARTIC sequencing be used to study within-host SARS-CoV-2 variation?
  a: Nick says it can, but a single PCR can give unreliable frequency estimates, especially with very little starting material. Repeating PCR three times from the same RNA improved agreement with metagenomics in the work he describes.
- q: How can sequencing teams make the case to policymakers?
  a: The discussion recommends building clinical and public health relationships, explaining the value of local sequencing and analysis, and using the WHO implementation guide to frame the argument. Nick also recommends agreeing public data sharing in the programme's initial protocols.
- q: What training does the panel recommend for bioinformatics beginners?
  a: Suggestions include Nextflow or Snakemake tutorials, Rosalind programming exercises, Edinburgh Genomics courses and basic terminal practice. One of the hosts cautions that short courses do not substitute for experienced staff when delivering operational analyses.
- q: What must be recorded to reproduce a Pangolin lineage analysis?
  a: Record both the Pangolin software version and the dated lineage-model release. Áine explains that historical releases remain available, while updated models can assign different lineages to sequences analysed earlier.
---

*SARS-CoV-2 analysis: metadata, training and validation*

Nick Loman chairs a panel with Andrew Page, Áine O'Toole, Will Rowe and Anna Price at the ARTICnetwork and CLIMB-BIG-DATA workshop held on 14–15 January 2021. They discuss practical barriers to SARS-CoV-2 genomic surveillance, from collecting usable metadata and securing government support to developing bioinformatics skills and validating software. The discussion distinguishes useful public health evidence from technical artefacts and explains why reproducibility requires tracking both software and changing lineage definitions.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 42: Overcoming barriers to SARS-CoV-2 data analysis" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/968019349&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 42: Overcoming barriers to SARS-CoV-2 data analysis on SoundCloud](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis)

## In this episode

### Making sequencing useful locally

Andrew Page describes working with about five hospitals and having sequenced nearly 10,000 SARS-CoV-2 samples. Direct contact with local public health teams and clinicians lets the sequencing team flag unusual clusters and investigate whether hospital cases might be linked. However, the samples clinicians most want investigated are sometimes unavailable or have high Ct values, leaving too little viral material to recover genomes.

Áine O'Toole explains how Civet moved outbreak reporting away from repeated requests for manually prepared trees and into the hands of hospital users. Will Rowe describes the benefits—and bugs—of rapidly developing a shared ARTIC pipeline. Anna Price discusses analysing COG-UK metadata for lineage distributions and importation from England into Wales, highlighting Public Health Wales sequencing more than 2,000 samples in the preceding week.

### Metadata that people can actually supply

Asked for example spreadsheets and sample identifier schemes, Andrew recommends requesting the minimum metadata needed for the investigation. Collection date and location are important; age, gender, healthcare-worker status or illness severity may also be relevant. Asking for hundreds of fields can produce missing information, shortcuts or boilerplate rather than richer evidence.

The administrative burden is substantial: Andrew describes supporting hospitals with around 150 different systems, and one processing change that left four people spending a couple of days tracking down metadata for 200 individuals. Nick points listeners towards two specifications: *The PHA4GE SARS-CoV-2 Contextual Data Specification for Open Genomic Epidemiology* and the metadata described in *MAJORA: Continuous integration supporting decentralised sequencing for SARS-CoV-2 genomic surveillance*. These offer starting points rather than a reason to collect every possible field.

### Within-host variation and technical noise

Nick cautions that, as understood in January 2021, a typical short SARS-CoV-2 infection often provides little useful within-host diversity. Apparent mixed infections can instead reflect contamination or sample mixing. Longer infections offer a different opportunity: he discusses reports lasting up to about 150 days and the then-speculative suggestion that B.1.1.7 emerged during chronic infection. Multiple time points provide stronger evidence than a single sample because mutation frequencies can be tracked.

ARTIC amplicon sequencing can measure within-host variation, but PCR introduces sampling noise, especially at high Ct values with very few starting molecules. Nick describes improved agreement with metagenomics when PCR was repeated three times from the same RNA. He puts Nanopore's error rate at roughly 5% at the time, unevenly distributed across the genome and worse near homopolymers. It was less suitable for discovering variants at 1–3% frequency than for examining variation around 25–50%, particularly at already identified sites.

### Government support and early data-sharing agreements

A participant from the International Livestock Research Institute describes being authorised to test for COVID-19 but facing delays in obtaining permission to sequence samples. The discussion stresses sustained relationships between academics, clinicians and public health authorities. Another participant reports that keeping sequencing local, without sending samples overseas, helped secure support in Trinidad.

Nick recommends establishing public data sharing at the outset, ideally in written sampling and sequencing protocols approved by government. Seeking permission only after sequencing can be harder, particularly when results have political consequences. Local analytical capacity also lets countries interpret their own data rather than depend on inferences from returning travellers. One of the hosts, Nabil-Fareed Alikhan, recommends the WHO report *Genomic sequencing of SARS-CoV-2: a guide to implementation for maximum impact on public health* as material for making the case to policymakers.

### Training, workflow skills and specialist staff

Will recommends Nextflow or Snakemake for learning to build and run workflows, Rosalind exercises for programming practice, and engagement with developers through GitHub issues and discussion channels. Another panellist recommends paid Edinburgh Genomics courses in Python and Linux, and Áine emphasises that basic terminal skills—knowing your directory and finding files—make practical bioinformatics training much more productive.

One of the hosts offers a complementary warning: a short course does not replace years of specialist experience. Hiring someone with established bioinformatics skills can avoid months spent struggling with unfamiliar problems. Nick encourages using existing, tested workflows under operational pressure rather than starting from scratch. Available resources discussed include ARTIC standard operating procedures covering laboratory work, sequencing and initial analysis, plus phylogenetic tutorials developed for Ebola training.

### Validation, releases and reproducible lineage assignments

Áine describes Pangolin's manually curated sequence-to-lineage training labels and ten-fold cross-validation. She reports average assignment accuracy of about 98.6% at the time, while stressing that performance differs between lineages and is affected by missing data. Civet primarily matches sequences to a large tree and summarises information; its inputs come through the grapevine workflow, run daily on CLIMB, and it uses established tools including minimap2.

Nick argues for validating the whole laboratory-to-result process. Examples include positive and negative controls on every run, comparisons between Nanopore and Illumina sequencing, and comparisons between amplicon and metagenomic approaches. Cross-checking pipelines can reveal differences such as missed deletions. Will recommends regression checks, tagged releases, controlled environments and checking build-test results.

Reproducibility also requires recording Pangolin's lineage-model release, not just its software version: assignments made early in 2020 may differ from later ones. Old releases remain available, but freezing everything indefinitely is not a sound operational strategy in a rapidly changing field. The panel also warns that a polished commercial interface does not guarantee valid assumptions or correct results.

## Highlights

- [00:00:52](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=0:52) — Andrew Page on nearly 10,000 sequences and working directly with hospitals and public health teams
- [00:02:19](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=2:19) — Áine O'Toole on Pangolin, Civet and moving outbreak reporting into hospitals
- [00:08:28](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=8:28) — Keeping metadata requests minimal enough for healthcare teams to complete
- [00:18:16](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=18:16) — Why a single sample's within-host variation may reveal artefacts rather than useful signal
- [00:19:30](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=19:30) — Obtaining government approval to sequence samples at the International Livestock Research Institute
- [00:24:15](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=24:15) — Establishing public data sharing before a sequencing programme begins
- [00:28:37](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=28:37) — Learning workflows, practising programming and engaging with software developers
- [00:30:45](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=30:45) — The case for hiring experienced bioinformaticians rather than relying on short courses
- [00:35:36](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=35:36) — How Pangolin's training data and lineage assignments are checked
- [00:38:14](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=38:14) — Validating the complete process with controls and comparisons between sequencing methods
- [00:40:30](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=40:30) — ARTIC regression checks, tagged software releases and controlled environments
- [00:42:34](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=42:34) — Tracking Pangolin software versions separately from lineage-model releases

## In their own words

> Once you've started sharing data it's kind of hard to stop.
>
> — Nick Loman, [00:24:15](https://soundcloud.com/microbinfie/42-overcoming-barriers-to-sars-cov-2-data-analysis#t=24:15)

## Who is talking

- **Nick Loman** (panellist, University of Birmingham)
- **Andrew Page** (panellist, Quadram Institute)
- **Áine O'Toole** (panellist, University of Edinburgh)
- **Will Rowe** (panellist, University of Birmingham)
- **Anna Price** (panellist, MRC CLIMB and Cardiff University)

## Tools and resources mentioned

ARTIC pipeline, ARTIC amplicon sequencing protocol, Pangolin, Civet, grapevine, pangoLEARN, MAJORA, Nextflow, Snakemake, Python, minimap2, Illumina, Oxford Nanopore MinION, Ten-fold cross-validation.

## Questions this episode answers

### What metadata should a SARS-CoV-2 sequencing programme collect?

The panel recommends collecting the minimum needed for the intended investigation, particularly collection date and location, with other fields chosen for the question being asked. PHA4GE and MAJORA provide specifications to consult rather than reinventing everything locally.

### Can ARTIC sequencing be used to study within-host SARS-CoV-2 variation?

Nick says it can, but a single PCR can give unreliable frequency estimates, especially with very little starting material. Repeating PCR three times from the same RNA improved agreement with metagenomics in the work he describes.

### How can sequencing teams make the case to policymakers?

The discussion recommends building clinical and public health relationships, explaining the value of local sequencing and analysis, and using the WHO implementation guide to frame the argument. Nick also recommends agreeing public data sharing in the programme's initial protocols.

### What training does the panel recommend for bioinformatics beginners?

Suggestions include Nextflow or Snakemake tutorials, Rosalind programming exercises, Edinburgh Genomics courses and basic terminal practice. One of the hosts cautions that short courses do not substitute for experienced staff when delivering operational analyses.

### What must be recorded to reproduce a Pangolin lineage analysis?

Record both the Pangolin software version and the dated lineage-model release. Áine explains that historical releases remain available, while updated models can assign different lineages to sequences analysed earlier.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

ARTICnetwork & CLIMB-BIG-DATA present a panel discussion on overcoming
barriers to SARS-CoV-2 data analysis with Nick Loman and Will Rowe
from the University of Birmingham, Áine O'Toole from the University of
Edinburgh, Andrew Page from the Quadram Institute and Anna Price from
MRC CLIMB and Cardiff University. This was part of a workshop on
COVID-19 data analysis.  Topics covered: Collecting sample metadata
intrapatient variability Building bridges with policy makers to start
sequencing Data sharing Improving bioinformatics skills Pipeline and
software validation Bioinformatics reproducibility and quality
Papers: The PHA4GE SARS-CoV-2 Contextual Data Specification for Open
Genomic Epidemiology
https://www.preprints.org/manuscript/202008.0220/v1 MAJORA: Continuous
integration supporting decentralised sequencing for SARS-CoV-2 genomic
surveillance
https://www.biorxiv.org/content/10.1101/2020.10.06.328328v1 Genomic
sequencing of SARS-CoV-2: a guide to implementation for maximum impact
on public health https://www.who.int/publications/i/item/9789240018440
Resources: https://www.climb.ac.uk/artic-and-climb-big-data-joint-
workshop/ https://github.com/SamStudio8/majora
https://soundcloud.com/microbinfie/majora
https://github.com/pha4ge/SARS-CoV-2-Contextual-Data-Specification
https://pha4ge.org/  Software: https://github.com/cov-
lineages/pangolin https://github.com/artic-network/civet
https://github.com/COG-UK/grapevine https://github.com/cov-
lineages/pangoLEARN
