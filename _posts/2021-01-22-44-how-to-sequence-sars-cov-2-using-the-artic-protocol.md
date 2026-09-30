---
layout: page
title: 'Episode 44: How to sequence SARS-CoV-2 using the ARTIC protocol with Joshua Quick'
date: '2021-01-22 00:00:00'
link: https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol
episode: '44'
soundcloud_track: '968531137'
tags:
- microbinfie
- podcast
description: Joshua Quick explains SARS-CoV-2 sequencing with ARTIC, covering primer design, amplicon dropouts, Nanopore barcoding and data quality.
excerpt: Joshua Quick explains SARS-CoV-2 sequencing with ARTIC, covering primer design, amplicon dropouts, Nanopore barcoding and data quality.
headline: Sequencing SARS-CoV-2 with Joshua Quick and the ARTIC protocol
guests:
- Joshua Quick
- Nick Loman
topics:
- sars-cov-2
- artic protocol
- genomic surveillance
- multiplex pcr
- primer design
- nanopore sequencing
- amplicon dropouts
- demultiplexing
- cog-uk
faq:
- q: What Ct range can the ARTIC method work with?
  a: Quick describes recovering complete or partial SARS-CoV-2 genomes from samples with Ct values around 30–35. He also explains that high Ct and degraded input material can increase amplicon dropouts, so this is not a guarantee of complete recovery.
- q: Can more sequencing fix ARTIC amplicon dropouts?
  a: 'Not if the amplicon failed to amplify: additional sequencing cannot recover material that is absent. RAMPART helps users distinguish continuing gains in genome coverage from samples that have reached saturation.'
- q: Why use native rather than rapid Nanopore barcoding for ARTIC?
  a: The workflow requires barcodes at both ends of a read for stringent demultiplexing, whereas rapid barcoding provides only a 5′ barcode. Quick also notes that rapid barcoding fragments the roughly 400-base amplicons further, which can leave reads too short for basecalling under the settings discussed.
- q: Could Primal Scheme design primers for segmented viruses in January 2021?
  a: Segments could be submitted as separate design runs, but the tool would not assess heterodimer formation between primers designed in different runs. Quick described integrated multi-segment design as a planned feature rather than an existing capability.
---

*Sequencing SARS-CoV-2 with Joshua Quick and the ARTIC protocol*

Joshua Quick of the University of Birmingham explains how the ARTIC protocol uses multiplex PCR and Nanopore sequencing to recover SARS-CoV-2 genomes. Recorded at the joint ARTICnetwork and CLIMB-BIG-DATA workshop on 14–15 January 2021, chaired by Nick Loman, the talk places the method within COG-UK's genomic surveillance work. The discussion covers primer design, missing amplicons, sequencing depth and the importance of stringent barcode assignment.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 44: How to sequence SARS-CoV-2 using the ARTIC protocol with Joshua Quick" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/968531137&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 44: How to sequence SARS-CoV-2 using the ARTIC protocol with Joshua Quick on SoundCloud](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol)

## In this episode

### Why ARTIC uses multiplex PCR

Quick describes COG-UK as a decentralised network combining rapid Nanopore sequencing of up to 96 samples with higher-throughput approaches, usually using Illumina sequencing. He distinguishes untargeted metagenomic RNA-seq from two targeted approaches: amplicon sequencing and bait capture. ARTIC's amplicon method is relatively cheap, scales readily and can recover complete or partial SARS-CoV-2 genomes from samples with cycle threshold values around 30–35, even with substantial host material present.

The multiplex approach grew out of work with clinical Zika virus samples in Brazil, where the modal Ct was about 36. Earlier Ebola work had used separate, singleplex RT-PCR reactions. Multiplex PCR offered a way to use less RNA while making the work faster and more suitable for processing many samples.

### Designing overlapping amplicons

Primal Scheme grew from Quick's attempt to reverse-engineer the primer-design principles behind AmpliSeq. The web tool accepts FASTA references and a requested amplicon size. Its updated design process uses parasail to align reference sequences and select conserved primer sites across multiple genomes. A pinned option restricts primer selection to sequences present in the first reference, retaining behaviour closer to the earlier version.

The SARS-CoV-2 scheme generates 96 amplicons across the approximately 30,000-base genome in two reactions. Neighbouring amplicons overlap, but their primers are separated into different pools: putting overlapping neighbours together could favour short, unwanted products. The overlaps also allow synthetic primer sequences to be trimmed during analysis while retaining coverage from adjacent amplicons. Quick stresses that analysis should reflect the viral sequence rather than the synthetic oligonucleotides used to amplify it.

### Dropouts and deciding when to stop

Coverage varies because primer pairs amplify with different efficiencies, while overlapping regions receive reads from neighbouring amplicons. Dropouts are regions with no usable amplification. Quick attributes them to poor primers, mutations at primer-binding sites, high Ct values or degraded input material. Less input cDNA generally means more dropouts and less complete genome recovery.

Sequencing more deeply cannot recover an amplicon that was never produced. Quick describes genome recovery levelling off after roughly 100,000 reads per sample in the example presented, rather than treating additional reads as an automatic route to completeness. RAMPART displays coverage profiles, barcode-associated sample information and progress towards saturation during a run. Those views help users decide whether further sequencing is worthwhile or whether to stop.

### Primer pools and shared protocols

