---
layout: page
title: 'Episode 7: Wham, BAM, thank you SAM.'
date: '2019-12-12 00:00:00'
link: https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam
episode: '7'
soundcloud_track: '719276641'
tags:
- microbinfie
- podcast
description: How SAM, BAM and CRAM store read alignments, with samtools workflows, clipping, genome viewers and the case for long-term software support.
excerpt: How SAM, BAM and CRAM store read alignments, with samtools workflows, clipping, genome viewers and the case for long-term software support.
headline: 'SAM, BAM and CRAM: alignment formats, tools and trade-offs'
guests: []
topics:
- sam
- bam
- cram
- read alignment
- alignment visualisation
- soft and hard clipping
- data compression
- long reads
- software maintenance
faq:
- q: What is the difference between SAM, BAM and CRAM?
  a: The episode describes SAM as a plain-text, tab-delimited alignment format, BAM as its binary representation and CRAM as a compressed binary format. CRAM supports lossless storage as well as optional lossy settings; Andrew says most users choose lossless compression.
- q: What is the difference between soft clipping and hard clipping?
  a: Soft clipping excludes bases from the alignment but retains them in the stored read sequence. Hard clipping removes those bases from the stored sequence as well.
- q: Which tools do the hosts recommend for checking and viewing alignments?
  a: Andrew recommends samtools stats with plot-bamcheck for summary statistics and plots. The viewing discussion covers Artemis and BamView, the samtools text viewer, Tablet, IGV and ASCIIGenome.
- q: Why were the hosts not using CRAM instead of BAM everywhere?
  a: 'Andrew describes CRAM’s origins as an archive format and says broader tool support was still needed at the time of the episode. He also sees archives as important: CRAM will have won once NCBI provides everything in it, and handing users back FASTQ files instead of CRAM rather defeats the purpose.'
---

*SAM, BAM and CRAM: alignment formats, tools and trade-offs*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss how SAM became a common format for read alignments, and how BAM and CRAM support different storage needs. They cover practical samtools operations, clipping, quality checks and alignment viewers, alongside the history of the formats. Andrew draws on his experience at Sanger to explain why shared libraries, institutional support and competing implementations helped make the ecosystem durable.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 7: Wham, BAM, thank you SAM." src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/719276641&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 7: Wham, BAM, thank you SAM. on SoundCloud](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam)

## In this episode

### Why a shared alignment format was needed

Nabil introduces Sequence Alignment Map (SAM) as a tab-delimited representation of how reads align to a reference, carrying metadata and quality information alongside the alignment. He dates its publication to 2009 and credits Heng Li, working for Richard Durbin at Sanger, with putting it together. The discussion connects its early use with the short-read aligner BWA.

Andrew describes the pressure that made a reusable format necessary: carefully maintained, bespoke genomics databases could not keep pace with Illumina’s 37-base single-ended reads. Lee and Nabil contrast SAM with older workflows involving Consed and ACE files, including the ACE variant used by 454. Their recollections emphasise awkward parsing and project setup, against a background of rapidly appearing assemblers and read aligners.

### An intermediate result that tools can share

The hosts distinguish plain-text SAM, binary BAM and compressed CRAM. For Lee, the important change was having an explicit stopping point between mapping reads and asking downstream questions such as which SNPs were present. An alignment file preserved the mapped reads for subsequent analysis rather than treating the journey from reads to variants as one indivisible operation.

Nabil values streaming operations and extracting selected regions without loading an entire five-gigabyte file into memory. He describes pipelines connecting samtools view, samtools sort and bcftools. Andrew highlights bitwise flags for selecting unmapped or unpaired reads and filtering secondary alignments. Mapping qualities and CIGAR strings supply further information about the alignment, including clipping and indels. Together, these features make the format useful for both broad processing and focused inspection.

### Clipping and alignment quality checks

Nabil explains soft and hard clipping as ways to represent reads that do not align along their entire length. Soft-clipped bases remain in the read sequence stored in the alignment file but are excluded from the alignment. Hard-clipped bases are removed from that stored sequence as well. Andrew notes the resulting file-size advantage, while the discussion considers long reads, chimeras, repeats and alignments spanning different contigs or chromosomes.

For a quick assessment of an alignment file, Andrew recommends samtools stats with plot-bamcheck. He describes summary information on mapped reads and mapping qualities, alongside insert-size distributions and other patterns that can be plotted. The attraction is a fast overview of what the file contains, rather than having to inspect every alignment manually.

### Viewing reads in terminals and graphical tools

Andrew credits Tim Carver’s work on BamView and its integration into Artemis. He describes viewing reads against an annotated reference and recalls Artemis adopting CRAM support very early. Lee had also used Artemis to examine genome homology, rather than solely for read mapping.

