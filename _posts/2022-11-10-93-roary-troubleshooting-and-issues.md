---
layout: page
title: 'Episode 93: Roary Troubleshooting And Issues'
date: '2022-11-10 00:00:00'
link: https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues
episode: '93'
soundcloud_track: '1284779149'
tags:
- microbinfie
- podcast
description: The hosts work through Roary bug reports, from missing sequences and dependencies to empty core genomes, and explain how to report problems clearly.
excerpt: The hosts work through Roary bug reports, from missing sequences and dependencies to empty core genomes, and explain how to report problems clearly.
headline: 'Roary troubleshooting: dependencies, inputs and empty core genomes'
guests: []
topics:
- roary troubleshooting
- pangenome analysis
- dependency management
- bug reporting
- gff inputs
- core genomes
- gene copy separation
- assembly quality
- incremental analysis
faq:
- q: Why does Roary report that it cannot guess a sequence alphabet?
  a: The hosts suggest that the input may be empty or lack nucleotide sequence. In particular, a GFF file may contain annotations without the assembly sequence at the bottom, so they recommend checking the file’s sequence content.
- q: What could cause a missing _clustered.clstr file in Roary?
  a: Andrew suspects that CD-HIT is missing, unavailable on the executable path, or crashing when executed. The hosts treat the accompanying standard-locale warning as a separate issue rather than the likely explanation.
- q: Can I add one genome to an existing Roary analysis?
  a: In the episode, Andrew says Roary does not support incremental additions. For the example of adding one genome to an analysis of 3,000 isolates, his answer is to rerun the analysis from scratch.
- q: Why might Roary find zero core genes in closely related bacteria?
  a: The hosts consider thresholds and poor-quality inputs, including empty files, very small assemblies and short contigs that prevent reliable gene calling. For the reported example, they suspect widespread assembly problems and suggest running QUAST on the assemblies.
- q: What should I include in a Roary bug report?
  a: Include how the software was installed, the operating system, the input files and their scale, the error output or traceback, and enough information to reproduce the failure. The hosts recommend GitHub issue templates to prompt users for these details.
---

*Roary troubleshooting: dependencies, inputs and empty core genomes*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan work through Roary GitHub issues, suggesting explanations for missing files, failed installations and unexpected pangenome results. They discuss how input sequences, software dependencies and assembly quality affect an analysis, alongside Roary’s handling of repeated genes and additional genomes. These are diagnoses from the reports rather than confirmed fixes, with practical advice on supplying enough information for a developer to investigate.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 93: Roary Troubleshooting And Issues" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1284779149&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 93: Roary Troubleshooting And Issues on SoundCloud](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues)

## In this episode

### Missing sequences and command-line help

The first report says that a sequence has no letters and its alphabet cannot be guessed. The hosts suggest an empty input, an input without nucleotide sequence, or a GFF file lacking the assembly sequence at the bottom. They note that GFF downloads from NCBI can lack that sequence and recommend checking the sequence content of both GFF and GenBank files.

The report also contains repeated GNU Parallel citation notices, reaching 62 runs. These are separate from the sequence problem. Another user wants to extract core or accessory gene sequences for annotation. One of the hosts points them towards Roary’s command-line help, tentatively recalling a -z flag rather than presenting a verified command.

### Tracing dependency and installation failures

A missing _clustered.clstr file leads Andrew to suspect CD-HIT: it may be absent, unavailable on the executable path, or failing when run. The hosts distinguish that likely failure from a warning about falling back to the standard C locale. They also discuss the limits of stack traces and dependency checks: finding an executable does not guarantee that it will run successfully.

A separate installation through cpanm produces hundreds of lines of output and failures among dependencies of dependencies. Andrew notes that this route does not install Roary’s non-Perl dependencies. Lee looks for the first actual error and identifies a BioPerl-related failure; Andrew points out that unrelated modules are failing too.

Their possible explanations include missing GCC, zlib or other system libraries. Berkeley DB and MySQL are also suggested as possible missing components, not established causes. A proposed PERL5LIB fix illustrates another distinction: Perl’s library-search configuration can cause problems, but Andrew does not think it explains this particular log.

### What makes a bug report actionable

An error saying that a file cannot be opened offers too little context for a confident diagnosis. The file might be missing, a symbolic link might point to something absent, or the user might be in the wrong directory or supplying the wrong path.

The hosts ask for installation details, the operating system, input files, their size and content, the traceback, and a way to reproduce the failure. A tiny GFF and several gigabytes of input present very different possibilities. GitHub issue templates can prompt users for these details instead of leaving them with an unrestricted text box, but users still need to describe what happened.

