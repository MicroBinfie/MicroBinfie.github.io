---
date: 2019-09-19 00:00:00
title: MicroBinfie Podcast, 01 What bioinformatics software not to write part 1
link: https://soundcloud.com/microbinfie/what-software-not-to-write-1
layout: page
tags:
  - microbinfie
  - podcast
---

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

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/679961927&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/microbinfie" title="Micro Binfie Podcast" target="_blank" style="color: #cccccc; text-decoration: none;">Micro Binfie Podcast</a> · <a href="https://soundcloud.com/microbinfie/40-a-crash-course-in-sars-cov-2-bioinformatics" title="01 What bioinformatics software not to write part 1" target="_blank" style="color: #cccccc; text-decoration: none;">40 A crash course in SARS-CoV-2 bioinformatics</a></div>