For a newly designed scheme, odd-numbered amplicon primer pairs go into one pool and even-numbered pairs into the other. Quick recommends starting with equimolar pools, sequencing them and then adjusting primer representation using observed coverage across multiple samples. Reaction efficiency cannot be predicted reliably enough to skip that initial assessment. Rebalancing is intended to improve coverage balance and genome completeness.

Quick also describes distributing the version 3 primer pools through IDT following a bulk synthesis arrangement. The low-cost protocol on protocols.io had received more than 100,000 views and around 56 forks. Comments and forks provided a place for troubleshooting and adaptations, although he notes that the platform's versioning is not equivalent to GitHub's. ONT also supported the protocol through technical support.

### Barcoding specificity and direct RNA

The preference for native rather than rapid Nanopore barcoding is not simply about how many barcodes are available. Quick explains that the analysis requires barcodes at both ends of a read for stringent demultiplexing; rapid barcoding supplies only a 5′ barcode. Rapid barcoding also fragments the approximately 400-base amplicons further, potentially producing reads below the roughly 250-base lower limit he cites for Guppy basecalling with standard settings.

Stringent assignment matters because amplicon coverage can differ by two or three orders of magnitude. Reads assigned to the wrong sample could fill an apparent dropout and pass a coverage threshold, producing a variant call where no call should have been made. A high-input sample or positive control could similarly contribute misleading reads to a low-input sample or negative control.

Direct RNA sequencing has different limitations: the kit targets polyadenylated RNA and requires high input amounts. Quick mentions an early Australian proof-of-principle study examining subgenomic RNA and annotating the genome, but describes little wider use for clinical genomic epidemiology at that point.

### Diverse, segmented and bacterial targets

The newer Primal Scheme handles more diverse reference sets better, but it cannot always find conserved primers across very diverse viruses. Quick presents this as a trade-off: the sensitivity of targeted amplification depends on having suitable primer-binding sites. A panellist added that SARS-CoV-2 was a favourable application at the time because its genomes shared a recent common ancestor and relatively little diversity.

Segmented viruses could be handled through separate design runs, but that would miss potential primer interactions across segments. Primal Scheme uses Primer3's thermodynamic engine to assess heterodimer stability within pools. Quick wanted a future multi-input workflow to apply those checks across segments or genes, potentially supporting bacterial cgMLST panels too.

For bacterial targets, high GC content can complicate primer design. The high-GC mode changes permitted primer lengths and other settings; for genomes around 50–55% GC, Quick suggests comparing both modes.

## Highlights

- [00:00:16](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=0:16) — SARS-CoV-2 sequencing approaches across the COG-UK network
- [00:10:54](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=10:54) — Input requirements and other limitations of Nanopore direct RNA sequencing
- [00:12:06](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=12:06) — Preparing two primer pools and rebalancing them using observed coverage
- [00:13:34](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=13:34) — Segmented viruses and the limits of checking primer interactions across separate designs
- [00:15:23](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=15:23) — How reference diversity limits conserved-primer design
- [00:17:17](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=17:17) — Why native barcoding is preferred to rapid barcoding for this workflow
- [00:18:41](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=18:41) — How barcode cross-talk can create misleading coverage and variant calls
- [00:20:41](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=20:41) — Using high-GC mode when designing primers for bacterial targets

## In their own words

> it's not possible to predict the efficiency of the reactions in advance
>
> — Joshua Quick, [00:12:06](https://soundcloud.com/microbinfie/44-how-to-sequence-sars-cov-2-using-the-artic-protocol#t=12:06)

## Who is talking

- **Joshua Quick** (guest, University of Birmingham)
- **Nick Loman** (panellist)

## Tools and resources mentioned

ARTIC protocol, Primal Scheme, RAMPART, parasail, Primer3, Guppy, protocols.io, AmpliSeq, Nanopore sequencing, Illumina sequencing, Nanopore native barcoding, Nanopore rapid barcoding, Nanopore direct RNA sequencing, cgMLST.

## Questions this episode answers

### What Ct range can the ARTIC method work with?

Quick describes recovering complete or partial SARS-CoV-2 genomes from samples with Ct values around 30–35. He also explains that high Ct and degraded input material can increase amplicon dropouts, so this is not a guarantee of complete recovery.

### Can more sequencing fix ARTIC amplicon dropouts?

Not if the amplicon failed to amplify: additional sequencing cannot recover material that is absent. RAMPART helps users distinguish continuing gains in genome coverage from samples that have reached saturation.

### Why use native rather than rapid Nanopore barcoding for ARTIC?

The workflow requires barcodes at both ends of a read for stringent demultiplexing, whereas rapid barcoding provides only a 5′ barcode. Quick also notes that rapid barcoding fragments the roughly 400-base amplicons further, which can leave reads too short for basecalling under the settings discussed.

### Could Primal Scheme design primers for segmented viruses in January 2021?

Segments could be submitted as separate design runs, but the tool would not assess heterodimer formation between primers designed in different runs. Quick described integrated multi-segment design as a planned feature rather than an existing capability.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Joshua Quick from the University of Birmingham talks about "How to
sequence SARS-CoV-2 using the ARTIC protocol". This was part of a
joint ARTICnetwork & CLIMB-BIG-DATA workshop on COVID-19 data analysis
and chaired by Nick Loman.    Links:
https://twitter.com/Scalene/status/1349402397249056779
https://primalscheme.com/
https://www.protocols.io/view/ncov-2019-sequencing-protocol-v3-locost-
bh42j8ye https://github.com/artic-network/rampart
