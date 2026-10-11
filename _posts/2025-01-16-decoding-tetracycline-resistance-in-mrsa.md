---
layout: page
title: 'Episode 138: Decoding Tetracycline Resistance in MRSA'
date: '2025-01-16 00:00:00'
link: https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa
episode: '138'
soundcloud_track: '1947875419'
tags:
- microbinfie
- podcast
description: Megan Phillips discusses pT181, tetK and variable tetracycline resistance in Staphylococcus aureus, using public genomes and historical papers.
excerpt: Megan Phillips discusses pT181, tetK and variable tetracycline resistance in Staphylococcus aureus, using public genomes and historical papers.
headline: How a small plasmid shapes tetracycline resistance in MRSA
guests:
- Megan Phillips
topics:
- mrsa
- staphylococcus aureus
- tetracycline resistance
- plasmids
- plasmid copy number
- horizontal gene transfer
- short-read sequencing
- evolution of antimicrobial resistance
faq:
- q: Why can S. aureus isolates carrying pT181 have different tetracycline MICs?
  a: Phillips reports that plasmid-carrying isolates range from susceptible to highly resistant. She suggests that differences in plasmid copy number may contribute, with more copies potentially supporting more TetK efflux pumps.
- q: How does Megan Phillips detect pT181 in short-read genome data?
  a: She uses BLAST with a stringent threshold requiring nearly the entire plasmid to be present. The approximately 4.4 kb plasmid assembles as one contig in the work she describes.
- q: How widespread is pT181 in the genomes discussed?
  a: Phillips reports finding it in more than 30 S. aureus clonal complexes. The metadata she examined indicate a distribution across all continents except Antarctica.
- q: What research was Megan Phillips planning to publish?
  a: She hoped to publish a paper on pT181 evolution covering its spread, copy-number evolution and sequence change. She also described plans to study gene-exchange networks and species-wide patterns of horizontal transfer in S. aureus.
---

*How a small plasmid shapes tetracycline resistance in MRSA*

Andrew Page speaks with Megan Phillips, a PhD student at Emory University, at the microbial genomics hackathon in Bethesda, Maryland. They discuss plasmid-mediated tetracycline resistance in Staphylococcus aureus, including why isolates carrying the same resistance plasmid can have very different minimum inhibitory concentrations. The conversation connects short-read genome analysis, plasmid evolution and gene transfer with historical perspectives on antimicrobial resistance.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 138: Decoding Tetracycline Resistance in MRSA" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1947875419&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 138: Decoding Tetracycline Resistance in MRSA on SoundCloud](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa)

## In this episode

### A resistance plasmid with variable effects

Phillips studies Staphylococcus aureus, an organism she finds particularly useful because of the amount of available data and its varied relationships with hosts. It occurs in humans and animals and can be harmless or cause serious illness. Her current focus is plasmid-mediated tetracycline resistance, particularly the small plasmid pT181.

The plasmid carries tetK, which encodes an efflux pump that moves tetracycline out of the bacterial cell. Yet carrying the plasmid does not correspond to one fixed minimum inhibitory concentration (MIC). Phillips describes isolates that remain susceptible and others with much higher MICs. She suggests that differences in plasmid copy number may partly explain this variation: more copies could allow bacteria to produce more efflux pumps and remove more drug. This is presented as a possible explanation, not a settled result.

### Public genomes and spread across lineages

Rather than concentrating on a single strain, Phillips works mostly with publicly available sequences across genetic backgrounds. The wet-lab work she describes includes primarily CC8 and USA 300 strains, alongside other lineages. She reports finding the plasmid in more than 30 clonal complexes. Available sample metadata place it on every continent except Antarctica.

Phillips argues that this distribution implies at least 30 horizontal transfer events, because the plasmid appears in more than 30 clonal complexes and is much younger than the complexes themselves. She also expects substantial vertical inheritance. The distinction matters to her evolutionary questions: the plasmid can move between lineages, but it can also persist as bacteria pass it to their descendants.

### Detecting pT181 with BLAST

Phillips uses short-read sequencing data to look for the plasmid, which she describes as approximately 4.4 kb long. Her detection approach uses BLAST and a stringent threshold: nearly the entire plasmid must be present before she counts a genome as carrying it. She reports that the plasmid assembles as a single contig.

To choose the threshold, she examined the distribution of BLAST coverage across her genomes. Coverage was concentrated close to the full plasmid length, giving her confidence in setting a cutoff just below that range. Her approach therefore looks for broad coverage of the plasmid rather than simply detecting its resistance gene. The episode describes this presence-detection strategy but does not set out a method for estimating copy number.

### Three genes, integration and treatment context

Phillips describes three genes on the plasmid: tetK for the efflux pump, pre associated with mobilisation, and repC involved in replication. In the conversation the plasmid is described as mobilisable, so it does not need its own complete transfer machinery.

Andrew also asks whether it integrates into the genome. Phillips says this is an area of ongoing work, but notes that the entire plasmid is already known to be integrated into the type 3 methicillin-resistance cassette. The discussion thus considers both the plasmid itself and its presence within a larger resistance element.

