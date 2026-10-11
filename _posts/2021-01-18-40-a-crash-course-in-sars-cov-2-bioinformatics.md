---
layout: page
title: 'Episode 40: A crash course in SARS-CoV-2 bioinformatics'
date: '2021-01-18 00:00:00'
link: https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics
episode: '40'
soundcloud_track: '966757894'
tags:
- microbinfie
- podcast
description: 'How to analyse SARS-CoV-2 amplicon data: established pipelines, missing bases, contamination checks, metadata and public health interpretation.'
excerpt: 'How to analyse SARS-CoV-2 amplicon data: established pipelines, missing bases, contamination checks, metadata and public health interpretation.'
headline: 'SARS-CoV-2 bioinformatics: pipelines, QC and common traps'
guests: []
topics:
- sars-cov-2
- amplicon sequencing
- consensus sequences
- quality control
- cross-contamination
- genomic epidemiology
- metadata
- data sharing
- benchmarking
faq:
- q: Which SARS-CoV-2 bioinformatics pipelines do the hosts recommend?
  a: They recommend established ARTIC workflows and the Connor lab's ncov2019-artic-nf workflow for Illumina data. Nabil also recommends ncov-tools for examining BAM files, quality metrics and evidence behind variant calls.
- q: Should missing SARS-CoV-2 consensus bases be filled from the reference?
  a: No. The hosts say unsupported bases should remain placeholders, because reference backfilling introduces information that was not recovered from the sample and can distort comparisons.
- q: What coverage thresholds are discussed for SARS-CoV-2 genomes?
  a: The episode describes a target of 90% confidently called bases, using at least 10× site coverage for Illumina and about 20× for Nanopore. These are the thresholds discussed in January 2021; the hosts also recognise uses for partial genomes in focused investigations.
- q: What should be checked in a SARS-CoV-2 sequencing negative control?
  a: Examine read lengths, how many reads map to the viral reference and how well they align, rather than relying on total read count. Short primer fragments and intact viral reads have different implications, and called variants in a blank raise serious concerns about cross-contamination.
- q: Can identical SARS-CoV-2 genomes identify an outbreak's index case?
  a: Not necessarily. The hosts explain that an outbreak may contain identical genomes, while differences in incubation periods mean the earliest symptomatic person need not be the index case.
---

*SARS-CoV-2 bioinformatics: pipelines, QC and common traps*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss the practical pitfalls of SARS-CoV-2 bioinformatics, from processing amplicon reads to sharing genomes and interpreting outbreaks. Drawing on their public health sequencing work, they explain why a small viral genome still demands careful quality control. Recorded on 13 January 2021, the discussion captures the pipelines, thresholds and data-sharing challenges they were working with at that point in the pandemic.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 40: A crash course in SARS-CoV-2 bioinformatics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/966757894&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 40: A crash course in SARS-CoV-2 bioinformatics on SoundCloud](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics)

## In this episode

### A small genome with unforgiving errors

Moving from roughly five-megabase bacterial genomes to a 30-kilobase SARS-CoV-2 genome initially sounded straightforward. The hosts explain why that expectation failed: viral sequencing, particularly targeted amplicon sequencing, introduces problems that familiar bacterial workflows do not necessarily handle. Coverage can jump from 10× in one region to 10,000× in another, causing difficulties for assemblers.

SARS-CoV-2 also offers little room for casual errors. In the relatively stable genomes discussed here, a single SNP can affect whether samples appear to belong to the same cluster. Synthetic primer sequences must be trimmed or masked rather than allowed to contribute artificial, reference-like bases to the result. Blind assembly or mapping can therefore produce misleading epidemiological conclusions.

### Established pipelines and honest consensus sequences

Andrew recommends starting with established workflows rather than writing another pipeline. ARTIC already had amplicon methods and Nanopore bioinformatics developed for Zika and Ebola, providing a foundation for SARS-CoV-2 analysis. For Illumina data, the hosts use the Connor lab workflow from Wales, linked in the show notes as ncov2019-artic-nf, and discuss its Nextflow implementation.

