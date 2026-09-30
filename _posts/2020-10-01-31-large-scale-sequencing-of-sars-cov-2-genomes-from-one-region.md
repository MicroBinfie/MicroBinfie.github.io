---
layout: page
title: 'Episode 31: Large scale sequencing of SARS-CoV-2 genomes from one region'
date: '2020-10-01 00:00:00'
link: https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region
episode: '31'
soundcloud_track: '901142494'
tags:
- microbinfie
- podcast
description: How Norfolk sequenced SARS-CoV-2 during the first wave, using ARTIC, lineage analysis and clinical data to investigate local outbreaks.
excerpt: How Norfolk sequenced SARS-CoV-2 during the first wave, using ARTIC, lineage analysis and clinical data to investigate local outbreaks.
headline: SARS-CoV-2 sequencing and outbreak tracking in Norfolk
guests:
- Alison Mather
- Justin O'Grady
topics:
- sars-cov-2
- genomic epidemiology
- norfolk
- cog-uk
- amplicon sequencing
- lineage assignment
- contamination control
- care home outbreaks
- hospital transmission
- reinfection
faq:
- q: How many SARS-CoV-2 genomes did the Norfolk study sequence?
  a: The study sequenced around 1,500 genomes and obtained high-quality genomes from 1,035 cases. It covered March–August 2020, with sequencing representing 42.6% of identified positive cases in the region.
- q: How quickly could the team sequence SARS-CoV-2 samples?
  a: Justin describes an ARTIC workflow capable of producing results in under 24 hours. The team demonstrated rapid turnaround by sequencing 35 positive samples from a food processing facility in less than 24 hours.
- q: Can SARS-CoV-2 genome sequencing prove who infected whom?
  a: The panellists explain that similarity within a common circulating lineage can make transmission links difficult to establish. Distinctive sublineages are more informative, while substantial genomic differences can help rule out a proposed shared outbreak; clinical and epidemiological data remain important.
- q: Did the Norfolk study find evidence of SARS-CoV-2 reinfection?
  a: No evidence of reinfection was found in 42 cases with longitudinal samples, with sampling extending up to 71 days. Justin notes that many of these patients remained in hospital with the same illness episode, so this was not equivalent to testing clearly separated episodes of infection.
---

*SARS-CoV-2 sequencing and outbreak tracking in Norfolk*

Nabil-Fareed Alikhan talks with Andrew Page, Alison Mather and Justin O'Grady about sequencing around 1,500 SARS-CoV-2 genomes from Norfolk and surrounding areas during March–August 2020. They explain the laboratory workflow, bioinformatics and collaboration needed to turn sequences into useful public health information. Examples from care homes, hospitals and a food processing facility show how genomic data can investigate suspected outbreaks—and why epidemiological context remains essential.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 31: Large scale sequencing of SARS-CoV-2 genomes from one region" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/901142494&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 31: Large scale sequencing of SARS-CoV-2 genomes from one region on SoundCloud](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region)

## In this episode

### Regional surveillance through COG-UK

The Quadram Institute team describes its contribution to the COVID-19 Genomics UK Consortium, COG-UK: sequencing positive samples mainly from Norfolk and parts of Suffolk. Norfolk and Norwich University Hospital supplied samples tested through its regional laboratory. Most were diagnostic samples from hospitals, with smaller numbers from key workers and their families. Much community testing went through the separate Lighthouse laboratories and was not represented in this dataset.

The study covered March–August 2020, spanning the first wave. Around 1,500 genomes were sequenced, with high-quality genomes obtained from 1,035 cases. Sequencing represented 42.6% of identified positive cases in the region. At the comparison reported in the study, only five countries had sequenced more SARS-CoV-2 genomes than Norfolk had for this work. The accompanying medRxiv manuscript is identified in the show notes as 10.1101/2020.09.28.20201475, version 1.

### From clinical samples to ARTIC libraries

Justin explains why sample handling is not uniform. Diagnostic platforms differ in sensitivity, extraction arrangements and readouts: some provide cycle-threshold values, others take-off values or relative fluorescence units. Receiving extracted RNA is easier for the sequencing team than receiving a primary sample requiring another extraction.