Lee favours the samtools text viewer because it is readily available, lean and fast, including when opening a specified region. He also discusses Tablet and IGV from the Broad Institute. IGV’s tracks, imported gene regions and simultaneous display of multiple mapped genomes are particularly useful; Nabil notes that when IGV came out, it was the only way to view 10 or 20 genomes mapped to one reference. Lee additionally points to ASCIIGenome, whose article he dates to 2017, as an alternative to the samtools text viewer.

### CRAM compression, adoption and long reads

Andrew presents CRAM as a response to sequencing data growing faster than storage becomes cheaper. His example is a bacterial genome at 200× coverage, with many reads matching the reference. He distinguishes optional lossy storage from lossless compression, which he says most users choose. CRAM reorganises data into more compressible groups, including sequences and quality scores, and compresses blocks while retaining access without decompressing the entire file. He reports space savings of roughly 40–50% compared with BAM.

Adoption is not just about file size. At the time of the discussion, Andrew sees limited tool support and archive distribution practices as obstacles to replacing BAM outright. The hosts also discuss failures caused by BAM’s CIGAR-length limitations with very long, noisy Nanopore reads. Andrew describes the frustration of a single problematic read breaking a workflow and suggests CRAM for workflows affected by that limitation, rather than converting through BAM.

### The maintenance behind a lasting format

The hosts repeatedly return to institutional support. Andrew credits John Marshall with extracting alignment-format processing from samtools into HTSlib, allowing other software to reuse the implementation and benefit from shared fixes. He also describes bcftools being separated from the growing codebase and James Bonfield’s continuing development work. Bonfield’s win in the 2011 Sequence Squeeze competition is another part of the compression history discussed.

Separate CRAM implementations in Java at EBI and C at Sanger helped expose issues quickly through both collaboration and competition. Alongside Sanger, EBI and GA4GH involvement, the hosts value public development on GitHub. Their closing argument is that sustained maintenance and common specifications prevent every research project or sequencing vendor from creating another incompatible mapping format.

## Highlights

- [00:01:08](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=1:08) — What SAM records, its origins with Heng Li, and the SAM, BAM and CRAM representations
- [00:02:17](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=2:17) — How early Illumina reads overwhelmed bespoke genomics databases
- [00:08:14](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=8:14) — Tools that read alignment files, including samtools, Picard and CRAMtools
- [00:11:01](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=11:01) — Lee’s view of SAM as a stopping point between mapping and downstream analysis
- [00:11:52](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=11:52) — Streaming BAM operations and connecting samtools commands in pipelines
- [00:14:00](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=14:00) — Read-level information and quality checks with samtools stats and plot-bamcheck
- [00:16:10](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=16:10) — What soft clipping and hard clipping retain or remove
- [00:18:53](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=18:53) — Tim Carver’s BamView work, Artemis integration and early CRAM support
- [00:19:53](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=19:53) — Lee’s preference for the fast, widely available samtools text viewer
- [00:22:27](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=22:27) — CRAM compression and the pressure created by growing sequencing data volumes
- [00:30:07](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=30:07) — Diagnosing BAM failures caused by an individual long read
- [00:31:28](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=31:28) — Long-term maintenance and international backing as a model for bioinformatics software

## In their own words

> this is a model for how we should be developing all bioinformatics software moving forward.
>
> — Andrew Page, [00:31:28](https://soundcloud.com/microbinfie/07-wham-bam-thank-you-sam#t=31:28)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Heng Li, Richard Durbin, John Marshall, James Bonfield, Tim Carver.

## Tools and resources mentioned

BWA, Bowtie, Bowtie2, minimap2, SMALT, Stampy, Consed, samtools, bcftools, HTSlib, pysam, Picard, GATK, CRAMtools, cram-js, plot-bamcheck, Artemis, BamView, Tablet, IGV, ASCIIGenome.

## Questions this episode answers

### What is the difference between SAM, BAM and CRAM?

The episode describes SAM as a plain-text, tab-delimited alignment format, BAM as its binary representation and CRAM as a compressed binary format. CRAM supports lossless storage as well as optional lossy settings; Andrew says most users choose lossless compression.

### What is the difference between soft clipping and hard clipping?

Soft clipping excludes bases from the alignment but retains them in the stored read sequence. Hard clipping removes those bases from the stored sequence as well.

### Which tools do the hosts recommend for checking and viewing alignments?

Andrew recommends samtools stats with plot-bamcheck for summary statistics and plots. The viewing discussion covers Artemis and BamView, the samtools text viewer, Tablet, IGV and ASCIIGenome.

### Why were the hosts not using CRAM instead of BAM everywhere?

Andrew describes CRAM’s origins as an archive format and says broader tool support was still needed at the time of the episode. He also sees archives as important: CRAM will have won once NCBI provides everything in it, and handing users back FASTQ files instead of CRAM rather defeats the purpose.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

This episode we discuss the ubiquitous Sequence Alignment Map
(SAM)format