Nabil highlights ncov-tools for inspecting BAM files, extracting quality metrics and investigating the evidence behind variant calls. It supplied the base-heterogeneity report he had been preparing to write himself. Nabil sees more scope for bespoke reporting than for rebuilding core processing: lineage summaries, geographic displays and detailed sample comparisons serve different audiences.

A central warning concerns missing sequence. Do not replace unsupported positions with reference bases, or simply mutate a reference at called variant sites while retaining everything else. Missing bases should remain placeholders, rather than becoming invented evidence.

### Viral material, coverage and incomplete genomes

Incomplete genomes often reflect insufficient viral material in the original sample, not a bioinformatics problem that can be repaired afterwards. The hosts discuss using PCR cycle-threshold values to guide sequencing decisions. Nabil gives CT32–33 as a rough point beyond which recovering enough genome for reliable phylogenetic analysis becomes difficult, while explicitly noting that the cutoff depends on the protocol.

For public sharing and broad comparative analyses, the discussion uses 90% confidently called bases as a target, with at least 10× coverage at a site for Illumina and about 20× for Nanopore. These are the thresholds described in this January 2021 conversation, not a universal specification.

Partial genomes can still help answer focused questions about reinfection, lineage identity or mutations during a long-term infection. The hosts distinguish those investigations from routine surveillance aimed at producing broadly usable genomes.

### Read filtering and controls that are actually examined

Targeted amplification does not guarantee that every read is viral. The hosts stress removing human reads and checking that apparent SARS-CoV-2 matches are substantial: for 150-base Illumina reads, they want intact or nearly intact alignments, not tiny matching fragments. A sample can yield hundreds of thousands of reads without containing useful coronavirus sequence.

Negative controls need investigation, not just inclusion. A blank may contain short primer-dimer fragments, whereas convincing full-length viral reads raise different concerns. Nabil recommends examining read lengths, mapping quality and the proportion mapping to the reference, then running the blank through variant calling. Called variants in a blank are a serious warning about contamination across the run.

Practical safeguards include allowing zero Illumina barcode mismatches, requiring Nanopore barcodes at both ends and changing index sets between runs. Andrew also warns that a run in which every sample passes should prompt scrutiny rather than automatic celebration.

### Sharing data without losing context or privacy

At recording, the COG-UK website offered about 176,000 genomes, a download of roughly five gigabytes, with minimal metadata and lineage assignments. Andrew describes approximately daily website releases and weekly GISAID uploads, arguing for continuous sharing rather than holding data back.

The hosts contrast GISAID's consensus-genome submissions and additional sharing protections with INSDC archives, which accept raw reads as well as genomes. They discuss the complexity of linked projects, samples, experiments, reads and assemblies, and point to submission walkthroughs in the PHA4GE SARS-CoV-2 metadata specification. Consistent metadata remains a major limitation.

Sample identifiers need equal care. COG-UK uses a sequencing-centre prefix, such as NORW for Norwich, plus a consortium-wide unique suffix. Identifiers should be readable, manageable in scripts and free of patient identifiers. The hosts warn against punctuation that breaks file formats and ambiguous characters that complicate manual transcription.

### Benchmarks and decisions in the real world

Lee describes a draft simulated benchmark, linked as SARS-CoV-2-trueTree, containing about 3,500 simulated assemblies. Starting with a fixed tree and a Wuhan 1 anchor genome, the simulation introduces SNPs so that an ideal analysis would reconstruct the chosen tree. He cautions that those SNPs do not necessarily represent biological processes. Andrew proposes a complementary end-to-end test: send laboratories 12 physical samples and compare their sequencing results. The discussion identifies Wuhan 1, GenBank MN908947, as the established reference.

