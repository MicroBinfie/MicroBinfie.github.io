---
layout: page
title: 'Episode 115: Write-the: speeding up software development for bioinformatics'
date: '2023-11-09 00:00:00'
link: https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics
episode: '115'
soundcloud_track: '1656605382'
tags:
- microbinfie
- podcast
description: Wytamma Wirth discusses write-the, codebase context, constrained AI agents and turning generated docstrings into searchable documentation.
excerpt: Wytamma Wirth discusses write-the, codebase context, constrained AI agents and turning generated docstrings into searchable documentation.
headline: 'Write-the: code, documentation and AI agents for bioinformatics'
guests:
- Wytamma Wirth
topics:
- bioinformatics software
- large language models
- code documentation
- vector databases
- ai agents
- code refactoring
- software papers
- documentation translation
- software testing
faq:
- q: Does write-the use an LLM to build its documentation website?
  a: The MkDocs utility demonstrated in the episode does not use an LLM. It extracts existing docstrings and populates documentation templates; those docstrings can have been generated in an earlier LLM-powered step.
- q: Can write-the refactor an entire codebase?
  a: Wirth describes codebase-wide refactoring and optimisation as areas he is investigating. He discusses using vector stores and project summaries to supply relevant context, rather than demonstrating a finished whole-project refactoring feature.
- q: Could write-the draft a JOSS software paper?
  a: The hosts propose this as an extension. Wirth thinks documented code, examples and journal templates could support drafting an introduction and background, with revision through a chat interface.
- q: Does write-the generate documentation for Perl projects?
  a: Wirth says he has not tried parsing Perl documentation and describes the current documentation generation as limited to Python files. He discusses plans to use a language-agnostic parsing library to support other languages.
- q: Why does the episode favour narrowly scoped AI agents?
  a: Wirth argues that agents with a specific task and constrained inputs and outputs may be less likely to lose track of their purpose. He also warns that letting an agent execute arbitrary code is unsafe.
---

*Write-the: code, documentation and AI agents for bioinformatics*

Wytamma Wirth of the University of Melbourne returns to discuss write-the with the MicroBinfie hosts. They explore language models for codebase-wide changes, narrowly scoped agents, diagrams, software papers and multilingual documentation. A demonstration distinguishes LLM-generated docstrings from the non-LLM steps that turn them into a searchable documentation website, with review and testing still important.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 115: Write-the: speeding up software development for bioinformatics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1656605382&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 115: Write-the: speeding up software development for bioinformatics on SoundCloud](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics)

## In this episode

### Giving language models context across a codebase

Wirth is exploring how write-the could work across an entire project rather than isolated pieces of code. A large Python script may exceed a language model’s context limit; truncating it leaves the model without information about earlier parts. Vector stores and vector databases offer a way to retrieve relevant code and add it to the context when needed.

The proposed approach combines project summaries, function definitions and related code retrieved for a particular task. This could support refactoring and optimisation across a codebase. Wirth presents these as directions he is investigating, with the central challenge being how to represent enough of a project for the model to understand the relationships within it.

### Constrained agents rather than general intelligence

Wirth uses LangChain to interface with language models and build prompts and agents. He also describes Langflow, which lets users connect components in flow diagrams, and Haystack as another library for defining tools that a model can use. The hosts compare this with ChatGPT’s GPT-4 plugins, where a tool retrieves information and the model formats or summarises it.

One experiment gave an agent a tool for writing and executing Perl scripts. Wirth explicitly warns against allowing arbitrary code execution. He contrasts narrowly defined tasks with the broad ambitions of AutoGPT and BabyAGI: an agent constrained to a specific bioinformatics task may be less likely to lose track of its purpose. Clearly specified inputs, outputs and responsibilities are recurring themes.

### UML diagrams and Mermaid

The hosts ask whether write-the could generate UML diagrams showing classes, attributes, methods and their relationships. One host explains why these diagrams can be useful: mapping a program may reveal a function in the wrong class, repeated behaviour or an opportunity to create a shared class. Producing the diagram by hand, however, can be tedious.

Lee Katz brings up Mermaid, describing a text-based way to express and visualise a flow chart. Diagram generation remains a possible extension rather than a demonstrated write-the feature. The discussion also distinguishes diagrams that help a programmer reason about a design from a model directly interpreting and reorganising the code.

### Drafting software papers and translating documentation

The hosts suggest a command that could draft a JOSS paper from a project. Wirth thinks documented code, examples and a description of the software could provide material for an introduction and background. Journal templates could supply a starting structure, while a chat interface would allow authors to revise wording through successive exchanges. Understanding the whole codebase remains a limitation.

The motivation is practical: the hosts enjoy writing software but find formal descriptions harder. One jokes about needing to explain a project whose functionality was already available in BEDTools. The conversation then turns to researchers who can write quickly in their first language but spend much longer producing formal English prose.

Wirth says he has not personally tried that translation workflow. He nevertheless sees value in multilingual project documentation, provided the translation preserves the intended meaning rather than changing it.

### From docstrings to a searchable website

