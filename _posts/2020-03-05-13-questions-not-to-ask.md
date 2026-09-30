---
layout: page
title: 'Episode 13: Questions not to ask'
date: '2020-03-05 00:00:00'
link: https://soundcloud.com/microbinfie/13-questions-not-to-ask
episode: '13'
soundcloud_track: '719280634'
tags:
- microbinfie
- podcast
description: The hosts compare Perl, Python and newer languages for bioinformatics, weighing readable code, performance, community support and maintenance.
excerpt: The hosts compare Perl, Python and newer languages for bioinformatics, weighing readable code, performance, community support and maintenance.
headline: Perl or Python? Choosing a language for bioinformatics
guests: []
topics:
- bioinformatics
- programming languages
- perl
- python
- software maintenance
- concurrency
- software performance
- community software
- automation
faq:
- q: Should a bioinformatics beginner learn Perl or Python?
  a: The hosts see the community moving towards Python and describe it as a versatile starting point. They also stress transferable programming concepts, readable code and the languages used by the people around you, rather than declaring Perl unusable.
- q: Why do the hosts recommend Python 3 rather than Python 2?
  a: They discuss Python 2's end of support and the risks for software left unmaintained after research projects finish. Earlier dependency gaps had discouraged migration, but one host says they no longer find modules that are not Python 3 ready.
- q: How can Python code approach C performance?
  a: The episode points to Cython and to NumPy and SciPy, whose underlying numerical code runs in C. One host recounts a colleague producing a Cython version that was as fast as their handcrafted C implementation.
- q: Is it always worth automating a bioinformatics task?
  a: 'No: the hosts compare implementation time with task frequency and the time saved each run. They also note that a small recurring saving across an entire community can justify automation that would not be worthwhile for one person alone.'
---

*Perl or Python? Choosing a language for bioinformatics*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss why asking which programming language to learn produces such complicated answers. Starting with Perl versus Python, they compare libraries, readability, performance and alternatives including Rust, Ruby and Julia. The conversation connects individual preferences with practical questions about maintaining software, hiring developers and deciding what is worth automating.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 13: Questions not to ask" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/719280634&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 13: Questions not to ask on SoundCloud](https://soundcloud.com/microbinfie/13-questions-not-to-ask)

## In this episode

### Learning concepts, not just syntax

Should a bioinformatics beginner learn Perl or Python? The hosts call this a loaded question: experience, local working practices and the problem being solved all influence the answer. Their software-engineering examples emphasise conceptual understanding rather than allegiance to a particular language.

Lee has used Perl since 2004, when graduate students were told to learn it through classes, laboratory work and their projects. Rather than moving to Python, he has concentrated on writing clearer Perl. The hosts agree that no language prevents bad code, and that good programming fundamentals transfer between languages.

### Perl's ecosystem and the argument about decline

The discussion distinguishes hard-to-maintain Perl scripts from engineered software using objects, unit tests and Dist::Zilla for packaging. CPAN is presented as a home for more professional code, rather than a complete picture of bioinformatics scripting.

Lee cites a blog comparing roughly 20–30 daily uploads to CPAN with 700–800 to Python's package repository. He describes competing interpretations: declining development activity, a maturing ecosystem, or developers moving to Python. BioPerl is his main bioinformatics library, with other modules under BioX. Biopython is praised as useful, although one host says it still lacks some BioPerl functionality. Perl 6's renaming to Raku is discussed as a useful distinction from Perl 5.

### Python's strengths and frustrations

The hosts favour Python 3 over Python 2, discussing the end of Python 2 support and the risk posed by abandoned PhD and postdoctoral software. Earlier delays in migrating dependencies are acknowledged, but one host says they no longer encounter modules unavailable for Python 3.

Python's readability, importable scripts and breadth make it attractive as a general-purpose starting point. Examples include plotting, Django web applications and numerical work, although R is held up as stronger for graphs. Lee dislikes some stylistic constraints and raises the global interpreter lock as a threading obstacle; pools and queues enter the discussion as part of managing concurrency.

For speed, the hosts highlight NumPy and SciPy's underlying C code. One recalls spending weeks handcrafting C, only for a colleague's Cython implementation to match its performance.

### Rust, Ruby, Julia and the browser

