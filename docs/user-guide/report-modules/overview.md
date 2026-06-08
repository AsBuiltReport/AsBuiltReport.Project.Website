---
title: Overview
description: Browse all available AsBuiltReport modules for documenting your infrastructure across multiple vendors and technologies
tags:
  - report-modules
  - modules
  - vendors
  - compatibility
---

# Overview

Report modules are the core of AsBuiltReport - each module provides vendor-specific or technology-specific documentation capabilities. A report module knows how to connect to a system, collect configuration data, and generate comprehensive documentation in multiple formats.

## What are Report Modules?

Each report module is a PowerShell module that extends AsBuiltReport to support a specific technology or platform:

- **Vendor-Specific** - VMware vSphere, Microsoft Active Directory, Veeam Backup & Replication, etc.
- **Self-Contained** - Each module includes all the logic to collect and format data for its technology
- **Independently Updated** - Modules are updated on their own schedule to support new product versions
- **Community-Driven** - Built and maintained by the AsBuiltReport community

## Getting Started with Report Modules

**1. Discover Available Modules**

Use PowerShell to find all available report modules:

```powershell title="Find all AsBuiltReport modules"
# List all available modules
Find-Module -Name AsBuiltReport.* | Select-Object Name, Description

# Search for a specific vendor
Find-Module -Name AsBuiltReport.VMware.* | Select-Object Name, Description
```

**2. Install a Module**

```powershell title="Install a report module"
# Install a report module (AsBuiltReport.Core is automatically installed)
Install-Module -Name AsBuiltReport.VMware.vSphere -Scope CurrentUser
```

**3. Check Module Requirements**

Before generating reports, check each module's GitHub README for:

- **Supported product versions** - Which versions of the target system are supported
- **PowerShell version requirements** - PowerShell 5.1, 7.x compatibility
- **Dependencies** - Required vendor PowerShell modules (e.g., VCF.PowerCLI)
- **Minimum permissions** - What access rights are needed

!!! tip "Module Documentation"
    Click on any report module name in the table below to access its GitHub repository with detailed documentation, examples, and known issues.

## PowerShell Compatibility

Most report modules support:

- **Windows PowerShell 5.1** - Built into Windows 10/11 and Windows Server 2016+
- **PowerShell 7+** - Cross-platform support (Windows, Linux, macOS)

!!! note "Check Module-Specific Requirements"
    Some modules may have specific PowerShell version requirements. Always check the module's README before installation.

## Finding Modules

There are multiple ways to discover and access report modules:

