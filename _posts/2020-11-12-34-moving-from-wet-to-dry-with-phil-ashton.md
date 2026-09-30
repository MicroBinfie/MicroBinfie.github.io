---
layout: page
title: 'Episode 34: Moving from wet to dry with Phil Ashton'
date: '2020-11-12 00:00:00'
link: https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton
episode: '34'
soundcloud_track: '907334761'
tags:
- microbinfie
- podcast
description: Phil Ashton on moving from wet-lab biology to bioinformatics, Salmonella surveillance, workflow tools and working in Vietnam and Malawi.
excerpt: Phil Ashton on moving from wet-lab biology to bioinformatics, Salmonella surveillance, workflow tools and working in Vietnam and Malawi.
headline: 'Phil Ashton: from wet-lab biology to public health bioinformatics'
guests:
- Phil Ashton
topics:
- bioinformatics careers
- wet-lab to dry-lab transition
- salmonella surveillance
- public health genomics
- workflow management
- clinical trial metadata
- low- and middle-income countries
- peer support
faq:
- q: How did Phil Ashton move from wet-lab research into bioinformatics?
  a: His PhD was mostly wet-lab work, with an RNA-sequencing chapter analysed using CLC bio. His first postdoc was entirely bioinformatics, so he learnt command-line work and Python on the job.
- q: Why keep sequencing Salmonella when so many genomes already exist?
  a: Phil distinguishes research datasets from prospective surveillance. Even if existing sequences can support research, sequencing must continue when it is being used to guide public health action.
- q: What would Phil learn earlier if starting bioinformatics again?
  a: He would engage with a workflow language, particularly Snakemake, rather than assemble scientific workflows himself in Python. He also names Nextflow when discussing potential productivity gains.
- q: Why sequence pathogen samples from clinical trials?
  a: Phil found exceptionally rich metadata in his fungal clinical-trial work, including illness severity and treatment response. He argues that adding sequencing can build on the substantial investment already made in collecting and characterising those samples.
---

*Phil Ashton: from wet-lab biology to public health bioinformatics*

Phil Ashton joins Lee Katz, Andrew Page and Nabil-Fareed Alikhan to discuss moving from bench microbiology into bioinformatics after his PhD. He traces work at Public Health England, in Vietnam and in Malawi, covering Salmonella surveillance, learning to code and finding support outside a large bioinformatics group. The discussion explains why technical skills need to be combined with microbiological and epidemiological understanding.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 34: Moving from wet to dry with Phil Ashton" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/907334761&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 34: Moving from wet to dry with Phil Ashton on SoundCloud](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton)

## In this episode

### From applied biology to bioinformatics

Phil's undergraduate degree was in applied biology. He pushed to take a genomics, proteomics and bioinformatics module, where he learnt about BLAST. Although genomics appeared in his PhD title, much of the work used AFLP in the wet lab. An RNA-sequencing chapter brought him to the bioinformatics group at Public Health England (PHE), where he used CLC bio.

He describes arriving with almost no command-line or scripting experience, apart from a little R and unsuccessful attempts to learn Perl from a book. His first postdoc, analysing E. coli O157, was entirely bioinformatics. By this conversation, he said he had not touched a pipette for eight years.

### What Salmonella surveillance can reveal

At PHE, Phil moved into a permanent role supporting Salmonella whole-genome sequencing as it replaced a mixture of microbiological methods. He valued the freedom to shape a new service relatively early in his career.

He describes a two-week to one-month delay between obtaining an isolate and generating a sequencing result, limiting its immediate usefulness for a restaurant outbreak. But sequencing could expose outbreaks hidden in the background: one published example involved contaminated feeder mice for reptiles and an outbreak continuing for at least three or four years. Around 200,000 Salmonella sequences are mentioned, prompting the question of whether that is enough. Phil distinguishes research from prospective surveillance: sequencing needs to continue when it informs public health action.

### Learning command lines and workflows

On his first day, Phil did not know what being asked to SSH into a server meant. He recalls the satisfaction of logging in the next morning to find that a Python pipeline, built from shell commands through os.system calls, had analysed the E. coli genomes.

Supportive colleagues and Friday coffee discussions helped him learn terminology as well as coding. The PHE bioinformatics group grew from six or seven to ten or twelve during his time there. He suggests that recent learners may be especially good at teaching beginners because they still remember the difficulties.

His retrospective advice is to learn a workflow language early. He names Snakemake and Nextflow as alternatives to assembling workflows himself in Python. A host also discusses Galaxy and the BioBlend API for working at scale.

### Staying close to laboratory and public health users

