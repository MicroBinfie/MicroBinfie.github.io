---
layout: page
title: 'Encore of episode 6: What software not to write'
date: '2021-07-01 00:00:00'
link: https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write
episode: encore-6
soundcloud_track: '1078225456'
tags:
- microbinfie
- podcast
description: Torsten Seemann discusses Prokka, reliable command-line tools, Conda packaging and the long-term work of maintaining bioinformatics software.
excerpt: Torsten Seemann discusses Prokka, reliable command-line tools, Conda packaging and the long-term work of maintaining bioinformatics software.
headline: 'What not to write: Torsten Seemann on bioinformatics software'
guests:
- Torsten Seemann
topics:
- bioinformatics software
- bacterial genome annotation
- command-line usability
- software packaging
- reproducibility
- data standards
- open-source maintenance
- user support
- software publication
faq:
- q: Why did Prokka become widely used?
  a: Seemann credits easy installation, bundled small databases, useful defaults and fast command-line operation. Standard GFF and GenBank outputs also made it straightforward to connect Prokka to downstream analysis tools.
- q: When should a bioinformatician avoid writing a new tool?
  a: Seemann advises against starting if the plan is simply to publish and abandon it, or if the developer will not use it themselves. Maintaining a useful tool is a long-term commitment, and encountering its problems firsthand helps drive improvements.
- q: Why use Conda as well as pip for a Python bioinformatics tool?
  a: In the episode’s examples, pip installs Python software but not external dependencies such as samtools or BWA. Conda can bring those components together using existing packages, without requiring administrator access.
- q: How does Torsten Seemann manage support for his tools?
  a: He encourages users to open GitHub issues rather than send private email, allowing other users to help answer questions. Community support reduces the burden, but he still describes substantial work and guilt around unresolved issues and pull requests.
---

*What not to write: Torsten Seemann on bioinformatics software*

Torsten Seemann joins Nabil-Fareed Alikhan and Andrew Page to discuss what makes bioinformatics software useful beyond its publication. Drawing on Prokka and his other tools, he explains the value of straightforward installation, small databases, standard formats and helpful command-line behaviour. The conversation also covers naming, packaging, promotion and the continuing responsibility of supporting users.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Encore of episode 6: What software not to write" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1078225456&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Encore of episode 6: What software not to write on SoundCloud](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write)

## In this episode

### Why Prokka became useful

Seemann traces Prokka back to modular bash scripts used internally at Monash University around 2004–2006, before its paper appeared in 2014. It began as a way to bootstrap manual gene curation for individual genomes. As sequencing volumes increased, the same approach became useful for annotating hundreds or thousands of bacterial genomes.

He attributes its adoption to practical details: a single download, bundled Linux and Mac binaries, small databases and usable defaults. Users could supply a FASTA file of contigs without choosing lots of settings, then receive valid GFF and GenBank files for downstream work in tools such as Artemis or Roary. Running locally on the command line also avoided uploading genomes to websites one at a time and tracking their downloads and failures. His wider design pattern is minimal input, predictable output and software that works immediately.

### Smaller databases and standard formats

Reducing Prokka’s download size was partly a distribution problem. Seemann recalls a roughly 1.2 GB archive, slow downloads from Australia and a Dropbox account suspended after excessive bandwidth use. He subsequently used Google Drive, but also reconsidered how much annotation data the tool needed.

Rather than use the whole NR database, with the risk of propagating poor annotations, he selected the curated UniProt SwissProt records and filtered further using evidence codes. This reduced the database to about 70,000 proteins; he says it could annotate around 60% of genes using a small, reliable reference set. Prokka later gained support for user-supplied reference genomes. He also recommends established formats such as BED, GFF, VCF and FASTA: interoperable outputs mean fewer conversion scripts between pipeline steps.

### Make the first run a good experience

The conversation follows a familiar disappointment: discover a promising paper, struggle to find its source-code link, work through installation instructions, then encounter an error on a small test dataset. Seemann argues that a software paper’s URL belongs in its abstract. Andrew Page adds examples of hardcoded institutional settings and instructions requiring users to edit a particular script line.

Once installed, a command run without the necessary inputs should explain what is missing, not crash or silently create files. Seemann favours informative progress messages, with a quiet option for larger pipelines. The discussion also identifies a troublesome Prokka dependency: NCBI’s table2asn tool, which writes its GenBank files. Seemann describes binary-only distribution, updates that appear without notice and expiry after roughly six months to a year. Although it produced compliant files, he regards relying on it as a mistake.

### Decide whether to write it at all

Seemann’s first advice to prospective developers is not to start unless they are prepared for maintenance. Publishing a tool and abandoning it does little for its users. Using the software yourself matters because experiencing its failures creates a direct incentive to improve it. Prokka illustrates how that commitment can extend well beyond the initial project or paper.

A distinctive name and a durable source-code home are also part of making software usable. Seemann describes checking names such as Prokka, Snippy and Barrnap through searches for conflicts; the discussion also recommends checking Urban Dictionary. He favours GitHub, GitLab or Bitbucket over institutional websites whose reorganisations can break download links. GitHub’s issue tracking and pull requests helped persuade him to move beyond distributing numbered archives from personal websites.

