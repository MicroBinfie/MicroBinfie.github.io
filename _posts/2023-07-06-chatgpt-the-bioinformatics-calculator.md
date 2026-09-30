---
layout: page
title: 'Episode 110: ChatGPT: The Bioinformatics Calculator'
date: '2023-07-06 00:00:00'
link: https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator
episode: '110'
soundcloud_track: '1555795549'
tags:
- microbinfie
- podcast
description: Can ChatGPT solve bioinformatics exercises? The hosts discuss coding tests, assessment, regular expressions and possible sequencing applications.
excerpt: Can ChatGPT solve bioinformatics exercises? The hosts discuss coding tests, assessment, regular expressions and possible sequencing applications.
headline: 'ChatGPT as a bioinformatics calculator: tests and limits'
guests: []
topics:
- microbial bioinformatics
- large language models
- code generation
- technical hiring
- academic assessment
- regular expressions
- basecalling
- read correction
- gene prediction
faq:
- q: How well did ChatGPT perform on the bioinformatics exercises discussed?
  a: The hosts describe a preprint testing 179 exercises and report 139 first-attempt solutions. Further prompting helped with additional exercises, but five reportedly remained unsolved despite repeated attempts.
- q: Why do the hosts compare ChatGPT with a calculator?
  a: Both can help users complete technical tasks, but the hosts argue that assistance does not remove the need for foundational knowledge. A bioinformatician still needs to judge whether the generated code or answer is appropriate and accurate.
- q: What coding limitations do the hosts identify?
  a: The benchmark exposed difficulty handling spaces and punctuation in a regular-expression exercise. One host also reports repeated code blocks in longer outputs, and the panel cautions against generalising from very short course exercises to scripts hundreds of lines long.
- q: Could language models improve basecalling or read correction?
  a: The hosts speculate that structured patterns in genetic sequences could support these applications, potentially through models running on sequencing instruments. They also warn against confusing plausible predicted sequence with observed data; the episode presents ideas rather than a validated method.
---

*ChatGPT as a bioinformatics calculator: tests and limits*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan examine whether ChatGPT can serve as a calculator for bioinformatics, using a preprint that tested it against course programming exercises. They discuss what this means for hiring and teaching, where generated code fails, and whether language-model approaches could help with sequencing data. Their central concern is how users retain enough understanding to check an AI-generated answer.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 110: ChatGPT: The Bioinformatics Calculator" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1555795549&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 110: ChatGPT: The Bioinformatics Calculator on SoundCloud](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator)

## In this episode

### Testing ChatGPT as a bioinformatics student

Following the previous episode’s live demonstrations, the hosts discuss the preprint **Many bioinformatics programming tasks can be automated with ChatGPT**, by Piccolo et al. The study supplied course exercises to ChatGPT and checked its generated programs with an automated testing suite, treating it much like a student submitting answers. The hosts describe 179 exercises and report 139 first-attempt solutions, with additional prompting resolving more of the problems.

Five exercises reportedly remained unsolved despite repeated prompting, in some cases around ten attempts. One involved finding words beginning with vowels in biological text using regular expressions. Extra spaces and punctuation caused difficulties. The hosts connect this failure to the need to understand the range of possible inputs before writing a suitable expression, offering a little reassurance to the Perl users listening.

### The calculator analogy and hiring

The benchmark immediately raises a hiring concern: a take-home technical test may no longer reveal whether a candidate understands the problem or has simply pasted it into ChatGPT. One host suggests that employers may need to sit with applicants while they solve a task, rather than relying on answers submitted in advance.

Lee Katz asks whether AI should instead be treated like a calculator: a legitimate tool for answering straightforward questions. The response is that tool use still requires foundational knowledge. Calculating GC content is a simple example, but more complex work demands someone who can assess whether an answer is accurate. The hosts argue that students, employees and scientists need enough understanding to recognise when a generated solution does not look right.

### Assessing understanding rather than submitted work

One host recalls undergraduate programming exams completed with pen and paper, covering pseudocode, data structures and Big O complexity without a computer or internet access. Such assessments already separate a student’s understanding from the tools available to them. Coursework and projects are harder to assess in the same way because the submitted product may conceal how it was produced.

The discussion considers compulsory passes in closed-book final exams, changing the weighting of assignments and asking students to explain a subject orally. The hosts also mention possible stylistic clues, including mixed indentation conventions and American spelling, while acknowledging that proving AI use from style is difficult. An ethics code alone is not presented as a sufficient safeguard.

### Short scripts, repetition and model access

The hosts distinguish success on short exercises from reliability on everyday programming work. The study’s generated answers had line counts comparable to the instructor’s solutions, which they regard as encouraging. However, the instructor’s solutions are described as never longer than about 30 to 39 lines, whereas tasks they assign can require scripts of 100–300 lines. One host reports seeing longer generated code repeat the same block of roughly ten lines while attempting simple statistics calculations.

They ask whether larger context windows could help, discussing limits of about 4,000 tokens, access to 32,000 tokens and research examples of 100,000 tokens. These are possibilities, not demonstrated fixes. They also discuss fine-tuned programming models, while remaining unconvinced that specialisation automatically makes a model better.

AlphaCode and OpenAI’s Codex provide context for earlier code-generation work. For one host, ChatGPT’s major change is accessibility: a web page and a prompt let many more people experiment.

### Sequencing applications without inventing data

The conversation turns to models that could run without an internet connection, potentially on a sequencing instrument such as Nanopore. The hosts imagine near-real-time applications and ask whether predicting sequence patterns could improve basecalling or read correction. These are proposed uses rather than results from an experiment discussed in the episode.

