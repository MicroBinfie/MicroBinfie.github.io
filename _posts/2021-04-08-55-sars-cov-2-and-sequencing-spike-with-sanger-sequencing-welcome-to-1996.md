---
layout: page
title: 'Episode 55: SARS-CoV-2 And Sequencing Spike With Sanger Sequencing - Welcome To 1995'
date: '2021-04-08 00:00:00'
link: https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996
episode: '55'
soundcloud_track: '1019197834'
tags:
- microbinfie
- podcast
description: Kai Blin and Tue Jorgensen explain rapid SARS-CoV-2 mutation screening with Sanger sequencing and a tested, portable analysis pipeline.
excerpt: Kai Blin and Tue Jorgensen explain rapid SARS-CoV-2 mutation screening with Sanger sequencing and a tested, portable analysis pipeline.
headline: SARS-CoV-2 variant screening with Sanger sequencing
guests:
- Kai Blin
- Tue Jorgensen
topics:
- sars-cov-2
- sanger sequencing
- spike mutations
- variants of concern
- public health surveillance
- contact tracing
- bioinformatics pipelines
- software testing
faq:
- q: How does this Sanger sequencing method screen SARS-CoV-2 samples?
  a: It amplifies a 1,001-base region of spike from samples already positive by qPCR, then obtains one Sanger read per sample. The software checks selected mutation positions and reports a mutation table.
- q: How quickly did the DTU workflow return results?
  a: The guests report an average of about 50–60 hours from swab to results, with the fastest samples taking about 30 hours. These figures include diagnostic testing, RT-PCR, outsourced Sanger sequencing and analysis.
- q: Can this assay replace whole-genome sequencing for lineage identification?
  a: That is not its intended role in the workflow described. Shared mutations and variable read quality can make lineage assignments ambiguous, so the team reports mutations and sends every positive sample for whole-genome sequencing.
- q: Which tools analyse the Sanger sequencing data?
  a: The covid-spike-classification pipeline uses Tracy to basecall AB1 files, Bowtie for reference mapping and SAMtools mpileup to inspect targeted positions. Python code processes the pileup results into the mutation table.
- q: Can the screening assay be updated for new mutations?
  a: New mutation positions within the sequenced region can be added to the software and output table. If another region becomes important or primers stop working, Jorgensen says the laboratory can order and test a different primer set.
---

*SARS-CoV-2 variant screening with Sanger sequencing*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan welcome Kai Blin and Tue Jorgensen from the Technical University of Denmark to discuss SARS-CoV-2 mutation screening using Sanger sequencing. Their method combines a simple laboratory protocol with software that reports mutations in a short region of spike, helping public health teams act before whole-genome sequencing results arrive. Recorded on 12 March 2021, the discussion covers the assay, Denmark’s first confirmed P1 detection, and the software engineering behind the analysis.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 55: SARS-CoV-2 And Sequencing Spike With Sanger Sequencing - Welcome To 1995" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1019197834&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 55: SARS-CoV-2 And Sequencing Spike With Sanger Sequencing - Welcome To 1995 on SoundCloud](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996)

## In this episode

### From antibiotic discovery to COVID-19 screening

Tue Jorgensen normally sequences and compares actinobacterial genomes to identify biosynthetic gene clusters and investigate new antibiotics. Kai Blin develops antiSMASH, which identifies such clusters in microbial genomes, alongside resources including MIBiG and the antiSMASH database. Blin says the public antiSMASH website handles around 100,000 or more jobs a year.

Jorgensen entered COVID-19 work by volunteering in DTU’s testing unit. Around New Year, the guests began discussing a simpler, faster approach to variant screening. They report developing the laboratory and software workflow in less than a week. Since mid-January 2021, it had been applied to all positive samples from their testing unit: initially around 200 a day, falling below 100 by the recording. Samples came mainly from hospitals in the Copenhagen area.

### A single amplicon and one Sanger read

The assay targets a 1,001-base region of the SARS-CoV-2 spike gene. The guests chose the region in early January, initially with B.1.1.7 in mind, because it contained several mutations of interest. They combined the forward primer from one ARTIC primer pair with the reverse primer from another, rather than designing an entirely new primer scheme.

Samples already found positive by qPCR are transferred into 96-well plates for reverse-transcription PCR. The reaction uses the same enzyme mix as the diagnostic qPCR workflow, chosen for accessibility rather than a claim of superior performance. The laboratory was already running about 10,000 reactions a day with that mix.

There is no product purification step. The team takes 1.5 microlitres of PCR product, mixes it with the forward primer and sends it to a commercial Sanger sequencing provider. Results return the following morning. Exactly one read per sample keeps the barcode matching and sample flow simple.

### An early warning for public health

The reported average turnaround is approximately 50–60 hours from swab to mutation results, with the fastest samples taking about 30 hours. This includes diagnostic qPCR, the subsequent RT-PCR, outsourced sequencing and analysis. Blin notes that local Sanger sequencing could shorten the process, while commercial providers make the method accessible without running sequencing in-house.

The guests describe flagging a sample with the hallmark mutations of P1, which was subsequently confirmed as Denmark’s first P1 detection. They alerted the authorities immediately, the person was isolated, and the sample was fast-tracked through whole-genome sequencing. Confirmation followed two days later.

Results go both to the hospitals and to Danish contact-tracing authorities. DTU works with barcodes rather than personal information. The screening sits alongside, rather than replaces, the Nanopore whole-genome sequencing effort discussed in the episode.

### Reporting mutations, not definitive lineages

