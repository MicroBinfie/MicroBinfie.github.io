---
layout: page
title: 'Episode 89: What do we do with WDL?'
date: '2022-09-15 00:00:00'
link: https://soundcloud.com/microbinfie/what-do-we-do-with-wdl
episode: '89'
soundcloud_track: '1284129610'
tags:
- microbinfie
- podcast
description: Joel and Danny discuss WDL, portable bioinformatics pipelines, and how containers and workflow languages support public health laboratories.
excerpt: Joel and Danny discuss WDL, portable bioinformatics pipelines, and how containers and workflow languages support public health laboratories.
headline: WDL and portable workflows for public health bioinformatics
guests:
- Joel
- Danny
topics:
- workflow languages
- microbial bioinformatics
- public health
- pipeline portability
- containerisation
- reproducibility
- cloud computing
- quality management
- viral genomics
faq:
- q: What does WDL do in a bioinformatics pipeline?
  a: WDL describes how computational tasks fit together, including how files pass between tools and where conditional or branching steps occur. Danny presents it as a way to connect already-containerised tools into portable workflows.
- q: How does WDL differ from Nextflow and Snakemake?
  a: The episode emphasises that WDL is a language specification separate from its execution engines, whereas Nextflow and Snakemake tie their languages more closely to their implementations. Danny also describes WDL as more restrictive for developers, with those restrictions helping workflows run across environments.
- q: Can the same WDL workflow run locally and in the cloud?
  a: That is the portability goal discussed in the episode, but it is conditional. The destination needs a suitable implementation, support for the containers, and enough memory, CPU and disk resources for the workflow.
- q: Why are containers and workflow managers useful to public health laboratories?
  a: Joel says they help make analysis standardised, reproducible, portable, scalable and easier to use. The Lyve-SET example shows how packaging software can reduce repeated installation work and the system-administration burden on laboratories.
- q: Why did the guests choose WDL?
  a: Danny points to DNAnexus adopting WDL as evidence that his group's viral pipelines could move between platforms. Joel emphasises Terra's suitability for supporting public health and the influence of collaborations with Danny and the Broad Institute.
---

*WDL and portable workflows for public health bioinformatics*

Guests Joel and Danny join Lee Katz, Andrew Page and Nabil-Fareed Alikhan to discuss the Workflow Description Language (WDL) and its use in public health bioinformatics. They explain how WDL connects containerised tools, why a language specification differs from an execution engine, and what portability requires. Experiences with Lyve-SET, viral analysis pipelines and public health laboratories show how workflow languages can reduce installation work while supporting reproducible, scalable analysis.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 89: What do we do with WDL?" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1284129610&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 89: What do we do with WDL? on SoundCloud](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl)

## In this episode

### Connecting containerised tools

Danny introduces WDL as a way to describe bioinformatics pipelines so they can run in different computing environments. In his explanation, the starting point is already-containerised tools. WDL describes how outputs become inputs, what file conversions or preparation steps are needed, and where a workflow branches or brings results together.

Lee tests the idea with a hypothetical workflow mapping reads to the human genome: could the same description run on a Raspberry Pi or an HPC system? Danny qualifies the portability claim. The destination must support the containers and provide the memory, CPU and disk resources required by the individual steps.

### A language specification, not an execution engine

WDL is not itself a program that executes a pipeline. Danny contrasts it with Nextflow and Snakemake, where the language and execution engine are more closely tied together. Like Common Workflow Language (CWL), WDL separates its specification from the implementations that interpret it.

The discussion identifies the Broad Institute, DNAnexus and CZI as active participants with investments in implementations. Cromwell is named as the underlying engine for Terra. Danny also cautions that the formal language documentation is primarily a reference for people maintaining the specification or implementing engines, rather than an introduction for someone beginning to write workflows.

### Public health's route from virtual machines to workflows

Joel describes five aims for public health bioinformatics: standardisation, reproducibility, portability, scalability and ease of use. When he started in public health, BioNumerics through PulseNet provided standardised analysis at state level, but work on other pathogens or alternative enteric pipelines often depended on custom scripts and local computing resources.

Lyve-SET illustrates the installation problem. To help other laboratories use it, the Colorado team created a Google Cloud virtual machine, had Lee install Lyve-SET, and distributed an image. This reduced repeated installation work but still required command-line expertise and did not fully solve scalability or usability.

Joel credits the StaphB Docker repository with making containerised tools available for workflow managers to connect. Removing system-administration work meant more time for scientific questions.

### Versioning and the StaphB community

Lee accepts that Lyve-SET was difficult to install, then recalls jokes about producing version two. The exchange becomes a discussion of quality management: even small fixes need identifiable versions, and patch numbers can accumulate as bugs are found. Lee compares the experience with repeatedly labelling a manuscript final.

Joel also revisits StaphB's origins. State-level public health bioinformaticians were asking similar questions through a shared contact without necessarily knowing one another. They were encouraged to talk directly. Joel recalls virtual conversations followed by an in-person gathering at an APHL meeting in 2017, helping connect people facing similar state laboratory challenges.

### Why Danny's viral group adopted WDL

Danny distinguishes his infectious disease work at the Broad Institute from the separate groups developing WDL and Terra. His priority was giving collaborators computational capabilities equivalent to those available within his own group, not choosing a tool because it came from the same institution.

His group had worked with DNAnexus since around 2014 to expand computing access for partners in West Africa. Initially, deploying pipelines required its proprietary workflow language and substantial hands-on help. Around 2016–2017, DNAnexus's adoption of WDL changed his assessment: there was now evidence that the language could run beyond a single organisation's platform. WDL became the primary route for deploying their viral pipelines on DNAnexus, later Terra, and also from the command line.

