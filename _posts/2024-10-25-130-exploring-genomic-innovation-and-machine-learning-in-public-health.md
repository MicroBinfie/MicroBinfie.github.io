---
layout: page
title: 'Episode 130: Exploring Genomic Innovation and Machine Learning in Public Health'
date: '2024-10-25 00:00:00'
link: https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health
episode: '130'
soundcloud_track: '1933418207'
tags:
- microbinfie
- podcast
description: Tim Dallman discusses Shiga toxin-producing E. coli, pangenome-based machine learning and the metadata needed to predict disease risk.
excerpt: Tim Dallman discusses Shiga toxin-producing E. coli, pangenome-based machine learning and the metadata needed to predict disease risk.
headline: Tim Dallman on pangenomes and public health prediction
guests:
- Tim Dallman
topics:
- pathogen genomics
- genomic surveillance
- machine learning
- pangenome graphs
- clinical metadata
- shiga toxin-producing e. coli
- prophages
- disease risk prediction
- public health collaboration
faq:
- q: Why use pangenome graphs in machine-learning models?
  a: Tim wants model inputs to preserve relationships and functional connections within genomes rather than represent variation only as disconnected features. The challenges discussed include graph complexity, pruning and selecting graph properties that are useful for prediction.
- q: Why is clinical metadata difficult to use for genomic prediction?
  a: Tim says relevant clinical severity data exists for some pathogens, but researchers need the right partnerships to access and connect it. Navigating governance and involving data custodians in the research question are central parts of that work.
- q: Why study Shiga toxin-producing E. coli for disease-risk prediction?
  a: Its prophages make the pangenome difficult to analyse, but it also has clear virulence factors and known variation associated with clinical outcomes. Those relationships provide checks on what a model should find, while researchers investigate additional genomic features.
- q: What does IPSN do at the WHO Pandemic and Epidemic Intelligence Hub?
  a: Tim describes IPSN as a network hosted by the Berlin hub that connects organisations interested in pathogen genomics. It provides opportunities for public health, academic, private-sector and philanthropic participants to collaborate on innovation and sustainable capacity.
---

*Tim Dallman on pangenomes and public health prediction*

Andrew Page speaks with Tim Dallman at the 10th Bioinformatics Hackathon in Bethesda, Maryland, about his work at Utrecht University and the WHO Pandemic and Epidemic Intelligence Hub. They discuss how pangenome graphs, structured surveillance data and clinical metadata might support predictions of disease risk and severity. Shiga toxin-producing E. coli provides a challenging example, with complex prophage variation but also known virulence factors against which to check predictions.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 130: Exploring Genomic Innovation and Machine Learning in Public Health" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1933418207&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 130: Exploring Genomic Innovation and Machine Learning in Public Health on SoundCloud](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health)

## In this episode

### From genomic services to research at Utrecht

Tim Dallman describes splitting his work between Utrecht University in the Netherlands and the WHO Pandemic and Epidemic Intelligence Hub in Berlin. At Utrecht, he is based in the veterinary faculty, where he says he has been for three years. Asked how someone working on gastrointestinal infections ended up in a veterinary setting, Tim explains that foodborne disease research often sits in veterinary schools because of its connections to animals and veterinary food safety.

The university role gives him time to pursue questions he could not fully explore while running a genomic service at UKHSA: how to turn large genome collections with good metadata into actionable predictions of disease risk or severity.

### Connecting people through the WHO hub

Tim describes the Berlin hub as an extension of WHO's capabilities, with an emphasis on innovation and collaborative surveillance. Part of its purpose is to bring together people who do not commonly work together, using both physical and digital spaces.

IPSN is a network hosted by the hub. Tim says it brings together actors interested in pathogen genomics, including national public health organisations, academic centres, the private sector and philanthropic organisations. Its role is to provide forums and opportunities for the right people to talk, innovate and support sustainable capacity. Andrew compares this with finding expertise through Twitter and Slack during a pandemic; Tim sees value in formalising those connections.

### Clinical metadata is a partnership problem

Andrew asks whether metadata quality is the main obstacle to predicting clinical outcomes from genomes. Tim emphasises getting the right metadata and establishing the partnerships needed to use it. Clinical severity information does exist somewhere for some pathogens, he says.

He describes much of the work as joining networks of people, navigating governance and involving data custodians in solving the research question. Andrew jokes about wrestling data from custodians and offering them middle authorship on a paper, and the exchange ends in a joke about being diplomatic. The discussion makes clear that usable genome collections depend on relationships and access arrangements as well as the genomic analysis itself.

### Putting pangenomes into machine learning

Andrew and Tim discuss their collaboration on Predict and Prevent. Tim has been exploring how genomic variation can enter machine-learning models without losing the genome's functional relationships. Rather than treating variation as disconnected features, the work aims to make pangenomes part of the model input.

