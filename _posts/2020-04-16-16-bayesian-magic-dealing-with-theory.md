---
layout: page
title: 'Episode 16: The theory behind Bayesian Magic'
date: '2020-04-16 00:00:00'
link: https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory
episode: '16'
soundcloud_track: '739227472'
tags:
- microbinfie
- podcast
description: Nabil-Fareed Alikhan, Conor Meehan and Leo Martins discuss Bayesian phylogenetics, MCMC, uncertainty and reproducible analyses.
excerpt: Nabil-Fareed Alikhan, Conor Meehan and Leo Martins discuss Bayesian phylogenetics, MCMC, uncertainty and reproducible analyses.
headline: 'Bayesian phylogenetics: priors, MCMC and uncertainty'
guests:
- Conor Meehan
- Leo Martins
topics:
- bayesian inference
- phylogenetics
- priors
- posterior distributions
- mcmc
- convergence
- molecular epidemiology
- reproducibility
faq:
- q: What is a posterior distribution in Bayesian phylogenetics?
  a: It describes a parameter after combining prior information with the likelihood from the data. The episode discusses posterior distributions for trees and mutation rates, emphasising that they retain uncertainty rather than supplying only a single value.
- q: Is Bayesian inference the same thing as MCMC?
  a: No. Bayesian inference defines the statistical model, while MCMC is an algorithm used to sample from its posterior distribution. The episode also discusses analytical solutions and variational inference.
- q: What should a Bayesian phylogenetics paper report?
  a: The panel asks for explicit model and prior settings, justification of those choices, convergence checks and uncertainty distributions or credible intervals. Sharing a BEAST configuration file is suggested as a practical way to support reproducibility.
- q: Do I need Bayesian inference just to reconstruct a tree?
  a: The panel suggests that a good maximum-likelihood analysis may be enough if the tree is the only goal. Bayesian analysis becomes more attractive when the research question involves other model components, such as mutation rates, dates or population processes.
---

*Bayesian phylogenetics: priors, MCMC and uncertainty*

Nabil-Fareed Alikhan joins guests Conor Meehan and Leo Martins to examine Bayesian inference in microbial phylogenetics. They explain priors and posterior distributions, distinguish statistical models from MCMC algorithms, and discuss why convergence and uncertainty need careful attention. Examples from tuberculosis, HIV and Ebola show how an analysis can investigate more than the shape of a tree.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 16: The theory behind Bayesian Magic" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/739227472&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 16: The theory behind Bayesian Magic on SoundCloud](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory)

## In this episode

### Priors, likelihoods and posterior distributions

The discussion introduces Bayesian inference as a class of models based on conditional probabilities, rather than a philosophy or belief system. A prior describes expectations about a parameter before examining the particular dataset. Combining that prior with the likelihood produces a posterior distribution: an updated description that still includes uncertainty.

A mutation-rate example starts with an estimate of around 10^-7 for Mycobacterium tuberculosis. That knowledge could inform a broad prior for another Mycobacterium species, while allowing the new data to favour a different value. The panel stresses that prior information can come from previous, well-supported research. It is not simply permission to impose an arbitrary personal preference on an analysis.

### The tree need not be the final result

A basic maximum-likelihood analysis in RAxML produces a phylogeny, but a Bayesian analysis can treat the tree as one component of a larger model. Sampling dates, locations, mutation rates and population processes can contribute to questions beyond topology.

Conor describes a Stadler paper on the Ebola outbreak that used a tree someone else had already built to investigate reproductive number and incubation time. He points out that the paper has no tree in it but is still entirely Bayesian statistics. The broader point is that researchers can supply some parts of a model and investigate others, rather than always treating tree reconstruction as the endpoint.

### Bayesian models and MCMC are different

Leo distinguishes the statistical model from the algorithm used to obtain results. Some Bayesian models have analytical solutions; conjugate priors are discussed as a case where the posterior belongs to the same distribution family as the prior. More complex, hierarchical models often require computational sampling.

MCMC is explained through a basket analogy: each cycle contributes a sample containing the current tree and other parameter values. A rejected proposal leaves the previous state in place, so it can appear repeatedly in the collection. The resulting samples are used to describe posterior distributions. Leo also introduces variational inference as an alternative that seeks an easier-to-calculate distribution resembling the posterior, while describing MCMC as phylogenetics’ workhorse.

### Convergence, thinning and computational cost