### Portability through limits and practical partnerships

Danny explains that WDL gives developers less freedom than a system such as Snakemake, which allows Python in input rules. Those restrictions can support portability: a workflow should not depend on a particular shared directory or file path. Implementations can then manage files differently on a laptop or in cloud storage. His group used validators and automated tests on GitHub to check compatibility across implementations, occasionally finding edge cases.

For Joel, the choice was driven by the environment available to support public health, especially Terra, and by collaborators. He describes work with the Massachusetts Department of Health, Danny and the Broad Institute. Their interactions during summer 2019 through summer 2020 helped show how these approaches could be applied in public health laboratories.

## Highlights

- [00:02:36](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=2:36) — Introducing WDL and its pronunciation
- [00:03:29](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=3:29) — How WDL connects containerised tools into computational pipelines
- [00:04:43](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=4:43) — Testing portability with a hypothetical human read-mapping workflow
- [00:06:05](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=6:05) — Separating the WDL specification from execution engines
- [00:07:31](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=7:31) — Organisations participating in the WDL consortium
- [00:10:20](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=10:20) — Public health's need for standardised, reproducible and usable pipelines
- [00:15:07](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=15:07) — Lyve-SET version numbers and quality-management requirements
- [00:16:22](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=16:22) — StaphB's origins in connecting state public health bioinformaticians
- [00:18:13](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=18:13) — Danny's route to WDL for portable viral analysis pipelines
- [00:21:34](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=21:34) — Parser implementations and automated compatibility testing
- [00:22:52](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=22:52) — Why restrictions on workflow developers can improve portability
- [00:24:09](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=24:09) — Joel's choice of WDL through Terra and public health partnerships

## In their own words

> But the problem it's trying to solve is inherently one of portability.
>
> — Danny, [00:09:09](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=9:09)

> I'll just say, I'm going to say you're right. It's hard to install.
>
> — Lee Katz, [00:14:08](https://soundcloud.com/microbinfie/what-do-we-do-with-wdl#t=14:08)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Joel** (guest, Theiagen Genomics)
- **Danny** (guest, Broad Institute of MIT and Harvard)

## Tools and resources mentioned

WDL, Common Workflow Language (CWL), Nextflow, Snakemake, Docker, Cromwell, Terra, DNAnexus, Lyve-SET, StaphB Docker repository, BioNumerics, Google Cloud, GitHub, BioPerl.

## Questions this episode answers

### What does WDL do in a bioinformatics pipeline?

WDL describes how computational tasks fit together, including how files pass between tools and where conditional or branching steps occur. Danny presents it as a way to connect already-containerised tools into portable workflows.

### How does WDL differ from Nextflow and Snakemake?

The episode emphasises that WDL is a language specification separate from its execution engines, whereas Nextflow and Snakemake tie their languages more closely to their implementations. Danny also describes WDL as more restrictive for developers, with those restrictions helping workflows run across environments.

### Can the same WDL workflow run locally and in the cloud?

That is the portability goal discussed in the episode, but it is conditional. The destination needs a suitable implementation, support for the containers, and enough memory, CPU and disk resources for the workflow.

### Why are containers and workflow managers useful to public health laboratories?

Joel says they help make analysis standardised, reproducible, portable, scalable and easier to use. The Lyve-SET example shows how packaging software can reduce repeated installation work and the system-administration burden on laboratories.

### Why did the guests choose WDL?

Danny points to DNAnexus adopting WDL as evidence that his group's viral pipelines could move between platforms. Joel emphasises Terra's suitability for supporting public health and the influence of collaborations with Danny and the Broad Institute.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Today on the @microbinfie podcast, we talk about WDL with @sevinsky and @DannyJPark. We learn
what widdle means to Andrew and his kids. Joel takes a shot at Lyve-SET and you'll never guess
what happens next.

In the MicroBinfie podcast, we discuss the workflow description language (WDL) commonly used to
describe bioinformatics pipelines in a portable and cross-environmental way. The starting point
is the presumption that tools are already containerized, and WDL helps to bind them together.
The guests highlighted that this standardizes bioinformatics in the field, making it more
reproducible and scalable. It also helps remove the need for excessive CIS admin work, enabling
researchers to spend more time on scientific questions. Despite having many workflow languages
available, WDL is unique in its formal specification and its orthogonality to the common
implementations that are used in executing those things.

In the second part of the podcast discussion, guests Joel and Danny talked about workflow
languages and public health bioinformatics. They highlighted the challenge of version control
to quality management and its effects on the field of bioinformatics. They spoke about the
origins of the community, StaphB, which comprises state-level public health bioinformaticians.
The community discusses various challenges and contributes to creating links between academia
and state public health departments.

WDL is a workflow language used for bioinformatics work that the hosts use. Danny shared his
story of how they came to use Whittle and how they realized it was the perfect language for
portability of pipelines. On the other hand, Joel talked about how they chose WDL for its
applicability to public health and the support it received from its creators, particularly the
Broad Institute. They both agreed that the choice of workflow language was driven by the
environment they could work in and which language was best suited to their needs.

In conclusion, the discussion focused on the vital role of workflow languages such as WDL in
bridging the gap between bioinformatics and public health. The choice of workflow language was
critical and would depend heavily on the environment in which the language was used. Finally,
they expressed their support for WDL and how it had helped them streamline their bioinformatics
workflows.