The workflow proceeds through RNA extraction where necessary, first-strand cDNA synthesis, ARTIC multiplex PCR and library preparation for Nanopore or Illumina sequencing. Justin describes two multiplex reactions containing 48 primer pairs each. The PCR takes about three and a half hours; even samples with cycle-threshold values above 35 can yield parts of the genome, although not necessarily complete genomes. The optimised low-cost protocol was described as costing roughly £10–£12 per genome, with sample-to-result turnaround possible in under 24 hours. Nanopore runs commonly used 48 samples per flow cell.

### Consensus genomes, controls and lineage reports

Andrew describes basecalling, strict demultiplexing and ARTIC processing pipelines, including iVar for Illumina data. Minimum coverage thresholds were approximately 10× for Illumina consensus calls and 20× for Nanopore, although actual coverage often exceeded 1,000×. Deep sequencing helped compensate for uneven coverage between amplicons.

Negative controls were essential. The team examined reads in blanks rather than accepting consensus output uncritically. Nabil distinguishes primer dimers and short incidental matches from clear reads mapping across the viral genome. Justin explains that post-PCR handling and the additional PCR in their Nextera-based Illumina workflow created contamination risks; clearly contaminated runs were repeated.

Sequences uploaded to COG-UK received global and finer-grained UK lineage assignments. Pangolin is named in this process. For rapid local investigations, CIVET produced reports showing related genomes and their variants in about an hour. Andrew then examined wider clusters to understand regional spread and distinguish new introductions from lineages already circulating.

### Diversity, evolution and longitudinal samples

The team identified 100 distinct UK lineages despite Norfolk's relatively stable, low-density population. Sixteen lineages found in key workers were not observed in patients or community-care samples. Alison interprets this as an encouraging finding for infection control, while emphasising the dense sampling and the combination of genomic, clinical and epidemiological data that made such comparisons possible.

Andrew reports an evolutionary rate of about two single-nucleotide polymorphisms, or SNPs, per month. The spike mutation D614G became dominant in their samples by about April and is discussed in relation to increased transmissibility.

No evidence of reinfection was found among 42 cases with longitudinal samples, including a sampling interval of up to 71 days. Justin notes that many samples came from patients still in hospital during the same illness episode. These observations describe the cohort available in 2020, rather than establishing that reinfection could not occur.

### Care homes and suspected hospital transmission

A query about one care facility led Andrew to investigate a distinctive sublineage: 14 of 15 samples belonged to it. Mapping related cases and examining ages and addresses revealed links involving six care homes. Some genomes were identical, while the surrounding community contained different lineages. The investigation suggested connections between care facilities that were not apparent from the initial query.

Justin stresses that this depended on the sublineage being distinguishable from widely circulating viruses. If an outbreak involved a common lineage such as UK5, genomic similarity alone would be much less informative about transmission.

At Ipswich Hospital, 18 high-quality genomes comprised six global lineages and eight UK lineages. That diversity argued against a single sustained hospital outbreak. Alison uses the example to explain why sequencing can be more decisive for ruling out a proposed outbreak than for proving transmission links.

### Rapid investigation of a food processing outbreak

In August 2020, the team sequenced 35 positive samples from workers at a food processing facility in less than 24 hours. The response involved the NHS microbiology laboratory, Norfolk County Council Test and Trace, Public Health England and Quadram. All genomes shared the same global and UK lineage, and Andrew describes two distinguishing SNPs that helped define the outbreak sublineage.

Subsequent sequencing detected that signature in hospital samples and elsewhere in Norfolk and further afield, indicating spread beyond the original facility. Knowing the sublineage allowed the team to follow its appearance over time.

The closing advice is practical: use established protocols and analysis tools, but build relationships with hospitals, public health teams, clinicians, data managers and epidemiologists. The panellists emphasise that rapid sequencing becomes useful through coordinated interpretation and feedback, supported by considerable staff and volunteer effort.

## Highlights

