---
layout: page
title: 'Episode 79: StaPH-B: Stable containers for public health bioinformatics'
date: '2022-04-14 00:00:00'
link: https://soundcloud.com/microbinfie/staph-b-stable-containers
episode: '79'
soundcloud_track: '1232844328'
tags:
- microbinfie
- podcast
description: Erin Young and Kelsey Florek explain StaPH-B containers, workflow validation and simpler ways to run public health bioinformatics.
excerpt: Erin Young and Kelsey Florek explain StaPH-B containers, workflow validation and simpler ways to run public health bioinformatics.
headline: StaPH-B containers for stable public health bioinformatics
guests:
- Erin Young
- Kelsey Florek
topics:
- public health bioinformatics
- software containers
- workflow validation
- software provenance
- dependency management
- bioinformatics training
- workflow interfaces
- sars-cov-2
faq:
- q: What is the StaPH-B Docker repository for?
  a: It provides shared containers for tools used by public health laboratories. Laboratories can reuse packaged environments instead of independently installing dependencies and resolving software conflicts.
- q: How does the StaPH-B Toolkit differ from running Docker directly?
  a: The toolkit is a Python-based interface that simplifies access to containers and workflows. It reduces the need for users to handle Docker commands, mounts and file-system details themselves.
- q: Why use an image hash rather than a container tag?
  a: Kelsey recommends using the image hash so laboratories know exactly which image they retrieve each time. This supports the discussion's emphasis on stable environments for validated public health workflows.
- q: Can people outside StaPH-B contribute containers?
  a: Yes. Erin describes forking the repository, following its tool-and-version layout, supplying a working Dockerfile and a way to test it, and submitting a pull request for checks.
---

*StaPH-B containers for stable public health bioinformatics*

