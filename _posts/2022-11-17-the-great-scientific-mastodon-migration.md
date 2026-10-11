---
layout: page
title: 'Episode 94: The great scientific Mastodon migration'
date: '2022-11-17 00:00:00'
link: https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration
episode: '94'
soundcloud_track: '1381583065'
tags:
- microbinfie
- podcast
description: Nabil-Fareed Alikhan explains the costs and moderation of mstdn.science, while Emma Hodcroft discusses why scientists are trying Mastodon.
excerpt: Nabil-Fareed Alikhan explains the costs and moderation of mstdn.science, while Emma Hodcroft discusses why scientists are trying Mastodon.
headline: 'Scientists move to Mastodon: running mstdn.science'
guests:
- Emma Hodcroft
topics:
- mastodon
- scientific social media
- twitter migration
- federated networks
- server administration
- hosting costs
- content moderation
- science communication
faq:
- q: What is mstdn.science?
  a: It is the Mastodon instance Nabil and Duncan set up initially for bioinformaticians, microbial genomics researchers and technically minded microbiologists. By the recording, it had almost 2,000 users and was attracting researchers from other disciplines.
- q: How much did running the Mastodon server cost?
  a: Nabil estimated roughly £100 per 1,000 users per month, up to a point. He stressed that costs also depend on interactions and connections with other instances, so user numbers alone do not determine the bill.
- q: Can users on different Mastodon servers interact?
  a: Yes. Nabil explains that users can follow, read and reply to accounts on other servers. His instance communicates with general-purpose servers as well as scientific ones, although he blocks some domains for moderation.
- q: Did the panellists think Mastodon would replace Twitter?
  a: They did not reach a firm prediction. Nabil thought it could serve scientific discussion without reproducing all of Twitter’s capabilities, while Emma valued it as a backup and welcomed its science-focused atmosphere.
---

*Scientists move to Mastodon: running mstdn.science*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss scientists’ move from Twitter to Mastodon, joined by Emma Hodcroft. Nabil explains how an experimental server grew to almost 2,000 users, while Emma describes joining as insurance against Twitter’s uncertain future. They examine hosting costs, moderation and whether a federated network can support scientific exchange.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 94: The great scientific Mastodon migration" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1381583065&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 94: The great scientific Mastodon migration on SoundCloud](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration)

## In this episode

### Why scientists were trying Mastodon

This November 2022 discussion follows a surge of interest in Mastodon after Elon Musk’s purchase of Twitter. Andrew describes Twitter as valuable for sharing papers, interacting with scientists and making friends since 2007. Nabil argues that the departures also reflect longer-standing dissatisfaction: a service once centred on people users chose to follow had become more dominated by promoted content, news and gossip.

Nabil introduces Mastodon as a free, open web application for short posts. Its distinguishing feature is communication between separately operated servers, or instances. An account on one server can follow, read and reply to accounts elsewhere, rather than being confined to that server’s membership.

### An experiment grows to almost 2,000 users

Nabil and Duncan set up mstdn.science to experiment with the technology. Duncan bought the domain, and Nabil configured a virtual server. They expected perhaps 50–100 bioinformaticians, microbial genomics researchers and technically minded microbiologists to join, share messages and exchange memes.

By the recording, almost 2,000 users had signed up. Nabil had noticed a Nobel laureate, journals and researchers from disciplines including pharmacology, immunology and history. Other science-focused instances were also receiving new users. He sees possible uses beyond a general social network: conferences, universities, research councils or interest groups could operate their own spaces. These are possibilities he raises, not deployments the episode documents.

### Hosting costs and the email problem

Nabil thinks the main virtual machine has 4 GB of memory and four virtual CPUs, with pictures and other static content stored separately in an object-storage bucket. He can resize the virtual server as demand grows rather than replacing physical hardware.

Asked about monthly costs, he gives a rough estimate of £100 per 1,000 users, up to a point. The relationship is not strictly linear: following and interacting with accounts on other servers creates additional work. Reliable email delivery is a particular difficulty, because anti-spam controls complicate even confirmation and password-reset messages.

There is no settled long-term funding model. Some users have contributed money, and Nabil discusses donation-based monthly subscriptions used by other instances. He also notes that Mastodon does not provide a built-in advertising system.

### Federation creates work behind the scenes

Nabil describes a stack using JavaScript and Ruby, PostgreSQL as the database, Redis as an in-memory cache and a background job processor. With roughly 200–300 people joining each day, evening activity sometimes exhausted available web-server threads. Visible posting activity understated the workload: the server had processed about 1.5 million jobs in a week, including work to retrieve and replicate content from other instances.

He does not restrict federation to science servers, since scientists also have accounts on general instances such as mastodon.social. However, he has blocked some domains because of their content, not to reduce traffic. Operating an instance therefore involves moderation as well as technical maintenance, including dealing with spam, bot accounts and unsafe material.

### Finding people and choosing a new feed

Andrew describes using websites that connect to Twitter and Mastodon, identify contacts and produce a CSV file to import. They do not find everyone, but can provide a starting point, particularly when people put their Mastodon handle somewhere in their profile. Nabil prefers making fresh choices about whom to follow.

The discussion also acknowledges that finding people and searching for content can be harder on Mastodon. Nabil compares this with an earlier internet where locating useful material required more effort. Emma suggests that large, accessible platforms first demonstrated the value of microblogging; users may now be willing to do more work to participate in a decentralised version.

### A backup, not necessarily a replacement

Emma describes joining Mastodon as bet hedging rather than announcing a complete departure from Twitter. She values a network that cannot be controlled entirely by one person, where users can move elsewhere if one part becomes unsuitable.

