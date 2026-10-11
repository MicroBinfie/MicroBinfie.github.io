---
layout: page
title: 'Episode 57: StaPH-B - Docker containers for Public Health bioinformatics Part 1'
date: '2021-05-07 00:00:00'
link: https://soundcloud.com/microbinfie/staph-b-part-1
episode: '57'
soundcloud_track: '1032644443'
tags:
- microbinfie
- podcast
description: Curtis Kapsak and Kevin Libuit explain StaPH-B Docker containers, version control, Pangolin automation and database choices for public health labs.
excerpt: Curtis Kapsak and Kevin Libuit explain StaPH-B Docker containers, version control, Pangolin automation and database choices for public health labs.
headline: StaPH-B Docker containers for public health bioinformatics
guests:
- Curtis Kapsak
- Kevin Libuit
topics:
- public health bioinformatics
- staph-b
- software containers
- reproducibility
- software validation
- version pinning
- database management
- sars-cov-2
- community contributions
faq:
- q: What does StaPH-B stand for?
  a: StaPH-B stands for the State Public Health Bioinformatics Workgroup. It began as a forum for scientists to address shared barriers to implementing bioinformatics in public health laboratories.
- q: Are StaPH-B containers individual tools or complete pipelines?
  a: Both are represented. Curtis describes images containing SPAdes and its dependencies, alongside larger images packaging complete pipeline environments such as Shovill.
- q: Does a version-pinned container make a pipeline validated?
  a: No validation guarantee is claimed in the episode. Pinning helps preserve the software environment, but laboratories still need to assess and validate their pipelines, including changes introduced by upgrades.
- q: Why are Kraken databases kept outside newer StaPH-B images?
  a: Bundling a mini Kraken database made some images difficult for users to download. Newer images omit the database and provide instructions for using a separate database, balancing image size with usability.
- q: How can someone request or contribute a StaPH-B container?
  a: Anyone can open a GitHub issue, submit a pull request with a Dockerfile or contact a maintainer. Curtis also points listeners to the project’s contribution guide.
---

*StaPH-B Docker containers for public health bioinformatics*

Lee Katz and Andrew Page speak with Curtis Kapsak and Kevin Libuit about the State Public Health Bioinformatics Workgroup (StaPH-B) and its Docker containers. They discuss how shared software environments can support reproducible analysis across laboratories with separate computing systems. The conversation covers version pinning, validation, Pangolin automation, database packaging and the limits of keeping software static.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 57: StaPH-B - Docker containers for Public Health bioinformatics Part 1" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1032644443&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 57: StaPH-B - Docker containers for Public Health bioinformatics Part 1 on SoundCloud](https://soundcloud.com/microbinfie/staph-b-part-1)

## In this episode

### A shared forum for separate laboratories

StaPH-B began in 2016 with four state public health bioinformatics scientists seeking guidance from one another. Kevin explains that US state laboratories faced infrastructure, procurement, training and implementation challenges that differed from those of federal agencies. By the time of this conversation, the group was approaching 200 members, with state, local, territorial, federal, academic and industry participation.

Its early focus reflected the use of sequencing for enteric pathogens. That broadened to healthcare-associated infections and antimicrobial resistance in 2018–2019, followed by viral work and SARS-CoV-2. The guests also explain their contracting roles: public agencies can commission specialised work when their existing workforce lacks the capacity to cover it.

### What the containers contain

Curtis describes a container as a standard software unit that packages code and dependencies so an application can run reliably across computing environments. StaPH-B develops Dockerfiles with compatibility in mind for systems such as Singularity and Podman. The collection ranges from individual tools, such as SPAdes and its dependencies, to complete pipeline environments such as Shovill.

Installation methods vary. Some images use Conda, but Curtis often avoids it because it can increase image size, instead using options such as Ubuntu’s package manager. His usual base is Ubuntu 16.04 LTS, moving to Ubuntu 18 or 20 when newer tools require it. Andrew describes his preference for Debian testing, contrasting it with Debian stable and unstable. The discussion treats base-image choice as a practical preference rather than a single prescribed answer.

### Reproducibility and validation are separate tasks

The repository’s first commit was in September 2018, with Curtis and Kelsey Florek helping establish the container work. Kevin recalls the progression from manually resolving dependencies to package managers such as Conda and pip. Containers addressed another problem: software working on one laboratory’s machine did not mean it would work on another’s separate infrastructure.

Version pinning is central to StaPH-B’s approach; Curtis gives BLAST 2.9 as an example. However, he is unsure whether laboratories have yet validated the images within their own pipelines. A new release is not automatically a reason to upgrade: Kevin argues that the benefit must justify the quality assessment and validation involved. Minor efficiency or reporting changes may not warrant adoption, whereas rapidly changing SARS-CoV-2 information can make updates more urgent.

### Controlled builds and Pangolin automation

Most builds were still manually controlled at the time of recording. Contributors submit Dockerfiles through pull requests; maintainers review and merge them, then arrange builds on Docker Hub. Curtis explains why rebuilding images automatically after every commit would conflict with the aim of preserving static environments. Image names identify the namespace and tool, with a tag specifying the tool version.