During the conversation, one host runs write-the on his own code and praises the result, while noting that he has not yet run tests. Wirth then demonstrates the separate MkDocs utility. Unlike the docstring-writing step, this utility does not use an LLM: it prepares a documentation template and uses existing docstrings to build an API reference.

The resulting site includes descriptions, input parameters, return types and other information extracted from consistently formatted docstrings. It is searchable, supports dark mode and can be deployed to GitHub Pages using a generated GitHub Actions script. A README becomes the front page; tutorials are not generated automatically.

The point is to reduce the effort needed to publish useful documentation. The model supplies docstring content, while ordinary parsing and templating turn that content into the website.

### Language support, testing and human review

Asked about Perl documentation, Wirth describes the current documentation parser as limited to Python files. He plans to integrate an unnamed open-source library used by GitHub for identifying symbols and relationships in code. Its concrete syntax tree parsing could help locate functions and docstrings across other programming languages.

The closing exchange sketches a sequence of converting code to Python, generating docstrings, building the documentation site and writing tests. It is a suggested workflow, not evidence that conversion produces a validated project. Together with the warning about arbitrary code execution and the host’s untested local run, this keeps an important distinction visible: generating code or documentation is not the same as checking that it is correct.

## Highlights

- [00:01:06](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=1:06) — Vector stores and project summaries as context for codebase-wide operations
- [00:02:33](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=2:33) — A request for automatically generated UML diagrams
- [00:03:28](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=3:28) — LangChain and Langflow for building language-model applications
- [00:05:09](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=5:09) — Defining agent tools, including an experiment that executes Perl scripts
- [00:05:55](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=5:55) — Why constrained agents may be more useful than broadly autonomous systems
- [00:06:55](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=6:55) — Mermaid as a text-based approach to diagrams
- [00:09:51](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=9:51) — Proposed commands for diagrams and JOSS paper drafts
- [00:13:51](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=13:51) — Multilingual documentation and the need to preserve meaning
- [00:15:30](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=15:30) — A host reports trying write-the on his code, with tests still outstanding
- [00:15:52](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=15:52) — The non-LLM MkDocs utility for generating and deploying documentation
- [00:19:54](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=19:54) — Extracting consistently formatted docstrings to populate documentation templates
- [00:20:47](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=20:47) — Python-only parsing and plans for broader programming-language support

## In their own words

> You shouldn't let it execute arbitrary code, but yeah, you can sort of define any sort of tool that you want using these interfaces and libraries.
>
> — Wytamma Wirth, [00:05:09](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=5:09)

> We are rapidly running out of excuses for why we don't have documentation.
>
> — one of the hosts, [00:17:51](https://soundcloud.com/microbinfie/write-the-speeding-up-software-development-for-bioinformatics#t=17:51)

## Who is talking

- **Wytamma Wirth** (guest, University of Melbourne)
- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

write-the, ChatGPT, GPT-4, LangChain, Langflow, Haystack, AutoGPT, BabyAGI, Unified Modeling Language (UML), Mermaid, MkDocs, GitHub, GitHub Actions, GitHub Pages, BEDTools.

## Questions this episode answers

### Does write-the use an LLM to build its documentation website?

The MkDocs utility demonstrated in the episode does not use an LLM. It extracts existing docstrings and populates documentation templates; those docstrings can have been generated in an earlier LLM-powered step.

### Can write-the refactor an entire codebase?

Wirth describes codebase-wide refactoring and optimisation as areas he is investigating. He discusses using vector stores and project summaries to supply relevant context, rather than demonstrating a finished whole-project refactoring feature.

### Could write-the draft a JOSS software paper?

The hosts propose this as an extension. Wirth thinks documented code, examples and journal templates could support drafting an introduction and background, with revision through a chat interface.

### Does write-the generate documentation for Perl projects?

Wirth says he has not tried parsing Perl documentation and describes the current documentation generation as limited to Python files. He discusses plans to use a language-agnostic parsing library to support other languages.

### Why does the episode favour narrowly scoped AI agents?

Wirth argues that agents with a specific task and constrained inputs and outputs may be less likely to lose track of their purpose. He also warns that letting an agent execute arbitrary code is unsafe.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We continue our conversation with Wytamma Wirth about write-the and all things AI. It starts
with discussing the usage of language models, specifically ChatGPT, in writing boilerplate
code, and how it can assist in generating code snippets, unit tests, and even documentation
strings. The participants also explore the potential of incorporating it into code editors to
make coding more efficient and less error-prone.

The conversation then shifts to discuss the generation of research papers, specifically
software announcements, by leveraging code documentation. The participants believe ChatGPT
could be useful in generating introductions and backgrounds for such publications. They also
touch upon the utility of language models in translating documentation into different human
languages to assist non-native English speakers.

The discussion returns to code documentation, focusing on the tool "write the docs" which auto-
generates well-structured and searchable documentation websites. The participants appreciate
the tool's ease of use and the potential it has in maintaining proper documentation for
projects. The conversation ends with an acknowledgment of the importance of human oversight in
automating tasks using language models.

Links: Write-the software: <https://github.com/Wytamma/write-the> Wytamma Wirth:
<https://www.wytamma.com/>
