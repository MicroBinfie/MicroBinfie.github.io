---
layout: page
title: 'Episode 123: The Revolution of Hash Databases in cgMLST'
date: '2024-03-21 00:00:00'
link: https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst
episode: '123'
soundcloud_track: '1770026592'
tags:
- microbinfie
- podcast
description: Lee Katz and Andrew Page discuss hash-based cgMLST allele naming, collision tests, exact matching and decentralised database standards.
excerpt: Lee Katz and Andrew Page discuss hash-based cgMLST allele naming, collision tests, exact matching and decentralised database standards.
headline: Hash-based allele names for decentralised cgMLST databases
guests: []
topics:
- microbial bioinformatics
- cgmlst
- allele identification
- hash databases
- hash collisions
- database synchronisation
- genomic surveillance
- sequence types
- decentralised databases
faq:
- q: Why use hashes instead of integer allele numbers in cgMLST?
  a: Separate databases can assign different integer names to the same allele. Hashing the sequence provides a way for institutions to calculate the same identifier independently, making synchronisation easier.
- q: Did Katz find collisions with MD5 or SHA-256?
  a: He reports finding no collisions with either algorithm in the MLST databases he tested or in a Salmonella database expanded to eleven times its original size using random mutations. CRC32 did produce collisions.
- q: Which organisms were included in the hash tests?
  a: Katz names Salmonella, E. coli, Listeria and Campylobacter among the whole-genome MLST and cgMLST databases he tested. He used Salmonella for the expanded mutation experiment because it was the largest database he could find.
- q: Can hashing also create decentralised sequence-type identifiers?
  a: Katz's specification includes hashing the allele hashes to identify a sequence type. The hosts note that long hash identifiers are awkward to communicate, and Katz says decentralising allele codes remains unresolved.
- q: Who might maintain the hash-database specification?
  a: Katz discusses Phage, GMI and PulseNet International as possible homes. He says the specification was made for PulseNet International, but no adoption decision is announced.
---

*Hash-based allele names for decentralised cgMLST databases*

Lee Katz and Andrew Page discuss using sequence hashes to name alleles consistently across separate MLST and cgMLST databases. Katz describes collision tests, changes needed in allele-calling software and a specification for hashing allele profiles. They also examine what remains unresolved: readable sequence-type names, quality control and community ownership of a shared standard.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 123: The Revolution of Hash Databases in cgMLST" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1770026592&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 123: The Revolution of Hash Databases in cgMLST on SoundCloud](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst)

## In this episode

### The same allele, different numbers

Katz starts with a practical frustration: separate MLST databases can assign different integer identifiers to the same allele. A database in England and another in the United States might each accumulate genomes and increment their allele numbers independently. Both can contain the same genetic sequences without sharing a naming system, complicating comparisons for genomic surveillance and population-structure studies.

The proposed alternative is to calculate an identifier from the allele sequence itself. If two institutions hash the same sequence using the same method, they can obtain the same identifier without coordinating the next available number. Katz sees this as especially useful for groups that lack the funding or system support needed to keep conventional databases synchronised.

### Testing CRC32, MD5 and SHA-256

The attraction of hashing is that even a single nucleotide polymorphism changes the resulting hash. That fits allele-based typing, where a sequence difference means a different allele. The complication is a collision: two different sequences can produce the same hash. Page introduces MD5 and the birthday-attack idea while discussing why collisions remain a consideration.

Katz reports testing whole-genome MLST and cgMLST databases covering Salmonella, E. coli, Listeria and Campylobacter. CRC32 produced collisions, whereas he found none with MD5 or SHA-256. To test a larger collection, he took the largest database available to him, Salmonella, and generated ten randomly mutated versions per allele. This made a database eleven times the original size; CRC32 again produced collisions, while MD5 and SHA-256 did not.

A collision could make genuinely different alleles appear identical, contributing zero rather than one to a locus-level distance. These are reported experimental results, not a claim that collisions are impossible.

### What allele callers would need to change

Katz contrasts exact hash comparisons with the looser sequence matching available through BLAST and other approaches used by MLST software. With hashes, a one-base difference changes the identifier rather than producing a partly matching result. He tried generating multiple hashes per allele to support a looser comparison, but says the approach became too complicated and produced a large database without solving the problem usefully.

He identifies eToKi as a caller that could work with the approach and mentions another caller still being tried out, whose name and availability he could not confirm. He also discusses chewieSnake, described as a hash-based version of chewBBACA from colleagues in Germany, while expressing concern about its use of CRC32. Checking Git history, he found that Torsten had added allele hashing to his seven-gene MLST work five years earlier.

### Sequence types and allele codes

Hashing individual alleles does not settle how to name their combinations. Katz gives the example of two databases assigning sequence type 10 and sequence type 30 to the same profile. His specification therefore includes a method for hashing the allele hashes to create a sequence-type identifier. Page points out the communication problem: a long hash is harder to discuss with a medic than a small integer.

Katz also argues that sequence types are less useful for cgMLST than for seven-gene MLST because almost every genome can yield a new type. He introduces allele codes, described in a Stevens et al. paper from a couple of years earlier. He confirms that the idea was copied from SNP addresses, but says he does not yet know how to decentralise it. Consistent allele identifiers are presented as a first step, not a complete decentralised typing system.

### Quality control and ownership of the standard

