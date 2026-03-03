---
draft: false
date: 2026-03-03
authors:
  - Tim
categories:
  - General
slug: How-I-approach-building-a-new-AsBuiltReport-report-module
---

# How I Approach Building a New AsBuiltReport Report Module

AsBuiltReport did not start as a framework. It started as a single PowerShell script designed to document a VMware vSphere environment. That script became the foundation of what would eventually grow into the VMware vSphere report module, and later, the AsBuiltReport framework itself.

When I built that first script, I was largely figuring it out as I went along. There was no established process, no structured approach, and no playbook to follow. I had a clear idea of what I wanted it to produce, but how I got there was very much an exercise in trial and error. When I made the decision to turn it into a modular framework, the vSphere script largely came along for the ride. It worked, and rebuilding it from scratch alongside everything else was not a priority, so it stayed largely as it was.

As I continued to develop new report modules, it became clear that working without a defined structure was not sustainable. Each new module raised the same questions. How should it be organised? What conventions should it follow? How should the code be structured? That realisation led directly to the creation of the [AsBuiltReport Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/), the foundation that every new report module is now built upon. The vSphere module still exists largely in its original state today, a testament to where the project started and a reminder of why those guidelines exist.

This post covers something different from the Developer Guide. It is about the personal habits and practices I follow when developing a new module, sitting alongside those guidelines rather than replacing them.

<!-- more -->

## Start With a Plan

### Build a Mindmap First

Before I open VS Code, I open a mindmapping tool. A mindmap lets me think through the full shape of the report before committing anything to code. The top-level sections, the subsections within each, and the specific data points that need to be captured at each level.

This step sounds simple but it is genuinely one of the most valuable things I do. It forces me to think about the report as a whole rather than diving straight into one corner of it. It also gives me a visual reference I can return to throughout development, which helps keep the overall structure coherent as the module grows.

### Align to the Vendor's GUI

When mapping out the report structure, I always use the vendor's own management interface as my guide. If a product organises its configuration around a specific set of menus, tabs, or object hierarchies, the report should typically reflect that same structure.

The engineers who will use the report are the same engineers who work in that GUI every day. A report that mirrors the interface they already know is immediately intuitive. A report that imposes its own structure creates friction and makes the documentation harder to navigate.

## Develop Methodically

### Start Small

One of the most common mistakes in module development is trying to build everything at once. I have done it myself, and it invariably leads to a tangled codebase and slow progress.

My approach now is to pick a single section, ideally a straightforward one, and focus entirely on getting that right before moving on. The goal at this stage is not to capture every data point in the report. It is to get the base framework in place, understand the code structure, and establish the patterns that will be repeated throughout the rest of the module. Once that foundation is solid, building out the remaining sections becomes significantly faster and more consistent.

### Use Existing Code as Reference

AsBuiltReport has a growing library of report modules and they are all available on [GitHub](https://github.com/AsBuiltReport/){:target="_blank"}. Before writing any new code, I spend time reviewing existing modules, particularly those that report against similar platforms or have a comparable structure. There is rarely a need to solve a problem from scratch when I or someone else has already solved it in another module.

Referencing existing code also helps maintain consistency across the project, which matters when you want your module to feel like a natural part of the AsBuiltReport ecosystem rather than something bolted on.

If you are new to AsBuiltReport development, I would also strongly recommend getting familiar with [PScribo](https://github.com/iainbrighton/PScribo/){:target="_blank"}, the PowerShell module that powers the report generation engine. PScribo ships with a set of example scripts that demonstrate its capabilities, from basic document structure through to tables, charts, and formatting options. Taking the time to work through those examples before diving into module development will give you a solid understanding of what is possible and how to use the framework effectively.

Once you are more confident with the basics, there are two additional libraries worth exploring. [Diagrammer.Core](https://github.com/rebelinux/Diagrammer.Core){:target="_blank"} provides the capability to generate topology and infrastructure diagrams directly within a report, and [AsBuiltReport.Chart](https://github.com/AsBuiltReport/AsBuiltReport.Chart){:target="_blank"} adds charting and data visualisation support. Both libraries have been developed by [Jonathan Colon](../../about/contributors.md#jonathan-colon), who has also contributed several of the report modules that make use of them. Both can add significant value to a report, but I would recommend getting comfortable with the core module structure first before introducing either of them. Trying to incorporate diagrams or charts too early adds complexity before you have a solid foundation in place.

If you want to see these features in action, the [Microsoft Active Directory](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.AD){:target="_blank"}, [Veeam Backup & Replication](https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VBR){:target="_blank"} and [NetApp ONTAP](https://github.com/AsBuiltReport/AsBuiltReport.NetApp.ONTAP){:target="_blank"} report modules are good examples of both libraries being used effectively.

### Get the Content Right First

AsBuiltReport supports multiple languages, but English (US) is the default language for the framework. When developing a new module, the priority should be getting the content right. The paragraph text, labels, and data points that form the substance of the report. Trying to build multilingual support in parallel with initial development adds unnecessary complexity at the worst possible time.

Get the English content right, get the structure right, and get the report producing accurate output. Language translations can be layered in later once the module is stable.

### Embrace AI

There is no shame in using AI to help develop a report module, and I say that as someone who has leaned on it heavily. Whether it is generating boilerplate code, working through a tricky data structure, suggesting how to handle an edge case, or simply rubber-ducking a problem, AI tools have become a genuine accelerator in my development workflow.

Use them. The goal is a well-built, well-documented report module. How you get there is your business.

## Keep It Clean

### Small Commits Over Large Ones

This is a habit I wish I had developed earlier. Large commits that bundle together dozens of changes across multiple files are a nightmare to review, difficult to roll back, and make it nearly impossible to understand the intent behind any individual change.

Small, focused commits where each one represents a single logical change make the development history readable, code reviews manageable, and debugging far easier. If something breaks, a small commit history makes it straightforward to identify exactly where things went wrong.

### Align to the Developer Guidelines

The [AsBuiltReport Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/) exists for good reason. The conventions it defines around code structure, naming, formatting, and report organisation ensure consistency across every module in the project. Following those guidelines is not a bureaucratic exercise. It is what makes the difference between a module that feels polished and professional and one that feels like it was built in isolation.

If you are developing a module with the intention of contributing it back to the project, alignment to the developer guidelines is essential. It also makes your own code easier to maintain, because you are working within a framework rather than reinventing it.

## Final Thoughts

Building a report module from scratch is a genuinely rewarding exercise. There is something satisfying about connecting to a live environment and watching a polished, structured document appear at the other end. But the quality of that output is directly tied to the quality of the process behind it.

Looking back, the evolution from a single script to a modular framework with defined guidelines was not planned. It happened because the need became obvious over time. The approach I have outlined here is what I follow now, and it has made every module built since faster to develop, easier to maintain, and better received by the people who use it.

If you are thinking about building a module of your own, the [Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/) is the right place to start. And if you have questions or want to discuss your ideas with the community, head over to [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"}. We would love to hear what you are working on.