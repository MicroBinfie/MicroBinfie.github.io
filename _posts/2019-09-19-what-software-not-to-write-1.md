---
layout: page
title: 'Episode 1: What bioinformatics software not to write part 1'
date: '2019-09-19 00:00:00'
link: https://soundcloud.com/microbinfie/what-software-not-to-write-1
episode: '1'
soundcloud_track: '679961927'
tags:
- microbinfie
- podcast
description: When should you avoid writing another assembler, mapper or variant caller? The hosts discuss mature tools, data quality and reinventing the wheel.
excerpt: When should you avoid writing another assembler, mapper or variant caller? The hosts discuss mature tools, data quality and reinventing the wheel.
headline: 'What bioinformatics software not to write: part 1'
guests: []
topics:
- microbial bioinformatics
- software development
- sequence alignment
- genome assembly
- read mapping
- variant calling
- reference selection
- workflow managers
- phylogenetics
- software reuse
faq:
- q: When do the hosts advise against writing a new bioinformatics tool?
  a: When many suitable tools already exist, the problem is effectively solved or unsolvable, or the underlying technology has been superseded. They still allow for specific use cases, but recommend examining existing work before starting another implementation.
- q: Which tools does the episode distinguish for sequence and whole-genome alignment?
  a: The hosts discuss MAFFT and MUSCLE for multiple sequence alignment of shorter sequences such as genes. For whole genomes, they name Mauve, Sibelia, Mugsy and Parsnp, warning against treating these as the same alignment problem.
- q: Why does reference selection matter for bacterial SNP calling?
  a: The hosts argue that a reference close to the data can improve SNP calls substantially. Katz recalls reference divergence skewing results in a student project, though he was unsure whether the threshold was about 15,000 or 50,000 SNPs; another host recommends an outbreak reference when investigating mobile genetic elements within that outbreak.
- q: How do the hosts compare Galaxy and Nextflow?
  a: Galaxy is described as more point-and-click, while Nextflow feels more like programming and requires more crafting of workflows. One host particularly values Nextflow's ability to integrate separate containers for individual tools, while acknowledging that this complexity can discourage users.
---

*What bioinformatics software not to write: part 1*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss areas of microbial bioinformatics where writing another tool may offer little benefit. In this episode, released in September 2019, they compare established options for alignment, assembly, read mapping, variant calling, workflows and phylogenetics. Their argument is that understanding existing software, choosing suitable data and adjusting parameters can be more useful than starting a competing implementation.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 1: What bioinformatics software not to write part 1" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/679961927&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 1: What bioinformatics software not to write part 1 on SoundCloud](https://soundcloud.com/microbinfie/what-software-not-to-write-1)

## In this episode

### Recognising peak bioinformatics

The hosts propose several reasons not to write new software: many suitable tools already exist, a problem is effectively solved or demonstrably unsolvable, or the underlying technology has been superseded. They frame this as a casual literature review, while allowing that a specific use case can still justify development. Assigning a PhD student another assembler or mapper without first examining existing work is their opening example of wasted effort.

Microarrays illustrate the risk of working on a technology's long tail. One host describes major sequencing centres moving towards RNA-seq around 2009–2010, yet cites 82,000 microarray papers in 2014 and 42,000 in 2018. These figures support that host's warning about continued software development after a technological shift, rather than a recommendation based simply on publication volume.

### Sequence alignment is not whole-genome alignment

For multiple sequence alignment, the hosts point to MAFFT and MUSCLE as established choices. They describe alignment as an old computer-science problem with many existing implementations, leaving limited room for a new general-purpose method. Their advice is to establish what existing algorithms already provide before attempting another implementation.

A practical distinction matters more than tool novelty: aligning genes or other short sequences is not the same problem as aligning whole genomes. Katz recalls people trying to align entire genome assemblies with MUSCLE and then asking why their analysis hangs. The hosts name Mauve, Sibelia and Mugsy as whole-genome alternatives with different constructions. Katz also recommends considering Parsnp in the Harvest package, which another host identifies as a comparatively recent, widely used option.

