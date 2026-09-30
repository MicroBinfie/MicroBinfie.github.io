---
layout: page
title: 'Episode 3: FASTQ - all your bases are belong to us'
date: '2019-10-17 00:00:00'
link: https://soundcloud.com/microbinfie/fastq-all-your-bases
episode: '3'
soundcloud_track: '678621687'
tags:
- microbinfie
- podcast
description: 'FASTQ quality scores, compression, read ordering and parsing traps: the hosts discuss the everyday format behind microbial sequencing analysis.'
excerpt: 'FASTQ quality scores, compression, read ordering and parsing traps: the hosts discuss the everyday format behind microbial sequencing analysis.'
headline: 'FASTQ: quality scores, compression and parsing pitfalls'
guests: []
topics:
- fastq
- quality scores
- phred encoding
- read compression
- read ordering
- subsampling bias
- illumina headers
- quality-score binning
- file parsing
faq:
- q: What does a FASTQ file contain?
  a: The episode describes FASTQ as a text format containing DNA sequence reads and quality strings representing the sequencing machine’s confidence in its base calls. Records also have identifiers and a plus line separating the sequence from its quality information.
- q: Does every FASTQ record have exactly four lines?
  a: No. The hosts explain that sequences and quality strings can extend across multiple lines, so a parser that simply reads four lines at a time can fail. One host describes normalising multiline records into four-line records before running other scripts.
- q: Why does Phred+33 versus Phred+64 matter?
  a: The offset changes which ASCII characters represent particular quality scores. The hosts warn that interpreting older Phred+64 data as Phred+33 can make the quality characters misleading; in this 2019 discussion, they treat Phred+33 as the usual encoding.
- q: Can sorting FASTQ reads improve compression?
  a: The hosts discuss reordering reads to make them more amenable to compression. They also warn that taking only the first part of an ordered file can introduce subsampling bias, and describe an ART simulation experiment where the placement of ambiguous bases caused a related problem.
---

*FASTQ: quality scores, compression and parsing pitfalls*

The hosts discuss how FASTQ stores sequence reads and quality scores, and why its conventions can catch out analysis scripts. They cover older encodings, compression, read ordering, Illumina headers and the gap between a familiar four-line layout and what the format actually permits.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 3: FASTQ - all your bases are belong to us" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/678621687&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 3: FASTQ - all your bases are belong to us on SoundCloud](https://soundcloud.com/microbinfie/fastq-all-your-bases)

## In this episode

### What FASTQ stores

FASTQ is introduced as a text format containing DNA sequences and the sequencing machine’s confidence in each base call. For the hosts, it is everyday working material: the data they exchange, retain and return to when someone asks how an analysis was performed. Its central role contrasts with the informal way its conventions developed.

The opening disagreement concerns keeping reads together in one file or separated into different files. One host prefers a single file per genome, while another finds separate files easier to analyse; SPAdes is mentioned as software that splits the combined input anyway. They also recall SFF files from 454 sequencing and the choice between SFF and FASTQ offered by Ion Torrent.

### Reading quality characters correctly

The quality string represents scores using ASCII characters rather than a sequence of written-out integers. The hosts discuss how familiar those characters become after years of inspecting reads, including the punctuation that can make a poor-quality read look as though it is swearing.

That visual intuition depends on the encoding. Their explanation distinguishes Sanger Phred+33 from older Phred+64: the former includes special characters at low scores, while the latter starts at the @ symbol and proceeds into capital letters. A reader accustomed to one encoding could misinterpret the other. Speaking in 2019, they describe Phred+33 as the normal case and Phred+64 as chiefly a concern for much older sequencing data.

### Compression can change read order

BAM and CRAM enter the conversation as alternatives to working solely with FASTQ. BAM carries alignment information, while CRAM is discussed for its compression potential: one host suggests that going fully down that route can reduce data to a tenth of the original size. Sharing remains a practical obstacle if the recipient does not know how to handle the format, so FASTQ remains their common exchange format.

They discuss compression levels from 1 to 9 and reordering reads to improve compression, including a tool associated with Brian Bushnell of BBMap. But ordering matters when another step takes only the beginning of a file. An ART simulation experiment provides a cautionary example: ambiguous N bases were concentrated at the beginning of the genome during a study of their effect on SNP calling, producing an unexpected subsampling bias.

### Headers, flow-cell bubbles and quality bins

Illumina FASTQ headers can encode machine identity, positional information, channel and tile. The hosts find that detail both useful and cumbersome. They recall how a literal air bubble on a flow cell could cause locally poor sequencing quality, making tile information useful when deciding which reads to filter.

