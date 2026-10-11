---
layout: page
title: 'Episode 26: SARS-CoV-2 contextual data specification for open genomic epidemiology'
date: '2020-08-13 00:00:00'
link: https://soundcloud.com/microbinfie/26-sars-cov-2-metadata
episode: '26'
soundcloud_track: '870812257'
tags:
- microbinfie
- podcast
description: PHA4GE panellists explain a SARS-CoV-2 metadata specification, repository submissions and how contextual data supports public health surveillance.
excerpt: PHA4GE panellists explain a SARS-CoV-2 metadata specification, repository submissions and how contextual data supports public health surveillance.
headline: SARS-CoV-2 contextual data for open genomic epidemiology
guests:
- Emma Griffiths
- Ruth Timme
- Duncan MacCannell
- Andrew Page
- Nabil-Fareed Alikhan
topics:
- sars-cov-2
- contextual data
- metadata standards
- genomic epidemiology
- public health surveillance
- data interoperability
- controlled vocabularies
- ethical data sharing
- sequence repositories
faq:
- q: What does the PHA4GE SARS-CoV-2 contextual data specification contain?
  a: It includes a collection template for sample, host, exposure, sequencing, bioinformatics and attribution information. Supporting materials include vocabulary guidance, mappings, an SOP and public repository submission protocols.
- q: Does using the specification require sharing all my data?
  a: No. Nabil explains that users can keep data private, share it with trusted partners or submit selected information publicly; the specification provides a consistent structure for those choices.
- q: Is the specification limited to clinical SARS-CoV-2 samples?
  a: Clinical samples are the first priority, but the specification also accommodates environmental sampling, animal hosts and different specimen types. The panel discusses sewage, surfaces and museum animal specimens as examples.
- q: What if a controlled-vocabulary term is missing?
  a: The SOP includes a protocol for sourcing new standardised terms from relevant ontologies. Emma says this is intended to accommodate investigations beyond the examples already covered.
---

*SARS-CoV-2 contextual data for open genomic epidemiology*

Lee Katz talks with Emma Griffiths, Ruth Timme, Duncan MacCannell, Andrew Page and Nabil-Fareed Alikhan about PHA4GE’s SARS-CoV-2 contextual data specification. They explain how a shared structure for sample, host, sequencing and analysis information can make genomic surveillance more interoperable. The discussion covers practical collection templates, public repository submissions, privacy and the distinction between organising data and choosing to share it.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 26: SARS-CoV-2 contextual data specification for open genomic epidemiology" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/870812257&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 26: SARS-CoV-2 contextual data specification for open genomic epidemiology on SoundCloud](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata)

## In this episode

### Why public health needs interoperable data

At the time of recording, Lee reports more than 16 million COVID-19 cases and 600,000 deaths worldwide, with about 12,000 SARS-CoV-2 genomes uploaded to INSDC and 75,000 to GISAID. Those sequence collections do not automatically come with consistent, usable metadata. Duncan describes a wider problem: public health laboratories often lack dedicated bioinformaticians, system administrators or access to cloud resources, making reproducible analysis across laboratories difficult to sustain.

PHA4GE—the Public Health Alliance for Genomic Epidemiology—was established to address openness, interoperability and sustainability in public health bioinformatics. Its working-group structure follows the model of the Global Alliance for Genomics and Health, GA4GH. Eight groups cover areas including data structures, infrastructure, pipelines, training, repositories, users, validation and ethical data sharing. COVID-19 gives that emerging collaboration a concrete problem to tackle.

### Inside the contextual data specification

Ruth describes a data structures working group with 22 members from about nine countries, including participants in SPHERES, the Canadian COVID Genomics Network and COG-UK. Emma explains that information is distributed across sample collectors, sequencing laboratories, bioinformaticians and public health decision-makers. Different formats, privacy concerns and limited staff time make bringing it together difficult.