Phil favours a hub-and-spoke model over keeping every bioinformatician in a central group. Working alongside microbiologists and epidemiologists kept him close to the people using the assays and their outputs.

The trade-off was coordination. He spent at least a month writing Python software to generate XML for uploading 10,000 genomes a year to the NCBI Pathogens Portal, only to discover three months later that a colleague had independently written the same thing.

A host with a computer science background stresses learning organism-specific biology from experts. Lee adds that public health bioinformaticians also need to talk to epidemiologists and other colleagues. Phil sees his ability to understand laboratory work as an important advantage.

### Clinical trials, Vietnam and Malawi

Between PHE and Malawi, Phil spent three and a half years in Vietnam, working mainly on fungal pathogens and tuberculosis, including two years supporting bioinformatics across his unit. In Malawi, his focus returned to Salmonella Typhi and invasive non-typhoidal Salmonella.

His fungal work drew on clinical-trial samples with detailed information for around 700 people. He describes much richer metadata than he had encountered at PHE, including blood pressure, illness severity and treatment response. He recommends approaching clinical researchers about sequencing well-characterised trial samples. His illustrative funding argument pairs a £2 million clinical trial with £100,000 for sequencing.

Working away from a large bioinformatics group has meant finding technical peers through Twitter and Slack. He values local clinical and epidemiological contact, while missing the informal learning that comes from a larger group of bioinformaticians.

### Writing practice and career preferences

Phil started blogging to practise writing without the demands of a full paper. Making work public encouraged him to double-check analyses and bring projects to a clear conclusion; later posts included how-to material.

He sees himself more on the academic side than in general support services. He would consider returning to PHE or working at a microbe-focused institute such as Quadram, but is less keen on a general university bioinformatics core role. Even a few weeks each year in an active bioinformatics group would, he feels, be valuable.

## Highlights

- [00:01:33](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=1:33) — Phil introduces his work and his route through PHE, Vietnam and Malawi.
- [00:03:24](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=3:24) — Applied biology, a mostly wet-lab PhD and early experience with CLC bio.
- [00:06:07](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=6:07) — Moving from an E. coli postdoc into routine Salmonella sequencing at PHE.
- [00:07:26](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=7:26) — Sequencing delays and detecting long-running outbreaks linked to feeder mice.
- [00:09:29](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=9:29) — Why prospective public health surveillance needs continuing sequencing.
- [00:11:16](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=11:16) — Hub-and-spoke bioinformatics, user contact and duplicated software development.
- [00:13:18](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=13:18) — Learning SSH and building a first Python analysis pipeline.
- [00:15:50](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=15:50) — Learning from colleagues, group discussions and online communities.
- [00:18:55](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=18:55) — Rich clinical-trial metadata and the case for sequencing trial samples.
- [00:20:47](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=20:47) — Blogging as writing practice and an incentive to check analyses.
- [00:22:38](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=22:38) — Career preferences and the value of time in an active bioinformatics group.
- [00:24:20](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=24:20) — Learning Snakemake or Nextflow instead of building workflows from scratch.

## In their own words

> I think being able to speak lab has definitely been very helpful in multiple parts of my career.
>
> — Phil Ashton, [00:26:21](https://soundcloud.com/microbinfie/34-moving-from-wet-to-dry-with-phil-ashton#t=26:21)

## Who is talking

- **Phil Ashton** (guest, MLW, Blantyre, Malawi)
- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

BLAST, AFLP, CLC bio, R, Perl, Python, SSH, NCBI Pathogens Portal, Snakemake, Nextflow, Galaxy, BioBlend API.

## Questions this episode answers

### How did Phil Ashton move from wet-lab research into bioinformatics?

His PhD was mostly wet-lab work, with an RNA-sequencing chapter analysed using CLC bio. His first postdoc was entirely bioinformatics, so he learnt command-line work and Python on the job.

### Why keep sequencing Salmonella when so many genomes already exist?

Phil distinguishes research datasets from prospective surveillance. Even if existing sequences can support research, sequencing must continue when it is being used to guide public health action.

### What would Phil learn earlier if starting bioinformatics again?

He would engage with a workflow language, particularly Snakemake, rather than assemble scientific workflows himself in Python. He also names Nextflow when discussing potential productivity gains.

### Why sequence pathogen samples from clinical trials?

Phil found exceptionally rich metadata in his fungal clinical-trial work, including illness severity and treatment response. He argues that adding sequencing can build on the substantial investment already made in collecting and characterising those samples.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We chat with Phil Ashton about his move from the wet lab into the dry
lab to become a bioinformatician, and his experiences with working in
public health and in low and middle income countries.