The immediate priority is identifying mutations that warrant intensified contact tracing, particularly E484K and the mutation at spike position 501. The guests distinguish that operational question from determining an exact lineage or reconstructing transmission. Every positive sample in their setup proceeds to whole-genome sequencing, which supplies more detailed information later.

The software therefore reports a table of mutations rather than definitive variant assignments. Different variants can share the same markers within the sequenced window. Missing calls or an extra apparent mutation make classification harder, particularly near the ends of Sanger reads, where quality can be less reliable. Quality values for the relevant positions were added to the output after the P1 finding.

New mutations can be added as priorities change. The guests give A.23.1 as an example prompted by discussions with researchers working in Africa. Where whole-genome sequencing is less comprehensive, they suggest the assay could help select samples for follow-up.

### From trace files to a mutation table

The covid-spike-classification software starts with AB1 Sanger trace files. Tracy performs basecalling, Bowtie maps the sequence to the reference genome, and SAMtools mpileup extracts information at the mutation positions. Python code then processes those results into the output table.

Rather than processing every possible variant in one operation, the pipeline makes a separate pileup call for each targeted position, examining the three nucleotides of the relevant codon. Blin estimates that the software was checking about 12 positions at the time. He acknowledges that this is not the most computationally efficient design, but it is straightforward to inspect and test. A 96-well plate takes roughly ten seconds to analyse on his machine; Windows execution is slower, but still fast relative to the laboratory workflow.

### Portable software with targeted tests

The hosts highlight the software’s Conda, Docker and Singularity packaging, as well as its tests. Blin connects these choices to lessons from more than a decade of antiSMASH development and his experience in open-source software engineering: getting an initial pipeline working is different from making it robust for routine use.

Tests concentrate on parsing mpileup output, where unexpected details—such as representations of nearby deletions—had caused problems. The code is deliberately defensive and stops when input does not match its expectations, rather than silently continuing. Blin does not claim comprehensive test coverage: much of the pipeline runs external tools whose behaviour he trusts. Adding a mutation position and output column takes about five minutes, followed by roughly ten minutes to deploy a release.

## Highlights

- [00:02:12](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=2:12) — Jorgensen’s usual work sequencing actinobacteria to find new antibiotics
- [00:03:39](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=3:39) — Moving from volunteer COVID-19 testing to a routine Sanger screening workflow
- [00:06:38](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=6:38) — Flagging Denmark’s first P1 sample before whole-genome confirmation
- [00:08:04](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=8:04) — Turnaround times from swab to mutation results
- [00:09:47](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=9:47) — The RT-PCR protocol, shared enzyme mix and commercial Sanger sequencing
- [00:11:04](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=11:04) — Choosing a mutation-rich spike region using existing ARTIC primers
- [00:13:31](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=13:31) — Using exactly one Sanger read per sample to simplify sample tracking
- [00:16:11](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=16:11) — Prioritising mutations that trigger more intensive contact tracing
- [00:18:04](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=18:04) — Reporting mutation tables instead of attempting definitive variant calls
- [00:22:08](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=22:08) — Accessible sequencing and software packaging with Conda and containers
- [00:24:51](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=24:51) — Basecalling AB1 files with Tracy, mapping with Bowtie and extracting pileups
- [00:26:08](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=26:08) — Checking about 12 mutation positions, analysis speed and testing the pileup parser

## In their own words

> we're not actually trying to call the variants right we're basically just calling the mutations
>
> — Kai Blin, [00:18:04](https://soundcloud.com/microbinfie/55-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1996#t=18:04)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Kai Blin** (guest, Technical University of Denmark)
- **Tue Jorgensen** (guest, Technical University of Denmark)

## Tools and resources mentioned

Sanger sequencing, qPCR, Reverse-transcription PCR (RT-PCR), ARTIC protocol, Nanopore sequencing, covid-spike-classification, Tracy, Bowtie, SAMtools mpileup, Conda, Docker, Singularity, antiSMASH, MIBiG, antiSMASH database.

## Questions this episode answers

### How does this Sanger sequencing method screen SARS-CoV-2 samples?

It amplifies a 1,001-base region of spike from samples already positive by qPCR, then obtains one Sanger read per sample. The software checks selected mutation positions and reports a mutation table.

### How quickly did the DTU workflow return results?

The guests report an average of about 50–60 hours from swab to results, with the fastest samples taking about 30 hours. These figures include diagnostic testing, RT-PCR, outsourced Sanger sequencing and analysis.

### Can this assay replace whole-genome sequencing for lineage identification?

That is not its intended role in the workflow described. Shared mutations and variable read quality can make lineage assignments ambiguous, so the team reports mutations and sends every positive sample for whole-genome sequencing.

### Which tools analyse the Sanger sequencing data?

The covid-spike-classification pipeline uses Tracy to basecall AB1 files, Bowtie for reference mapping and SAMtools mpileup to inspect targeted positions. Python code processes the pileup results into the mutation table.

### Can the screening assay be updated for new mutations?

New mutation positions within the sequenced region can be added to the software and output table. If another region becomes important or primers stop working, Jorgensen says the laboratory can order and test a different primer set.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Today we’re going through a new method for identifying variants of
concern using Sanger sequencing, and we’re joined by two of the
authors of this method Kai Blin and Tue Jorgensen, both from the
Technical University of Denmark.   The preprint:
https://www.medrxiv.org/content/10.1101/2021.03.27.21252266v1  The
protocol:  https://www.protocols.io/view/sanger-sequencing-of-a-part-
of-the-sars-cov-2-spik-bsbdnai6  The software:
https://github.com/kblin/covid-spike-classification  The web app:
https://ssi.biolib.com/app/covid-spike-classification/run
