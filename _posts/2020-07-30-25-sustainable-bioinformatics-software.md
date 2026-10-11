---
layout: page
title: 'Episode 25: Sustainable bioinformatics software'
date: '2020-07-30 00:00:00'
link: https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software
episode: '25'
soundcloud_track: '829243711'
tags:
- microbinfie
- podcast
description: The hosts discuss documentation, testing, versioning, licences and funding models for bioinformatics software used in research and public health.
excerpt: The hosts discuss documentation, testing, versioning, licences and funding models for bioinformatics software used in research and public health.
headline: 'Sustainable bioinformatics: testing, documentation and funding'
guests: []
topics:
- software sustainability
- bioinformatics
- documentation
- coding conventions
- reproducibility
- software licensing
- automated testing
- institutional knowledge
- software funding
- public health
faq:
- q: What documentation makes a bioinformatics tool easier to maintain and reuse?
  a: The hosts recommend a usage statement or README explaining parameters, input and output formats, plus a small worked example. They also recommend documenting the laboratory workflow around a tool so that institutional knowledge survives staff changes.
- q: Why does versioning matter for reproducible bioinformatics?
  a: Recording versions makes it possible to retrieve and rerun the code used for an earlier result. The episode connects this with manuscript reproducibility and validation, since changed software can produce different answers from the same data.
- q: How can developers measure software impact beyond citations?
  a: Suggested measures include downloads, installations, GitHub activity, institutional and geographical reach, and examples of research enabled by the tool. Surveys, mailing lists, literature searches and website analytics can help, although decentralised distribution makes exact usage totals difficult.
- q: Can paid support sustain open-source bioinformatics software?
  a: The hosts discuss Ubuntu and Red Hat as examples of free software supported by paid services. They see this as a possible model, but question whether small projects can attract enough paying users and note that users may resist paying even when support takes substantial developer time.
---

*Sustainable bioinformatics: testing, documentation and funding*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss how bioinformatics tools can outlast a single research contract. They cover documentation, coding conventions, versioning, institutional knowledge, licensing and automated testing, before considering how to demonstrate impact and pay for maintenance. The discussion connects everyday development practices with the validation and reliability needed to move academic software into public health and clinical use.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 25: Sustainable bioinformatics software" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/829243711&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 25: Sustainable bioinformatics software on SoundCloud](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software)

## In this episode

### Documentation people can actually use

Documentation is the hosts’ first priority for sustainable software. It needs to serve ordinary users as well as developers: explain parameters, expected inputs and output formats rather than assuming users will work them out. A usage statement or README is a useful starting point, with Read the Docs mentioned as another option. A small worked example helps people understand what to expect and can reveal how a program operates.

One host describes having to inspect source code to discover which spreadsheet columns a tool expected, then guess what those column names meant. Ryan Wick is singled out for good documentation and informative output while his tools run. The practical aim is to make using a tool possible without reverse-engineering it.

### Readable code and consistent conventions

Code organisation can communicate information that would otherwise need explanation. One host defends splitting a package into many clearly named files and classes rather than compressing it into a single script. The example contrasts 50 files with roughly 300 lines in one script: separating responsibilities makes it easier for another developer to find relevant code and fix bugs. Keeping methods below about ten lines is presented as that host’s personal preference, not a universal rule.

The discussion also recommends following the conventions of the language being used, including Python’s PEP 8. Consistent naming and descriptive variables matter; single-letter counters can be appropriate in loops, but obscure names elsewhere make maintenance harder. Hidden changes to objects or variables are criticised because they complicate understanding and debugging.

### Versions, workflows and institutional knowledge

Version numbers let developers return to the code that produced an earlier result. The hosts discuss semantic versioning: the first number signals an interface-breaking change, the middle number adds functionality without breaking that interface, and the final number records a patch or bug fix. Keeping versions in source control allows an earlier release to be retrieved and rerun when someone asks why results have changed.

Tool documentation alone does not preserve a laboratory’s working knowledge. Using samtools as an example, Lee describes documenting the surrounding process: quality control, data handling and the steps connecting one operation to the next. Recording processes and versions helps new staff, returning users and validation work. It also matters when revisiting a manuscript, since rerunning an assembly with different software versions can produce a different answer.

### Explicit licences and a route to contributing

Putting code online and calling it open source is not enough to tell others what they may do with it. The hosts argue for an explicit licence covering modification, redistribution and commercial use. A restriction on commercial use can prevent a company from adopting a tool. GPL version 3, BSD and MIT are named, with one host describing GPL version 3 as their habitual choice. They also note that the employer ultimately determines which licence can be applied.

