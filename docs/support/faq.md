# Frequently Asked Questions

This page answers common questions about AsBuiltReport. Can't find what you're looking for? Check our [Troubleshooting](troubleshooting.md) guide or visit the [Discussion Board](https://github.com/orgs/AsBuiltReport/discussions).

## Getting Started

### What is AsBuiltReport?

AsBuiltReport is an open source configuration document framework which utilises Microsoft PowerShell to produce as-built documentation in multiple document formats for multiple vendors and technologies.

The framework allows users to easily generate clear and consistent documentation, for any environment which supports Microsoft PowerShell and/or a RESTful API.

### What versions of PowerShell are supported?

AsBuiltReport will generally support both Windows PowerShell 5.1 and PowerShell 7, however each individual report will have its own system requirements.

Please refer to the [report module user guides](../user-guide/report-modules/overview.md) for PowerShell compatibility and system requirements.

### How do I install AsBuiltReport?

The easiest way to install AsBuiltReport is from the PowerShell Gallery:

```powershell
# Install the Core module
Install-Module -Name AsBuiltReport.Core -Scope CurrentUser

# Install a report module (e.g., VMware vSphere)
Install-Module -Name AsBuiltReport.VMware.vSphere -Scope CurrentUser
```

For detailed installation instructions, including offline installation and alternative methods, see the [Installation Guide](../user-guide/installation.md).

### How do I install AsBuiltReport if I do not have access to PowerShell Gallery?

Please refer to the [Offline Installation](../user-guide/installation.md#offline-installation) section or [GitHub Installation](../user-guide/installation.md#github-installation) options for instructions on how to install AsBuiltReport without access to PowerShell Gallery.

### How do I generate my first report?

After installing the Core module and a report module, follow these steps:

1. Create a report configuration file:
    ```powershell
    New-AsBuiltReportConfig -Report VMware.vSphere -Path C:\Reports
    ```

2. Generate the report:
    ```powershell
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Username admin -Password (ConvertTo-SecureString 'P@ssw0rd' -AsPlainText -Force) -Format HTML -OutputFolderPath C:\Reports
    ```

For detailed instructions, see the [New-AsBuiltReport](../user-guide/new-asbuiltreport.md) command reference.

### Do I need to install AsBuiltReport on the target system?

No. AsBuiltReport runs on your workstation or management server and connects remotely to the target systems to gather information. You do not need to install anything on the systems you're documenting.

### Will AsBuiltReport modify my infrastructure?

No. AsBuiltReport only performs read operations. It does not make any changes to your infrastructure. The reports are generated using read-only queries and API calls.

## Report Generation

### What document formats are supported?

AsBuiltReport supports three output formats:

- **DOCX** (Microsoft Word) - Best for formal documentation, editing, and distribution
- **HTML** - Best for web viewing, sharing via email, or integration with wikis
- **Text** - Best for quick reviews or environments without document viewers

You can generate multiple formats simultaneously:

```powershell
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential $Cred -Format HTML,DOCX
```

### Do I need Microsoft Word installed to generate a report in DOCX format?

No. Microsoft Word is not required to generate the report, however a document viewer which supports the DOCX format would be required to view the report.

The DOCX files are created using the PScribo framework, which generates native Word documents without requiring Microsoft Office.

### How do I customise the level of detail in my reports?

Reports use InfoLevel settings to control the depth of information collected. You can customise these in the report JSON configuration file:

1. Create a configuration file:
    ```powershell
    New-AsBuiltReportConfig -Report VMware.vSphere -Path C:\Reports
    ```

2. Edit the JSON file and adjust InfoLevel values (typically 0-3):
    ```json
    {
      "InfoLevel": {
        "vCenter": 2,
        "Cluster": 3,
        "VMHost": 2,
        "VM": 1
      }
    }
    ```

Higher InfoLevels provide more detail but take longer to generate. Start with lower values and increase as needed.

### Can I generate reports for multiple targets at once?

Yes, you can specify multiple targets:

```powershell
New-AsBuiltReport -Report VMware.vSphere -Target vcenter01.example.com,vcenter02.example.com -Credential $Cred
```

Some report modules also support generating a combined report for multiple systems. Check the specific [report module documentation](../user-guide/report-modules/overview.md) for details.

### How do I schedule reports to run automatically?

You can schedule AsBuiltReport using Windows Task Scheduler, cron (Linux/macOS), or other scheduling tools:

**Windows Task Scheduler Example:**

1. Create a PowerShell script (e.g., `C:\Scripts\Generate-Report.ps1`):
    ```powershell
    $Credential = Import-Clixml -Path C:\Secure\credential.xml
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential $Credential -Format HTML -OutputFolderPath C:\Reports
    ```

2. Save credentials securely (run once):
    ```powershell
    Get-Credential | Export-Clixml -Path C:\Secure\credential.xml
    ```

3. Create a scheduled task to run the script at your desired interval

!!! warning "Credential Security"
    Credentials exported with `Export-Clixml` can only be decrypted by the same user account on the same computer. Ensure the scheduled task runs under the same account that exported the credentials.

### How do I customise report styling and branding?

AsBuiltReport supports custom styles for personalising report appearance (colours, fonts, logos, etc.).

See the [Creating a Report Style](../dev-guide/creating-a-report-style.md) guide for detailed instructions on customising report branding.

### What credentials and permissions do I need?

Generally, AsBuiltReport requires **read-only** access to the target systems. Specific requirements vary by report module:

- Most modules work with standard read-only user accounts
- Some features may require elevated privileges (e.g., viewing certain security settings)
- API-based reports typically require API tokens or service accounts

Check the specific [report module documentation](../user-guide/report-modules/overview.md) for detailed permission requirements.

## Technical Questions

### What is PScribo?

[PScribo](https://github.com/iainbrighton/PScribo){:target="_blank"} (pronounced 'skree-bo') is an open-source project created by [Iain Brighton](../about/contributors.md#iain-brighton).

PScribo provides a set of functions that make it easy to create a document-like structure within PowerShell, without having to handle multiple output formats. A document's layout and contents only need to be defined once regardless of target output format(s).

### Which vendors and technologies are supported?

AsBuiltReport supports a wide range of vendors and technologies, including:

- **VMware** (vSphere, ESXi, Horizon, NSX, SRM, App Volumes)
- **Microsoft** (Active Directory, Azure, DHCP, SCVMM, Windows Server)
- **Veeam** (Backup & Replication, Backup for Microsoft 365)
- **NetApp** (ONTAP)
- **Pure Storage** (FlashArray)
- **Nutanix** (Prism Element)
- **Dell EMC** (VxRail)
- **Rubrik** (CDM)
- **Fortinet** (FortiGate)
- **Aruba** (ClearPass)

For a complete list, see the [Report Modules](../user-guide/report-modules/overview.md) page.

### Can AsBuiltReport run on Linux or macOS?

Yes, AsBuiltReport runs on Windows, Linux, and macOS using PowerShell 7.

!!! info "Known Limitation"
    Due to .NET 6 changes, images are not supported in reports generated on Linux or macOS. See [Known Issues](known-issues.md) for details.

### Why is my report failing or producing errors?

If you're experiencing issues generating reports:

1. Enable verbose output to see detailed progress:
    ```powershell
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential $Cred -Verbose
    ```

2. Check the [Troubleshooting](troubleshooting.md) guide for common issues and solutions

3. Review [Known Issues](known-issues.md) for documented platform limitations

4. Search or post on the [Discussion Board](https://github.com/orgs/AsBuiltReport/discussions)

### Why are sections missing from my report?

Missing sections can occur for several reasons:

- **Insufficient permissions** - Verify your account has read access to the missing components
- **Component not configured** - The feature/component may not be deployed in your environment
- **InfoLevel set to 0** - Check your JSON configuration file and increase InfoLevel for the missing section
- **Module version** - Ensure you're using the latest version: `Update-Module -Name AsBuiltReport.*`

See the [Troubleshooting - Missing or Incomplete Data](troubleshooting.md#missing-or-incomplete-data) section for more details.

### How do I update AsBuiltReport modules?

To update all AsBuiltReport modules to the latest versions:

```powershell
Update-Module -Name AsBuiltReport.*
```

To update a specific module:

```powershell
Update-Module -Name AsBuiltReport.VMware.vSphere
```

For detailed update instructions, see the [Updating Modules](../user-guide/installation.md#updating-modules) section.

## Community & Support

### How can I contribute to the project?

We welcome contributions! You can contribute by:

- Reporting bugs or suggesting features
- Improving documentation
- Creating or enhancing report modules
- Fixing bugs or adding features

Please refer to the [Contributing Guide](../dev-guide/contributing.md) for detailed information on how to contribute to this project.

### Where can I get help or ask questions?

There are several ways to get help:

- **Troubleshooting Guide** - [Troubleshooting](troubleshooting.md) page for common issues
- **Discussion Board** - [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions) for questions and community support
- **Known Issues** - [Known Issues](known-issues.md) page for documented limitations
- **Contact** - [Contact page](../about/contact.md) for direct enquiries

### How can I donate to the project?

If you find AsBuiltReport useful and would like to support its development, please refer to the [Donate](donate.md) page for information on how to offer your support for this project.

### Is there a community or user group?

Yes! Join the conversation:

- **GitHub Discussions** - [https://github.com/orgs/AsBuiltReport/discussions](https://github.com/orgs/AsBuiltReport/discussions)
- **Social Media** - Follow us on [X/Twitter](https://x.com/AsBuiltReport) and [Bluesky](https://bsky.app/profile/asbuiltreport.com)

### Can I request a new report module or feature?

Absolutely! You can:

1. Check if it's already been requested in [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions)
2. Start a new discussion describing your use case and requirements
3. Consider [contributing](../dev-guide/contributing.md) by developing the module yourself (we're happy to help!)

Feature requests are always welcome, though implementation timelines depend on community contributions and maintainer availability.
