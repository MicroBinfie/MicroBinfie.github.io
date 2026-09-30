---
layout: page
title: 'Episode 97: Advances in sequencing technologies'
date: '2022-12-29 00:00:00'
link: https://soundcloud.com/microbinfie/advances-in-sequencing-technologies
episode: '97'
soundcloud_track: '1405848646'
tags:
- microbinfie
- podcast
description: The hosts compare Nanopore Q20, adaptive sequencing, PacBio HiFi and Illumina long-read plans, and consider the implications for microbial software.
excerpt: The hosts compare Nanopore Q20, adaptive sequencing, PacBio HiFi and Illumina long-read plans, and consider the implications for microbial software.
headline: 'Sequencing advances: Nanopore, PacBio and Illumina'
guests: []
topics:
- microbial bioinformatics
- sequencing technologies
- adaptive sequencing
- pathogen enrichment
- long reads
- paired-end reads
- genome assembly
- sequencing quality
- gpu computing
- software compatibility
faq:
- q: How can Nanopore adaptive sequencing enrich pathogens?
  a: Andrew describes reading an initial stretch of a molecule, deciding whether it matches a target and rejecting unwanted molecules by reversing the pore’s polarity. He cites reported enrichment of roughly 3–10× and gives Listeria and Campylobacter as examples of possible pathogen targets.
- q: What read lengths helped with E. coli assembly in the episode?
  a: Andrew describes a 96-isolate Nanopore experiment in which reads averaging about 1.5 kb performed poorly, while moving towards roughly 5 kb improved the results. The hosts consider reads around 5–6 kb useful for many E. coli assembly problems, while noting that tandem phage repeats can remain difficult.
- q: What Illumina long-read figures were discussed?
  a: Nabil reports advertised figures of a 6–7 kb read N50 and read lengths potentially exceeding 30 kb for the Complete Long Read solution. The hosts separately discuss 300-base paired-end NextSeq reads; they do not present an independent benchmark of the long-read offering.
- q: Did the hosts identify a hard-coded read-length limit in SPAdes or SKESA?
  a: No. Lee asks whether such a constant might exist, and Andrew explains how memory allocations, stack sizes or optimisations could impose assumptions about read length. They do not inspect the source code or verify a particular limit in either assembler.
---

*Sequencing advances: Nanopore, PacBio and Illumina*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan compare sequencing developments they have heard about at conferences and meetings. They discuss Nanopore Q20 chemistry and adaptive sequencing, increased PacBio HiFi throughput, and Illumina’s long-read announcements and longer paired-end reads. The conversation connects these developments to microbial genome assembly, computing requirements and software assumptions that may not accommodate changing read lengths.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 97: Advances in sequencing technologies" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1405848646&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 97: Advances in sequencing technologies on SoundCloud](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies)

## In this episode

### New instruments and Nanopore Q20

Nabil describes encountering an instrument from Element Biosciences that he had not previously heard about. Its apparent ability to address his needs made him curious but also suspicious, and he asks whether listeners have used it. This is a conference roundup rather than a tested comparison: the hosts distinguish promising announcements from equipment and chemistry they have used themselves.

Andrew highlights Nanopore’s Q20 chemistry as a development he wants to try properly. Nabil says published papers suggest that the improvement is real, rather than just promotional claims, but reports that they have not yet got their hands on it.

### Adaptive sequencing for pathogen enrichment

Andrew explains Nanopore adaptive sequencing as a way to accept or reject reads during sequencing. A reference database can guide selection: a run might retain human reads, reject human host contamination, or enrich for pathogens such as Listeria and Campylobacter in an uncultured sample.

In his description, the instrument might read the first 500 bases, identify what it is reading and then accept the molecule or reverse the pore’s polarity to reject it. He cites reported target enrichment of roughly 3–10×, which could make the difference between detecting a pathogen with some genome coverage and barely seeing it. Lee raises the prospect of reducing unwanted data storage, but Andrew clarifies that some sequence is still read before rejection.

### Gaming hardware and integrated computers

The computing needed alongside sequencing leads to a discussion of gaming hardware. Andrew describes using powerful Alienware desktops in the sequencing laboratory. Lee recalls academic labs picking up PS3s for heavy computing; the hosts recall them being stitched together into grid clusters, and Andrew remembers reliability problems associated with memory lacking error correction.

The hosts also discuss Nanopore’s P2 and P2 Solo offerings. Andrew is cautious about computers supplied with sequencers: he recalls earlier Nanopore and PacBio systems whose accompanying computers quickly became underpowered. His laboratory’s plan is to run a P2 Solo using an existing gaming machine with upgrades. Lee notes that the computers his laboratory uses for Nanopore work have capable GPU cards.

### PacBio HiFi and microbial read lengths

Nabil reports that PacBio was emphasising increased HiFi throughput at the meetings he attended. Andrew describes the method as circularising DNA with hairpins and repeatedly reading the same fragment, combining those passes into a higher-quality consensus. Nabil sees the offering as strongly directed towards human genomes, while Andrew contrasts it with the flexibility of stopping a Nanopore run, washing a flow cell and returning to it later.

For microbial assembly, the hosts discuss the practical value of reads several kilobases long. Andrew describes a 96-isolate E. coli Nanopore experiment: an initial attempt averaging about 1.5 kb did not work well, whereas moving towards roughly 5 kb made assembly much more successful. They still acknowledge difficult structures such as tandem phage repeats.

### Illumina announcements and longer paired-end reads

Nabil reports advertised figures for Illumina’s Complete Long Read solution: a read N50 of 6–7 kb and read lengths potentially exceeding 30 kb. He considers around 6 kb useful for many of his E. coli assembly problems. The hosts also discuss NovaSeq announcements, sequencing chemistry changes and easier reagent shipping.