For operational surveillance, Andrew emphasises recent samples: the UK work described prioritises specimens collected within three weeks, ideally within one week. Hospital, prison and factory examples show how genomic evidence can distinguish multiple introductions from a shared outbreak and inform screening, ward closures or cleaning.

The limits matter too. Identical genomes cannot necessarily reveal who infected whom or identify the index case. Genomics can also provide reassurance by supporting separate community introductions rather than transmission within a ward.

## Highlights

- [00:02:36](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=2:36) — Why moving from bacterial genomes to a 30 kb virus was not straightforward
- [00:05:38](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=5:38) — ARTIC's existing workflows and adapting analysis for Illumina data
- [00:06:57](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=6:57) — Why unsupported bases must not be backfilled from the reference
- [00:11:05](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=11:05) — Removing human reads from targeted amplicon sequencing data
- [00:14:27](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=14:27) — Nextflow workflows, ncov-tools and the remaining scope for bespoke reporting
- [00:21:15](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=21:15) — Insufficient viral material and choosing cycle-threshold cutoffs
- [00:27:24](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=27:24) — Interpreting primer fragments, viral reads and variant calls in negative controls
- [00:32:26](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=32:26) — Continuous COG-UK data releases rather than holding genomes back
- [00:35:39](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=35:39) — GISAID, INSDC and the need for consistent metadata
- [00:39:49](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=39:49) — Lee's draft simulated benchmark built around a known tree
- [00:42:46](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=42:46) — Designing readable, unique and anonymised sample identifiers
- [00:49:57](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=49:57) — Using genomes to investigate hospital and factory outbreaks

## In their own words

> The world has been doing this for a year and you don't need yet another pipeline.
>
> — Andrew Page, [00:13:39](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=13:39)

> if the base isn't supported, you just put a placeholder and you just leave it.
>
> — Nabil-Fareed Alikhan, [00:06:57](https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics#t=6:57)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

ARTIC pipelines, ncov2019-artic-nf, Nextflow, ncov-tools, BLAST, SAMtools, pangolin, Microreact, R, matplotlib, NumPy, SciPy, GISAID, INSDC, ENA, NCBI, GenBank, Illumina, Nanopore, PacBio, Ion Torrent, PCR.

## Questions this episode answers

### Which SARS-CoV-2 bioinformatics pipelines do the hosts recommend?

They recommend established ARTIC workflows and the Connor lab's ncov2019-artic-nf workflow for Illumina data. Nabil also recommends ncov-tools for examining BAM files, quality metrics and evidence behind variant calls.

### Should missing SARS-CoV-2 consensus bases be filled from the reference?

No. The hosts say unsupported bases should remain placeholders, because reference backfilling introduces information that was not recovered from the sample and can distort comparisons.

### What coverage thresholds are discussed for SARS-CoV-2 genomes?

The episode describes a target of 90% confidently called bases, using at least 10× site coverage for Illumina and about 20× for Nanopore. These are the thresholds discussed in January 2021; the hosts also recognise uses for partial genomes in focused investigations.

### What should be checked in a SARS-CoV-2 sequencing negative control?

Examine read lengths, how many reads map to the viral reference and how well they align, rather than relying on total read count. Short primer fragments and intact viral reads have different implications, and called variants in a blank raise serious concerns about cross-contamination.

### Can identical SARS-CoV-2 genomes identify an outbreak's index case?

Not necessarily. The hosts explain that an outbreak may contain identical genomes, while differences in incubation periods mean the earliest symptomatic person need not be the index case.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Over the last year we've learnt a lot about SARS-CoV-2 genomics. Lee
extracts all the insider knowledge from our brains and we give him the
honest truth to his probing questions.  We cover: Pipelines for SARS-
CoV-2 Archives & metadata Read filtering Assembly vs consensus
Amplicon data analysis Controls  If things look too good Coverage
....    Some URLs: https://github.com/connor-lab/ncov2019-artic-nf
https://github.com/jts/ncov-tools https://github.com/lskatz/SARS-
CoV-2-trueTree
