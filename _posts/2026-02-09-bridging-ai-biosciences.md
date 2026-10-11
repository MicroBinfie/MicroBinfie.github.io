---
layout: page
title: 'Episode 149: Bridging AI & Biosciences'
date: '2026-02-09 00:00:00'
link: https://soundcloud.com/microbinfie/bridging-ai-biosciences
episode: '149'
soundcloud_track: '2261246297'
tags:
- microbinfie
- podcast
description: 'A live Bristol panel on AI in biosciences: microscopy, LLM-assisted research, data leakage, validation and interdisciplinary collaboration.'
excerpt: 'A live Bristol panel on AI in biosciences: microscopy, LLM-assisted research, data leakage, validation and interdisciplinary collaboration.'
headline: 'AI in biosciences: useful tools, trust and collaboration'
guests:
- Mark Basham
- Elisa Pedone
- James Thomas
topics:
- ai in biosciences
- microscopy image analysis
- generative ai
- scientific software development
- data privacy
- scientific validation
- research bias
- interdisciplinary collaboration
- environmental impact
- predictive biology
faq:
- q: How has AI changed microscopy analysis?
  a: Mark Basham describes a shift from studying individual images in detail to analysing large image collections statistically. He credits deep learning and neural networks with substantial changes, with transformers bringing further advances.
- q: What research tasks can LLMs help with?
  a: The panel discusses coding assistance, literature reviews and translating plain-English questions into SQL queries. Basham and Thomas stress that users still need enough expertise to assess the results.
- q: What is the lethal trifecta for AI agents handling research data?
  a: James Thomas describes the combination of untrusted input, private-data access and internet access. An injected instruction in the input could redirect an agent and cause private information to be leaked.
- q: How can computer scientists collaborate effectively with biologists?
  a: Elisa Pedone advises finding a collaborator in the other discipline and defining the biological problem before choosing a model. The panel also recommends frequent communication, shared terminology and close work with domain experts on data preparation and validation.
- q: Should researchers always use the most sophisticated AI model?
  a: Basham recommends comparing large models with simpler alternatives such as random forests. He describes situations where a small improvement in performance may not justify the additional power use, while acknowledging that some tasks need larger models.
---

*AI in biosciences: useful tools, trust and collaboration*

Kieren Sharma and Andrew Page chair a live panel at the Bridging AI & Biosciences Workshop at the University of Bristol, with Mark Basham, Elisa Pedone and James Thomas. They discuss where AI has changed biological research, how generative tools affect research workflows, and why scientific validation remains essential. The conversation connects practical applications in microscopy and software development with data security, environmental costs and collaboration between biologists and computer scientists.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 149: Bridging AI & Biosciences" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2261246297&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 149: Bridging AI & Biosciences on SoundCloud](https://soundcloud.com/microbinfie/bridging-ai-biosciences)

## In this episode

### What has changed in biological image analysis?

Mark Basham distinguishes the current AI investment cycle from advances that would remain useful even if enthusiasm faded. Since he began working on image processing around 2015–2016, deep learning and neural networks have changed microscopy analysis substantially, with transformers bringing further advances. His central example is the move from analysing individual images in detail to performing statistical analysis across large quantities of image data.

Elisa Pedone describes CellVoyant’s combination of computer vision, machine learning, label-free microscopy and other input data to understand and control cellular processes. James Thomas sees opportunities not only in developing new methods, but in transferring established tools into subjects that have not yet adopted them. He mentions computer vision and transformers for genomics. He also notes that some people want to use AI because it attracts funding, and says that using these systems well requires thinking about the problem in a structured way.

### LLMs as research and software assistants

The panel separates AI used to analyse research data from AI used to help researchers work more quickly. Basham and Thomas report that coding assistants can be productive in experienced hands, but can cause problems when users lack the background needed to assess their output. Andrew Page places greater emphasis on prompt engineering and coordinating agents and models, describing work with VS Code and Copilot rather than manually writing every line.

Basham also describes promising work translating plain-English questions into SQL queries, allowing colleagues to access data repositories without knowing SQL themselves. Pedone identifies literature reviews as another useful application when planning experiments. She describes experiments lasting weeks, with substantial manual work, annotation and data processing, and sees opportunities for AI support across those tasks and the preparation of quality-control logs and standard operating procedures.

