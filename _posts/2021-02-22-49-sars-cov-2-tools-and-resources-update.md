---
layout: page
title: 'Episode 49: SARS-CoV-2 Tools and resources update'
date: '2021-02-22 00:00:00'
link: https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update
episode: '49'
soundcloud_track: '989496307'
tags:
- microbinfie
- podcast
description: Peter van Heusden joins the hosts to discuss SARS-CoV-2 analysis tools, data sharing, CoronaHiT and benchmarks for public health genomics.
excerpt: Peter van Heusden joins the hosts to discuss SARS-CoV-2 analysis tools, data sharing, CoronaHiT and benchmarks for public health genomics.
headline: SARS-CoV-2 tools, data sharing and pipeline benchmarks
guests:
- Peter van Heusden
topics:
- sars-cov-2 genomics
- variant surveillance
- lineage assignment
- sequence alignment
- genomic data sharing
- public health bioinformatics
- pipeline benchmarking
- nanopore sequencing
- data provenance
faq:
- q: What was Nextalign intended to improve for SARS-CoV-2 analysis?
  a: Nextalign provides command-line-friendly alignment functionality from Nextclade, aligning sequences against a reference genome. The panel discusses potentially processing hundreds of thousands of genomes in minutes, but does not present its own benchmark of the new C++ version.
- q: How did COG-UK share sequencing data in the workflow described?
  a: Sites generated reads and consensus sequences locally and sent them by FTP to a central server. Central processing supported phylogenetic analysis and submission to ENA and GISAID, with a turnaround described as a couple of days.
- q: Why is the CoronaHiT dataset useful for benchmarking bioinformatics pipelines?
  a: The same samples were sequenced repeatedly using different platforms and preparation approaches. A pipeline can therefore be tested for whether results from the same sample cluster together; raw reads and consensus sequences were deposited in ENA, although some records were still becoming public.
- q: Why are public SARS-CoV-2 FAST5 benchmark datasets difficult to find?
  a: The panel explains that sequencing can include human reads, which are filtered after basecalling to avoid accidental release. This is offered as a reason relatively little FAST5 data is shared publicly.
---

*SARS-CoV-2 tools, data sharing and pipeline benchmarks*

Peter van Heusden joins Lee Katz, Andrew Page and Nabil-Fareed Alikhan for a SARS-CoV-2 genomics update recorded on 19 February 2021. They review alignment and variant-tracking tools, compare ways of sharing sequencing data, and discuss the gap between research archives and rapid public health reporting. CoronaHiT sequencing and benchmark datasets provide examples of how to test pipelines across platforms.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 49: SARS-CoV-2 Tools and resources update" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/989496307&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 49: SARS-CoV-2 Tools and resources update on SoundCloud](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update)

## In this episode

### Faster alignment and mutation searches

Nextalign brings part of Nextclade’s alignment functionality into a more command-line-friendly form. Peter describes the limitations of browser-based alignment and his earlier workflow wrapper around Nextclade’s Docker container. The panel discusses the prospect of aligning hundreds of thousands of SARS-CoV-2 genomes against a reference on a laptop in minutes, rather than waiting through long MAFFT runs. This is an anticipated benefit: the speakers discussing the new C++ version had not yet tried it.

The COG Mutation Explorer provides a different kind of speed: quickly investigating mutations in UK sequencing data. Users can examine frequencies, recent appearances and occurrence across lineages. The panel relates it to CoV-GLUE and discusses how mutation-frequency information could help assess whether two samples from a suspected reinfection represent different strains.

### Lineage reports and variant maps

Grinch automates reporting for the CovLineages website. The discussion covers reports on B.1.1.7 and other emerging lineages, including countries affected, flight patterns and numbers of genomes in GISAID. These reports can reveal spread before it reaches media coverage, although documentation for the underlying software is still catching up.

The panel also discusses criteria for recognising a new lineage: a supported monophyletic group, epidemiological evidence, circulation within a region and defining mutations. Lee introduces two CDC maps showing variants of concern in the US and worldwide. He stresses that he is not directly involved in their development and appreciates their straightforward presentation.

### Sharing reads, consensus sequences and responsibility

In the COG-UK workflow described here, sequencing sites generate reads and consensus sequences locally, then send them by FTP to a central server. Central processing supports phylogenetic analysis and submission to ENA and GISAID, reportedly within a couple of days. COG-UK also offers single-file downloads updated approximately every three days. GISAID licensing is discussed as a constraint on building derivative resources.

Local processing introduces variation: sites may use old pipeline releases, forked software or entirely different approaches. Bugs and version differences can produce batch effects, so central collection does not automatically guarantee consistent results.

Peter describes similar challenges among collaborators across Africa, compounded by gaps in bioinformatics skills. A Docker Compose-based installation with a web interface is one approach to making local analysis easier. However, consensus sequences and vague methods metadata often leave too little information to reconstruct how a submitted genome was produced or investigate its quality.

### Public health needs more than an archive

Peter distinguishes raw-data archives from systems designed for outbreak response. Waiting for archive accessions and public release is not a practical route to every urgent regional analysis. Local clinicians may need lineage results quickly to inform action or enhanced contact tracing, while national surveillance can inform decisions such as vaccine deployment. Increasing sampling density also creates demand for more geographically specific answers.

The panel considers central clearing houses, local analysis and web services such as Pangolin and Nextclade. Bandwidth, expertise and legal jurisdiction affect which approach is workable. Concerns about inappropriate reuse of data lead one panellist to favour consortium agreements with flexible sharing inside an agreed boundary. A simple upload interface may suit occasional users, while higher-throughput groups need managed workflows.

