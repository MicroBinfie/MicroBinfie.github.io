---
layout: page
title: 'Episode 147: NextFlow debate 2'
date: '2025-10-30 00:00:00'
link: https://soundcloud.com/microbinfie/147-nextflow-debate-2
episode: '147'
soundcloud_track: '2189256127'
tags:
- microbinfie
- podcast
description: Can Nextflow pipelines move easily between clouds? The hosts debate containers, debugging, restart limits and the learning curve.
excerpt: Can Nextflow pipelines move easily between clouds? The hosts debate containers, debugging, restart limits and the learning curve.
headline: 'Nextflow debate: portability, debugging and robustness'
guests: []
topics:
- bioinformatics workflows
- workflow portability
- containerisation
- cloud computing
- pipeline debugging
- fault tolerance
- documentation
- ai-assisted coding
faq:
- q: Can the same Nextflow pipeline run on Google and AWS?
  a: Andrew reports building a pipeline on a Google virtual machine, moving it to Google Batch and later running it on AWS without changing the pipeline code. The hosts credit containers with much of this portability, while noting that environment configuration still needs attention.
- q: Why can debugging a containerised Nextflow pipeline be difficult?
  a: Lee describes cases where a failing script is inside a container rather than the pipeline repository. Investigating it requires locating the executable in that environment, and a fix to the packaged script requires a new container.
- q: Does Nextflow always recover successfully after an interruption?
  a: Andrew says restart support is useful but not infallible. He describes problems involving repeated spot-instance interruptions, memory or disk shortages, and unrealistic resource requests.
- q: Is Nextflow documentation enough to make pipeline modification straightforward?
  a: The hosts praise the documentation and videos but say finding and internalising the relevant material can take substantial time. Even small modifications may require understanding the workflow’s conceptual model and its Groovy-based syntax.
---

*Nextflow debate: portability, debugging and robustness*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan continue their debate about Nextflow, focusing on portability, robustness and documentation. Andrew describes running the same pipeline across Google and AWS, while Lee takes the devil’s advocate role to examine debugging and configuration difficulties. The discussion distinguishes the experience of running an existing pipeline from the work required to understand, modify and maintain one.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 147: NextFlow debate 2" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2189256127&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 147: NextFlow debate 2 on SoundCloud](https://soundcloud.com/microbinfie/147-nextflow-debate-2)

## In this episode

### Portability tested across two clouds

Andrew Page describes a practical test of Nextflow’s portability: he built a pipeline on a Google virtual machine, moved execution to Google Batch, then ran the same pipeline on AWS a few months later without changing its code. He reports using three execution arrangements across two clouds successfully. For him, this demonstrates that portability is more than a theoretical selling point.

The hosts credit much of this success to containers. Packaging the tools supplies much of the execution environment, while Nextflow links the steps together. Another host argues that this abstraction reduces the need to manage installations separately on different hosts, although understanding the container environment remains important.

### Containers make debugging less direct

Lee agrees that running the same pipeline in different places is valuable, but describes the difficulty of tracing a failure through several layers. A Nextflow process may call a script that is absent from the pipeline’s GitHub repository because it lives inside a Docker container or a Conda package. Investigating it can mean downloading the container, entering its environment and locating the executable in its filesystem.

If the fix belongs inside the container, Lee says a new container must be released. If understanding the script instead reveals a fix in the Nextflow code, the developer is back to debugging that code and interpreting difficult error messages. His criticism is about the visibility and accessibility of dependencies, rather than whether portability works.

### Cloud logging and configuration have costs

Andrew recalls an AWS Batch run that produced millions of lines of logging output. Those messages went to cloud logging, contributing to a bill of roughly £1,000. He warns that logs which might otherwise be written to a disposable filesystem on a virtual machine can become chargeable cloud operations. Moving execution successfully does not remove the need to understand the services around it.

Lee raises a separate configuration problem: portable pipeline code still needs a description of the execution environment. He finds it difficult to decide what belongs in the pipeline repository and what should remain elsewhere. He also questions whether publishing infrastructure details, such as HPC node or CPU counts, could expose sensitive information.