### Package for people who just want to install it

The intended audience is often a biologist with data to analyse, not another developer. Traditional distribution packages can be demanding to prepare, and installation may require administrator access. Homebrew and Conda offer alternatives, with Seemann highlighting Conda’s handling of versions and environments as important for reproducibility.

For Python tools, he recommends packaging for PyPI so users can install them with pip. That also simplifies subsequent Conda packaging. However, pip does not install external programs such as samtools or BWA alongside the Python scripts. Conda can combine the tool with those dependencies by reusing existing packages.

Clear dependency lists and setup instructions make life easier for the Bioconda contributors who package tools for the community. Seemann describes volunteers updating packages before he has noticed, and connects straightforward installation with wider research use and citations.

### Promotion, support and paying for maintenance

Seemann has promoted tools through blog posts and Twitter, often before writing papers. The hosts advocate preprints while cautioning that authors should check journal policies. The Journal of Open Source Software interests Seemann because its review focuses on software quality, documentation and installation. Its reviewer guidelines are suggested as a useful checklist even for developers not submitting there.

For support, he encourages GitHub issues rather than private email. Other users often answer questions before he reaches them, making maintenance partly a community effort. Nevertheless, unresolved issues and unreviewed pull requests create a substantial workload and a sense of guilt. He says his employer recognises maintenance as part of his job, while acknowledging that many bioinformaticians lack that support.

At the time of the conversation, he was investigating a Chan Zuckerberg grant programme for established computational biology software. He describes awards of US$50,000–250,000, with three rounds per year, intended for maintenance rather than creating new tools. The broader point is that successful software needs continuing resources, not just an initial publication.

## Highlights

- [00:03:03](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=3:03) — Prokka’s bundled databases, minimal settings and origins in manual genome annotation.
- [00:08:37](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=8:37) — Standard formats reduce the glue needed between bioinformatics tools.
- [00:10:23](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=10:23) — Reducing dependencies and shrinking Prokka’s annotation databases.
- [00:12:36](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=12:36) — The frustrating journey from discovering a software paper to a failed first run.
- [00:16:12](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=16:12) — What a command-line tool should do when users run it without required inputs.
- [00:19:45](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=19:45) — Why developers should not start a tool they will neither use nor maintain.
- [00:22:38](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=22:38) — Moving Prokka from website downloads to GitHub and version control.
- [00:24:40](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=24:40) — Choosing a distinctive software name and checking for conflicts.
- [00:28:24](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=28:24) — Installation without administrator access and the community effort behind Bioconda.
- [00:31:06](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=31:06) — Packaging explained, from configure and make to PyPI and Conda.
- [00:36:54](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=36:54) — JOSS and reviewing software for usability, documentation and installation.
- [00:38:01](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=38:01) — Managing support through GitHub issues and sustaining long-term maintenance.

## In their own words

> I think the software URL should be in the abstract.
>
> — Torsten Seemann, [00:14:39](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=14:39)

> If you're going to just write a tool, publish it and then abandon it, please do not start that project.
>
> — Torsten Seemann, [00:19:45](https://soundcloud.com/microbinfie/encore-06-what-software-not-to-write#t=19:45)

## Who is talking

- **Torsten Seemann** (guest, Microbiological Diagnostic Unit Public Health Lab, Doherty Institute for Immunity and Infection, University of Melbourne)
- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)
- **Lee Katz** (host)

## Tools and resources mentioned

Prokka, Snippy, Barrnap, Abricate, Nullarbor, MLST, Artemis, Roary, UniProt, UniProt SwissProt, NR database, GenBank, table2asn, Conda, Bioconda, Homebrew, PyPI, pip, samtools, BWA, GitHub, GitLab, Bitbucket, SourceForge, Debian Med.

## Questions this episode answers

### Why did Prokka become widely used?

Seemann credits easy installation, bundled small databases, useful defaults and fast command-line operation. Standard GFF and GenBank outputs also made it straightforward to connect Prokka to downstream analysis tools.

### When should a bioinformatician avoid writing a new tool?

Seemann advises against starting if the plan is simply to publish and abandon it, or if the developer will not use it themselves. Maintaining a useful tool is a long-term commitment, and encountering its problems firsthand helps drive improvements.

### Why use Conda as well as pip for a Python bioinformatics tool?

In the episode’s examples, pip installs Python software but not external dependencies such as samtools or BWA. Conda can bring those components together using existing packages, without requiring administrator access.

### How does Torsten Seemann manage support for his tools?

He encourages users to open GitHub issues rather than send private email, allowing other users to help answer questions. Community support reduces the burden, but he still describes substantial work and guilt around unresolved issues and pull requests.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Torsten Seemann joins us to discuss how to write good bioinformatics
software. Torsten is the author of many popular bioinformatics tools
such as Prokka, Snippy, Barrnap, Abricate, Shovill, and Nullarbor.
Links: https://github.com/tseemann
