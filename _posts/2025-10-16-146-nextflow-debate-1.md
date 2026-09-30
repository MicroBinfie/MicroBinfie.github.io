---
layout: page
title: 'Episode 146: NextFlow debate 1'
date: '2025-10-16 00:00:00'
link: https://soundcloud.com/microbinfie/146-nextflow-debate-1
episode: '146'
soundcloud_track: '2188229951'
tags:
- microbinfie
- podcast
description: A staged Nextflow debate on AWS and HPC performance, task overhead, spot instances, modular workflows and difficult debugging.
excerpt: A staged Nextflow debate on AWS and HPC performance, task overhead, spot instances, modular workflows and difficult debugging.
headline: 'Nextflow in 2025: cloud scale, HPC limits and debugging'
guests: []
topics:
- nextflow
- workflow management
- microbial bioinformatics
- cloud computing
- hpc
- task granularity
- resource monitoring
- spot instances
- debugging
- reproducibility
faq:
- q: Does Nextflow automatically make a bioinformatics pipeline faster?
  a: Andrew argues that Nextflow orchestrates work, but performance still depends on the software, parallelisation and resource requests. Asking for many processors or large amounts of memory does not help if the underlying tool cannot use them effectively.
- q: Why can many small Nextflow tasks cause problems on an HPC?
  a: The hosts describe scheduler overhead, large job counts and the supporting files created in task working directories. Lee’s SGE example shows how a ten-second task could incur another one to fifteen seconds before execution, making very small tasks inefficient.
- q: What are the risks of running Nextflow on cloud spot instances?
  a: Andrew describes discounted capacity that can be reclaimed, interrupting a job. He warns that repeated retries of large, memory-intensive jobs can outweigh the saving, while the wider discussion highlights the risk of expensive cloud mistakes.
- q: What is the hosts’ main criticism of Nextflow debugging?
  a: Lee says error output can identify a failing module without clearly explaining where the problem lies. The hosts connect this difficulty to the same abstraction that simplifies containers, dependencies, outputs and remote execution, and discuss whether AI assistance could help.
---

*Nextflow in 2025: cloud scale, HPC limits and debugging*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan begin a debate about Nextflow’s strengths and frustrations in 2025. Andrew argues for it while Lee deliberately takes the critical position, covering cloud and HPC performance, modular workflows, resource management and debugging. The hosts stress that their debate positions do not necessarily reflect their personal opinions.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 146: NextFlow debate 1" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2188229951&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 146: NextFlow debate 1 on SoundCloud](https://soundcloud.com/microbinfie/146-nextflow-debate-1)

## In this episode

### A debate, not a verdict

The hosts set up an intentionally opinionated discussion rather than a shared verdict on Nextflow. Lee volunteers to argue the cons, Andrew takes the pro position, and the third host balances the arguments. Lee explicitly says that he likes aspects of Nextflow even while presenting criticisms. This episode is the first part of a discussion that will continue in further rounds.

Andrew describes extensive use of Nextflow for cancer bioinformatics and microbiome analysis. He runs it on AWS through Seqera Tower, also referred to in the conversation as Nextflow Tower, and often starts with an nf-core pipeline. For more bespoke work, he describes using AI to create a tool that manipulates indexes in a FASTQ file, then turn it into a Nextflow pipeline and Docker container.

### Performance depends on task design

Andrew distinguishes Nextflow’s orchestration from the performance of the software it runs. Parallelisation, processor requests and memory requests still need to match the underlying tools. Nextflow helps connect processes and handle data, including data in cloud object storage, but it cannot make poorly designed software efficient.

Lee uses genome assembly followed by annotation to show how a workflow can be divided into increasingly small tasks. That flexibility can also create more jobs than an HPC scheduler can comfortably manage. He gives an illustrative contrast between a scheduler tracking 10,000 jobs and a workflow accidentally submitting a million. Working directories add another burden: Lee estimates roughly five to ten supporting files per task, making eight million files a possible illustration for a million-task run. These are examples of potential overhead, not reported benchmark results.

### Small jobs, batching and resource reports

One host praises Nextflow’s built-in trace and reporting facilities. For a pipeline run repeatedly, these help reveal resource use and support adjustments to individual processes without building a monitoring system from scratch.

The counterargument is that a separate task for every sample and processing step can be inefficient when each task does very little work. Lee gives an SGE example: a ten-second job might wait another one to fifteen seconds before being picked up, potentially stretching the elapsed time to 25 seconds. The hosts discuss batching small tasks and HPC job arrays as ways of thinking about this overhead. One host says the nf-core specification discourages batching because it becomes harder to identify exactly what failed. The discussion leaves this tension between efficiency and failure tracking unresolved.