| Method | Description |
|--------|-------------|
| **PowerShell Gallery** | Use `Find-Module -Name AsBuiltReport.*` to search |
| **This Documentation** | Browse by vendor in the left sidebar |
| **GitHub Organization** | View all repositories at [github.com/AsBuiltReport](https://github.com/orgs/AsBuiltReport/repositories) |
| **Activity Table** | See the table below for published modules with version and activity status |

## Quick Start by Vendor

=== "VMware"

    VMware report modules require VCF PowerCLI:

    ```powershell title="Install VMware modules"
    # Install VCF PowerCLI
    Install-Module -Name VCF.PowerCLI -Scope CurrentUser -AllowClobber -SkipPublisherCheck

    # Install VMware vSphere report module
    Install-Module -Name AsBuiltReport.VMware.vSphere -Scope CurrentUser

    # Generate a report
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential (Get-Credential)
    ```

    **Available VMware Modules:**

    - **VMware vSphere** - Document vCenter, clusters, hosts, VMs, networking, storage
    - **VMware ESXi** - Standalone ESXi host documentation
    - **VMware Horizon** - VDI environment documentation
    - **VMware App Volumes** - Application delivery documentation
    - **VMware Site Recovery Manager** - Disaster recovery configuration

=== "Microsoft"

    Microsoft modules may require specific Windows features or modules:

    ```powershell title="Install Microsoft modules"
    # For Active Directory (requires RSAT-AD-PowerShell feature)
    Install-Module -Name AsBuiltReport.Microsoft.AD -Scope CurrentUser

    # For DHCP (requires RSAT-DHCP feature)
    Install-Module -Name AsBuiltReport.Microsoft.DHCP -Scope CurrentUser

    # For Windows Servers
    Install-Module -Name AsBuiltReport.Microsoft.Windows -Scope CurrentUser

    # Generate an Active Directory report
    New-AsBuiltReport -Report Microsoft.AD -Target dc01.example.com -Credential (Get-Credential)
    ```

    **Available Microsoft Modules:**

    - **Active Directory** - Domain controllers, forest, domains, sites, replication
    - **DHCP** - DHCP server configuration and scope documentation
    - **Windows** - Windows Server configuration and roles
    - **Azure** - Azure subscription and resource documentation
    - **SCVMM** - System Center Virtual Machine Manager

=== "Veeam"

    Veeam modules require Veeam PowerShell snapins:

    ```powershell title="Install Veeam modules"
    # Install Veeam Backup & Replication module
    Install-Module -Name AsBuiltReport.Veeam.VBR -Scope CurrentUser

    # Install Veeam Backup for Microsoft 365 module
    Install-Module -Name AsBuiltReport.Veeam.VB365 -Scope CurrentUser

    # Generate a VBR report
    New-AsBuiltReport -Report Veeam.VBR -Target veeam-server.example.com -Credential (Get-Credential)
    ```

    **Available Veeam Modules:**

    - **Veeam VBR** - Backup & Replication infrastructure and jobs
    - **Veeam VB365** - Backup for Microsoft 365 configuration

=== "Storage"

    Storage vendor modules:

    ```powershell title="Install storage modules"
    # NetApp ONTAP
    Install-Module -Name AsBuiltReport.NetApp.ONTAP -Scope CurrentUser

    # Pure Storage FlashArray
    Install-Module -Name AsBuiltReport.PureStorage.FlashArray -Scope CurrentUser

    # Dell EMC VxRail
    Install-Module -Name AsBuiltReport.DellEMC.VxRail -Scope CurrentUser
    ```

    **Available Storage Modules:**

    - **NetApp ONTAP** - Storage system configuration
    - **Pure Storage FlashArray** - FlashArray configuration
    - **Dell EMC VxRail** - Hyperconverged infrastructure

=== "Networking"

    Networking vendor modules:

    ```powershell title="Install networking modules"
    # Fortinet FortiGate
    Install-Module -Name AsBuiltReport.Fortinet.FortiGate -Scope CurrentUser

    # Aruba ClearPass
    Install-Module -Name AsBuiltReport.Aruba.ClearPass -Scope CurrentUser
    ```

    **Available Networking Modules:**

    - **Fortinet FortiGate** - Firewall configuration
    - **Aruba ClearPass** - Network access control

=== "Other"

    Additional infrastructure modules:

    ```powershell title="Install other modules"
    # Nutanix Prism Element
    Install-Module -Name AsBuiltReport.Nutanix.PrismElement -Scope CurrentUser

    # Rubrik CDM
    Install-Module -Name AsBuiltReport.Rubrik.CDM -Scope CurrentUser

    # System Resources
    Install-Module -Name AsBuiltReport.System.Resources -Scope CurrentUser
    ```

    **Available Modules:**

    - **Nutanix Prism Element** - Hyperconverged infrastructure
    - **Rubrik CDM** - Cloud Data Management
    - **System Resources** - General system resource documentation

## Activity Status

The table below provides the status of report modules currently published to the [PowerShell Gallery](https://www.powershellgallery.com/packages?q=AsBuiltReport*){:target="_blank"}.

For a complete list of report modules, including those still in development, please refer to the [AsBuiltReport GitHub Organization](https://github.com/orgs/AsBuiltReport/repositories?q=&type=all&language=&sort=name){:target="_blank"}.

To check the status of a report module, click on the module's last updated or contributors links and reach out to the module's maintainers.

### Aruba

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Aruba ClearPass](https://github.com/AsBuiltReport/AsBuiltReport.Aruba.ClearPass/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Aruba.ClearPass/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Aruba.ClearPass/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Aruba.ClearPass" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Aruba.ClearPass?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Aruba.ClearPass/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Aruba.ClearPass?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Aruba.ClearPass/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Aruba.ClearPass?label=Contributors"> |

### Dell EMC

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Dell EMC VxRail](https://github.com/AsBuiltReport/AsBuiltReport.DellEMC.VxRail/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.DellEMC.VxRail/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.DellEMC.VxRail/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.DellEMC.VxRail" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.DellEMC.VxRail?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.DellEMC.VxRail/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.DellEMC.VxRail?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.DellEMC.VxRail/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.DellEMC.VxRail?label=Contributors"> |

### Fortinet

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Fortinet FortiGate](https://github.com/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Fortinet.FortiGate" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Fortinet.FortiGate?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Fortinet.FortiGate?label=Contributors"> |

### Microsoft

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Microsoft Active Directory](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.AD/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.AD/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Microsoft.AD/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Microsoft.AD" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Microsoft.AD?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.AD/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Microsoft.AD?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.AD/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Microsoft.AD?label=Contributors"> |
| [Microsoft Azure](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Azure/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Azure/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Microsoft.Azure/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Microsoft.Azure" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Microsoft.Azure?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Azure/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Microsoft.Azure?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Azure/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Microsoft.Azure?label=Contributors"> |
| [Microsoft DHCP](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.DHCP/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.DHCP/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Microsoft.DHCP/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Microsoft.DHCP" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Microsoft.DHCP?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.DHCP/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Microsoft.DHCP?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.DHCP/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Microsoft.DHCP?label=Contributors"> |
| [Microsoft SCVMM](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Microsoft.SCVMM" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Microsoft.SCVMM?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Microsoft.SCVMM?label=Contributors"> |
| [Microsoft Windows](https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Windows/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Windows/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Microsoft.Windows/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Microsoft.Windows" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Microsoft.Windows?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Windows/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Microsoft.Windows?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Microsoft.Windows/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Microsoft.Windows?label=Contributors"> |

### NetApp

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [NetApp ONTAP](https://github.com/AsBuiltReport/AsBuiltReport.NetApp.ONTAP/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.NetApp.ONTAP/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.NetApp.ONTAP/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.NetApp.ONTAP" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.NetApp.ONTAP?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.NetApp.ONTAP/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.NetApp.ONTAP?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.NetApp.ONTAP/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.NetApp.ONTAP?label=Contributors"> |

### Nutanix

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Nutanix Prism Element](https://github.com/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Nutanix.PrismElement" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Nutanix.PrismElement?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Nutanix.PrismElement?label=Contributors"> |

### Pure Storage

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Pure Storage FlashArray](https://github.com/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.PureStorage.FlashArray" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.PureStorage.FlashArray?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.PureStorage.FlashArray?label=Contributors"> |

### Rubrik

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Rubrik CDM](https://github.com/AsBuiltReport/AsBuiltReport.Rubrik.CDM/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Rubrik.CDM/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Rubrik.CDM/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Rubrik.CDM" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Rubrik.CDM?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Rubrik.CDM/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Rubrik.CDM?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Rubrik.CDM/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Rubrik.CDM?label=Contributors"> |

### System

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [System Resources](https://github.com/AsBuiltReport/AsBuiltReport.System.Resources/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.System.Resources/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.System.Resources/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.System.Resources" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.System.Resources?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.System.Resources/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.System.Resources?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.System.Resources/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.System.Resources?label=Contributors"> |

### Veeam

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [Veeam VB365](https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VB365/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VB365/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Veeam.VB365/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Veeam.VB365" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Veeam.VB365?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VB365/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Veeam.VB365?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VB365/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Veeam.VB365?label=Contributors"> |
| [Veeam VBR](https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VBR/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VBR/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.Veeam.VBR/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.Veeam.VBR" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.Veeam.VBR?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VBR/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.Veeam.VBR?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.Veeam.VBR/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.Veeam.VBR?label=Contributors"> |

### VMware

| Report | Last Updated |Version | Release Date | Contributors |
| :----- | :----: | :---- | :---- | :---- |
| [VMware App Volumes](https://github.com/AsBuiltReport/AsBuiltReport.VMware.AppVolumes/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.AppVolumes/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.VMware.AppVolumes/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.VMware.AppVolumes" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.VMware.AppVolumes?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.AppVolumes/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.VMware.AppVolumes?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.AppVolumes/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.VMware.AppVolumes?label=Contributors"> |
| [VMware ESXi](https://github.com/AsBuiltReport/AsBuiltReport.VMware.ESXi/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.ESXi/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.VMware.ESXi/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.VMware.ESXi" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.VMware.ESXi?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.ESXi/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.VMware.ESXi?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.ESXi/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.VMware.ESXi?label=Contributors"> |
| [VMware Horizon](https://github.com/AsBuiltReport/AsBuiltReport.VMware.Horizon/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.Horizon/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.VMware.Horizon/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.VMware.Horizon" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.VMware.Horizon?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.Horizon/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.VMware.Horizon?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.Horizon/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.VMware.Horizon?label=Contributors"> |
| [VMware Site Recovery Manager](https://github.com/AsBuiltReport/AsBuiltReport.VMware.SRM/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.SRM/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.VMware.SRM/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.VMware.SRM" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.VMware.SRM?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.SRM/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.VMware.SRM?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.SRM/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.VMware.SRM?label=Contributors"> |
| [VMware vSphere](https://github.com/AsBuiltReport/AsBuiltReport.VMware.vSphere/tree/master){:target="_blank"} | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.vSphere/commits/master" alt="Commits" target="_blank"><img src="https://img.shields.io/github/last-commit/AsBuiltReport/AsBuiltReport.VMware.vSphere/master?label=Last%20Updated" /></a> | <a href="https://www.powershellgallery.com/packages?q=AsBuiltReport.VMware.vSphere" alt="Version" target="_blank"><img src="https://img.shields.io/powershellgallery/v/AsBuiltReport.VMware.vSphere?include_prereleases&label=Version" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.vSphere/releases" alt="GitHub Release Date" target="_blank"><img src="https://img.shields.io/github/release-date/AsBuiltReport/AsBuiltReport.VMware.vSphere?label=Release%20Date" /></a> | <a href="https://github.com/AsBuiltReport/AsBuiltReport.VMware.vSphere/graphs/contributors" alt="GitHub Contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AsBuiltReport/AsBuiltReport.VMware.vSphere?label=Contributors"> |

## Next Steps

- **[Installation Guide](../installation.md)** - Learn how to install report modules
- **[Quickstart Guide](../quickstart.md)** - Generate your first report in 5 minutes
- **[Best Practices](../best-practices.md)** - Recommended approaches for using report modules
- **[Contributing](../../dev-guide/contributing.md)** - Help improve or create new report modules
