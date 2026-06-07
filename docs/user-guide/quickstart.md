---
title: Quickstart Guide
description: Get your first AsBuiltReport generated in 5 minutes - just 4 simple steps from installation to your first report
tags:
  - quickstart
  - getting-started
  - beginner
  - tutorial
---

# Quickstart Guide

Get your first AsBuiltReport up and running in 5 minutes!

Just 4 simple steps from zero to your first generated report.

## Prerequisites

Before you begin, ensure you have:

- **PowerShell 5.1 or PowerShell 7+** installed
- **Internet connection** for module installation
- **Access to a target system** you want to document (e.g., vCenter, Active Directory, etc.)
- **Credentials** with read-only access to the target system

## Step 1: Install a Report Module (2 minutes)

Open PowerShell and install a report module for your environment. AsBuiltReport.Core will be automatically installed as a dependency.

### Discover Available Report Modules

First, see what report modules are available:

```powershell title="Find available AsBuiltReport modules"
# List all available AsBuiltReport modules in PowerShell Gallery
Find-Module -Name AsBuiltReport.* | Select-Object Name, Description | Format-Table -AutoSize

# Or search for a specific vendor (e.g., VMware)
Find-Module -Name AsBuiltReport.VMware.* | Select-Object Name, Description

# Or search for a specific vendor (e.g., Microsoft)
Find-Module -Name AsBuiltReport.Microsoft.* | Select-Object Name, Description
```

This will display all published report modules you can install.

