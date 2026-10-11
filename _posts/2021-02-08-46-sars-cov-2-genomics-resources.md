---
layout: page
title: 'Episode 46: SARS-CoV-2 genomics resources'
date: '2021-02-08 00:00:00'
link: https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources
episode: '46'
soundcloud_track: '981548209'
tags:
- microbinfie
- podcast
description: A February 2021 roundup of CoVariants, lineage reports, Microreact, training resources and faster ways to track and share SARS-CoV-2 genomes.
excerpt: A February 2021 roundup of CoVariants, lineage reports, Microreact, training resources and faster ways to track and share SARS-CoV-2 genomes.
headline: 'SARS-CoV-2 genomics resources: variants, dashboards and training'
guests:
- Leonardo de Oliveira Martins
topics:
- sars-cov-2
- variants of concern
- genomic surveillance
- genomic epidemiology
- phylogenetic visualisation
- sampling bias
- bioinformatics training
- targeted pcr
- genomic data sharing
faq:
- q: Which SARS-CoV-2 variant resources were recommended in February 2021?
  a: The panel highlights CoVariants for mutation summaries and country-level distributions, cov-lineages reports for variant spread and travel context, and Microreact for viewing trees, timelines and geographical patterns. These recommendations reflect the resources discussed on 5 February 2021.
- q: What changed in Microreact to help track SARS-CoV-2 variants?
  a: New shortcuts let users jump directly to variants of interest. Microreact also added lineage frequencies as a proportion of samples, helping users distinguish changes in variant representation from changes in the number of samples sequenced.
- q: What training resources does the episode recommend for SARS-CoV-2 genomic analysis?
  a: The CLIMB ARTIC workshop offers practical videos, homework and assignments on analysing ARTIC sequencing data. The CDC’s COVID-19 genomic epidemiology toolkit provides introductory material, including reading phylogenetic trees, which the panel suggests using alongside the workshop.
- q: What are the limitations of variant-specific PCR screening?
  a: Andrew questions whether assays targeting particular lineages could become outdated within a week or two as variants change. Targeting individual mutations might help, but targeted screening does not provide the broader genomic epidemiology available from whole genomes; the panel nevertheless recognises PCR’s value where sequencing resources are limited.
---

*SARS-CoV-2 genomics resources: variants, dashboards and training*

Recorded on 5 February 2021, this roundup brings hosts Lee Katz, Andrew Page and Nabil-Fareed Alikhan together with Leonardo de Oliveira Martins, introduced as head of phylogenomics at the Quadram Institute. They review resources for tracking SARS-CoV-2 variants, interpreting mutations, training analysts and submitting genomes. The discussion connects these tools to practical public health problems: uneven surveillance, rapidly changing variants and the pressure to share results quickly.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 46: SARS-CoV-2 genomics resources" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/981548209&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 46: SARS-CoV-2 genomics resources on SoundCloud](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources)

## In this episode

### Variant catalogues and gaps in surveillance

Nabil-Fareed Alikhan introduces CoVariants, with Emma Hodcroft leading the work. The website brings together variants, their mutations and literature about possible effects, including changes to antibody recognition or spike protein structure. It also plots variant distributions within and between countries using data submitted to GISAID. The panel stresses that there are thousands of variants, and their significance may only become apparent after they have spread.

The cov-lineages reports add another perspective, combining genomic observations with passenger numbers and reports from sources such as local newspapers. The discussion covers B.1.1.7, B.1.351 and P.1, associated in the episode with the UK, South Africa and northern Brazil respectively. Andrew Page describes a period when Poland had substantial passenger traffic from the UK but no recorded B.1.1.7 cases: a warning about surveillance gaps rather than reassurance that the variant was absent. More broadly, the panel cautions that countries doing more sequencing can appear disproportionately affected. They also discuss the tension between rapid public data sharing and researchers’ concerns about acknowledgement or being scooped.

### Microreact makes variant tracking easier

Microreact combines a phylogenetic tree, timeline and geographical display. Nabil describes new shortcuts that let users jump directly to variants of interest, rather than navigate the full SARS-CoV-2 collection. Another update displays a lineage’s frequency as a proportion of all samples, not just its absolute count. That distinction matters when changing sample numbers make a lineage appear to decline. Anthony Underwood and colleagues at CGPS are credited with these developments.

Andrew explains that Microreact regularly imports public COG-UK data, which can make its display more current than data available through GISAID. This is not privileged access to secret data. Users can also upload their own trees and metadata. The hosts are impressed by the scale: hundreds of thousands of genomes, approaching half a million in the discussion.

### Mutation nicknames and targeted screening

The panel discusses N501Y, nicknamed Nelly, and E484K, nicknamed Eek. Andrew describes N501Y as present in the UK, South African and Brazilian variants of concern being discussed. E484K is discussed in connection with B.1.351, P.1 and P.2, and its detection in B.1.1.7. The concern is that these mutations are arising independently in different lineages, which Andrew expects will probably make things slightly worse.

Multiplex PCR protocols offer a more accessible way to screen for variants, but Andrew questions how long lineage-specific assays will remain useful. He asks whether targeting mutations of concern would be more durable, while noting that this loses the broader genomic epidemiology available from whole genomes. Sanger sequencing of part of the spike gene is raised as another possibility. Nabil sees openly shared protocols as useful early progress, following the use of spike gene target failure to detect B.1.1.7. The panel expects RT-qPCR to remain important where sequencing resources are limited.

