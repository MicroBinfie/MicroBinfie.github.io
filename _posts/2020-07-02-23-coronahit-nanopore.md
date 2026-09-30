---
layout: page
title: 'Episode 23: CoronaHiT: large scale multiplexing of SARS-CoV-2 genomes on Nanopore'
date: '2020-07-02 00:00:00'
link: https://soundcloud.com/microbinfie/23-coronahit-nanopore
episode: '23'
soundcloud_track: '850174978'
tags:
- microbinfie
- podcast
description: Justin O'Grady and David Baker explain CoronaHiT, a lower-cost method for multiplexing up to 94 SARS-CoV-2 samples on a Nanopore flow cell.
excerpt: Justin O'Grady and David Baker explain CoronaHiT, a lower-cost method for multiplexing up to 94 SARS-CoV-2 samples on a Nanopore flow cell.
headline: 'CoronaHiT: multiplexing 94 SARS-CoV-2 genomes on Nanopore'
guests:
- Justin O'Grady
- David Baker
topics:
- sars-cov-2
- covid-19
- multiplexing
- nanopore sequencing
- amplicon sequencing
- barcode design
- demultiplexing
- genome coverage
- public health surveillance
faq:
- q: How many SARS-CoV-2 samples can CoronaHiT sequence on one MinION flow cell?
  a: The episode describes testing up to 94 samples plus a negative control. Lower multiplexing, such as 48 samples, leaves more coverage available for difficult samples.
- q: How much did CoronaHiT sequencing cost per sample?
  a: Baker quotes approximately £13–£18 per sample, depending on multiplexing, compared with close to £40 for the standard approach discussed. These are the costs reported in the July 2020 episode.
- q: Does CoronaHiT replace the ARTIC PCR protocol?
  a: No. It retains the initial ARTIC amplification and changes the subsequent barcode preparation, using Nextera-based adapter insertion followed by PCR addition of Nanopore barcodes.
- q: Does CoronaHiT still require primer masking?
  a: Yes. Although tagmentation removes some amplicon-end sequence, synthetic primer sequence can remain and must be masked to avoid misleading SNP calls.
---

*CoronaHiT: multiplexing 94 SARS-CoV-2 genomes on Nanopore*

Justin O'Grady and David Baker join Nabil-Fareed Alikhan and Andrew Page to explain CoronaHiT, a method for sequencing up to 94 SARS-CoV-2 samples on one Oxford Nanopore MinION flow cell. They discuss how it combines ARTIC PCR with Nextera-based barcode preparation, reduces costs and fits existing analysis pipelines. This July 2020 episode also examines barcode design, uneven genome coverage and choosing between Nanopore and Illumina as sample numbers change.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 23: CoronaHiT: large scale multiplexing of SARS-CoV-2 genomes on Nanopore" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/850174978&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 23: CoronaHiT: large scale multiplexing of SARS-CoV-2 genomes on Nanopore on SoundCloud](https://soundcloud.com/microbinfie/23-coronahit-nanopore)

## In this episode

### More samples at a lower cost

CoronaHiT was developed to increase throughput and reduce the cost of SARS-CoV-2 sequencing without losing Nanopore's rapid turnaround. The standard approach discussed handled 23 samples plus a negative control, costing close to £40 per sample depending on reagent sourcing. David Baker puts CoronaHiT at approximately £13–£18 per sample, depending on multiplexing.

The team tested 48 and 94 samples on a single flow cell. The 94-sample configuration uses 95 barcodes including the negative control: one of the original 96 did not work. The accompanying preprint is identified in the show notes by DOI: 10.1101/2020.06.24.162156.

### Keeping ARTIC PCR, changing barcode preparation

CoronaHiT retains the initial RNA, cDNA and ARTIC PCR stages. ARTIC produces roughly 98 overlapping fragments of about 400 base pairs, covering the approximately 30 kb SARS-CoV-2 genome. Instead of adding native barcodes by ligation, CoronaHiT uses a modified low-input Nextera approach to introduce adapters, then PCR enrichment to add 24-base Nanopore barcodes.

Switching requires additional primers and a Nextera kit, but otherwise uses standard laboratory equipment. Tagmentation can remove sequence from amplicon ends; overlaps of up to about 100 bases help maintain coverage. The discussion also notes that Nextera XT was already being used for Illumina sequencing of COVID samples.

### From a PacBio experiment to Nanopore barcodes

Andrew Page recalls discussing Baker's multiplexing idea during a flight to MRC Gambia. The initial work involved bacterial samples and PacBio sequencing. Baker subsequently tried leftover pooled material on a Nanopore flow cell and found that it performed well even without the size selection used for the PacBio preparation.

Early tests used 16-base PacBio barcodes, including a run with 158 samples, but demultiplexing was inadequate. Moving to 24-base Nanopore barcodes improved separation and compatibility with Guppy. Additional flanking sequence helped protect against losing barcode bases at fragment ends. Custom barcode designs required more work, such as configuring Porechop.

