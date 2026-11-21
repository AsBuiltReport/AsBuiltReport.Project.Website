---
title: AsBuiltReport - Document Your Datacenter With PowerShell
description: Open source PowerShell framework for automated infrastructure documentation in Word, HTML, and Text formats
template: home.html
hide:
  - navigation
  - toc
tags:
  - asbuiltreport
  - powershell
  - documentation
  - automation
  - infrastructure
  - vmware
  - microsoft
  - veeam
  - azure
  - cloud
  - open-source
---

<section class="abr-section" markdown>

## Three commands to a finished report

Everything installs from the PowerShell Gallery. Configuration lives in JSON files you can keep in source control and reuse on a schedule. The [Quickstart Guide](user-guide/quickstart.md) covers each step in detail.
{ .abr-lede }

<div class="abr-steps" markdown>

<div class="abr-step" markdown>

### Install the framework

The core module, plus a report module for each product you want to document.

```powershell
Install-Module AsBuiltReport.Core
Install-Module AsBuiltReport.Microsoft.Azure
```

</div>

<div class="abr-step" markdown>

### Set it up once

Record your company details, then choose how much detail and which health checks each report includes.

```powershell
New-AsBuiltConfig
New-AsBuiltReportConfig -Report Microsoft.Azure
```

</div>

<div class="abr-step" markdown>

### Generate the report

Run it by hand or from a scheduled task. The document is rebuilt from the live system each time.

```powershell
New-AsBuiltReport -Report Microsoft.Azure `
  -Target $TenantId -UseInteractiveAuth `
  -Format Word
```

</div>

</div>

</section>

<section class="abr-section abr-split" markdown>

## Features

<div class="abr-spec" markdown>

-   :octicons-log-16:{ .abr-icon } **Multiple Document Formats**

    Generate reports in one or more document formats, including DOCX, HTML, and Text.

-   :octicons-sliders-16:{ .abr-icon } **Granular Information Level**

    Configure the information level for each report section. You can create a summary report, a fully comprehensive report, or something in between.

-   :octicons-pulse-16:{ .abr-icon } **Health Checks**

    Enable health checks to ==highlight configuration issues== within a report. Toggle individual health checks on or off as required.

-   :octicons-paintbrush-16:{ .abr-icon } **Customised Styling**

    Use the default style or [create your own](dev-guide/creating-a-report-style.md) to match your corporate identity. Set page orientation, text and table formatting with fonts, colours, borders and highlighted cells and rows.

