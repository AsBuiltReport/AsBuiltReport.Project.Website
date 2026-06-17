---
title: AI Use Policy
description: Guidelines for using AI-assisted tools when contributing to AsBuiltReport
tags:
  - ai
  - contributing
  - development
  - guidelines
---

The AsBuiltReport project encourages contributors to develop code by hand,
drawing on the project's Plaster template, developer documentation, and
existing report modules as their primary references. This hands-on approach
builds genuine understanding of the codebase and produces contributions that
are easier to review, maintain, and extend.

AI-assisted tools (such as GitHub Copilot, ChatGPT, Claude, or similar) are
permitted where they help or enhance that process — for example, to clarify
a vendor API, suggest a table structure, or refine documentation. This page
sets out how AI tools fit into that workflow and the expectations that apply
when they are used.

!!! info "Summary"
    Hand-developed code is encouraged. AI tools are permitted as a supplement
    — to assist and enhance, not to replace the hands-on development process.
    You are responsible for everything you submit, regardless of how it was
    produced.

## Core Principles

### You Own What You Submit

All contributions — whether written by hand or generated with AI assistance —
are submitted under your name and are subject to the same review standards.
Maintainers cannot distinguish AI-generated code from human-written code during
review, nor should they need to. It is your responsibility to understand,
test, and stand behind every line you submit.

### Quality Standards Are Non-Negotiable

AI tools can produce code that looks correct but contains subtle errors,
outdated patterns, or hallucinated API calls. Before submitting a contribution:

- Run [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer){:target="_blank"} and
  resolve all `Warning` and `Error` severity findings
- Follow the [Coding Style Guidelines](contributing.md#coding-style-guidelines)
  exactly — AI output frequently diverges from project conventions and must be
  corrected before submission
- Complete the [Manual Testing Checklist](contributing.md#manual-testing-checklist)
  against a real target system — not a mocked or simulated environment

### Do Not Submit Code You Do Not Understand

If you cannot explain what a function does, why a particular pattern was chosen,
or what data a table renders — do not submit it. AI-generated code you cannot
explain is a maintenance liability for the project team. Maintainers will ask
questions during review; "the AI wrote it" is not an acceptable answer.

## Using the Project's Resources

The project provides everything needed to develop a contribution by hand.
Establishing these foundations first — before writing any code or involving
an AI tool — produces better results and reduces the amount of correction
required later.

**1. Read the developer documentation**

Read the relevant Developer Guide sections before starting work. These define
the conventions, structure, and patterns the project expects:

| Task | Reference |
|---|---|
| Any contribution | [Contributing Guide](contributing.md) |
| Building or extending a report module | [Creating a Report Module](creating-a-report-module.md) |
| Adding charts | [Adding Charts to a Report Module](adding-charts-to-a-report-module.md) |
| Adding diagrams | [Adding Diagrams to a Report Module](adding-diagrams-to-a-report-module.md) |
| Creating a report style | [Creating a Report Style](creating-a-report-style.md) |

**2. Scaffold with the Plaster template**

New report modules should always be created using the
[AsBuiltReport Plaster template](creating-a-report-module.md#scaffolding-your-module-with-plaster).
This generates the correct repository layout, module manifest, configuration
file, and script stubs. Do not ask an AI tool to create this structure
manually — the template is the authoritative starting point.

**3. Study existing report modules**

The [AsBuiltReport GitHub organisation](https://github.com/AsBuiltReport){:target="_blank"}
contains many published report modules. Before writing a new section or
module, review how similar sections are implemented in an existing module.

These same resources are just as useful when working with an AI tool. Sharing
them as context means the tool's output is more likely to follow project
conventions from the start, with less manual correction needed afterwards.

!!! tip "Using project resources with your AI tool"
    Paste the relevant documentation pages into your AI tool's session before
    asking it to generate or review code. Paste an example function from an
    existing module to give the tool a concrete pattern to follow. Some tools
    (such as GitHub Copilot Workspace or Claude Projects) support persistent
    context — upload the relevant pages there so the standards apply
    automatically across your entire session.

## Acceptable Uses

The following uses of AI assistance are consistent with project standards:

| Use Case | Notes |
|---|---|
| Drafting boilerplate or scaffolding | Must be reviewed and corrected to match project conventions |
| Generating `PSCustomObject` table structures | Verify property names match the vendor API |
| Writing or improving inline comments | Comments must remain accurate after edits |
| Drafting or refining documentation | Accuracy must be verified against actual module behaviour |
| Suggesting test cases or edge cases | All test cases must be validated manually |
| Translating report strings for language support | Verify translations with a native speaker where possible |

## What AI Tools Should Not Do

:octicons-x-circle-fill-16:{ .x-circle-fill } DO NOT use AI tools to:

- **Generate an entire report module end-to-end without hands-on development.**
  Report modules require real-environment testing against the target vendor's
  API. A module that has never been run against a live system is not ready for
  contribution.
- **Fabricate sample output, API responses, or configuration values.** All
  data structures in code and documentation must reflect what the vendor API
  actually returns.
- **Bypass the review process.** Generating a large volume of AI-produced PRs
  in quick succession to flood the review queue is not acceptable.
- **Hardcode credentials, secrets, or sensitive data**, whether AI-suggested
  or otherwise. See the [DO NOT](contributing.md#coding-style-guidelines)
  section of the Coding Style Guidelines.
- **Introduce dependencies or imports** that are not already part of the
  project's declared requirements without prior discussion.

## Disclosure

You are not required to declare that you used an AI tool when submitting a
contribution. However, if AI assistance played a significant role — for
example, if the majority of a function or document section was AI-generated —
it is good practice to note this in the PR description. This helps reviewers
calibrate how closely to check for accuracy and convention compliance.

## Licence and Intellectual Property

By submitting a contribution you confirm that, to the best of your knowledge,
the contribution does not infringe third-party intellectual property rights.
AI tools trained on public code can occasionally reproduce protected content
verbatim. If you recognise content in AI output that appears to originate
from a specific third-party source, remove it and write the equivalent
yourself.

All accepted contributions are licensed under the
[MIT Licence](../about/license.md), consistent with the rest of the project.

## In Summary

The project's Plaster template, developer documentation, and existing report
modules give you everything you need to develop a contribution by hand. AI
tools have a role to play alongside those resources — helping you understand
a vendor API, drafting repetitive structures, or refining documentation —
but they work best as a supplement to hands-on development, not a
replacement for it. Every contribution must still be understood, tested
against a real environment, and ready to be defended in review.

If you have questions about whether a particular use of AI assistance is
appropriate, raise it in the
[Discussions board](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"}
before submitting.
