---
layout: page
title: 'Episode 90: Public health bioinformatics on the cloud with WDL + Terra.bio'
date: '2022-09-29 00:00:00'
link: https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio
episode: '90'
soundcloud_track: '1284274303'
tags:
- microbinfie
- podcast
description: How public health labs use Terra.bio and WDL for SARS-CoV-2 analysis, data sharing and cloud computing without managing their own servers.
excerpt: How public health labs use Terra.bio and WDL for SARS-CoV-2 analysis, data sharing and cloud computing without managing their own servers.
headline: Terra.bio and WDL for public health bioinformatics in the cloud
guests:
- Joel Savinsky
- Danny Park
topics:
- public health bioinformatics
- cloud computing
- sars-cov-2 surveillance
- workflow management
- containerisation
- data sharing
- laboratory capacity
- reproducibility
- compute costs
faq:
- q: What is the difference between Terra, WDL and Cromwell?
  a: Terra provides the user-facing environment for managing data and running analyses. WDL describes workflows, while Cromwell is an execution engine that interprets those descriptions and orchestrates computing resources.
- q: Do public health scientists need command-line skills to use Terra?
  a: The guests describe running existing workflows through a browser without routine command-line work. Users still need to learn data upload, table preparation, workflow inputs and specimen selection; pipeline development and troubleshooting remain areas for bioinformatics expertise.
- q: How quickly could a laboratory start analysing data in Terra?
  a: Savinsky reports onboarding laboratories in 60–90 minutes using prepared, cloned workspaces. This covered the practical steps needed to upload data and launch an existing workflow, rather than building a new pipeline.
- q: Did Terra support Azure and Nextflow when this episode was recorded?
  a: As described at the time of recording, the established setup was WDL on Google Cloud. Azure-backed workspaces and Nextflow support were still under development, while Galaxy pipelines could run with additional setup.
---

*Terra.bio and WDL for public health bioinformatics in the cloud*

Lee Katz, Andrew Page and Nabil-Fareed Alikhan discuss Terra.bio with Joel Savinsky of Theogen Genomics and Danny Park of the Broad Institute of MIT and Harvard. They explain how browser-based access to workflows, cloud computing and data management helped public health laboratories analyse SARS-CoV-2 sequencing data. The conversation covers practical onboarding, collaboration, errors, costs and the platform’s development plans at the time of recording.

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" title="Episode 90: Public health bioinformatics on the cloud with WDL + Terra.bio" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1284274303&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=false"></iframe>

[Listen to Episode 90: Public health bioinformatics on the cloud with WDL + Terra.bio on SoundCloud](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio)

## In this episode

### Terra, WDL and Cromwell do different jobs

Danny Park describes Terra as the web-facing layer through which users manage data, workflows and computing. WDL describes the workflow, while an execution engine such as Cromwell interprets it, starts cloud virtual machines and moves files. These components are modular: Cromwell can operate separately from Terra, and other engines can run WDL.

For a bench scientist with sequencing data and an existing pipeline, Terra removes much of the infrastructure configuration normally required before analysis. Users connect data and workflows within a workspace rather than buying servers or configuring a workflow manager themselves. It does not, however, replace the scientific work of interpreting results.

### Accessibility mattered as much as scale

Park, who works at the Broad but not in Terra’s development group, describes its origins in human and cancer genomics. Growing computing requirements were outpacing local infrastructure, while large datasets were repeatedly copied. His own microbial work had different needs: making pipelines accessible to collaborators, particularly in West Africa through work associated with H3Africa. Once data were uploaded, cloud analysis could continue despite a local power outage, without laboratories maintaining server racks and backup power.

Savinsky describes another barrier: command-line training was difficult to sustain when laboratory staff did not use those skills daily. Terra offered an open-source, browser-based process that could resemble a wet-laboratory SOP. For government approval, his deployments also relied on Google Cloud billing arrangements and assurances that uploaded data contained neither personally identifiable information nor protected health information.

### SARS-CoV-2 surveillance put the model to work

Savinsky recalls public health laboratories initially concentrating on diagnostic testing in early 2020. By that summer, many had sequencing capability but lacked accessible bioinformatics for SARS-CoV-2 surveillance. Existing Nextflow workflows and shared containers provided starting points for WDL implementations; he also mentions the arrival of containers for tools such as Pangolin.

Cloning a prepared Terra workspace meant workflows could already be in place. Training then covered uploading data, creating a data table, selecting specimens and launching analysis. Savinsky reports getting laboratories running in 60–90 minutes. In his examples, batches of 10, 100 or 1,000 specimens produced results in about 40 minutes, and larger runs reached tens of thousands of specimens. He reports more than 40 laboratories using Terra nationally at the time.

### Data tables, permissions and audit trails

Terra workspaces organise both inputs and results. A tab-separated file can establish the initial data table, with specimens represented as rows and results as columns. File entries can point to objects in Google Cloud Storage; Terra renders those addresses as downloadable links, including links to BAM alignment files. Results can also be exported as a tab-separated table.

