---
layout: page
title: 'Episode 56: SARS-CoV-2 And Sequencing Spike With Sanger Sequencing part 2'
date: '2021-04-21 00:00:00'
link: https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995
episode: '56'
soundcloud_track: '1019140078'
tags:
- microbinfie
- podcast
description: Kai Blin and Tue Jorgensen explain a $5 Sanger screen for SARS-CoV-2 variants, its Ct limits and browser-based analysis without data uploads.
excerpt: Kai Blin and Tue Jorgensen explain a $5 Sanger screen for SARS-CoV-2 variants, its Ct limits and browser-based analysis without data uploads.
headline: SARS-CoV-2 variant screening with $5 Sanger sequencing
guests:
- Kai Blin
- Tue Jorgensen
topics:
- sars-cov-2
- variant screening
- sanger sequencing
- qpcr
- ct values
- contamination control
- webassembly
- data privacy
- public health bioinformatics
faq:
- q: How much does the Sanger variant screen cost?
  a: The guests report $5 per sample from end to end, including plasticware. They describe costs as scaling linearly with sample numbers, without the minimum batch requirement associated with starting an Illumina run.
- q: How well does the method work at high Ct values?
  a: They report about 90% success up to Ct 30 on their DTU system, falling to about 25% at Ct 35 on that system. They stress that Ct values depend on the qPCR setup and that their assay includes seven initial dark cycles; no formal limit-of-detection study had been performed.
- q: Does the browser app upload patient sample data?
  a: According to the guests, the BioLib implementation runs the analysis locally in the browser using WebAssembly. Sample data remains on the user's computer, and the browser provides the results for download.
- q: How long does the analysis take?
  a: The browser implementation is described as taking three to four minutes for 100 samples, compared with about ten seconds outside that environment. Laboratory hands-on work consists of setting up a PCR and about five minutes transferring product into a new plate.
- q: Can the software be updated to screen additional mutations?
  a: For mutations within the existing sequencing window, the guests describe adding an entry to a dictionary in the code and making a new release. They estimate roughly five minutes of work for that change.
---

*SARS-CoV-2 variant screening with $5 Sanger sequencing*

In part two of this discussion, Kai Blin and Tue Jorgensen from the Technical University of Denmark join the hosts to explain their SARS-CoV-2 variant-screening workflow using Sanger sequencing. They discuss performance at low viral loads, contamination controls and a reported cost of $5 per sample. The software discussion centres on making analysis accessible to laboratories without dedicated bioinformatics staff while keeping sample data on the user's computer.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 56: SARS-CoV-2 And Sequencing Spike With Sanger Sequencing part 2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1019140078&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 56: SARS-CoV-2 And Sequencing Spike With Sanger Sequencing part 2 on SoundCloud](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995)

## In this episode

### Why return to Sanger sequencing?

The guests describe choosing Sanger sequencing because it was the simplest approach they thought would work for screening SARS-CoV-2 variants. One guest, accustomed to Nanopore and Illumina sequencing, had not used Sanger sequencing since starting a master's thesis in 2008. The decision prompted someone to write jokingly, "welcome to 1995", but the practical argument was cost and simplicity rather than novelty.

The reported cost is $5 per sample from end to end, including plasticware. Unlike an Illumina run, the workflow does not require accumulating a minimum batch before starting. Costs scale linearly with sample numbers. The guests also emphasise the absence of multiplexing, demultiplexing and assembly, with approximately 300 kilobytes of data per sequence.

### Ct values and sequencing success

The guests caution that Ct values cannot be compared directly across qPCR systems. Their DTU assay has seven initial dark cycles before recording Ct; because those cycles use a higher annealing temperature, they describe an adjustment of about five ordinary cycles when comparing with other setups.

They report roughly 90% success up to Ct 30 on their system, which they compare with approximately Ct 35 elsewhere. Success then falls, reaching about 25% at Ct 35 on their own system. They mention running 45 cycles of PCR. An initial batch had an overall reported efficiency of 85%, including samples that recorded only one target in the qPCR.

There was no formal limit-of-detection study. Instead, the manuscript compares sample Ct values with whether sequencing produced a result. The workflow attempts samples showing any target signal in the diagnostic qPCR, rather than imposing its own positive-result cutoff.

### Laboratory separation and controls

Contamination control relies on physical separation and staff practices already used by the diagnostic laboratory. Master mix preparation, PCR setup, PCR running and post-PCR transfer take place in separate rooms. Anyone entering the post-PCR room cannot return to the earlier rooms. Negative controls are distributed randomly through the workflow.

The guests report occasional isolated position calls in negative controls, but no full-length sequence from one. They were not running a positive control, although a high-titre control had been considered and SSI had suggested one. Their rationale was that this screen reports successful calls rather than interpreting a failure to obtain sequence as a diagnostic negative.

Hands-on work is described as setting up one PCR and spending about five minutes transferring product into a new plate.

### Browser analysis without sample uploads

The command-line tool was convenient for development, but the intended users included hospitals and regional testing centres without dedicated bioinformatics staff. Even running a command line could be a barrier. A conventional upload-based service would also raise concerns about sending patient sample data to an external website.

