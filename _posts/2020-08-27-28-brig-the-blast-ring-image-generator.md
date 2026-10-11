---
layout: page
title: 'Episode 28: BRIG the BLAST Ring Image Generator'
date: '2020-08-27 00:00:00'
link: https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator
episode: '28'
soundcloud_track: '844305547'
tags:
- microbinfie
- podcast
description: Nabil-Fareed Alikhan explains BRIG’s circular genome plots, its beer-wager origins, and the design choices behind its lasting use.
excerpt: Nabil-Fareed Alikhan explains BRIG’s circular genome plots, its beer-wager origins, and the design choices behind its lasting use.
headline: 'BRIG: building circular genome comparisons with BLAST'
guests: []
topics:
- comparative genomics
- genome visualisation
- plasmid comparison
- reference-based comparison
- graphical interfaces
- software documentation
- software testing
- bioinformatics software development
faq:
- q: What does BRIG do?
  a: BRIG, the BLAST Ring Image Generator, compares input sequences against a selected reference using BLAST and displays the results as concentric rings. It supports annotations and adjustable settings for producing publication-ready figures.
- q: Do I need to install BLAST separately to use BRIG?
  a: Yes. BRIG runs BLAST for you, but does not install it; you must point BRIG to a BLAST installation. Nabil says it worked with both legacy BLAST and BLAST+, which had only just been released at the time.
- q: Can BRIG show sequence that is absent from the reference?
  a: Not in the reference-based figure described here. Query sequence without a counterpart in the reference is not displayed, so the plot does not reveal all accessory sequence differences among the queries.
- q: Does the episode describe a command-line version of BRIG?
  a: Command-line operation is discussed as a recurring request, not as the BRIG workflow presented in the episode. Nabil says he would favour reimplementing the software and discusses possible online operation and additional input formats.
---

*BRIG: building circular genome comparisons with BLAST*

Lee Katz and Andrew Page talk with fellow host Nabil-Fareed Alikhan about BRIG, the BLAST Ring Image Generator, which he authored. In this 2020 software deep dive, they discuss how BRIG turns sequence comparisons into publication-ready circular figures, why its interface and manual mattered, and how its reference-based design limits what users can see.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 28: BRIG the BLAST Ring Image Generator" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/844305547&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 28: BRIG the BLAST Ring Image Generator on SoundCloud](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator)

## In this episode

### What a BRIG figure shows

BRIG accepts sequences in GenBank, FASTA or multi-FASTA format. Users select a reference genome, compare the other sequences against it with BLAST, and display the results as concentric rings. Annotations, thresholds and other settings can be adjusted. BRIG runs BLAST on the user’s behalf, but does not install it: users must supply a BLAST installation. Nabil says that BLAST+ had only just been released at the time, and BRIG worked with both legacy BLAST and BLAST+.

The attraction is a simple view of what is conserved relative to one reference. By this discussion, Nabil was seeing substantial use for plasmid comparisons, whereas earlier applications more often involved complete genomes. He also recalls someone asking him to increase the supported scale so that it would work for eukaryotes such as yeast. Lee Katz introduces BRIG as having around a thousand citations.

### A jug-of-beer challenge

BRIG began with a challenge from Nabil’s PhD supervisor, Scott Beatson. Scott was using a Perl script to prepare configuration files for BLAST Atlas and wanted something simpler: a tool that would take BLAST results and draw the picture. The reward for the first working solution was one jug of beer, described as two imperial pints, or about 1.2 litres.

The basic brief took Nabil a week or two. Requests then accumulated for GenBank input, annotations, BAM coverage and other features, extending development to roughly six to nine months. BRIG was published in August 2011. Its name describes its function—BLAST Ring Image Generator—but also reflects Nabil’s interest in ships and the feeling of being locked in the brig while debugging.

### Drawing, feedback and a borrowed colour palette

The image-rendering package underneath BRIG is CGView, which Nabil had already used in other projects. He stresses that circular comparative figures were not new: alternatives discussed include BLAST Atlas, DNAPlotter and the CGView server. BRIG’s contribution was not inventing the representation, but making it accessible and producing figures people wanted to use.

Development involved repeatedly emailing versions to users and collecting bug reports, ideas and aesthetic feedback, including from colleagues at the University of Queensland. Publication-ready SVG and PNG output was a central requirement. The default palette, containing about 20 colours, came from an unnamed fellow PhD student whose presentation figures Nabil admired. He still recognises that sequence of colours in published BRIG figures.

### Java implementation and maintenance regrets

