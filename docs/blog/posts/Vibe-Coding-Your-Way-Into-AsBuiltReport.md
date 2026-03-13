---
draft: false
date: 2026-03-14
authors:
  - Tim
categories:
  - General
tags:
  - contributing
  - ai
  - open source
  - vibe coding
  - github copilot
  - claude
  - gemini
slug: Vibe-Coding-Your-Way-Into-AsBuiltReport
---

# Vibe Coding Your Way Into AsBuiltReport

Something has shifted in the last couple of years. The barrier to writing working code (real, functional, useful code) has dropped dramatically. Not because the problems have gotten simpler, but because the tools available to help you solve them have gotten remarkably capable. AI-assisted development is no longer a curiosity or a shortcut for beginners. It is a genuine productivity accelerator that experienced engineers use every day.

Which means the old excuses for not contributing to AsBuiltReport no longer hold up. Not the "I'm not a PowerShell expert" excuse. Not the "I don't know the codebase" excuse. Not even the "I wouldn't know where to start" excuse. If you have ever thought about fixing an issue or adding something useful to the project and talked yourself out of it, this post is for you.

<!-- more -->

## What Is Vibe Coding?

If you haven't heard the term "vibe coding" by now, where have you been? It is the practice of working with an AI tool (Claude, GitHub Copilot, Google Gemini, take your pick) in an iterative, conversational way. You describe what you want to achieve, the AI scaffolds an approach, you review it, steer it, test it, and refine it. You are not handing the wheel over entirely. You are collaborating with a tool that happens to know a lot about PowerShell, Git, and whatever platform you are trying to document.

I have been doing this for the past six months and the results speak for themselves. I used it to add multilingual support to AsBuiltReport. I used it to resolve issues in report modules that had me stumped for years. I am even using it to write this blog post. If it can do all of that, it can certainly help you make your first contribution.

## The Barrier Was Real. Now It Isn't.

Back in 2023, I wrote honestly about the challenges AsBuiltReport was facing. One of the things I said was that I believed there was a large amount of untapped potential in the user base. People who used the reports, saw things that could be better, but did not take the step of fixing them. The [User Guide](https://www.asbuiltreport.com/user-guide/quickstart/) and [Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/) now cover that gap, and yes, AI helped write those too. But partly it was a genuine skills gap. Contributing to a PowerShell framework is not the same as writing a quick automation script for your own use.

That gap has not disappeared, but it is a lot easier to close than it used to be. An AI tool can explain an unfamiliar codebase section by section. It can suggest how to retrieve a specific piece of data from an API you have never used before. It can write the scaffolding, handle the edge cases you haven't thought of yet, and help you understand why something isn't working. The cognitive load of starting is dramatically lower than it was two years ago.

## No More Excuses

Let's be direct about the objections, because I have heard them all.

**"I'm not a PowerShell expert."** You do not need to be. You need enough familiarity to read the output the AI produces and tell whether it looks right. Describe what you want to achieve, ask it to explain anything you do not follow, and iterate. The [Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/) gives you the structural framework and the AI helps you fill it in.

**"I don't know the codebase."** Neither did anyone else before they looked at it. Ask your AI tool of choice to explain how a section of an existing module works. Point it at the function you are trying to modify and ask what it does. You will have a working mental model in minutes, not days.

**"I don't have time to learn Git and GitHub."** GitHub Copilot lives inside your editor. Claude can walk you through forking a repository, creating a branch, committing your changes, and opening a pull request, step by step, in plain English. The workflow is documented, the AI knows it, and the community on [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"} is happy to help if you get stuck.

**"What if I break something?"** That is what the branching model and pull request review process are for. Nothing you submit goes directly into a release without being reviewed. The safety net is built in.

## What This Means for AsBuiltReport Specifically

AsBuiltReport's modular architecture works in your favour here. Each report module is a self-contained repository. You do not need to understand the entire framework to contribute to one module. You can scope your contribution tightly. A missing data point, a broken query, a section that hasn't kept pace with a vendor's updated API. You can work entirely within that boundary.

There are gaps across the project. There always are. Platforms that users work with every day that don't have a report module yet. Existing modules where specific configuration data is not captured. Fields that were relevant to an older product version that need updating. If you are working with an environment that AsBuiltReport touches, you almost certainly know of something that could be better. That knowledge is the starting point.

The project is also not asking you to figure it out alone. The [Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/) covers everything from repository structure and naming conventions through to code formatting and pull request expectations. [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"} is the right place to share what you are thinking about before you write a single line of code. Combine those resources with a capable AI tool and the combination is genuinely powerful.

## The Vibe Coding Contribution Loop

If you are not sure where to begin, here is the loop that works:

1. **Find something that bothers you.** A data point missing from a report you run regularly. A platform you use that has no AsBuiltReport module. An issue in the GitHub repository that has been sitting open.
2. **Read the relevant code with AI assistance.** Open the module, point your AI tool at the section you want to change, and ask it to explain what is happening. Ask follow-up questions until the structure makes sense.
3. **Describe what you want to build.** Let the AI scaffold an initial approach. Review it carefully, because you are the one who knows whether the output is accurate for your environment.
4. **Test against a real environment.** This part is yours. Run the report, check the output, iterate until it is right.
5. **Follow the Developer Guide conventions** for branching, commit messages, and pull request structure. The AI can help you write a clear PR description.
6. **Submit and engage with the review.** The review process is there to help, not to gatekeep. Feedback is normal and the community is constructive.

!!! tip
    AI tools are also excellent at writing commit messages and pull request descriptions. If you are unsure how to summarise your change clearly, describe it to your AI tool and ask it to draft the message for you.

## Final Thoughts

The tools available to developers today have genuinely changed what is possible for a motivated contributor, regardless of prior experience. AsBuiltReport has always had more users than contributors, and I understand why. The gap between using a tool and improving it can feel wide. But that gap is narrower now than it has ever been.

If there is an environment you document every day that AsBuiltReport does not yet cover, that is your opportunity. If there is a report you use regularly that is missing something you care about, that is your opportunity too. The project is open, the documentation exists, the community is active, and the AI tools are ready.

Start with the [Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/). Bring your questions to [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"}. Browse the [open issues](https://github.com/AsBuiltReport/){:target="_blank"} across the repositories and find something labelled `good first issue` or `help wanted`.

There has never been a better time to contribute. The vibe is right.

Oh, and this blog post? I started it at 7:30am on a Saturday, and it's done by 7:38am. Eight minutes, on a Saturday! If it were me, I'd still be on the first paragraph.
