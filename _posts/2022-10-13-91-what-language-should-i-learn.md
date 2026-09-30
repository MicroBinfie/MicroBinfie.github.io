---
layout: page
title: 'Episode 91: What language should I learn?'
date: '2022-10-13 00:00:00'
link: https://soundcloud.com/microbinfie/91-what-language-should-i-learn
episode: '91'
soundcloud_track: '1284484477'
tags:
- microbinfie
- podcast
description: Python, R, Perl or SQL? Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss where to start and why libraries and local support matter.
excerpt: Python, R, Perl or SQL? Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss where to start and why libraries and local support matter.
headline: Which programming language should you learn for bioinformatics?
guests: []
topics:
- bioinformatics
- programming languages
- python
- r
- sql
- data visualisation
- software libraries
- programming education
- query optimisation
faq:
- q: What programming language should I learn first for bioinformatics?
  a: The hosts recommend Python as a strong general-purpose starting point because of its consistency, established libraries and usefulness for learning fundamentals. They also advise considering the languages used by people who can help you and the requirements of your project.
- q: Why learn R if the hosts find it frustrating?
  a: They value R for statistics and figures, particularly libraries such as ggplot2 and ggtree. Their frustrations concern its syntax, competing programming styles and inconsistent library conventions rather than the usefulness of its outputs.
- q: Why avoid a trendy language as a beginner?
  a: The hosts warn that a newer or less commonly used language may lack established bioinformatics libraries, leaving beginners to write parsers themselves. Frequent changes can also make tutorials stop working before a learner has enough experience to diagnose the problem.
- q: Is SQL worth learning for bioinformatics?
  a: The hosts find SQL useful both directly and as a way to understand structured data, keys and relationships between tables. Andrew’s example of a database with tens of millions of rows per table illustrates how indexing and query optimisation can determine whether lookups take milliseconds or seconds.
---

*Which programming language should you learn for bioinformatics?*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan revisit their episode 13 discussion about learning programming languages for bioinformatics. They recommend Python as a strong starting point, while stressing that projects, colleagues and available libraries should influence the choice. Their conversation covers R for statistics and figures, Perl for quick scripts, SQL for understanding data, and why becoming proficient takes much longer than completing an introductory course.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 91: What language should I learn?" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1284484477&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 91: What language should I learn? on SoundCloud](https://soundcloud.com/microbinfie/91-what-language-should-i-learn)

## In this episode

### Start with Python, but consider your surroundings

Andrew proposes a learning sequence: Python first, then R, followed by languages such as C, C++, C# or Java. His reasoning is that scripting, statistical analysis and heavy-duty programming fill different needs. He recommends developing substantial competence before moving into languages he describes as trendy, including Rust, Haskell, Go and Ruby.

The discussion also makes room for a less prescriptive approach. Someone learning through tutorials rather than a formal course should consider what nearby colleagues use and who can help. A web application may call for different choices from a statistical analysis. Understanding conditionals, loops and other programming fundamentals makes subsequent languages easier to learn. Lee favours Python for general-purpose collaborative work, despite his personal enthusiasm for Perl: teams and shared code on GitHub matter more than choosing a language in isolation.

### Learning syntax is not the same as gaining expertise

The hosts reached bioinformatics through different routes. Lee began with a college course in C, moved into PHP and the LAMP stack for web development, and learned Perl in graduate school in 2004. Andrew studied software engineering, starting with C++ and Java before working with several other languages, including Perl, PHP and Ruby with Rails. Nabil began mainly with Java and spent a year using Perl for his first bioinformatics research project because that was what the laboratory used, later switching to Python.

Andrew distinguishes introductory syntax from knowing a language’s frameworks, libraries and quirks. He suggests that even an experienced programmer may need a year or two to develop in-depth knowledge of another language. Lee estimates that becoming really good at Perl took him about five years, despite already knowing PHP.

### R’s useful libraries and frustrating inconsistencies

R earns a place for statistics, data manipulation and figures, but the hosts describe considerable frustration with it. Andrew uses it infrequently enough that he has to relearn parts each time; modifying existing code is easier for him than remembering how to write everything afresh. His quick-script preference is Perl, or Python when he expects to reuse the code.

Nabil singles out ggplot2 and ggtree as exceptionally useful libraries whose visualisations would otherwise require substantial work from scratch. His complaint is that R offers different programming styles within the same analysis, while libraries use inconsistent conventions. Python’s more consistent style is presented as an advantage for learning and collaboration, although the hosts acknowledge its own alternative approaches, including list comprehensions and several ways of formatting strings. Nabil sees Python as striking a balance: it avoids too much ambiguity without burdening the programmer with extra verbosity, such as specifying types all the time.

### Established parsers beat starting from scratch