BioLib provided an alternative using WebAssembly to run the analysis inside the browser. The discussion names Bowtie, samtools, Tracy and a Python interpreter as components of this environment. Users supply their input, run the analysis and receive text output and a downloadable results archive; the sample data remains on their computer.

The convenience has a performance cost: approximately 100 samples take three to four minutes in the browser, compared with about ten seconds otherwise. The guests consider that acceptable within a workflow taking roughly a day or two, and say their day-to-day laboratory users use the BioLib page.

### Simple controls and maintainable software

The browser interface deliberately exposes few choices. The guests argue that this suits a narrowly defined public-health task, while acknowledging that the same simplicity would not extend to a more complex analysis pipeline. Lee Katz questions whether a one-button interface remains easy when something goes wrong.

The command-line version offers additional options. One example concerns finding an arginine substitution when the requested screen expected histidine: an optional setting can report the alternative rather than only the specified mutation.

Other users run the software on a cluster with Singularity. Bioconda provides another installation route, including dependencies. Adding a mutation within the existing sequencing window is described as roughly five minutes of work: edit the mutation dictionary and make a release. Keeping that maintenance burden small matters because this is an important side project.

### Sharing the method and documenting its performance

The protocol is available through protocols.io, the software through the covid-spike-classification GitHub repository, and browser analysis through the SSI BioLib page. The guests distinguish these practical resources from the preprint, which documents the calls generated by the method and how well it works.

They describe reaching full production in less than a week and discussing adoption with representatives from two African countries whose COVID-19 testing units already had Sanger sequencing. They did not know whether those laboratories had subsequently started using the method.

Publication also brought an administrative obstacle. After bioRxiv declined the submission, medRxiv required ethics documentation. According to the guest, the anonymised study did not require Danish ethics approval, so they needed to obtain confirmation of that position for the submission.

## Highlights

- [00:00:59](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=0:59) — How rising Ct values and falling viral load affect the method
- [00:04:30](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=4:30) — Choosing Sanger sequencing as the simplest workable approach
- [00:05:23](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=5:23) — Physical laboratory separation and negative controls for contamination
- [00:08:25](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=8:25) — Discussing adoption with testing laboratories in two African countries
- [00:09:06](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=9:06) — Preprint submission and Danish ethics-approval documentation
- [00:10:45](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=10:45) — Making software usable without dedicated bioinformatics staff
- [00:11:48](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=11:48) — Moving beyond the command line to browser-local WebAssembly analysis
- [00:14:37](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=14:37) — Browser runtime versus dependency-management convenience
- [00:16:51](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=16:51) — Restricting options and reporting specified versus alternative mutations
- [00:21:32](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=21:32) — Cluster installations, Singularity, Bioconda and software releases
- [00:23:41](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=23:41) — Linear sample costs without a minimum sequencing batch

## In their own words

> Like it costs $5 to run a sample from end to end, including all plasticware, including everything.
>
> — a guest, [00:03:45](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=3:45)

> The old stuff still works.
>
> — Lee Katz, [00:04:05](https://soundcloud.com/microbinfie/56-sars-cov-2-and-sequencing-spike-with-sanger-sequencing-welcome-to-1995#t=4:05)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Kai Blin** (guest, Technical University of Denmark)
- **Tue Jorgensen** (guest, Technical University of Denmark)

## Tools and resources mentioned

Sanger sequencing, PCR, qPCR, covid-spike-classification, BioLib, Tracy, Bowtie, samtools, WebAssembly, Python, Rust, LLVM, Singularity, Bioconda, GitHub, protocols.io.

## Questions this episode answers

### How much does the Sanger variant screen cost?

The guests report $5 per sample from end to end, including plasticware. They describe costs as scaling linearly with sample numbers, without the minimum batch requirement associated with starting an Illumina run.

### How well does the method work at high Ct values?

They report about 90% success up to Ct 30 on their DTU system, falling to about 25% at Ct 35 on that system. They stress that Ct values depend on the qPCR setup and that their assay includes seven initial dark cycles; no formal limit-of-detection study had been performed.

### Does the browser app upload patient sample data?

According to the guests, the BioLib implementation runs the analysis locally in the browser using WebAssembly. Sample data remains on the user's computer, and the browser provides the results for download.

### How long does the analysis take?

The browser implementation is described as taking three to four minutes for 100 samples, compared with about ten seconds outside that environment. Laboratory hands-on work consists of setting up a PCR and about five minutes transferring product into a new plate.

### Can the software be updated to screen additional mutations?

For mutations within the existing sequencing window, the guests describe adding an entry to a dictionary in the code and making a new release. They estimate roughly five minutes of work for that change.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Part 2 going through a new method for identifying variants of concern
using Sanger sequencing, and we’re joined by two of the authors of
this method Kai Blin and Tue Jorgensen, both from the Technical
University of Denmark.  The preprint:
www.medrxiv.org/content/10.1101/2….03.27.21252266v1  The protocol:
www.protocols.io/view/sanger-sequ…-2-spik-bsbdnai6  The software:
github.com/kblin/covid-spike-classification  The web app:
ssi.biolib.com/app/covid-spike-classification/run