### Cloud scale comes with financial risk

Andrew argues that some limitations belong to the infrastructure rather than Nextflow itself. He reports running 3,800 CPUs simultaneously in the cloud and contrasts this with the availability and shared-resource constraints of an HPC system. In his account, object storage avoids the NFS and inode problems being discussed, while Tower can place several small jobs on a node. The hosts also warn that cloud mistakes can cost thousands of dollars in minutes.

Spot instances introduce another trade-off. Andrew describes accepting spare capacity at a discount of around 60–70%, with a 90-second warning if the resources are reclaimed. He considers this useful for small jobs, but warns that repeatedly restarting large, memory-intensive jobs can cost more than the original saving.

### Modular workflows versus difficult debugging

Andrew compares Nextflow modules to Lego blocks: they connect tools, containers, inputs and outputs while expressing which work can run in parallel. He contrasts this with a home-written Bash script, where moving files and keeping dependencies straight can become complicated. Lee also highlights the learning required to understand module inputs, outputs and syntax, potentially including Java or Groovy.

Lee’s main workflow-management criticism is debugging. In his experience, an error may identify the failing module without clearly locating the underlying problem. He objects to relying on AI assistance where the error output should provide a useful explanation. Andrew accepts that remote execution and multiple container layers make diagnosis harder, and suggests integrated AI assistance as a possible improvement.

The balancing view is that Nextflow removes substantial boilerplate for package management, outputs, resuming work and resource handling, but also obscures those mechanisms. That abstraction can make pipelines accessible while making failures harder to understand.

## Highlights

- [00:00:03](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=0:03) — The hosts set up a staged debate, with Lee volunteering to argue the cons.
- [00:02:29](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=2:29) — Andrew describes AWS, Seqera Tower, nf-core pipelines and AI-assisted pipeline creation.
- [00:04:03](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=4:03) — Nextflow’s orchestration is distinguished from software performance and resource efficiency.
- [00:05:16](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=5:16) — Splitting assembly and annotation into smaller tasks can multiply jobs and working files.
- [00:08:21](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=8:21) — Andrew contrasts HPC constraints with cloud scaling, including a 3,800-CPU run.
- [00:09:34](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=9:34) — Built-in tracing and reporting help tune resources, but small-task batching complicates failure tracking.
- [00:11:39](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=11:39) — Lee explains how SGE scheduling delays can dominate a ten-second task.
- [00:12:09](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=12:09) — Spot instances offer discounted capacity but risk interruptions and repeated work.
- [00:13:23](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=13:23) — Andrew compares modular workflow construction with maintaining a Bash script.
- [00:14:20](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=14:20) — Lee argues that unclear errors make debugging slow and AI assistance an unsatisfactory substitute.
- [00:16:36](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=16:36) — The hosts weigh reduced workflow boilerplate against the difficulty of understanding hidden mechanisms.

## In their own words

> You can just kind of join it together in Lego blocks, and it makes life a million times easier.
>
> — Andrew Page, [00:04:03](https://soundcloud.com/microbinfie/146-nextflow-debate-1#t=4:03)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Nextflow, nf-core, Seqera Tower (Nextflow Tower), AWS, Docker, Slurm, SGE, Bash, Java, Groovy, Perl.

## Questions this episode answers

### Does Nextflow automatically make a bioinformatics pipeline faster?

Andrew argues that Nextflow orchestrates work, but performance still depends on the software, parallelisation and resource requests. Asking for many processors or large amounts of memory does not help if the underlying tool cannot use them effectively.

### Why can many small Nextflow tasks cause problems on an HPC?

The hosts describe scheduler overhead, large job counts and the supporting files created in task working directories. Lee’s SGE example shows how a ten-second task could incur another one to fifteen seconds before execution, making very small tasks inefficient.

### What are the risks of running Nextflow on cloud spot instances?

Andrew describes discounted capacity that can be reclaimed, interrupting a job. He warns that repeated retries of large, memory-intensive jobs can outweigh the saving, while the wider discussion highlights the risk of expensive cloud mistakes.

### What is the hosts’ main criticism of Nextflow debugging?

Lee says error output can identify a failing module without clearly explaining where the problem lies. The hosts connect this difficulty to the same abstraction that simplifies containers, dependencies, outputs and remote execution, and discuss whether AI assistance could help.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Andrew, Nabil, and Lee debate about NextFlow!
