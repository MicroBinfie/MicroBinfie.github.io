---
layout: page
title: 'Episode 9: Nobel prize or contamination'
date: '2020-01-09 00:00:00'
link: https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination
episode: '9'
soundcloud_track: '727541380'
tags:
- microbinfie
- podcast
description: How to spot contamination in microbial sequencing with taxonomic checks, assembly metrics and controls, and recognise short- and long-read failures.
excerpt: How to spot contamination in microbial sequencing with taxonomic checks, assembly metrics and controls, and recognise short- and long-read failures.
headline: Nobel prize or contamination? Checking microbial sequence data
guests: []
topics:
- sequencing contamination
- taxonomic classification
- genome assembly
- quality control
- short-read sequencing
- long-read sequencing
- experimental controls
- low-biomass samples
- batch effects
faq:
- q: How can I check whether a bacterial isolate is contaminated?
  a: Compare its taxonomic profile with the expected organism using Kraken or a nearest-reference approach with Mash. The hosts also recommend checking assembly size and contig counts, GC and k-mer patterns, and mixed calls in genes expected to be single-copy.
- q: What does a second peak in a k-mer histogram tell me?
  a: In the episode, multiple peaks are treated as a warning that different components may have been sequenced at different coverages. Lee describes the histogram as a rapid screening tool, not a way to identify the organisms involved.
- q: Can good read-quality scores rule out sequencing problems?
  a: No. The hosts describe samples with acceptable Q-scores and read totals but large coverage gaps, and recommend inspecting mapped reads in IGV or Artemis.
- q: What controls are useful for low-biomass sequencing?
  a: The episode discusses negative controls such as blanks and sterile-media extractions, alongside known positive controls. Controls should be processed with the samples, because kit-derived contamination and batch effects can overwhelm the signal in low-biomass work.
---

*Nobel prize or contamination? Checking microbial sequence data*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss how to distinguish an interesting microbial sequencing result from contamination or a technical failure. They compare taxonomic classifiers, assembly checks, single-copy markers and visual inspection, then work through short- and long-read problems. Their central advice is to check the sample’s identity and build controls into the experiment before interpreting unusual biology.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 9: Nobel prize or contamination" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/727541380&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 9: Nobel prize or contamination on SoundCloud](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination)

## In this episode

### Check what is actually in the sample

For a supposed single isolate, Nabil starts with Kraken for taxonomic classification or Mash to find the closest reference genome. The result should match the expected species, rather than simply accepting the sample label. He gives a rough example of one in 100 samples returning something unexpected, such as Proteus mirabilis or Citrobacter when Salmonella was expected.

Reference databases matter for plate sweeps and metagenomic samples too. Other options discussed include GTDB, MiniKraken, MIDAS, Torsten’s MLST tool and RefSeq Masher. Lee describes gradually building a custom Kalamari database with advice from subject-matter experts at CDC about expected organisms and common contaminants. He favours complete or nearly complete genomes to avoid questionable contigs entering the reference set. At the time of recording, the underlying genomes were not all online, but a compiled database was available to try.

### Assembly checks and single-copy markers

Contamination checks need not begin with a database. For Salmonella sequenced with the Illumina workflows discussed, Nabil expects roughly 200 or fewer contigs and about 4.5 Mb of assembled sequence; 20 Mb or 2,000 contigs would be warning signs. GC plots and k-mer histograms provide checks for inconsistent sequence composition or coverage. Lee describes multiple k-mer peaks as a rapid warning of different sequenced components, not a way to identify them.

FastQC and fastp provide useful read-quality plots. Single-copy markers offer another check: BUSCO, CheckM and MLST with ARIBA are discussed as ways to detect extra copies or mixed allele calls. Lee expects seven alleles at seven loci in his routine MLST checks and mentions beginning similar work with the gp60 gene in Cryptosporidium.

### Look beyond read-quality scores

Andrew recommends inspecting raw FASTQ files or mapping reads to a reference and viewing them in IGV or Artemis. Good Q-scores and an adequate total number of reads can coexist with large coverage gaps. Without inspecting the alignments, missing sequence could be mistaken for an interesting biological property of a strain.

The hosts also discuss coverage that tracks GC content as a sign of bias. Nabil adds a tip about coverage sloping down away from the origin of replication. Lee describes recognising these patterns as something of an art: visual inspection can reveal problems that are impossible to completely automate.

### Carryover, short reads and barcode problems

Carryover from earlier sequencing runs and neighbouring experiments can introduce unexpected organisms. Fixed-tip robots may transfer material between samples despite washing. Human material and Staphylococcus aureus from a person’s skin are other examples. Distinguishing ancient human DNA from DNA belonging to the person handling it illustrates how difficult same-species contamination can be.

