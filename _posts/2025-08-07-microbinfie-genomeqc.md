---
layout: page
title: 'Episode 142: Genomeqc'
date: '2025-08-07 00:00:00'
link: https://soundcloud.com/microbinfie/microbinfie-genomeqc
episode: '142'
soundcloud_track: '2140006038'
tags:
- microbinfie
- podcast
description: Nabil-Fareed Alikhan explains species-specific genome QC thresholds, machine-learning outlier removal and the limits of Illumina-based assemblies.
excerpt: Nabil-Fareed Alikhan explains species-specific genome QC thresholds, machine-learning outlier removal and the limits of Illumina-based assemblies.
headline: 'GenomeQC, now qualibact: species-specific bacterial genome QC'
guests: []
topics:
- bacterial genome quality
- assembly quality control
- species-specific thresholds
- outlier detection
- machine learning
- genome size
- n50
- short-read assemblies
- long-read sequencing
faq:
- q: Are GenomeQC and qualibact the same project?
  a: Yes. The episode uses GenomeQC, but the show notes state that the project was renamed qualibact.
- q: How were the bacterial genome QC thresholds calculated?
  a: The analysis reuses AllTheBacteria assemblies and species assignments, recalculates assembly metrics, and applies machine-learning outlier removal across multiple metrics. Nabil then trims the filtered distributions at the 0.5th and 99.5th percentiles.
- q: Can these thresholds be applied directly to long-read assemblies?
  a: 'The episode cautions against treating them as technology-independent: they were derived from Illumina assemblies, with contiguity expectations tied to Shovill. Nanopore or PacBio assemblies may need separate reference ranges.'
- q: Was the traffic-light QC reporting tool available when this episode was recorded?
  a: No; Nabil described it as unfinished. The website already provided thresholds and a summary CSV, while the planned companion tool would read other tools' outputs and generate CSV or HTML reports.
---

*GenomeQC, now qualibact: species-specific bacterial genome QC*

Nabil-Fareed Alikhan discusses GenomeQC with hosts Lee Katz and Andrew Page: a resource for interpreting bacterial assembly quality using species-specific thresholds. The conversation covers its underlying data, outlier filtering, example ranges and planned reporting software. The show notes clarify that the project was subsequently renamed qualibact.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 142: Genomeqc" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2140006038&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 142: Genomeqc on SoundCloud](https://soundcloud.com/microbinfie/microbinfie-genomeqc)

## In this episode

### Why assembly metrics need reference ranges

GenomeQC, now called qualibact, is presented primarily as a process for generating reference thresholds rather than a finished standalone program. Nabil describes a familiar problem: someone runs QUAST, obtains an N50 or contig count, and still cannot tell whether their assembly is any good. Comparing samples within a project helps identify outliers, but cannot establish quality if the whole dataset is poor.

Species-specific expectations provide a starting point. The hosts discuss variation within Salmonella, including the host-adapted serovar Typhi and other serovars such as Dublin that are adapted in different ways, and differences between species in the same genus. Nabil notes that a one-megabase difference in a five-megabase genome represents 20% variation—enough to make a universal genome-size threshold misleading.

### Reusing AllTheBacteria assemblies

The analysis builds on AllTheBacteria, avoiding the need for Nabil to assemble 1.2 million genomes himself. It also reuses that dataset's taxonomic assignments from sylph, described in the episode as a fast approximation of GTDB classification. Recalculating assembly metrics such as GC content took roughly half a day to a day on a compute cluster.

Species are the initial grouping, not a requirement of the method. Nabil says the same approach could generate thresholds for sequence types, subspecies or broader groups such as families. He contrasts the reproducible workflow with existing in-house ranges, NCBI genome-size expectations, earlier EnteroBase thresholds and KlebNET's Klebsiella-specific numbers.

### Removing outliers before setting thresholds

Nabil found that conventional statistical approaches, including treating metric distributions as normal, struggled with extreme outliers in Sequence Read Archive-derived data. He gives the example of a Klebsiella assembly with a total length of only 0.3 megabases. His approach instead removes anomalies using machine learning, then trims the remaining extremes at the 0.5th and 99.5th percentiles.

Although the website illustrates results with two-dimensional plots, the filtering uses multiple metrics together, including N50, total assembly length, contig count and GC content. The analysis is written in Python using scikit-learn and statistical libraries. Taxonomic mixtures remain a limitation: the combined E. coli and Shigella analysis retains a visible Shigella sub-distribution after filtering.

### Example ranges and rounded numbers