On treatment, Phillips emphasises that antibiotic choice depends on infection site and severity. Andrew contrasts topical and bloodstream infections, illustrating why the conversation cannot reduce tetracycline's place in treatment to a single universal sequence.

### Historical papers and the next research questions

Reading about tetracycline resistance has led Phillips back to early antibiotic research. She particularly enjoys a 1948 paper about the discovery of an early tetracycline, praising the poetic language and freedom of expression in older scientific writing. Access has generally been straightforward through her university library.

The conversation also turns to tracing historical samples through chains of papers and personal exchanges. Andrew describes how a sample's provenance can become difficult to establish when each publication points to another researcher. Phillips recognises the same problem: sometimes the trail ends with a statement that a friend supplied the material.

Beyond writing style, Phillips is struck by how early resistance was framed as a narrow biochemical interaction rather than an evolutionary problem. Her planned pT181 paper takes a broader approach, examining spread, copy-number evolution and sequence change. Looking further ahead, she wants to investigate networks of gene exchange and species-wide patterns of horizontal transfer in S. aureus.

## Highlights

- [00:00:46](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=0:46) — Andrew Page introduces the interview from the hackathon in Bethesda
- [00:01:10](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=1:10) — Why Staphylococcus aureus offers varied questions about hosts and disease
- [00:02:02](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=2:02) — Variable tetracycline MICs and the possible role of plasmid copy number
- [00:02:44](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=2:44) — Public genome sequences and wet-lab strains, including CC8 and USA 300
- [00:03:27](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=3:27) — Evidence for horizontal transfer alongside vertical inheritance
- [00:04:22](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=4:22) — The 4.4 kb plasmid and stringent BLAST-based detection
- [00:05:10](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=5:10) — The plasmid's three genes: tetK, pre and repC
- [00:05:49](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=5:49) — Integration into the type 3 methicillin-resistance cassette
- [00:06:15](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=6:15) — Treatment choices depend on infection site and severity
- [00:06:51](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=6:51) — Historical tetracycline papers and a favourite example from 1948
- [00:09:10](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=9:10) — Early resistance research and the neglect of evolutionary explanations
- [00:10:16](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=10:16) — Plans for a pT181 evolution paper and research on gene-exchange networks

## In their own words

> So we definitely see some horizontal transfer, but it can also be vertically inherited and I suspect that's happening a lot too.
>
> — Megan Phillips, [00:03:27](https://soundcloud.com/microbinfie/decoding-tetracycline-resistance-in-mrsa#t=3:27)

## Who is talking

- **Andrew Page** (host)
- **Megan Phillips** (guest, Emory University)
- **Lee Katz** (host)

## Tools and resources mentioned

BLAST.

## Questions this episode answers

### Why can S. aureus isolates carrying pT181 have different tetracycline MICs?

Phillips reports that plasmid-carrying isolates range from susceptible to highly resistant. She suggests that differences in plasmid copy number may contribute, with more copies potentially supporting more TetK efflux pumps.

### How does Megan Phillips detect pT181 in short-read genome data?

She uses BLAST with a stringent threshold requiring nearly the entire plasmid to be present. The approximately 4.4 kb plasmid assembles as one contig in the work she describes.

### How widespread is pT181 in the genomes discussed?

Phillips reports finding it in more than 30 S. aureus clonal complexes. The metadata she examined indicate a distribution across all continents except Antarctica.

### What research was Megan Phillips planning to publish?

She hoped to publish a paper on pT181 evolution covering its spread, copy-number evolution and sequence change. She also described plans to study gene-exchange networks and species-wide patterns of horizontal transfer in S. aureus.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie Podcast, host Andrew Page takes listeners to the heart of
the microbial genomics hackathon in Bethesda, Maryland, for an engaging conversation with
special guest Megan Phillips, a PhD student from Emory University. Megan delves into her
research on Staphylococcus aureus (MRSA), highlighting its fascinating dual nature as both a
harmless and potentially serious pathogen.

Megan discusses the complexities of tetracycline resistance, particularly focusing on plasmid-
mediated mechanisms involving the pt181 plasmid. She explains how this plasmid’s efflux pump,
encoded by the gene tetK, contributes to variable resistance levels and the factors influencing
MIC (Minimum Inhibitory Concentration) variability. Listeners will learn about the intricacies
of plasmid copy numbers, their global spread across clonal complexes, and the occurrence of
horizontal and vertical gene transfer.

Throughout the episode, Megan shares insights on working with short-read sequencing data and
the strategies she employs to detect plasmid presence using tools like BLAST. She also touches
on the challenges and fascinating discoveries of tracking historical sample data and
integrating findings from older research papers, showcasing her appreciation for the poetic
style of scientific writing from the 1940s.

For those interested in antimicrobial resistance, evolutionary microbiology, and the subtleties
of bacterial genome analysis, this episode offers a compelling blend of technical details and
engaging storytelling. Tune in to hear more about Megan’s upcoming publications, her
experiences navigating complex genomic data, and her thoughts on antimicrobial stewardship and
historical perspectives on drug resistance.
