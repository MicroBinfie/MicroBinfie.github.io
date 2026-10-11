---
layout: page
title: 'Episode 19: Microbinfies assemble'
date: '2020-05-28 00:00:00'
link: https://soundcloud.com/microbinfie/microbinfies-assemble
episode: '19'
soundcloud_track: '767640103'
tags:
- microbinfie
- podcast
description: How bacterial short-read assemblers evolved, and how Velvet, SPAdes, Shovill and SKESA compare on speed, accuracy and reproducibility.
excerpt: How bacterial short-read assemblers evolved, and how Velvet, SPAdes, Shovill and SKESA compare on speed, accuracy and reproducibility.
headline: 'Short-read bacterial assembly: Velvet, SPAdes and SKESA'
guests: []
topics:
- bacterial genome assembly
- short reads
- de novo assembly
- de bruijn graphs
- k-mer selection
- assembly accuracy
- reproducibility
- assembler benchmarking
- public sequence archives
faq:
- q: How do SPAdes and SKESA compare for bacterial assembly?
  a: Lee describes SPAdes as favouring longer, more contiguous output and SKESA as stopping more conservatively at ambiguity. He reports typical working times of two to ten minutes for SKESA and 30 to 90 minutes for SPAdes, but explicitly identifies these as personal observations rather than a controlled benchmark.
- q: Can multithreading change the result of a genome assembly?
  a: Nabil recalls that multithreaded Velvet could produce different results between runs, while single-threaded runs were repeatable in his experience. Lee contrasts this with SKESA, which he describes as producing the same assembly from the same input and essential parameters regardless of thread count or computer.
- q: Why did the hosts keep using Velvet for so long?
  a: They valued its reliable operation and conservative contigs. VelvetOptimiser made parameter selection easier, while early concerns about SPAdes' memory use and assembly decisions helped keep Velvet embedded in existing workflows.
- q: What does Shovill change about a SPAdes workflow?
  a: The episode describes Shovill overlapping reads before assembly, turning off SPAdes' read correction and handling correction separately. The hosts also discuss subsequent SPAdes guidance and an isolate option, but do not provide a fresh benchmark of those changes.
- q: What reading does the episode recommend for understanding assembly graphs?
  a: Nabil recommends the Velvet paper and its author's dissertation. He highlights their explanations of graph features such as bubbles and spurs, and questions such as why k-mers have odd-numbered lengths.
---

*Short-read bacterial assembly: Velvet, SPAdes and SKESA*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss the history and practical use of short-read de novo assembly, focusing on bacterial genomes. They compare Velvet, SPAdes and SKESA through their own experience, covering conservative contigs, memory use, reproducibility and parameter selection. The discussion also explains why assembler comparisons need careful interpretation as software and recommended settings change.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 19: Microbinfies assemble" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/767640103&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 19: Microbinfies assemble on SoundCloud](https://soundcloud.com/microbinfie/microbinfies-assemble)

## In this episode

### From capillary sequencing to de Bruijn graphs

Nabil-Fareed Alikhan starts with the assembly problem: sequencing produces fragments rather than a complete chromosome, so overlapping observations must be used to reconstruct the original sequence. The historical discussion covers CAP3, phrap and the TIGR assembler in the capillary-sequencing era. The hosts remember inspecting consensus sequences alongside their underlying reads, obtaining software by emailing its authors, and struggling with installation requirements.

The discussion moves to overlap-consensus approaches, including Newbler for 454 data and Minimus. Increasing coverage from Illumina and SOLiD made those approaches computationally harder to use. De Bruijn graphs offered a more efficient representation for that data. Nabil identifies EULER as an important early implementation and a step towards Velvet, which became a familiar bacterial assembly tool.

### Why Velvet stayed in bacterial pipelines

The hosts remember Velvet as dependable and conservative: its contigs were something they felt they could trust. One host recalls running half a million assemblies through an automated pipeline at Sanger, where bacterial samples were assembled as they came off the sequencers. That pipeline later moved to SPAdes, but Velvet remained the default for years.

They also recall limitations. The default maximum k-mer size was small—remembered as 31—and became less suitable as reads grew longer. Broad variation in library insert sizes could cause problems too. VelvetOptimiser helped by trying different parameters and returning a usable assembly. Its reliability and accessibility mattered as much as any individual setting; the discussion also recalls a graphical interface that made the workflow easier to use.

### SPAdes, Shovill and bacterial isolate settings

Early SPAdes versions are remembered as more memory-intensive than Velvet, with some assembly decisions that initially made users cautious. The hosts stress that SPAdes improved substantially over time. Nabil also argues that the comparison was not like-for-like: SPAdes included read correction and post-processing that mapped reads back to check for errors, whereas Velvet concentrated on assembly itself.

Shovill enters the discussion as a way to alter that workflow, including overlapping reads before assembly and handling correction separately rather than using SPAdes' own correction stage. The hosts recall a comparison blog post, a response from the SPAdes team explaining suitable parameters, and an isolate option for bacterial assemblies. Lee explicitly says he has not made a thorough comparison since that response, so the episode does not establish how the revised settings perform against SKESA.

### SKESA: repeatability, speed and conservative contigs

Lee highlights SKESA's deterministic behaviour: the same input and essential parameters should produce the same assembly regardless of thread count or computer. This contrasts with the hosts' recollection that multithreaded assembly can produce different results between runs. Nabil remembers single-threaded Velvet as repeatable, while qualifying that account as experience from when he used it.