### Assemblers, versions and sequencing chemistry

Katz introduces the 2011 PLoS ONE paper *A Practical Comparison of De Novo Genome Assembly Software Tools for Next-Generation Sequencing Technologies*. The discussion contrasts continuing use of SPAdes and Velvet with SKESA, described as a 2018 release from NCBI. One host notes that Velvet remains embedded in pipelines despite limited recent development and difficulty handling longer Illumina reads.

For long-read assembly, the hosts discuss HGAP, Flye, Canu, Ra and Unicycler. One reports experience with thousands of HGAP assemblies and corresponding Canu assemblies, preferring Canu; the same host finds Unicycler very good for bacteria. These are accounts of their experience, not a controlled ranking.

Benchmarking also changes with software versions and parameters. They recall a SPAdes blog post responding to better results from SKESA and Shovill: parameter adjustments brought results closer together. Their broader point is that data quality, settings and ongoing maintenance complicate claims that a new assembler fundamentally outperforms existing tools.

### Mapping and SNP calls depend on the reference

The hosts describe short-read mapping as a mature area, naming BWA, Bowtie2, BBtools, BLAST and SMALT. SMALT prompts discussion of how an unpublished tool can be used widely yet still face adoption barriers. They also cite a blog post favouring BWA for short reads and Minimap2 for long reads, presenting this as guidance available at the time of recording.

Variant calling follows a similar argument: existing options include Snippy, the PHEnix pipeline using GATK, VIPR and VarScan2. Katz explains that the variant caller he originally used for the Haiti cholera outbreak did not give a base call at every site, only variant calls, so he chose VarScan2 for his polished pipeline instead.

The hosts stress filtering, coverage settings and reference selection over writing another caller. Katz recalls a project with a student at a Virginia public-health laboratory where reference divergence skewed SNP results, though he was unsure whether the threshold was about 15,000 or 50,000 SNPs. For investigating mobile genetic elements in an outbreak, one host recommends using a reference from that outbreak.

### Use workflow managers and existing parsers

Workflow managers provide the glue between analysis tools. One host recalls working for years on bespoke software used by only one organisation, contrasting that experience with established options such as Snakemake, Nextflow and Galaxy. Galaxy is praised for its point-and-click interface; Nextflow is described as more programming-oriented, offering flexibility at the cost of greater complexity. The hosts characterise these systems as specifying expected inputs, expected outputs and commands between them.

Nextflow's container integration receives particular attention, including the ability to put individual tools in separate containers. Katz mentions its use by the European INNUENDO project and reports that some colleagues at CDC use Bpipe, described here as a Java-based command-line workflow system.

The same reuse principle applies to file parsers. Existing libraries handle formats such as FASTQ and BLAST results, including awkward edge cases such as split FASTQ lines. A faster handwritten parser may omit precisely those checks.

### Phylogenetics and specialised optimisation

For phylogenetic inference, the hosts discuss RAxML, IQ-TREE, FastTree, BEAST and RevBayes. They see a crowded field supported by substantial specialist groups, and describe IQ-TREE as increasingly replacing FastTree in their experience. Their argument concerns the difficulty of competing with mature, maintained implementations, rather than denying that a particular research question could need something different.

RAxML illustrates the engineering involved: one host praises builds targeting different processor instruction sets to make better use of Intel and AMD hardware. The conversation then moves to optimisation of BWA-MEM and commercial FPGA boards for alignment. Reimplementing algorithms for such hardware requires expertise well beyond an ordinary single-student software project, reinforcing the episode's warning against casually reinventing established tools.

## Highlights