Andrew points out that graphs can become extremely complex even for relatively small genome collections. Tim identifies graph sub-selection, pruning and feature selection as important challenges: which parts of the graph are informative, and which graph properties help prediction?

They also discuss the uncertainty introduced when one machine-learning method predicts gene function and another uses those predictions. Tim says they are trying to use as much real data from structured surveillance as possible. Andrew contrasts this with using miscellaneous data found in RefSeq. Tim is interested in the prevalence of variation as a feature, alongside variation that may be selected for in different phenotypes.

### Shiga toxin-producing E. coli as a test case

The project focuses on Shiga toxin-producing E. coli. Tim describes its pangenome as particularly difficult because of prophage complexity. The team has undertaken substantial long-read sequencing to help resolve paralogous regions and improve the genomic representation used for the work.

Despite that complexity, the organism offers useful reference points. Shiga toxin is a clear virulence factor, and some genomic variation is already associated with clinical outcomes. These known relationships give the researchers things their models should recover. Tim presents an association between Shiga toxin and poor clinical outcomes as an expected finding, rather than a new discovery from the project.

He is also interested in other prophages that work in partnership across the E. coli genome and may help explain the phenotypes under study. The longer-term aim is to use genomic predictions to assess risk and prioritise resources in public health or food safety. The discussion presents this as ongoing research, not an established prediction service.

## Highlights

- [00:00:48](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=0:48) — Andrew introduces Tim Dallman at the hackathon in Bethesda.
- [00:01:12](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=1:12) — Tim describes his move to Utrecht University in the Netherlands.
- [00:01:53](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=1:53) — The WHO hub's emphasis on innovation and collaborative surveillance.
- [00:02:30](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=2:30) — IPSN brings public health, academic, private-sector and philanthropic organisations together.
- [00:03:39](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=3:39) — Why foodborne disease research fits within Utrecht's veterinary faculty.
- [00:04:53](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=4:53) — Obtaining clinical metadata through partnerships, governance and collaboration with data custodians.
- [00:06:49](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=6:49) — Preserving genomic relationships when building machine-learning inputs.
- [00:07:42](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=7:42) — Pruning pangenome graphs and selecting informative graph features.
- [00:08:39](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=8:39) — Using the prevalence of genomic variation as a predictive feature.
- [00:10:19](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=10:19) — Shiga toxin and clinical outcome as an expected association for the models to recover.

## In their own words

> Because obviously, evolution works on function, not on random variation in the genome.
>
> — Tim Dallman, [00:06:49](https://soundcloud.com/microbinfie/130-exploring-genomic-innovation-and-machine-learning-in-public-health#t=6:49)

## Who is talking

- **Andrew Page** (host)
- **Tim Dallman** (guest, Utrecht University; WHO Pandemic and Epidemic Intelligence Hub)
- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

RefSeq.

## Questions this episode answers

### Why use pangenome graphs in machine-learning models?

Tim wants model inputs to preserve relationships and functional connections within genomes rather than represent variation only as disconnected features. The challenges discussed include graph complexity, pruning and selecting graph properties that are useful for prediction.

### Why is clinical metadata difficult to use for genomic prediction?

Tim says relevant clinical severity data exists for some pathogens, but researchers need the right partnerships to access and connect it. Navigating governance and involving data custodians in the research question are central parts of that work.

### Why study Shiga toxin-producing E. coli for disease-risk prediction?

Its prophages make the pangenome difficult to analyse, but it also has clear virulence factors and known variation associated with clinical outcomes. Those relationships provide checks on what a model should find, while researchers investigate additional genomic features.

### What does IPSN do at the WHO Pandemic and Epidemic Intelligence Hub?

Tim describes IPSN as a network hosted by the Berlin hub that connects organisations interested in pathogen genomics. It provides opportunities for public health, academic, private-sector and philanthropic participants to collaborate on innovation and sustainable capacity.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro binfie Podcast, host Andrew Page sits down with Tim Dallman at the
10th Bioinformatics Hackathon in Bethesda, Maryland. Tim shares insights from his work at
Utrecht University in the Netherlands, where he focuses on genomic surveillance and machine
learning models to predict disease risk and severity. They discuss the challenges of
integrating genomic variation into predictive models, the importance of high-quality metadata,
and the complexities of working with pathogens like Shiga toxin-producing E. coli. Tim also
talks about his role at the WHO Pandemic and Epidemic Intelligence Hub and how global
collaboration can drive innovation in public health genomics. Tune in to hear about cutting-
edge research, the importance of interdisciplinary teamwork, and how genomic data can be
harnessed for future pandemic preparedness.
