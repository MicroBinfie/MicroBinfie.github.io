---
layout: page
title: 'Episode 17: Bayesian magic in practice'
date: '2020-04-30 00:00:00'
link: https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice
episode: '17'
soundcloud_track: '739228246'
tags:
- microbinfie
- podcast
description: 'Practical Bayesian phylogenetics: learning RevBayes, checking MCMC convergence, comparing clock models and testing priors and sampling dates.'
excerpt: 'Practical Bayesian phylogenetics: learning RevBayes, checking MCMC convergence, comparing clock models and testing priors and sampling dates.'
headline: 'Bayesian phylogenetics: software, clocks and practical checks'
guests:
- Conor Meehan
- Leo Martins
topics:
- bayesian phylogenetics
- microbial bioinformatics
- molecular epidemiology
- mcmc convergence
- molecular clocks
- prior distributions
- model comparison
- time trees
- mycobacterium tuberculosis
faq:
- q: Where should I start learning practical Bayesian phylogenetics?
  a: The guests recommend RevBayes tutorials for understanding parameters and their relationships, and Taming the Beast for worked biological examples. Stan is also suggested as a widely used modelling language.
- q: How can I check whether my Bayesian phylogenetic analysis has converged?
  a: Use tools such as Tracer to inspect traces, effective sample sizes and agreement between independent runs. RWTY adds checks based on the sampled trees themselves; simply running an analysis for several weeks is not enough.
- q: Are Bayesian phylogenetic trees always time trees?
  a: No. The panel distinguishes BEAST's clock-based time trees from Bayesian analyses in MrBayes, PhyloBayes and RevBayes that need not be time-calibrated. LSD is discussed as a non-Bayesian route to constructing a time tree from a maximum-likelihood tree.
- q: How can I test whether my data are informing the Bayesian result?
  a: 'Run the model without data and compare the resulting prior distribution with the posterior. For dating analyses, the panel also recommends randomising tip dates: recovering the same root age can indicate that the original sampling dates contribute little information.'
---

*Bayesian phylogenetics: software, clocks and practical checks*

Nabil-Fareed Alikhan is joined by Conor Meehan and Leo Martins for a practical follow-up on Bayesian analysis in microbial bioinformatics. They discuss learning tools, checking MCMC convergence, choosing phylogenetic models and testing how much information the data contribute. Molecular epidemiology and Mycobacterium tuberculosis provide recurring examples.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 17: Bayesian magic in practice" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/739228246&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 17: Bayesian magic in practice on SoundCloud](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice)

## In this episode

### Where to start learning

Graphical models offer a way into Bayesian statistics by making parameters and their dependencies explicit. The discussion introduces Stan, BUGS, WinBUGS and the Rev language used by RevBayes. Rather than treating an analysis as a black box, learners can describe how parameters interact, use data to obtain a posterior distribution, or simulate data from a model. Plate notation provides a visual counterpart: circles, squares and arrows describe variables and conditional relationships.

The guests recommend RevBayes tutorials and Taming the Beast for practical exercises. Taming the Beast has online introductory, intermediate and advanced material alongside its in-person courses. Many examples concern eukaryotes, including bears, but the panel recommends them for understanding both the inputs to an analysis and the results it produces.

### Developing a Bayesian method

Writing a Bayesian version of an existing method is not presented as a straightforward coding exercise. One guest describes how a first-author paper from his Bayesian phylogenetics PhD turned out to contain a mistake: someone else published a correction, which he reviewed and had to accept. The lesson is to involve someone who can check the statistical model, proposals and conditional relationships, even when the implementation feels well tested.

Two starting points are suggested. Simulated annealing is the optimisation counterpart of a Bayesian model: it searches for the best values rather than estimating the full posterior, so it still works even if the conditionals contain mistakes, as long as the best value is the same. The guest routinely implements a simulated annealing version of his models to check the maximum likelihood estimate. ABC offers a simulation-based route when the likelihood cannot be calculated: simulated outputs are accepted according to rules, producing a distribution used as a posterior approximation. The panel also stresses that phylogenetic analyses need organism-specific biological knowledge rather than completely automatic choices of priors.

### Checking convergence and reporting uncertainty

A long runtime is not evidence that an MCMC analysis has finished. Tracer is recommended for inspecting traces, effective sample sizes and agreement between independent runs. RWTY, expanded as Are We There Yet, examines sampled trees and their movement through tree space; CODA is mentioned for analyses outside phylogenetics.

One guest commonly runs an analysis four or five times, compares the results, then combines and thins samples. Retaining around 10,000 samples is described as a personal workflow, not a universal requirement. Combining results also depends on using the same model and parameters.

The discussion distinguishes log-file results, such as mutation-rate estimates, from summaries of sampled trees. A maximum a posteriori tree is described as the tree appearing most frequently in the posterior sample, while continuous parameters can be summarised with means or medians. FigTree is suggested for displaying uncertainty: a tree figure should not conceal the uncertainty behind it.

### Choosing software and understanding time trees

BEAST is praised for its graphical interface and accompanying tools for combining, thinning and summarising outputs. Ease of use also creates a risk: users may accept defaults without understanding the analysis. The panel notes that newer versions warn when defaults have not been changed. BEAST 1 and BEAST 2 are discussed as separate projects rather than simply successive releases of one programme.

