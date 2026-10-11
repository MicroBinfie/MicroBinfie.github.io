---
layout: page
title: 'Episode 11: Phylogenetics with the arborists part 1'
date: '2020-02-06 00:00:00'
link: https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1
episode: '11'
soundcloud_track: '719459716'
tags:
- microbinfie
- podcast
description: Conor Meehan and Leonardo de Oliveira Martins discuss phylogenetic methods, core-genome bias, alignment checks and misleading branch lengths.
excerpt: Conor Meehan and Leonardo de Oliveira Martins discuss phylogenetic methods, core-genome bias, alignment checks and misleading branch lengths.
headline: 'Phylogenetic trees: choosing methods and checking the data'
guests:
- Conor Meehan
- Leonardo de Oliveira Martins
topics:
- phylogenetics
- outbreak analysis
- maximum likelihood
- bayesian inference
- core genomes
- horizontal gene transfer
- alignment quality
- selection bias
- branch lengths
- mycobacteria
faq:
- q: Do I need a phylogenetic tree for a bacterial outbreak?
  a: The guests recommend starting with the question rather than assuming a tree is required. A SNP distance matrix and cut-offs may be enough to assess relatedness, while questions about transmission events or their timing may require more complex modelling.
- q: Is IQ-TREE or RAxML-NG better for bacterial phylogenetics?
  a: Conor and Leo regard both as robust, and their experiences with speed differ by dataset. They place more emphasis on selecting and checking the input data than on declaring one program universally better.
- q: Why can a concatenated core-genome alignment give a misleading tree?
  a: Core genes do not necessarily share a single history of vertical inheritance. Horizontal transfer and orthologous replacement can introduce conflicting signals, which Conor says can cause problems for maximum-likelihood analysis of a combined alignment.
- q: How can I check whether a phylogenetic alignment is reliable?
  a: Leo recommends inspecting gaps and checking sensitivity to sequence order or reversal. His head-and-tails example reverses the sequences, realigns them and reverses the result back to see whether the alignment changes.
- q: What branch-length problems should I check in a bacterial tree?
  a: The discussion flags identical lengths, unexpectedly long branches and zero or near-zero branches as reasons to investigate. For SNP-only data, Conor also recommends checking ascertainment-bias correction or the inclusion of constant sites, alongside the expected biological relationships.
---

*Phylogenetic trees: choosing methods and checking the data*

Nabil-Fareed Alikhan talks with Conor Meehan and Leonardo de Oliveira Martins about choosing phylogenetic methods for outbreaks, clonal complexes and broader bacterial comparisons. They weigh quick distance-based approaches against maximum likelihood and Bayesian inference, then examine how gene selection, horizontal transfer and alignment quality affect the result. Their central warning is that obtaining a tree is easy; establishing whether it answers the biological question takes considerably more work.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 11: Phylogenetics with the arborists part 1" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/719459716&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 11: Phylogenetics with the arborists part 1 on SoundCloud](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1)

## In this episode

### Start with the biological question

Conor Meehan describes a research path from HIV transmission trees through human microbiomes and lateral gene transfer to mycobacteria, including Mycobacterium tuberculosis and Mycobacterium ulcerans. Leonardo de Oliveira Martins combines phylogenetic analysis support with software development, particularly Bayesian models for recombination and species-tree inference.

Their first practical question is why a tree is needed at all. Conor often encounters researchers building one because they think a paper requires it. For an outbreak, a SNP distance matrix and cut-offs may answer a question about relatedness without a more elaborate reconstruction. The discussion refers to Simon Harris’s MRSA hospital-outbreak paper when distinguishing simple relatedness questions from analyses that need branch lengths, transmission timing or a more detailed evolutionary model.

### Where quick methods still help

Conor argues that faster computers and streamlined software have removed many reasons for choosing parsimony or distance-based methods over maximum likelihood or Bayesian inference. He recalls maximum-likelihood analyses of perhaps 20–30 taxa taking days around 10–15 years earlier. These more complex approaches can model multiple substitutions at the same alignment position.

Leo nevertheless sees continuing space for quick methods. Over a short outbreak timescale, with little opportunity for repeated substitutions, parsimony or distances may give an adequate answer. Nabil also uses a first-pass neighbour-joining tree to check that a dataset looks sensible before moving to a more robust analysis. The guests note that maximum-likelihood searches themselves can start from parsimony or distance trees. When the question becomes transmission rather than relatedness, they mention outbreaker and TransPhylo as Bayesian approaches that attempt to account for missed events.

### RAxML-NG, IQ-TREE and the input alignment

For comparisons across a clonal complex or within a species, Conor says much of his effort now goes into preparing the input rather than choosing the tree-building program. He favours RAxML-NG, while Leo generally uses IQ-TREE because he finds it quick and easy to use. Both regard the programs as robust choices rather than declaring an overall winner.

Their contrasting experiences show why performance depends on the dataset. Leo returned to IQ-TREE after a RAxML analysis took longer than expected. Conor describes a large, complex analysis for which IQ-TREE estimated roughly two months, whereas RAxML-NG was much faster. He also praises IQ-TREE’s model selection and bootstrap workflow. A core-genome alignment, potentially assembled using Roary, is a common input, but the guests stress that its contents deserve more attention than the software contest.

### Gene shopping, transfer and conflicting signals

Leo distinguishes purposeful gene selection from its potential biases. For divergence-time estimation, a researcher might seek constitutive, nearly neutral genes rather than genes under unusual selection. But choosing genes because they are easy to detect, widely available or present in single copy can favour one evolutionary signal while excluding others. He also questions whether clustering samples and removing very similar sequences could introduce bias.

