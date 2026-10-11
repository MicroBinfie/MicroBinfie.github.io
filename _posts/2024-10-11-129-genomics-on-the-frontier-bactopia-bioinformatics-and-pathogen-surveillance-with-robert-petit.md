---
layout: page
title: 'Episode 129: Genomics on the Frontier: Bactopia, Bioinformatics, and Pathogen Surveillance with Robert Petit'
date: '2024-10-11 00:00:00'
link: https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit
episode: '129'
soundcloud_track: '1933410251'
tags:
- microbinfie
- podcast
description: Robert Petit on Bactopia, human-read filtering, YAML-based typing and the practicalities of public health genomics in Wyoming.
excerpt: Robert Petit on Bactopia, human-read filtering, YAML-based typing and the practicalities of public health genomics in Wyoming.
headline: Bactopia, bacterial surveillance and bioinformatics in Wyoming
guests:
- Robert Petit
topics:
- bacterial genomics
- pathogen surveillance
- public health bioinformatics
- human-read filtering
- taxonomic classification
- sequence-based typing
- software documentation
- genomic reporting
- wyoming
faq:
- q: Why does Bactopia ask for a genome size?
  a: Robert explains that Bactopia uses genome size to reduce coverage to 100× by default, saving processing time. If no genome size is supplied, it skips that reduction rather than preventing the analysis.
- q: What is Teton intended to do before Bactopia?
  a: Teton combines human-read removal and taxonomic classification for bacterial and viral samples, excluding metagenomic samples in the workflow described. For bacteria, it is intended to generate a Bactopia sample sheet with genome sizes assigned from the classification.
- q: Why filter human reads from bacterial isolate sequencing?
  a: Robert says the laboratory does not expect human DNA in its isolate-derived data. It nevertheless filters the reads routinely to address privacy and security requirements with a concrete processing step.
- q: What reporting improvements are planned for Bactopia?
  a: The Chan Zuckerberg Initiative grant supports visualisation and reporting work, including integration with tools such as MicrobeTrace and Microreact. Robert wants reports suitable for epidemiology colleagues rather than handing them collections of TSV files.
- q: How does CamelHUMP simplify sequence-based typing?
  a: It separates a shared programming framework from typing schemes defined in YAML, with reference sequences supplied in FASTA files. Robert describes this as a way for people without programming expertise to define schemas and for him to maintain one framework instead of three separate tools.
---

*Bactopia, bacterial surveillance and bioinformatics in Wyoming*

Andrew Page talks with Robert Petit of the Wyoming Public Health Laboratory about Bactopia, an end-to-end pipeline for bacterial genomics. They discuss its origins, documentation, human-read filtering and plans for clearer public health reporting, alongside Robert's CamelHUMP project for sequence-based typing. Recorded at the Microbial Bioinformatics Hackathon in Bethesda, Maryland, the conversation also explores genomic surveillance in a sparsely populated state with limited bioinformatics staffing.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 129: Genomics on the Frontier: Bactopia, Bioinformatics, and Pathogen Surveillance with Robert Petit" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1933410251&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 129: Genomics on the Frontier: Bactopia, Bioinformatics, and Pathogen Surveillance with Robert Petit on SoundCloud](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit)

## In this episode

### From Staphopia to Bactopia

Robert introduces Bactopia as an end-to-end pipeline for bacterial genomics, alongside his work on pathogen surveillance at the Wyoming Public Health Laboratory. Its origins lie in Staphopia, a project intended to analyse all available Staph aureus genomes. At the time, Robert recalls, there were only about 700 genomes to process.

Andrew describes running roughly 20 Salmonella genomes through Bactopia and finding the analysis finished about half an hour later. This is his experience rather than a formal performance benchmark. Robert attributes the pipeline's reliability to years of resolving issues and fixing straightforward problems. Andrew also values its ability to identify a pathogen and run pathogen-specific analyses.

### Documentation and coverage reduction

Bactopia's documentation starts inside its configuration files. Robert writes the information there once, then uses a script to convert it into Markdown for the documentation site. He compares this with writing API documentation alongside a function. Andrew highlights the clear layout and examples that users can copy and paste.

Genome size has a practical role in keeping analyses quick. By default, Bactopia reduces coverage to 100×; without a supplied genome size, it skips that reduction and processing takes longer. A batch containing one organism can share a genome-size value, whereas a sequencing run containing 20 different organisms needs a way to assign suitable values to individual samples.

### Teton and human-read filtering

Robert describes Teton as a step intended to run before Bactopia. Named after Wyoming's Grand Tetons, it combines human-read removal with taxonomic classification. The plan is to run it across bacterial and viral samples, rather than metagenomic samples. For bacteria, it would also produce a Bactopia sample sheet with genome sizes assigned from the classification.

For human-read filtering, Robert favours giving users several choices. He discusses the NCBI/SRA human scrubber and Michael Hall's approach using Kraken against a human pangenome, with Hostile as another forthcoming option and Scrubby also mentioned.

The motivation is partly administrative. Their isolate-derived data are not expected to contain human DNA, but explaining that repeatedly to privacy and security colleagues has proved difficult. Routinely filtering the reads gives the laboratory a concrete processing step to report, without relying solely on an explanation of how isolates were prepared.

### Reports for public health colleagues

A Chan Zuckerberg Initiative Essential Open Source Software grant is supporting work on visualisation and reporting for Bactopia. Robert distinguishes between producing substantial analytical output and presenting it in a form that colleagues outside bioinformatics can use. A collection of TSV files is not the report his epidemiology colleagues need.