Pangolin is an exception because its frequent updates make manual maintenance time-consuming. Curtis describes a GitHub Actions workflow triggered by new Pangolin versions or new pangoLEARN model versions. It creates a Dockerfile, builds the image and publishes it to Docker Hub. He says an updated image can be available within about 15 minutes.

### Database size and the limits of static images

A fixed container does not prevent every failure. Kevin reports R packages used in an R Markdown reporting workflow that check against remote versions and can fail when versions no longer align. He also describes an NCBI tool with a calendar-based expiry. Both behaviours can force maintainers to rebuild supposedly static environments.

Database packaging presents a different trade-off. Kraken databases can range from roughly 8 GB to 100 GB. StaPH-B initially included a mini Kraken database, but some users struggled to download the resulting images. Newer Kraken images therefore omit the database and provide instructions for using a separate one. Smaller, relatively static resources can remain bundled: Curtis gives the SerotypeFinder database for E. coli serotyping as an example.

### Contributing and citing the work

Contributions are open to anyone, not just StaPH-B members. Listeners can request a container through a GitHub issue, submit a pull request or contact a maintainer. Curtis points to the contribution guide and acknowledges the wider group maintaining the collection.

There was no paper available at the time, although one was being worked on. The suggested citation route is the GitHub repository alongside the original developers of the packaged tools. StaPH-B documents original authors, source repositories and software licences rather than treating container packaging as a replacement for crediting tool developers.

## Highlights

- [00:05:10](https://soundcloud.com/microbinfie/staph-b-part-1#t=5:10) — StaPH-B’s origins as a forum for state public health bioinformatics scientists
- [00:08:48](https://soundcloud.com/microbinfie/staph-b-part-1#t=8:48) — The shift from enteric pathogens towards healthcare-associated infections, resistance and viruses
- [00:10:50](https://soundcloud.com/microbinfie/staph-b-part-1#t=10:50) — What containers package and why they help software run across environments
- [00:12:22](https://soundcloud.com/microbinfie/staph-b-part-1#t=12:22) — Container granularity: individual tools such as SPAdes versus pipelines such as Shovill
- [00:13:13](https://soundcloud.com/microbinfie/staph-b-part-1#t=13:13) — Manual builds, installation control and pinning software versions
- [00:18:10](https://soundcloud.com/microbinfie/staph-b-part-1#t=18:10) — Dependency problems and the need for interoperability between separate laboratories
- [00:22:37](https://soundcloud.com/microbinfie/staph-b-part-1#t=22:37) — Deciding whether a version update justifies adoption and renewed validation
- [00:24:28](https://soundcloud.com/microbinfie/staph-b-part-1#t=24:28) — Pull-request review and controlled Docker Hub builds
- [00:26:47](https://soundcloud.com/microbinfie/staph-b-part-1#t=26:47) — Automating Pangolin and pangoLEARN image updates with GitHub Actions
- [00:28:32](https://soundcloud.com/microbinfie/staph-b-part-1#t=28:32) — Open contributions, container requests and recognition of maintainers
- [00:31:02](https://soundcloud.com/microbinfie/staph-b-part-1#t=31:02) — Why remote version checks and expiry dates can break static containers
- [00:32:33](https://soundcloud.com/microbinfie/staph-b-part-1#t=32:33) — Handling databases that may be too large to package inside an image

## In their own words

> So I like to think of a container as an extremely lightweight virtual machine.
>
> — Curtis Kapsak, [00:10:50](https://soundcloud.com/microbinfie/staph-b-part-1#t=10:50)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Curtis Kapsak** (guest, Theiagen Genomics)
- **Kevin Libuit** (guest, Theiagen Genomics)

## Tools and resources mentioned

Docker, Docker Hub, Singularity, Podman, SPAdes, Shovill, BLAST, Conda, pip, FastQC, Ubuntu, Debian, GitHub Actions, Pangolin, pangoLEARN, R Markdown, Kraken, mini Kraken database, SerotypeFinder.

## Questions this episode answers

### What does StaPH-B stand for?

StaPH-B stands for the State Public Health Bioinformatics Workgroup. It began as a forum for scientists to address shared barriers to implementing bioinformatics in public health laboratories.

### Are StaPH-B containers individual tools or complete pipelines?

Both are represented. Curtis describes images containing SPAdes and its dependencies, alongside larger images packaging complete pipeline environments such as Shovill.

### Does a version-pinned container make a pipeline validated?

No validation guarantee is claimed in the episode. Pinning helps preserve the software environment, but laboratories still need to assess and validate their pipelines, including changes introduced by upgrades.

### Why are Kraken databases kept outside newer StaPH-B images?

Bundling a mini Kraken database made some images difficult for users to download. Newer images omit the database and provide instructions for using a separate database, balancing image size with usability.

### How can someone request or contribute a StaPH-B container?

Anyone can open a GitHub issue, submit a pull request with a Dockerfile or contact a maintainer. Curtis also points listeners to the project’s contribution guide.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

The crew talks to Curtis Kapsak and Kevin Libuit about the StaPH-B
containers.  What a valuable resource!  Some URLS:  * StaPH-B docker-
builds code repository: https://github.com/StaPH-B/docker-builds *
StaPH-B DockerHub container repositories:
https://hub.docker.com/u/staphb * Guide for contributing:
https://staph-b.github.io/docker-builds/contribute/