A contributing document addresses a separate barrier: how someone who likes a package can help maintain it rather than write a replacement. Explaining desired features and how to get involved can support a community around the tool and bring in fixes and additional functionality.

### Testing as repeatable validation

Lee describes adding separate tests for new software functionality and finding that failures quickly reveal what a change has broken. Another host distinguishes unit tests, which check individual methods, from integration testing and broader functional or end-to-end tests. A website purchase flow illustrates how a test can cover a whole sequence of user actions; Cucumber is mentioned in this context.

For substantial software engineering, one host offers a rule of thumb of spending about half the development time writing tests. Test-driven development reverses the usual order: write a failing test, then write the code that makes it pass. Thinking through tests first can improve design and expose edge cases. Constructing unusual input data or mock objects takes effort, but the hosts argue that automated checks repay it by making repeated validation quicker and giving users and developers greater confidence.

### Evidence of use and paying for maintenance

The hosts look beyond paper citations to downloads, installations, GitHub clones, stars and watchers. Packaging services such as Conda and Galaxy can provide usage indicators, but decentralised distribution means there may be no exact total. They also suggest literature searches, surveys, mailing lists and website analytics to discover which institutions use a tool, where users are based and what research it enables.

When grant funding is unavailable, user payments or paid support may help sustain development. Ubuntu and Red Hat illustrate free software paired with paid support, though one host questions whether smaller projects can attract enough paying users. Both academics and commercial users may expect free support, despite the developer’s time having a real cost.

Commercial providers may also undertake the validation, accreditation and platform development needed for clinical deployment. The desired interface is a reliable button, not a bioinformatician in every surgery. Cost remains a concern: one example contrasts a $100,000 annual hire with an $80,000 software price. The episode closes by arguing for funding plans that extend beyond one person’s three-year contract, whether supported by users or funders.

## Highlights

- [00:01:14](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=1:14) — Documentation for developers and ordinary users, including parameters and formats
- [00:03:45](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=3:45) — Code organisation, short methods, descriptive names and language-specific style guides
- [00:07:48](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=7:48) — Semantic versioning and what the three version numbers communicate
- [00:08:43](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=8:43) — Preserving institutional knowledge through documented workflows around tools such as samtools
- [00:10:37](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=10:37) — Why software needs an explicit licence for reuse, modification and distribution
- [00:12:42](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=12:42) — Lee’s experience of using tests to catch breakages and build confidence
- [00:13:28](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=13:28) — Automated validation, testing effort and test-driven development
- [00:16:44](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=16:44) — Measuring software impact beyond citations to justify continued development
- [00:20:03](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=20:03) — User-pays models when external maintenance funding is unavailable
- [00:22:22](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=22:22) — Commercial providers, validation and moving academic tools into clinical use
- [00:25:31](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=25:31) — Longer-term funding beyond a single developer’s contract

## In their own words

> Like every single thing I put in my software now, I make sure that there's a separate script now to test the thing and make sure it works.
>
> — Lee Katz, [00:12:42](https://soundcloud.com/microbinfie/25-sustainable-bioinformatics-software#t=12:42)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Ryan Wick.

## Tools and resources mentioned

Read the Docs, samtools, Git, GitHub, PEP 8, Semantic versioning, Unit testing, Integration testing, Behaviour-driven development, Test-driven development, Cucumber, Conda, Galaxy, Ubuntu, Red Hat.

## Questions this episode answers

### What documentation makes a bioinformatics tool easier to maintain and reuse?

The hosts recommend a usage statement or README explaining parameters, input and output formats, plus a small worked example. They also recommend documenting the laboratory workflow around a tool so that institutional knowledge survives staff changes.

### Why does versioning matter for reproducible bioinformatics?

Recording versions makes it possible to retrieve and rerun the code used for an earlier result. The episode connects this with manuscript reproducibility and validation, since changed software can produce different answers from the same data.

### How can developers measure software impact beyond citations?

Suggested measures include downloads, installations, GitHub activity, institutional and geographical reach, and examples of research enabled by the tool. Surveys, mailing lists, literature searches and website analytics can help, although decentralised distribution makes exact usage totals difficult.

### Can paid support sustain open-source bioinformatics software?

The hosts discuss Ubuntu and Red Hat as examples of free software supported by paid services. They see this as a possible model, but question whether small projects can attract enough paying users and note that users may resist paying even when support takes substantial developer time.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

How do you make bioinformatics software sustainable so that we can
move our field from academic research into hospitals and doctors
offices? We discuss the nuts and bolts of making sustainable
bioinformatics software and changes you can make in your own
practices: Documentation, Coding styles, Versioning, SOPs and
capturing institutional knowledge, Software licencing, Automated
testing, Measuring your impact, and going the commercial route.