- [00:00:47](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=0:47) — Introducing the Norfolk sequencing project and the participants
- [00:08:30](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=8:30) — Why the team attempted sequencing even for low-viral-load samples
- [00:15:08](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=15:08) — The ARTIC laboratory workflow, costs and rapid turnaround
- [00:19:26](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=19:26) — Basecalling, strict demultiplexing and consensus genome coverage
- [00:21:29](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=21:29) — Inspecting negative controls and recognising contamination
- [00:24:20](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=24:20) — Global and UK lineages, Pangolin and rapid CIVET reports
- [00:28:02](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=28:02) — Norfolk's lineage diversity and findings in key workers
- [00:33:01](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=33:01) — An evolutionary rate of approximately two SNPs per month
- [00:34:00](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=34:00) — Longitudinal sampling and the search for reinfection
- [00:39:05](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=39:05) — Tracing a distinctive sublineage across six care homes
- [00:43:39](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=43:39) — Using lineage diversity to assess a suspected hospital outbreak
- [00:46:37](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=46:37) — Following the distinctive SNP signature of a food processing outbreak

## In their own words

> it's easier to rule things out than to rule things in
>
> — Alison Mather, [00:43:39](https://soundcloud.com/microbinfie/31-large-scale-sequencing-of-sars-cov-2-genomes-from-one-region#t=43:39)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)
- **Lee Katz** (host)
- **Alison Mather** (guest, Quadram Institute Bioscience)
- **Justin O'Grady** (guest, Quadram Institute Bioscience; University of East Anglia)

## Tools and resources mentioned

ARTIC protocol, ARTIC pipelines, RT-qPCR, Nanopore, Illumina, Nextera, iVar, Pangolin, CIVET.

## Questions this episode answers

### How many SARS-CoV-2 genomes did the Norfolk study sequence?

The study sequenced around 1,500 genomes and obtained high-quality genomes from 1,035 cases. It covered March–August 2020, with sequencing representing 42.6% of identified positive cases in the region.

### How quickly could the team sequence SARS-CoV-2 samples?

Justin describes an ARTIC workflow capable of producing results in under 24 hours. The team demonstrated rapid turnaround by sequencing 35 positive samples from a food processing facility in less than 24 hours.

### Can SARS-CoV-2 genome sequencing prove who infected whom?

The panellists explain that similarity within a common circulating lineage can make transmission links difficult to establish. Distinctive sublineages are more informative, while substantial genomic differences can help rule out a proposed shared outbreak; clinical and epidemiological data remain important.

### Did the Norfolk study find evidence of SARS-CoV-2 reinfection?

No evidence of reinfection was found in 42 cases with longitudinal samples, with sampling extending up to 71 days. Justin notes that many of these patients remained in hospital with the same illness episode, so this was not equivalent to testing clearly separated episodes of infection.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat to Justin O'Grady, Andrew Page and Alison Mather about how
they went about sequencing 1500 SARS-CoV-2 genomes from one small
region in the UK (Norfolk), and how they went about using the data for
genomic epidemiology to help get a detailed, near real-time view of
the pandemic as it unfolded.  Some of the key points are that in
Norfolk and surrounding regions:  100 distinct UK lineages were
identified. 16 UK lineages found in key workers were not observed in
patients or in community care.  172 genomes from SARS-CoV-2 positive
samples sequenced per 100,000 population representing 42.6% of all
positive cases. SARS-CoV-2 genomes from 1035 cases sequenced to a high
quality. Only 5 countries, out of 103, have sequenced more SARS-CoV-2
genomes than have been sequenced in Norfolk for this paper. Samples
covered the entire first wave, March to August 2020. Stable
evolutionary rate of 2 SNPs per month. D614G mutation is the dominant
genotype and associated with increased transmission. No evidence of
reinfection in 42 cases with longitudinal samples. WGS identified a
sublineage associated with care facilities. WGS ruled out nosocomial
outbreaks.  Rapid WGS confirmed the relatedness of cases from an
outbreak at a food processing facility.  The manuscript is available
from: https://www.medrxiv.org/content/10.1101/2020.09.28.20201475v1