### Restart support has limits

Andrew values Nextflow’s ability to restart after an error rather than repeat everything from the beginning. However, he says checkpointing and restart behaviour do not always work as hoped. Repeated interruptions to spot instances, insufficient memory and exhausted disk space can still cause a workflow to fail.

Some problems can be corrected incrementally, but resource requests themselves can go wrong. His example is a suspected bug requesting something like 100 terabytes of RAM, beyond what was available in AWS. The broader point is that robustness still depends on supplying suitable information up front; the workflow system cannot compensate for every incorrect request or environmental constraint.

### Good documentation, difficult concepts

Andrew rates the documentation favourably, particularly the nf-core material, and Lee praises the short explanatory videos. Taking the opposing side, Lee argues that the volume of material can be overwhelming. Learning modules and configuration takes time, and even an intermediate developer may struggle to locate a specific detail, such as how to place a variable in a shell block.

Andrew distinguishes users running established pipelines through graphical interfaces from developers who continually modify and extend workflows. Another host responds that modularity invites modification: adding an output, changing a flag or collecting results into a CSV still requires understanding how the pipeline works. Reference documentation and worked examples do not necessarily explain the conceptual model of how its parts interact, and unfamiliarity with Groovy adds difficulty.

AI assistance is treated cautiously. Andrew worries that reliance on ChatGPT and Copilot can leave practitioners unable to understand or rebuild their code. He also says AI can help with documentation, but only when given the right information.

## Highlights

- [00:01:32](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=1:32) — Portability between a laptop, HPC and the cloud opens the debate.
- [00:02:00](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=2:00) — Andrew reports running the same Nextflow pipeline across Google and AWS.
- [00:03:11](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=3:11) — Lee weighs portable execution against debugging scripts buried in containers.
- [00:05:13](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=5:13) — Containers abstract away host installation differences but introduce their own environment.
- [00:06:16](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=6:16) — Millions of log lines from an AWS Batch run lead to a roughly £1,000 bill.
- [00:07:01](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=7:01) — Configuration files raise questions about repository contents and sensitive infrastructure details.
- [00:08:24](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=8:24) — Andrew discusses AI-dependent coding habits before assessing restart support and failure cases.
- [00:10:18](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=10:18) — Lee praises the documentation but argues that its volume creates a steep learning curve.
- [00:11:41](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=11:41) — Andrew distinguishes pipeline end users from developers working on continual modifications.
- [00:12:31](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=12:31) — Modifying modular pipelines requires a conceptual understanding that reference material may not supply.

## In their own words

> So I've tried it in three different formats on two different clouds, and it just worked.
>
> — Andrew Page, [00:02:00](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=2:00)

> So I think the portability is fine, but it's obfuscated code.
>
> — Lee Katz, [00:03:11](https://soundcloud.com/microbinfie/147-nextflow-debate-2#t=3:11)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Nextflow, nf-core, Docker, Conda, Google Batch, AWS Batch, GitHub, Groovy, ChatGPT, Copilot.

## Questions this episode answers

### Can the same Nextflow pipeline run on Google and AWS?

Andrew reports building a pipeline on a Google virtual machine, moving it to Google Batch and later running it on AWS without changing the pipeline code. The hosts credit containers with much of this portability, while noting that environment configuration still needs attention.

### Why can debugging a containerised Nextflow pipeline be difficult?

Lee describes cases where a failing script is inside a container rather than the pipeline repository. Investigating it requires locating the executable in that environment, and a fix to the packaged script requires a new container.

### Does Nextflow always recover successfully after an interruption?

Andrew says restart support is useful but not infallible. He describes problems involving repeated spot-instance interruptions, memory or disk shortages, and unrealistic resource requests.

### Is Nextflow documentation enough to make pipeline modification straightforward?

The hosts praise the documentation and videos but say finding and internalising the relevant material can take substantial time. Even small modifications may require understanding the workflow’s conceptual model and its Groovy-based syntax.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Part two of debating NextFlow