Conor focuses on concatenating core genes into a superalignment. This can assume that the genes share a history of vertical inheritance, despite horizontal gene transfer. Through orthologous replacement, a bacterium can replace an existing gene with a copy from another bacterium; genes combined in one alignment may therefore support conflicting trees. Even 16S is not automatically straightforward: some bacteria have four or more copies that are not identical, and some have acquired copies horizontally. Deciding which sequences belong in the analysis requires attention to paralogy, orthology and conflicting histories.

### Test the alignment and challenge the tree

Leo warns that tree-building software can return a tree even from aligned random sequences with no common ancestry. His first response to an exciting phylogram would be to revisit the primary data and ask which models and algorithms were tried. He recommends checking gaps and alignment sensitivity, describing a head-and-tails test: reverse the sequences, realign them, then reverse the result back and compare it with the original alignment.

Conor suggests comparing trees from different data sources, such as 16S, multilocus sequence types and whole genomes. Agreement supports a strong shared signal; disagreement does not necessarily mean one tree is wrong. It may reflect different histories. The appropriate response depends on the original question and can require checking individual genes for recombination or lateral transfer.

### Support values and branch-length warning signs

The guests recommend examining bootstrap support or, for Bayesian analyses, the posterior distribution of trees. Conor says he is more inclined to trust a Bayesian result when its priors and models have been checked properly.

Biological expectations provide another sanity check. In tuberculosis analyses, Conor looks for the expected relationships among lineages and subspecies. He also checks whether a SNP-only analysis has used ascertainment-bias correction or included constant sites, because omitting these considerations can distort branch lengths. Nabil flags supposedly maximum-likelihood trees with identical branch lengths and taxa with inexplicably long branches. Leo pays particular attention to zero or near-zero lengths, including values around 10 to the minus 6. Such branches are not automatically wrong, but they are a reason to inspect the data again.

## Highlights

- [00:02:13](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=2:13) — Conor’s work on HIV, microbiomes, gene transfer and mycobacterial phylogenetics
- [00:04:04](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=4:04) — The shift from parsimony and distances towards maximum likelihood and Bayesian methods
- [00:05:25](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=5:25) — Leo’s case for retaining quick methods in outbreaks and clonal complexes
- [00:06:23](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=6:23) — Asking why a tree is needed before choosing an outbreak analysis
- [00:10:29](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=10:29) — Input-data preparation, core genomes and choosing between RAxML-NG and IQ-TREE
- [00:12:38](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=12:38) — Gene shopping and selection bias in genes and samples
- [00:14:25](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=14:25) — Core-genome concatenation, horizontal transfer and multiple 16S copies
- [00:16:44](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=16:44) — Why even random sequences can produce a phylogenetic tree
- [00:18:01](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=18:01) — Returning to primary data, comparing models and testing alignment sensitivity
- [00:19:15](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=19:15) — Alignment quality and comparing trees from different data sources
- [00:20:23](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=20:23) — Checking bootstrap support and Bayesian posterior distributions
- [00:21:38](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=21:38) — Expected biological relationships, SNP ascertainment bias and branch-length scales

## In their own words

> Understanding what data you should be putting in can be quite difficult.
>
> — Conor Meehan, [00:14:25](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=14:25)

> So first thing would be to check the alignment to see if there's a lot of gaps in those.
>
> — Leonardo de Oliveira Martins, [00:18:01](https://soundcloud.com/microbinfie/11-phylogenetics-with-the-arborists-part1#t=18:01)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Conor Meehan** (guest, University of Bradford)
- **Leonardo de Oliveira Martins** (guest, Quadram Institute Bioscience)
- **Lee Katz** (host)

Also mentioned: Andrew Page, Simon Harris.

## Tools and resources mentioned

RAxML, RAxML-NG, IQ-TREE, PhyML, Roary, outbreaker, TransPhylo, Maximum likelihood, Bayesian inference, Parsimony, Neighbour joining, Bootstrapping, Ascertainment-bias correction, Head-and-tails alignment test.

## Questions this episode answers

### Do I need a phylogenetic tree for a bacterial outbreak?

The guests recommend starting with the question rather than assuming a tree is required. A SNP distance matrix and cut-offs may be enough to assess relatedness, while questions about transmission events or their timing may require more complex modelling.

### Is IQ-TREE or RAxML-NG better for bacterial phylogenetics?

Conor and Leo regard both as robust, and their experiences with speed differ by dataset. They place more emphasis on selecting and checking the input data than on declaring one program universally better.

### Why can a concatenated core-genome alignment give a misleading tree?

Core genes do not necessarily share a single history of vertical inheritance. Horizontal transfer and orthologous replacement can introduce conflicting signals, which Conor says can cause problems for maximum-likelihood analysis of a combined alignment.

### How can I check whether a phylogenetic alignment is reliable?

Leo recommends inspecting gaps and checking sensitivity to sequence order or reversal. His head-and-tails example reverses the sequences, realigns them and reverses the result back to see whether the alignment changes.

### What branch-length problems should I check in a bacterial tree?

The discussion flags identical lengths, unexpectedly long branches and zero or near-zero branches as reasons to investigate. For SNP-only data, Conor also recommends checking ascertainment-bias correction or the inclusion of constant sites, alongside the expected biological relationships.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

11 Phylogenetics with the arborists part 1 by Microbial Bioinformatics