Lee identifies Neisseria meningitidis as his original area of work, and Nabil asks him to assess these example expectations:

- Genome size: 2.0–2.4 megabases.
- Coding sequences: 1,900–2,500.
- Contigs with Shovill: no more than around 300.
- GC content: 51–53%.

Lee questions how neatly rounded the values are. Nabil explains that the displayed thresholds are rounded for readability and recall; detailed summary tables retain the underlying statistics, including quartiles, means and medians. The discussion also gives genome-size ranges of 1.6–2.2 megabases for Campylobacter coli and 1.5–2.0 megabases for Campylobacter jejuni, illustrating why related species should not automatically share thresholds.

### Limits imposed by sequencing and assembly

These thresholds come from Illumina data and are not presented as interchangeable with long-read expectations. Nabil expects Nanopore assemblies to shift some genome-size distributions because they can recover sequence missing or collapsed in short-read assemblies. He notes discrepancies between the AllTheBacteria assemblies and RefSeq, and invites suitable Oxford Nanopore or PacBio datasets for equivalent analyses.

Contig counts and N50 also depend on the assembler. The examples here are tied to Shovill; Nabil says Velvet would have higher expected contig counts. The hosts discuss the idea of separating reference values in future, such as an N50 for Illumina and an N50 for PacBio.

### Using the thresholds in pipelines

The website offers species pages, supporting plots, detailed statistics and a summary CSV covering the included species. Nabil hopes users will download the thresholds and incorporate them into their own pipelines. This separates the reference data from any particular reporting interface.

At the time of recording, he was also developing a Python companion tool to consume outputs from programs such as QUAST and CheckM and produce CSV or HTML reports. The intended interface resembles MultiQC, with traffic-light assessments; Conda and PyPI distribution were planned, not yet available. He invites expert feedback, especially where mixed populations make thresholds too lenient. The aim is to refine the initial ranges through critique rather than present them as final limits for every organism.

## Highlights

- [00:01:17](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=1:17) — Why N50 and contig counts need species-specific reference values
- [00:04:32](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=4:32) — Species classification and the option to analyse other taxonomic groupings
- [00:05:54](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=5:54) — Reusing 1.2 million assemblies and recalculating assembly metrics
- [00:06:40](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=6:40) — Accessing website thresholds and plans for a reporting tool
- [00:08:50](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=8:50) — EnteroBase experience and the push to define useful expected values
- [00:10:54](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=10:54) — Example quality thresholds for Neisseria meningitidis
- [00:11:41](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=11:41) — Rounded display values versus detailed statistical summaries
- [00:12:53](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=12:53) — Why Illumina-derived thresholds depend on sequencing and assembly choices
- [00:15:19](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=15:19) — Existing QC ranges and the case for reproducible threshold generation
- [00:18:53](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=18:53) — Python implementation of the reporting tool and threshold analysis
- [00:22:46](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=22:46) — Filtering across multiple metrics and dealing with mixed populations

## In their own words

> The algorithm or method that I'm using is not dependent on these classifications.
>
> — Nabil-Fareed Alikhan, [00:04:32](https://soundcloud.com/microbinfie/microbinfie-genomeqc#t=4:32)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

GenomeQC, qualibact, AllTheBacteria, sylph, GTDB, QUAST, CheckM, MultiQC, Shovill, Velvet, EnteroBase, RefSeq, Sequence Read Archive (SRA), Python, scikit-learn, Conda, PyPI.

## Questions this episode answers

### Are GenomeQC and qualibact the same project?

Yes. The episode uses GenomeQC, but the show notes state that the project was renamed qualibact.

### How were the bacterial genome QC thresholds calculated?

The analysis reuses AllTheBacteria assemblies and species assignments, recalculates assembly metrics, and applies machine-learning outlier removal across multiple metrics. Nabil then trims the filtered distributions at the 0.5th and 99.5th percentiles.

### Can these thresholds be applied directly to long-read assemblies?

The episode cautions against treating them as technology-independent: they were derived from Illumina assemblies, with contiguity expectations tied to Shovill. Nanopore or PacBio assemblies may need separate reference ranges.

### Was the traffic-light QC reporting tool available when this episode was recorded?

No; Nabil described it as unfinished. The website already provided thresholds and a summary CSV, while the planned companion tool would read other tools' outputs and generate CSV or HTML reports.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

The crew talks about the genomeqc ecosystem. Check it out at
<https://happykhan.github.io/qualibact/>

Errata: The project name was chaned to qualibact and is no longer genomeqc as mentioned on the
episode.