!!! tip "Browse Online"
    You can also browse all available modules at the [Report Modules Overview](report-modules/overview.md) page or the [PowerShell Gallery](https://www.powershellgallery.com/packages?q=AsBuiltReport).

### Install Your Chosen Report Module

Choose a report module for your environment:

=== "VMware vSphere"
    ```powershell title="Install VMware vSphere report module"
    Install-Module -Name AsBuiltReport.VMware.vSphere -Scope CurrentUser
    ```

=== "Microsoft Active Directory"
    ```powershell title="Install Active Directory report module"
    Install-Module -Name AsBuiltReport.Microsoft.AD -Scope CurrentUser
    ```

=== "Veeam Backup & Replication"
    ```powershell title="Install Veeam VBR report module"
    Install-Module -Name AsBuiltReport.Veeam.VBR -Scope CurrentUser
    ```

=== "Nutanix Prism"
    ```powershell title="Install Nutanix Prism report module"
    Install-Module -Name AsBuiltReport.Nutanix.PrismElement -Scope CurrentUser
    ```

!!! info "AsBuiltReport.Core Dependency"
    The report module installation will automatically install AsBuiltReport.Core if it's not already present. You'll see both modules being installed.

Browse all [available report modules](report-modules/overview.md) for more options.

### Verify Installation

Check that both the Core and report module are installed:

```powershell title="Verify installation"
# List installed AsBuiltReport modules
Get-Module -Name AsBuiltReport.* -ListAvailable
```

You should see both AsBuiltReport.Core and your chosen report module listed.

## Step 2: Check Requirements (1 minute)

Before generating your first report, check the report module's README for:

- **Target system version support** - Ensure your system version is supported
- **PowerShell module dependencies** - Install any required vendor modules
- **Minimum permissions** - Verify your credentials have the necessary access

```powershell title="Check report module information"
# View the report module's project URI (links to GitHub README)
Find-Module -Name AsBuiltReport.VMware.vSphere | Select-Object Name, ProjectUri
```

Visit the GitHub repository to review the README for specific requirements.

!!! example "Common Dependencies"
    - **VMware vSphere** requires `VCF.PowerCLI`
    - **Microsoft AD** requires `ActiveDirectory` module
    - **Veeam VBR** requires `Veeam.Backup.PowerShell` snapin

    Example installation:
    ```powershell
    # Install VMware PowerCLI for vSphere reports
    Install-Module -Name VCF.PowerCLI -Scope CurrentUser -AllowClobber -SkipPublisherCheck
    ```

## Step 3: Generate Your First Report (2 minutes)

Now generate your first report! Replace the example values with your environment details:

=== "VMware vSphere"

    ```powershell title="Generate VMware vSphere report"
    # Store credentials
    $Credential = Get-Credential

    # Generate the report
    New-AsBuiltReport -Report VMware.vSphere `
        -Target vcenter.example.com `
        -Credential $Credential `
        -Format HTML `
        -OutputFolderPath C:\Reports
    ```

=== "Microsoft Active Directory"

    ```powershell title="Generate Active Directory report"
    # Store credentials
    $Credential = Get-Credential

    # Generate the report
    New-AsBuiltReport -Report Microsoft.AD `
        -Target dc01.example.com `
        -Credential $Credential `
        -Format HTML `
        -OutputFolderPath C:\Reports
    ```

=== "Veeam Backup & Replication"

    ```powershell title="Generate Veeam VBR report"
    # Store credentials
    $Credential = Get-Credential

    # Generate the report
    New-AsBuiltReport -Report Veeam.VBR `
        -Target veeam-server.example.com `
        -Credential $Credential `
        -Format HTML `
        -OutputFolderPath C:\Reports
    ```

=== "Nutanix Prism"

    ```powershell title="Generate Nutanix Prism report"
    # Store credentials
    $Credential = Get-Credential

    # Generate the report
    New-AsBuiltReport -Report Nutanix.PrismElement `
        -Target prism.example.com `
        -Credential $Credential `
        -Format HTML `
        -OutputFolderPath C:\Reports
    ```

!!! note "First Run Experience"
    On your first run, you'll be prompted to create configuration files:

    - **AsBuiltReport configuration**: Author name, company info, email settings (optional)
    - **Report configuration**: Automatically created with default settings

    You can press Enter to accept defaults or customise as needed.

!!! info "How Long Will This Take?"
    Report generation time depends on your environment size and InfoLevel settings:

    | Environment Size | InfoLevel | Typical Duration |
    |-----------------|-----------|-----------------|
    | Small (single host / small domain) | 1–2 | Under 1 minute |
    | Medium (10–50 hosts / typical domain) | 2–3 | 2–10 minutes |
    | Large (50+ hosts / complex environment) | 3–5 | 10–60+ minutes |

    During generation, no output is shown by default. If you want to see live progress, add `-Verbose` to your command. If the report appears to hang, it is usually still running — particularly at higher InfoLevels against large environments.

## Step 4: View Your Report

Once generation completes:

1. Navigate to `C:\Reports` (or your chosen output folder)
2. Open the HTML file in your web browser
3. Review your first as-built report!

## What's Next?

Congratulations! You've generated your first AsBuiltReport. Here's what to explore next:

### Customise Report Detail

Adjust the level of detail in your reports using InfoLevel settings:

```powershell title="Create a report configuration file"
# Generate a configuration file
New-AsBuiltReportConfig -Report VMware.vSphere -FolderPath C:\Reports

# Edit the JSON file to adjust InfoLevel values (0-3)
# Then use it when generating reports
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -ReportConfigFilePath C:\Reports\AsBuiltReport.VMware.vSphere.json
```

See [New-AsBuiltReportConfig](new-asbuiltreportconfig.md) for details on customising reports.

### Enable Health Checks

Highlight configuration issues with health checks:

```powershell title="Generate report with health checks"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -EnableHealthCheck -OutputFolderPath C:\Reports
```

### Generate Multiple Formats

Create reports in Word and HTML simultaneously:

```powershell title="Generate multiple formats"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -Format HTML,Word -OutputFolderPath C:\Reports
```

### Customise Branding

Apply your corporate branding with custom styles:

1. See [Creating a Report Style](../dev-guide/creating-a-report-style.md)
2. Use the `-StyleFilePath` parameter to apply your style

### Automate Reports

Schedule reports to run automatically:

- **Windows**: Use Task Scheduler
- **Linux/macOS**: Use cron

See [FAQ - How do I schedule reports?](../support/faq.md#how-do-i-schedule-reports-to-run-automatically)

## Common Beginner Pitfalls

Avoid these common mistakes:

### Forgetting to Install Dependencies

**Problem**: Report module requires vendor PowerShell modules (e.g., VMware PowerCLI)

**Solution**: Check the report module's README for dependencies and install them:

```powershell title="Install required dependencies"
# Example: VMware vSphere requires PowerCLI
Install-Module -Name VCF.PowerCLI -Scope CurrentUser -AllowClobber -SkipPublisherCheck
```

### Using Insufficient Permissions

**Problem**: "Access Denied" or missing report sections

**Solution**: Ensure your credentials have read access to all components you want to document.

### Not Using `-Verbose` When Troubleshooting

**Problem**: Report fails with generic error

**Solution**: Always use `-Verbose` to see detailed progress:

```powershell title="Use verbose output for troubleshooting"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -Verbose
```

### Expecting Instant Results for Large Environments

**Problem**: Report seems to hang with no output

**Solution**: Reports generate silently by default. Use `-Verbose` to see live progress. For your first run against a large environment, lower the InfoLevel to get faster results:

```powershell title="Generate report with verbose output"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -Format HTML -OutputFolderPath C:\Reports -Verbose
```

```powershell title="Create configuration with lower InfoLevels for faster results"
New-AsBuiltReportConfig -Report VMware.vSphere -FolderPath C:\Reports
# Edit the JSON file to set InfoLevel values to 1 or 2, then use it:
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -ReportConfigFilePath C:\Reports\AsBuiltReport.VMware.vSphere.json `
    -Format HTML -OutputFolderPath C:\Reports -Verbose
```

## Getting Help

If you run into issues:

1. **Check verbose output** - Run with `-Verbose` to see detailed progress
2. **Review documentation** - [Installation Guide](installation.md), [FAQ](../support/faq.md), [Troubleshooting](../support/troubleshooting.md)
3. **Search GitHub Issues** - Check if others have encountered similar issues
4. **Ask the community** - [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions)

## Next Steps

Now that you've generated your first report, explore these guides:

- **[Best Practices](best-practices.md)** - Learn recommended approaches for report generation
- **[New-AsBuiltReport](new-asbuiltreport.md)** - Detailed command reference
- **[New-AsBuiltReportConfig](new-asbuiltreportconfig.md)** - Customise report detail levels
- **[Report Modules](report-modules/overview.md)** - Explore all available reports
- **[FAQ](../support/faq.md)** - Common questions answered