-   :fontawesome-solid-language:{ .abr-icon } **Multilingual Support**

    Comprehensive [multilingual support](dev-guide/creating-a-report-module.md#language-support-implementation) allows reports to be generated in [multiple languages](dev-guide/creating-a-report-module.md#language-configuration), where available.

-   :octicons-apps-16:{ .abr-icon } **Modular Architecture**

    The modular architecture and core framework enables users to use the same in-built commands to generate as-built configuration reports from a library of technology vendors.

-   :octicons-mail-16:{ .abr-icon } **Email Reports**

    Attach and send reports via email to one or more recipients.

</div>

</section>

<section class="abr-section" markdown>

## Use Cases

<div class="abr-grid" markdown>

-   **Compliance Audits**

    Generate point-in-time infrastructure documentation for ISO 27001, SOC 2, PCI-DSS, and other compliance frameworks.

-   **Change Management**

    Produce before-and-after documentation for change advisory board (CAB) submissions and post-change verification.

-   **Environment Handover**

    Accelerate onboarding and handover with comprehensive, consistent infrastructure documentation generated on demand.

-   **Disaster Recovery**

    Maintain accurate as-built records of your infrastructure to support disaster recovery planning and runbook validation.

</div>

</section>

<section class="abr-section abr-modules abr-bleed" markdown>

## Report Modules

Each module documents one product and is maintained by people who run it. See the [report module overview](user-guide/report-modules/overview.md) for compatibility and documentation.
{ .abr-lede }

<div class="abr-spec" markdown>

-   **Aruba**

    [Aruba.ClearPass](https://github.com/AsBuiltReport/AsBuiltReport.Aruba.ClearPass#readme){ .abr-chip }

-   **Dell EMC**

    [DellEMC.VxRail](https://github.com/AsBuiltReport/AsBuiltReport.DellEMC.VxRail#readme){ .abr-chip }

-   **Fortinet**

    [Fortinet.FortiGate](https://github.com/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate#readme){ .abr-chip }

-   **Microsoft**

    [Microsoft.AD](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.AD#readme){ .abr-chip }
    [Microsoft.Azure](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Azure#readme){ .abr-chip }
    [Microsoft.DHCP](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.DHCP#readme){ .abr-chip }
    [Microsoft.SCVMM](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM#readme){ .abr-chip }
    [Microsoft.Windows](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Windows#readme){ .abr-chip }

-   **NetApp**

    [NetApp.ONTAP](https://github.com/AsBuiltReport/AsBuiltReport.NetApp.ONTAP#readme){ .abr-chip }

-   **Nutanix**

    [Nutanix.PrismElement](https://github.com/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement#readme){ .abr-chip }

-   **Pure Storage**

    [PureStorage.FlashArray](https://github.com/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray#readme){ .abr-chip }

-   **Rubrik**

    [Rubrik.CDM](https://github.com/AsBuiltReport/AsBuiltReport.Rubrik.CDM#readme){ .abr-chip }

-   **Veeam**

    [Veeam.VB365](https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VB365#readme){ .abr-chip }
    [Veeam.VBR](https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VBR#readme){ .abr-chip }

-   **VMware**

    [VMware.AppVolumes](https://github.com/AsBuiltReport/AsBuiltReport.VMware.AppVolumes#readme){ .abr-chip }
    [VMware.ESXi](https://github.com/AsBuiltReport/AsBuiltReport.VMware.ESXi#readme){ .abr-chip }
    [VMware.Horizon](https://github.com/AsBuiltReport/AsBuiltReport.VMware.Horizon#readme){ .abr-chip }
    [VMware.SRM](https://github.com/AsBuiltReport/AsBuiltReport.VMware.SRM#readme){ .abr-chip }
    [VMware.vSphere](https://github.com/AsBuiltReport/AsBuiltReport.VMware.vSphere#readme){ .abr-chip }

</div>

</section>

<section class="abr-section" markdown>

## How the pieces fit

Each report starts on the live system and ends as a finished document. Your settings travel with it as JSON files and a style script, so the same command gives the same report every time.
{ .abr-lede }

<div class="abr-flow" markdown>

<div class="abr-flow__stage" markdown>

### Your platform

The system you want to document, such as a vCenter Server, an Azure tenant or a Veeam backup server.

</div>

<div class="abr-flow__stage" markdown>

### Report module

Collects the configuration through the vendor's PowerShell module or REST API. There is one module for each product.

-   <code>AsBuiltReport.<wbr>Microsoft.<wbr>Azure.json</code><br>
    Information levels, health checks and report options. Create it with [New-AsBuiltReportConfig](user-guide/new-asbuiltreportconfig.md).

</div>

<div class="abr-flow__stage" markdown>

### Core module

Provides the [base commands](user-guide/new-asbuiltreport.md) and builds the document with PScribo.

-   `AsBuiltReport.json`<br>
    Author, company and email settings. Create it with [New-AsBuiltConfig](user-guide/new-asbuiltconfig.md).
-   Style script<br>
    Fonts, colours, cover page and table styles. Use the default or [create your own](dev-guide/creating-a-report-style.md).

</div>

<div class="abr-flow__stage abr-flow__stage--out" markdown>

### Your report

Saved as Word, HTML or text, and sent by email if you choose.

</div>

</div>

</section>

<div class="abr-band abr-bleed" markdown>

<div class="abr-band__copy" markdown>

## Document the kit you run

AsBuiltReport is written by the people who use it. If your platform is missing, the developer guide shows how to build a report module for it.

</div>

<div class="abr-actions" markdown>

[Read the developer guide](dev-guide/contributing.md){ .abr-btn .abr-btn--dark }
[Join the discussion](https://github.com/orgs/AsBuiltReport/discussions){ .abr-btn .abr-btn--outline }

</div>

</div>
