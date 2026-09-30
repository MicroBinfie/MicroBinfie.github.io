---
layout: page
title: 'Episode 18: Panel - Has Nanopore rendered onsite Illumina obsolete?'
date: '2020-05-14 00:00:00'
link: https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete
episode: '18'
soundcloud_track: '746428444'
tags:
- microbinfie
- podcast
description: A January 2020 panel in The Gambia weighs Nanopore against Illumina for outbreaks, metagenomics, sequencing access and data ownership.
excerpt: A January 2020 panel in The Gambia weighs Nanopore against Illumina for outbreaks, metagenomics, sequencing access and data ownership.
headline: Has Nanopore made on-site Illumina sequencing obsolete?
guests:
- David Baker
- Ozan Gundogdu
- Abdul Sesay
- Nick Loman
- Suzie Hingley-Wilson
- Mark Pallen
- Muna Anjum
- Arnoud van Vliet
- Martin Antonio
- Archie Worwui
topics:
- nanopore sequencing
- illumina sequencing
- long-read sequencing
- metagenomics
- outbreak investigation
- antimicrobial resistance
- sequencing access
- basecalling
- sample ownership
faq:
- q: Did the panel conclude that Nanopore had made Illumina obsolete?
  a: No single conclusion emerged. In this January 2020 discussion, participants favoured Nanopore for accessibility and long-read applications but retained a role for Illumina where single-base accuracy and detailed outbreak attribution mattered.
- q: Why might Nanopore be more attractive for laboratories in The Gambia?
  a: Abdul Sesay emphasises difficult access to external sequencing providers and the value of affordable in-house sequencing. He argues that a platform covering most local needs could displace Illumina sooner there than in better-resourced settings.
- q: Can Illumina analysis pipelines be used unchanged for Nanopore data?
  a: The panel says different pipelines are needed to account for the errors in long-read data. FASTQ or FASTA can be used for hybrid assembly, but sharing a file format does not make the analysis interchangeable.
- q: Why did the panel recommend retaining Nanopore raw signal?
  a: Participants describe rapid changes in Guppy and other basecalling software. Retaining the squiggles allows the same experiment to be re-basecalled later to obtain improved reads.
---

*Has Nanopore made on-site Illumina sequencing obsolete?*

Recorded live at MRC Gambia at the London School of Hygiene and Tropical Medicine in January 2020, this panel asks whether Nanopore has made on-site Illumina sequencing obsolete. Chaired by Suzie Hingley-Wilson, it brings together Andrew Page, David Baker, Ozan Gundogdu, Abdul Sesay and Nick Loman to compare accuracy, access, costs and public-health needs. Nick Loman joined by Skype, but his audio could not be included in the recording.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 18: Panel - Has Nanopore rendered onsite Illumina obsolete?" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/746428444&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 18: Panel - Has Nanopore rendered onsite Illumina obsolete? on SoundCloud](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete)

## In this episode

### Long reads versus single-base accuracy

The opening argument favours long reads for biological interpretation. A panellist contrasts short-read shotgun metagenomic bins containing 10,000–20,000 contigs with a PromethION gut metagenomic assembly yielding bins of 10–20 much larger contigs. The criticism is that fragmented assemblies depend heavily on algorithms to group sequences, sometimes producing questionable metagenome-assembled genomes.

The response separates usefulness from complete replacement. One panellist suggests Nanopore might cover 80–90% of applications, while questioning whether its accuracy will become sufficient for single-nucleotide polymorphism (SNP) resolution. Illumina, or PacBio where accessible, could still serve work requiring higher accuracy. These are positions expressed in January 2020, rather than a settled verdict on the technologies.

### Outbreak detection is not the same as attribution

A question asks whether Nanopore has been tested against Illumina for bacterial outbreak analysis, including Acinetobacter. Muna Anjum explains why accuracy matters for antimicrobial resistance: a SNP difference can distinguish resistant from sensitive isolates. Her group uses MinION and Illumina together. She describes an Oxford comparison in which PacBio and MinION both worked well, but PacBio was more accurate; cost remained a barrier for surveillance involving hundreds of isolates.

A hypothetical Salmonella outbreak illustrates the distinction between detecting related cases and tracing infection to a particular kebab shop or farm. One proposed workflow screens 1,000 isolates with Nanopore, then uses Illumina on 50 similar isolates for finer resolution. Muna says their current approach is essentially the reverse.

Another contributor prioritises rapid pathogen and serotype or genotype identification to guide vaccine responses. Direct sequencing might avoid a day or two of culture, but participants caution that low bacterial biomass in a nasopharyngeal swab could still require culture. PCR amplification for viruses is also mentioned.

### Access may drive replacement sooner in Africa

Abdul Sesay argues that Illumina could become obsolete sooner in his African setting than in better-resourced settings. Access to external sequencing providers is harder, so an affordable local technology covering most needs may matter more than achieving the lowest error rate. He describes a Gates Foundation grant initially tied to 20 small Illumina instruments for sepsis metagenomics, with the work subsequently extended to allow Nanopore.

The discussion puts Nanopore's entry cost at $1,000 and contrasts that with larger instruments and their supporting infrastructure. Existing investment can nevertheless slow change: a panellist compares this with the persistence of microarrays. Ozan Gundogdu describes a similar institutional tension at LSHTM, where an Illumina core facility coexists with individual groups acquiring Nanopore equipment for work abroad. Sustainability, warranties and responsibility for ongoing costs remain unresolved.

### FASTQ files do not make the pipelines interchangeable