There is also a practical request: use AI to correct a malformed sample sheet instead of merely reporting that it cannot be processed. This sits alongside a more serious reservation about sequence correction. A joke about turning 10× sequencing into 1,000× by making up the remainder prompts an objection to fabricated data. The discussion exposes a tension between correcting likely errors and replacing an observation with what a model expects to see.

### Structured language, temperature and future alleles

Stephen Wolfram’s article **What Is ChatGPT Doing … and Why Does It Work?** provides a starting point for discussing why language prediction works. The hosts describe language as structured rather than random, then ask whether comparable structure in genetic code makes similar approaches useful. Lee Katz compares next-word prediction with Markov models and asks about applications such as gene prediction.

Another host explains temperature as a source of randomness that can move generation away from repeatedly selecting the same likely continuation. They speculate about supplying sequences from an orthologous gene family and asking a model to propose possible future alleles. The idea is explicitly constrained: meaningful predictions would need to account for protein structure as well as sequence. No organism-specific dataset or validated allele-prediction result is presented.

## Highlights

- [00:00:43](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=0:43) — A preprint tests ChatGPT against bioinformatics course exercises using automated assessment.
- [00:03:11](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=3:11) — Take-home coding tests may no longer demonstrate a job candidate’s own knowledge.
- [00:04:11](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=4:11) — Lee Katz introduces the analogy between AI assistance and calculator use.
- [00:08:23](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=8:23) — Mandatory final-exam passes offer a check on understanding beyond submitted coursework.
- [00:10:53](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=10:53) — Unsolved exercises include regular expressions for words beginning with vowels.
- [00:13:28](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=13:28) — Earlier language models and ChatGPT’s accessible interface put its coding abilities in context.
- [00:16:00](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=16:00) — Longer generated code can fall into loops and repeat blocks of calculations.
- [00:17:29](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=17:29) — Larger token limits raise questions about whether models could handle longer programs.
- [00:20:03](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=20:03) — Offline models on sequencing instruments could create new near-real-time applications.
- [00:20:52](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=20:52) — A practical suggestion: automatically correct malformed sequencing sample sheets.
- [00:22:36](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=22:36) — Stephen Wolfram’s explanation of language structure prompts a comparison with genetic code.
- [00:24:02](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=24:02) — Gene prediction leads into temperature, creative generation and possible future alleles.

## In their own words

> We do need to ensure that students and employees and scientists in general do fundamentally know what they're doing
>
> — one of the hosts, [00:04:28](https://soundcloud.com/microbinfie/chatgpt-the-bioinformatics-calculator#t=4:28)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Stephen Wolfram.

## Tools and resources mentioned

ChatGPT, GPT-4, AlphaCode, OpenAI Codex, Perl, Nanopore, regular expressions, Markov models.

## Questions this episode answers

### How well did ChatGPT perform on the bioinformatics exercises discussed?

The hosts describe a preprint testing 179 exercises and report 139 first-attempt solutions. Further prompting helped with additional exercises, but five reportedly remained unsolved despite repeated attempts.

### Why do the hosts compare ChatGPT with a calculator?

Both can help users complete technical tasks, but the hosts argue that assistance does not remove the need for foundational knowledge. A bioinformatician still needs to judge whether the generated code or answer is appropriate and accurate.

### What coding limitations do the hosts identify?

The benchmark exposed difficulty handling spaces and punctuation in a regular-expression exercise. One host also reports repeated code blocks in longer outputs, and the panel cautions against generalising from very short course exercises to scripts hundreds of lines long.

### Could language models improve basecalling or read correction?

The hosts speculate that structured patterns in genetic sequences could support these applications, potentially through models running on sequencing instruments. They also warn against confusing plausible predicted sequence with observed data; the episode presents ideas rather than a validated method.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode there is a comprehensive discussion on the influence of AI, especially GPT-4,
in the sphere of microbial bioinformatics. They reflect on a study testing GPT-4's problem-
solving capabilities, which raises concerns about its potential impact on employment practices
and academic integrity.

There's speculation that AI's proficiency in tackling standard technical problems could
interfere with genuinely evaluating a candidate's knowledge during interviews. Drawing
parallels with calculators, the hosts deliberate on whether AI tools should be permitted during
assessments. They stress the necessity for individuals to possess a deep understanding of their
domain to accurately interpret and validate AI solutions.

Discussing the AI's limitations, the hosts highlight its struggles with regular expressions and
handling larger scripts. They observe the AI tends to loop and repeat itself, performing better
with shorter scripts but faltering on more complex tasks often seen in bioinformatics. This
prompts a discussion on how educators should address these developments in their teaching
strategies.

Moreover, the hosts explore the potential of large language models to improve base calling and
read correction in sequencing, drawing on the structured and predictable nature of language and
genetic code. They also discuss the idea of introducing randomness in these models to generate
creative and varied solutions, potentially predicting future alleles or gene configurations.

Ultimately, they express a blend of enthusiasm and apprehension towards the swift advances in
this field and the ensuing implications for bioinformatics. They end on a note of anticipation
for future developments, with a humorous nod towards AI's potential for automating mundane
tasks like auto-correcting sample sheets.

References: What Is ChatGPT Doing … and Why Does It Work?
<https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/> Many
bioinformatics programming tasks can be automated with ChatGPT
<https://arxiv.org/ftp/arxiv/papers/2303/2303.13528.pdf> ChatGPT for bioinformatics
<https://medium.com/@91mattmoore/chatgpt-for-bioinformatics-404c6d0817a1> Empowering Beginners
in Bioinformatics with ChatGPT <https://www.biorxiv.org/content/10.1101/2023.03.07.531414v1>
Lawyer uses GPT and get ethics violation <https://simonwillison.net/2023/May/27/lawyer-
chatgpt/> Can ChatGPT solve bioinformatic problems with Python?
<https://dmnfarrell.github.io/bioinformatics/chatGPT-python>
