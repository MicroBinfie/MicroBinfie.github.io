---
layout: page
title: 'Episode 148: NextFlow debate 3'
date: '2025-11-13 00:00:00'
link: https://soundcloud.com/microbinfie/nextflow-debate-3
episode: '148'
soundcloud_track: '2194492795'
tags:
- microbinfie
- podcast
description: The hosts weigh Nextflow maintenance, nf-core standards, AI-assisted interpretation and alternatives including Galaxy, WDL, Terra and Snakemake.
excerpt: The hosts weigh Nextflow maintenance, nf-core standards, AI-assisted interpretation and alternatives including Galaxy, WDL, Terra and Snakemake.
headline: 'Nextflow debate: maintenance, AI and workflow alternatives'
guests: []
topics:
- workflow managers
- pipeline maintenance
- nf-core standards
- cloud computing
- ai-assisted coding
- quality control interpretation
- sample data management
- public health bioinformatics
- workflow alternatives
faq:
- q: What maintenance problems do the hosts identify with nf-core modules?
  a: Lee uses a locally modified SPAdes module to illustrate the work of merging upstream changes and retesting a professional pipeline. Andrew recommends contributing useful changes upstream rather than maintaining a separate fork.
- q: Why are the hosts concerned about AI interpretation in MultiQC?
  a: They worry that readers may accept an AI explanation without the experimental context available to a subject specialist. Andrew contrasts Salmonella with amplified-virus data and gives an example of an unexpected change in insert size.
- q: How do Terra and WDL compare with Nextflow in this discussion?
  a: Andrew describes Terra and WDL as sample-centric, with web access to standard validated pipelines. He contrasts this with the work users face connecting a sample’s Nextflow results across multiple analyses and directories.
- q: Do the hosts recommend Nextflow for every bioinformatics project?
  a: No. Nabil says the appropriate choice depends on learning requirements, scale and infrastructure, and suggests that Snakemake or custom Python scripts may be enough for some users.
---

*Nextflow debate: maintenance, AI and workflow alternatives*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan conclude their three-part Nextflow debate by examining maintenance, community standards, costs and AI. Lee again takes the cons position for the discussion, rather than necessarily expressing his own views. The hosts compare Nextflow with earlier workflow systems and current alternatives, asking how well each fits different users, infrastructure and data-management needs.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 148: NextFlow debate 3" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2194492795&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 148: NextFlow debate 3 on SoundCloud](https://soundcloud.com/microbinfie/nextflow-debate-3)

## In this episode

### Community stability versus maintenance work

Andrew recalls seven or eight internally developed workflow managers at the Sanger Institute. For him, Nextflow’s community and commercial backing offer continuity beyond an individual PhD or grant, while concentrating work on fixes and features.

Lee’s counterargument is that rapid development creates maintenance pressure. Versioning helps, but keeping a professional pipeline current still requires testing. His example is a locally modified fork of an nf-core SPAdes module: upstream updates must be merged, checked and tested against those local changes. Andrew argues that useful modifications should instead be contributed upstream through pull requests, so others can benefit and the changes need not remain a separate local responsibility.

### What nf-core standardisation gives and takes

Nabil describes nf-core’s standards as opinionated: following them can mean accepting choices that are not optimal for a particular project. Taking a pipeline as a template and diverging remains possible, but the team then owns the resulting maintenance problems.

Andrew values the alternative to every incoming postdoc writing another SNP caller or mapping pipeline. For standard tasks, he often prefers nf-core over a bespoke analysis that might produce a slightly different result but take weeks to develop. Andrew also praises Seqera Tower, formerly Nextflow Tower, for making repository-based workflows and cloud execution easier, though he notes it can be a little pricey, and Lee stresses that it is expensive for professional use. They give no prices.

### AI-generated code is not expert interpretation

The hosts ask whether AI-generated workflow code needs to target Nextflow at all. Lee also argues, from his cons position, that difficult error messages can push users towards Copilot, Claude or ChatGPT for help.

His sharper concern is AI interpretation inside MultiQC reports. A collaborator or molecular biologist could ask an embedded assistant to explain results without consulting the expert who produced the analysis. Andrew illustrates the missing context: Salmonella data and data from an amplified virus require different judgements, even when outputs look similar. An expected insert size of 400 becoming 200 might need investigation rather than reassurance.

Andrew worries about users accepting subtle errors without understanding the underlying work. Nevertheless, he recommends Claude Sonnet 4 as his current coding assistant, preferring it to ChatGPT 5.

### From internal Perl systems to shared infrastructure

Andrew traces his experience through internal Perl workflow managers, including VR codebase and VR tracking, then Galaxy and Nextflow. Those early systems handled tens of thousands of samples but remained tied to one organisation. Galaxy’s web interface let biologists with little technical knowledge use standard tools and pipelines; Andrew sees Nextflow as a further step towards scalable cloud execution.

Lee describes unsuccessful experience with Bpipe, which his team abandoned after repeated crashes. Although he still feels the pull to build something better, he acknowledges how difficult a reliable workflow manager is to create. He identifies WDL as another alternative that people are using successfully.