Page asks whether allowing anyone to generate allele hashes could pollute databases. He contrasts this with centralised systems that have gatekeepers, verification and validation. Later, he notes that submitting alleles can involve waiting for acceptance or being asked for Sanger sequencing, while applying comparable checks across cgMLST's many genes is difficult.

The discussion ends with stewardship. Page asks whether a specification held in Katz's personal GitHub account would have greater longevity under an international organisation. Katz names Phage, GMI and PulseNet International as possible homes, explaining that he made the specification for PulseNet International. These are possibilities rather than announced adoption plans: Katz describes the conversation as brainstorming about who might maintain and develop the work.

## Highlights

- [00:00:43](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=0:43) — Andrew Page introduces the discussion of hash databases with Lee Katz.
- [00:01:14](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=1:14) — Siloed MLST databases can give the same allele different integer identifiers.
- [00:03:42](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=3:42) — MD5 introduces the discussion of hash collisions and birthday attacks.
- [00:06:26](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=6:26) — Katz describes CRC32 collisions and their possible effect on allele distances.
- [00:07:45](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=7:45) — Tests cover four organism groups and an elevenfold-expanded Salmonella database.
- [00:09:48](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=9:48) — Allele submission, acceptance and quality-control barriers in existing databases.
- [00:10:29](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=10:29) — Exact hash matching changes software requirements for allele callers.
- [00:12:40](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=12:40) — How sequence-type identifiers might be allocated from collections of allele hashes.
- [00:14:21](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=14:21) — Why cgMLST sequence types are less useful than seven-gene MLST types.
- [00:15:32](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=15:32) — Whether a community organisation should maintain Katz's specification.
- [00:15:57](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=15:57) — Phage, GMI and PulseNet International are discussed as possible organisational homes.

## In their own words

> And so that would be a unique identifier that if I found it and you found it in your institution, we'd have the same identifier and we could synchronize our databases much more easily.
>
> — Lee Katz, [00:01:14](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=1:14)

> I'm looking for a parent to adopt me on this specification.
>
> — Lee Katz, [00:15:57](https://soundcloud.com/microbinfie/123-hash-databases-for-cgmlst#t=15:57)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)

Also mentioned: Nabil-Fareed Alikhan, Torsten.

## Tools and resources mentioned

MLST, cgMLST, whole-genome MLST, CRC32, MD5, SHA-256, BLAST, eToKi, chewBBACA, chewieSnake, Git, GitHub, Sanger sequencing, allele codes, SNP addresses.

## Questions this episode answers

### Why use hashes instead of integer allele numbers in cgMLST?

Separate databases can assign different integer names to the same allele. Hashing the sequence provides a way for institutions to calculate the same identifier independently, making synchronisation easier.

### Did Katz find collisions with MD5 or SHA-256?

He reports finding no collisions with either algorithm in the MLST databases he tested or in a Salmonella database expanded to eleven times its original size using random mutations. CRC32 did produce collisions.

### Which organisms were included in the hash tests?

Katz names Salmonella, E. coli, Listeria and Campylobacter among the whole-genome MLST and cgMLST databases he tested. He used Salmonella for the expanded mutation experiment because it was the largest database he could find.

### Can hashing also create decentralised sequence-type identifiers?

Katz's specification includes hashing the allele hashes to identify a sequence type. The hosts note that long hash identifiers are awkward to communicate, and Katz says decentralising allele codes remains unresolved.

### Who might maintain the hash-database specification?

Katz discusses Phage, GMI and PulseNet International as possible homes. He says the specification was made for PulseNet International, but no adoption decision is announced.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie Podcast, hosts Dr. Andrew Page and Dr. Lee Katz delve into
the fascinating world of hash databases and their application in cgMLST (core genome Multilocus
Sequence Typing) for microbial bioinformatics.

The discussion begins with the challenges faced by bioinformaticians due to siloed MLST
databases across the globe, which hinder synchronization and effective genomic surveillance. To
address these issues, the concept of using hash databases for allele identification is
introduced. Hashing allows for the creation of unique identifiers for genetic sequences,
enabling easier database synchronization without the need for extensive system support or
resources.

Dr. Katz explains the principle of hashing and its application in genomics, where even a single
nucleotide polymorphism (SNP) can result in a different hash, making it a perfect solution for
distinguishing alleles. Various hashing algorithms, such as MD5 and SHA-256, are discussed,
along with their advantages and potential risks of hash collisions. Despite these risks, the
use of more complex hashes has been shown to significantly reduce the probability of such
collisions.

The episode also explores practical aspects of implementing hash databases in bioinformatics
software, highlighting the need for exact matching algorithms due to the nature of hashing.
Existing tools like eToKi and upcoming software are mentioned as examples of applications that
can utilize hash databases.

Furthermore, the conversation touches on the concept of sequence types in cgMLST and the
challenges associated with naming and standardizing them in a decentralized database system.
Alternatives like allele codes are mentioned, which could potentially simplify the
representation of sequence types.

Finally, the potential for adopting this hashing approach within larger bioinformatics
organizations like Phage or GMI is discussed, with an emphasis on the need for a standardized
and community-supported framework to ensure the longevity and effectiveness of hash databases
in microbial genomics.

This episode provides a comprehensive overview of how hash databases can revolutionize
microbial genomics by solving long-standing issues of database synchronization and allele
identification, paving the way for more efficient and collaborative genomic surveillance
worldwide.
