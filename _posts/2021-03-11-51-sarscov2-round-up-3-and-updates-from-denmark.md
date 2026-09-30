---
layout: page
title: 'Episode 51: SARSCOV2 Round-up 3 and updates from Denmark'
date: '2021-03-11 00:00:00'
link: https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark
episode: '51'
soundcloud_track: '1004378554'
tags:
- microbinfie
- podcast
description: Denmark's SARS-CoV-2 sequencing coverage, emerging variants, public health workflows and practical checks for contamination and sample swaps.
excerpt: Denmark's SARS-CoV-2 sequencing coverage, emerging variants, public health workflows and practical checks for contamination and sample swaps.
headline: 'SARS-CoV-2 in Denmark: variants, sequencing and quality control'
guests:
- Mads Albertsen
topics:
- sars-cov-2
- denmark
- genomic surveillance
- variants of concern
- sequencing protocols
- within-host diversity
- phylogenetics
- lineage assignment
- quality control
- sample tracking
faq:
- q: How much SARS-CoV-2 sequencing was Denmark doing in March 2021?
  a: At the 9 March recording, Mads Albertsen reported attempted sequencing for more than 90% of cases during most of the year so far. About 70% of cases produced genomes meeting the programme's completeness criterion.
- q: Why did the panel criticise assembling ARTIC reads with SPAdes?
  a: Andrew Page argued that conventional assembly was inappropriate for the ARTIC amplicon data being assessed and explained the poor assembly metrics. He stressed understanding the sequencing protocol and generating consensus sequences for this workflow.
- q: How should an unexpected SARS-CoV-2 lineage call be checked?
  a: The panel recommends checking whether the expected lineage-defining mutations are actually present. Page describes a misleading P.1 assignment and points to Public Health England's machine-readable variant definitions as a resource for validation.
- q: How can sequencing teams detect plate swaps or rotations?
  a: The episode describes comparing sequencing success with diagnostic Ct patterns and checking expected empty wells or negative-control positions. Page also discusses using residual human reads to compare recorded sex with sample layout, with those reads removed before public deposition.
---

*SARS-CoV-2 in Denmark: variants, sequencing and quality control*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan are joined by Mads Albertsen to discuss SARS-CoV-2 genomic surveillance in Denmark. Recorded on 9 March 2021, the conversation covers emerging variants, public health analysis tools, sequencing papers and the limits of automated lineage calls. Practical examples show why contamination checks, sample tracking and manual review remain important even in high-throughput sequencing programmes.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 51: SARSCOV2 Round-up 3 and updates from Denmark" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1004378554&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 51: SARSCOV2 Round-up 3 and updates from Denmark on SoundCloud](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark)

## In this episode

### Denmark's high-coverage surveillance

At the time of recording, Denmark was attempting to sequence more than 90% of SARS-CoV-2 cases, with about 70% of cases producing genomes meeting its completeness criterion. Mads Albertsen describes watching B.1.1.7 rise to roughly 80% while previously circulating lineages declined. B.1.525, which carries E484K, represented a few per cent; the discussion mentions around 200 cases.

Denmark was reopening after suppressing transmission, and Albertsen expected some other variants to continue circulating rather than B.1.1.7 necessarily reaching 100%. The surveillance programme aimed to support variant-specific interventions through extensive testing, sequencing and targeted testing around suspected community spread. Most other variants of concern had been associated with travel, although increasing imports were making containment harder. Denmark's public statistics page used an automatically generated R Markdown report: essentially the same breakdown supplied to government, published online a few days later.

### Variant terminology and analysis tools

The panel distinguishes variants of concern, variants under investigation and variants of interest, while criticising inconsistent usage between countries and organisations. B.1.1.7, B.1.351 and P.1 frame the discussion, alongside newer lineages and recurring mutations. A central request is to release sequence data and coordinate lineage assignments before announcing a newly identified variant. The hosts also note the WHO's work on definitions.

For communicating surveillance results, the conversation covers Tableau, Microreact, Nextstrain and outbreak.info. The latter is described as a resource for geographically organised case information, doubling rates and downloadable metadata. A proposed Galaxy public health community prompts discussion of accessible, click-based analysis and the XML wrappers developers write to add tools. The panel also highlights a SARS-CoV-2 Nextflow pipeline on GitLab that extends processing beyond variant calls and consensus sequences to tree creation and visualisation.

### Sequencing protocols and pooled samples

Andrew Page criticises the approach in A Comparison of Performance for Different SARS-Cov-2 Sequencing Protocols: assembling ARTIC amplicon data with SPAdes and then assessing the resulting poor assemblies. His warning is that archived reads cannot be interpreted sensibly without understanding how they were generated. For the amplicon workflow under discussion, the intended output is a consensus sequence rather than a conventional de novo assembly.

The panel then examines Before the Surge: Molecular Evidence of SARS-CoV-2 in New York City Prior to the First Report. The concern is that samples from ten patients were pooled to obtain consensus genomes, which were deposited in GISAID without a way to distinguish them from individual-sample genomes. Such data could mislead analyses of mixed variants or recombination. The speakers distinguish pooling for diagnostic screening from sequencing individual infections: pooled sequence data need explicit labelling and a repository that preserves that distinction.

### Within-host diversity and phylogenetic masking

SARS-CoV-2 within-host diversity and transmission receives a positive assessment. The Oxford work used hybrid capture rather than the ARTIC protocol, allowing clearer examination of minority variants in the study. Page notes a limitation with high-Ct samples, but highlights observations of minority variants passing between people, sometimes alongside the dominant variant.

