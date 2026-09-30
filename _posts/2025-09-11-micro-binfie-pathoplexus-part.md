---
layout: page
title: 'Episode 144: Micro binfie Pathoplexus part 1'
date: '2025-09-11 00:00:00'
link: https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part
episode: '144'
soundcloud_track: '2158644894'
tags:
- microbinfie
- podcast
description: How Pathoplexus shares viral genomes, protects publication priority and supports outbreak responses with Nextclade, APIs and links to INSDC.
excerpt: How Pathoplexus shares viral genomes, protects publication priority and supports outbreak responses with Nextclade, APIs and links to INSDC.
headline: 'Pathoplexus: sharing viral genomes without losing credit'
guests:
- Emma Hodcroft
- Theo Sanderson
- Arthur Shem Kasambula
topics:
- viral genomics
- pathogen data sharing
- public health surveillance
- publication priority
- sequence quality control
- data citation
- database interoperability
- ebola
- uganda
faq:
- q: What is Pathoplexus used for?
  a: Pathoplexus is a virus genome database for sharing sequences, finding data by mutations or time period, and downloading sequences for public health and research. Uploaded sequences undergo preprocessing that provides lineage assignments, mutation calls and quality-control information.
- q: Can restricted-use Pathoplexus sequences be used in public dashboards?
  a: Yes. Restricted sequences remain publicly accessible and can support public health and communication, including dashboards, with appropriate credit and identification of the restricted data. Papers and preprints using those sequences require permission during the restricted period, which can last up to one year.
- q: Does Pathoplexus perform full phylogenetic analysis?
  a: The team says full in-house outbreak phylogenetic analysis is not its aim. Pathoplexus provides preprocessing and links selected sequences to external tools; the Nextclade link-out offers quick tree placement.
- q: How quickly do Pathoplexus sequences reach GenBank?
  a: The episode distinguishes availability on Pathoplexus, which can take about five minutes, from onward transfer. The team aims to submit through ENA within one to two days, but reports subsequent INSDC synchronisation times ranging from roughly five days to a month, with delays outside its direct control.
---

*Pathoplexus: sharing viral genomes without losing credit*

Lee Katz and Nabil-Fareed Alikhan, joined by guest host Clint, talk with Emma Hodcroft, Theo Sanderson and Arthur Shem Kasambula about Pathoplexus. They discuss how the viral genome database balances rapid public health access with time for data generators to publish. The conversation covers Nextclade quality control, sequence citation, Uganda's Ebola outbreak, APIs and transfer to INSDC databases.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 144: Micro binfie Pathoplexus part 1" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2158644894&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 144: Micro binfie Pathoplexus part 1 on SoundCloud](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part)

## In this episode

### A home for viral genomes

Pathoplexus is a virus genome database designed for sharing sequences for public health responses and research. Its name combines pathogen with plexus: an interwoven network. Theo describes drag-and-drop submission and searches by mutation and time period, with downloads of the matching sequences.

Emma explains that the platform launched with four pathogens: Ebola Zaire, Ebola Sudan, West Nile virus and Crimean-Congo haemorrhagic fever virus. Researchers were already sharing these sequences through Virological, GitHub and scattered web pages, making them difficult to find. At the time of recording, mpox, RSV and HMPV had been added, with measles expected in the next few days. Further additions depend on evidence of community support, including surveys and letters, rather than public health importance alone.

### Public access with a publication window

The central problem is a tension between rapid sharing and academic credit. Laboratories may hesitate to release sequences if another group could publish first. Pathoplexus offers open-use data, which can be used without asking the submitter, and restricted-use data. For up to one year, restricted data can support public health and communication, but papers or preprints using them require permission.

Restricted does not mean hidden: all the data remain publicly accessible. Users explicitly choose whether to include restricted sequences when downloading, and a metadata column records their status. Emma also confirms that public dashboards and tools such as outbreak.info can use restricted data. Such uses must provide appropriate credit and make it possible to identify the restricted sequences through links back to Pathoplexus.

### Nextclade checks and linked analysis

For the viruses supported at the time, uploading sequences triggers a preprocessing pipeline based on Nextclade. It assigns lineages, calls mutations relative to a reference genome and provides quality-control information, including genome coverage. Submitters see the results within seconds and can decide whether to release the sequences or investigate further. Existing data are also reprocessed as lineage definitions change.

Pathoplexus is not intended to provide a complete in-house phylogenetic analysis for an outbreak. Instead, a recently launched link-out feature sends selected sequences to other websites. Two destinations were available at recording; the one discussed is Nextclade, which offers quick tree placement alongside its other analyses. The team welcomes further web-based tools that could accept sequences directly.

### Credit and experience in Uganda

Theo describes a sequence-set citation system. Authors list the accessions used in a paper, generate a set with an associated DOI and cite that DOI. Citations can then be tracked through Crossref. The team is still developing tools to show data generators which papers used their sequences, so the discussion distinguishes the existing citation mechanism from planned reporting features.

