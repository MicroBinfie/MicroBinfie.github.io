---
layout: page
title: 'Episode 92: Avoid dependency hell and get up and running fast'
date: '2022-10-27 00:00:00'
link: https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast
episode: '92'
soundcloud_track: '1284764644'
tags:
- microbinfie
- podcast
description: Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss bioinformatics dependencies, Conda, Mamba and containers for more manageable installations.
excerpt: Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss bioinformatics dependencies, Conda, Mamba and containers for more manageable installations.
headline: Avoiding dependency hell in bioinformatics
guests: []
topics:
- bioinformatics software
- dependency management
- software installation
- virtual environments
- package managers
- containers
- software maintenance
- high-performance computing
faq:
- q: Should I create a separate Conda environment for every project?
  a: Nabil-Fareed recommends doing so, keeping each project's tools and language versions together and leaving the base environment largely untouched. Particularly complicated tools may benefit from their own separate environments.
- q: Why use Mamba instead of Conda?
  a: The hosts describe Mamba as using the same style of package-management commands while solving environments much faster. Nabil-Fareed reports good results with small environments, while Lee raises an unverified concern about shortcuts rather than presenting a demonstrated failure.
- q: When do the hosts use Docker rather than Singularity?
  a: Nabil-Fareed uses Docker for services such as databases and web servers, and for interactive R environments. He prefers Singularity for more complicated software when working across local machines and HPC.
- q: Why can software work for its author but fail for another user?
  a: The episode gives examples involving conflicting dependency versions, missing compilers, shared libraries being overwritten and different processor architectures. Developers may also lack the hardware or operating system needed to reproduce a user's problem.
---

*Avoiding dependency hell in bioinformatics*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan compare painful software-installation experiences with practical ways to manage bioinformatics dependencies. They discuss conflicting library versions, software maintenance and hardware compatibility before turning to per-project Conda environments, Mamba, Docker and Singularity. Their emphasis is on keeping installations separate so researchers can spend less time repairing software and more time using it.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 92: Avoid dependency hell and get up and running fast" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1284764644&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 92: Avoid dependency hell and get up and running fast on SoundCloud](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast)

## In this episode

### Why installations become dependency hell

Andrew recalls a team where one person spent virtually all their time working out how to install software. Instructions could involve editing a particular configuration line, compiling source code and finding dozens of exact dependency versions. Sometimes authors supplied a compiler command without explaining the required libraries or compiler.

Nabil-Fareed explains a diamond dependency: a tool uses two components that require incompatible versions of the same underlying library. The user may have to modify someone else's code before doing any analysis. Circular dependencies and long chains of dependencies create further problems. The hosts connect this fragility with academic software that has not been thoroughly tested for other people's environments.

### Versioning and the cost of maintenance

Lee describes reviewing software whose dependencies required different Biopython versions. An installation that worked on its developers' computer was difficult for a new reviewer to reproduce. He argues that minor-version updates should not break existing code, while small patches and documentation changes belong in the patch number. Kraken's executable names, changed to include a two, provide his example of making releases distinguishable.

Andrew's experience with Roary illustrates the maintenance burden. CPAN installation failures can produce extensive output while obscuring an underlying problem such as a missing compiler. Maintaining software written eight or nine years earlier competes with current work, even when users still need help.

### Hardware compatibility and bundled dependencies

Apple M1 laptops introduce another installation barrier. Andrew explains that Intel and ARM processors use different instructions, and that emulation can slow things down. He would like to address Roary's M1 problems but does not have the hardware to test them. The hosts also report difficulties running bioinformatics software under Windows Subsystem for Linux.

Lee contrasts shared-library conflicts with Rust's approach: downloading the required dependency versions into separate project directories before compilation. He describes the resulting executable as self-contained, with a bloated source directory as the trade-off. Across these examples, the discussion returns to the difficulty of supporting environments developers cannot test themselves.

### Keep Conda environments small and separate

Nabil-Fareed recommends a separate Conda environment for each project, containing the required language versions and tools, such as Python, Perl, R and samtools. A particularly complicated tool may warrant its own environment. Keeping project software out of the system installation and Conda's base environment makes a damaged environment easier to discard and rebuild. He also advises against nesting another virtual environment inside Conda, because it becomes difficult to know what needs activating.

Lee goes further by loading Conda explicitly from a separate shell script rather than automatically when his shell starts. Mamba is discussed as a replacement for Conda's package-management commands, with much faster dependency solving: Nabil-Fareed recalls a roughly 15-minute operation taking about one minute. Lee raises a concern he has heard about Mamba taking shortcuts, but Nabil-Fareed reports no failures in his relatively small, project-specific environments.

### Package managers and community packaging

The discussion also covers Homebrew, pip and Perlbrew. Lee describes Perlbrew as a way to install Perl and its libraries locally, rather than as a virtual environment. Andrew now relies heavily on Conda, and the hosts suggest that packaging software for it becomes straightforward after the first attempt.

