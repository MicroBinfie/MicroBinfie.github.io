---
layout: page
title: 'Episode 96: IMMEM XIII and ASM NGS conference roundup'
date: '2022-12-22 00:00:00'
link: https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs
episode: '96'
soundcloud_track: '1405835830'
tags:
- microbinfie
- podcast
description: Lee Katz, Andrew Page and Nabil-Fareed Alikhan compare hybrid conferences, real-time wastewater surveillance and genomic metadata.
excerpt: Lee Katz, Andrew Page and Nabil-Fareed Alikhan compare hybrid conferences, real-time wastewater surveillance and genomic metadata.
headline: 'IMMEM XIII and ASM NGS: wastewater, metadata and hybrid meetings'
guests: []
topics:
- hybrid conferences
- public health genomics
- wastewater surveillance
- covid-19
- contextual metadata
- data standards
- genomic epidemiology
- software sustainability
- open source
faq:
- q: What problems did the hosts encounter at hybrid conferences?
  a: They describe reduced audience engagement during remote talks, missing visual cues for speakers, difficult question sessions and overruns. Nabil nevertheless argues that virtual participation improves accessibility and should not simply be abandoned.
- q: What was new about the wastewater surveillance discussed?
  a: The hosts distinguish established wastewater sequencing research from its growing use for regular, real-time public health reporting. They suggest it can provide an earlier signal than hospital sampling, which in their COVID work could lag infection by two or three weeks.
- q: What metadata should accompany microbial genomes?
  a: The discussion emphasises collection date, location, sampling context and relevant patient, animal or food-production information. The hosts recommend consistent definitions and ISO 8601 dates, while warning that privacy adjustments and automatically assigned coordinates can make apparently precise values misleading.
- q: Why is sustaining genomic epidemiology software difficult?
  a: Routine platforms need maintenance, user support, documentation and validation, but academic incentives favour new research and publications. Open-source availability does not resolve the funding problem, and the hosts leave the question of long-term support open.
---

*IMMEM XIII and ASM NGS: wastewater, metadata and hybrid meetings*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan reflect on IMMEM XIII and ASM NGS, comparing conference formats and the scientific themes running through both meetings. They discuss wastewater surveillance moving into routine public health use, the metadata needed to interpret millions of genomes, and the difficulty of sustaining genomic epidemiology platforms. Their discussion connects lessons from COVID sequencing with practical questions about accessibility, data quality and long-term software support.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 96: IMMEM XIII and ASM NGS conference roundup" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1405835830&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 96: IMMEM XIII and ASM NGS conference roundup on SoundCloud](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs)

## In this episode

### Hybrid conferences and divided attention

Andrew describes hybrid sessions in rooms of 200 or 400 people where switching to an online speaker disrupted the meeting. Audience members appeared to return to their Zoom habits, checking phones rather than engaging with the presentation. Remote speakers lacked visual feedback from the room, while technical barriers made questions and timekeeping difficult. Lee says smaller conferences of fewer than 200 people, with everyone in person, felt pretty nice.

Nabil agrees that some hybrid sessions worked poorly, but argues against losing the accessibility of virtual meetings. Online conferences had allowed researchers from distant places, who might otherwise have been unable to attend, to present strong science. He questions whether resistance reflects an inherently unworkable format or exhaustion after so much virtual participation.

### Different audiences, shared COVID lessons

Nabil characterises ASM NGS as more focused on public health applications, with substantial attendance from US government and public health organisations. IMMEM had a more academic emphasis. He also noticed more formal introductions and use of professional titles at the US meeting, compared with the informal atmosphere at IMMEM in the UK.

Both meetings felt unusually friendly after a long gap in face-to-face conferences. COVID lineage plots and stacked abundance plots were recurring presentation features, but the programme was not entirely dominated by COVID. A repeated question was whether tools and lessons developed for COVID could transfer to other organisms, including whether something like UShER could be used beyond its existing application.

### Wastewater moves towards real-time surveillance

Wastewater was a prominent theme at both meetings. The hosts mention uses beyond COVID, such as tracking polio and Salmonella Typhi, and Andrew recalls an older study of antibiotic resistance genes in wastewater at increasing distances from a hospital. Nabil asks how well approaches that distinguish COVID lineages will work for more nuanced questions or other organisms. The hosts also discuss a practical limitation: sampling centralised sewage cannot represent everyone where septic tanks, latrines or disconnected systems are common. Infrastructure and population density matter, not simply national wealth.

The novelty, they stress, is not wastewater sequencing itself. They recall earlier work using pyrosequencing and 454, including metagenomics of aircraft toilet samples. The change is from isolated academic snapshots to repeated analysis intended to inform public health in real time.

During their COVID sequencing work, hospital samples could reflect infections from two or three weeks earlier. Wastewater surveillance might recover some of that reporting time, rather than waiting for people to become ill enough to enter hospital and have samples collected and sequenced.

### Millions of genomes still need context