The planned work includes clearer reports and integration with third-party tools such as MicrobeTrace and Microreact. Andrew identifies this presentation layer as something missing from many analysis tools. The discussion presents these improvements as upcoming work, not as an existing reporting interface: the aim is to make Bactopia's results easier to communicate to the people who need them.

### CamelHUMP and reusable typing schemas

CamelHUMP separates the programming machinery of sequence-based typing from the definition of a typing scheme. Robert wants someone who can describe a schema in YAML to be able to use a shared analysis framework without implementing a new typing program. He describes YAML as readable and says the project uses a standard structure for these definitions.

This also addresses his own maintenance workload. Instead of maintaining three separate typing tools, he can maintain one framework, with each tool represented by two files: a YAML schema and a FASTA file containing the relevant reference sequences.

The name has personal and professional connections. Robert's wife's favourite animal is a camel, and Wyoming has worked with Oman's Central Public Health Laboratory through an Association of Public Health Labs twinning experience. Reciprocal visits between the laboratories made camels a reminder of that collaboration too.

### Public health genomics on the frontier

Robert describes Wyoming as a rural and frontier state covering about 250,000 square kilometres, with only around 600,000 people. He enjoys the small-town setting, scenery, camping and hiking. Andrew also asks about Robert's recognisable colourful shirts, which Robert says he wears all the time.

The staffing picture is more challenging. Robert describes himself as Wyoming's only bioinformatician and says the four other US states in the Northern Plains Consortium also lack a bioinformatician. He nevertheless praises his laboratory colleagues for embracing sequencing and genomic analysis, including working at the command line. The conversation closes at the hackathon in Bethesda, with Andrew and Robert preparing to return to coding.

## Highlights

- [00:00:50](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=0:50) — Robert introduces his Wyoming surveillance work and Bactopia.
- [00:01:24](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=1:24) — Bactopia's origins in Staphopia and an initial collection of about 700 Staph aureus genomes.
- [00:02:32](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=2:32) — Writing documentation once inside Bactopia's configuration files.
- [00:03:24](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=3:24) — Teton: a pre-Bactopia step for human-read removal and taxonomic classification.
- [00:04:27](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=4:27) — Why genome size matters for Bactopia's default reduction to 100× coverage.
- [00:05:17](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=5:17) — Chan Zuckerberg Initiative funding for visualisation, reporting and tool integration.
- [00:06:15](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=6:15) — Human-read filtering choices, including the NCBI scrubber, Kraken and Hostile.
- [00:07:09](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=7:09) — Why the laboratory filters human reads even from isolate-derived data.
- [00:08:14](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=8:14) — CamelHUMP's name, its Oman connection and its YAML-based typing framework.
- [00:11:07](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=11:07) — Andrew asks about living in Wyoming and Robert's colourful shirts.
- [00:13:04](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=13:04) — Bioinformatics staffing gaps in Wyoming and the Northern Plains Consortium.

## In their own words

> But this is just a simple way to remove the human reads, do a quick taxon classification, and then assign a genome size based on that.
>
> — Robert Petit, [00:05:01](https://soundcloud.com/microbinfie/129-genomics-on-the-frontier-bactopia-bioinformatics-and-pathogen-surveillance-with-robert-petit#t=5:01)

## Who is talking

- **Andrew Page** (host)
- **Robert Petit** (guest, Wyoming Public Health Laboratory)
- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Michael Hall.

## Tools and resources mentioned

Bactopia, Staphopia, Teton, NCBI/SRA human scrubber, Kraken, Hostile, Scrubby, MicrobeTrace, Microreact, CamelHUMP.

## Questions this episode answers

### Why does Bactopia ask for a genome size?

Robert explains that Bactopia uses genome size to reduce coverage to 100× by default, saving processing time. If no genome size is supplied, it skips that reduction rather than preventing the analysis.

### What is Teton intended to do before Bactopia?

Teton combines human-read removal and taxonomic classification for bacterial and viral samples, excluding metagenomic samples in the workflow described. For bacteria, it is intended to generate a Bactopia sample sheet with genome sizes assigned from the classification.

### Why filter human reads from bacterial isolate sequencing?

Robert says the laboratory does not expect human DNA in its isolate-derived data. It nevertheless filters the reads routinely to address privacy and security requirements with a concrete processing step.

### What reporting improvements are planned for Bactopia?

The Chan Zuckerberg Initiative grant supports visualisation and reporting work, including integration with tools such as MicrobeTrace and Microreact. Robert wants reports suitable for epidemiology colleagues rather than handing them collections of TSV files.

### How does CamelHUMP simplify sequence-based typing?

It separates a shared programming framework from typing schemes defined in YAML, with reference sequences supplied in FASTA files. Robert describes this as a way for people without programming expertise to define schemas and for him to maintain one framework instead of three separate tools.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Host Andrew Page is joined by Robert Petit from the Wyoming Public Health Laboratory. Robert, a
key developer of the Bactopia pipeline, shares insights into how this end-to-end tool is
transforming bacterial genomic surveillance. They dive into the origins of Bactopia, its
applications in public health, and Robert's experience leading genomic projects in a rural
setting. Discover how Bactopia streamlines pathogen detection, improves documentation, and
integrates with other tools to deliver fast and accurate results.

Listen in as they discuss new innovations in bioinformatics, including visualizations and
human-read filtering, and explore future projects like CamelHUMP, designed to simplify
sequence-based typing. Recorded live at the Microbial Bioinformatics Hackathon in Bethesda,
Maryland, this episode brings you the latest in pathogen genomics and the challenges and
rewards of working on the frontier of public health.
