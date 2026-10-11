---
layout: page
title: 'Episode 109: AI Unleashed: Navigating the Opportunities and Challenges of AI in Microbial Bioinformatics'
date: '2023-06-22 00:00:00'
link: https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics
episode: '109'
soundcloud_track: '1541726071'
tags:
- microbinfie
- podcast
description: Lee, Andrew and Nabil test AI code translation, discuss Copilot workflows and examine convincing errors in bioinformatics content.
excerpt: Lee, Andrew and Nabil test AI code translation, discuss Copilot workflows and examine convincing errors in bioinformatics content.
headline: 'ChatGPT and Copilot for bioinformatics: code, checks and limits'
guests: []
topics:
- microbial bioinformatics
- generative ai
- ai-assisted programming
- code translation
- boilerplate code
- dna translation
- ai hallucinations
- human oversight
faq:
- q: Can ChatGPT convert a Perl bioinformatics script into Python?
  a: The hosts try this with Lee’s script for converting pipe-separated sequences into standard FASTA entries. The Python output uses argparse and Biopython and looks reasonable on inspection, but they do not establish functional correctness by running it.
- q: How does Andrew use GitHub Copilot in VS Code?
  a: He writes comments or descriptions of the required behaviour, often with input headers and example rows, then accepts suggested code with Tab. In the June 2023 episode, he describes a $10 monthly GitHub subscription and a VS Code extension connected to his GitHub account.
- q: What information helped Copilot generate the spreadsheet-comparison code?
  a: Andrew provided the purpose of the comparison, the accession column used to join the files, the species columns to compare, and sample headers and rows. The task compared assembly metadata with GAMBIT predictions using pandas.
- q: What limitations did the hosts find in AI-generated content?
  a: They encountered plausible but incorrect factual answers, including a Morrowind route and details in generated bioinformatics tool reviews. They also stress that code which looks convincing still needs checking, particularly when the user lacks experience with the task or programming language.
---

*ChatGPT and Copilot for bioinformatics: code, checks and limits*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss how they use generative AI for coding, document drafting and routine data tasks. They try translating a Perl script into Python and back, generate DNA-to-protein translation code, and examine a spreadsheet-comparison workflow. Their examples show where AI can save typing and searching, but also why plausible code and confident explanations still need human checks.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 109: AI Unleashed: Navigating the Opportunities and Challenges of AI in Microbial Bioinformatics" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1541726071&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 109: AI Unleashed: Navigating the Opportunities and Challenges of AI in Microbial Bioinformatics on SoundCloud](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics)

## In this episode

### Copilot for everyday coding

Andrew describes using GitHub Copilot in VS Code to turn comments and task descriptions into code. He supplies the intended behaviour, input filenames and a few example lines, then accepts suggestions with Tab. He estimates that initial output is often about 90% right and that the assistance has increased his coding speed by roughly 20–30%. Remembering pandas syntax is one recurring task it helps with: suggestions can use the variable names already present in his project.

In this June 2023 discussion, Andrew says he pays $10 a month for Copilot and connects it through a VS Code extension using his GitHub account. Copilot Chat is then available through a waiting list. He also describes generating methods, comments and unit tests, explaining unfamiliar lines, and suggesting fixes for errors. These features reduce typing and repeated lookups, rather than removing the need to understand the program.

### Routine tasks and convincing wrong answers

Nabil uses ChatGPT for jobs such as converting mixed date representations into ISO year-month-day format. He also experiments with shortening paper abstracts from around 300 words to 100 words, or just three lines. For familiar documentation tasks, such as explaining SSH keys, he finds that it can produce a useful tutorial alongside documentation he already has.

His warning comes from less routine questions. Asked for a route from Caldera to Ebonheart in Morrowind, the model mentions recognisable transport options, including the Mages Guild and silt striders, but gives incorrect connections. The answer sounds convincing to someone who recognises the terminology. Nabil uses this example to distinguish helpful boilerplate from answers whose apparent fluency conceals factual mistakes.

### AI-written articles and synthetic podcasts

Andrew reports that an editorial on the ethics of AI in microbial genomics research has just been accepted. Written with ChatGPT during a hackathon, it includes a human-written introductory paragraph. He also describes an AI-generated companion podcast about the ethics of using AI in academic research, using ElevenLabs to produce speech from cloned versions of his and his partner’s voices.