Andrew contrasts this with the higher entry bar for Ubuntu and Debian's APT packaging. He describes substantial review and mentoring that can last six months or a year. That effort supports stable, long-lived packages, with volunteers doing the work of making bioinformatics tools installable alongside their dependencies.

### Containers for services, HPC and teams

Nabil-Fareed finds Docker useful for starting databases such as Postgres and web servers without installing everything directly onto the operating system. He prefers Singularity for more complicated software when moving between local work and high-performance computing. Andrew describes building Docker containers around Conda installations, keeping one tool in each container, while noting the additional challenge of coordinating multiple containers.

For interactive R work, Nabil-Fareed discusses Rocker, tidyverse and extra packages assembled into a ready-to-use container. Connecting this to RStudio or Jupyter Notebooks lets the user work through a browser without dealing directly with Docker during the analysis.

At team level, his group shares a directory of Singularity containers. These replace the shared directories of carefully prepared binary files that teams previously passed around.

## Highlights

- [00:02:10](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=2:10) — Manual compilation, exact dependency versions and incomplete installation instructions
- [00:04:50](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=4:50) — How a diamond dependency creates conflicting library requirements
- [00:11:12](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=11:12) — What version numbers should mean, and Kraken's distinct executable names
- [00:13:48](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=13:48) — Roary installation failures, CPAN and difficult error messages
- [00:15:52](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=15:52) — Intel versus ARM instructions and the difficulty of testing M1 compatibility
- [00:21:59](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=21:59) — Separate Conda environments for projects and a clean base environment
- [00:25:20](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=25:20) — Mamba as a faster replacement for Conda package-management commands
- [00:28:12](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=28:12) — APT packaging, quality review and long-term package stability
- [00:29:17](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=29:17) — Docker for databases and web servers, and Singularity for HPC
- [00:30:50](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=30:50) — Container base systems and keeping individual Conda-installed tools separate
- [00:32:19](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=32:19) — Building interactive R environments with containers and browser interfaces
- [00:33:23](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=33:23) — Sharing Singularity containers within a team instead of binary files

## In their own words

> So if it's not in Conda, then it doesn't exist.
>
> — Andrew Page, [00:27:27](https://soundcloud.com/microbinfie/avoid-dependency-hell-and-get-up-and-running-fast#t=27:27)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Roary, Biopython, Kraken, samtools, Python, Perl, R, Rust, CPAN, Conda, Mamba, pip, Homebrew, Perlbrew, APT, Docker, Singularity, Postgres, Rocker, tidyverse, RStudio, Jupyter Notebooks, Windows Subsystem for Linux.

## Questions this episode answers

### Should I create a separate Conda environment for every project?

Nabil-Fareed recommends doing so, keeping each project's tools and language versions together and leaving the base environment largely untouched. Particularly complicated tools may benefit from their own separate environments.

### Why use Mamba instead of Conda?

The hosts describe Mamba as using the same style of package-management commands while solving environments much faster. Nabil-Fareed reports good results with small environments, while Lee raises an unverified concern about shortcuts rather than presenting a demonstrated failure.

### When do the hosts use Docker rather than Singularity?

Nabil-Fareed uses Docker for services such as databases and web servers, and for interactive R environments. He prefers Singularity for more complicated software when working across local machines and HPC.

### Why can software work for its author but fail for another user?

The episode gives examples involving conflicting dependency versions, missing compilers, shared libraries being overwritten and different processor architectures. Developers may also lack the hardware or operating system needed to reproduce a user's problem.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Often the hard part of bioinformatics isnt the analysis, its getting all of the software you
need setup and installed. Come with us on this journey and avoid dependancy hell.

In the MicroBinfie podcast, the hosts discuss the struggles of installing, managing, and
dealing with dependencies with bioinformatics software. In the past, software installations
were a nightmare, and it was common to edit lines of code and manage dependencies manually,
causing conflicts like diamond dependency. To ease this process, the hosts suggest using
containers, virtual machines, and local environments. They stress the importance of adhering to
semantic versioning guidelines and understanding the end-users' perspective for proper
documentation, testing, and clarity regarding dependencies. Additionally, software maintenance
is critical for its longevity and usability.

The hosts also discuss software dependency management with different chip architectures and
operating systems. The M1 Apple architecture's differences from traditional computer processors
cause compatibility issues and slow down emulation, leading to difficulties in informatics.
Using separate Conda environments for each project or Mamba as a package manager can solve
dependency-related problems that can cause significant issues. However, Mamba may take
shortcuts and create conflicts with specific programs. Other package managers like Homebrew and
APT are also discussed.

The episode also covers the benefits of using Docker and Singularity to manage software
packages on a local machine. Docker is useful for databases, web servers, and complicated
pipelines, while Singularity is perfect for more complex software and plays better with HPC.
The hosts provide tips on using containers or virtual machines in a team environment, passing
containers instead of binary files, and using Docker and Singularity as tools to ease the
process. Overall, the episode offers practical advice to streamline the workflow of researchers
who manage software packages.