Lee describes working through Rust's training manual without skipping steps. He finds the learning curve steep but values its strict compilation checks and speed. Writing a FASTQ parser helped him learn, and he mentions his Fasten scripts. He describes Rust's bioinformatics library as still developing.

Other alternatives receive more tentative assessments. One host recalls Ruby and Ruby on Rails as pleasant to use but memory-inefficient for their work. Julia attracts interest for data science, although another recalls needing 4 GB of RAM just to reach its command prompt; the group has little practical experience with it.

JavaScript introduces a different challenge: thinking in events and coordinating data moving between components. The hosts contrast that complexity with typical scripts built around loops and conditional statements, while recognising its concurrency-oriented approach.

### Languages are also a community decision

Developer time, salaries and recruitment complicate purely technical comparisons. One host describes language-dependent salaries ranging from $30,000 to $100,000 a year, alongside temporary demand such as COBOL work around Y2K. Limiting a team's language mix can make hiring and sharing projects easier.

Packaging unfamiliar languages can also burden collaborators, particularly when compilers fail on different architectures. The hosts favour familiar community languages for shared software. Fortran in physics illustrates how communities settle on long-lived choices. They expect bioinformatics' growing software base to make another large language shift slower than the move they observed from Perl to Python.

### When automation is worth the effort

An xkcd comic prompts a final question: will automating a task save more time than writing the automation takes? Frequency and time saved per run matter; sometimes continuing manually is cheaper.

The calculation changes at community scale. A task taking everyone five minutes each week may justify shared automation even when it would not repay one person's effort. The episode closes by recognising that language choice matters, with the community seen as moving towards—or already using—Python.

## Highlights

- [00:01:35](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=1:35) — Why asking whether Perl or Python is better is a loaded question.
- [00:02:49](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=2:49) — Programming experience and fundamentals that transfer between languages.
- [00:05:04](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=5:04) — Lee defends Perl and discusses package-upload figures as evidence of activity.
- [00:06:40](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=6:40) — BioPerl, BioX and the role of language-specific bioinformatics libraries.
- [00:08:07](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=8:07) — Python 2 versus Python 3 and the maintenance risks of unsupported software.
- [00:11:43](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=11:43) — Python's readability and importable scripts, followed by threading frustrations.
- [00:13:22](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=13:22) — A Cython implementation matches weeks of work on handcrafted C.
- [00:14:26](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=14:26) — Lee's experience learning Rust and its strict compilation checks.
- [00:16:42](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=16:42) — Experience with Ruby on Rails and concerns about memory use.
- [00:20:45](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=20:45) — Cheap computer time, costly developer time, salaries and team language choices.
- [00:22:58](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=22:58) — Packaging unfamiliar languages and choosing software others can maintain.
- [00:27:36](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=27:36) — Using an xkcd automation comparison to weigh effort against time saved.

## In their own words

> It's dead, and I keep programming in it, so it must be alive.
>
> — Lee Katz, [00:05:04](https://soundcloud.com/microbinfie/13-questions-not-to-ask#t=5:04)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Perl, Python, Python 2, Python 3, CPAN, Dist::Zilla, BioPerl, BioX, Biopython, Perl 6, Raku, Java, NetBeans, Django, R, NumPy, SciPy, Cython, C, C++, Rust, Fasten, Ruby, Ruby on Rails, Julia, JavaScript, Fortran, Go, PHP, COBOL.

## Questions this episode answers

### Should a bioinformatics beginner learn Perl or Python?

The hosts see the community moving towards Python and describe it as a versatile starting point. They also stress transferable programming concepts, readable code and the languages used by the people around you, rather than declaring Perl unusable.

### Why do the hosts recommend Python 3 rather than Python 2?

They discuss Python 2's end of support and the risks for software left unmaintained after research projects finish. Earlier dependency gaps had discouraged migration, but one host says they no longer find modules that are not Python 3 ready.

### How can Python code approach C performance?

The episode points to Cython and to NumPy and SciPy, whose underlying numerical code runs in C. One host recounts a colleague producing a Cython version that was as fast as their handcrafted C implementation.

### Is it always worth automating a bioinformatics task?

No: the hosts compare implementation time with task frequency and the time saved each run. They also note that a small recurring saving across an entire community can justify automation that would not be worthwhile for one person alone.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Someone asks a simple question like "What programming language should
I learn?", without realising just how difficult it is to answer. We
discuss different programming languages and their use in
Bioinformatics.
