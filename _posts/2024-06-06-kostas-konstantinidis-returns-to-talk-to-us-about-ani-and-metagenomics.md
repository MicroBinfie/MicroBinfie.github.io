---
layout: page
title: 'Episode 125: Kostas Konstantinidis returns to talk to us about ANI and metagenomics'
date: '2024-06-06 00:00:00'
link: https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics
episode: '125'
soundcloud_track: '1826512452'
tags:
- microbinfie
- podcast
description: Kostas Konstantinidis joins Lee Katz and Andrew Page to discuss soil diversity, Nonpareil, oil-spill microbes and long-read metagenomics.
excerpt: Kostas Konstantinidis joins Lee Katz and Andrew Page to discuss soil diversity, Nonpareil, oil-spill microbes and long-read metagenomics.
headline: Soil metagenomics, Nonpareil and oil-degrading microbes
guests:
- Kostas Konstantinidis
topics:
- soil microbiome
- metagenomics
- sequencing coverage
- oil biodegradation
- biosurfactants
- functional annotation
- long-read sequencing
- horizontal gene transfer
- ani
faq:
- q: What does Nonpareil estimate for a metagenomic sample?
  a: Kostas describes Nonpareil as estimating how much of the microbial DNA in a sample has been represented by sequencing, using redundancy among reads. It also projects the sequencing needed to reach a target coverage.
- q: What did metagenomics reveal during the Gulf of Mexico oil spill?
  a: Microbes that were undetectable before oil reached the beach sand rose to roughly 10–20% of the community during the spill. Genome analysis suggested a possible role for biosurfactants in their success, but that mechanism was still being investigated.
- q: Why check GenBank after using a curated annotation database?
  a: Kostas says curated resources such as SwissProt provide reliable starting points, but newer information may appear in GenBank before reaching curated databases. His lab therefore checks GenBank for functions central to a research question.
- q: Does the episode recommend a particular metagenomic assembler?
  a: No specific assembler or binning package is named. Kostas explains that choices depend on the data and on what works reliably, while acknowledging that many alternative tools exist.
---

*Soil metagenomics, Nonpareil and oil-degrading microbes*

Returning guest Kostas Konstantinidis joins Lee Katz and Andrew Page to discuss what metagenomics can reveal about microbial communities and their responses to environmental change. They cover soil diversity, Nonpareil's sampling estimates, oil-degrading microbes and the practical steps from sequencing to functional hypotheses. The discussion centres on moving beyond cataloguing diversity towards understanding mechanisms that could inform agriculture and oil-spill clean-up.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 125: Kostas Konstantinidis returns to talk to us about ANI and metagenomics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1826512452&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 125: Kostas Konstantinidis returns to talk to us about ANI and metagenomics on SoundCloud](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics)

## In this episode

### Soil microbiomes: beyond cataloguing diversity

Andrew opens with a practical challenge: sequencing soil from a garden could still reveal previously undescribed genera and species. He recalls a postdoc obtaining complete chromosomes from novel organisms while testing MinION sequencing protocols on soil collected around the institute.

Kostas argues that describing every organism is not necessarily the most useful goal. He wants research to explain how soil communities work, adapt to climate change and respond to agricultural practices. Retaining more nitrogen in soil is one potential application. He draws a parallel with efforts to maintain a healthy human microbiome: understanding mechanisms should make it possible to model communities and intervene when needed. He also argues that soil microbiome research deserves more funding.

### Nonpareil and the scale of soil sampling

Nonpareil arose from a question the lab could not readily answer: how much of a sample's microbial DNA had actually been sampled by sequencing? Kostas credits its development to his former student Luis Miguel and places the work around 2013–2014.

The underlying idea is read redundancy. As sequencing captures more of what is present, reads should increasingly overlap information already sampled. Kostas describes Nonpareil as a way to distinguish between very different sampling depths, such as 9% and 99% coverage, and to project how much additional sequencing would be needed to reach a target.

In comparisons involving lakes, the human gut, soils and sediments, soils were the most diverse. The lab estimated that reaching 99% coverage in soil typically required sequencing on the terabase scale.

### An oil spill reveals microbial specialists

Kostas describes sampling Gulf of Mexico beach sand before oil arrived and again while oil was present. At least a couple of microbes that were undetectable beforehand rose to roughly 10–20% of the microbial community during the spill. He interprets this as low-abundance organisms growing rapidly when oil became available.

Metagenomic sequencing allowed the team to assemble a genome and describe a novel candidate taxon. Similarity between some of its genes and genes associated with surfactant production suggested a mechanistic hypothesis: the organisms might release biosurfactants that help them access and degrade oil.