An end-user question asks whether moving from Illumina to Nanopore means changing analysis pipelines or merely converting files. The response is that Nanopore and PacBio require different pipelines to account for their errors, although hybrid assembly can combine long and short reads supplied as FASTQ or FASTA files.

The panel distinguishes native instrument output from routine analysis input: Illumina produces BCL files, but users generally analyse FASTQ. For Nanopore, rapidly changing basecalling software such as Guppy provides a reason to retain the raw signal, or squiggles. Re-basecalling the same data can improve the resulting reads; keeping only FASTQ is presented as a possibility once basecalling becomes sufficiently stable.

### In-country sequencing and control of samples

Abdul describes a two-year planning horizon for future equipment, leaving time to reassess technology before committing funds. Human genetics raises throughput and cost questions, while Plasmodium and Anopheles are suggested as possible uses for PromethION. Participants also discuss bringing work previously done through the Sanger into their own facilities.

A question about donors' data rights prompts a distinction between consent for a test and the machine used to perform it. One response argues that protecting the resulting data is the central issue; participants say human sequences from non-human projects should not be released.

Local sequencing could reduce the need to export infectious samples. The discussion also covers government ownership of specimens and requirements to retain aliquots locally, including the practical burden of keeping material without linked metadata.

### Could PacBio offer another route?

David Baker closes by arguing that PacBio may be missing an opportunity. He proposes a more affordable instrument combining Illumina-like quality with Nanopore-like read length as a potential all-in-one option for a core sequencing facility, while acknowledging that it would not necessarily serve fieldwork.

The response from the Gambian setting is that both purchase cost and maintenance would remain obstacles, even if PacBio became cheaper. Smaller machines therefore retain their appeal. The discussion ends without a single replacement decision: the acceptable balance between accuracy, throughput, infrastructure and access depends on the research question and the setting.

## Highlights

- [00:01:00](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=1:00) — The panel's central question: has Nanopore made on-site Illumina obsolete?
- [00:01:07](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=1:07) — Panel introductions and the case for long-read metagenomic assemblies
- [00:02:48](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=2:48) — Whether Nanopore accuracy can support SNP-level resolution
- [00:04:06](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=4:06) — Abdul Sesay on sequencing access and why replacement could happen sooner in Africa
- [00:07:12](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=7:12) — Muna Anjum on resistance, hybrid sequencing and the need for accuracy
- [00:09:16](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=9:16) — Rapid pathogen and serotype identification for public-health responses
- [00:10:22](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=10:22) — Biomass limits on direct sequencing, followed by an end-user pipeline question
- [00:11:45](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=11:45) — BCL versus FASTQ, Guppy updates and retaining Nanopore raw signal
- [00:12:45](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=12:45) — A two-year equipment-planning horizon and future human genetics work
- [00:14:19](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=14:19) — Consent for testing, instrument choice and protection of sequence data
- [00:16:40](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=16:40) — Ozan Gundogdu on core facilities, portable equipment and warranty costs
- [00:17:29](https://soundcloud.com/microbinfie/18-has-nanopore-rendered-onsite-illumina-obsolete#t=17:29) — David Baker's proposal for a more accessible PacBio core-facility instrument

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **David Baker** (panellist, Quadram Institute)
- **Ozan Gundogdu** (panellist, LSHTM (UK))
- **Abdul Sesay** (panellist, LSHTM (Gambia))
- **Nick Loman** (panellist, University of Birmingham)
- **Suzie Hingley-Wilson** (guest, University of Surrey)
- **Mark Pallen** (guest, Quadram Institute)
- **Muna Anjum** (guest, APHA)
- **Arnoud van Vliet** (guest, University of Surrey)
- **Martin Antonio** (guest, LSHTM)
- **Archie Worwui** (guest, LSHTM)

## Tools and resources mentioned

Illumina, Illumina MiSeq, Illumina GA2, Oxford Nanopore, MinION, GridION, PromethION, PacBio, Guppy, PCR.

## Questions this episode answers

### Did the panel conclude that Nanopore had made Illumina obsolete?

No single conclusion emerged. In this January 2020 discussion, participants favoured Nanopore for accessibility and long-read applications but retained a role for Illumina where single-base accuracy and detailed outbreak attribution mattered.

### Why might Nanopore be more attractive for laboratories in The Gambia?

Abdul Sesay emphasises difficult access to external sequencing providers and the value of affordable in-house sequencing. He argues that a platform covering most local needs could displace Illumina sooner there than in better-resourced settings.

### Can Illumina analysis pipelines be used unchanged for Nanopore data?

The panel says different pipelines are needed to account for the errors in long-read data. FASTQ or FASTA can be used for hybrid assembly, but sharing a file format does not make the analysis interchangeable.

### Why did the panel recommend retaining Nanopore raw signal?

Participants describe rapid changes in Guppy and other basecalling software. Retaining the squiggles allows the same experiment to be re-basecalled later to obtain improved reads.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

A panel discussion held in MRC Gambia at The London School of Hygiene
and Tropical Medicine, recorded in front of a live audience of
scientists in January 2020, when SARS-CoV-2 was just beginning to be
reported as an emerging infectious disease.  The panel consisted of
Andrew Page and David Baker from the Quadram Institute, Ozan Gundogdu
from LSHTM (UK), Abdul Sesay from LSHTM (Gambia) and Nick Loman from
the University of Birmingham and chaired by Suzie Hingley-Wilson from
the University of Surrey.  Questions, discussion and comments from:
Mark Pallen - Quadram Institute Muna Anjum - APHA Arnoud van Vliet -
University of Surrey Martin Antonio - LSHTM Archie Worwui - LSHTM
Unfortunately we weren't able to capture the audio from Nick Loman who
joined via Skype, but he did make really great contributions.