The discussion then turns to quality-score binning on newer machines, including NextSeq. Rather than retaining a continuous range of scores, binning groups values together. The hosts express reservations about the information lost, particularly because quality scores are already logarithmic. One host describes trying to avoid binning in his own lab's work, though he does not recall the exact increments used.

### An informal format with parsing traps

The hosts trace FASTQ to internal use at Sanger rather than an original formal specification. They describe a 2010 paper that documented the format after it was already established, and mention the BWA website as an earlier but incomplete source of description.

This history matters when writing parsers. The conversation names samtools and seqtk, but also describes home-written scripts, including Perl parsers, that assumed every record occupied four lines. FASTQ can instead contain line breaks within the sequence and quality strings. The plus line helps separate those parts, and the sequence and quality strings must have matching lengths.

One host recalls receiving multiline FASTQ from samtools and raising the issue online, where Heng Li pointed out that FASTQ was not necessarily a four-line format. The resulting workaround was a parser that normalised records into four lines before other scripts processed them.

### When software expects no score above Q40

The final technical issue is software that rejects quality scores outside an expected range. The hosts discuss PacBio and Nanopore data, with PacBio offered as an example of scores reaching Q50 or higher while some programs are hard-coded to expect no more than Q40.

They disagree about how much those higher scores matter in practice. One host questions the value of distinguishing extremely low error rates; another values a claimed rate of one error in a million when considering a genome of five million bases. The exchange closes the discussion without pretending that every preference has been resolved.

## Highlights

- [00:01:08](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=1:08) — Keeping reads in one FASTQ file versus separate files, and what SPAdes does with them
- [00:01:56](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=1:56) — Defining FASTQ through DNA sequences and per-read quality strings
- [00:02:41](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=2:41) — Earlier sequencing formats and the transition from 454 data to FASTQ
- [00:04:34](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=4:34) — Distinguishing Sanger Phred+33 from older Phred+64 quality encoding
- [00:05:41](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=5:41) — BAM, reference alignments and interest in CRAM
- [00:06:27](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=6:27) — FASTQ compression levels and sorting reads to improve compression
- [00:07:23](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=7:23) — An ART simulation experiment exposes bias from where ambiguous bases occur
- [00:08:24](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=8:24) — Decoding machine, position, channel and tile information in Illumina headers
- [00:10:35](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=10:35) — Concerns about information loss when logarithmic quality scores are binned
- [00:11:02](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=11:02) — FASTQ’s informal origins and a 2010 paper documenting the format
- [00:12:39](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=12:39) — Why four-line assumptions fail for multiline FASTQ records
- [00:15:01](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=15:01) — Programs expecting at most Q40 encounter higher PacBio quality scores

## In their own words

> I'd say it's a glorified text file that has the nucleotides that came off the machine and the confidence the machine has when they called it.
>
> — one of the hosts, [00:02:10](https://soundcloud.com/microbinfie/fastq-all-your-bases#t=2:10)

## Who is talking

- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)

Also mentioned: Brian Bushnell, Heng Li.

## Tools and resources mentioned

SPAdes, samtools, seqtk, BBMap, ART, BWA, NextSeq, Ion Torrent, 454, Phred quality scoring, LZ compression.

## Questions this episode answers

### What does a FASTQ file contain?

The episode describes FASTQ as a text format containing DNA sequence reads and quality strings representing the sequencing machine’s confidence in its base calls. Records also have identifiers and a plus line separating the sequence from its quality information.

### Does every FASTQ record have exactly four lines?

No. The hosts explain that sequences and quality strings can extend across multiple lines, so a parser that simply reads four lines at a time can fail. One host describes normalising multiline records into four-line records before running other scripts.

### Why does Phred+33 versus Phred+64 matter?

The offset changes which ASCII characters represent particular quality scores. The hosts warn that interpreting older Phred+64 data as Phred+33 can make the quality characters misleading; in this 2019 discussion, they treat Phred+33 as the usual encoding.

### Can sorting FASTQ reads improve compression?

The hosts discuss reordering reads to make them more amenable to compression. They also warn that taking only the first part of an ordered file can introduce subsampling bias, and describe an ART simulation experiment where the placement of ambiguous bases caused a related problem.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

FASTQ files are the foundation of modern bioinformatics. Tune into an
informal chat between Lee, Nabil and Andrew as they tell the story of
how FASTQs evolved out of nowhere, with all the backstories and
qwerks. You might even learn something.
