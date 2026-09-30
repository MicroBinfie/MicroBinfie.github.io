---
layout: page
title: 'Episode 35: The Wandering Bioinformatician'
date: '2020-11-26 00:00:00'
link: https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician
episode: '35'
soundcloud_track: '908307031'
tags:
- microbinfie
- podcast
description: 'Phil Ashton on bioinformatics in Vietnam and Malawi: metered data, power cuts, Salmonella surveillance and plans for ETEC research.'
excerpt: 'Phil Ashton on bioinformatics in Vietnam and Malawi: metered data, power cuts, Salmonella surveillance and plans for ETEC research.'
headline: 'Phil Ashton: bioinformatics from Vietnam to Malawi'
guests:
- Phil Ashton
topics:
- microbial bioinformatics
- research infrastructure
- malawi
- vietnam
- fungal genomics
- salmonella typhi
- antimicrobial resistance
- etec
- research careers
- covid-19
faq:
- q: How does Phil Ashton run bioinformatics analyses from Malawi?
  a: He uses MRC CLIMB for remote computation and connects from home over 4G MiFi. At about a dollar per gigabyte, data transfer costs make it important to avoid downloading large datasets locally, even though the connection is fast enough for SSH and web browsing.
- q: Which Salmonella projects are discussed?
  a: Phil describes a Salmonella Typhi vaccine study involving 30,000 children, with follow-up monitoring and isolates for sequencing. He also discusses invasive non-typhoidal Salmonella and an XDR outbreak in the paediatric nursery at Queen Elizabeth Central Hospital.
- q: How are SNP-sites and Genotyphi used in the episode?
  a: Phil describes using PHE pipelines to produce SNP calls and consensus FASTA sequences, followed by SNP-sites to extract variable positions for phylogenetics. He and Lee also discuss Genotyphi as a useful way to give researchers consistent terminology for typhoid clades.
- q: What ETEC research does Phil propose?
  a: He is considering a prospective study of healthy children and children with diarrhoea in a high-burden country. Proposed work includes collecting stool samples, looking for genetic associations with illness through pathogen GWAS, and potentially collaborating with an immunologist.
---

*Phil Ashton: bioinformatics from Vietnam to Malawi*

Phil Ashton joins the hosts to discuss moving from the UK to Vietnam and then Malawi, and how infrastructure and family decisions shape his research. The conversation covers remote computing on metered mobile data, Salmonella Typhi vaccination and genomic surveillance, and a proposed ETEC project. It connects the practicalities of working abroad with questions about antimicrobial resistance, bacterial lineages and diarrhoeal disease.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 35: The Wandering Bioinformatician" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/908307031&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 35: The Wandering Bioinformatician on SoundCloud](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician)

## In this episode

### From the UK to Vietnam and Malawi

Phil and his wife married in September 2016 and moved to Ho Chi Minh City three or four days later. Her PhD viva, their wedding and the move across continents all happened within about six weeks. He describes the decision as an opportunity to try living elsewhere rather than a carefully planned career strategy.

A tweet from Steve Baker advertising six to twelve months of work on fungal genomes led to the Vietnam job. Phil wanted to switch kingdoms: he felt fungal bioinformatics was roughly five to eight years behind bacterial bioinformatics in its development. His work focused on cryptococcal meningitis, a fungal disease caused by Cryptococcus neoformans that primarily affects people with HIV.

The next move was for his wife’s job as lead molecular biologist at the unit in Malawi. They alternate whose career determines their location. Her three-year contract brought them to Blantyre, where Phil arrived just before international flights were cancelled during the pandemic.

### Metered data, power cuts and remote computing

Working mainly from home in Malawi, Phil uses a 4G MiFi connection costing about a dollar per gigabyte. The connection itself is good: he reports speeds around 50 megabits per second. The constraint is the cost of transferring large files, so downloading BAM files for visual inspection is something to think carefully about rather than do automatically.

Power cuts were more or less daily when he arrived. He describes load shedding lasting six to eight hours and links the electricity shortage to dependence on hydropower, particularly during the dry season. A household inverter system with several large batteries keeps lower-power essentials running, including laptop and phone charging, but not appliances such as a washing machine.

Phil runs his analyses on MRC CLIMB, which he calls invaluable to his work. SSH and web browsing are manageable over his connection; the practical challenge is arranging workflows so that large datasets do not have to pass through his local computer.

### Salmonella surveillance and typing

Phil’s main work in Malawi concerns Salmonella Typhi and invasive non-typhoidal Salmonella, working with Professor Melita Gordon. He describes a study immunising 30,000 children against Salmonella Typhi with a new vaccine, followed by monitoring to assess its effectiveness. The resulting isolates provide material for sequencing and investigating resistance.

He also discusses an XDR non-typhoidal Salmonella outbreak in the paediatric nursery at Queen Elizabeth Central Hospital, which is affiliated with MLW. Asked during the conversation whether this is the same XDR seen in Pakistan, he explains that it is a non-typhoidal strain, and that South Asia is well ahead when it comes to drug-resistant typhoid. Phil contrasts the frequent ciprofloxacin resistance seen in typhoid associated with travel to the Indian subcontinent with the lower level of resistance he describes in Africa. He stresses that further resistance would worsen an already difficult situation.