Separately, Andrew describes longer-read NextSeq kits, including discussion of 300-base paired-end reads and the possibility of going further. The hosts compare this with MiSeq and consider potential benefits for covering more 16S hypervariable regions. They recall people pushing sequencing kits beyond their intended lengths, but stress the risk of declining base quality. Lee asks whether longer Illumina reads would require much longer runs; the discussion leaves that question unresolved.

### Read categories and software assumptions

The hosts question whether “short” and “long” remain useful categories as read lengths change. Andrew suggests a possible medium-read category, while Nabil argues that naming the technology might be clearer. Lee’s “fourth generation” and “5G” suggestions are jokes, not proposed technical standards.

Andrew raises a practical compatibility concern: much long-read software does not support paired-end data, while software written for Illumina may assume an upper read-length limit. Lee asks whether SPAdes or SKESA might contain such constants. Andrew suggests that memory allocations, stack sizes or other optimisations could encode assumptions about maximum lengths. They do not inspect either program or establish a specific limit; the point is that longer paired-end reads may require software changes.

## Highlights

- [00:01:14](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=1:14) — Nabil describes an unfamiliar Element Biosciences instrument and asks for user experience.
- [00:01:55](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=1:55) — Andrew discusses Nanopore Q20 chemistry, followed by adaptive sequencing.
- [00:03:25](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=3:25) — Lee recalls PS3 computing clusters and the use of gaming hardware in laboratories.
- [00:05:00](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=5:00) — Andrew questions how well computers supplied with sequencers age.
- [00:06:15](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=6:15) — Adaptive sequencing reads an initial stretch before rejection, with reported 3–10× enrichment.
- [00:06:49](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=6:49) — PacBio’s emphasis on HiFi sequencing and increased throughput.
- [00:08:31](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=8:31) — Illumina’s Complete Long Read announcement and changes to its sequencing offering.
- [00:09:27](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=9:27) — Andrew describes how longer reads improved a 96-isolate E. coli experiment.
- [00:10:31](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=10:31) — Longer-read NextSeq kits and possible applications to 16S sequencing.
- [00:12:11](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=12:11) — Lee raises base-quality concerns and asks about the runtime cost of longer reads.
- [00:13:40](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=13:40) — The hosts debate terminology for short, medium and long reads.
- [00:15:18](https://soundcloud.com/microbinfie/advances-in-sequencing-technologies#t=15:18) — Longer paired-end reads may challenge assumptions in existing sequencing software.

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Nanopore Q20 chemistry, Nanopore adaptive sequencing, Nanopore P2, Nanopore P2 Solo, PacBio HiFi sequencing, Illumina Complete Long Read, Illumina NovaSeq, Illumina NextSeq, Illumina MiSeq, 454, SPAdes, SKESA.

## Questions this episode answers

### How can Nanopore adaptive sequencing enrich pathogens?

Andrew describes reading an initial stretch of a molecule, deciding whether it matches a target and rejecting unwanted molecules by reversing the pore’s polarity. He cites reported enrichment of roughly 3–10× and gives Listeria and Campylobacter as examples of possible pathogen targets.

### What read lengths helped with E. coli assembly in the episode?

Andrew describes a 96-isolate Nanopore experiment in which reads averaging about 1.5 kb performed poorly, while moving towards roughly 5 kb improved the results. The hosts consider reads around 5–6 kb useful for many E. coli assembly problems, while noting that tandem phage repeats can remain difficult.

### What Illumina long-read figures were discussed?

Nabil reports advertised figures of a 6–7 kb read N50 and read lengths potentially exceeding 30 kb for the Complete Long Read solution. The hosts separately discuss 300-base paired-end NextSeq reads; they do not present an independent benchmark of the long-read offering.

### Did the hosts identify a hard-coded read-length limit in SPAdes or SKESA?

No. Lee asks whether such a constant might exist, and Andrew explains how memory allocations, stack sizes or optimisations could impose assumptions about read length. They do not inspect the source code or verify a particular limit in either assembler.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We discuss recent advancements in genome sequencing technologies, based on what we've been
hearing at conferences and within the community.

The Microbial Bioinformatics podcast brought together three experts, Andrew, Lee, and Nabil, to
discuss the latest advances in sequencing technologies. The team explored the new developments
in the market, including a cutting-edge instrument from Element Biosciences that captured
Nabil's attention. Andrew analyzed the adaptive sequencing feature in Illumina that enables the
checkout of unwanted reads.

The discussion highlighted how the computing power of sequencing labs has developed due to
advancements in computers, with gaming computers being repurposed to aid in data analysis.
Illumina's complete long-read solution and NextSeq's kits were also topics of discussion.
Moreover, the team also discussed the increasing popularity of pacbio with its hi-fi sequencing
capabilities to achieve more high fidelity readings.

The experts then discussed how longer reads pave the way for 4th generation sequencing while
also acknowledging the challenges posed by software tools catering to the new technology. While
the developments in sequencing technology seem exciting, Nabil cautioned the panel to not
forget the importance of quality over quantity.

In the second part of the episode, the team moved on to analyze the limitations of sequencing
software, particularly regarding its long-read handling capabilities. Andrew explained how
sequencing software is hard-coded to operate up to 300 paired-ended reads, and exceeding this
limit often leads to software crashes.

Lee asked if there was a constant limit in the source code of Spades or SKESA to limit the
software's ability to handle larger datasets. Andrew answered the query by explaining that
developers may have set some limits on the memory or stack size of the software, leading to
issues when processing larger datasets.

The team concluded by noting that the hard-coding and data processing limitations shouldn't be
considered permanent obstacles as software development is a continuous process. As sequencing
technologies advance, software solutions must also advance to handle increasingly complex
genetic datasets better.