- [00:00:19](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=0:19) — The hosts introduce criteria for deciding when new bioinformatics software is unnecessary.
- [00:02:45](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=2:45) — Microarrays illustrate the long tail of research after a shift in sequencing technology.
- [00:04:19](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=4:19) — Established alignment methods and the limited case for another general-purpose aligner.
- [00:05:27](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=5:27) — Why multiple sequence alignment differs from whole-genome alignment.
- [00:06:54](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=6:54) — A 2011 assembly comparison introduces SPAdes, Velvet and SKESA.
- [00:08:08](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=8:08) — Moving from Illumina assembly to long-read tools such as HGAP, Flye, Canu and Unicycler.
- [00:11:37](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=11:37) — SMALT's different mapping method and the adoption barrier of an unpublished tool.
- [00:13:44](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=13:44) — Katz explains why wanting calls at every site led him towards VarScan2.
- [00:14:56](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=14:56) — Choosing a close reference can improve SNP calls more than changing the caller.
- [00:16:44](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=16:44) — Workflow managers replace bespoke glue code: Snakemake, Nextflow and Galaxy.
- [00:19:43](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=19:43) — Existing file-parsing libraries handle edge cases that handwritten parsers can miss.
- [00:20:41](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=20:41) — Phylogenetics as a mature field with substantial specialist software-development teams.

## In their own words

> Just to be clear, multiple sequence alignment is a different problem to whole genome alignment.
>
> — one of the hosts, [00:05:27](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=5:27)

