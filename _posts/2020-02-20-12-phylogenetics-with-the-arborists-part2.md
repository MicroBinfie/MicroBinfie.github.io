---
layout: page
title: 'Episode 12: Phylogenetics with the arborists part 2'
date: '2020-02-20 00:00:00'
link: https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2
episode: '12'
soundcloud_track: '719460007'
tags:
- microbinfie
- podcast
description: Conor Meehan and Leonardo de Oliveira Martins discuss evolutionary models, recombination, SNP bias and whole-genome phylogenetics.
excerpt: Conor Meehan and Leonardo de Oliveira Martins discuss evolutionary models, recombination, SNP bias and whole-genome phylogenetics.
headline: Phylogenetic models, recombination and the limits of SNP trees
guests:
- Conor Meehan
- Leonardo de Oliveira Martins
topics:
- phylogenetics
- evolutionary models
- recombination
- supertrees
- ascertainment bias
- snp analysis
- indels
- whole-genome alignment
- phylogenetic uncertainty
- bacterial genomics
faq:
- q: Should I use HKY or GTR for a bacterial phylogeny?
  a: The guests say model choice depends on the data and can be assessed through model selection. Martins favours HKY’s analytical solution, while Meehan argues that under-parameterisation is generally more worrying than over-parameterisation; neither presents one model as universally correct.
- q: Why can SNP-only phylogenies have misleading branch lengths?
  a: Excluding constant sites changes the nucleotide frequencies seen by the model and omits information needed to estimate evolutionary change. The episode recommends including full sequence information where possible, or supplying appropriate constant-site information with an ascertainment-bias correction.
- q: Should recombinant regions always be removed before building a tree?
  a: Not without considering the question and how much information would be lost. For highly recombinant organisms, the guests suggest that networks, multiple regional trees or population-level approaches may be more useful than a single filtered tree.
- q: What is the difference between a supermatrix and a supertree?
  a: A supermatrix combines sequence data into one alignment for tree inference. A supertree combines information from individual trees; the guests see potential advantages for whole-gene transfer, but not a general solution to recombination within genes.
- q: Which paper discusses phylogenies being driven by a few genes?
  a: Martins recommends Contentious relationships in phylogenetic studies can be driven by a handful of genes, published in Nature Ecology & Evolution in 2017. He describes examples where removing a few genes, or a few sites within genes, changes the inferred phylogeny.
---

*Phylogenetic models, recombination and the limits of SNP trees*

Nabil-Fareed Alikhan continues the phylogenetics discussion with Conor Meehan and Leonardo de Oliveira Martins. They examine evolutionary models, recombination, supertrees and the biases introduced by analysing SNPs without constant sites. Throughout, they ask whether a single tree can answer the biological question, and what information is lost when genomic data are filtered or compressed.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 12: Phylogenetics with the arborists part 2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/719460007&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 12: Phylogenetics with the arborists part 2 on SoundCloud](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2)

## In this episode

### Choosing an evolutionary model

Evolutionary models describe changes between nucleotide or amino-acid states, including multiple substitutions at the same site. Meehan compares a useful model to the London Underground map: it should capture enough detail to answer the question without reproducing every feature of reality.

Martins favours HKY partly because his PhD supervisor was Kishino, the K in its name, and partly because it has an analytical solution. Meehan’s experience with HIV led him towards GTR and the view that under-parameterisation is generally more concerning than over-parameterisation. Both acknowledge that models are imperfect. Model selection is data-dependent: they contrast IQ-TREE’s testing of alternative models with RAxML’s traditional emphasis on GTR, while noting that other models can be specified.

### Rate variation and the information in indels

A substitution model is only part of the specification. Rates can vary across sites or along branches, and the discussion separates these forms of heterogeneity. Martins explains that CAT means category, not concatenate. The CAT models associated with RAxML and PhyloBayes are different: one concerns site-rate categories, while the other concerns amino-acid equilibrium frequencies. Gamma-distributed rates provide another way to describe variation among sites.

Insertions and deletions receive particular attention because ordinary substitution-based analyses do not explicitly model their evolutionary history. Martins highlights TKF91, TKF92 and the Poisson indel process as approaches that do. These models are computationally demanding, but could help estimate alignments and trees together. Ignoring indels can also discard useful information, particularly when examining non-coding regions.

### When recombination undermines a single tree

Meehan’s blunt starting point is that extensive recombination may make a single tree the wrong target. He cites Burkholderia pseudomallei as an example, with an estimate that 70–80% of its genome reflects recombination. Removing most of that information raises a basic question: what is the remaining tree intended to represent?

The guests discuss ClonalFrameML and Gubbins, phylogenetic networks such as those explored with SplitsTree, and Bayesian ancestral recombination graphs in BEAST. Martins cautions that a network summarising conflicting trees does not necessarily explain which genomic regions have different histories.

They distinguish recombination within genes from transfer of whole genes. Whole-gene transfers can be investigated using individual gene trees; within-gene recombination is harder. When recombination is relatively rare, trees and breakpoints along the genome may be recoverable. With very frequent recombination, population-level approaches may be more appropriate than seeking one tree.

### Supertrees and conflicting gene histories

A supermatrix combines sequences into one alignment. A supertree instead summarises information from multiple trees. Martins explains that supertrees historically combined trees with overlapping but incomplete species coverage; the term is now also used more broadly for summarising collections of gene trees.

The discussion covers subtree prune-and-regraft distances and an approximate implementation Martins contributed to the R package phangorn. Such approaches may help with whole-gene transfer, but the guests do not present them as a solution to within-gene recombination.

