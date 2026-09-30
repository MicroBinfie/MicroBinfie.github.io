---
layout: page
title: 'Episode 20: Assembly read healing'
date: '2020-06-11 00:00:00'
link: https://soundcloud.com/microbinfie/20-assembly-read-healing
episode: '20'
soundcloud_track: '770088196'
tags:
- microbinfie
- podcast
description: How trimming, correction and filtering affect genome assembly, and why duplicate reads, uneven coverage and plasmids need care.
excerpt: How trimming, correction and filtering affect genome assembly, and why duplicate reads, uneven coverage and plasmids need care.
headline: 'Read healing before assembly: trimming, errors and plasmids'
guests: []
topics:
- read healing
- read trimming
- read correction
- de novo assembly
- k-mer abundance
- duplicate reads
- coverage subsampling
- plasmid recovery
- salmonella typhi
faq:
- q: What does read healing mean in this episode?
  a: Lee describes read healing as a collective term for read correction, read trimming and read filtering, used in work with Darlene Wagner on preprocessing sequence data.
- q: Should Illumina reads always be corrected before assembly?
  a: The hosts do not present correction as an automatic requirement. It can simplify an assembly graph, but it can also remove minority variants; one host says they avoid correcting short reads unless necessary.
- q: Can read preprocessing cause plasmids to disappear?
  a: Yes. The discussion covers small plasmids lost through length-based processing, and low- or high-copy plasmids lost through abundance filters. TipToft is suggested for checking raw reads for plasmid signals missing from an assembly.
- q: What did Plasmidtron recover from the Pakistan Typhi outbreak?
  a: Comparing outbreak strains with background strains recovered nearly the entire implicated plasmid from short reads in three chunks. Later long-read sequencing supported the reconstruction.
---

*Read healing before assembly: trimming, errors and plasmids*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss preprocessing sequence reads before de novo genome assembly. They consider trimming, error correction and filtering under the collective term “read healing”, weighing cleaner assembly graphs against the risk of removing real biological variation. Plasmids provide a recurring example of what can disappear when length cutoffs or coverage filters are applied without care.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 20: Assembly read healing" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/770088196&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 20: Assembly read healing on SoundCloud](https://soundcloud.com/microbinfie/20-assembly-read-healing)

## In this episode

### Read healing and trimming choices

Lee describes work with Darlene Wagner on “read healing”, divided into read correction, read trimming and read filtering. At the time of recording, they hoped to publish it that year. The central trade-off is that improving individual reads can improve an assembly, but discarding sequence when coverage is already low can make the result worse.

Trimmomatic and fastp are among the hosts’ trimming choices. They compare fixed trimming from read ends, trimming to a quality threshold and rolling-average approaches. Lee describes using thresholds such as Q20 or Q30, alongside filters for minimum read length and average quality. He also discusses his CG pipeline trimming script and PRINSEQ. The conversation does not settle on one universally best trimming rule.

### Long-read cleanup and overlapping pairs

For long reads, the discussion covers chimeras, adapters and low-quality sequence. Gene Myers’ Dazzler suite is mentioned in connection with PacBio data, along with PacBio’s own CCS and cleanup software. Filtlong is used to filter low-quality reads, while Porechop removes adapters and can split reads containing an internal adapter. One host notes that Porechop is no longer being supported.

Overlapping paired-end reads present another preprocessing opportunity. Rather than feeding both overlapping reads into an assembler unchanged, the hosts describe merging them and supplying the merged sequence as a singleton. They identify this as a longstanding trick implemented in Shovill that can improve assembly quality.

### Correction can simplify graphs—or remove real sequence

Read correction is discussed as a way to simplify an assembly graph: sequencing errors introduce branches, making the graph larger and harder to traverse. Removing errors can therefore reduce complexity and help avoid downstream assembly mistakes. The hosts nevertheless express mixed feelings about correcting Illumina reads, particularly because minority variants may be removed and the data may appear more reliable than they really are.

Long-read correction brings a related warning. One host describes a missing 3 kb plasmid in Nanopore data and explains how a 5 kb cutoff could leave shorter reads contributing only to correction of longer reads. TipToft is presented as a way to look for plasmid Inc types and rep sequences in raw reads, helping identify plasmids absent from an assembly.

### Duplicates, uneven coverage and subsampling

Lee describes an exploratory script that removes identical reads and assigns higher Phred scores to retained reads seen more than once. He presents the quality-score adjustment as an idea he had not put past others, rather than an established recommendation. Picard is also mentioned for identifying duplicates, with a warning that laboratory problems can produce strongly over-represented sequences and uneven assembly coverage.

