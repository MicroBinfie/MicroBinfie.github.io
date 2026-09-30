---
layout: page
title: 'Episode 114: Write-the: Automating Code Documentation ChatGPT'
date: '2023-11-04 00:00:00'
link: https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt
episode: '114'
soundcloud_track: '1656603129'
tags:
- microbinfie
- podcast
description: Wytamma Wirth explains how write-the uses ChatGPT to generate docstrings and tests, convert code and build a phylogenetic tree library.
excerpt: Wytamma Wirth explains how write-the uses ChatGPT to generate docstrings and tests, convert code and build a phylogenetic tree library.
headline: 'write-the: AI-generated documentation, tests and code conversion'
guests:
- Wytamma Wirth
topics:
- automated code documentation
- large language models
- prompt engineering
- software testing
- code conversion
- phylogenetics
- bioinformatics software
- academic careers
faq:
- q: What does write-the automate?
  a: It uses the OpenAI API to generate docstrings, scaffold tests and convert files between formats. Its documentation workflow can process a project directory and generate an API reference and documentation website.
- q: Does write-the verify that generated documentation is correct?
  a: Wirth describes checking whether the returned docstring content is valid YAML before inserting it. He discusses possible additional structural checks, but does not describe a comprehensive check of the documentation's semantic accuracy.
- q: Which models does write-the use, and does it cost money?
  a: In the episode, Wirth says it defaults to GPT-3.5 and offers a flag for GPT-4. It requires an OpenAI API key and paid API usage; he describes documentation runs costing a few cents, with requests sent in parallel.
- q: How was write-the used to develop phylo.js?
  a: Wirth used the convert command to turn existing MIT-licensed JavaScript tree-manipulation code into modern TypeScript. The resulting phylo.js package provides phylogenetic tree manipulation separately from visualisation, and he says the work took about a day.
---

*write-the: AI-generated documentation, tests and code conversion*

Wytamma Wirth joins the hosts to discuss write-the, a command-line tool that uses the OpenAI API for documentation, tests and file conversion. He explains its prompt templates, response handling and token limits, then describes using code conversion to develop a phylogenetic tree library. The conversation also covers his move from turtle histopathology to bioinformatics, the difficulty of keeping up with language models and his reasons for staying in academia.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 114: Write-the: Automating Code Documentation ChatGPT" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1656603129&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 114: Write-the: Automating Code Documentation ChatGPT on SoundCloud](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt)

## In this episode

### From turtle pathology to bioinformatics

Wytamma Wirth describes a PhD at James Cook University studying a viral pathogen in freshwater turtles in North Queensland. Alongside laboratory and field work, he spent time on web development and discovered an interest in programming. Rather than changing direction midway through the PhD, he finished it and subsequently joined a phylogenetics research group at the Doherty Institute, developing software packages and carrying out analyses.

About a year and a half later, he joined the Microbial Diagnostic Unit in a bioinformatics role. His work includes COVID-related work, pipeline development, analyses and tool development. He describes his current position as service-focused, with plans to return to more research-oriented work.

### Bootstrapping documentation and tests

The name write-the is a pun on Read the Docs. Wirth developed it after repeatedly copying code into ChatGPT to request documentation or tests. His aim was to standardise those requests and reduce the copying and pasting, rather than require users to supply the same instructions and context each time.

The command-line interface passes files to a large language model. Given a project directory, its documentation command can generate docstrings for functions and classes, then use a documentation-generation tool to produce an API reference and a website suitable for hosting on GitHub. Wirth describes a two-command route to bootstrapping a project's documentation. The package also scaffolds tests and supports file conversion. He has used it to document write-the itself and to submit documentation pull requests to other open-source projects.

### Prompt templates and YAML validation

Each command has an associated prompt. For documentation, an F-string template combines instructions, an example, the requested response structure and the source code. Wirth describes this as prompt engineering, using few-shot learning and code completion to encourage a predictable response. The example takes an undocumented addition function and shows a YAML response containing its description, arguments, return value and usage example.

Much of the software handles what happens around generation: extracting responses, parsing YAML, validating the format and inserting docstrings into code. Asked how it checks validity, Wirth says the main check is whether the returned content is valid YAML. He discusses possible additional checks on argument fields and types, but says he largely trusts the model to follow the prompt. This is format validation, rather than a demonstrated check that every generated explanation is correct.

### Model choices, context limits and cost

Wirth says write-the uses GPT-3.5 by default, with a flag for GPT-4. When asked about a 16k-context version, he says he has not tried it and believes it is available through the chat API rather than the completion API used by the project. A larger context would allow more material to fit into a request.

For files that exceed the available context, write-the can split code into chunks and send individual functions. A large script containing functions is therefore different from a long, unstructured block of code; the latter may need refactoring. Requests are sent in parallel, which Wirth says makes project-wide documentation generation quick. An OpenAI API key is required, and API usage costs money. He describes his documentation runs as costing a few cents, not as a fixed price for every project.