Erin Young and Kelsey Florek join Lee Katz and Nabil-Fareed Alikhan to discuss the StaPH-B Docker repository and toolkit. They explain how shared containers reduce installation work across public health laboratories, why stable software environments matter for validation, and how simpler interfaces help laboratories concentrate on biological questions.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 79: StaPH-B: Stable containers for public health bioinformatics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1232844328&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 79: StaPH-B: Stable containers for public health bioinformatics on SoundCloud](https://soundcloud.com/microbinfie/staph-b-stable-containers)

## In this episode

### Containers as controlled environments

Erin introduces containers through an experimental analogy. Using the software already available in a computing environment resembles citizen science; a conda environment offers more control, like a laboratory bench with pipettes and fume hoods. A container takes that control further, like an experiment on a space shuttle. Everything needed should be inside it, working together and capable of being optimised together.

The practical benefit is shared installation work. Rather than 50 laboratories independently resolving dependencies, a few contributors can package a tool for everyone. Erin gives installing Perl libraries as an example of something laboratories then do not each need to learn.

### A shared repository for public health laboratories

Kelsey describes the repository's origins in efforts to run workflows on a university high-performance computing cluster. Containers developed in Wisconsin could also serve colleagues in Colorado and Virginia. Collecting them in one place would spare other laboratories from repeating dependency installation and resolving conflicting Python versions. SPAdes provides a straightforward example: install Docker and use the existing container rather than assembling the tool's environment yourself.

Erin highlights the pangolin containers used for SARS-CoV-2 lineage determination, praising their ease of use and prompt updates. Kelsey also mentions containerising a SARS coronavirus dataset repository with a substantial dependency list.

Contributions are open beyond the StaPH-B community. Contributors fork the repository, organise files by tool and version, provide a Dockerfile and README, and include a way to test the container. Accepted contributions reach Docker Hub and Quay.

### Stability, provenance and validation

A host asks why StaPH-B should maintain its own collection when BioContainers and Bioconda already provide related resources. Kelsey's answer centres on state public health laboratories and their need to validate workflows, pipelines and tools. A host also reports finding StaPH-B containers more dependable than some automatically assembled alternatives; this is a user experience, not a comparative benchmark.

Kelsey recommends retrieving an image by its hash rather than relying only on a tag, so laboratories know exactly which image they are obtaining. Other approaches discussed include secured or locked images and multi-stage builds incorporating test datasets and validation checks.

The pandemic delayed plans for a publication. Maintaining the containers remained the priority, with broader continuous integration and continuous testing identified as work to advance before publishing.

### What the StaPH-B Toolkit simplifies

The StaPH-B Toolkit is a Python-based utility originally developed to support training. Running a container directly requires knowledge of images, Linux mounts and file systems—details that can distract from analysing sequence data. The toolkit provides a help menu and a simpler interface to the Docker images, then extends that approach to workflows, including Nextflow workflows.

Kelsey describes being able to install the toolkit with pip and access a collection of resources. It is useful beyond introductory training: Kelsey sometimes uses it for a one-off samtools task simply to avoid constructing the Docker command. Erin adds that the toolkit curates workflows with a public health focus, helping users navigate an otherwise overwhelming choice.

### Workflow packaging and long-term use

A host compares the toolkit with earlier package-management approaches such as Homebrew and BrewSci, and with the module system in nf-core. The question is whether container interfaces represent another turn in a recurring cycle: packaging software, then building a friendlier layer over the package.

Kelsey is cautious about predicting the toolkit's lifespan, but says continued downloads and requests to retain older software demonstrate its usefulness. Erin notes a maintenance challenge when a workflow exists both independently and inside the toolkit: the two versions can drift out of sync. A host also argues that containers become particularly valuable when moving workflows between laptops and computing clusters.

### Web interfaces without abandoning the command line

Terra and Nextflow Tower enter the discussion as ways to make workflows accessible to laboratories with limited resources or computing environments. Erin argues that making workflows easier for non-bioinformaticians to use improves their prospects for long-term survival, whether they are written in Snakemake or Nextflow.

Kelsey sees room for both web applications and command-line work. A cloud-based web tool can suit a laboratory that lacks local capacity, while laboratories developing genomic analysis expertise still need flexibility when handling many files, different file systems and networked resources.

The closing goal is not simply easier installation. With more accessible tools and workflows, attention can shift from training people to install tools towards the analytical questions the tools can answer—and the group can spend more time doing biology.

## Highlights

- [00:01:16](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=1:16) — Erin compares ordinary environments, conda and containers using an experimental analogy.
- [00:02:41](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=2:41) — Kelsey explains how the shared public health container repository began.
- [00:05:56](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=5:56) — Pangolin containers support SARS-CoV-2 lineage determination.
- [00:08:15](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=8:15) — How to contribute a Dockerfile, documentation and tests.
- [00:09:36](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=9:36) — Public health validation needs distinguish StaPH-B's container collection.
- [00:13:08](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=13:08) — Publication plans follow container maintenance and continuous testing priorities.
- [00:14:03](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=14:03) — The Python-based toolkit simplifies container use and incorporates workflows.
- [00:17:28](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=17:28) — Kelsey considers the toolkit's lifespan as web-based workflow access develops.
- [00:21:38](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=21:38) — Erin discusses keeping toolkit workflows and standalone repositories updated.
- [00:24:15](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=24:15) — Web tools can help resource-limited laboratories without replacing command-line flexibility.
- [00:26:44](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=26:44) — Simpler installation leaves more time for analytical questions and biology.

## In their own words

> I think there's always been things quote-unquote threatening the command line and it's stood the test of time.
>
> — Kelsey Florek, [00:24:15](https://soundcloud.com/microbinfie/staph-b-stable-containers#t=24:15)

## Who is talking

- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)
- **Erin Young** (guest, Utah Department of Health)
- **Kelsey Florek** (guest, Wisconsin State Laboratory of Hygiene)

## Tools and resources mentioned

StaPH-B Toolkit, StaPH-B Docker repository, Docker, Docker Hub, Quay, conda, SPAdes, pangolin, samtools, Bioconda, BioContainers, Singularity, Galaxy, Nextflow, Snakemake, nf-core, Terra, Nextflow Tower, Homebrew, BrewSci, Python, pip, Perl, CPAN.

## Questions this episode answers

### What is the StaPH-B Docker repository for?

It provides shared containers for tools used by public health laboratories. Laboratories can reuse packaged environments instead of independently installing dependencies and resolving software conflicts.

### How does the StaPH-B Toolkit differ from running Docker directly?

The toolkit is a Python-based interface that simplifies access to containers and workflows. It reduces the need for users to handle Docker commands, mounts and file-system details themselves.

### Why use an image hash rather than a container tag?

Kelsey recommends using the image hash so laboratories know exactly which image they retrieve each time. This supports the discussion's emphasis on stable environments for validated public health workflows.

### Can people outside StaPH-B contribute containers?

Yes. Erin describes forking the repository, following its tool-and-version layout, supplying a working Dockerfile and a way to test it, and submitting a pull request for checks.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Dr Erin Young from the Utah Department of Health and Dr Kelsey Florek
from the Wisconsin State Laboratory of Hygiene join us to talk about
StaPH-B containers for public health bioinformatics. Its basically how
to make biology easier for everyone!

Github: https://github.com/StaPH-B