> But ultimately, right, it all comes down to how good your data is.
>
> — one of the hosts, [00:08:45](https://soundcloud.com/microbinfie/what-software-not-to-write-1#t=8:45)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

MAFFT, MUSCLE, Mauve, Sibelia, Mugsy, Parsnp, Harvest, SPAdes, Velvet, SKESA, HGAP, Flye, Canu, Ra, Unicycler, Shovill, BWA, BWA-MEM, Bowtie2, BBtools, BLAST, SMALT, Minimap2, Snippy, PHEnix, GATK, VIPR, VarScan2, Snakemake, Nextflow, Galaxy, Bpipe, RAxML, IQ-TREE, FastTree, BEAST, RevBayes.

## Questions this episode answers

### When do the hosts advise against writing a new bioinformatics tool?

When many suitable tools already exist, the problem is effectively solved or unsolvable, or the underlying technology has been superseded. They still allow for specific use cases, but recommend examining existing work before starting another implementation.

### Which tools does the episode distinguish for sequence and whole-genome alignment?

The hosts discuss MAFFT and MUSCLE for multiple sequence alignment of shorter sequences such as genes. For whole genomes, they name Mauve, Sibelia, Mugsy and Parsnp, warning against treating these as the same alignment problem.

### Why does reference selection matter for bacterial SNP calling?

The hosts argue that a reference close to the data can improve SNP calls substantially. Katz recalls reference divergence skewing results in a student project, though he was unsure whether the threshold was about 15,000 or 50,000 SNPs; another host recommends an outbreak reference when investigating mobile genetic elements within that outbreak.

### How do the hosts compare Galaxy and Nextflow?

Galaxy is described as more point-and-click, while Nextflow feels more like programming and requires more crafting of workflows. One host particularly values Nextflow's ability to integrate separate containers for individual tools, while acknowledging that this complexity can discourage users.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode we identify areas of “Peak-bioinformatics”. There are a lot of existing bioinformatics software out there - more often than not the new tool you want to write already exists or a new tool cannot effectively improve. We discuss this in terms of genome assembly, read mapping and phylogenetics.

Question and comments? microbinfie@gmail.com

## SHOW NOTES

Generally, novel software is not needed if:
There are a plethora of existing tools
The problem is more or less solved or its been shown to be unsolvable
The underlying technology or problem is now obsolete and/or superceded by other methods.

Multiple sequence aligners:

- MAFFT https://mafft.cbrc.jp/alignment/software/
- MUSCLE https://www.drive5.com/muscle/
- Whole genome aligners:
- Mauve http://darlinglab.org/mauve/mauve.html
- Mugsy http://mugsy.sourceforge.net/
- Sibellia http://bioinf.spbau.ru/sibelia
- Parsnp https://github.com/marbl/parsnp

Assemblers:

- SPADES https://github.com/ablab/spades
- Skesa https://github.com/ncbi/SKESA
- Velvet https://www.ebi.ac.uk/~zerbino/velvet/
- Abyss https://github.com/bcgsc/abyss
- Edena http://www.genomic.ch/edena.php
- Ray http://denovoassembler.sourceforge.net/

Long read assemblies

- HGAP https://github.com/PacificBiosciences/Bioinformatics-Training/wiki/HGAP-2.0
- Flye https://github.com/fenderglass/Flye
- Canu https://github.com/marbl/canu
- Ra https://www.biorxiv.org/content/10.1101/656306v1
- Unicycler https://github.com/rrwick/Unicycler

Read mapping

- BWA http://bio-bwa.sourceforge.net/
- Bowtie2 http://bio-bwa.sourceforge.net/
- Minimap2 https://github.com/lh3/minimap2 (BWA better for short reads: https://lh3.github.io/2018/04/02/minimap2-and-the-future-of-bwa)
- BBtools https://jgi.doe.gov/data-and-tools/bbtools/
- BLAST/BLAT: https://genome.ucsc.edu/FAQ/FAQblat.html
- SMALT https://www.sanger.ac.uk/science/tools/smalt-0
- Snippy https://github.com/tseemann/snippy
- Phenix: https://github.com/phe-bioinformatics/PHEnix

Variant callers

- GATK: https://software.broadinstitute.org/gatk/
- VIPR: https://www.viprbrc.org/brc/home.spg?decorator=vipr
- Varscan2 http://varscan.sourceforge.net/

Workflow managers

- Bespoke example https://github.com/VertebrateResequencing/vr-codebase
- Snakemake. https://snakemake.readthedocs.io/en/stable/
- Nextflow https://www.nextflow.io/
- Galaxy https://usegalaxy.org/
- Bpipe https://github.com/ssadedin/bpipe

Phylogenetics:

- Raxml - Raxml-NG https://cme.h-its.org/exelixis/software.html
- IQTREE http://www.iqtree.org/
- FastTree http://www.microbesonline.org/fasttree/
- BEAST 1&amp;2 https://www.beast2.org/
- RevBayes https://revbayes.github.io/

Metagenomics

- Taxonomic classification: Megan, Kraken, SIGMA, MIDAS, metaphlan2, mOTUs.
- Assemblers: MetaSpades, metaflye, MEGAHIT, MetaVelvet, a lot of single isolate assemblers have been tweaked to run on metagenomes. https://github.com/lskatz/Kalamari

AMR

- https://github.com/arpcard/amr_curation
- https://food-safety-bioinformatics-hackathon.github.io/AMR-protocols/
- ABRICATE https://github.com/tseemann/abricate
- ARIBA https://www.sanger.ac.uk/science/tools/ariba
- Too many detection tools: https://docs.google.com/spreadsheets/d/18XGWpDiaE249qQKDAL7gdBCka0Z1drpA_s3FElfMJe0/edit#gid=0

### Other mentioned resources

- Mentioned Recent review. Zhang et al. (2011) A Practical Comparison of De Novo Genome Assembly Software Tools for Next-Generation Sequencing Technologies. PLoS ONE 6(3): e17915. https://doi.org/10.1371/journal.pone.0017915
- The Assemblerthon: https://assemblathon.org/
- Blog post describing that BWA better for short reads: https://lh3.github.io/2018/04/02/minimap2-and-the-future-of-bwa
- The science web: https://thescienceweb.wordpress.com/2015/03/23/each-bioinformatician-to-have-their-own-personal-short-read-aligner-by-2016/
