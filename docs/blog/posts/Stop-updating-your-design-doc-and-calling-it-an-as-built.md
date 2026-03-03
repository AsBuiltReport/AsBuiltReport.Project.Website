---
draft: false
date: 2026-03-03
authors:
  - Tim
categories:
  - General
slug: Stop-Updating-Your-Design-Doc-and-Calling-It-an-As-Built
---

# Stop Updating Your Design Doc and Calling It an As-Built

In nearly 20 years delivering enterprise infrastructure solutions, there is a common misconception I have encountered time and again — that an as-built document is simply a design document updated to reflect what was built, a past-tense version of the original plan. It is an understandable assumption, but it is fundamentally wrong. The two documents serve entirely different purposes, capture entirely different information, and should never be confused with one another.

This distinction matters. Getting it wrong means critical information goes undocumented, environments become harder to support, and the as-built loses its value as a source of truth.

## What a Design Document Is For

A design document is created before a single component is deployed. Its purpose is to record **intent** — to describe what will be built, why it will be built that way, and how the proposed solution meets the requirements of the business.

A well-structured design document will typically capture:

- **Business requirements** and how the proposed architecture meets them
- **Assumptions** made during the design process — for example, that a specific network segment will be available, or that a licensing tier will be in place
- **Constraints** that influenced design decisions, such as budget limits, existing infrastructure, or compliance obligations
- **Risks** identified and how they are mitigated
- **Planned architecture** — topology diagrams, component lists, configuration standards
- **Design decisions and justifications** — the specific choices made during the design process and the reasoning behind them, such as why a particular platform, topology, or configuration approach was selected over alternatives

Critically, a design document captures the **why**. Why was this platform chosen over an alternative? Why is the solution architected this way? Why were certain trade-offs made? This reasoning is invaluable for future engineers who need to understand the intent behind a system — but it belongs in the design document, not the as-built.

## What an As-Built Document Is For

An as-built document is not written in advance. It is generated **from the system itself**, after deployment, and its sole purpose is to record reality — what was actually deployed, how it is configured, and what it looks like right now.

An as-built document does not need to explain the *why*. Its focus is entirely on the *is*.

A thorough as-built document will capture:

- The actual deployed configuration of every component
- Network addressing, VLANs, and routing as they exist in the environment
- Storage configurations, datastores, and volume assignments
- Identity and access configurations
- The current state of services, roles, and features

And here is the key point that the "updated design" misconception completely misses.

## The Information That Cannot Exist Until the System Is Built

A design document is authored before the environment exists. By definition, it cannot contain information that is only generated at provisioning time. Yet this is precisely the information that is most valuable in an as-built document.

Consider the following examples:

**VMware environments:**
- Virtual machine instance UUIDs assigned at creation
- Managed Object Reference IDs (MOREFs) for vCenter objects
- Datastore URNs
- MAC addresses assigned to virtual network adapters

**Microsoft Azure:**
- Resource GUIDs for every deployed resource
- Subscription and tenant IDs
- Managed identity object IDs
- Auto-generated storage account endpoints and connection strings
- Deployment correlation IDs

**Active Directory and Windows:**
- Security Identifiers (SIDs) for users, groups, and computer accounts
- ObjectGUIDs for directory objects
- GPO GUIDs

None of these values exist at design time. No engineer can write them into a design document, and no amount of updating a design document to past tense will produce them. They can only be captured by interrogating the live system after deployment.

This is why an as-built document must be **generated from the system**, not authored by hand. Manual documentation of these values is error-prone, time-consuming, and almost always incomplete.
<!-- more -->

## A Real-World Example

Consider a large-scale VMware deployment across multiple datacentres. The design document will describe the intended cluster topology, the networking architecture, the storage layout, and the vSphere configuration standards. It will explain why certain design decisions were made, reference the business requirements, and document the assumptions and risks.

Once the environment is deployed, that design document becomes a historical artefact. It describes what was intended. The as-built document describes what exists. In a project of any complexity, there will always be deviations — configurations adjusted during deployment, IP addresses reallocated, resource names that followed a slightly different convention than planned. The as-built captures these realities.

More importantly, the as-built captures every GUID, every UUID, every system-generated identifier that now forms part of the operational fabric of the environment. These are the values that support engineers need when troubleshooting, that security teams need during audits, and that migration teams need when planning future change.

## Automating the As-Built

