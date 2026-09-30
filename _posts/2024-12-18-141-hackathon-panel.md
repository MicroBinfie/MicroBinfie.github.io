---
layout: page
title: 'Episode 141: Hackathon panel'
date: '2024-12-18 00:00:00'
link: https://soundcloud.com/microbinfie/141-hackathon-panel
episode: '141'
soundcloud_track: '1992914191'
tags:
- microbinfie
- podcast
description: A hackathon panel on cgMLST, Nanopore workflows, complete genomes and the limits of routine analysis in public health.
excerpt: A hackathon panel on cgMLST, Nanopore workflows, complete genomes and the limits of routine analysis in public health.
headline: MLST, Nanopore and the push for complete microbial genomes
guests:
- Torsten
- Fin
topics:
- microbial bioinformatics
- public health genomics
- cgmlst
- nanopore
- complete genomes
- structural variation
- variant calling
- fungal genomics
- antimicrobial resistance
- wastewater surveillance
faq:
- q: Will the new PulseNet cgMLST caller support seven-gene MLST?
  a: Lee says the caller can report the seven genes when supplied. He also explains that the broader PulseNet 2.0 pipeline incorporates an existing seven-gene MLST caller alongside its other modules.
- q: Why are complete microbial genomes not yet routine in public health?
  a: The panel points to residual indel errors, the need for manual validation and judgement, and limitations in high-throughput automation. Lee says Illumina remains the established automated option across public-health laboratories.
- q: Why does Nanopore basecalling choice matter?
  a: Andrew says rapid basecalling can sacrifice accuracy compared with more computationally demanding methods. The panel also cautions that convenient built-in workflows may prioritise quick results rather than the most accurate analysis for a particular task.
- q: Why are long reads useful for studying fungal antimicrobial resistance?
  a: The panel explains that resistance can depend on multiple or tandem copies of a gene rather than simply its presence. Measuring those repeats and their extent is therefore important for inferring phenotype.
- q: Can a wastewater AMR gene be linked to a particular pathogen?
  a: Not necessarily. The panel notes that short, fragmented DNA may reveal an AMR gene without enough surrounding context to identify its host, leaving a useful surveillance signal rather than a directly actionable organism-level result.
---

*MLST, Nanopore and the push for complete microbial genomes*

Andrew Page and Lee Katz join Torsten and Fin at the ASM NGS Hackathon in Bethesda, Maryland, to discuss missing tools and resources in microbial bioinformatics. The panel considers new allele callers, Nanopore analysis, structural variation and the practical barriers to making complete genomes routine. Fungal infections and wastewater surveillance illustrate why better assemblies alone will not answer every public-health question.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 141: Hackathon panel" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1992914191&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 141: Hackathon panel on SoundCloud](https://soundcloud.com/microbinfie/141-hackathon-panel)

## In this episode

### Seven-gene MLST and the next cgMLST caller

Lee revisits an MLST hashing idea discussed in earlier episodes and anticipates a new cgMLST caller through PulseNet and PulseNet International. Andrew distinguishes this from seven-gene MLST, which Lee describes as an already solved problem.

The discussion separates the core cgMLST module from the broader PulseNet 2.0 pipeline, which includes public-health analyses such as serotyping. Lee says the caller can report the seven genes when supplied, while the broader pipeline incorporates an existing seven-gene MLST caller. The panel also asks how generalisable individual modules are beyond their original tasks.

### Nanopore workflows need clearer guidance

The panel sees a gap between growing Nanopore adoption and the maturity of its analysis tools, particularly as laboratories in low- and middle-income countries begin using genomics. Assembly protocols, variant-calling choices and interpretation of results remain unsettled. Flye is discussed as a commonly used assembler, with concerns about duplication of regions expected to be single-copy. Changing Nanopore chemistry also makes error profiles harder to treat as fixed.

Andrew stresses that basecalling choices matter. He contrasts rapid basecalling with more computationally demanding, highly accurate methods requiring GPUs with substantial memory, illustrating the difference as roughly 92% versus 99% accuracy. Another panellist cautions that built-in EPI2ME workflows can favour speed and computational efficiency over maximum accuracy, citing comparisons of influenza analysis workflows.

### Typing structural variation in complete genomes

Long reads raise the prospect of using structural variation alongside allele-based typing. Andrew describes socru, his tool for typing fully complete, circularised genomes according to the order of major chromosomal blocks between ribosomal operons. Its naming scheme provides a way to compare genome organisation rather than only individual sequences.

A panellist asks why closed genomes have not yet become the field's standard unit of analysis, replacing routine read-to-reference comparisons with genome-to-genome comparisons. Ryan Wick and Unicycler are mentioned in this context. The concern is not simply whether an assembly closes: even ten remaining indel errors can leave frameshifted genes and disrupt downstream analyses such as pangenomics. The panel also discusses pling, which uses double-cut-and-join distances to compare plasmid structures.

### Manual validation and variant-calling benchmarks

Complete assemblies still require investigation and judgement. One panellist describes building manually validated local reference genomes in a hospital laboratory to help detect sequencing problems. Trycycler is presented as a useful tool whose manual decisions remain a barrier to high-throughput clinical and public-health use. Lee argues that Illumina still provides the established automation and instrument availability across public-health laboratories.

