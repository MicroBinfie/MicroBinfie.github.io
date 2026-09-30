---
layout: page
title: 'Episode 6: Writing good bioinformatics software with Torsten Seemann'
date: '2019-11-28 00:00:00'
link: https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann
episode: '6'
soundcloud_track: '679080552'
tags:
- microbinfie
- podcast
description: Torsten Seemann discusses Prokka, standard formats, Conda packaging and the long-term work of maintaining useful bioinformatics software.
excerpt: Torsten Seemann discusses Prokka, standard formats, Conda packaging and the long-term work of maintaining useful bioinformatics software.
headline: Writing usable bioinformatics software with Torsten Seemann
guests:
- Torsten Seemann
topics:
- bioinformatics software
- genome annotation
- command-line interfaces
- software packaging
- standard file formats
- documentation
- open-source maintenance
- community support
- software publication
faq:
- q: Why did Prokka become widely used?
  a: Seemann credits straightforward installation, bundled databases, minimal required settings and fast command-line operation. Its standard GFF and GenBank outputs also made it easy to connect to downstream analysis tools.
- q: Why does Prokka use a small annotation database?
  a: Seemann wanted to reduce download size and avoid propagating poorly supported annotations. He describes filtering UniProt Swiss-Prot using evidence codes to obtain about 70,000 proteins, sufficient to annotate roughly 60% of genes with high reliability.
- q: Why use Conda when a Python tool is already available through pip?
  a: The episode distinguishes installing Python code from installing its external dependencies. Conda recipes can also bring in tools such as SAMtools and BWA, reusing existing packages without requiring administrator access.
- q: How does Torsten Seemann manage software support requests?
  a: He encourages GitHub issues rather than private email so that other users can contribute answers. Community help reduces the burden, but he still describes maintenance as substantial work requiring time, employer support and better funding.
---

*Writing usable bioinformatics software with Torsten Seemann*

Torsten Seemann joins Nabil-Fareed Alikhan and Andrew Page to discuss what makes bioinformatics software useful beyond its accompanying paper. Drawing on Prokka and his other tools, he explains the value of straightforward installation, small curated databases, standard outputs and predictable command-line behaviour. The conversation also covers packaging, publication, user support and the commitment required to maintain software.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 6: Writing good bioinformatics software with Torsten Seemann" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/679080552&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 6: Writing good bioinformatics software with Torsten Seemann on SoundCloud](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann)

## In this episode

### Prokka as a practical model

Seemann approaches good software by avoiding the experiences that make bad software frustrating. The implementation language matters less to users than whether a tool works reliably and does what they need. Prokka illustrates that approach: it bundled small databases and Linux and Mac binaries, accepted a FASTA file of contigs with minimal configuration, and produced standard annotation outputs.

He traces Prokka to modular Bash scripts developed around 2004–2006 at Monash University's Department of Microbiology, with the paper following in 2014. It originally helped bootstrap manual curation of a single genome. As sequencing expanded to hundreds and thousands of genomes, its command-line interface made automated annotation practical without repeated website uploads. GFF and GenBank outputs could feed downstream tools such as Artemis and Roary.

### Smaller databases, better-supported annotations

Prokka's database design was partly a response to distribution problems. Seemann recalls a 1.2 GB download hosted on a university website, complaints from users outside Australia, and a Dropbox account suspended after one day of excessive bandwidth use. Google Drive subsequently handled the bandwidth, but reducing the download remained worthwhile.

Rather than use the whole nr database, he selected the curated UniProt Swiss-Prot collection and filtered records using their evidence codes. He describes a resulting set of about 70,000 proteins that could annotate roughly 60% of genes with high reliability. His concern was that poorly supported annotations could otherwise propagate between records. For users wanting more detailed annotation, Prokka gained the ability to incorporate supplied reference genomes.

### Standard outputs and predictable behaviour

The discussion recommends established formats such as BED, GFF, VCF and FASTA instead of inventing another format that downstream users must interpret. Seemann argues that interoperability reduces the glue code needed between tools. Barrnap follows the same general model as Prokka: a focused task, bundled databases and simple inputs and outputs.

A command run without sufficient arguments should explain what is missing, not produce a traceback or silently create files. Help should be available, and progress messages should tell users what is happening; Seemann favours informative logging with a quiet option.

Dependencies can undermine reliability. He describes NCBI's tbl2asn converter as a recurring Prokka problem: it is distributed only as a binary, updates appear without warning, and it expires after roughly six months to a year. He wants to remove that dependency despite its value in producing compliant GenBank files.

### Hosting and packaging for installation

Seemann recommends public source repositories over personal or institutional websites, where reorganisations can leave software links broken. GitHub helped him organise issues and contributions; he also considers Bitbucket and GitLab suitable alternatives.

For installation, he favours Conda and Bioconda. Conda supports versions and separate environments without requiring administrator access, while recipes reuse packages for existing dependencies. He contrasts this with Homebrew's flatter versioning approach and the complexity of traditional distribution packaging.