### Why repeated genes can remain separate

A request to remove redundant genes prompts an explanation of Roary’s treatment of multiple gene copies. Andrew says that Roary examines roughly five genes upstream and downstream, using the surrounding context as a fingerprint to separate copies according to where they occur.

Consequently, seeing the same gene represented more than once in a core genome is not automatically an error: the separation carries information about repeated copies. Andrew tentatively recalls a -s flag for disabling this splitting. The discussion also stresses the importance of orthology and asks what a sequence-only gene catalogue is intended to achieve before deciding that those distinctions should be removed.

### Adding genomes and supporting new hardware

One user has analysed 3,000 isolates and wants to add one more. Andrew explains that Roary does not support this incremental, n-plus-one operation: the analysis must be rerun from scratch. Clustering depends on the collection of genomes, and adding incremental support would require substantial engineering. He contrasts this with other pangenome implementations designed around that capability from the beginning.

A request for a Bioconda version compatible with macOS Monterey on M1 ARM64 hardware raises a separate support limitation. Andrew says he does not have one of those machines and cannot investigate the platform-specific problem himself.

### Investigating a zero-sized core genome

The final example concerns supposedly closely related bacteria with no core or soft-core genes. The user expects genes such as rpoB to be present. Looking at 25 genomes and roughly 3,800 clusters, the hosts consider thresholds but focus on poor inputs: empty files, very small assemblies, or contigs too short for reliable gene calling.

They suggest running QUAST to assess the assemblies. They also credit the user for checking expected shared genes such as 16S and recognising that the result is suspicious rather than accepting it blindly. As context, they discuss shared genes across Gram-positive and Gram-negative bacteria, mention E. coli and Salmonella, and recall early comparative work involving Mycoplasma and E. coli.

## Highlights

- [00:00:47](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=0:47) — Andrew introduces the exercise of diagnosing Roary GitHub issues from their reports.
- [00:01:55](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=1:55) — Empty inputs and GFF files without assembly sequence can explain an alphabet-guessing error.
- [00:03:39](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=3:39) — A missing _clustered.clstr file prompts investigation of CD-HIT and dependency failures.
- [00:05:59](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=5:59) — Useful bug reports need installation details, inputs, operating system and reproducible errors.
- [00:06:58](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=6:58) — GitHub issue templates can ask users for the information developers need.
- [00:07:34](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=7:34) — Roary uses neighbouring genes to distinguish multiple copies of the same gene.
- [00:09:12](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=9:12) — A cpanm installation exposes failures among several layers of dependencies.
- [00:11:35](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=11:35) — Clustering makes incremental genome additions difficult; Roary requires a complete rerun.
- [00:14:02](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=14:02) — The hosts interpret roughly 3,800 clusters across 25 genomes as a warning about input quality.
- [00:15:06](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=15:06) — The hosts suggest QUAST and credit the user for checking expected shared genes after a zero-core result.

## In their own words

> I would say for filing a bug report, you need to actually provide some more information.
>
> — Andrew Page, [00:05:59](https://soundcloud.com/microbinfie/93-roary-troubleshooting-and-issues#t=5:59)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Roary, GNU Parallel, CD-HIT, cpanm, Perl, BioPerl, GCC, zlib, Berkeley DB, MySQL, Bioconda, QUAST, GitHub, GenBank.

## Questions this episode answers

### Why does Roary report that it cannot guess a sequence alphabet?

The hosts suggest that the input may be empty or lack nucleotide sequence. In particular, a GFF file may contain annotations without the assembly sequence at the bottom, so they recommend checking the file’s sequence content.

### What could cause a missing _clustered.clstr file in Roary?

Andrew suspects that CD-HIT is missing, unavailable on the executable path, or crashing when executed. The hosts treat the accompanying standard-locale warning as a separate issue rather than the likely explanation.

### Can I add one genome to an existing Roary analysis?

In the episode, Andrew says Roary does not support incremental additions. For the example of adding one genome to an analysis of 3,000 isolates, his answer is to rerun the analysis from scratch.

### Why might Roary find zero core genes in closely related bacteria?

The hosts consider thresholds and poor-quality inputs, including empty files, very small assemblies and short contigs that prevent reliable gene calling. For the reported example, they suspect widespread assembly problems and suggest running QUAST on the assemblies.

### What should I include in a Roary bug report?

Include how the software was installed, the operating system, the input files and their scale, the error output or traceback, and enough information to reproduce the failure. The hosts recommend GitHub issue templates to prompt users for these details.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We go through bug reports and issues and give insights into how bioinformaticians dig into
them. We suggest the underlying problems and possible solutions and also provide tips on how to
file better bug reports.