On Illumina, the discussion covers over-clustering, reagent failures, broad fragment-size distributions and Ns in the middle of reads. Fragment-size variation can complicate assembly: older mate-pair libraries could contain roughly 3–5 kb fragments alongside a 100–200 bp shadow library. Picard and samtools stats are suggested for inspecting insert-size distributions after mapping. Barcode similarity, sequencing errors and contaminated indexes can cause bleed-through during demultiplexing. The hosts discuss Hamming distance and dual indexing, and recommend examining the report from bcl2fastq when barcode problems are suspected.

### Long reads still depend on the input

Andrew stresses that a long-read library made from 50-base fragments cannot yield long reads. He also cautions against expecting informatics to repair every underlying error: good input material remains essential.

He describes a PacBio run using an early chemistry version in which about 90% of reads were truncated. Diagnosing the failure took time, and the problem was attributed to chemistry rather than wet-lab mistakes. He also discusses overloading wells, which can produce mixed signals, and underloading, which wastes sequencing capacity. A further practical reminder concerns runs requiring refuelling: somebody needs to be on site at the right time.

### Build controls into the experiment

Positive and negative controls belong throughout the workflow, not in a separate run months later. Examples include sequencing a blank, extracting sterile media, checking media by growth, and putting a known organism into a plate well. For an external provider, Andrew recommends placing a control randomly without disclosing its position. Deliberately mixing sequence types, serovars or species across a plate can also reveal a rotation or sample mix-up.

In low-biomass samples, kit-derived contamination can overwhelm the biological signal. Nabil has heard of cases where blanks returned more DNA or taxa than the intended samples; the placenta microbiome is raised as a cautionary example. The hosts warn against confounding comparison groups with sequencing runs, technicians or reagent batches. They recommend mixing groups across batches and processing controls alongside cases from the outset, rather than treating controls as an afterthought.

## Highlights

- [00:01:30](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=1:30) — Checking isolate identity with Kraken and Mash
- [00:04:20](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=4:20) — Testing the single-isolate assumption with database-driven classification
- [00:06:20](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=6:20) — Reference-free checks using assembly size and contig counts
- [00:11:15](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=11:15) — Single-copy genes, BUSCO, CheckM and mixed MLST alleles
- [00:13:47](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=13:47) — Inspecting raw reads and reference alignments by eye
- [00:16:36](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=16:36) — Carryover between experiments and contamination from fixed-tip robots
- [00:20:29](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=20:29) — Over-clustering and short-read signal quality
- [00:27:42](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=27:42) — Barcode similarity, Hamming distance and contaminated indexes
- [00:31:28](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=31:28) — Why short DNA fragments cannot produce long reads
- [00:32:22](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=32:22) — A PacBio chemistry failure that truncated about 90% of reads
- [00:34:50](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=34:50) — Positive and negative controls throughout the workflow
- [00:37:13](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=37:13) — Placenta microbiome claims and batch effects in low-biomass work

## In their own words

> Well, the most fundamental thing is that you can't make long reads if you only have very short DNA fragments.
>
> — Andrew Page, [00:31:28](https://soundcloud.com/microbinfie/09-nobel-prize-or-contamination#t=31:28)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Kraken, Mash, GTDB, MiniKraken, MIDAS, Torsten’s MLST tool, RefSeq Masher, Kalamari, FastQC, fastp, BUSCO, CheckM, ARIBA, MLST, IGV, Artemis, Picard, samtools stats, bcl2fastq, Illumina, PacBio.

## Questions this episode answers

### How can I check whether a bacterial isolate is contaminated?

Compare its taxonomic profile with the expected organism using Kraken or a nearest-reference approach with Mash. The hosts also recommend checking assembly size and contig counts, GC and k-mer patterns, and mixed calls in genes expected to be single-copy.

### What does a second peak in a k-mer histogram tell me?

In the episode, multiple peaks are treated as a warning that different components may have been sequenced at different coverages. Lee describes the histogram as a rapid screening tool, not a way to identify the organisms involved.

### Can good read-quality scores rule out sequencing problems?

No. The hosts describe samples with acceptable Q-scores and read totals but large coverage gaps, and recommend inspecting mapped reads in IGV or Artemis.

### What controls are useful for low-biomass sequencing?

The episode discusses negative controls such as blanks and sterile-media extractions, alongside known positive controls. Controls should be processed with the samples, because kit-derived contamination and batch effects can overwhelm the signal in low-biomass work.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Have you made a nobel prize winning discovery, or are you just looking
at contamination. We discuss common sources of contamination in genome
sequencing, covering both short and long reads.