Language-specific packaging still matters: Python software should use PyPI, Perl software CPAN, and R software CRAN. A Python package can make subsequent Conda packaging easier, but pip alone will not install external tools such as SAMtools or BWA. Clear dependency and installation documentation helps community packagers produce reliable packages.

### Names, visibility and software publication

A distinctive name helps people find software without confusing it with another package. Seemann describes checking proposed names through Google searches, including incognito searches. The group also discusses checking Urban Dictionary and the pitfalls of forced backronyms.

Seemann has mainly promoted tools through blog posts and Twitter, usually waiting until a tool is in a reasonably good state. His blog post on command-line software standards became a GigaScience paper. He argues that a software paper's URL belongs in its abstract, where readers can find it immediately.

The group discusses preprints and the Journal of Open Source Software. Seemann values JOSS's emphasis on installability, documentation and software quality. Its review guidance is suggested as useful even for developers who do not submit there.

### Maintenance is part of the project

Seemann's first advice to someone considering a new tool is not to write one, because doing it properly is a big commitment. He discourages writing software merely to publish and abandon it, and argues that using it yourself exposes problems that motivate improvements. Releasing code before publication also lets the community find problems the author has missed.

For support, he prefers GitHub issues to private email because users can help one another. He describes substantial community assistance, but also unreviewed pull requests, unresolved problems and guilt about work he cannot complete. His employer recognises maintenance as part of his job; he notes that others do not have that support.

He identifies maintenance funding as an unmet need. In this 2019 discussion, he describes then-new Chan Zuckerberg grants offering US$50,000–250,000 for established software, with three rounds a year, as a possible route to supporting Prokka and other tools.

## Highlights

- [00:01:51](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=1:51) — Avoiding bad software experiences and prioritising the user's interaction
- [00:03:05](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=3:05) — Prokka's bundled databases, minimal inputs and origins in genome curation
- [00:08:37](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=8:37) — Standard file formats and command-line workflows
- [00:10:21](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=10:21) — Reducing dependencies and building a smaller, curated annotation database
- [00:16:13](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=16:13) — What a tool should do when first run without the required arguments
- [00:18:38](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=18:38) — The reliability problems caused by Prokka's tbl2asn dependency
- [00:19:46](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=19:46) — Why writing a new tool requires a commitment to maintenance
- [00:22:35](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=22:35) — Adopting GitHub for source distribution, issues and contributions
- [00:24:40](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=24:40) — Choosing distinctive software names and checking for conflicts
- [00:28:21](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=28:21) — Installing without administrator access through Conda and community packaging
- [00:36:51](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=36:51) — JOSS and reviewing software for usability and quality
- [00:38:00](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=38:00) — Managing support requests, community help and maintenance funding

## In their own words

> You don't expect it to just spit out an error. You expect it to spit out a useful piece of information to tell you what to do next.
>
> — Torsten Seemann, [00:16:13](https://soundcloud.com/microbinfie/05-writing-good-bioinformatics-software-with-torsten-seemann#t=16:13)

## Who is talking

- **Torsten Seemann** (guest, Microbiological Diagnostic Unit Public Health Lab, Doherty Institute for Immunity and Infection, University of Melbourne)
- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)
- **Lee Katz** (host)

## Tools and resources mentioned

Prokka, Snippy, Barrnap, Abricate, Nullarbor, MLST, Roary, Artemis, UniProt, UniProt Swiss-Prot, nr, GenBank, tbl2asn, Conda, Bioconda, Homebrew, GitHub, Bitbucket, GitLab, PyPI, pip, CPAN, CRAN, SAMtools, BWA.

## Questions this episode answers

### Why did Prokka become widely used?

Seemann credits straightforward installation, bundled databases, minimal required settings and fast command-line operation. Its standard GFF and GenBank outputs also made it easy to connect to downstream analysis tools.

### Why does Prokka use a small annotation database?

Seemann wanted to reduce download size and avoid propagating poorly supported annotations. He describes filtering UniProt Swiss-Prot using evidence codes to obtain about 70,000 proteins, sufficient to annotate roughly 60% of genes with high reliability.

### Why use Conda when a Python tool is already available through pip?

The episode distinguishes installing Python code from installing its external dependencies. Conda recipes can also bring in tools such as SAMtools and BWA, reusing existing packages without requiring administrator access.

### How does Torsten Seemann manage software support requests?

He encourages GitHub issues rather than private email so that other users can contribute answers. Community help reduces the burden, but he still describes maintenance as substantial work requiring time, employer support and better funding.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Torsten Seemann joins us to discuss how to write good bioinformatics
software. Torsten is the author of many popular bioinformatics tools
such as Prokka, Snippy, Barrnap, Abricate, Shovill, and Nullarbor.

Links: https://github.com/tseemann