The hosts discuss examining k-mer abundance and reducing excessively abundant sequence. At 10,000-fold coverage, errors may start to resemble real signal and complicate the assembly graph; subsampling towards roughly 100-fold coverage is offered as a more manageable alternative. One host also uses fastp reports to inspect k-mer abundance and over-represented sequences.

### Why abundance filters can miss plasmids

Removing rare k-mers may eliminate errors, but it may also discard real sequence, minority variants or low-copy plasmids. Removing highly abundant k-mers carries the opposite risk: losing high-copy plasmids. The hosts note that plasmid abundance is not necessarily equal to or greater than chromosomal abundance, and discuss assembling bins and subsampling as ways to recover some sequences.

The same limitation affects coverage-based plasmid identification. They describe plasmidSPAdes as using k-mer abundance differences between presumed chromosomal and plasmid sequence. A plasmid at approximately the chromosome’s copy number can be missed, whereas a substantial abundance difference makes it easier to distinguish. The hosts stress that coverage-based approaches have important edge cases.

### Plasmidtron and drug-resistant Salmonella Typhi

Plasmidtron is described as comparing sets of cases and controls, finding k-mers associated with the cases and assembling the corresponding sequence. The aim is to recover mobile genetic elements that may explain a difference between the groups, such as more severe disease.

The example is an extensively drug-resistant Salmonella Typhi outbreak in Pakistan, where a plasmid entered a multidrug-resistant Typhi strain. Comparing background strains with outbreak strains allowed the team to recover nearly the entire plasmid from short-read data in three chunks. Later long-read sequencing supported that reconstruction. The example returns the discussion to its broader caution: preprocessing decisions need to preserve the plasmids an investigation is trying to find.

## Highlights

- [00:01:05](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=1:05) — Initial trimming choices, long-read cleanup and the danger of losing coverage
- [00:02:59](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=2:59) — fastp, PacBio cleanup tools and quality-threshold versus window-based trimming
- [00:04:30](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=4:30) — Lee’s trimming script, PRINSEQ and length and average-quality filters
- [00:05:35](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=5:35) — Merging overlapping paired-end reads into singletons, as implemented in Shovill
- [00:06:22](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=6:22) — Lee introduces read-healing work with Darlene Wagner
- [00:07:01](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=7:01) — Long-read correction, missing small plasmids and checking raw reads with TipToft
- [00:08:08](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=8:08) — Why correction simplifies assembly graphs but can hide minority variants
- [00:10:09](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=10:09) — Lee’s exploratory approach to identical reads and Phred scores
- [00:10:56](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=10:56) — Picard, duplicate bias and subsampling excessively deep sequence data
- [00:13:36](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=13:36) — How plasmidSPAdes can miss plasmids with chromosome-like abundance
- [00:14:37](https://soundcloud.com/microbinfie/20-assembly-read-healing#t=14:37) — Plasmidtron and reconstruction of a plasmid from the Pakistan Typhi outbreak

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Darlene Wagner, Gene Myers, Nick Waters.

## Tools and resources mentioned

Trimmomatic, Dazzler, Filtlong, Porechop, fastp, PacBio CCS, PRINSEQ, CG pipeline, Shovill, TipToft, Picard, SPAdes, plasmidSPAdes, Plasmidtron.

## Questions this episode answers

### What does read healing mean in this episode?

Lee describes read healing as a collective term for read correction, read trimming and read filtering, used in work with Darlene Wagner on preprocessing sequence data.

### Should Illumina reads always be corrected before assembly?

The hosts do not present correction as an automatic requirement. It can simplify an assembly graph, but it can also remove minority variants; one host says they avoid correcting short reads unless necessary.

### Can read preprocessing cause plasmids to disappear?

Yes. The discussion covers small plasmids lost through length-based processing, and low- or high-copy plasmids lost through abundance filters. TipToft is suggested for checking raw reads for plasmid signals missing from an assembly.

### What did Plasmidtron recover from the Pakistan Typhi outbreak?

Comparing outbreak strains with background strains recovered nearly the entire implicated plasmid from short reads in three chunks. Later long-read sequencing supported the reconstruction.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Preprocessing of sequence data in advance of de novo assembly is a
critical step to improving the final quality of your assembly. We chat
about read trimming, correction and filtering, collectively called
'Read Healing'.  Software mentioned: https://github.com/sanger-
pathogens/plasmidtron