The panel discusses discarding early samples as burn-in, because the starting tree and initial parameter values may be poor. Neighbouring MCMC states can be correlated, leading into thinning and effective sample size: a long chain does not automatically provide an equally large amount of independent information.

Convergence is a recurring practical concern. Separate runs can produce similar best trees yet different distributions, leaving uncertainty about whether longer runs are needed. Conor contrasts his experience of HIV analyses using chains of roughly 10,000–20,000 steps with tuberculosis analyses normally requiring 40 million. These are examples from his work, not universal settings. Discovering a poorly specified parameter after a lengthy run can mean starting again.

### Assumptions matter more than statistical labels

Flat-hunting and restaurant choices provide everyday analogies for updating expectations and exploring alternatives. A roulette question then prompts discussion of the gambler’s fallacy, independent observations and model assumptions. The guests resist treating such problems as failures unique to Bayesian inference.

For microbial applications, the underlying study design still matters. Population-size analysis is given as an example requiring a single population sampled randomly under the model being discussed. The panel also argues for choosing methods pragmatically: a good maximum-likelihood analysis may be sufficient when the goal is simply a tree. More elaborate models need justification, understandable assumptions and simple sanity checks.

### What a convincing analysis should report

A reproducible Bayesian methods section should describe the model’s components, prior distributions and their settings, rather than merely name a program. Choices should be justified through relevant previous work or model comparison; marginal likelihood analysis is discussed in this context.

For software such as BEAST, the panel recommends sharing the configuration file containing the model settings, for example through FigShare. This is compared with publishing a laboratory standard operating procedure so others can repeat an experiment.

Results should show distributions and uncertainty, not just a preferred tree or a single date. Credible intervals and highest posterior density are discussed, alongside convergence checks and testing whether the data are informative. An analysis can return a tree and a distribution even after an inadequate run; obtaining output is not itself evidence that the answer is dependable.

## Highlights

- [00:01:14](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=1:14) — Bayesian inference as conditional-probability models, not a belief system
- [00:05:22](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=5:22) — How priors, likelihoods and posterior distributions relate
- [00:16:34](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=16:34) — Using an Ebola phylogeny to study reproductive number and incubation time
- [00:18:13](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=18:13) — Separating Bayesian models from MCMC and introducing variational inference
- [00:21:12](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=21:12) — A basket-of-samples explanation of MCMC cycles and proposals
- [00:25:22](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=25:22) — Correlated chain states, thinning and effective sample size
- [00:28:52](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=28:52) — Why convergence is difficult to establish for large phylogenetic analyses
- [00:34:16](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=34:16) — Coin tosses, roulette and the importance of model assumptions
- [00:38:48](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=38:48) — Reporting prior settings and justifying model choices
- [00:44:20](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=44:20) — Deciding whether Bayesian analysis is necessary for the research question

## In their own words

> I want to see the distribution of values because otherwise it's not Bayesian.
>
> — Leo Martins, [00:41:24](https://soundcloud.com/microbinfie/16-bayesian-magic-dealing-with-theory#t=41:24)

## Who is talking

- **Nabil-Fareed Alikhan** (host)
- **Conor Meehan** (guest, University of Bradford)
- **Leo Martins** (guest, Quadram Institute Bioscience)

## Tools and resources mentioned

Bayesian inference, maximum likelihood, RAxML, bootstrapping, MCMC, variational inference, marginal likelihood analysis, BEAST, FigShare, parsimony.

## Questions this episode answers

### What is a posterior distribution in Bayesian phylogenetics?

It describes a parameter after combining prior information with the likelihood from the data. The episode discusses posterior distributions for trees and mutation rates, emphasising that they retain uncertainty rather than supplying only a single value.

### Is Bayesian inference the same thing as MCMC?

No. Bayesian inference defines the statistical model, while MCMC is an algorithm used to sample from its posterior distribution. The episode also discusses analytical solutions and variational inference.

### What should a Bayesian phylogenetics paper report?

The panel asks for explicit model and prior settings, justification of those choices, convergence checks and uncertainty distributions or credible intervals. Sharing a BEAST configuration file is suggested as a practical way to support reproducibility.

### Do I need Bayesian inference just to reconstruct a tree?

The panel suggests that a good maximum-likelihood analysis may be enough if the tree is the only goal. Bayesian analysis becomes more attractive when the research question involves other model components, such as mutation rates, dates or population processes.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

The dark world of Bayesian magic with Dr Conor Meehan, Dr. Leo Martins
and Dr Nabil-Fareed Alikhan.