A separate hackathon experiment takes the name of a bioinformatics tool and generates a review episode, speech, show notes and a title. Andrew says factual errors were serious enough that he instructed the model not to include people’s names or institutions. He worries that cheaply generated podcasts, videos and web pages will create a flood of unreliable material that looks authoritative. Audio descriptions might help visually impaired users access information about software, but he argues that a human still needs to check whether the content makes sense.

### A live Perl–Python round trip

Lee supplies a script from his LSK scripts repository for a live translation exercise. It reads a non-standard FASTA file in which sequences are separated by pipe characters, then writes separate sequence entries in standard FASTA format. Nabil and Andrew each ask an AI assistant to convert it from Perl to Python (Nabil says he is using GPT-4 in ChatGPT), and Andrew then converts the Python back to Perl.

The hosts inspect the generated command-line handling, use of argparse and Biopython, output-directory creation, and writing to files or standard output. Their results differ: one Python version preserves Lee’s introductory comments and authorship, while another drops the attribution. Andrew finds the returned Perl neatly written and also tries requesting a one-liner.

These are visual inspections, not completed functional tests. Lee explicitly says he will not know whether the translation is right until he runs it. The model also supplies a disclaimer about possible differences and further adaptation.

### DNA translation and spreadsheet comparisons

Nabil next asks for Python code to translate DNA into protein. ChatGPT produces a Biopython example that creates a sequence object, calls its translation method and returns the protein sequence. He requests equivalent Rust code and later JavaScript. The examples look plausible to the hosts, but Nabil notes that he does not know Rust and deliberately chose a simple task to make inspection easier.

Andrew shares a more detailed Copilot prompt for a Python class comparing two spreadsheets with pandas: assembly metadata and GAMBIT results. The files are joined on an accession number, such as a GCA accession, and the species column in the assembly metadata is compared with the predicted-name column in the other file. He includes headers, example rows and the purpose of the comparison—assessing GAMBIT’s species recall. Andrew says this supplied enough context to generate about 95% of the code, and Nabil observes that the instruction is high-level and conceptual rather than pseudocode.

### Experience still matters

Lee asks whether generated spreadsheet code might miss a subtle case. Andrew’s answer is that he reads and checks the output: having implemented similar tasks many times helps him recognise what should be there. He warns that a new undergraduate or PhD student might not have the experience needed to spot errors, even when most of the generated program looks correct.

The episode also considers refusals and developer-imposed constraints. Nabil explicitly asks ChatGPT for a malicious script to delete everyone’s data, and it refuses on ethical grounds. The hosts discuss the possibility of circumventing such constraints, but do not demonstrate it. Across the examples, they distinguish useful assistance with familiar tasks from trusting generated output without review.

## Highlights

- [00:01:12](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=1:12) — Andrew describes Copilot-generated code, contextual suggestions and estimated time savings.
- [00:04:45](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=4:45) — Nabil discusses date standardisation, shorter abstracts and convincing wrong answers.
- [00:08:05](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=8:05) — Automatically generated bioinformatics tool-review podcasts expose factual errors.
- [00:12:15](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=12:15) — Lee introduces the non-standard FASTA script for a Perl–Python round trip.
- [00:17:33](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=17:33) — Lee distinguishes code that looks right from code that has actually been run.
- [00:18:16](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=18:16) — Nabil proposes generating DNA-to-protein translation code and converting it to Rust.
- [00:19:13](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=19:13) — Andrew shares his prompt for generating a spreadsheet-comparison class.
- [00:21:30](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=21:30) — Andrew explains why programming experience remains important for checking AI output.
- [00:22:34](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=22:34) — Copilot subscription, VS Code setup, chat features and unit-test generation.
- [00:25:26](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=25:26) — Nabil reviews the generated Biopython DNA-translation example and its Rust conversion.
- [00:29:25](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=29:25) — ChatGPT refuses an explicitly malicious request to delete users’ data.

## In their own words

> It sounds very convincing, but it's wrong.
>
> — Nabil-Fareed Alikhan, [00:04:45](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=4:45)