Lee advises beginners against choosing a new language solely because it is fashionable. Established bioinformatics libraries let researchers concentrate on their work instead of writing basic infrastructure. He recalls writing bioinformatics code in PHP and JavaScript, and warns against becoming the person who must build the first FASTA parser in a language. FASTQ, SAM and VCF add further demands.

Andrew distinguishes reading a file you produced yourself from handling files produced by thousands of people. His FASTQ examples include a Nanopore read a million bases long and records spread across more than four lines. Nabil has written GenBank parsers in three languages, but says they worked for his particular tasks rather than as general solutions. Rapidly changing languages introduce another beginner trap: tutorials only six months or a year old may no longer work, and inexperienced programmers may struggle to recognise a version mismatch.

### Shell scripts, web applications and laboratory robots

The hosts discuss languages beyond their main analysis workflows. Lee defends shell scripting as a legitimate programming language whose priority is making system calls. For web development, they distinguish JavaScript from Java and compare experiences with jQuery, Prototype and React. Nabil describes older JavaScript work as difficult after a Java background, while finding newer approaches more comfortable.

Python’s usefulness also extends to laboratory hardware. Andrew describes a laboratory technician writing Python scripts for an Opentrons liquid-handling robot and getting it working within a few hours. The hosts nevertheless identify limits: Nabil finds Python frustrating for multithreading, and Andrew describes low-level optimisation and GPU programming with CUDA as specialist work. The broader point is that an accessible starting language does not remove the need for other tools or expertise when performance requirements change.

### SQL teaches useful ways to think about data

The database discussion focuses on concepts as much as syntax: primary keys, unique fields and relationships between tables. Nabil has used SQL more than he expected and argues that understanding data structure is valuable even when an interface handles database interaction. Lee continues to use SQL and values SQLite’s portability, while describing it as slower.

Andrew recalls building a search engine for a social network during his PhD, with tens of millions of rows in each table and a small, inexpensive server. Multi-table joins, indexing and careful query optimisation mattered because web-page lookups needed to take milliseconds rather than seconds. Nabil connects that experience to everyday problem-solving: deciding which collection to search first and how to cross-check results. Database knowledge is presented as a broadly useful skill, not merely preparation for creating a database.

## Highlights

- [00:01:04](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=1:04) — Andrew’s suggested learning order: Python, R, then C-family languages or Java
- [00:03:18](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=3:18) — Choosing a language around local support and the project you want to build
- [00:05:57](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=5:57) — The hosts compare their routes into programming
- [00:07:49](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=7:49) — Why introductory syntax is different from mastering libraries and frameworks
- [00:09:34](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=9:34) — Lee makes the case for shell scripting as a programming language
- [00:10:18](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=10:18) — Web languages and the distinction between JavaScript and Java
- [00:13:52](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=13:52) — R’s valuable plotting libraries and inconsistent ways of working
- [00:17:37](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=17:37) — Programming an Opentrons liquid-handling robot with Python
- [00:19:01](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=19:01) — Python as a starting point for learning programming fundamentals
- [00:20:15](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=20:15) — Why beginners benefit from established languages and file-parsing libraries
- [00:24:59](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=24:59) — SQL, primary keys and relationships between tables
- [00:26:36](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=26:36) — Optimising SQL queries across tables with tens of millions of rows

## In their own words

> We work with teams, we work on GitHub, which is inherently collaborative.
>
> — Lee Katz, [00:04:49](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=4:49)

> If you know the fundamentals, you can program in any language.
>
> — Nabil-Fareed Alikhan, [00:19:01](https://soundcloud.com/microbinfie/91-what-language-should-i-learn#t=19:01)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Python, R, Perl, C, C++, C#, Java, SQL, Bash, PHP, JavaScript, Rust, Haskell, Go, Ruby, Rails, LAMP, GitHub, ggplot2, ggtree, jQuery, Prototype, React, Opentrons, CUDA, SQLite, MySQL, Hadoop, Roary.

## Questions this episode answers

### What programming language should I learn first for bioinformatics?

The hosts recommend Python as a strong general-purpose starting point because of its consistency, established libraries and usefulness for learning fundamentals. They also advise considering the languages used by people who can help you and the requirements of your project.

### Why learn R if the hosts find it frustrating?

They value R for statistics and figures, particularly libraries such as ggplot2 and ggtree. Their frustrations concern its syntax, competing programming styles and inconsistent library conventions rather than the usefulness of its outputs.

### Why avoid a trendy language as a beginner?

The hosts warn that a newer or less commonly used language may lack established bioinformatics libraries, leaving beginners to write parsers themselves. Frequent changes can also make tutorials stop working before a learner has enough experience to diagnose the problem.

### Is SQL worth learning for bioinformatics?

The hosts find SQL useful both directly and as a way to understand structured data, keys and relationships between tables. Andrew’s example of a database with tens of millions of rows per table illustrates how indexing and query optimisation can determine whether lookups take milliseconds or seconds.

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