A central distinction is that Bayesian trees do not necessarily have to be time trees. BEAST is described as requiring a clock model, whereas MrBayes, PhyloBayes and RevBayes support analyses that need not be time-calibrated. RevBayes makes model choices explicit through scripting, which is useful but potentially demanding for beginners.

For a non-Bayesian route, LSD is discussed as taking a maximum-likelihood tree, a mutation rate and sampling times to construct a time tree quickly.

### Clock models, coalescence and model comparison

The tree itself is part of the evolutionary model, not something separate from it. Molecular clock models connect genetic change with elapsed time. The guests contrast strict clocks, with one rate across the tree, and relaxed clocks, with rates varying among branches. They also discuss exponential and log-normal rate distributions and whether rates on related branches are correlated.

The practical advice is to test alternatives rather than infer the right model from an outbreak label alone. Path sampling and stepping-stone approaches estimate marginal likelihoods, allowing comparison through Bayes factors. These calculations can be expensive: the panel describes running chains 30 or 40 times for such comparisons.

Coalescent models provide another component, describing how sampled lineages trace back to common ancestors and how population size changes through time. Birth-death skyline models are also mentioned as options whose relevance depends on the biological question.

### Testing priors, dates and biological plausibility

A clock-rate paper by Sebastian Duchêne and colleagues is discussed as a starting point for choosing a prior, not a fixed answer for every dataset. For Mycobacterium tuberculosis, the panel notes differences among lineages and between short- and long-term evolution. Published estimates can guide the prior while still allowing other values to be explored.

Two checks test what the data contribute. First, run the model without data to sample its prior distribution, then compare that with the posterior. Similar distributions can warn that the data have added little information. Second, randomly reassign sampling dates among tips and check whether the estimated root age changes. If the same age emerges, the original tip dates may not be informative enough to support confidence in the dating result.

The closing advice is to collaborate across biology, bioinformatics and Bayesian modelling. Biological sense-checks matter too: an inferred origin of multidrug-resistant tuberculosis before the relevant drugs existed would demand investigation.

## Highlights

- [00:01:19](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=1:19) — Graphical models and learning Bayesian statistics with Stan and RevBayes.
- [00:02:47](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=2:47) — Taming the Beast tutorials and biological practice datasets.
- [00:04:20](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=4:20) — Why even experienced developers need statistical collaborators.
- [00:05:16](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=5:16) — Simulated annealing as a starting point for developing Bayesian software.
- [00:07:43](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=7:43) — Checking convergence with Tracer, effective sample sizes and repeated runs.
- [00:11:45](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=11:45) — BEAST's interface, supporting tools and the risks of accepting defaults.
- [00:12:58](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=12:58) — BEAST 1 and BEAST 2 as separate projects.
- [00:18:04](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=18:04) — The phylogenetic tree as part of the evolutionary model.
- [00:22:40](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=22:40) — Comparing models using marginal likelihoods, path sampling and stepping stones.
- [00:24:57](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=24:57) — Using published clock-rate estimates as a starting point.
- [00:26:43](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=26:43) — Running without data to compare the prior with the posterior.
- [00:28:21](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=28:21) — Randomising tip dates to test their contribution to estimated root ages.

## In their own words

> I often run any of my analysis by somebody else as well, just to be sure.
>
> — a guest, [00:05:12](https://soundcloud.com/microbinfie/17-bayesian-magic-in-practice#t=5:12)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Conor Meehan** (guest, University of Bradford)
- **Leo Martins** (guest, Quadram Institute Bioscience)

Also mentioned: Sebastian Duchêne.

## Tools and resources mentioned

Stan, BUGS, WinBUGS, RevBayes, BEAST, BEAST 2, MrBayes, PhyloBayes, Tracer, RWTY, CODA, FigTree, LSD, Markov chain Monte Carlo (MCMC), Simulated annealing, ABC, Plate notation, Path sampling, Stepping-stone sampling, Bayes factors, Coalescent models, Birth-death skyline models, Tip-date randomisation.

## Questions this episode answers

### Where should I start learning practical Bayesian phylogenetics?

The guests recommend RevBayes tutorials for understanding parameters and their relationships, and Taming the Beast for worked biological examples. Stan is also suggested as a widely used modelling language.

### How can I check whether my Bayesian phylogenetic analysis has converged?

Use tools such as Tracer to inspect traces, effective sample sizes and agreement between independent runs. RWTY adds checks based on the sampled trees themselves; simply running an analysis for several weeks is not enough.

### Are Bayesian phylogenetic trees always time trees?

No. The panel distinguishes BEAST's clock-based time trees from Bayesian analyses in MrBayes, PhyloBayes and RevBayes that need not be time-calibrated. LSD is discussed as a non-Bayesian route to constructing a time tree from a maximum-likelihood tree.

### How can I test whether my data are informing the Bayesian result?

Run the model without data and compare the resulting prior distribution with the posterior. For dating analyses, the panel also recommends randomising tip dates: recovering the same root age can indicate that the original sampling dates contribute little information.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

The second part of the dark world of Bayesian magic with Dr Conor
Meehan, Dr. Leo Martins and Dr Nabil-Fareed Alikhan.
