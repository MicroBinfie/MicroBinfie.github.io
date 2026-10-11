---
layout: page
title: 'Episode 117: From Math to Metagenomics - Titus Brown on Career Journeys and Software Solutions'
date: '2023-12-07 00:00:00'
link: https://soundcloud.com/microbinfie/titus-brown-1
episode: '117'
soundcloud_track: '1657196202'
tags:
- microbinfie
- podcast
description: Titus Brown on his route into bioinformatics, digital normalisation, khmer, sourmash and the practical barriers to scientific data reuse.
excerpt: Titus Brown on his route into bioinformatics, digital normalisation, khmer, sourmash and the practical barriers to scientific data reuse.
headline: 'Titus Brown: from maths to metagenomics and usable software'
guests:
- Titus Brown
topics:
- microbial bioinformatics
- metagenomics
- transcriptomics
- k-mers
- digital normalisation
- minhash
- software documentation
- data reuse
- fair data
- career journeys
faq:
- q: Why did Titus Brown move from experimental biology into bioinformatics?
  a: Growing volumes of sequence data created problems his programming background could help solve. At Michigan State, colleagues’ transcriptome datasets persuaded him to focus on analysis rather than generating more data, leading him towards non-model transcriptomics and metagenomics.
- q: How does Brown describe digital normalisation?
  a: It estimates the coverage of each read and discards reads once coverage is high enough. Brown’s motivating example was a single-cell E. coli dataset with about 400× coverage, where he wondered whether 50–100× would be sufficient.
- q: How does sourmash reduce the burden of working with k-mers?
  a: Brown describes a MinHash-derived approach adapted for metagenomics that throws away 99.9% of k-mers. This makes it possible to compare many genomes and metagenomes without retaining every k-mer in memory or on disk.
- q: What makes scientific data reuse difficult beyond the technical work?
  a: Brown argues that solutions must account for how people work, not just provide infrastructure. The discussion also identifies differences in national and state laws, alongside efforts that appear to share data without actually making it available.
---

*Titus Brown: from maths to metagenomics and usable software*

Titus Brown joins Lee Katz and Andrew Page to trace his career from maths and experimental developmental biology to metagenomics and software development. He explains how researchers’ practical problems shaped his work on khmer, digital normalisation and sourmash, and why documentation matters as much as implementation. The discussion closes with the organisational and legal obstacles to reusing scientific data.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 117: From Math to Metagenomics - Titus Brown on Career Journeys and Software Solutions" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1657196202&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 117: From Math to Metagenomics - Titus Brown on Career Journeys and Software Solutions on SoundCloud](https://soundcloud.com/microbinfie/titus-brown-1)

## In this episode

### From maths to experimental biology

Brown studied maths at Reed College, where his undergraduate research covered digital evolution and physical meteorology. The latter involved estimating Earth’s albedo by using the Moon as a mirror: comparing the brightness of its dark and illuminated portions provided a measurement of sunlight reflected from Earth. Digital evolution drew him towards biology, a direction reinforced by three senior physicists who independently recommended it for graduate study.

At Caltech, Brown joined a developmental biology laboratory studying sea urchin gene regulatory networks and cis-regulatory elements. He spent six or seven years doing experiments, including PCR and microinjections, and later completed a short postdoctoral appointment working on chick neural crest.

### Software that colleagues could use independently

As genome sequences accumulated in the late 1990s and early 2000s, Brown’s maths and open-source programming background made him useful to colleagues facing more data than they could handle. He began with large-scale BLAST searches, then developed comparative sequence analysis software, a graphical interface and a web server for computationally demanding work.

One tool helped researchers find conserved non-coding elements in large stretches of eukaryotic DNA. Brown wrote tutorials and documentation, then returned to his own experiments. At a subsequent sea urchin meeting, he discovered that eight colleagues had used it successfully without needing his support. That experience shaped his commitment to usable software and instructions that let others work independently.

### The sequencing boom and digital normalisation

Brown arrived at Michigan State University in 2008 intending to combine embryology with large-scale gene expression analysis. As the Illumina GA2 became widely available, colleagues brought him transcriptome datasets they could not open in Excel. He shifted towards analysing non-model transcriptomes and metagenomes, with k-mers becoming central to his work on khmer and digital normalisation.

The digital normalisation idea crystallised while he was considering a single-cell E. coli dataset with roughly 400× coverage. Why retain that depth if 50–100× would suffice? He tried estimating each read’s coverage and discarding reads once coverage was high enough. A Python interface helped him produce a functioning implementation in about 30 minutes. It proved useful for RNA-seq and metagenomic datasets. Soil metagenomes became a demanding test case: Brown reasoned that tools able to handle their scale would be broadly applicable.

### UC Davis, MinHash and sourmash

After moving to UC Davis, Brown combined his research programme with informal advice and collaborations in the veterinary school. He describes arriving exhausted and worrying that he would not be creative again. Two papers helped change that: MetaPalette, concerning k-mers and species-level specificity, and Mash, which applied MinHash to genomic sequences.