A listener-style question asks about up-to-date masking strategies for SARS-CoV-2 phylogenetics. The discussion raises independently recurring mutations as a complication for tree interpretation; the show notes provide resources on problematic sites and a masking VCF. One of the panellists explains that they no longer build global trees. Instead, they assign lineages and construct smaller trees for particular lineages or questions of interest.

### Checking lineage assignments

Page describes an apparent P.1 detection that did not withstand inspection. The genome came from an under-sequenced African setting and was 18 SNPs from its nearest observed ancestor. Only about one of the dozen mutations expected for P.1 was present. The example illustrates how incomplete geographical sampling can produce misleading lineage assignments and how much transmission may remain invisible between sampled genomes.

For important calls, the recommendation is to check the expected defining mutations rather than accept a label uncritically. Public Health England's machine-readable variant definitions provide one resource for doing this. Lee Katz and Page debate YAML versus VCF: YAML offers flexibility for expressing definitions, while Katz emphasises VCF's compatibility with existing pipelines and software such as BCFtools.

### Quality control at 100,000 samples

Albertsen describes four negative controls per plate, checks for unexpectedly long branches and scrutiny of ambiguous base calls. In his experience, most apparent internal variation of this kind was contamination. An R Markdown report brings trees and SNP information together for manual review. Page likewise describes checking important or unusual samples by hand, including whether their mutation patterns make sense for the assigned lineage.

Having quality-controlled around 100,000 samples, Albertsen had encountered sample and plate mix-ups. Comparing sequencing success with the pattern of diagnostic Ct values could reveal swapped plates. In Denmark's setup, success began declining around Ct 32 and fell well below 50% above Ct 35, although Ct values were not directly comparable across testing setups.

Page describes another check using residual human reads to assess whether recorded sex matched the sample layout, helping investigate plate rotations or swaps. Those reads were removed before public deposition. Expected empty wells and negative-control positions offered additional clues.

## Highlights

- [00:01:24](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=1:24) — Why VOC, VUI and VOI terminology needs coordination
- [00:05:40](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=5:40) — Denmark attempts sequencing for more than 90% of cases
- [00:06:13](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=6:13) — B.1.1.7 reaches roughly 80% in Denmark as other lineages decline
- [00:08:55](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=8:55) — R Markdown powers Denmark's public and government reporting
- [00:10:48](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=10:48) — outbreak.info and a proposed Galaxy public health community
- [00:13:40](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=13:40) — A SARS-CoV-2 Nextflow pipeline adds tree creation and visualisation
- [00:14:37](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=14:37) — Criticism of assembling ARTIC amplicon data with SPAdes
- [00:17:10](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=17:10) — Pooled patient samples create interpretation problems in GISAID
- [00:19:38](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=19:38) — Hybrid capture reveals within-host diversity and transmission
- [00:21:49](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=21:49) — An apparent P.1 call exposes the risks of incomplete sampling
- [00:26:04](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=26:04) — Negative controls, ambiguous calls and contamination checks
- [00:29:12](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=29:12) — Using Ct patterns to detect sample and plate mix-ups

## In their own words

> This is a mix of ideas that just shouldn't have been mixed, pooling and genome sequencing.
>
> — Lee Katz, [00:17:51](https://soundcloud.com/microbinfie/51-sarscov2-round-up-3-and-updates-from-denmark#t=17:51)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Mads Albertsen** (guest, Center for Microbial Communities, Aalborg University)

## Tools and resources mentioned

Tableau, Microreact, outbreak.info, R Markdown, Nextstrain, Galaxy, Nextflow, ARTIC protocol, SPAdes, GISAID, BCFtools, ProblematicSites_SARS-CoV2.

## Questions this episode answers

### How much SARS-CoV-2 sequencing was Denmark doing in March 2021?

At the 9 March recording, Mads Albertsen reported attempted sequencing for more than 90% of cases during most of the year so far. About 70% of cases produced genomes meeting the programme's completeness criterion.

### Why did the panel criticise assembling ARTIC reads with SPAdes?

Andrew Page argued that conventional assembly was inappropriate for the ARTIC amplicon data being assessed and explained the poor assembly metrics. He stressed understanding the sequencing protocol and generating consensus sequences for this workflow.

### How should an unexpected SARS-CoV-2 lineage call be checked?

The panel recommends checking whether the expected lineage-defining mutations are actually present. Page describes a misleading P.1 assignment and points to Public Health England's machine-readable variant definitions as a resource for validation.

### How can sequencing teams detect plate swaps or rotations?

The episode describes comparing sequencing success with diagnostic Ct patterns and checking expected empty wells or negative-control positions. Page also discusses using residual human reads to compare recorded sex with sample layout, with those reads removed before public deposition.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We discuss the latest developments in SARS-CoV-2 genomics over the
last 2 weeks with Mads Albertsen and the latest developments in
Denmark.

- Denmark covid stats: www.covid19genomics.dk/statistics
- Tools and resources mentioned: https://outbreak.info/
- https://virological.org/t/outbreak-info-sars-cov-2-mutation-situation-reports/629
- https://gitlab.com/johan.bernal.morales/sarscov2
- Info on masking SARSCOV2 sites: https://virological.org/t/issues-with-sars-cov-2-sequencing-data/473
- https://github.com/W-L/ProblematicSites_SARS-CoV2/blob/master/subset_vcf/problematic_sites_sarsCov2.mask.vcf

### Publications mentioned:

- A Comparison of Performance for Different SARS-Cov-2 Sequencing Protocols https://www.biorxiv.org/content/10.1101/2021.03.01.433428v1
- Before the Surge: Molecular Evidence of SARS-CoV-2 in New York City Prior to the First Report https://www.medrxiv.org/content/10.1101/2021.02.08.21251303v1
- SARS-CoV-2 within-host diversity and transmission https://science.sciencemag.org/content/early/2021/03/09/science.abg0821