The discussion of roughly 14 million COVID genomes returns to a longstanding problem: sequence volume does not compensate for missing contextual metadata. Nabil calls for consistent standards and identifiable data stewards who can answer questions about records. Andrew jokingly proposes machine learning as a universal solution; Nabil says the attempts he has seen are not convincing substitutes for metadata.

For Salmonella, useful context includes collection circumstances, location, disease state, patient or animal outcomes, and sampling position within a factory. Nabil puts sequencing costs at £50–£100 per isolate, making neglected metadata a substantial wasted investment. The hosts also emphasise shared ontologies: collaborators need to agree, for example, where an animal carcass becomes a food product along a processing chain.

### Dates, coordinates and misleading precision

Collection dates receive particular attention. A year-only date, an exact sampling date and a date deliberately shifted to protect privacy are not interchangeable. Excel conversions and US-style date ordering can create further ambiguity. The hosts recommend ISO 8601 formatting, while stressing that users also need to know the precision and provenance of a date.

Lee explains that metadata for rare organisms can risk identifying patients. His group sometimes mixes retrospective isolates into uploads so that upload dates cannot simply be treated as dates of infection.

Coordinates can be equally misleading. A precise-looking location may be an automatically filled country midpoint, an assumed population centre or the address of a public health organisation receiving samples. The practical advice is to check what each field represents before using it for mapping or epidemiological interpretation.

### Who maintains public health platforms?

An unnamed commercial provider ending support prompts a discussion about replacement platforms. Nabil reports interest in open-source, transparent systems that users can control, but asks who will pay for maintenance. Research funding tends to reward new findings rather than the continuing work of keeping infrastructure operational.

The hosts contrast a pipeline written quickly and shared on GitHub with an end-to-end genomic epidemiology platform requiring developers, documentation, technical support and a help desk. Public health deployment adds serious validation, change tracking and consistent results when the same sample is analysed again.

Nabil uses an imagined EnteroBase successor to illustrate the tension between accreditation and a bioinformatician’s wish to keep changing software. Commercial teams can support routine maintenance, but that work offers few academic rewards. Institutional support and public funding are discussed as possibilities; the episode leaves the long-term funding question unresolved.

## Highlights

- [00:01:05](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=1:05) — Which parts of in-person, virtual and hybrid conference formats failed?
- [00:03:42](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=3:42) — Nabil defends the accessibility and wider participation offered by virtual meetings.
- [00:07:26](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=7:26) — ASM NGS and IMMEM differ in audience, formality and public health emphasis.
- [00:10:18](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=10:18) — Recurring COVID lineage plots and questions about transferring COVID tools to other organisms.
- [00:12:41](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=12:41) — Wastewater surveillance attracts attention, alongside questions about its limits.
- [00:15:51](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=15:51) — The shift from retrospective wastewater studies to real-time public health surveillance.
- [00:19:21](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=19:21) — Millions of COVID genomes expose longstanding gaps in contextual metadata.
- [00:23:22](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=23:22) — Defining sampling sites and food-production stages requires agreement between collaborators.
- [00:25:11](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=25:11) — Collection dates need clear precision, provenance and protection against conversion errors.
- [00:29:22](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=29:22) — A commercial platform ending support raises questions about replacements and maintenance funding.
- [00:31:16](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=31:16) — Public health pipelines require validation, documentation and tracked changes.

## In their own words

> a genome is only worth the contextual metadata that goes along with it
>
> — Nabil-Fareed Alikhan, [00:19:40](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=19:40)

> No, I don't want to support the same software for the next 20 years.
>
> — Nabil-Fareed Alikhan, [00:32:48](https://soundcloud.com/microbinfie/immem-xiii-and-asm-ngs#t=32:48)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

## Tools and resources mentioned

Zoom, UShER, 454, pyrosequencing, Excel, GitHub, EnteroBase.

## Questions this episode answers

### What problems did the hosts encounter at hybrid conferences?

They describe reduced audience engagement during remote talks, missing visual cues for speakers, difficult question sessions and overruns. Nabil nevertheless argues that virtual participation improves accessibility and should not simply be abandoned.

### What was new about the wastewater surveillance discussed?

The hosts distinguish established wastewater sequencing research from its growing use for regular, real-time public health reporting. They suggest it can provide an earlier signal than hospital sampling, which in their COVID work could lag infection by two or three weeks.

### What metadata should accompany microbial genomes?

The discussion emphasises collection date, location, sampling context and relevant patient, animal or food-production information. The hosts recommend consistent definitions and ISO 8601 dates, while warning that privacy adjustments and automatically assigned coordinates can make apparently precise values misleading.

### Why is sustaining genomic epidemiology software difficult?

Routine platforms need maintenance, user support, documentation and validation, but academic incentives favour new research and publications. Open-source availability does not resolve the funding problem, and the hosts leave the question of long-term support open.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

We've been busy attending in-person conferences such as IMMEM XIII and ASM NGS so we thought
we'd give you some of our reflections. We discuss waste water surveillance, hybrid conferences
and metadata amongst other things.