For speed, Lee gives personal working ranges of two to ten minutes per bacterial genome with SKESA, compared with 30 to 90 minutes for SPAdes. When asked, he clarifies that these are day-to-day observations, not a controlled comparison using matched resources.

He describes a trade-off between contiguity and conservative base calls: SPAdes tries to extend contigs, while SKESA stops at ambiguity. In one comparison, he reports zero ambiguous bases in the SKESA assemblies, versus ambiguous bases in the SPAdes output.

### Public assemblies as a starting point

Lee describes NCBI going back through SRA data to assemble genomes, particularly those in its pathogen detection pipeline. He believes the Listeria work is complete at that point and describes assemblies from CDC- or FDA-generated sequence data being available through RefSeq. This is presented as an ongoing effort to assemble more public data, not a claim that every SRA dataset has already been processed.

The hosts see substantial value in avoiding repeated assembly work. They describe assembly as the computationally intensive starting point, after which analyses such as genotyping and SNP calling can proceed. Ready-made assemblies could therefore save processing time and feed directly into downstream pipelines.

### Benchmarks, other assemblers and further reading

One host recalls an AMOS comparison in which an E. coli genome of about five million bases took a month to assemble on one core. The hosts also discuss Assemblathon 1 and 2, including jump libraries that not every assembler could use. Their recollections of the benchmark details are explicitly uncertain.

Other tools mentioned include A5, ABySS, SOAPdenovo and MIRA. Lee remembers MIRA 3 producing different assemblies between runs and taking all day with carefully chosen options, particularly in work involving 454 data.

For understanding assembly graphs, Nabil recommends the Velvet paper and its author's dissertation, including explanations of bubbles, spurs and odd-numbered k-mers. The hosts emphasise that assembler performance is a moving target: conclusions from this May 2020 discussion may not hold for later software versions.

## Highlights

- [00:00:58](https://soundcloud.com/microbinfie/microbinfies-assemble#t=0:58) — Why fragmented sequencing data need de novo assembly, and the earliest approaches
- [00:06:00](https://soundcloud.com/microbinfie/microbinfies-assemble#t=6:00) — De Bruijn graphs, EULER and the rise of Velvet
- [00:07:05](https://soundcloud.com/microbinfie/microbinfies-assemble#t=7:05) — Half a million Velvet assemblies and the limitations of its default k-mer size
- [00:09:44](https://soundcloud.com/microbinfie/microbinfies-assemble#t=9:44) — An automated Sanger assembly pipeline and a month-long AMOS comparison
- [00:11:40](https://soundcloud.com/microbinfie/microbinfies-assemble#t=11:40) — Why SPAdes and Velvet do different amounts of work, plus recommended reading
- [00:13:01](https://soundcloud.com/microbinfie/microbinfies-assemble#t=13:01) — Multithreading and whether repeated assembly runs give identical results
- [00:14:59](https://soundcloud.com/microbinfie/microbinfies-assemble#t=14:59) — Lee explains SKESA's deterministic output and his early experience with it
- [00:15:42](https://soundcloud.com/microbinfie/microbinfies-assemble#t=15:42) — NCBI's assembly of public SRA data and availability through RefSeq
- [00:18:10](https://soundcloud.com/microbinfie/microbinfies-assemble#t=18:10) — SPAdes versus SKESA: contiguity, ambiguity and conservative base calls
- [00:19:07](https://soundcloud.com/microbinfie/microbinfies-assemble#t=19:07) — Shovill, SPAdes parameter choices and the bacterial isolate option
- [00:21:45](https://soundcloud.com/microbinfie/microbinfies-assemble#t=21:45) — Assemblathon comparisons and the complications of specialised libraries

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

CAP3, phrap, TIGR Assembler, Newbler, Minimus, EULER, Velvet, VelvetOptimiser, SPAdes, Shovill, SKESA, AMOS, A5, ABySS, SOAPdenovo, MIRA, SRA, RefSeq, de Bruijn graphs, 454, Illumina, SOLiD.

## Questions this episode answers

### How do SPAdes and SKESA compare for bacterial assembly?

Lee describes SPAdes as favouring longer, more contiguous output and SKESA as stopping more conservatively at ambiguity. He reports typical working times of two to ten minutes for SKESA and 30 to 90 minutes for SPAdes, but explicitly identifies these as personal observations rather than a controlled benchmark.

### Can multithreading change the result of a genome assembly?

Nabil recalls that multithreaded Velvet could produce different results between runs, while single-threaded runs were repeatable in his experience. Lee contrasts this with SKESA, which he describes as producing the same assembly from the same input and essential parameters regardless of thread count or computer.

### Why did the hosts keep using Velvet for so long?

They valued its reliable operation and conservative contigs. VelvetOptimiser made parameter selection easier, while early concerns about SPAdes' memory use and assembly decisions helped keep Velvet embedded in existing workflows.

### What does Shovill change about a SPAdes workflow?

The episode describes Shovill overlapping reads before assembly, turning off SPAdes' read correction and handling correction separately. The hosts also discuss subsequent SPAdes guidance and an isolate option, but do not provide a fresh benchmark of those changes.

### What reading does the episode recommend for understanding assembly graphs?

Nabil recommends the Velvet paper and its author's dissertation. He highlights their explanations of graph features such as bubbles and spurs, and questions such as why k-mers have odd-numbered lengths.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Short read de novo assembly is discussed in this podcast. We cover the
history of assembly and how short read assemblers have evolved into
what we use today. The main focus is on bacterial assembly.