This is exactly the problem that [AsBuiltReport](https://www.asbuiltreport.com) was built to solve.

AsBuiltReport is an open-source PowerShell framework that connects directly to live infrastructure — VMware vSphere, Microsoft Azure, Windows Server, networking platforms, and more — and generates structured, professional as-built documentation automatically. Rather than asking engineers to manually capture hundreds of configuration values, AsBuiltReport interrogates the environment and produces accurate, consistent documentation in minutes.

The result is an as-built document that contains the information a design document never could: the real hostnames, the actual GUIDs, the live configuration state of every component in the environment. It is a forensic record of reality, not a sanitised version of a plan.

With over 240,000 downloads from the PowerShell Gallery, AsBuiltReport has become a widely adopted tool across infrastructure teams who understand that documentation quality directly impacts operational resilience.

### Becoming Familiar with a New Environment

One of the most immediate use cases for AsBuiltReport is onboarding. When an engineer inherits responsibility for an environment they have never worked in — whether joining a new organisation, taking over from a colleague, or engaging with a client's infrastructure for the first time — accurate as-built documentation is invaluable. Rather than spending days manually exploring the environment and piecing together a picture of what exists, AsBuiltReport can produce a comprehensive snapshot in minutes. That snapshot becomes the starting point for understanding the environment's topology, configuration standards, and current state.

### Auditing and Compliance

As-built documentation plays a critical role in security audits, compliance reviews, and internal governance processes. Auditors need evidence of what is deployed and how it is configured — not what was planned. AsBuiltReport provides a consistent, repeatable output that can be generated on demand, ensuring that the documentation presented during an audit accurately reflects the environment at that point in time. For organisations operating under frameworks such as ISO 27001, SOC 2, or government security standards, this capability is not a nice-to-have — it is essential.

### Disaster Recovery and Environment Rebuild

An as-built document is an essential component of any disaster recovery strategy. In the event of an unplanned change — a misconfiguration, a failed update, or an unexpected system behaviour — having an accurate record of how the environment was configured before the incident can be the difference between a swift recovery and hours of guesswork. Engineers can refer directly to the as-built to understand what the environment looked like at a known good state and work methodically to restore it.

In a full disaster recovery scenario, the value is even greater. Rebuilding an environment from memory or from an outdated design document is slow, error-prone, and incomplete. An accurate, detailed as-built document — one that captures every configuration value, every system-generated identifier, and every deployed component — provides the blueprint needed to reconstruct the environment with confidence. This is particularly critical in complex environments where the interdependencies between systems, the specific configuration of network components, or the precise values of identifiers like GUIDs and UUIDs must be restored exactly as they were.

### Differential Outputs and Change Tracking

Perhaps one of the most powerful but underutilised use cases is comparing as-built outputs over time. By generating reports at regular intervals — or before and after a change window — teams can produce differential outputs that clearly show what has changed in an environment. This is invaluable for change validation, incident investigation, and identifying configuration drift. If something breaks after a maintenance window, a differential comparison between the pre- and post-change as-built can quickly surface what changed and where. This level of visibility is simply not possible with manually maintained documentation.

## The Bottom Line

A design document and an as-built document are not versions of the same thing. They serve different purposes, are created at different stages of a project, and contain fundamentally different types of information.

- A **design document** captures intent, rationale, and planning — it explains what will be built and why.
- An **as-built document** captures reality — it records what was deployed, how it is configured, and the system-generated information that could not exist until the environment was built.

If your as-built process involves opening a design document and changing verb tenses, you are not producing an as-built. You are producing an incomplete document and leaving critical operational information undocumented.

## Getting Started with AsBuiltReport

AsBuiltReport is free and open source. Whether you are looking to document an existing environment, prepare for an audit, or simply get up to speed on an infrastructure you have inherited, the best place to start is the [Quickstart Guide](https://www.asbuiltreport.com/user-guide/quickstart/), which walks through installation, configuration, and generating your first report.

For those who want to go further — whether that means contributing to an existing report module, building a new one for a platform not yet covered, or extending the framework for your own use case — the [Developer Guide](https://www.asbuiltreport.com/dev-guide/contributing/) provides everything you need to get started. AsBuiltReport is built on a modular architecture, making it straightforward to develop report modules for virtually any infrastructure platform that exposes a PowerShell interface or API.

The project is actively maintained and welcomes contributions from the community. If you are working with infrastructure platforms that are not yet covered, or have ideas for improving existing reports, the project's [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"} is the right place to start that conversation.