Nabil cautions against expecting a one-for-one Twitter replacement. He points to delays between independent servers and the difficulty of providing comprehensive search without central control of the data. Nevertheless, Mastodon could suit academics sharing and discussing papers. Emma is more optimistic about its atmosphere: she enjoys the scientific conversation and reduced pressure to pursue algorithmic visibility. Neither treats its future as settled, and Emma separates Mastodon’s prospects from Twitter’s eventual fate.

## Highlights

- [00:01:04](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=1:04) — Nabil explains Mastodon and communication between independent servers.
- [00:04:13](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=4:13) — How Nabil and Duncan launched mstdn.science and attracted almost 2,000 users.
- [00:07:54](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=7:54) — Virtual-server resources, object storage and the difficulty of sending account emails.
- [00:09:04](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=9:04) — Why hosting costs depend on cross-server activity as well as user numbers.
- [00:10:12](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=10:12) — Donations and possible subscription-based funding for an instance.
- [00:12:10](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=12:10) — Growing demand, exhausted server threads and the application’s technical stack.
- [00:14:34](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=14:34) — Federating with general servers while blocking domains for moderation.
- [00:17:32](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=17:32) — Emma explains joining Mastodon as a backup against Twitter’s uncertain future.
- [00:20:17](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=20:17) — Emma considers how large platforms introduced people to the value of microblogging.
- [00:22:47](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=22:47) — Andrew describes finding Twitter contacts through CSV import tools.
- [00:23:54](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=23:54) — Nabil considers Mastodon’s future, federation delays and search limitations.
- [00:25:55](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=25:55) — Emma welcomes the scientific atmosphere and considers whether the migration will last.

## In their own words

> I mean, the most expensive thing is actually getting a mail server that works.
>
> — Nabil-Fareed Alikhan, [00:07:54](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=7:54)

> For me, it's a little bit of bet hedging.
>
> — Emma Hodcroft, [00:17:32](https://soundcloud.com/microbinfie/the-great-scientific-mastodon-migration#t=17:32)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Emma Hodcroft** (guest)

Also mentioned: Duncan, Elon Musk.

## Tools and resources mentioned

Mastodon, Twitter, PostgreSQL, Redis.

## Questions this episode answers

### What is mstdn.science?

It is the Mastodon instance Nabil and Duncan set up initially for bioinformaticians, microbial genomics researchers and technically minded microbiologists. By the recording, it had almost 2,000 users and was attracting researchers from other disciplines.

### How much did running the Mastodon server cost?

Nabil estimated roughly £100 per 1,000 users per month, up to a point. He stressed that costs also depend on interactions and connections with other instances, so user numbers alone do not determine the bill.

### Can users on different Mastodon servers interact?

Yes. Nabil explains that users can follow, read and reply to accounts on other servers. His instance communicates with general-purpose servers as well as scientific ones, although he blocks some domains for moderation.

### Did the panellists think Mastodon would replace Twitter?

They did not reach a firm prediction. Nabil thought it could serve scientific discussion without reproducing all of Twitter’s capabilities, while Emma valued it as a backup and welcomed its science-focused atmosphere.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

Over the past few weeks scientists have been swapping Twitter for Mastodon. Our very own Nabil-
Fareed Alikhan talks about his experience with setting up and running a Mastodon server called
<https://mstdn.science> which is one of the places where scientists have moved over to. We are
joined by Emma Hodcroft to get an independent scientists view on the whole thing.

In the MicroBinfie podcast, Andrew and Nabil discuss the migration of academics from Twitter to
a new platform called Mastodon, with Nabil playing a significant role in this shift. According
to Nabil, Mastodon is a free and open web application designed for micro-blogging. It enables
integration and communication between servers, allowing the users to follow, reply, or read
content from other servers.

The migration happened after Elon Musk bought Twitter and made significant changes that
concerned people about freedom of speech and democracy. In response, Nabil and Duncan set up
their own Mastodon instance called <https://mstdn.science> initially planning to create a
social network for bioinformaticians, microbial genomics people, and tech-savvy
microbiologists. Expected to have only 50-100 users, many more scientists, including Nobel
Laureates, journals, and scientists from other disciplines, joined, and Nabil's instance now
has almost 2000 users.

Meanwhile, other instances around science, like genomic.social or ecoevo.social, also saw a
surge in sign-ups. In terms of resources, Nabil and Duncan's virtual server have almost 2000
users costing around £100 per 1000 users, depending on how much interaction and following goes
on.

The Mastodon network replicates content from other instances, spawning many jobs, even if a
user's account doesn't change much. Nabil does not limit which instances of Mastodon
communicate with his site but does block domains serving unwanted or unsafe content. Even
though the Mastodon network can crash and burn, Nabil thinks it could still work in the long
run.

The podcast contributors suggest that Twitter's recent changes have left some users feeling
dissatisfied, leading them to Mastodon, which is a decentralized social media platform. Some
dodgy servers have been blocked by Mastodon for moderation, and people have moved from Twitter
to Mastodon as a total replacement for Twitter. Mastodon has become a "sign" for fed-up users.

According to Emma, who recently moved from Twitter to Mastodon, Mastodon is a hedge against
Twitter's unknown future. Mastodon's decentralized platform allows for a shift of power towards
content and interaction, not available in a centrally controlled platform. Mastodon may not
replace Twitter as a one-for-one replacement, but it fits certain use cases, such as a place
for academics to complain about papers.

Mastodon's success is not dependent on Twitter's fate but rather on what "crazy ideas" Twitter
comes up with in the future, Emma argues. While Mastodon may never be quite the same as
Twitter, it could be even better.