### Generated papers still need scientific judgement

Page describes a thought experiment combining about 200 patient metadata fields from a clinical study with genome sequencing data. He asked an AI-driven workflow to try combinations and write papers. It explored roughly 5,000 combinations and produced 40 papers he described as significant; the outputs included 20-page papers with statistics, figures and references. He thought they looked publishable, but explicitly says he did not publish them and did not intend to.

Basham stresses that scientific accuracy remains the researcher’s responsibility: information returned by an LLM must be validated, and the worry begins when people excuse incorrect work by blaming the AI. Thomas compares the tools to junior staff whose work requires review. Page also distinguishes generating text or code from building a useful scientific model, noting the difficulties of noisy data, small patient samples and large numbers of metadata fields.

### Private data, reproducibility and inherited bias

Thomas introduces Simon Willison’s lethal trifecta: untrusted input, access to private data and access to the internet. His concern is that an instruction hidden in the material an agent is analysing could redirect it and cause private information to be sent elsewhere. He distinguishes this from concerns about providers using submitted data to train models, and points to protected health-data environments without internet access as an important setting for these questions.

Pedone raises related concerns about tracing information from induced pluripotent stem cells, or iPSCs, back to donors, alongside the reproducibility of models used in biology. Page adds that models can inherit the biases of the research literature. His microbiome example concerns the emphasis on populations in the US and Europe, whose results may not represent the wider population.

### Collaboration starts with the biological problem

Pedone identifies a mutual trust problem. Biologists may distrust a model presented as a black box and want experimental validation, while data scientists can underestimate biological complexity. Her advice is to find a collaborator in the other discipline and start by understanding the problem, rather than selecting a model first. The aim is an answer with biological meaning, not simply analysed data.

Basham focuses on data preparation: researchers should not expect to arrive at a beautifully curated, labelled image collection ready for training. Domain experts are often needed to turn raw observations into useful information. Thomas explains why his team embeds data scientists within research groups rather than relying only on monthly progress meetings. Frequent communication helps establish shared language and clarify what counts as a useful result: model metrics alone may not answer the scientist’s question.

### Choosing models that fit the task

Asked about environmental impact, Basham argues for benchmarking sophisticated models against simpler alternatives. He describes cases where large models perform only roughly half a per cent better than a random forest while using much more power. His group investigates whether better data representations can achieve useful results at lower computational cost, while recognising that some problems require larger models.

Thomas cautions that environmental comparisons also need to account for the time and resources a person would use to complete the task manually. He says a lack of transparent data makes that comparison difficult. In the final discussion, Pedone distinguishes prediction from mechanistic understanding: for translational and therapeutic applications, she considers pattern recognition and reaching a desired phenotype valuable even without fully explaining the mechanism. She does not dismiss mechanism-focused research, which can proceed in parallel.

## Highlights

- [00:06:21](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=6:21) — Basham distinguishes AI hype from lasting advances in microscopy image analysis.
- [00:08:44](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=8:44) — Thomas discusses transferring established AI tools between research subjects.
- [00:11:43](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=11:43) — LLMs in software development, followed by plain-English access to SQL databases.
- [00:12:55](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=12:55) — Pedone discusses literature reviews and support for lengthy experimental workflows.
- [00:15:50](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=15:50) — Page describes prompt engineering, agent-assisted coding and a paper-generation experiment.
- [00:19:59](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=19:59) — The lethal trifecta of untrusted input, private data and internet access.
- [00:23:22](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=23:22) — Basham stresses scientific accuracy and checking AI-generated work.
- [00:24:35](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=24:35) — Page explains how population biases in research can carry into AI models.
- [00:26:00](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=26:00) — Pedone identifies mutual trust as a barrier to interdisciplinary work.
- [00:27:41](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=27:41) — Close partnerships with domain experts are needed to make research data useful.
- [00:31:40](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=31:40) — Environmental costs and benchmarking large models against random forests.
- [00:34:33](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=34:33) — Pedone considers prediction versus mechanistic understanding in therapeutic research.