### Training for analysts and epidemiologists

The CLIMB ARTIC workshop provides online videos, homework and assignments introducing analysis of ARTIC sequencing data. Andrew reports that the course ran for 133 people from more than 30 countries. It brings together developers involved in ARTIC and tools including pangolin, civet and llama, giving learners access to people building the methods used in SARS-CoV-2 analysis.

Lee introduces the CDC’s COVID-19 genomic epidemiology toolkit, a collection of introductory videos intended to help epidemiologists engage with genomic data. The panel mentions material on reading phylogenetic trees and applications in Arizona. They suggest combining this introductory material with the more practical workshop resources to develop well-rounded analysts. Training remains difficult to maintain because methods change quickly and the same experts are occupied with processing and analysing large numbers of samples.

### Scaling sequencing and automating submissions

Denmark provides an example of rapidly expanding sequencing capacity. Andrew describes a compact laboratory running roughly 20–30 MinION instruments simultaneously, helping put Denmark among the leading countries for genomes generated per head of population. The resulting genomic surveillance tracks a rapidly increasing proportion of B.1.1.7. Nabil wonders whether the effort is now getting more support from SSI, which would formalise and amplify it.

The final resource update concerns GISAID’s new command-line/API submission tool. Previously, submitting genomes involved preparing an Excel or CSV metadata file and a separate multi-FASTA sequence file, then uploading them through a web page. Batch uploads were possible, but the process was not programmatic. The new interface allows submissions to be integrated with consensus-sequence generation. Nabil expects easier submission to shorten the delay before genomic information reaches the variant reports and visualisation resources discussed throughout the episode.

## Highlights

- [00:02:30](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=2:30) — CoVariants catalogues variants, mutations and evidence about their possible effects.
- [00:04:45](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=4:45) — Uneven sequencing between countries can distort the apparent distribution of variants.
- [00:05:39](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=5:39) — The trade-off of open data sharing leads into cov-lineages reports and travel-based surveillance gaps.
- [00:10:17](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=10:17) — Microreact adds variant shortcuts and lineage frequencies rather than absolute counts alone.
- [00:14:13](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=14:13) — N501Y and E484K illustrate important mutations appearing across different lineages.
- [00:16:00](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=16:00) — Further mutation nicknames precede an introduction to CLIMB ARTIC workshop resources.
- [00:17:02](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=17:02) — Lee introduces the CDC’s COVID-19 genomic epidemiology training videos.
- [00:18:52](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=18:52) — Variant-specific PCR raises questions about assay lifespan and lost genomic information.
- [00:19:34](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=19:34) — Spike gene target failure and shared PCR protocols are discussed as practical early steps.
- [00:20:49](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=20:49) — Denmark’s rapid sequencing expansion enables genomic tracking of B.1.1.7.
- [00:21:56](https://soundcloud.com/microbinfie/46-sars-cov-2-genomics-resources#t=21:56) — Possible SSI support for Danish sequencing precedes the update on GISAID API submissions.

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Leonardo de Oliveira Martins** (guest, Quadram Institute)

Also mentioned: Emma Hodcroft, Anthony Underwood.

## Tools and resources mentioned

CoVariants, cov-lineages reports, Microreact, GISAID, GISAID CLI/API submission tool, ARTIC, pangolin, civet, llama, Multiplex RT-qPCR, Sanger sequencing, Spike gene target failure, MinION.

## Questions this episode answers

### Which SARS-CoV-2 variant resources were recommended in February 2021?

The panel highlights CoVariants for mutation summaries and country-level distributions, cov-lineages reports for variant spread and travel context, and Microreact for viewing trees, timelines and geographical patterns. These recommendations reflect the resources discussed on 5 February 2021.

### What changed in Microreact to help track SARS-CoV-2 variants?

New shortcuts let users jump directly to variants of interest. Microreact also added lineage frequencies as a proportion of samples, helping users distinguish changes in variant representation from changes in the number of samples sequenced.

### What training resources does the episode recommend for SARS-CoV-2 genomic analysis?

The CLIMB ARTIC workshop offers practical videos, homework and assignments on analysing ARTIC sequencing data. The CDC’s COVID-19 genomic epidemiology toolkit provides introductory material, including reading phylogenetic trees, which the panel suggests using alongside the workshop.

### What are the limitations of variant-specific PCR screening?

Andrew questions whether assays targeting particular lineages could become outdated within a week or two as variants change. Targeting individual mutations might help, but targeted screening does not provide the broader genomic epidemiology available from whole genomes; the panel nevertheless recognises PCR’s value where sequencing resources are limited.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We discuss recent updates to the best SARS-CoV-2 resources, so that
you can stay on top of the latest bioinformatics and genomics tools.
Recorded 5 February 2021.  CoVariants website:  http://covariants.org/
Microreact:  https://microreact.org/project/cogconsortium/ Lineage
reports: https://cov-lineages.org/ CLIMB ARTIC workshop online
resources: https://www.climb.ac.uk/artic-and-climb-big-data-joint-
workshop/ Multiplex PCR for B.1.1.7, B.1.351 and P.1:
https://www.protocols.io/view/multiplexed-rt-qpcr-to-screen-for-sars-
cov-2-b-1-1-brrhm536  CDC videos:
https://www.cdc.gov/amd/training/covid-19-gen-epi-toolkit.html