Routine reporting also requires sustained support. Lee describes transferring part of his foodborne reporting work to a designated team. Commercial provision is suggested as another possible route beyond temporary academic services. Existing MiSeq equipment, training and expertise in the PulseNet and GenomeTrakr networks are discussed as infrastructure supporting the US SARS-CoV-2 response.

### CoronaHiT and cross-platform benchmarks

The newly published CoronaHiT paper in Genome Medicine describes a preparation approach usable with either Nanopore or Illumina sequencing. The hosts report using it for up to 1,500 SARS-CoV-2 samples on Illumina and 96 samples on a single MinION run. A protocol is also available through protocols.io.

Repeated sequencing of the same samples makes the study useful beyond evaluating the laboratory method. The dataset includes roughly 100 samples for each platform or approach, allowing bioinformaticians to check whether results from the same sample cluster together. Raw reads and consensus sequences are deposited in ENA, although some records were still becoming public during preparation of the benchmark resource.

Lee describes work through the Public Health Alliance for Genomic Epidemiology to assemble benchmark datasets. Another available dataset contains three introductions of SARS-CoV-2, providing an outbreak example for testing clustering. The wider discussion concerns standards and user needs, rather than simply encouraging adoption of another newly written pipeline.

### Raw Nanopore data and community work

Peter asks about benchmark FAST5 data for testing ARTIC workflows. The panel contrasts a Medaka route using FASTQ data with a Nanopolish route requiring upstream sequencing data, without settling their relative advantages. Human reads can carry over into sequencing and are filtered after basecalling to avoid accidental release. This is offered as a reason public FAST5 datasets are scarce. Small test datasets in the ARTIC repository are mentioned, but their SARS-CoV-2 content is not confirmed.

The episode closes with plans for the virtual ABPHM conference, costing £100 that year, with an abstract deadline of 9 March. Earlier in the episode, a panellist suggested a documentation-focused hackathon ahead of ABPHM, following an earlier event that worked on testing and GitHub Actions.

## Highlights

- [00:01:32](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=1:32) — Nextalign, Nextclade and moving browser-based alignment to the command line
- [00:02:49](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=2:49) — Using the COG Mutation Explorer to investigate mutation frequencies and lineages
- [00:06:21](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=6:21) — Criteria for deciding whether a sequence cluster represents a new lineage
- [00:08:17](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=8:17) — CDC maps of variants of concern in the US and worldwide
- [00:09:26](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=9:26) — COG-UK’s central collection and submission of reads and consensus sequences
- [00:11:40](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=11:40) — Local analysis, skills gaps and uncertain provenance of consensus sequences
- [00:13:08](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=13:08) — Why raw-data archives are not the same as outbreak-response systems
- [00:20:21](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=20:21) — Moving from academic software development to a reliable reporting service
- [00:24:53](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=24:53) — CoronaHiT publication and reported Illumina and MinION sample capacities
- [00:26:13](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=26:13) — Using repeated cross-platform sequencing to build pipeline benchmarks
- [00:29:36](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=29:36) — Human-read contamination as a barrier to releasing FAST5 data
- [00:30:43](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=30:43) — Plans for the virtual ABPHM conference

## In their own words

> These are archives. These are not outbreak response databases. They're not designed for public health needs.
>
> — Peter van Heusden, [00:13:08](https://soundcloud.com/microbinfie/49-sars-cov-2-tools-and-resources-update#t=13:08)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Peter van Heusden** (guest, South African National Bioinformatics Institute)

## Tools and resources mentioned

Nextalign, Nextclade, MAFFT, COG Mutation Explorer, CoV-GLUE, Grinch, Pangolin, GISAID, ENA, Docker, Docker Compose, GitHub Actions, AWS, Azure, MiSeq, MinION, CoronaHiT, ARTIC, Medaka, Nanopolish.

## Questions this episode answers

### What was Nextalign intended to improve for SARS-CoV-2 analysis?

Nextalign provides command-line-friendly alignment functionality from Nextclade, aligning sequences against a reference genome. The panel discusses potentially processing hundreds of thousands of genomes in minutes, but does not present its own benchmark of the new C++ version.

### How did COG-UK share sequencing data in the workflow described?

Sites generated reads and consensus sequences locally and sent them by FTP to a central server. Central processing supported phylogenetic analysis and submission to ENA and GISAID, with a turnaround described as a couple of days.

### Why is the CoronaHiT dataset useful for benchmarking bioinformatics pipelines?

The same samples were sequenced repeatedly using different platforms and preparation approaches. A pipeline can therefore be tested for whether results from the same sample cluster together; raw reads and consensus sequences were deposited in ENA, although some records were still becoming public.

### Why are public SARS-CoV-2 FAST5 benchmark datasets difficult to find?

The panel explains that sequencing can include human reads, which are filtered after basecalling to avoid accidental release. This is offered as a reason relatively little FAST5 data is shared publicly.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We are joined by Peter van Heusden to discuss all the latest
developments in SARS-CoV-2 genomics, particularly around tools and
resources. We also discuss the challenges of building and sharing data
in large scale sequencing endeavours.  Tools and resources:  Nextalign
github.com/nextstrain/nextclade/releases  COG mutation explorer
http://sars2.cvr.gla.ac.uk/cog-uk/  Grinch https://cov-lineages.org
New US tool for variants:
https://www.cdc.gov/coronavirus/2019-ncov/transmission/variant-
cases.html  https://www.cdc.gov/coronavirus/2019-ncov/cases-
updates/variant-surveillance/global-variant-map.html   Online lineage
assignment: https://pangolin.cog-uk.io/  CoronaHiT paper published: ht
tps://genomemedicine.biomedcentral.com/articles/10.1186/s13073-021-008
39-5