Different genes need not tell the same story. Martins uses Rashomon as an analogy and recommends the 2017 Nature Ecology & Evolution paper Contentious relationships in phylogenetic studies can be driven by a handful of genes. Its examples show that removing a few genes, or sites within genes, can change inferred relationships.

### Why SNP-only trees need constant-site information

Meehan calls ascertainment-bias correction of SNP data his pet peeve. Programs may assume they have received complete sequences containing both constant and variable sites, while users supply only SNPs. Alikhan reports that topology can remain broadly similar in his comparisons while branch lengths become unreliable.

The missing information affects nucleotide frequencies as well as estimates of change. Meehan uses Mycobacterium tuberculosis as an example: a high-GC genome can have variable sites with a very different base composition. Estimating a model from those sites alone can therefore distort branch lengths.

They compare the Lewis correction, which needs no additional constant-site counts, a Felsenstein correction using the total number of constant sites, and a Stamatakis approach using separate constant A, C, G and T counts. Their practical preference is to include the full sequence information where possible. They also warn that whole-genome sequencing data may exclude repetitive regions, so even an apparently complete dataset needs scrutiny.

### Scaling up without losing the biological question

Meehan and Alikhan separate diagnostic discrimination from evolutionary interpretation. A marker useful for diagnosis may contain too little variation for transmission analysis, while maximising differences between isolates does not automatically produce a meaningful evolutionary history. Martins also questions whether 100 SNPs can adequately resolve a tree with 1,000 tips.

For future development, Meehan wants Bayesian methods that can handle larger bacterial datasets, contrasting papers based on 20 isolates a decade earlier with expectations of hundreds of isolates. Both guests are interested in joint alignment and tree estimation. They discuss SATé and PASTA, alongside hidden Markov model approaches and indel-aware methods.

Martins’s broader priority is whole-genome alignment and its use in phylogenomics, including the promise of genome graphs. The closing advice is to understand the data before deciding how to build the tree.

## Highlights

- [00:02:04](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=2:04) — Why evolutionary models must account for changes between states and repeated substitutions.
- [00:02:53](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=2:53) — Rate heterogeneity across sites and branches, including different meanings of CAT.
- [00:06:48](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=6:48) — Martins explains his personal and mathematical reasons for preferring HKY.
- [00:08:01](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=8:01) — Model selection depends on the data rather than one universally best model.
- [00:09:05](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=9:05) — TKF91 and TKF92 explicitly model insertions and deletions.
- [00:11:57](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=11:57) — Extensive recombination can make a single tree an inappropriate target.
- [00:17:13](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=17:13) — Supertrees combine information from collections of individual trees.
- [00:22:16](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=22:16) — Methods built for complete gene sequences can be misused with SNP-only data.
- [00:24:25](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=24:25) — Ascertainment-bias corrections differ in the constant-site information they require.
- [00:27:04](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=27:04) — Scaling Bayesian phylogenetics to larger bacterial genomes and isolate collections.
- [00:29:42](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=29:42) — Genome graphs are discussed as a promising direction for whole-genome alignment.
- [00:30:06](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=30:06) — A 2017 paper shows how a handful of genes or sites can change a phylogeny.

## In their own words

> Understand your data and then build your tree from there.
>
> — Conor Meehan, [00:30:04](https://soundcloud.com/microbinfie/12-phylogenetics-with-the-arborists-part2#t=30:04)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Conor Meehan** (guest, University of Bradford)
- **Leonardo de Oliveira Martins** (guest, Quadram Institute Bioscience)
- **Lee Katz** (host)

## Tools and resources mentioned

HKY, GTR, IQ-TREE, RAxML, PhyloBayes, CAT models, Gamma-distributed rate models, TKF91, TKF92, Poisson indel process, ClonalFrameML, Gubbins, SplitsTree, BEAST, Subtree prune-and-regraft distance, phangorn, Lewis ascertainment-bias correction, Felsenstein ascertainment-bias correction, Stamatakis ascertainment-bias correction, SATé, PASTA, Hidden Markov models.

## Questions this episode answers

### Should I use HKY or GTR for a bacterial phylogeny?

The guests say model choice depends on the data and can be assessed through model selection. Martins favours HKY’s analytical solution, while Meehan argues that under-parameterisation is generally more worrying than over-parameterisation; neither presents one model as universally correct.

### Why can SNP-only phylogenies have misleading branch lengths?

Excluding constant sites changes the nucleotide frequencies seen by the model and omits information needed to estimate evolutionary change. The episode recommends including full sequence information where possible, or supplying appropriate constant-site information with an ascertainment-bias correction.

### Should recombinant regions always be removed before building a tree?

Not without considering the question and how much information would be lost. For highly recombinant organisms, the guests suggest that networks, multiple regional trees or population-level approaches may be more useful than a single filtered tree.

### What is the difference between a supermatrix and a supertree?

A supermatrix combines sequence data into one alignment for tree inference. A supertree combines information from individual trees; the guests see potential advantages for whole-gene transfer, but not a general solution to recombination within genes.

### Which paper discusses phylogenies being driven by a few genes?

Martins recommends Contentious relationships in phylogenetic studies can be driven by a handful of genes, published in Nature Ecology & Evolution in 2017. He describes examples where removing a few genes, or a few sites within genes, changes the inferred phylogeny.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

12 Phylogenetics with the arborists part 2 by Microbial Bioinformatics
