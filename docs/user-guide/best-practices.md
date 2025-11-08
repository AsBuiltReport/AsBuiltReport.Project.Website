---
title: Best Practices
description: Essential recommendations for generating and managing AsBuiltReport documentation effectively
tags:
  - best-practices
  - recommendations
  - tips
  - scheduling
  - security
---

# Best Practices

This guide provides essential recommendations for using AsBuiltReport effectively in production environments.

## Module Management

### Keep Modules Updated

Update modules regularly to benefit from bug fixes and new features:

```powershell title="Update AsBuiltReport modules"
Update-Module -Name AsBuiltReport.*
```

!!! tip "Module Updates"
    After updating modules, regenerate your report JSON configuration files to ensure you have the latest structure and options.

### Regenerate Configuration Files After Updates

When you update a report module, regenerate the JSON configuration file to ensure you have the latest structure and options:

```powershell title="Regenerate report configuration file"
New-AsBuiltReportConfig -Report VMware.vSphere -Path C:\Reports -Force
```

## Report Generation

### Start with Default InfoLevels

Begin with the default InfoLevels to understand report structure and generation time. Adjust only for sections requiring more or less detail.

**Benefits:**

- Optimal balance of detail and performance
- Report modules set sensible defaults
- Easier to identify which sections need adjustment

### Enable Health Checks

Always enable health checks for production reports to highlight configuration issues and best practice violations:

```powershell title="Enable health checks"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -EnableHealthCheck
```

### Use Descriptive File Names

Use the `-Filename` parameter to create meaningful report names:

```powershell title="Custom report filenames"
# Weekly summary report
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -Filename "vSphere-Weekly-Summary" `
    -OutputFolderPath C:\Reports\Weekly

# Client-specific report
New-AsBuiltReport -Report VMware.vSphere -Target vcenter-clienta.com `
    -Credential $Cred -Filename "ClientA-vSphere-Production" `
    -OutputFolderPath C:\Reports\Clients

# Combine with -Timestamp for dated reports
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -Filename "vSphere-Audit" -Timestamp `
    -OutputFolderPath C:\Reports\Audit
```

Name configuration files based on purpose and scope:

```text title="Configuration file naming examples"
✔️ AsBuiltReport.VMware.vSphere-Weekly-Summary.json
❌ config1.json
```

## Credential Management

### Use Dedicated Service Accounts

Create dedicated read-only service accounts for report generation:

- Easy audit trail
- Simple to disable if needed
- Consistent permissions
- No dependency on personal accounts

### Never Store Credentials in Scripts

Use secure credential storage methods:

**Option 1: Encrypted Credential File**

```powershell title="Encrypted credential file"
# One-time setup
Get-Credential | Export-Clixml -Path C:\Secure\vcenter-cred.xml

# In your script
$Credential = Import-Clixml -Path C:\Secure\vcenter-cred.xml
```

**Option 2: PowerShell SecretManagement Module (Recommended)**

```powershell title="SecretManagement module"
# One-time setup - Install SecretManagement module
Install-Module -Name Microsoft.PowerShell.SecretManagement -Scope CurrentUser
Install-Module -Name SecretStore -Scope CurrentUser

# Configure the SecretStore (first time only)
Register-SecretVault -Name 'LocalStore' -ModuleName 'Microsoft.PowerShell.SecretStore' -DefaultVault

# Store credentials
$Credential = Get-Credential -Message "Enter vCenter credentials"
Set-Secret -Name 'vCenter-Prod' -Secret $Credential -Vault 'LocalStore'

# In your script - retrieve the credential
$Credential = Get-Secret -Name 'vCenter-Prod' -Vault 'LocalStore' -AsPlainText
```

!!! tip "SecretManagement Benefits"
    The SecretManagement module provides a standardised interface for storing and retrieving secrets. It supports multiple vault extensions including Azure Key Vault, KeePass, and HashiCorp Vault for enterprise environments.

!!! warning "Credential Security"
    Never hardcode passwords in scripts. Always use encrypted credential files or credential management systems.

## Scheduling Reports

### Schedule During Off-Peak Hours

Run reports when systems are less busy:

- **Daily reports**: Early morning (e.g., 02:00 AM)
- **Weekly reports**: Weekend nights
- **Monthly reports**: First weekend of month

### Use Timestamps

Always use the `-Timestamp` parameter for scheduled reports to maintain history:

```powershell title="Generate report with timestamp"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
    -Credential $Cred -Timestamp -OutputFolderPath C:\Reports\Archive
```

## Organisation

### Use Folder Structure

Organise reports and configurations logically:

```text title="Recommended folder structure"
C:\Reports\
├── Production\
├── Development\
├── Archive\
├── Config\
├── Logs\
└── Scripts\
```

### Version Control Configurations

Use Git to track configuration changes:

```powershell title="Initialise Git repository for configurations"
cd C:\Reports\Config
git init
git add *.json
git commit -m "Initial commit of report configurations"
```

## Testing and Validation

### Validate Report Content

Periodically review reports to ensure:

- All expected sections are present
- Data appears current and accurate
- Health checks highlight known issues
- No unexpected errors or warnings

If you find data that is missing, incorrect, or not reported as expected:

1. Check the [Troubleshooting](../support/troubleshooting.md) guide for common issues
2. Review the [Known Issues](../support/known-issues.md) for the specific report module
3. If the issue persists, raise an issue on the report module's GitHub repository with:
    - Description of the expected vs actual behaviour
    - Report module version (`Get-Module -Name AsBuiltReport.* -ListAvailable`)
    - Target system version
    - Relevant verbose output (use `-Verbose` parameter)

## Summary

Following these best practices will help you:

- Generate reliable, consistent reports
- Maintain security and compliance
- Optimise performance and resource usage
- Simplify maintenance and troubleshooting

For more information, see:

- [Quickstart Guide](quickstart.md) - Getting started
- [Installation Guide](installation.md) - Module installation and updates
- [Troubleshooting](../support/troubleshooting.md) - Solving common issues
- [FAQ](../support/faq.md) - Frequently asked questions