## In their own words

> You should never start from the model. Never start from the model. Start from understanding the problem.
>
> — Elisa Pedone, [00:26:00](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=26:00)

> Understanding that maybe the best isn't what you need when you can run something that's much cheaper is a really important thing.
>
> — Mark Basham, [00:31:40](https://soundcloud.com/microbinfie/bridging-ai-biosciences#t=31:40)

## Who is talking

- **Kieren Sharma** (host)
- **Andrew Page** (host)
- **Mark Basham** (panellist, Rosalind Franklin Institute)
- **Elisa Pedone** (panellist, CellVoyant)
- **James Thomas** (panellist, Jean Golding Institute, University of Bristol)

Also mentioned: Simon Willison.

## Tools and resources mentioned

ChatGPT, Claude, VS Code, Copilot, SQL, random forests, transformers, label-free microscopy.

## Questions this episode answers

### How has AI changed microscopy analysis?

Mark Basham describes a shift from studying individual images in detail to analysing large image collections statistically. He credits deep learning and neural networks with substantial changes, with transformers bringing further advances.

### What research tasks can LLMs help with?

The panel discusses coding assistance, literature reviews and translating plain-English questions into SQL queries. Basham and Thomas stress that users still need enough expertise to assess the results.

### What is the lethal trifecta for AI agents handling research data?

James Thomas describes the combination of untrusted input, private-data access and internet access. An injected instruction in the input could redirect an agent and cause private information to be leaked.

### How can computer scientists collaborate effectively with biologists?

Elisa Pedone advises finding a collaborator in the other discipline and defining the biological problem before choosing a model. The panel also recommends frequent communication, shared terminology and close work with domain experts on data preparation and validation.

### Should researchers always use the most sophisticated AI model?

Basham recommends comparing large models with simpler alternatives such as random forests. He describes situations where a small improvement in performance may not justify the additional power use, while acknowledging that some tasks need larger models.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Join hosts Kieren Sharma (Artificially Ever After podcast, University of Bristol) and Andrew
Page (MicroBinfie podcast, Origin Sciences) for a compelling live panel discussion exploring
the dynamic intersection of artificial intelligence and the biosciences.

In this episode, our expert panel discusses:

🔬 The AI Revolution in Biology - How machine learning and deep learning have transformed
everything from microscopy image processing to drug discovery, enabling researchers to move
from analyzing single images to conducting statistical analysis on massive datasets.

🤖 The LLM Era - Real experiences with generative AI tools like ChatGPT and Claude in research
workflows, from accelerating literature reviews to writing thousands of lines of code through
prompt engineering rather than manual coding.

⚖️ Finding Balance - When AI is genuinely transformative versus when it's just hype, including
practical guidance on choosing between sophisticated transformer models and simpler, more
energy-efficient approaches like random forests.

🔒 Safety & Trust Challenges - The "lethal trifecta" of untrusted data, private information, and
internet access; reproducibility concerns; and the critical importance of validation in
scientific AI applications.

🤝 Building Interdisciplinary Bridges - Honest insights about the mutual trust deficit between
biologists and data scientists, the importance of finding a "buddy" in the other discipline,
and why starting with the biological problem (not the model) is essential for meaningful
results.

💡 Practical Advice for Computer Scientists - What skills and mindsets are needed to
successfully apply computational expertise to new domains, from understanding domain-specific
language to recognizing the complexity of biological problems.

Featured Panelists:

Dr. Mark Basham - Science Director for AI and Informatics, Rosalind Franklin Institute Dr.
Elisa Pedone - Senior Research Scientist, CellVoyant (AI for cell therapy development) James
Thomas - Senior Data Scientist, Jean Golding Institute, University of Bristol

Key Themes: AI in drug discovery • machine learning in microscopy • generative AI in research •
interdisciplinary collaboration • data quality challenges • environmental impact of AI • the
future of computational biology

This episode was recorded live at the Bridging AI & Biosciences Workshop in the University of
Bristol and is part of AIBio UK's mission to highlight innovative applications of artificial
intelligence across the biosciences.