The panel discusses Michael Hall's Nanopore variant-calling benchmark, described as available on bioRxiv and newly published in eLife. It compares approaches across different bacteria and Nanopore data, including Clair3 and FreeBayes. A panellist reports that Nanopore's machine-learning models performed best, while expressing concern about adapting models as chemistry changes. Another notes that the Bayesian model in FreeBayes complicates a simple distinction between machine-learning and non-machine-learning approaches.

### Unusual infections and fungal resistance

Performance on well-characterised bacteria may not transfer reliably to the unusual organisms that hospital laboratories sequence precisely because a case is difficult. The panel describes uncommon mould infections for which only a distantly related reference genome may be available, making misassemblies harder to recognise.

Candida auris provides a fungal example. Long reads are needed not only for assembly but also to measure multiple or tandem copies of resistance-associated genes: copy number can affect phenotype. Lee also raises epigenomics, clarified as including methylation, while acknowledging that its practical benefits are not yet fully understood.

### What wastewater AMR signals can tell us

Lee asks whether an antimicrobial-resistance gene detected in wastewater can be connected to an organism of public-health importance. The panel identifies a fundamental phasing limitation: a tiny DNA fragment from a plasmid cannot establish that wider context.

They distinguish broad surveillance from an actionable response. A single AMR gene can provide useful surveillance information without identifying its host, whereas detecting something such as polio raises a different prospect for tracing and investigation.

## Highlights

- [00:00:35](https://soundcloud.com/microbinfie/141-hackathon-panel#t=0:35) — MLST hashing and an anticipated PulseNet cgMLST caller
- [00:02:21](https://soundcloud.com/microbinfie/141-hackathon-panel#t=2:21) — Gaps in Nanopore assembly and variant-calling tools as adoption grows
- [00:03:32](https://soundcloud.com/microbinfie/141-hackathon-panel#t=3:32) — Why basecalling settings need clearer guidance
- [00:04:47](https://soundcloud.com/microbinfie/141-hackathon-panel#t=4:47) — Speed and accuracy trade-offs in built-in Nanopore workflows
- [00:05:42](https://soundcloud.com/microbinfie/141-hackathon-panel#t=5:42) — Andrew describes socru for typing complete genome organisation
- [00:06:18](https://soundcloud.com/microbinfie/141-hackathon-panel#t=6:18) — Why closed genomes are not yet the routine unit of analysis
- [00:07:27](https://soundcloud.com/microbinfie/141-hackathon-panel#t=7:27) — Plasmid structural comparisons with pling and the need for validation
- [00:08:52](https://soundcloud.com/microbinfie/141-hackathon-panel#t=8:52) — Illumina's established role in high-throughput public-health workflows
- [00:09:35](https://soundcloud.com/microbinfie/141-hackathon-panel#t=9:35) — Michael Hall's benchmark of Nanopore variant-calling approaches
- [00:10:49](https://soundcloud.com/microbinfie/141-hackathon-panel#t=10:49) — Epigenomics and the still-uncertain benefits of methylation analysis
- [00:11:39](https://soundcloud.com/microbinfie/141-hackathon-panel#t=11:39) — Long reads for fungal genomes and resistance-associated gene copies
- [00:12:19](https://soundcloud.com/microbinfie/141-hackathon-panel#t=12:19) — The difficulty of linking wastewater AMR genes to their biological context

## In their own words

> But I think that the real automation right now is with Illumina and that's why we haven't really gotten there yet.
>
> — Lee Katz, [00:08:52](https://soundcloud.com/microbinfie/141-hackathon-panel#t=8:52)

## Who is talking

- **Andrew Page** (host)
- **Lee Katz** (host)
- **Torsten** (guest)
- **Fin** (guest)

Also mentioned: Ryan Wick, Michael Hall.

## Tools and resources mentioned

MLST, cgMLST, MLST hashing, PulseNet 2.0, Illumina, Oxford Nanopore, Flye, EPI2ME, socru, Unicycler, Trycycler, pling, Clair3, FreeBayes, Double-cut-and-join distance.

## Questions this episode answers

### Will the new PulseNet cgMLST caller support seven-gene MLST?

Lee says the caller can report the seven genes when supplied. He also explains that the broader PulseNet 2.0 pipeline incorporates an existing seven-gene MLST caller alongside its other modules.

### Why are complete microbial genomes not yet routine in public health?

The panel points to residual indel errors, the need for manual validation and judgement, and limitations in high-throughput automation. Lee says Illumina remains the established automated option across public-health laboratories.

### Why does Nanopore basecalling choice matter?

Andrew says rapid basecalling can sacrifice accuracy compared with more computationally demanding methods. The panel also cautions that convenient built-in workflows may prioritise quick results rather than the most accurate analysis for a particular task.

### Why are long reads useful for studying fungal antimicrobial resistance?

The panel explains that resistance can depend on multiple or tandem copies of a gene rather than simply its presence. Measuring those repeats and their extent is therefore important for inferring phenotype.

### Can a wastewater AMR gene be linked to a particular pathogen?

Not necessarily. The panel notes that short, fragmented DNA may reveal an AMR gene without enough surrounding context to identify its host, leaving a useful surveillance signal rather than a directly actionable organism-level result.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Andrew, Lee, Torsten, and Fin muse over the future of MLST, Illumina, and Nanopore at the ASM
NGS Hackathon