### Why total yield does not determine sample capacity

The panel describes approximately 12 Gb from an ARTIC Nanopore run lasting 24–36 hours. In principle, that is ample data for many small viral genomes. In practice, the limiting factor is uneven amplification: different primer pairs can produce coverage differences of roughly a thousand-fold across the genome.

Consequently, they describe needing at least 1,000-fold overall genome coverage to recover enough data from poorly covered regions. This constrains multiplexing despite the apparently generous total yield. Further primer optimisation can improve one region while worsening another. Splitting the multiplex PCR into more reactions might help, but would add cost and preparation time.

### Checking consensus sequences and selecting samples

Andrew reports comparing the same samples using Illumina, standard ARTIC Nanopore sequencing and CoronaHiT. With comparable coverage, they obtained matching consensus sequences, checked every SNP and found consistent phylogenetic results. Despite tagmentation, primer masking remains essential: some synthetic primer sequence survives, and a false SNP matters when genomes differ at only a few positions.

Sample quality also affects multiplexing. A Ct below 30 is discussed as a possible selection threshold for easier samples; including harder samples may favour reducing a run to 48. An alternative is assessing ARTIC PCR success, with a suggested concentration threshold above 2 ng/µl. That preserves the opportunity to recover some higher-Ct samples, but incurs PCR costs before rejection.

### Matching the platform to changing demand

For consistently large batches, Baker favours Illumina and describes obtaining up to 120 Gb from a high-output NextSeq run. Nanopore offers flexibility when only a few samples arrive: sequencing can be monitored in real time, stopped, and the flow cell washed for reuse with different barcodes.

That flexibility became more useful as local demand fell from hundreds to tens of samples per week. Waiting to fill an Illumina run could delay information about clusters and outbreaks. The panel also considers anticipated native 96-barcode kits from Oxford Nanopore, but cannot yet make a firm comparison: ligase requirements and workflow complexity would influence their cost and convenience.

## Highlights

- [00:01:37](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=1:37) — CoronaHiT's aims: higher throughput and lower sequencing costs
- [00:02:40](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=2:40) — Using Nextera adapters and PCR to add Nanopore barcodes
- [00:05:49](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=5:49) — Testing 48 and 94 samples, barcode crosstalk and Guppy compatibility
- [00:08:06](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=8:06) — The multiplexing idea's origins in a conversation about PacBio
- [00:12:59](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=12:59) — How tagmentation affects the ends of overlapping ARTIC amplicons
- [00:14:28](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=14:28) — Why residual synthetic primer sequence still needs masking
- [00:15:28](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=15:28) — Uneven amplicon coverage limits the number of genomes per flow cell
- [00:18:02](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=18:02) — Choosing Illumina for large batches or Nanopore for flexible turnaround
- [00:22:06](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=22:06) — Comparing consensus sequences and SNPs across three sequencing approaches
- [00:24:59](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=24:59) — Using ARTIC PCR concentration as an alternative to a Ct cutoff
- [00:25:59](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=25:59) — Potential competition from native 96-barcode Nanopore kits

## In their own words

> So essentially being able to process more samples more quickly at a lower cost.
>
> — David Baker, [00:01:37](https://soundcloud.com/microbinfie/23-coronahit-nanopore#t=1:37)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)
- **Justin O'Grady** (guest, Quadram Institute Bioscience; University of East Anglia)
- **David Baker** (guest, Quadram Institute Bioscience)

## Tools and resources mentioned

CoronaHiT, ARTIC protocol, Nextera, Nextera XT, Guppy, Porechop, Oxford Nanopore MinION, Illumina NextSeq, PacBio Sequel, TapeStation, Qubit.

## Questions this episode answers

### How many SARS-CoV-2 samples can CoronaHiT sequence on one MinION flow cell?

The episode describes testing up to 94 samples plus a negative control. Lower multiplexing, such as 48 samples, leaves more coverage available for difficult samples.

### How much did CoronaHiT sequencing cost per sample?

Baker quotes approximately £13–£18 per sample, depending on multiplexing, compared with close to £40 for the standard approach discussed. These are the costs reported in the July 2020 episode.

### Does CoronaHiT replace the ARTIC PCR protocol?

No. It retains the initial ARTIC amplification and changes the subsequent barcode preparation, using Nextera-based adapter insertion followed by PCR addition of Nanopore barcodes.

### Does CoronaHiT still require primer masking?

Yes. Although tagmentation removes some amplicon-end sequence, synthetic primer sequence can remain and must be masked to avoid misleading SNP calls.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat with the authors of CoronaHiT which lets you sequence up to 94
SARS-CoV-2 samples on a single MinION flowcell. This reduces the cost
of sequencing 3-fold, with a simpler, faster protocol. Justin O'Grady
and David Baker join Andrew Page and Nabil-Fareed Alikhan to chat
about how it all works, how it came into being and why its awesome.
Preprint: https://doi.org/10.1101/2020.06.24.162156