While reviewing Mash, Brown implemented MinHash himself in a few lines of Python and became an advocate for the paper. Together, the papers prompted him to start sourmash, with a graduate student joining through GitHub pull requests. Brown describes sourmash as a MinHash-derived approach adapted for metagenomics: it discards 99.9% of k-mers, allowing much broader comparisons without the memory and disk demands of retaining them all. Looking back, he regards the period he had feared would be unproductive as one of his most creative.

### GAMBIT and targeted k-mers

One of the hosts recommends GAMBIT as another way to avoid examining every k-mer. In the host’s description, it selects sequences using a particular prefix and examines the sequence after that prefix. The host relates this to start codons and approximately one k-mer per bacterial gene, highlighting its usefulness for typing. This is a brief recommendation rather than a detailed comparison with sourmash.

### Why data reuse needs more than infrastructure

Brown also describes several years working on NIH data infrastructure, beginning with the Data Commons Pilot Phase Consortium and continuing into the Common Fund Data Ecosystem. He became one of two people running a large consortium, but left that coordination role in April of the year he was interviewed. The experience taught him about practical obstacles to reuse—and about his own limited appetite for meetings.

He frames FAIR data—findability, accessibility, interoperability and reusability—as a difficult problem requiring socio-technical solutions that account for how people actually work. One of the hosts adds that different national and state laws complicate sharing, and criticises spending that creates an appearance of data sharing without making data available. The episode ends before that discussion can develop further.

## Highlights

- [00:00:00](https://soundcloud.com/microbinfie/titus-brown-1#t=0:00) — Lee Katz introduces Titus Brown and the interview.
- [00:01:33](https://soundcloud.com/microbinfie/titus-brown-1#t=1:33) — Brown traces his background from maths, digital evolution and physical meteorology.
- [00:08:31](https://soundcloud.com/microbinfie/titus-brown-1#t=8:31) — One of the hosts describes using khmer to downsample very high-coverage bacterial data.
- [00:08:50](https://soundcloud.com/microbinfie/titus-brown-1#t=8:50) — A deeply sequenced single-cell E. coli dataset prompts the digital normalisation idea.
- [00:16:12](https://soundcloud.com/microbinfie/titus-brown-1#t=16:12) — GAMBIT is recommended for prefix-targeted k-mers and bacterial typing.
- [00:17:11](https://soundcloud.com/microbinfie/titus-brown-1#t=17:11) — Brown discusses NIH data infrastructure, consortium coordination and barriers to reuse.
- [00:19:07](https://soundcloud.com/microbinfie/titus-brown-1#t=19:07) — Different legal jurisdictions and the gap between apparent and actual data sharing.

## In their own words

> if you can analyze a soil metagenome, any other metagenome is easier.
>
> — Titus Brown, [00:08:50](https://soundcloud.com/microbinfie/titus-brown-1#t=8:50)

## Who is talking

- **Titus Brown** (guest, UC Davis, School of Veterinary Medicine)
- **Lee Katz** (host)
- **Andrew Page** (host)

## Tools and resources mentioned

BLAST, PCR, Illumina GA2, Excel, khmer, Digital normalisation, RNA-seq, Python, MetaPalette, Mash, MinHash, sourmash, GitHub, GAMBIT.

## Questions this episode answers

### Why did Titus Brown move from experimental biology into bioinformatics?

Growing volumes of sequence data created problems his programming background could help solve. At Michigan State, colleagues’ transcriptome datasets persuaded him to focus on analysis rather than generating more data, leading him towards non-model transcriptomics and metagenomics.

### How does Brown describe digital normalisation?

It estimates the coverage of each read and discards reads once coverage is high enough. Brown’s motivating example was a single-cell E. coli dataset with about 400× coverage, where he wondered whether 50–100× would be sufficient.

### How does sourmash reduce the burden of working with k-mers?

Brown describes a MinHash-derived approach adapted for metagenomics that throws away 99.9% of k-mers. This makes it possible to compare many genomes and metagenomes without retaining every k-mer in memory or on disk.

### What makes scientific data reuse difficult beyond the technical work?

Brown argues that solutions must account for how people work, not just provide infrastructure. The discussion also identifies differences in national and state laws, alongside efforts that appear to share data without actually making it available.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie Podcast, Andrew Page and Lee Katz interview Titus Brown
about his journey from studying math and physics as an undergrad to becoming a bioinformatician
focusing on metagenomics and software development.

Topics discussed:

Titus' background in math, physics, digital evolution research, and developmental biology His
transition into bioinformatics to analyze the influx of genomic data in the 1990s Developing
early tools for comparative genomics and sequence analysis The philosophy of creating usable
software with good documentation Work on transcriptomics, metagenomics, and k-mers at Michigan
State Digital normalization and dealing with large sequencing datasets Moving to UC Davis and
continuing work on metagenomics and software like khmer and sourmash Thoughts on challenges
around data reuse and accessibility in science.

Papers: Spacegraphcats -
<https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02066-4> Sourmash -
<https://www.biorxiv.org/content/10.1101/2022.01.11.475838v2> IBD exploration - <https://dib-
lab.github.io/2021-paper-ibd/>
