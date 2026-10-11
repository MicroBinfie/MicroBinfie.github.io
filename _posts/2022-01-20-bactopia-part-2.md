---
layout: page
title: 'Episode 73: Bactopia and using workflow managers in bioinformatics part 2'
date: '2022-01-20 00:00:00'
link: https://soundcloud.com/microbinfie/bactopia-part-2
episode: '73'
soundcloud_track: '1131859324'
tags:
- microbinfie
- podcast
description: Robert Petit discusses workflow managers, Prokka and containers, and when custom bioinformatics scripts should become reproducible workflows.
excerpt: Robert Petit discusses workflow managers, Prokka and containers, and when custom bioinformatics scripts should become reproducible workflows.
headline: Bactopia, reproducible workflows and life beyond Bash
guests:
- Robert Petit
topics:
- workflow managers
- bacterial genomics
- reproducibility
- pipeline portability
- genome annotation
- dependency management
- software containers
- high-performance computing
- system administration
faq:
- q: Why use a workflow manager instead of a Bash script for bioinformatics?
  a: The panel emphasises restarting failed analyses, tracking inputs and outputs, managing dependencies and moving between computing environments. These features avoid repeatedly implementing fragile checks and scheduler-specific scripts.
- q: When is a workflow manager unnecessary?
  a: A quick, one-off analysis or simple file manipulation may not justify the setup effort. The panel sees more value when an analysis will be repeated, shared or reused in another workflow.
- q: Can workflow managers be useful on a laptop?
  a: Yes. Robert describes testing a small dataset locally and then changing the execution configuration to run on Slurm. The discussion also highlights consistent environments when moving between machines.
- q: How do Conda and containers help bioinformatics workflows?
  a: A workflow can specify a Conda environment or use a Docker or Singularity container, reducing manual installation and making software versions explicit. The panel also discusses how Bioconda recipes and container builds let users share that setup work.
- q: Do beginners need to write workflows before using them?
  a: 'No: the episode distinguishes running an existing workflow from developing one. Existing workflows can handle dependencies and file movement for beginners, although failures still require investigation or support.'
---

*Bactopia, reproducible workflows and life beyond Bash*

Robert Petit of the Wyoming Public Health Laboratory returns for a discussion of Bactopia and the shift from custom scripts to workflow managers. The conversation covers restarting failed analyses, managing software dependencies, moving between computing environments and reusing other people's work. The panel also considers when a simple script is enough, and how existing workflows can help newcomers without removing the need to understand failures.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 73: Bactopia and using workflow managers in bioinformatics part 2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1131859324&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 73: Bactopia and using workflow managers in bioinformatics part 2 on SoundCloud](https://soundcloud.com/microbinfie/bactopia-part-2)

## In this episode

### Why move beyond Bash scripts?

Bactopia, a workflow designed for bacterial genomes, provides the starting point for this wider discussion. Robert Petit is introduced as developing bioinformatics infrastructure at the Wyoming Public Health Laboratory to support its SARS-CoV-2 sequencing response. His earlier work includes Staphopia and a typing scheme for identifying Bacillus anthracis in metagenomic sequences. The show notes identify the Bactopia paper by DOI: 10.1128/mSystems.00190-20.

The central question is why routine tasks—quality control, genotyping, metrics and species-specific typing—have moved from custom Bash scripts towards workflow managers. Restarting failed analyses is an immediate advantage: checking that a file exists does not necessarily establish that a step finished successfully. Reproducibility and portability are equally important. Rather than rebuilding the same machinery, developers can use frameworks that manage inputs, outputs and execution across a laptop, a Slurm cluster or Google Cloud.

### The cost of building everything yourself

Lee Katz describes learning to use completion-marker files and then repeatedly implementing similar checks in his own pipelines. His SNP pipeline and SneakerNet illustrate the problem: useful analyses also required custom logic to decide which work had already been done. He reflects that adopting a workflow manager earlier could have avoided some of that repeated development.

Another host recalls spending months writing Python scripts around Fabric to transfer reads, create PBS batch scripts and submit jobs to an HPC system. Despite that effort, the pipeline remained fragile and needed manual checking between stages. It was tied to its scheduler: on a different cluster the scripts would break, and running a small batch on a laptop was not possible.

### Dependencies and reusable building blocks

Workflow managers also reduce the work involved in preparing software environments. The panel discusses giving Nextflow a YAML description of a Conda environment, or using Docker and Singularity containers. These approaches make tool versions explicit and reduce the need to reinstall and reconfigure everything on each machine. They are not presented as infallible: one host estimates that the Conda approach works 95% of the time, with exceptions.

Shared code matters alongside shared environments. GitHub and GitLab make reporting problems and contributing fixes more direct than trying to reach a tool's author by email. The discussion points to nf-core and Nextflow Patterns as useful examples, and to Nextflow DSL 2 as a way to organise work into reusable modules rather than one large workflow.

### Prokka and the annotation workload

Prokka is used as an example of the field converging on a practical solution. Robert recalls a class exercise in which groups had to assemble an annotation workflow from multiple programs, followed by the discovery that Prokka already brought bacterial annotation together. The point is not that every successful pipeline must use a workflow language: Prokka's Perl implementation had been doing its job well for almost ten years.

Lee contrasts this with a more extensive genome annotation pipeline he helped develop, which was harder to install and run. The discussion includes TMHMM, SignalP and InterProScan, illustrating the dependency burden of a broader analysis. A host also highlights Prokka's trimmed Swiss-Prot database, contrasting it with searching every gene against all of nr. Defining the useful first-pass result can be as important as adding more analyses.

