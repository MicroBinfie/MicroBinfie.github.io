---
layout: page
title: 'Episode 127: Minimum spanning trees'
date: '2024-09-05 00:00:00'
link: https://soundcloud.com/microbinfie/127-minimum-spanning-trees
episode: '127'
soundcloud_track: '1897691619'
tags:
- microbinfie
- podcast
description: Lee Katz and Nabil-Fareed Alikhan discuss minimum spanning trees, GrapeTree, outbreak profiles and the limits of reading minimum spanning trees as…
excerpt: Lee Katz and Nabil-Fareed Alikhan discuss minimum spanning trees, GrapeTree, outbreak profiles and the limits of reading minimum spanning trees as…
headline: Minimum spanning trees for outbreaks and transmission networks
guests: []
topics:
- minimum spanning trees
- graph theory
- outbreak analysis
- genetic distances
- phylogenetics
- allele profiles
- transmission networks
faq:
- q: How does a minimum spanning tree differ from a phylogenetic tree?
  a: The hosts describe an MST as connecting observed nodes with the lowest total edge weight and no loops. Unlike the phylogenetic trees they discuss, it does not introduce hypothetical ancestral nodes, and one observed profile can connect directly to several others.
- q: Why use minimum spanning trees for outbreak analysis?
  a: Lee finds them useful when many samples share a dominant profile and a minority differ by only a few SNPs or alleles. Circle sizes can show profile frequencies, while connections display the genetic differences between profiles.
- q: Why can the same distance data produce more than one minimum spanning tree?
  a: Several different trees can share the same minimum total edge weight. Nabil explains that software therefore needs tie-breaking rules, and some tools make additional adjustments, such as those he discusses for missing allele data in GrapeTree.
- q: Can an MST resemble a person-to-person transmission network?
  a: The hosts discuss this possibility using tuberculosis and Shigella. They frame it around comprehensive sampling in a closed setting, where transmission can be followed and an unobserved third party is not infecting both people.
---

*Minimum spanning trees for outbreaks and transmission networks*

Lee Katz and Nabil-Fareed Alikhan explain minimum spanning trees and why they are useful in microbial bioinformatics. They discuss genetic distances, software tie-breaking rules and the appeal of showing outbreak profiles as connected blobs. They also examine the limitations of treating these connections as evolutionary history or transmission links, particularly when ancestral strains have not been sampled.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 127: Minimum spanning trees" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1897691619&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 127: Minimum spanning trees on SoundCloud](https://soundcloud.com/microbinfie/127-minimum-spanning-trees)

## In this episode

### Connecting every node with minimum total distance

A minimum spanning tree, or MST, connects every node in a connected, undirected, weighted graph without creating loops, while minimising the total edge weight. Nabil explains this as points on a page with known distances between them: the task is to connect all the points with only one path between any pair.

For microbial data, those points can represent strains or genetic profiles, and the distances can measure genetic differences. The hosts contrast this arrangement with the commonly bifurcating phylogenetic trees they use: an MST can connect one observed profile directly to several others.

### Tied solutions and software choices

Minimising total distance does not always produce a unique answer. Nabil explains that several trees can have the same minimum total edge weight, leaving software to choose between tied solutions. He points to the goeBURST paper discussed in the episode for this problem.

The conversation names eBURST, BioNumerics, PHYLOViZ and GrapeTree. Lee asks whether their choices optimise the tree in an evolutionary context. Nabil distinguishes tie-breaking from further adjustments intended to make the output more realistic, particularly GrapeTree’s handling of missing allele data. He argues that these modifications mean its output departs from a strict mathematical MST.

### Outbreak profiles as connected blobs

Lee describes using MSTs for outbreaks that appear to involve a founder followed by a bottleneck expansion. In that setting, many pathogens may share one genetic profile, with a minority differing by only a couple of SNPs or alleles. A central profile with nearby variants radiating outwards can be a useful way to display that pattern.

The visualisation can also show how common each profile is: a larger circle represents the majority profile, while smaller circles represent less common profiles. Lee values displaying these small, direct differences rather than correcting them through evolutionary assumptions.

### Missing ancestors and understandable distances

Nabil identifies the absence of hypothetical ancestral nodes as an important limitation. An MST connects the observed nodes; interpreting one of them as the founder may be misleading if the actual founder was not sampled. He contrasts this with the internal splits shown in phylogenetic trees, especially when considering longer evolutionary timescales.

The hosts also value the flexibility of distance measures. They discuss allele distances in MLST, SNP counts and repeat counts, and suggest that even plasmid insertions or structural variation could define distances. Nabil notes that counts familiar to users can be easier to interpret than substitutions per site.

### Comparing MSTs with transmission networks

Lee contrasts foodborne outbreaks, where a shared food vehicle may contain a common ancestor, with person-to-person transmission. He uses tuberculosis and Shigella as examples where an MST might resemble a transmission network if the relevant infections have all been sampled.

Nabil adds that transmission networks may already be familiar to people who do not routinely read phylogenetic trees. Their comparison is conditional: they describe a closed setting where transmission can be followed and there is no unobserved third party infecting both people. Under those circumstances, the transmission network and MST may look similar.

## Highlights

- [00:00:00](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=0:00) — Lee introduces minimum spanning trees and their use in microbial bioinformatics.
- [00:01:35](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=1:35) — Nabil explains nodes, edges and connecting points without loops.
- [00:03:19](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=3:19) — How MST connections differ from commonly bifurcating phylogenetic trees.
- [00:03:57](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=3:57) — Spanning every node while minimising total edge weight.
- [00:07:26](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=7:26) — Tie-breaking rules and GrapeTree’s adjustments for missing allele data.
- [00:08:31](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=8:31) — Lee describes founder expansion and profile-sized blobs in outbreak analysis.
- [00:09:56](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=9:56) — Why the absence of hypothetical ancestral nodes can be problematic.
- [00:12:22](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=12:22) — Using distances beyond conventional measures of evolutionary change.
- [00:13:05](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=13:05) — Tuberculosis and Shigella as examples for comparing MSTs with transmission networks.
- [00:14:02](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=14:02) — Why transmission-network interpretations depend on a closed, traceable setting.

## In their own words

> Something like substitutions per site is something a little less intuitive.
>
> — Nabil-Fareed Alikhan, [00:09:56](https://soundcloud.com/microbinfie/127-minimum-spanning-trees#t=9:56)

## Who is talking

- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Minimum spanning trees (MSTs), MLST, eBURST, goeBURST, BioNumerics, PHYLOViZ, GrapeTree.

## Questions this episode answers

### How does a minimum spanning tree differ from a phylogenetic tree?

The hosts describe an MST as connecting observed nodes with the lowest total edge weight and no loops. Unlike the phylogenetic trees they discuss, it does not introduce hypothetical ancestral nodes, and one observed profile can connect directly to several others.

### Why use minimum spanning trees for outbreak analysis?

Lee finds them useful when many samples share a dominant profile and a minority differ by only a few SNPs or alleles. Circle sizes can show profile frequencies, while connections display the genetic differences between profiles.

### Why can the same distance data produce more than one minimum spanning tree?

Several different trees can share the same minimum total edge weight. Nabil explains that software therefore needs tie-breaking rules, and some tools make additional adjustments, such as those he discusses for missing allele data in GrapeTree.

### Can an MST resemble a person-to-person transmission network?

The hosts discuss this possibility using tuberculosis and Shigella. They frame it around comprehensive sampling in a closed setting, where transmission can be followed and an unobserved third party is not infecting both people.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Nabil and Lee have a quick chat about minimum spanning trees (MST).

Eburst paper: <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-10-152>