> I mean, I'm not going to know until I run it. I'm probably not going to run it, but it looks right.
>
> — Lee Katz, [00:17:33](https://soundcloud.com/microbinfie/ai-unleashed-navigating-the-opportunities-and-challenges-of-ai-in-microbial-bioinformatics#t=17:33)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

ChatGPT, GPT-4, GitHub Copilot, GitHub Copilot Chat, VS Code, pandas, Biopython, argparse, ElevenLabs, GAMBIT.

## Questions this episode answers

### Can ChatGPT convert a Perl bioinformatics script into Python?

The hosts try this with Lee’s script for converting pipe-separated sequences into standard FASTA entries. The Python output uses argparse and Biopython and looks reasonable on inspection, but they do not establish functional correctness by running it.

### How does Andrew use GitHub Copilot in VS Code?

He writes comments or descriptions of the required behaviour, often with input headers and example rows, then accepts suggested code with Tab. In the June 2023 episode, he describes a $10 monthly GitHub subscription and a VS Code extension connected to his GitHub account.

### What information helped Copilot generate the spreadsheet-comparison code?

Andrew provided the purpose of the comparison, the accession column used to join the files, the species columns to compare, and sample headers and rows. The task compared assembly metadata with GAMBIT predictions using pandas.

### What limitations did the hosts find in AI-generated content?

They encountered plausible but incorrect factual answers, including a Morrowind route and details in generated bioinformatics tool reviews. They also stress that code which looks convincing still needs checking, particularly when the user lacks experience with the task or programming language.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

In this episode of the Micro Binfie Podcast, titled "AI Unleashed: Navigating the Opportunities
and Challenges of AI in Microbial Bioinformatics", Lee, Nabil, and Andrew unpack the
implications of generative predictive text AI tools, notably GPT, on microbial bioinformatics.

They kick off the conversation by outlining the various applications of AI tools in their work,
which range from generating boilerplate programs, drafting documents, to summarizing vast
tracts of data. Andrew talks about his experience with GPT in coding, specifically via VS Code
and GitHub Copilot, highlighting how GPT can generate nearly 90% of the necessary code based on
a brief description of the task, thereby accelerating his work.

He goes on to discuss the use of GPT in clarifying lines of code and notes that they used AI to
generate a paper on the ethical considerations of employing AI in microbial genomics research
during a recent hackathon. The conversation then switches gears as Nabil shares his experience
of using GPT to standardize date formats in tables and summarize paper abstracts. While GPT is
generally accurate in performing simple tasks, he warns that the tool can sometimes provide
erroneous answers.

Nabil also highlights GPT's ability to generate plausible but inaccurate responses for complex
prompts, as illustrated by his experience when he used it to find a route in a video game.
Andrew then talks about a script they created during a hackathon, which produces podcast
episodes reviewing math tools. He points out the issues encountered, such as GPT providing
wrong factual information.

Looking ahead, Andrew envisions a future awash with GPT-generated content that may or may not
be correct, raising the challenge of discerning real and false information. However, they also
acknowledge the potential benefits of AI technologies for those with visual impairments, though
it's far from a perfect solution at present.

The conversation veers to the use of AI tech in handling boilerplate code and generating code
snippets based on predictive text. The hosts further discuss the potential for this tool in
rapid language learning. A live experiment ensues where Nabil and Andrew use a Perl script and
utilize GPT-4 to convert this script into Python and back again to assess its capabilities in
language translation. The AI tool proves proficient, considering comments, usage, and
authorship and employing popular libraries like BioPython intelligently, though it does leave a
disclaimer about potential inaccuracies.

They consider the possibility of using AI to optimize coding, similar to minifying JavaScript,
and even the idea of iterating through multiple languages and assessing the output. Nabil
initiates a simpler task for the AI, asking it to write a Python script translating DNA into
protein, which then gets translated into Rust. Andrew shares his experience of using AI to
generate a Python class that compares two spreadsheets using pandas, demonstrating AI's
comprehension and execution of complex tasks.

In summary, this episode underscores the power and potential of AI in coding and the need for
human oversight to ensure the quality and effectiveness of AI-generated content. It offers a
glimpse into a future where AI tools, despite their limitations, can revolutionize many aspects
of programming, bringing in new efficiencies and methods of working.
