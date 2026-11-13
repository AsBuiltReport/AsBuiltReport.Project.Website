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
  -Target $TenantId -UseInteractiveAuth -Format Word
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

<section class="abr-section abr-split" markdown>

## Components

<div class="abr-spec" markdown>

-   :octicons-package-16:{ .abr-icon } **Core Module**

    The core module provides the framework for each individual report module. It provides the [base commands](user-guide/new-asbuiltreport.md) and default style script used to generate each individual report.

-   :octicons-plug-16:{ .abr-icon } **Reports Module**

    The report module is specific to each vendor and/or technology and is used to extract information from the specific environment. It is written to utilise PowerShell modules or RESTful APIs which the vendor/technology provides.

-   :material-code-json:{ .abr-icon } **Core Module Configuration**

    A JSON file which stores information relating to the author's name, company information and SMTP mail server configuration. Individual core module configuration files can be saved and specified when generating reports.

-   :material-code-json:{ .abr-icon } **Reports Module Configuration**

    A JSON file which stores information specific to the related report, such as the report name, version, and release status. It also provides configurable report options, health checks and granular information levels. Individual report module configuration files can be saved and specified when generating reports.

-   :material-powershell:{ .abr-icon } **Styles Script**

    The styles script sets the default layout, fonts, colours and sizes used within the report, and can lay out cover pages, table of contents and other unique tables or sections. Custom style scripts can be [created](dev-guide/creating-a-report-style.md) to format reports to match your corporate identity.

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

<div class="abr-titleblock">
  <div class="abr-titleblock__brand">
    <img src="assets/images/logos/asbuiltreport-mark.svg#only-light" alt="">
    <img src="assets/images/logos/asbuiltreport-mark-reversed.svg#only-dark" alt="">
    AsBuiltReport
  </div>
  <div><dl><dt>Licence</dt><dd>MIT</dd></dl></div>
  <div><dl><dt>Built with</dt><dd>PowerShell and PScribo</dd></dl></div>
  <div><dl><dt>Maintained by</dt><dd>Tim Carman, Jonathan Colon</dd></dl></div>
  <div><dl><dt>Downloads</dt><dd>250,000+ on the PowerShell Gallery</dd></dl></div>
  <div><dl><dt>Formats</dt><dd>Word, HTML, Text</dd></dl></div>
  <div><dl><dt>Site</dt><dd>Made with ProperDocs</dd></dl></div>
</div>