### When a small script is enough

The panel does not recommend turning every command into a managed workflow. A quick, one-off analysis or some file manipulation may take less effort in a Bash script. The case becomes stronger when an analysis will be repeated, shared or reused as part of another workflow.

Workflow managers are not reserved for large computing systems. Robert describes testing a small dataset locally before changing the execution configuration to submit work to Slurm. They can also handle queue submission without requiring a fresh set of batch scripts. Another host finds them increasingly useful when moving analyses between virtual machines, where consistent dependencies and configuration matter even without a large HPC workload.

### Making analysis accessible without hiding every problem

Existing workflows can help people with little command-line experience obtain results because dependency installation and file handling happen behind the scenes. That is different from asking a beginner to write a workflow. When something breaks, users still need to investigate or ask for help, and regular bioinformatics practitioners are encouraged to invest time in learning a workflow language.

The panel also questions how much system administration bioinformaticians should have to do. Galaxy offers a graphical abstraction, while command-line workflows can retain configurable control. Bioconda, BioContainers and automatically generated Singularity images are presented as ways to share installation effort. The closing message is that the particular language matters less than introducing structure, reproducibility and portability into workflow design.

## Highlights

- [00:03:12](https://soundcloud.com/microbinfie/bactopia-part-2#t=3:12) — Resuming failed analyses, reproducibility and portability beyond custom Bash scripts
- [00:06:19](https://soundcloud.com/microbinfie/bactopia-part-2#t=6:19) — Lee Katz reflects on completion markers and repeatedly building custom pipelines
- [00:07:52](https://soundcloud.com/microbinfie/bactopia-part-2#t=7:52) — A Fabric-based HPC pipeline illustrates months of development and fragile automation
- [00:11:50](https://soundcloud.com/microbinfie/bactopia-part-2#t=11:50) — Shared best practices and Prokka as a milestone in bacterial annotation
- [00:13:25](https://soundcloud.com/microbinfie/bactopia-part-2#t=13:25) — Lee describes building a more extensive but harder-to-install annotation pipeline
- [00:16:07](https://soundcloud.com/microbinfie/bactopia-part-2#t=16:07) — Why a quick Bash script can still be appropriate for a one-off analysis
- [00:19:27](https://soundcloud.com/microbinfie/bactopia-part-2#t=19:27) — Prototyping locally with a small test set before running on a cluster
- [00:21:13](https://soundcloud.com/microbinfie/bactopia-part-2#t=21:13) — How existing workflows help beginners, and what happens when an analysis breaks
- [00:24:48](https://soundcloud.com/microbinfie/bactopia-part-2#t=24:48) — Breaking large workflows into modules and reusing other people's code
- [00:26:29](https://soundcloud.com/microbinfie/bactopia-part-2#t=26:29) — Bioconda and container builds reduce repeated software installation work
- [00:27:19](https://soundcloud.com/microbinfie/bactopia-part-2#t=27:19) — The closing advice: focus on workflow structure rather than language choice

## In their own words

> I don't think there's been a day in my bioinformatics career where I haven't also acted as a sys administrator for some server that we're processing on.
>
> — Robert Petit, [00:23:56](https://soundcloud.com/microbinfie/bactopia-part-2#t=23:56)

> It doesn't matter what language you pick, just start playing around with it and getting used to thinking of it that way.
>
> — one of the hosts, [00:27:19](https://soundcloud.com/microbinfie/bactopia-part-2#t=27:19)

## Who is talking

- **Robert Petit** (guest, Wyoming Public Health Laboratory)
- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Bactopia, Staphopia, Nextflow, Snakemake, WDL, CWL, Galaxy, Airflow, Swift, Bash, Fabric, PBS, Slurm, Google Cloud, Conda, Bioconda, Docker, Singularity, BioContainers, nf-core, Nextflow Patterns, GitHub, GitLab, Prokka, TMHMM, SignalP, InterProScan, Swiss-Prot, nr, SneakerNet, BLAST, Velvet.

## Questions this episode answers

### Why use a workflow manager instead of a Bash script for bioinformatics?

The panel emphasises restarting failed analyses, tracking inputs and outputs, managing dependencies and moving between computing environments. These features avoid repeatedly implementing fragile checks and scheduler-specific scripts.

### When is a workflow manager unnecessary?

A quick, one-off analysis or simple file manipulation may not justify the setup effort. The panel sees more value when an analysis will be repeated, shared or reused in another workflow.

### Can workflow managers be useful on a laptop?

Yes. Robert describes testing a small dataset locally and then changing the execution configuration to run on Slurm. The discussion also highlights consistent environments when moving between machines.

### How do Conda and containers help bioinformatics workflows?

A workflow can specify a Conda environment or use a Docker or Singularity container, reducing manual installation and making software versions explicit. The panel also discusses how Bioconda recipes and container builds let users share that setup work.

### Do beginners need to write workflows before using them?

No: the episode distinguishes running an existing workflow from developing one. Existing workflows can handle dependencies and file movement for beginners, although failures still require investigation or support.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We are again joined by Dr Robert Petit from the Wyoming Public Health
Laboratory who is talking to us about BACTOPIA, a bioinformatics
workflow specifically for bacterial genomes.  Docs:
https://bactopia.github.io/  Repo:
https://github.com/bactopia/bactopia/ Pub:
https://doi.org/10.1128/mSystems.00190-20
