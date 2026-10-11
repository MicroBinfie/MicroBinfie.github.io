---
layout: page
title: 'Encore: What language should I learn?'
date: '2023-06-08 00:00:00'
link: https://soundcloud.com/microbinfie/109-what-language-should-i-learn
episode: ''
soundcloud_track: '1533198916'
tags:
- microbinfie
- podcast
description: Python, R or Perl? The hosts compare first languages, established libraries, programming fundamentals and SQL skills for bioinformatics.
excerpt: Python, R or Perl? The hosts compare first languages, established libraries, programming fundamentals and SQL skills for bioinformatics.
headline: What programming language should you learn for bioinformatics?
guests: []
topics:
- bioinformatics programming
- learning to code
- python
- r
- perl
- software libraries
- sql databases
- query optimisation
faq:
- q: What programming language should I learn first for bioinformatics?
  a: The hosts broadly favour Python for general-purpose work and learning programming fundamentals. Nabil also recommends considering which languages colleagues use and who can help, while Andrew proposes following Python with R and then a statically typed language.
- q: Why do the hosts hesitate to recommend R as a first language?
  a: They recognise R’s value for statistics and visualisation, particularly through ggplot2 and ggtree. Their reservations concern unfamiliar syntax, inconsistent library conventions and the difficulty of developing good programming habits without clearer guidance.
- q: Why choose a language with established bioinformatics libraries?
  a: The hosts argue that beginners should not have to build robust file parsers before tackling their biological work. FASTA, FASTQ, SAM, VCF and GenBank examples illustrate how apparently simple parsing tasks become harder when handling varied files from other people.
- q: Is SQL worth learning for bioinformatics?
  a: The hosts find SQL useful, but emphasise that database concepts matter even without direct SQL use. Primary keys, table relationships, joins and indexing help with organising data and understanding why some queries run much faster than others.
---

*What programming language should you learn for bioinformatics?*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan revisit their episode 13 discussion about which programming languages to learn for bioinformatics. They broadly favour Python as a starting point, while weighing local support, project requirements and the value of established libraries. Their own learning histories show why becoming proficient takes years, and why database concepts and programming fundamentals matter beyond any single language.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Encore: What language should I learn?" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1533198916&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Encore: What language should I learn? on SoundCloud](https://soundcloud.com/microbinfie/109-what-language-should-i-learn)

## In this episode

### A starting language depends on the work and the support

Andrew Page proposes learning Python first, then R, followed by a statically typed language such as C++, C#, Java or C. His reasoning separates three needs: scripting, statistics and figures, and heavier-duty programming. He recommends developing substantial proficiency before branching into other languages.

Nabil-Fareed Alikhan puts more weight on the learner’s environment: which languages do nearby colleagues use, and who is willing to help? Conditionals, loops and other fundamentals transfer between languages, even when syntax changes. Lee Katz also favours Python for general-purpose collaborative work, despite his personal affection for Perl. The intended project matters too: statistical analysis points towards R, while web applications may point towards JavaScript.

### Learning syntax is not the same as becoming proficient

Lee began with C in a college course, moved into PHP and LAMP for web development, and was taught Perl in graduate school, when it was the latest and greatest in 2004. Andrew’s software engineering degree included C++, Java and several other languages before he moved into Perl and PHP; his first job was with Ruby on Rails, followed by Perl, C and Python. Nabil’s undergraduate teaching concentrated on Java; his first bioinformatics research project then required a year of Perl because that was what the laboratory used, before he moved to Python.

These histories span at least a decade, not a few short courses. Andrew suggests that learning a language deeply can take a year or two even for an experienced programmer. Lee estimates that becoming really good at Perl took him about five years after PHP.

### Established libraries save beginners from difficult parsing

The hosts caution against choosing a language simply because it is fashionable. Andrew names Rust, Haskell, Go and Ruby in this discussion, while Lee stresses that the objection is not that newer languages are bad: beginners need established code and bioinformatics libraries. Changing versions can also make tutorials difficult to follow when learners cannot yet diagnose the incompatibility.

Lee uses FASTA, FASTQ, SAM and VCF parsing to illustrate the work that libraries save. Andrew distinguishes reading a file you produced from supporting files made by thousands of people: a FASTQ parser might encounter a million-base Nanopore read or files that break a four-line assumption. Nabil has written GenBank parsers in three languages, but says they were task-specific rather than general solutions.

### Python’s consistency and R’s useful but frustrating libraries

Python appeals to the hosts because its conventions support readable, collaborative code without Java’s verbosity. Nabil particularly values it for teaching how to break a task into steps, with linting and a style guide helping beginners develop maintainable habits. They also discuss list comprehensions and the competing approaches to string formatting, so the praise for consistency is not unqualified.

R prompts more mixed feelings. Nabil values ggplot2 and ggtree, but finds the differing conventions and approaches across R libraries difficult to keep track of. Andrew uses R infrequently enough that he feels he must relearn it each time. For quick scripts he prefers Perl, choosing Python when he expects reuse; another of the hosts also answers Perl when asked about his immediate choice for a task.

### Shell scripts, web development and hardware

The conversation extends beyond the main language shortlist. Lee defends shell scripting as a legitimate programming language, with system calls as its priority. The hosts distinguish JavaScript from Java and discuss web tools including jQuery, Prototype and React. Nabil describes becoming more comfortable with newer JavaScript after finding earlier work with it confusing.

Andrew gives a practical example of Python’s accessibility: a laboratory technician programmed an Opentrons liquid-handling robot within a few hours. That does not make Python suitable for everything. Nabil finds multithreading frustrating, and Andrew discusses the specialist knowledge needed to get maximum performance from machines, extending to GPU programming with CUDA.

