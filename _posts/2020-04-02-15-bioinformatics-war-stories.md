---
layout: page
title: 'Episode 15: Bioinformatics war stories'
date: '2020-04-02 00:00:00'
link: https://soundcloud.com/microbinfie/15-bioinformatics-war-stories
episode: '15'
soundcloud_track: '727720000'
tags:
- microbinfie
- podcast
description: The hosts recount Listeria pseudo-outbreaks, flow cell faults, contaminated reference databases, Excel mix-ups and a flooded sequencing facility.
excerpt: The hosts recount Listeria pseudo-outbreaks, flow cell faults, contaminated reference databases, Excel mix-ups and a flooded sequencing facility.
headline: 'Bioinformatics war stories: contamination, mix-ups and floods'
guests: []
topics:
- microbial bioinformatics
- listeria
- laboratory contamination
- reference databases
- sequencing quality
- taxonomic classification
- metadata errors
- protocol changes
- sample transport
faq:
- q: What caused the apparent multi-state Listeria outbreak described in the episode?
  a: Lee Katz says the sheep blood used in blood agar was contaminated with Listeria. The team was therefore recovering Listeria from the culture medium itself, creating the appearance of a widespread outbreak.
- q: Why did Shigella samples appear to be Salmonella in Kraken?
  a: Katz describes two Salmonella genomes in the standard Kraken database containing regions shared with Shigella. His team investigated the misleading results in IGV and found large differences between covered and uncovered regions.
- q: How can FASTQ headers help investigate flow cell problems?
  a: The hosts explain that FASTQ headers contain machine, tile and coordinate information. Examining quality by tile or sector can reveal localised drops, such as those associated with a bubble putting the camera out of focus.
- q: What happened when an Excel metadata sheet was sorted incorrectly?
  a: The genome data remained usable, but their associated years, countries and sample identities could no longer be trusted. Some information was reconstructed, while samples whose identities could not be recovered were discarded.
---

*Bioinformatics war stories: contamination, mix-ups and floods*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan share bioinformatics war stories about misleading results and the work needed to explain them. Their examples range from contaminated culture media and reference databases to sequencing faults, unannounced protocol changes and scrambled metadata. The recurring lesson is that sequencing results need scrutiny: problems can originate in the laboratory, software inputs, sample handling or human decisions.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 15: Bioinformatics war stories" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/727720000&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 15: Bioinformatics war stories on SoundCloud](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories)

## In this episode

### An apparent Listeria outbreak in the culture media

Lee Katz recalls the early years of the Listeria real-time WGS project, when results suggested an unusually large outbreak spanning several states. The explanation was contamination in the sheep blood used to make blood agar: the team was growing Listeria from the plate itself as well as from the samples.

Katz identifies a paper in the Journal of Clinical Microbiology as *Two Listeria monocytogenes pseudo outbreaks caused by contaminated laboratory culture and media*. The hosts also recount a forensic parallel: repeated DNA signatures across murder investigations were attributed to contamination from someone making police swabs. Both stories prompt a warning against blindly trusting the sequencing data that comes back.

### Low-diversity sequencing and flow cell bubbles

One host remembers early TraDIS experiments, described as transposon mutagenesis, on the GAII. Adding the same adapter to the front of every DNA fragment meant that every cluster showed the same colour during a cycle, and the sequencer failed. The discussion connects this lack of sequence diversity with the first few bases used for templating; a host recalls a 15-base templating period.

Another recurring fault involved bubbles on flow cells, which put the camera out of focus and degraded the data. Repeated problems in the same tile helped expose the cause. The hosts explain that FASTQ headers contain machine, tile and coordinate information, allowing quality to be examined by location rather than only across the whole sample.

### Contaminated samples and misleading database matches

While working on the Haiti cholera outbreak, Katz was looking at earlier samples just as the idea of using a metagenomics database to check whether every sample matched cholera alone had been introduced. He describes samples from previous studies with roughly 25% or 50% contamination by organisms unrelated to Vibrio, and says the findings were reported in his team's manuscript.

Reference databases can also produce misleading identifications. One host describes Salmonella sequences matching a mountain beetle because bacteria from the beetle's gut had been included in its sequence data. Another recalls a similar mismatch involving Pseudomonas and camels, without knowing how it arose.