The specification provides a spreadsheet-based collection template with fields for sample information and processing, sequence identifiers and repository accession numbers, host and exposure information, sequencing and bioinformatics methods, and contributor attribution. Fields are colour-coded as essential or required, highly recommended, or optional, with controlled-vocabulary picklists to support consistency. The package also includes a reference guide, an SOP with instructions and examples, and repository submission protocols on protocols.io. The aim is to organise the information from the outset, rather than reconstruct it when an analysis or submission becomes urgent.

### Building on standards without requiring disclosure

Emma stresses that the specification incorporates existing standards rather than replacing them. Broad, pathogen-agnostic standards do not necessarily supply the SARS-CoV-2 detail or public health guidance the group needs. The package maps its fields to existing standards, including MIxS and MIGS, while the show notes describe it as an extension to the INSDC pathogen package.

The reference guide addresses sharing concerns, including re-identification. Emma explains date jitter: adding or subtracting a day or several days from a collection date. Ruth distinguishes INSDC’s unrestricted data usage from GISAID’s usage restrictions and says the specification maps to both submission formats.

Nabil emphasises that adopting the specification does not require publishing every field. Users can keep information private, exchange it with trusted collaborators or release selected information publicly. The purpose is to make data consistently structured before those sharing decisions arise.

### What context adds to genomic surveillance

Andrew explains why a genome alone is insufficient for many surveillance questions. Collection location and date, host age and exposure information can help investigate introductions into an area or relationships with disease severity. Context turns a sequence collection into something that can support public health decisions.

For COG-UK, he describes weekly uploads to a central UK repository from about 16 sequencing centres. Combining the data allows teams to examine which lineages are circulating in hospitals, care facilities and the community. Multiple lineages can suggest several outbreaks happening at once rather than one expanding outbreak. Shared lineages across care facilities in a wide geographical area can also reveal possible links worth investigating, such as people moving between sites. These are leads for contact tracing, not explanations established by the sequences alone. Andrew frames rapid detection and returning information to contact tracers as important preparation for further infections.

### Beyond clinical samples

Clinical data is the specification’s first priority because it represents most available samples, but Nabil describes a broader scope. Environmental contexts include sewage, door handles and air ventilation shafts. Host information can cover pets, livestock and wild animals, while specimen information can distinguish tissues and materials such as breast milk, saliva and blood. Recording those details supports investigations into viral persistence, environmental contamination and diagnostic sampling.

Ruth adds a museum use case: a global consortium of curators is developing a specification for broad coronavirus surveillance in museum specimens. Historical animal specimens could help researchers investigate background reservoirs. The panel presents this as work being developed, rather than a completed surveillance dataset.

### Extending the vocabulary and starting work

Emma explains that users are not restricted to the vocabulary terms already supplied. The SOP includes instructions for finding new standardised terms in relevant ontologies, recognising that the group cannot anticipate every investigation. Duncan reports adoption by the Canadian sequencing initiative and many US SPHERES laboratories, with implementation being considered in Australia and circulation through SANBI and Africa CDC.

The materials are available through the project’s GitHub repository, including the template, mappings, the SOP and links to submission protocols for NCBI, EBI and GISAID. Duncan recommends downloading the package, reading the preprint and following the SOP. The group wants feedback on unclear instructions, missing documentation and practical obstacles. The show notes provide the preprint alongside the specification and protocols.

## Highlights

- [00:02:07](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=2:07) — Duncan explains the public health bioinformatics gaps that led to PHA4GE.
- [00:07:00](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=7:00) — PHA4GE’s eight working groups and its GA4GH-inspired structure.
- [00:10:32](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=10:32) — Emma introduces the data structures group’s focus on interoperability.
- [00:12:50](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=12:50) — Andrew explains what contextual data adds to genome analysis.
- [00:16:11](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=16:11) — Ruth walks through the template, field priorities, guidance and submission protocols.
- [00:19:02](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=19:02) — How the specification builds on existing standards with a public health focus.
- [00:24:58](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=24:58) — Nabil separates structured data collection from decisions about sharing.
- [00:26:25](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=26:25) — Andrew describes weekly COG-UK surveillance and lineage-based outbreak investigations.
- [00:29:27](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=29:27) — Environmental samples, animal hosts and specimen types beyond clinical surveillance.
- [00:31:23](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=31:23) — Emma explains how users can source additional controlled-vocabulary terms.
- [00:32:20](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=32:20) — Duncan reports adoption and international review of the specification.
- [00:36:12](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=36:12) — Getting started with the materials and providing practical feedback.