### SQL and thinking clearly about data

Nabil argues that understanding primary keys, unique fields and relationships between tables is useful even when a project does not require writing SQL directly. Lee describes continuing to use SQL after graduate school and favours SQLite for portability, while acknowledging speed concerns. He also finds the dominance of SQL across database systems reassuring.

Andrew recalls building a social-network search engine during his PhD, with tens of millions of rows in each table and a small, inexpensive server. Multi-table joins and indexing required careful optimisation so lookups could work in milliseconds rather than seconds. Nabil connects these ideas to everyday searching and cross-checking: understanding how to navigate and compare collections of data is a transferable skill, not merely a database-specific technique.

## Highlights

- [00:01:04](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=1:04) — Andrew proposes Python, then R, then a statically typed language.
- [00:03:18](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=3:18) — Nabil recommends considering local expertise, available help and project goals.
- [00:07:49](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=7:49) — Knowing basic syntax differs from mastering a language and its libraries.
- [00:09:34](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=9:34) — Lee explains shell scripting’s emphasis on system calls.
- [00:12:47](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=12:47) — Andrew discusses relearning R and choosing Perl or Python for scripts.
- [00:13:52](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=13:52) — R’s valuable plotting libraries come with frustratingly varied conventions.
- [00:17:37](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=17:37) — A laboratory technician uses Python to program an Opentrons robot.
- [00:19:01](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=19:01) — Nabil favours Python for teaching programming fundamentals and maintainable code.
- [00:20:15](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=20:15) — Lee advises beginners to prioritise established bioinformatics libraries.
- [00:24:59](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=24:59) — SQL introduces useful concepts for structuring and relating data.
- [00:26:36](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=26:36) — Andrew describes optimising SQL tables containing tens of millions of rows.

## In their own words

> If you know the fundamentals, you can program in any language.
>
> — Nabil-Fareed Alikhan, [00:19:01](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=19:01)

> you don't want to be the one to write the first FASTA parser in this language
>
> — Lee Katz, [00:20:15](https://soundcloud.com/microbinfie/109-what-language-should-i-learn#t=20:15)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Python, R, Perl, C, C++, C#, Java, JavaScript, PHP, Ruby, Rails, Rust, Haskell, Go, SQL, SQLite, Bash, LAMP, ggplot2, ggtree, jQuery, Prototype, React, Opentrons, CUDA.

## Questions this episode answers

### What programming language should I learn first for bioinformatics?

The hosts broadly favour Python for general-purpose work and learning programming fundamentals. Nabil also recommends considering which languages colleagues use and who can help, while Andrew proposes following Python with R and then a statically typed language.

### Why do the hosts hesitate to recommend R as a first language?

They recognise R’s value for statistics and visualisation, particularly through ggplot2 and ggtree. Their reservations concern unfamiliar syntax, inconsistent library conventions and the difficulty of developing good programming habits without clearer guidance.

### Why choose a language with established bioinformatics libraries?

The hosts argue that beginners should not have to build robust file parsers before tackling their biological work. FASTA, FASTQ, SAM, VCF and GenBank examples illustrate how apparently simple parsing tasks become harder when handling varied files from other people.

### Is SQL worth learning for bioinformatics?

The hosts find SQL useful, but emphasise that database concepts matter even without direct SQL use. Primary keys, table relationships, joins and indexing help with organising data and understanding why some queries run much faster than others.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

The MicroBinfie podcast discusses the top programming languages for bioinformatics. Andrew,
Lee, and Nabil agree that Python is a great starting point for its consistency and rigor. Its
strict syntax is ideal for teaching programming fundamentals that are essential in any
language. In contrast, Perl encourages multiple ways of doing the same thing, creating
confusion and difficulties in keeping track of things.

The hosts caution against starting with trendy languages that are constantly changing. Instead,
stick with more established languages like Python, which have established libraries and
concepts that will help you advance more easily. Trendy languages come and go like changing
tides, making them riskier choices. Additionally, they highlight the importance of
understanding databases and their primary keys and unique fields. SQL is useful, particularly
in dealing with large datasets. It is consistent across flavors and unlikely to go away soon.
It takes a lot of skill to optimize queries to work in milliseconds.

The hosts emphasize that the language you choose to learn depends on your individual goals and
environment. For instance, Lee suggests that you should look to who is in your space and what
they are using and who is willing to help you. Once you understand the programming concepts, it
is easier to transfer them to other languages, and it is just a question of understanding the
syntax.

Andrew, Lee, and Nabil also discuss their own trajectories of learning programming languages,
revealing that it takes a long time to become an expert in a language, and it is something that
needs to be appreciated. They highlight the difference between just learning the basics of a
language and really getting into the depths of it and the frameworks and libraries.

The hosts also mention languages that are important to pick up, like SQL and bash scripting,
and languages that are popular for web development, like JavaScript. However, they caution that
JavaScript and Java are not the same thing and that JavaScript has a reputation for being a
weird language.

When asked what language they would choose for a task, Nabil says he would use Perl, Lee
mentions R for stats, while Andrew admits that he has to relearn R every time he comes back to
it and therefore prefers Perl for quick scripts. They also discuss their love-hate relationship
with R, mentioning that while it has useful libraries like GGplot and GGtree, its syntax is
difficult to work with and has separate paradigms of approaching the same problem.

The hosts conclude by acknowledging that there is no one-size-fits-all approach to learning
programming languages. One should choose based on their goals, environment, and personal
preferences. Python is a useful language to learn, even if one is not interested in
bioinformatics. Additionally, they note that the fundamentals of databases and how they work
are crucial to understand and utilized across fields.