Katz then describes Shigella samples repeatedly appearing to be Salmonella when analysed with standard Kraken. The team found two Salmonella genomes in the standard database with regions shared with Shigella. Inspection in IGV revealed a marked disparity between covered and uncovered regions, but tracking down the explanation took considerable time.

### Protocol shortcuts and irrecoverable metadata

In a project involving about 1,000 samples, the first plates looked good before many samples began showing mixed strains. A laboratory worker had changed the protocol without telling the team: instead of picking single colonies and culturing them, they sequenced directly from beads, assuming one bead would contain one organism. Discovering the change required substantial sequencing and investigation, followed by repeating the work.

One host calls human interference with a dataset the worst kind of contamination. Their example is an Excel metadata sheet sorted incorrectly, leaving valid genome data disconnected from trustworthy years, countries and sample identities. Some metadata could be reconstructed, but other samples had to be discarded because the shuffle could not be reversed.

### Sample transport and a flooded sequencing facility

The discussion extends to failures outside the analysis pipeline: refrigerated shipments left warm, and samples potentially compromised when customs staff open lids or seals. One host advocates a secret positive control as a check on whether the material arriving at the other end is what the team expects.

The final story concerns the Sanger Institute's sequencing facility on the River Cam floodplain. A host recalls rising water entering the ground-floor facility through leaks and holes. Staff had to carry heavy, carefully calibrated ABI sequencers upstairs, and the sequencing facility subsequently moved to an upper floor.

## Highlights

- [00:00:00](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=0:00) — Lee Katz introduces the hosts and their microbial bioinformatics work
- [00:02:06](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=2:06) — The paper describing Listeria pseudo-outbreaks caused by contaminated culture media
- [00:02:28](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=2:28) — Early TraDIS experiments on the GAII fail when every cluster shows the same colour
- [00:03:22](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=3:22) — The first few sequencing bases and their role in templating
- [00:04:04](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=4:04) — Using FASTQ header information to investigate tile-specific quality problems
- [00:04:42](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=4:42) — Contamination discovered in earlier samples during Haiti cholera outbreak work
- [00:05:28](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=5:28) — Salmonella matching a mountain beetle because of bacterial sequences in a database
- [00:05:56](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=5:56) — Shigella samples appearing as Salmonella in standard Kraken analysis
- [00:06:38](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=6:38) — An unannounced protocol change produces mixed strains in a 1,000-sample project
- [00:07:30](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=7:30) — An Excel sorting error disconnects genomes from their sample metadata
- [00:08:26](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=8:26) — Sample shipments compromised by temperature and handling
- [00:09:17](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=9:17) — Moving ABI sequencers upstairs as water enters the Sanger sequencing facility

## In their own words

> The worst one was someone missorting an Excel sheet with all the metadata.
>
> — one of the hosts, [00:07:30](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=7:30)

> Once that gets into a database it's hard to get it out again.
>
> — one of the hosts, [00:05:28](https://soundcloud.com/microbinfie/15-bioinformatics-war-stories#t=5:28)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Kraken, Standard Kraken database, IGV, TraDIS, Illumina GAII, ABI sequencers.

## Questions this episode answers

### What caused the apparent multi-state Listeria outbreak described in the episode?

Lee Katz says the sheep blood used in blood agar was contaminated with Listeria. The team was therefore recovering Listeria from the culture medium itself, creating the appearance of a widespread outbreak.

### Why did Shigella samples appear to be Salmonella in Kraken?

Katz describes two Salmonella genomes in the standard Kraken database containing regions shared with Shigella. His team investigated the misleading results in IGV and found large differences between covered and uncovered regions.

### How can FASTQ headers help investigate flow cell problems?

The hosts explain that FASTQ headers contain machine, tile and coordinate information. Examining quality by tile or sector can reveal localised drops, such as those associated with a bubble putting the camera out of focus.

### What happened when an Excel metadata sheet was sorted incorrectly?

The genome data remained usable, but their associated years, countries and sample identities could no longer be trusted. Some information was reconstructed, while samples whose identities could not be recovered were discarded.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We share short war stories about bioinformatics from the trenches of
research. We share tales about a mystery massive Listeria outbreak,
bubbles on flowcells, GAII woes, contaminated databases, the mass
murderer, water pouring into a sequencing centre, changing protocols
without validation, Excel issues and the ultimate complexity in
science - Humans.