### Terra, WDL and keeping results with samples

Andrew describes Terra and WDL as a different approach, used in public health to give biologists and epidemiologists access to standard, validated pipelines through a web interface. He characterises that environment as sample-centric: an analysis output belongs to a particular sample.

By contrast, he says users must solve the problem of connecting Nextflow outputs themselves. His example is remembering that one sample has passed through 10 analyses in 20 directories, then bringing the results together. He identifies this kind of results management as a gap in Seqera Tower and asks listeners for solutions. Nabil has seen Terra demonstrations but has not used it himself.

### Choosing a workflow model that fits

Nabil does not recommend Nextflow for everyone. The learning curve, infrastructure and scale matter; custom Python scripts or Snakemake may suit someone working on a laptop. He says a person with some programming knowledge can get started with Snakemake in an afternoon, without handling threading and resource management directly. Lee also argues that Make is an excellent workflow manager.

Nabil introduces Airflow and Dagster while discussing task- or data-oriented approaches. Rather than simply specifying a sequence of processes, he describes defining required values, types and relationships, then running tasks to fill gaps or refresh inconsistent records. He has not yet seen a bioinformatics implementation of this approach that makes sense to him.

## Highlights

- [00:00:03](https://soundcloud.com/microbinfie/nextflow-debate-3#t=0:03) — Lee introduces the final debate instalment and again takes the cons position.
- [00:01:19](https://soundcloud.com/microbinfie/nextflow-debate-3#t=1:19) — Community and commercial backing offer stability beyond internal workflow managers.
- [00:02:14](https://soundcloud.com/microbinfie/nextflow-debate-3#t=2:14) — Rapid updates create versioning, merging and testing work for maintained pipelines.
- [00:04:31](https://soundcloud.com/microbinfie/nextflow-debate-3#t=4:31) — Opinionated nf-core standards trade local flexibility for shared conventions.
- [00:06:13](https://soundcloud.com/microbinfie/nextflow-debate-3#t=6:13) — Shared nf-core pipelines reduce repeated development of standard analyses.
- [00:07:41](https://soundcloud.com/microbinfie/nextflow-debate-3#t=7:41) — Convenient nf-core execution leads into the costs of the wider hosted ecosystem.
- [00:10:03](https://soundcloud.com/microbinfie/nextflow-debate-3#t=10:03) — AI interpretation can miss organism-specific and experimental context.
- [00:13:52](https://soundcloud.com/microbinfie/nextflow-debate-3#t=13:52) — Andrew traces the progression from internal Perl workflows to Galaxy and Nextflow.
- [00:17:28](https://soundcloud.com/microbinfie/nextflow-debate-3#t=17:28) — Terra and WDL provide sample-centric public-health workflows.
- [00:19:04](https://soundcloud.com/microbinfie/nextflow-debate-3#t=19:04) — Workflow choices depend on users’ skills, scale and infrastructure.
- [00:20:56](https://soundcloud.com/microbinfie/nextflow-debate-3#t=20:56) — Data-oriented workflows can fill missing values and reconcile related records.
- [00:22:25](https://soundcloud.com/microbinfie/nextflow-debate-3#t=22:25) — Snakemake offers an accessible starting point for people with some programming knowledge.

## In their own words

> I would not go and say Nextflow is for everyone.
>
> — Nabil-Fareed Alikhan, [00:19:04](https://soundcloud.com/microbinfie/nextflow-debate-3#t=19:04)

> It's whatever the machine is telling them.
>
> — Lee Katz, [00:07:41](https://soundcloud.com/microbinfie/nextflow-debate-3#t=7:41)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Nextflow, nf-core, SPAdes, Seqera Tower, Nextflow Tower, MultiQC, Copilot, Claude, Claude Sonnet 4, ChatGPT, ChatGPT 5, Galaxy, VR codebase, VR tracking, Bpipe, WDL, Terra, Snakemake, Make, CWL, Airflow, Dagster.

## Questions this episode answers

### What maintenance problems do the hosts identify with nf-core modules?

Lee uses a locally modified SPAdes module to illustrate the work of merging upstream changes and retesting a professional pipeline. Andrew recommends contributing useful changes upstream rather than maintaining a separate fork.

### Why are the hosts concerned about AI interpretation in MultiQC?

They worry that readers may accept an AI explanation without the experimental context available to a subject specialist. Andrew contrasts Salmonella with amplified-virus data and gives an example of an unexpected change in insert size.

### How do Terra and WDL compare with Nextflow in this discussion?

Andrew describes Terra and WDL as sample-centric, with web access to standard validated pipelines. He contrasts this with the work users face connecting a sample’s Nextflow results across multiple analyses and directories.

### Do the hosts recommend Nextflow for every bioinformatics project?

No. Nabil says the appropriate choice depends on learning requirements, scale and infrastructure, and suggests that Snakemake or custom Python scripts may be enough for some users.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Final part of our discussion/debate on NextFlow