For analysis, Phil uses PHE pipelines to go from reads to SNP calls and consensus FASTA sequences, then SNP-sites to extract variable positions for phylogenetics. He also uses Genotyphi, sometimes receiving data on which collaborators have already run it. The discussion values typing systems that let researchers use consistent names for clades. Lee says he is using Genotyphi in his own project after finding it through a GitHub search.

### ETEC as a fellowship direction

Looking towards research independence, Phil is considering a fellowship focused on E. coli diarrhoea, particularly ETEC. Its incomplete characterisation is part of the attraction: he notes that it has not been well characterised, especially through a deep dive in a single high-burden country.

Andrew describes a paper defining eight ETEC lineages with hand-curated and hand-annotated reference genomes. The discussion connects this with an earlier ETEC study published in Nature Genetics in 2014. Different lineages have different combinations of virulence genes, and ETEC can be found in both healthy children and children with diarrhoea.

Phil proposes a prospective study collecting stool samples from healthy and sick children, with the relevant ethical permissions. A pathogen genome-wide association study could look for genes associated with illness rather than healthy carriage. He is also interested in adding immunology and finding an immunologist to collaborate with. These are proposed directions, not results from a completed study.

### Building a career and sharing ideas

Phil’s initial position in Malawi is a one-year contract, secured through earlier collaboration with a researcher at the University of Liverpool who also works closely with his new collaborator. That short appointment sits alongside his wife’s longer contract and his own ambition to move towards independence.

When the hosts point out that he is describing a fellowship idea publicly, Phil argues for discussing ideas rather than keeping them secret. Delivering a project, he says, is harder than coming up with its premise. He is similarly open about future locations: the work brought the family to Vietnam and Malawi, rather than a fixed list of countries they wanted to live in.

### COVID-19 in the background

In this episode, released in November 2020, Phil says he has done no COVID-19 work himself, while his wife’s work is entirely focused on it. He had expected Vietnam’s proximity and connections to China to make it an early centre of transmission, but praises its public health response.

Andrew announces that a project with Zimbabwe has sequenced 97 genomes in the COVID-19 discussion. He mentions interesting findings without describing specific genomic results. Phil also raises an unresolved question at the time: why mortality in Africa appeared relatively low even after accounting for population age structure. He explains that he chose not to engage professionally with COVID-19 when so many other bioinformaticians were already working on it.

## Highlights

- [00:01:14](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=1:14) — Marriage, a PhD viva and a move to Vietnam within six weeks
- [00:02:47](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=2:47) — A tweet leads to fungal genomics work on Cryptococcus neoformans
- [00:06:40](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=6:40) — Moving to Malawi for his wife’s molecular biology role
- [00:07:29](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=7:29) — Working from home with metered 4G data and daily power cuts
- [00:11:02](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=11:02) — MRC CLIMB as an essential remote computing resource
- [00:12:48](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=12:48) — Avoiding large downloads to a local computer
- [00:17:09](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=17:09) — Balancing organisational research priorities with academic interests
- [00:17:36](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=17:36) — A one-year appointment and plans for an E. coli diarrhoea fellowship
- [00:19:31](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=19:31) — Eight ETEC lineages and curated reference genomes
- [00:22:12](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=22:12) — Sharing research ideas openly rather than keeping them secret
- [00:23:16](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=23:16) — Letting research opportunities guide future international moves
- [00:24:48](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=24:48) — A COVID-19 project with Zimbabwe has sequenced 97 genomes

## In their own words

> Coming up with an idea for a project is not the hard bit of the project, right?
>
> — Phil Ashton, [00:22:12](https://soundcloud.com/microbinfie/35-the-wandering-bioinformatician#t=22:12)

## Who is talking

- **Phil Ashton** (guest, MLW, Blantyre, Malawi)
- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)

Also mentioned: Steve Baker, Melita Gordon.

## Tools and resources mentioned

MRC CLIMB, SSH, SNP-sites, Genotyphi, pathogen GWAS.

## Questions this episode answers

### How does Phil Ashton run bioinformatics analyses from Malawi?

He uses MRC CLIMB for remote computation and connects from home over 4G MiFi. At about a dollar per gigabyte, data transfer costs make it important to avoid downloading large datasets locally, even though the connection is fast enough for SSH and web browsing.

### Which Salmonella projects are discussed?

Phil describes a Salmonella Typhi vaccine study involving 30,000 children, with follow-up monitoring and isolates for sequencing. He also discusses invasive non-typhoidal Salmonella and an XDR outbreak in the paediatric nursery at Queen Elizabeth Central Hospital.

### How are SNP-sites and Genotyphi used in the episode?

Phil describes using PHE pipelines to produce SNP calls and consensus FASTA sequences, followed by SNP-sites to extract variable positions for phylogenetics. He and Lee also discuss Genotyphi as a useful way to give researchers consistent terminology for typhoid clades.

### What ETEC research does Phil propose?

He is considering a prospective study of healthy children and children with diarrhoea in a high-burden country. Proposed work includes collecting stool samples, looking for genetic associations with illness through pathogen GWAS, and potentially collaborating with an immunologist.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Have you ever wanted to pack in your job and move to the other side of
the world? We chat to Phil Ashton on his travels as a
bioinformatician, going from the UK to Vietnam to Malawi. We also
wander into microbial bioinformatics and his passion for Salmonella
and ETEC.  Papers mentioned: SNP-sites:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5320690/ Genotyphi:
https://www.nature.com/articles/ncomms12827/ ETEC lineages:
https://www.biorxiv.org/content/10.1101/2020.07.16.203430v1.abstract