## In their own words

> I mean, the real goal is to get different types of information into a single format structured in a standardized way.
>
> — Nabil-Fareed Alikhan, [00:24:58](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=24:58)

> You know, most labs just don't have access to a dedicated team of bioinformaticians.
>
> — Duncan MacCannell, [00:02:07](https://soundcloud.com/microbinfie/26-sars-cov-2-metadata#t=2:07)

## Who is talking

- **Lee Katz** (host)
- **Emma Griffiths** (guest, University of British Columbia)
- **Ruth Timme** (guest, FDA Center for Food Safety and Applied Nutrition)
- **Duncan MacCannell** (guest, CDC Office of Advanced Molecular Detection)
- **Andrew Page** (panellist, Quadram Institute)
- **Nabil-Fareed Alikhan** (panellist, Quadram Institute)

## Tools and resources mentioned

GitHub, protocols.io, GISAID, INSDC, BioSample.

## Questions this episode answers

### What does the PHA4GE SARS-CoV-2 contextual data specification contain?

It includes a collection template for sample, host, exposure, sequencing, bioinformatics and attribution information. Supporting materials include vocabulary guidance, mappings, an SOP and public repository submission protocols.

### Does using the specification require sharing all my data?

No. Nabil explains that users can keep data private, share it with trusted partners or submit selected information publicly; the specification provides a consistent structure for those choices.

### Is the specification limited to clinical SARS-CoV-2 samples?

Clinical samples are the first priority, but the specification also accommodates environmental sampling, animal hosts and different specimen types. The panel discusses sewage, surfaces and museum animal specimens as examples.

### What if a controlled-vocabulary term is missing?

The SOP includes a protocol for sourcing new standardised terms from relevant ontologies. Emma says this is intended to accommodate investigations beyond the examples already covered.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We talk to Dr Emma Griffiths (UBC), Dr Ruth Timme (FDA) and Dr Duncan
MacCannell (CDC) about the PHA4GE SARS-CoV-2 contextual data
specification for open genomic epidemiology.  Paper:
https://www.preprints.org/manuscript/202008.0220/v1  Specification:
https://github.com/pha4ge/SARS-CoV-2-Contextual-Data-Specification
Protocols: https://www.protocols.io/workspaces/pha4ge  The Public
Health Alliance for Genomic Epidemiology (PHA4GE) (https://pha4ge.org)
is a global coalition that is actively working to establish consensus
standards, document and share best practices, improve the availability
of critical bioinformatic tools and resources, and advocate for
greater openness, interoperability, accessibility and reproducibility
in public health microbial bioinformatics. In the face of the current
pandemic, PHA4GE has identified a clear and present need for a fit-
for-purpose, open source SARS-CoV-2 contextual data standard. As such,
we have developed an extension to the INSDC pathogen package,
providing a SARS-CoV-2 contextual data specification based on
harmonisable, publicly available, community standards. The
specification is implementable via a collection template, as well as
an array of protocols and tools to support the harmonisation and
submission of sequence data and contextual information to public
repositories. Well-structured, rich contextual data adds value,
promotes reuse, and enables aggregation and integration of disparate
data sets. Adoption of the proposed standard and practices will better
enable interoperability between datasets and systems, improve the
consistency and utility of generated data, and ultimately facilitate
novel insights and discoveries in SARS-CoV-2 and COVID-19.