Nabil wrote BRIG in Java, using Swing for the graphical interface, because Java was the language he knew best from his undergraduate software-engineering training. It is distributed as a Java archive, or JAR. Looking back, he would have used library-management tools such as Maven to make updating and installation easier.

BRIG launches BLAST as a subprocess. Nabil describes the work needed to ensure that terminating the main interface also stopped BLAST, rather than leaving searches consuming resources and slowing users’ laptops.

His major regret is the lack of unit tests. Although the code is object-oriented and follows design principles, it lacks a strong test suite. That makes substantial changes difficult to attempt without breaking existing behaviour.

### Documentation and manageable figures

BRIG’s documentation is a roughly 50-page manual written in LaTeX and distributed with the software. It begins with finished figures and directs readers to worked examples showing exactly which controls to use and which settings to change. A reference section then explains CGView configuration, BLAST parameters and the interface’s options. Nabil says this structure took considerable effort; users’ praise for the manual was not accidental. He would now favour publishing similar material on Read the Docs.

He is also proud of the logic that simplifies overlapping BLAST hits before drawing them. Creating a separate SVG object for every hit could produce an unwieldy file. The optimisation keeps figures manageable, and he has seen users produce working images containing around 50 genomes with annotations.

### What the reference leaves out

The same reference-centred design that makes BRIG easy to understand also creates a blind spot. Sequence present in query genomes but absent from the reference will not appear in the figure. Users therefore cannot use that image alone to see all accessory sequence shared or exchanged among their queries. The output is also static, rather than an interactive view for exploring regions in detail.

Nabil recalls Kat Holt requesting BED and wiggle file support, which he did not add. Command-line operation was another recurring request. Asked about future development, he says he would favour reimplementing BRIG, imagining an online version with more input types, including GFF. These are retrospective wishes and possible redesign ideas, not capabilities demonstrated in the episode.

## Highlights

- [00:01:14](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=1:14) — BRIG’s sequence inputs, reference-based rings and built-in handling of BLAST.
- [00:03:00](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=3:00) — What the figure communicates, with applications to plasmids, complete genomes and yeast.
- [00:04:16](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=4:16) — BRIG’s longevity and the beer wager that started its development.
- [00:06:55](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=6:55) — CGView, alternative plotting tools and the feedback behind publication-ready figures.
- [00:10:57](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=10:57) — Ease of use, documentation and the choice of Java and Swing.
- [00:12:31](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=12:31) — Why missing unit tests now make major changes difficult.
- [00:13:19](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=13:19) — Managing BLAST subprocesses so they do not keep running after BRIG closes.
- [00:14:09](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=14:09) — JAR packaging, the 50-page manual and optimisation of overlapping BLAST hits.
- [00:17:13](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=17:13) — The fellow PhD student’s colour palette that became BRIG’s default.
- [00:18:01](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=18:01) — Credit for the colour palette, followed by missing formats and reference-based limitations.
- [00:20:39](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=20:39) — Command-line requests and ideas for an online reimplementation.

## In their own words

> It just provides a very simple, I guess, intuitive visualization of what your different genomes look like to a single reference.
>
> — Nabil-Fareed Alikhan, [00:03:00](https://soundcloud.com/microbinfie/28-brig-the-blast-ring-image-generator#t=3:00)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Scott Beatson, Kat Holt.

## Tools and resources mentioned

BRIG, BLAST, BLAST+, CGView, BLAST Atlas, DNAPlotter, CGView server, Java, Swing, Perl, Maven, LaTeX, Read the Docs.

## Questions this episode answers

### What does BRIG do?

BRIG, the BLAST Ring Image Generator, compares input sequences against a selected reference using BLAST and displays the results as concentric rings. It supports annotations and adjustable settings for producing publication-ready figures.

### Do I need to install BLAST separately to use BRIG?

Yes. BRIG runs BLAST for you, but does not install it; you must point BRIG to a BLAST installation. Nabil says it worked with both legacy BLAST and BLAST+, which had only just been released at the time.

### Can BRIG show sequence that is absent from the reference?

Not in the reference-based figure described here. Query sequence without a counterpart in the reference is not displayed, so the plot does not reveal all accessory sequence differences among the queries.

### Does the episode describe a command-line version of BRIG?

Command-line operation is discussed as a recurring request, not as the BRIG workflow presented in the episode. Nabil says he would favour reimplementing the software and discusses possible online operation and additional input formats.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat to Nabil-Fareed Alikhan about the bioinformatics software he
authored called BRIG, the BLAST Ring Image Generator.  Software:
http://brig.sourceforge.net/  Paper: https://bmcgenomics.biomedcentral
.com/articles/10.1186/1471-2164-12-402