### Converting code for phylogenetic trees

The convert subcommand accepts an input file and an output filename, inferring formats from their extensions. Wirth gives the example of converting script.py into script.ts, moving from Python to TypeScript. A flag can specify the format instead of relying on the extension. He also mentions English-to-French conversion as a possible use, although his main application has been programming-language conversion.

A concrete result was phylo.js, a TypeScript library for manipulating phylogenetic trees. Wirth wanted a standalone, NPM-installable package without the larger dependency imposed by tree visualisation software. The project reused MIT-licensed tree-manipulation code from an existing JavaScript visualisation library and used write-the convert to modernise it into TypeScript. He reports producing the library in about a day, building on existing code rather than implementing every operation from scratch.

### Keeping up with AI and staying in academia

Wirth follows developments through a GPT Slack channel, Twitter, GitHub activity and YouTube, including channels covering open-source language models. One host recommends This Day in AI, a podcast by two Australian brothers. Wirth also uses ChatGPT to summarise documentation and help him understand unfamiliar terminology.

He is cautious about promises that AI will improve everything tenfold, and describes uncertainty about which frameworks and applications will last. The discussion ends with why he remains in academia despite potential industry earnings. Wirth values universities, interesting colleagues and technical conversations, and says he has no immediate plans to move to the private sector, while acknowledging that funding could affect that decision.

## Highlights

- [00:01:41](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=1:41) — Wirth's turtle histopathology PhD and transition into programming and phylogenetics
- [00:04:23](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=4:23) — How write-the replaces repeated copying and pasting for documentation and tests
- [00:06:04](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=6:04) — Using the OpenAI API with templated prompts and structured responses
- [00:07:16](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=7:16) — Command-specific prompts, few-shot learning and code completion
- [00:09:56](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=9:56) — How the tool checks whether a generated docstring is valid
- [00:13:03](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=13:03) — Generated docstrings describe arguments, conditional behaviour and examples
- [00:16:12](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=16:12) — Splitting large scripts into functions to fit model context limits
- [00:16:54](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=16:54) — Following rapid language-model developments through community channels
- [00:19:07](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=19:07) — Wirth's caution about AI hype and uncertainty over future model progress
- [00:20:08](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=20:08) — The convert subcommand infers file formats from input and output extensions
- [00:22:33](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=22:33) — Why Wirth stays in academia rather than pursuing higher industry pay

## In their own words

> I like talking jargon with people
>
> — Wytamma Wirth, [00:22:53](https://soundcloud.com/microbinfie/write-the-automating-code-documentation-chatgpt#t=22:53)

## Who is talking

- **Wytamma Wirth** (guest, The University of Melbourne; Doherty Institute)
- **Lee Katz** (host)
- **Nabil-Fareed Alikhan** (host)
- **Andrew Page** (host)

## Tools and resources mentioned

write-the, ChatGPT, OpenAI API, GPT-3.5, GPT-4, Read the Docs, GitHub, phylo.js, NPM, few-shot learning.

## Questions this episode answers

### What does write-the automate?

It uses the OpenAI API to generate docstrings, scaffold tests and convert files between formats. Its documentation workflow can process a project directory and generate an API reference and documentation website.

### Does write-the verify that generated documentation is correct?

Wirth describes checking whether the returned docstring content is valid YAML before inserting it. He discusses possible additional structural checks, but does not describe a comprehensive check of the documentation's semantic accuracy.

### Which models does write-the use, and does it cost money?

In the episode, Wirth says it defaults to GPT-3.5 and offers a flag for GPT-4. It requires an OpenAI API key and paid API usage; he describes documentation runs costing a few cents, with requests sent in parallel.

### How was write-the used to develop phylo.js?

Wirth used the convert command to turn existing MIT-licensed JavaScript tree-manipulation code into modern TypeScript. The resulting phylo.js package provides phylogenetic tree manipulation separately from visualisation, and he says the work took about a day.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode, we dive deep into the world of automated code documentation and conversion
using ChatGPT through the write-the software developed by Dr Wytamma Wirth from The University
of Melbourne. Our guest, an experienced software engineer, takes us on a journey through the
challenges and nuances of writing code documentation and the role AI can play in easing this
process. We explore the intersection of ChatGPT's capabilities with Write the Docs, a
documentation system widely used by developers. From highlighting ChatGPT's ability to
understand and generate code snippets, to demonstrating real-time code conversion across
multiple programming languages, this episode is a treasure trove for developers looking to
enhance their workflow. Whether you're a seasoned developer or just getting started, tune in to
discover how the synergy of AI and coding can elevate your documentation game to the next
level!

Links: Write-the software: <https://github.com/Wytamma/write-the> Wytamma Wirth:
<https://www.wytamma.com/>