Arthur explains why restricted use can reassure sequencing laboratories in Uganda, particularly when outbreak work leaves little time to prepare publications. He highlights near-real-time characterisation during a recent Ebola outbreak and direct submission to Pathoplexus. Importantly, the teams could submit without constant support from the platform's developers. Arthur also makes clear that he was not part of the team that performed that outbreak's analysis.

### APIs and submission without the web interface

Pathoplexus has separate interfaces for submission and querying. The submission API supports submitting and revising sequences without using the website. The query API uses LAPIS, developed at ETH Zurich and also used by CovSpectrum, to search viral genetic data by mutation patterns, countries, dates and other criteria.

Theo presents interoperability as a practical requirement for an ecosystem of analysis tools: databases need to provide the data those tools require. A command-line interface is also in early development, rather than presented as a finished feature. The discussion connects automated submission with another goal: making it easier for laboratories to move their data into the INSDC databases without relying on manual web forms or email.

### Getting sequences into INSDC

The team says Pathoplexus data ultimately go to the INSDC databases: GenBank, ENA and DDBJ. Pathoplexus submits through ENA because it provides an API. Theo says the team would hope to submit a sequence within one to two days, but subsequent synchronisation between the archives is variable: roughly five days to a month in their experience. Longer cases can require manual follow-up to investigate stalled transfers.

Emma distinguishes those external delays from release on Pathoplexus itself, where a submission can be live in about five minutes. The closing discussion contrasts rapid access during outbreaks with the broader archival role of INSDC. Pathoplexus can focus on near-real-time pathogen data, while the team continues working with the archives to improve onward transfer.

## Highlights

- [00:02:54](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=2:54) — Emma explains the name Pathoplexus and its emphasis on connected pathogen data.
- [00:03:26](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=3:26) — Theo introduces the database, drag-and-drop uploads and sequence searches.
- [00:04:09](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=4:09) — Open and restricted use balance rapid sharing with protection against scooping.
- [00:05:40](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=5:40) — Nextclade preprocessing supplies lineage assignments, mutation calls and quality checks.
- [00:06:56](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=6:56) — Initial pathogen coverage, later additions and community input into new viruses.
- [00:09:42](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=9:42) — Download choices and metadata identify restricted-use sequences.
- [00:10:26](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=10:26) — Public dashboards can use restricted data with appropriate credit.
- [00:11:08](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=11:08) — Sequence sets, DOIs and Crossref provide a route to tracking data reuse.
- [00:12:53](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=12:53) — Arthur discusses sharing incentives and submissions during Uganda's Ebola outbreak.
- [00:15:26](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=15:26) — Link-outs connect selected sequences to external analysis, including Nextclade.
- [00:17:02](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=17:02) — Submission and query APIs support interoperability, with a command-line interface in development.
- [00:19:26](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=19:26) — Submission through ENA and variable synchronisation times across INSDC databases.

## In their own words

> So essentially the worry that if you publish your data soon, someone else could publish a paper on it and you won't get credit for the work that you had to do to get those sequences.
>
> — Emma Hodcroft, [00:04:09](https://soundcloud.com/microbinfie/micro-binfie-pathoplexus-part#t=4:09)

## Who is talking

- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)
- **Clint** (host)
- **Emma Hodcroft** (guest, Swiss Tropical and Public Health Institute)
- **Theo Sanderson** (guest, London School of Hygiene and Tropical Medicine)
- **Arthur Shem Kasambula** (guest)

## Tools and resources mentioned

Pathoplexus, Nextclade, LAPIS, CovSpectrum, GenBank, ENA, DDBJ, outbreak.info, Crossref, GitHub, Nextstrain, Taxonium.

## Questions this episode answers

### What is Pathoplexus used for?

Pathoplexus is a virus genome database for sharing sequences, finding data by mutations or time period, and downloading sequences for public health and research. Uploaded sequences undergo preprocessing that provides lineage assignments, mutation calls and quality-control information.

### Can restricted-use Pathoplexus sequences be used in public dashboards?

Yes. Restricted sequences remain publicly accessible and can support public health and communication, including dashboards, with appropriate credit and identification of the restricted data. Papers and preprints using those sequences require permission during the restricted period, which can last up to one year.

### Does Pathoplexus perform full phylogenetic analysis?

The team says full in-house outbreak phylogenetic analysis is not its aim. Pathoplexus provides preprocessing and links selected sequences to external tools; the Nextclade link-out offers quick tree placement.

### How quickly do Pathoplexus sequences reach GenBank?

The episode distinguishes availability on Pathoplexus, which can take about five minutes, from onward transfer. The team aims to submit through ENA within one to two days, but reports subsequent INSDC synchronisation times ranging from roughly five days to a month, with delays outside its direct control.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Nabil and Lee bring a guest host Clint to talk with some of the people behind Pathoplexus
<http://pathoplexus.org/>

* Dr. Emma Hodcroft - <https://pathoplexus.org/about/eb>
* Dr. Theo Sanderson - <https://pathoplexus.org/about/development-team>
* Mr. Arthur Shem Kasambula - <https://pathoplexus.org/about/development-team>