At the time of recording, a US National Science Foundation-funded project was investigating that possibility. Kostas stresses that the work was ongoing: the team had not yet identified a suitable surfactant, but hoped the research could eventually inform oil-spill clean-up.

### From a metagenome to a functional hypothesis

Asked which software connects metagenomic data to a proposed pathway, Kostas resists offering a definitive tool list. Many alternatives exist for each step, and a tool that works reliably in his lab is not necessarily the best available option.

He outlines DNA extraction, sequencing, assembly, binning and subsequent sequence analysis. The oil-spill work used short reads, and he notes that assembly and binning choices depend on the data. No specific assembler or binning package is named.

For functional annotation, the lab starts with curated resources such as SwissProt. For functions of particular interest, it also checks GenBank. Kostas says curated databases provide reliable information but can lag behind newer records. Pipelines can combine the steps, although the workflow is not yet standardised.

### Long reads and the value of fresh samples

Kostas expects long-read technologies to play an increasing role because they can produce more complete, sometimes fully complete, genomes. Extracting enough high-molecular-weight DNA from soils and sediments had previously been a barrier. He points to improved extraction results and reduced input requirements—from a few micrograms to a few nanograms in the examples he discusses—as reasons that barrier is changing.

He also mentions hybrid assembly and binning approaches, without naming individual packages. Andrew highlights another practical advantage of MinION: it can be taken onto a ship or to a beach during an oil spill. He connects field sampling with the value of fresh material, reporting substantial changes in gut microbial communities after freezing.

### Open questions and opportunities to get involved

A continuing research question is how quickly plasmids move between organisms during a disturbance: on the scale of days, months or years? Kostas wants metagenomics to help explain how horizontal transfer contributes to adaptation, alongside changes in community composition.

He invites interested researchers to contact the lab and mentions human microbiome collaborations with CDC, Emory University and partners outside Atlanta. He also flags forthcoming publications on ANI gaps, including gaps within species. This is a brief preview rather than a presentation of those results.

## Highlights

- [00:01:03](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=1:03) — Why ordinary garden soil still presents a major microbial discovery challenge
- [00:01:42](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=1:42) — Moving soil microbiome research from diversity descriptions to mechanisms
- [00:04:35](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=4:35) — Unseen plasmid and phage reservoirs, and complete genomes from local soil
- [00:06:15](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=6:15) — Why the lab developed Nonpareil to estimate metagenomic sampling coverage
- [00:10:21](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=10:21) — Oil-spill sampling reveals microbes rising to 10–20% of the community
- [00:13:54](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=13:54) — Why reliable software choices are not the same as a universal recommendation
- [00:14:53](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=14:53) — The workflow from DNA extraction to annotation with SwissProt and GenBank
- [00:17:26](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=17:26) — Long reads, lower DNA inputs and more complete metagenomic genomes
- [00:19:17](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=19:17) — Taking MinION into the field and preserving the value of fresh samples
- [00:20:28](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=20:28) — Lab opportunities, microbiome collaborations and forthcoming ANI-gap publications

## In their own words

> I'm not sure we need to describe all this diversity, but I think we need to understand what drives it, like the mechanisms.
>
> — Kostas Konstantinidis, [00:01:42](https://soundcloud.com/microbinfie/kostas-konstantinidis-returns-to-talk-to-us-about-ani-and-metagenomics#t=1:42)

## Who is talking

- **Kostas Konstantinidis** (guest)
- **Lee Katz** (host)
- **Andrew Page** (host)

## Tools and resources mentioned

Nonpareil, MinION, SwissProt, GenBank.

## Questions this episode answers

### What does Nonpareil estimate for a metagenomic sample?

Kostas describes Nonpareil as estimating how much of the microbial DNA in a sample has been represented by sequencing, using redundancy among reads. It also projects the sequencing needed to reach a target coverage.

### What did metagenomics reveal during the Gulf of Mexico oil spill?

Microbes that were undetectable before oil reached the beach sand rose to roughly 10–20% of the community during the spill. Genome analysis suggested a possible role for biosurfactants in their success, but that mechanism was still being investigated.

### Why check GenBank after using a curated annotation database?

Kostas says curated resources such as SwissProt provide reliable starting points, but newer information may appear in GenBank before reaching curated databases. His lab therefore checks GenBank for functions central to a research question.

### Does the episode recommend a particular metagenomic assembler?

No specific assembler or binning package is named. Kostas explains that choices depend on the data and on what works reliably, while acknowledging that many alternative tools exist.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

125 Kostas Konstantinidis returns to talk to us about ANI and metagenomics by Microbial
Bioinformatics