Workspace permissions control who can view data, perform computations, add users or share access. Savinsky describes this as useful for projects involving state, county and industry partners. Behind the browser interface, execution directories and logs remain available. Bioinformaticians can inspect the actual commands and parameters used, while bench scientists work through the tables.

### Errors and the limits of cloud scale

Spaces in filenames are a recurring problem, but shared workflows make faults easier to identify across laboratories. Savinsky describes fixes moving through GitHub, Dockstore and Terra as new versions. Earlier versions remain available, allowing laboratories to delay changes until they have completed their own verification requirements.

Cloud infrastructure does not eliminate resource limits or interference between workloads. Park distinguishes user mistakes, pipeline defects and infrastructure failures, while noting that responsibility can overlap. More resilient code can accommodate awkward filenames; better resource declarations can prevent memory failures. He also describes Terra’s option to retry with more memory. Public health brings its own scaling challenge: millions of small genomes rather than thousands of human genomes, with specimens arriving continuously.

### Getting started, costs and the roadmap

The guests direct newcomers to Terra.bio, Dockstore and training materials from Terra, the Broad and Theogen. Access uses Google authentication, potentially a free Gmail account, alongside a billing arrangement; trial credits are mentioned as a way to experiment.

Savinsky frames cloud computing as a consumable rather than capital equipment, with budgets tied to specimen throughput. He contrasts analysis costing a couple of dollars per specimen with data generation costing about a hundred dollars.

The roadmap discussion is explicitly time-dependent. At the time of recording, the established route was WDL on Google Cloud. Galaxy pipelines could run with additional effort, while Nextflow support and Azure-backed workspaces were still developing. Savinsky also wanted better public health data management, reporting and integration, rather than treating browser access alone as a complete solution.

## Highlights

- [00:02:45](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=2:45) — Danny Park distinguishes Terra’s web interface from workflow languages and execution engines.
- [00:08:00](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=8:00) — Terra’s human-genomics origins contrast with microbial needs for accessibility and portability.
- [00:11:35](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=11:35) — Joel Savinsky explains command-line training, open-source requirements and government approval.
- [00:18:19](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=18:19) — The pandemic creates demand for accessible SARS-CoV-2 analysis and rapid laboratory onboarding.
- [00:24:18](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=24:18) — Tab-separated data tables connect browser-visible results to cloud files and execution logs.
- [00:26:34](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=26:34) — Workspace permissions support data sharing across public health collaborators.
- [00:27:53](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=27:53) — Filename errors, shared workflow fixes and versioning affect laboratory support.
- [00:33:14](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=33:14) — Millions of small genomes expose different scaling needs and overlapping responsibilities for errors.
- [00:35:02](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=35:02) — The roadmap at the time of recording includes Azure, Nextflow and broader backend support.
- [00:39:31](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=39:31) — New users can start with Google authentication and available Terra and workflow training.
- [00:42:10](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=42:10) — Cloud computing becomes a per-specimen consumable rather than locally maintained capital equipment.

## In their own words

> You can budget for cloud resources based on the number of specimens that you're going to run through your lab in a week.
>
> — Joel Savinsky, [00:42:10](https://soundcloud.com/microbinfie/public-health-bioinformatics-on-the-cloud-with-wdl-terrabio#t=42:10)

## Who is talking

- **Lee Katz** (host)
- **Andrew Page** (host)
- **Nabil-Fareed Alikhan** (host)
- **Joel Savinsky** (guest, Theogen Genomics)
- **Danny Park** (guest, Broad Institute of MIT and Harvard)

## Tools and resources mentioned

Terra.bio, WDL, Cromwell, Google Cloud, Google Cloud Storage, Dockstore, Nextflow, Galaxy, GitHub, BaseSpace, Pangolin, Microsoft Azure, AWS.

## Questions this episode answers

### What is the difference between Terra, WDL and Cromwell?

Terra provides the user-facing environment for managing data and running analyses. WDL describes workflows, while Cromwell is an execution engine that interprets those descriptions and orchestrates computing resources.

### Do public health scientists need command-line skills to use Terra?

The guests describe running existing workflows through a browser without routine command-line work. Users still need to learn data upload, table preparation, workflow inputs and specimen selection; pipeline development and troubleshooting remain areas for bioinformatics expertise.

### How quickly could a laboratory start analysing data in Terra?

Savinsky reports onboarding laboratories in 60–90 minutes using prepared, cloned workspaces. This covered the practical steps needed to upload data and launch an existing workflow, rather than building a new pipeline.

### Did Terra support Azure and Nextflow when this episode was recorded?

As described at the time of recording, the established setup was WDL on Google Cloud. Azure-backed workspaces and Nextflow support were still under development, while Galaxy pipelines could run with additional setup.

*This page was written from a machine transcript of the episode and checked against it. Listen to the episode for the whole conversation.*

## Show notes

90 Public health bioinformatics on the cloud with WDL + Terra.bio by Microbial Bioinformatics
