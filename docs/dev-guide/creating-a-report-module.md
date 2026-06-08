---
title: Creating a Report Module
description: Comprehensive standards and guidelines for developing AsBuiltReport report modules
tags:
  - development
  - report-modules
  - guidelines
  - standards
  - powershell
  - best-practices
---

# Creating a Report Module

This guide provides comprehensive standards and guidelines for developing AsBuiltReport report modules. Following these practices ensures consistency, maintainability, and quality across the AsBuiltReport ecosystem.

## Getting Started

Before beginning development of a new report module, you should first discuss your plans with the project contributors. This ensures there's no duplication of effort, allows for guidance on implementation approach, and helps coordinate with the broader project roadmap. You can initiate this discussion by creating an issue in the [AsBuiltReport Discussions board](https://github.com/orgs/AsBuiltReport/discussions) or by contacting the [maintainers](../about/contributors.md) directly. A good proposal includes:

- The technology or product you want to document and the vendor name
- The PowerShell module or API you plan to use for data collection
- The PowerShell editions and platforms you intend to support (Windows PowerShell 5.1, PowerShell 7+, or both)
- A rough outline of the report sections you have in mind

Once your module proposal is approved, a new GitHub repository will be created under the AsBuiltReport organisation following the standard naming convention. Review the naming standards and repository structure below, then use the AsBuiltReport Plaster template to scaffold the module locally before beginning development.

The naming convention is not just cosmetic — it is how AsBuiltReport.Core locates your module at runtime. When you run `New-AsBuiltReport -Report 'Vendor.Technology'`, the framework constructs the module name `AsBuiltReport.Vendor.Technology` and the function name `Invoke-AsBuiltReport.Vendor.Technology` from that string, imports the module, and calls the function directly. No registration step is required beyond following the naming convention.

!!! failure "Do Not Publish AsBuiltReport Modules to the PowerShell Gallery Using Your Personal Account"
    Never publish an `AsBuiltReport.*` module to the PowerShell Gallery under your own account. Once a package name is registered on the PowerShell Gallery, it is permanently claimed — no other account can ever use that name. Publishing under a personal account would prevent the AsBuiltReport project from officially releasing that module, and is a violation of the project guidelines.

    All AsBuiltReport modules are published to the PowerShell Gallery exclusively by the [project maintainer](https://www.powershellgallery.com/profiles/tpcarman).

## Module Naming and Structure

### Naming Convention
All AsBuiltReport modules must follow the standardised naming pattern:

```text title="Module naming pattern"
AsBuiltReport.Vendor.Technology
```

**Examples:**
- `AsBuiltReport.VMware.vSphere`
- `AsBuiltReport.Microsoft.AD`
- `AsBuiltReport.Veeam.VBR`
- `AsBuiltReport.NetApp.ONTAP`

### Repository Structure
Organise your module repository with the following standard structure:

```text title="Repository folder structure"
AsBuiltReport.Vendor.Technology/                                # Repository root
├── .github/                                                    # GitHub workflows and templates
├── .vscode/                                                    # VS Code configuration
├── AsBuiltReport.Vendor.Technology/                            # PowerShell module directory
│   ├── AsBuiltReport.Vendor.Technology.json                    # Report configuration file
│   ├── AsBuiltReport.Vendor.Technology.psd1                    # PowerShell manifest
│   ├── AsBuiltReport.Vendor.Technology.psm1                    # PowerShell module script
│   ├── Language/                                               # Language support folders
│   │   ├── en-US/
│   │   │   └── VendorTechnology.psd1                           # en-US language translation file
│   │   └── <language>-<REGION>/                                # Additional language support folders
│   │       └── VendorTechnology.psd1
│   └── Src/
│       ├── Private/                                            # Private functions
│       │   └── Get-Abr[VendorAbbr|Technology][Resource].ps1       # One file per resource type
│       └── Public/                                             # Exported functions
│           └── Invoke-AsBuiltReport.Vendor.Technology.ps1
├── Samples/                                                    # Sample report outputs in Word, HTML, and Text formats generated against a real target environment
├── Tests/                                                      # Pester test suite
│   ├── AsBuiltReport.Vendor.Technology.Tests.ps1               # Module manifest and structure tests
│   ├── LocalizationData.Tests.ps1                              # Localization key validation tests
│   └── Invoke-Tests.ps1                                        # Test runner
├── README.md                                                   # Module documentation
├── CHANGELOG.md                                                # Version history
├── CODE_OF_CONDUCT.md                                          # Code of Conduct policy
├── CONTRIBUTING.md                                             # Contributing guidelines
├── SECURITY.md                                                 # Security policy
└── LICENSE                                                     # MIT License
```

### GitHub Actions Workflows

The `.github/workflows/` folder scaffolded by Plaster contains four pre-configured workflows:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `PSScriptAnalyzer.yml` | Push, pull request | Lints all PowerShell code; fails the build on errors |
| `Pester.yml` | Push/PR to `dev`, `master`, `main` | Runs the Pester test suite across Windows, Linux, and macOS on both Windows PowerShell 5.1 and PowerShell 7+ |
| `Release.yml` | GitHub release published | Publishes the module to the PowerShell Gallery and posts release announcements |
| `Stale.yml` | Daily schedule | Marks issues and PRs stale after 90 days of inactivity and closes them after a further 7 days |

The PSScriptAnalyzer and Stale workflows require no configuration and work immediately. The Pester workflow requires no configuration but will upload code coverage results to Codecov if a `CODECOV_TOKEN` secret is set. The Release workflow is managed by the project maintainers and requires PowerShell Gallery and social media secrets to be configured in the repository settings — you do not need to set these up yourself.

## Scaffolding Your Module with Plaster

The AsBuiltReport project provides a [Plaster](https://github.com/PowerShellOrg/Plaster) template that generates the complete, standardised module structure automatically, including the directory layout, manifest, module script, CI/CD workflows, Pester tests, and documentation templates.

### Prerequisites

- PowerShell 5.1 or 7+
- [Plaster](https://www.powershellgallery.com/packages/Plaster) module
- [AsBuiltReport.Core](https://www.powershellgallery.com/packages/AsBuiltReport.Core) module (required to test report generation locally)
- Git (required to initialise the repository and push to GitHub)
- The vendor PowerShell module for the technology you are documenting (e.g. VCF.PowerCLI, Az)
- A test environment running the target technology to collect data against

```powershell title="Install Plaster"
Install-Module -Name Plaster -Scope CurrentUser
```

#### 1. Clone the template

```powershell title="Clone the AsBuiltReport Plaster template"
git clone https://github.com/AsBuiltReport/AsBuiltReport.Plaster.Template C:\AsBuiltReport.Plaster.Template
```

#### 2. Scaffold a new module

Run `Invoke-Plaster`, specifying the cloned template path and your destination directory:

```powershell title="Scaffold a new module"
Invoke-Plaster -TemplatePath 'C:\AsBuiltReport.Plaster.Template' -DestinationPath 'C:\Development'
```

Plaster will prompt for the following:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `VendorName` | Vendor or technology name (e.g. `VMware`) | — |
| `ProductName` | Product name (e.g. `vSphere`) | — |
| `ModuleName` | Full module name | `AsBuiltReport.<VendorName>.<ProductName>` |
| `Description` | Brief module description | Auto-generated |
| `Version` | Initial module version | `0.1.0` |
| `Author` | Module author name | Git config value |
| `CompanyName` | Company or organisation name | `Unknown` |
| `PowerShellVersion` | Supported PowerShell edition(s) | `PowerShell 7+ only` |

**PowerShell edition options:**

| Choice | `PowerShellVersion` | `CompatiblePSEditions` |
|--------|---------------------|------------------------|
| Windows PowerShell 5.1 only | `5.1` | `@('Desktop')` |
| PowerShell 7+ only | `7.0` | `@('Core')` |
| Windows PowerShell 5.1 and PowerShell 7+ | `5.1` | `@('Desktop', 'Core')` |

#### 3. Next steps

After `Invoke-Plaster` completes, the module directory is ready for development. The key files to work on are:

1. **Rename and populate** `Src\Private\Get-AbrVendorTechnologyExample.ps1` — add your data collection functions following the [private functions](#private-functions) standards
2. **Update** `Src\Public\Invoke-AsBuiltReport.Vendor.Technology.ps1` — wire up your private functions inside the `foreach ($System in $Target)` loop
3. **Expand** `AsBuiltReport.Vendor.Technology.json` — add your sections under `InfoLevel` and `HealthCheck`
4. **Update** `Language\en-US\VendorTechnology.psd1` — add your translation strings following the [language support](#language-support-implementation) standards
5. **Initialise git** — run `git init` and commit your scaffolded files locally. You can develop and commit locally before the organisation repository is provisioned. Once the maintainers provide the remote URL, add it and push: `git remote add origin <url> && git push -u origin dev`

#### 4. Testing your module locally

Before pushing to the organisation repository, you can import and test your module entirely from a local path. This inner development loop does not require the GitHub repository to be set up yet.

**1. Install AsBuiltReport.Core**

```powershell title="Install AsBuiltReport.Core"
Install-Module -Name AsBuiltReport.Core -Scope CurrentUser
```

**2. Import your local module**

```powershell title="Import the local module"
Import-Module 'C:\Development\AsBuiltReport.Vendor.Technology\AsBuiltReport.Vendor.Technology.psd1' -Force
```

**3. Generate a report configuration file**

Use `New-AsBuiltReportConfig` to generate a copy of your module's JSON configuration file at a writable path. This is the file you edit to set InfoLevel and HealthCheck values for each test run.

```powershell title="Generate a report configuration file"
New-AsBuiltReportConfig -Report 'Vendor.Technology' -FolderPath 'C:\Reports' -Filename 'VendorTechnology.json'
```

**4. Run a test report**

```powershell title="Run a test report"
New-AsBuiltReport -Report 'Vendor.Technology' -Target '192.168.1.100' -Credential (Get-Credential) -Format HTML -OutputFolderPath 'C:\Reports' -ReportConfigFilePath 'C:\Reports\VendorTechnology.json'
```

Add `-Verbose` to see `Write-PScriboMessage` output during report generation, which helps confirm your data collection functions are running and catching errors correctly.

## PowerShell Manifest (.psd1) Requirements

### Essential Properties
Your module manifest must include these standardised properties:

```powershell title="Module manifest (.psd1) template"
@{
    ModuleVersion = '0.1.0'                        # Semantic versioning
    Author = 'Your Name'
    Description = 'A PowerShell module to generate an as built report on the configuration of [Technology]'
    PowerShellVersion = '5.1'
    CompatiblePSEditions = @('Desktop', 'Core')    # Where applicable

    RequiredModules = @(
        @{
            ModuleName = 'AsBuiltReport.Core'
            ModuleVersion = '1.6.1'               # Minimum required version
        }
        # Add vendor-specific modules as needed
    )

    FunctionsToExport = 'Invoke-AsBuiltReport.Vendor.Technology'

    PrivateData = @{
        PSData = @{
            Tags = @('AsBuiltReport', 'Report', 'Documentation', 'PScribo', 'Windows', 'Linux', 'MacOS', 'PSEdition_Desktop', 'PSEdition_Core', '[Vendor]', '[Technology]')     # Include tags which are applicable
            LicenseUri = 'https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology/blob/master/LICENSE'
            ProjectUri = 'https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology'
            IconUri = 'AsBuiltReport.png'
            ReleaseNotes = 'https://raw.githubusercontent.com/AsBuiltReport/AsBuiltReport.Vendor.Technology/master/CHANGELOG.md'
        }
    }
}
```

## Module Script (.psm1) Pattern

The `.psm1` file should dynamically discover and load all function files from `Src/Public` and `Src/Private` using dot-sourcing. This avoids maintaining a manual import list as the module grows.

```powershell title="Module script (.psm1) template"
# Dot-source all Public and Private function files
foreach ($Folder in @('Public', 'Private')) {
    $FolderPath = Join-Path -Path $PSScriptRoot -ChildPath "Src\$Folder"
    if (Test-Path -Path $FolderPath) {
        Get-ChildItem -Path $FolderPath -Filter '*.ps1' -Recurse | ForEach-Object {
            try {
                . $_.FullName
            } catch {
                Write-Warning "Failed to import function $($_.FullName): $_"
            }
        }
    }
}
```

**Key points:**

- Uses `$PSScriptRoot` for portable path resolution — do not use relative paths
- Errors on individual files are non-fatal (warns and continues loading)
- No explicit `Export-ModuleMember` call is needed; the `FunctionsToExport` field in the `.psd1` manifest controls what is exported to callers

## Configuration File Standards

### JSON Configuration Structure
Create a configuration file using the JSON template provided in the report module repository. The `Report` section uses standard properties. Avoid modifying the property fields, only values should be customised. The `Options`, `InfoLevel`, and `HealthCheck` sections should be tailored to your specific module requirements. Additional schemas may be added if necessary.

```json title="Report configuration JSON template"
{
"Report": {                                         // Avoid modifying the Report parameters, use Options if needed
    "Name": "<Vendor> <Technology> As Built Report",
    "Version": "1.0",
    "Status": "Released",
    "Language": "en-US",
    "ShowCoverPageImage": true,
    "ShowTableOfContents": true,
    "ShowHeaderFooter": true,
    "ShowTableCaptions": true
  },
  "Options": {                                     // Used for configurable report options
  },
  "InfoLevel": {
    "_comment_": "0 = Disabled, 1 = Enabled / Summary, 2 = Adv Summary, 3 = Detailed, 4 = Adv Detailed, 5 = Comprehensive"
  },
  "HealthCheck": {
  }
}
```

### Language Configuration

!!! info
    AsBuiltReport.Core v1.5.0+ provides the translation functionality for both core UI prompts and report module content.

    Individual report modules provide their own translation files for report-specific content such as headings, text, and tables.

    Please refer to individual [report module documentation](https://www.asbuiltreport.com/user-guide/report-modules/overview/) for their language support.

The `Language` property in the `Report` section specifies the default language for report content. This setting can be overridden at runtime using the [New-AsBuiltReport](../user-guide/new-asbuiltreport.md) `-ReportLanguage` parameter when generating reports.

**Language Support Requirements:**

- **Minimum requirement:** All report modules must provide `en-US` (English - United States) language support
- **Optional:** Additional languages can be provided based on contributor availability and community needs

#### Languages supported by AsBuiltReport.Core

| Locale Code | Language | Locale Code | Language |
|-------------|----------|-------------|----------|
| **en-US (default)** | English (United States) | **hu-HU** | Hungarian (Hungary) |
| **en-GB** | English (United Kingdom) | **it-IT** | Italian (Italy) |
| **ar-SA** | Arabic (Saudi Arabia) | **ja-JP** | Japanese (Japan) |
| **cs-CZ** | Czech (Czech Republic) | **ko-KR** | Korean (South Korea) |
| **da-DK** | Danish (Denmark) | **nb-NO** | Norwegian Bokmål (Norway) |
| **de-DE** | German (Germany) | **nl-NL** | Dutch (Netherlands) |
| **el-GR** | Greek (Greece) | **pl-PL** | Polish (Poland) |
| **es-ES** | Spanish (Spain) | **pt-PT** | Portuguese (Portugal) |
| **fi-FI** | Finnish (Finland) | **ru-RU** | Russian (Russia) |
| **fr-FR** | French (France) | **sv-SE** | Swedish (Sweden) |
| **he-IL** | Hebrew (Israel) | **th-TH** | Thai (Thailand) |
| **hi-IN** | Hindi (India) | **tr-TR** | Turkish (Turkey) |
| **vi-VN** | Vietnamese (Vietnam) | **zh-CN** | Chinese (China, Simplified) |
| **zh-Hans** | Chinese (Simplified) | **zh-Hant** | Chinese (Traditional) |

For comprehensive language mapping and fallback chains, see the [Language Support Implementation](#language-support-implementation) section below.

The following example shows a populated configuration for a module with three report sections and health checks enabled for two of them:

```json title="Report configuration JSON example (populated)"
{
  "Report": {
    "Name": "Vendor Technology As Built Report",
    "Version": "1.0",
    "Status": "Released",
    "Language": "en-US",
    "ShowCoverPageImage": true,
    "ShowTableOfContents": true,
    "ShowHeaderFooter": true,
    "ShowTableCaptions": true
  },
  "Options": {},
  "InfoLevel": {
    "_comment_": "0 = Disabled, 1 = Enabled / Summary, 2 = Adv Summary, 3 = Detailed, 4 = Adv Detailed, 5 = Comprehensive",
    "Infrastructure": 1,
    "Storage": 2,
    "Network": 3
  },
  "HealthCheck": {
    "Infrastructure": {
      "CPUUtilisation": true,
      "MemoryUtilisation": true
    },
    "Storage": {
      "StorageUtilisation": true
    }
  }
}
```

The keys under `InfoLevel` and `HealthCheck` are defined by you and must match the keys your module reads from `$ReportConfig.InfoLevel` and `$ReportConfig.HealthCheck` in code.

### InfoLevel Standards
Implement consistent information levels across all sections. Use the appropriate number of InfoLevel values based on the granular detail levels your report module requires:

| Setting | InfoLevel         | Description|
| :---: | --- | --- |
| **0** | Disabled | Does not collect or display any information |
| **1** | Enabled / Summary | Provides summarised information for a collection of objects |
| **2** | Adv Summary | Provides condensed, detailed information for a collection of objects |
| **3** | Detailed | Provides detailed information for individual objects |
| **4** | Adv Detailed | Provides detailed information for individual objects, as well as information for associated objects |
| **5** | Comprehensive | Provides comprehensive information for individual objects, such as advanced configuration settings |

## PScribo Framework Integration

AsBuiltReport modules are built on the [PScribo](https://github.com/iainbrighton/PScribo) framework, which provides the underlying document generation capabilities. Understanding PScribo is essential for creating effective AsBuiltReport modules.

### Core PScribo Concepts

PScribo organises reports using a hierarchical structure:

- **Document**: The root container for your entire report
- **Section**: Logical divisions within your report (e.g., "Infrastructure", "Storage")
- **Paragraph**: Text content and headings
- **Table**: Structured data presentation
- **BlankLine**: Spacing and formatting
- **Write-PScriboMessage**: Writes a formatted verbose output message with the time and PScribo plugin name

### Essential PScribo Commandlets

```powershell title="List PScribo commands"
# List all PScribo Commandlets
Get-Command -Module PScribo
```

#### Document Structure

PScribo section styles control both visual hierarchy and Table of Contents (TOC) inclusion. To keep the TOC readable, headings at `Heading5` and above should use a `NOTOCHeading` style so they do not appear in the TOC.

| Style | TOC | Typical use |
|-------|-----|-------------|
| `Heading1` | Yes | Top-level report section (e.g. tenant, site) |
| `Heading2` | Yes | Major resource category |
| `Heading3` | Yes | Resource type within a category |
| `Heading4` | Yes | Individual resource instance |
| `NOTOCHeading5` | No | Sub-detail within a resource instance |
| `NOTOCHeading6` | No | Further nesting below Heading5 |

```powershell title="Section heading styles"
Section -Name 'Infrastructure' -Style Heading1 {

    Section -Name 'Compute' -Style Heading2 {

        Section -Name 'Virtual Machines' -Style Heading3 {

            foreach ($VM in $VMs) {
                Section -Name $VM.Name -Style Heading4 {

                    Section -Name 'Network Adapters' -Style NOTOCHeading5 {
                        # Detail tables that should not clutter the TOC
                    }
                }
            }
        }
    }
}
```

#### Content Creation
```powershell title="Add content to report sections"
# Add descriptive text
Paragraph "This section provides detailed information about the virtual infrastructure."

# Add spacing between sections
BlankLine

# Create tables from data
$VMData | Table @TableParams
```

#### Messaging and Logging
```powershell title="User feedback and logging"
# Provide user feedback during report generation
Write-PScriboMessage -Plugin "Module" -Message "Collecting virtual machine information..."

# Warning messages for missing data or errors
Write-PScriboMessage -Plugin "Module" -IsWarning "Unable to collect storage information: $($_.Exception.Message)"
```

### Table Standards

PScribo tables are the primary method for presenting structured data. Use `List = $false` for multi-row collections and `List = $true` for single-object key-value pairs.

**Column width rules:**

- Always specify `ColumnWidths` to avoid excessive text wrapping
- List tables (`List = $true`) should use `40, 60` whenever possible
- Non-list table column widths should sum to 100 and be sized to the data

**Caption rule:** Always include a caption when `$Report.ShowTableCaptions` is set.

```powershell title="Multi-row collection table (List = false)"
$ServerData = foreach ($Server in $Servers) {
    [PSCustomObject]@{
        'Server Name'  = $Server.Name
        'OS Version'   = $Server.OperatingSystem
        'CPU Cores'    = $Server.ProcessorCount
        'Memory (GB)'  = [Math]::Round($Server.TotalPhysicalMemory / 1GB, 2)
        'CPU Usage %'  = $Server.CPUUsagePercent
        'Status'       = $Server.Status
    }
}

$TableParams = @{
    Name         = 'Server Inventory'
    List         = $false
    ColumnWidths = 20, 20, 12, 13, 15, 20
}

if ($Report.ShowTableCaptions) {
    $TableParams['Caption'] = "- $($TableParams.Name)"
}

$ServerData | Sort-Object 'Server Name' | Table @TableParams
```

```powershell title="Single-object key-value table (List = true)"
$ServerInfo = [PSCustomObject]@{
    'Server Name' = $Server.Name
    'Version'     = $Server.Version
    'Build'       = $Server.Build
    'Edition'     = $Server.Edition
}

$TableParams = @{
    Name         = 'Server Information'
    List         = $true
    ColumnWidths = 40, 60
}

if ($Report.ShowTableCaptions) {
    $TableParams['Caption'] = "- $($TableParams.Name)"
}

$ServerInfo | Table @TableParams
```

### Conditional Formatting and Styling

Use PScribo styling to highlight important information based on health checks:

```powershell title="Apply conditional formatting for health checks"
if ($ReportConfig.HealthCheck.Infrastructure.CPUUtilisation) {
    foreach ($Server in $ServerData) {
        if ($Server.'CPU Usage %' -gt $ReportConfig.HealthCheck.Infrastructure.CPUThreshold) {
            $Server | Set-Style -Style Critical -Property 'CPU Usage %'
        } elseif ($Server.'CPU Usage %' -gt ($ReportConfig.HealthCheck.Infrastructure.CPUThreshold * 0.8)) {
            $Server | Set-Style -Style Warning -Property 'CPU Usage %'
        }
    }
}
```

## AsBuiltReport Core Integration

### Configuration Management

AsBuiltReport.Core acts as the orchestrator: it reads your module's JSON configuration file and language files, then injects pre-populated variables into your module's scope before calling your `Invoke-AsBuiltReport.*` function. You do not declare or populate these variables yourself — they are always present when your function runs.

| Variable | Source | Contents |
|---|---|---|
| `$ReportConfig` | Your module's `.json` configuration file | Parsed JSON as a PowerShell object |
| `$reportTranslate` | Your module's language `.psd1` file | Parsed translation hashtable |

Both variables are set in the script scope by AsBuiltReport.Core immediately before your module's main function is called. This means they are readable anywhere in your module — including inside private functions — without needing to be passed as parameters.

```powershell title="Access report configuration"
# Access configuration sections in your module
$Report = $ReportConfig.Report
$InfoLevel = $ReportConfig.InfoLevel
$Options = $ReportConfig.Options
$HealthCheck = $ReportConfig.HealthCheck

# Use InfoLevel to control data collection and presentation
if ($InfoLevel.Infrastructure -ge 2) {
    # Collect detailed infrastructure information
    $DetailedInfo = Get-DetailedInfrastructure
}
```

### Standard Module Messages

Include standard informational messages at the beginning of your module using `Write-ReportModuleInfo`

```powershell title="Display module information"
Write-ReportModuleInfo -ModuleName "Vendor.Technology"
```

### Version Checking

Include version checking for prerequisite PowerShell modules by using `Get-RequiredModule`

```powershell title="Check prerequisite module versions"
# Throws a terminating error if the module is not installed or the installed version is below the minimum.
# On success, prints the module name and installed version.
Get-RequiredModule -Name 'Az' -Version '14.4.0'
```

## Report Structure and Flow

### Hierarchical Organisation

Structure your reports logically using PScribo sections:

```powershell title="Organise report with nested sections"
# Main infrastructure section
Section -Name 'Infrastructure' -Style Heading1 {

    # Subsection for compute resources
    Section -Name 'Compute Resources' -Style Heading2 {
        if ($InfoLevel.Infrastructure -ge 1) {
            # Summary information
            Section -Name 'Host Summary' -Style Heading3 {
                $HostSummary | Table @TableParams
            }
        }

        if ($InfoLevel.Infrastructure -ge 3) {
            # Detailed individual host information
            Section -Name 'Host Details' -Style Heading3 {
                foreach ($Host in $Hosts) {
                    Section -Name $Host.Name -Style Heading4 {
                        $HostDetails | Table @TableParams
                    }
                }
            }
        }
    }
}
```

### InfoLevel-Driven Content

Use InfoLevel settings to control the depth of information presented:

```powershell title="Control content depth with InfoLevel"
# Implement progressive information disclosure
switch ($InfoLevel.Storage) {
    0 {
        # Skip storage section entirely
        break
    }
    1 {
        # Show only storage summary
        $StorageSummary | Table @SummaryTableParams
    }
    {$_ -ge 2} {
        # Show storage summary and datastore information
        $StorageSummary | Table @SummaryTableParams
        $Datastores | Table @DatastoreTableParams
    }
    {$_ -ge 4} {
        # Add storage performance metrics
        $StorageSummary | Table @SummaryTableParams
        $Datastores | Table @DatastoreTableParams
        $StoragePerformance | Table @PerformanceTableParams
    }
}
```

### Error Handling in Reports

Implement graceful error handling that doesn't break report generation:

```powershell title="Graceful error handling in reports"
# Collect data with error resilience
try {
    Write-PScriboMessage -Plugin "Module" -Message "Collecting network information..."
    $NetworkData = Get-NetworkConfiguration -ErrorAction Stop

    if ($NetworkData) {
        Section -Name 'Network Configuration' -Style Heading2 {
            $NetworkData | Table @NetworkTableParams
        }
    } else {
        Section -Name 'Network Configuration' -Style Heading2 {
            Paragraph "No network configuration data available."
        }
    }

} catch {
    Write-PScriboMessage -Plugin "Module" -IsWarning "Unable to collect network information: $($_.Exception.Message)"

    Section -Name 'Network Configuration' -Style Heading2 {
        Paragraph "Network configuration data could not be retrieved. Please check connectivity and permissions."
    }
}
```

## Function Design and Implementation

### Main Function
Every module must export a single main function following this pattern:

```powershell title="Main module function template"
function Invoke-AsBuiltReport.Vendor.Technology {
    <#
    .SYNOPSIS
        A PowerShell function to generate a [Vendor] [Technology] As Built report.
    .DESCRIPTION
        Documents the configuration of [Vendor] [Technology] in Word/HTML/Text formats.
    .PARAMETER Target
        The target [Vendor] [Technology] system(s) to report on.
    .PARAMETER Credential
        PowerShell credential to use for authentication.
    .NOTES
        Version:        0.1.0
        Author:         Your Name
        Creation Date:  YYYY-MM-DD
        Purpose/Change: Initial script development
    .LINK
        https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology
    .EXAMPLE
        PS C:\> Invoke-AsBuiltReport.Vendor.Technology -Target '192.168.1.100' -Credential $cred
    #>

    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $false)]
        [ValidateNotNullOrEmpty()]
        [String[]] $Target,

        [Parameter(Mandatory = $true, ValueFromPipeline = $false)]
        [ValidateNotNullOrEmpty()]
        [PSCredential] $Credential
    )

    # Displays the module name and version number at the start of report generation
    Write-ReportModuleInfo -ModuleName 'Vendor.Technology'

    # Import Report Configuration
    $Report = $ReportConfig.Report
    $InfoLevel = $ReportConfig.InfoLevel
    $Options = $ReportConfig.Options
    $LocalizedData = $reportTranslate.InvokeAsBuiltReportVendorTechnology

    # Used to convert strings to TitleCase where required, e.g. $TextInfo.ToTitleCase('powered on') returns 'Powered On'
    $TextInfo = (Get-Culture).TextInfo

    #region foreach loop
    foreach ($System in $Target) {
        try {
            Write-PScriboMessage ($LocalizedData.Connecting -f $System)

            # Establish a connection to the target system.
            # Replace this with the appropriate connection cmdlet for your technology.
            # Store the connection object so it can be used by private functions and
            # closed in the end{} block.
            $script:Connection = Connect-VendorSystem -Server $System -Credential $Credential -ErrorAction Stop  # script: scope makes this readable by all Get-Abr* private functions without passing it as a parameter

            Section -Style Heading1 $System {
                # Call private functions here, one per report section.
                # Each function collects data from $script:Connection and renders a PScribo section.
                Get-Abr[VendorAbbr|Technology][Resource]
            }

        } catch {
            Write-PScriboMessage -IsWarning ($LocalizedData.ConnectionError -f $System, $_.Exception.Message)
        }
    }
    #endregion foreach loop

    end {
        # Disconnect from the target system and clean up any open sessions.
        if ($script:Connection) {
            Disconnect-VendorSystem -Connection $script:Connection -Confirm:$false -ErrorAction SilentlyContinue
        }
    }
}
```

### Private Functions

Private functions in `Src/Private/` serve two distinct purposes:

- **Report section functions** (`Get-Abr[VendorAbbr|Technology][Resource]`) — each responsible for collecting data from the target system and rendering it as a PScribo section. Every report section function must have its own `.ps1` file named after the function (e.g. `Get-AbrVendorLocation.ps1`). Following PowerShell naming conventions, the resource noun must be **singular** (e.g. `Get-AbrVbrBackupJob`, not `Get-AbrvSphereVMHost`).
- **Utility helpers** (`ConvertTo-HashToYN`, `ConvertTo-TextYN`, connection helpers, etc.) — reusable functions that support report section functions. These may be grouped into a dedicated helper file (`Src/Private/Helpers.ps1`).

#### Functions must be self-contained

Every **report section function** must be **readable in isolation**. A reviewer should be able to understand what data is collected, what the table will look like, and how it is rendered, without opening any other file.

Keep the `[ordered]@{}` property list, `$TableParams` definition, and `Table @TableParams` call **inline** within each function body. Do not delegate these to generic table-construction or rendering wrappers. These abstractions hide which data and columns appear in the output, making the function harder to follow during review.

Utility helpers like `ConvertTo-HashToYN` and `ConvertTo-TextYN` are fine. They transform individual values without hiding the overall data shape or column selection. Avoid wrappers that accept a data object and produce a table, as the structure of the output is no longer visible in the function body.

#### Private Function Structure

All report section functions should follow this pattern:

```powershell
function Get-Abr[VendorAbbr|Technology][Resource] {
    <#
    .SYNOPSIS
        Used by As Built Report to retrieve <Vendor> <Technology> section information.
    .DESCRIPTION
        Documents the configuration of <Vendor> <Technology> in Word/HTML/Text formats using PScribo.
    .NOTES
        Version:    0.1.0
        Author:     Your Name
    .LINK
        https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology
    #>
    [CmdletBinding()]
    param ()

    begin {
        Write-PScriboMessage "Collecting <section> information."
        $LocalizedData = $reportTranslate.GetAbrVendorSectionName
    }

    process {
        try {
            $Data = Get-VendorApiData
            if ($Data) {
                Section -Style Heading3 $LocalizedData.Heading {
                    Paragraph $LocalizedData.Paragraph
                    BlankLine
                    $OutObj = @()
                    foreach ($Item in $Data) {
                        try {
                            $inObj = [ordered] @{
                                $LocalizedData.Name    = $Item.Name
                                $LocalizedData.Status  = $Item.Status
                                $LocalizedData.Version = $Item.Version
                            }
                            $OutObj += [pscustomobject]$inObj
                        } catch {
                            Write-PScriboMessage -IsWarning "$($Item.Name): $($_.Exception.Message)"
                        }
                    }
                    $TableParams = @{
                        Name         = $LocalizedData.TableHeading
                        List         = $false
                        ColumnWidths = 40, 30, 30
                    }
                    if ($Report.ShowTableCaptions) {
                        $TableParams['Caption'] = "- $($TableParams.Name)"
                    }
                    $OutObj | Sort-Object $LocalizedData.Name | Table @TableParams
                }
            }
        } catch {
            Write-PScriboMessage -IsWarning "<Section>: $($_.Exception.Message)"
        }
    }
    end {}
}
```

This example demonstrates:

- **Data collected upfront** (`Get-VendorApiData`) before any PScribo calls, so collection errors are isolated from rendering
- **`begin/process/end` blocks** — `begin` logs progress and loads translations; `process` contains all data collection and rendering; `end` is used for cleanup such as disconnecting sessions
- **`[ordered]@{}` built inline** with explicit, named property-to-column mappings visible at a glance
- **`$TableParams` defined inline** so column widths and table type are immediately clear
- **`Table @TableParams` called directly** — no intermediate rendering wrapper
- **`try/catch` at both levels** — the outer `catch` protects the section as a whole; the inner `catch` protects individual items so one bad record does not abort the entire table
- **Graceful continuation** — the section renders what it can and logs warnings for failures

## Language Support Implementation

AsBuiltReport.Core v1.5.0+ introduces comprehensive multilingual support, allowing report modules to generate documentation in multiple languages. This section explains how to implement language support in your report module.

### Overview

The language support system consists of two components:

1. **UI Language** (Core Module): Translates on-screen prompts and messages based on the user's PowerShell session culture
2. **Document Language** (Report Module): Translates report content (headings, text, tables) based on the specified report language

### Language Selection Priority

Report modules use the following priority for determining the document language:

1. [New-AsBuiltReport](../user-guide/new-asbuiltreport.md) `-ReportLanguage` parameter (if explicitly specified by user)
2. `Report.Language` setting from [report JSON configuration file](creating-a-report-module.md#json-configuration-structure)
3. Default fallback to 'en-US'

### Creating Language Files

#### Directory Structure
Create a `Language` folder in your module root with subfolders for each supported language:

```text title="Language folder structure"
AsBuiltReport.Vendor.Technology/
└── AsBuiltReport.Vendor.Technology/
    └── Language/
        ├── en-US/
        │   └── VendorTechnology.psd1
        ├── es-ES/
        │   └── VendorTechnology.psd1
        ├── fr-FR/
        │   └── VendorTechnology.psd1
        └── de-DE/
            └── VendorTechnology.psd1
```

#### Language File Format
Language files use PowerShell data files (.psd1) with a hashtable structure containing multiple `ConvertFrom-StringData` blocks. This format allows you to organise translations by function or section:

```powershell title="Language file template (en-US)"
# culture = 'en-US'
@{
    # Main module translations
    InvokeAsBuiltReportVendorTechnology = ConvertFrom-StringData @'
        Connecting = Connecting to {0}.
        DefaultOrder = No custom section order specified. Using default order.
        CustomOrder = Using custom section order from report JSON configuration.
        InfoLevelNotFound = InfoLevel for '{0}' not found.
        SectionError = Error processing section '{0}': {1}
'@

    # Virtual Machine section translations (Get-AbrVirtualMachine)
    GetAbrVirtualMachine = ConvertFrom-StringData @'
        InfoLevel = VirtualMachine InfoLevel set at {0}.
        Collecting = Collecting Virtual Machine information.
        SectionInfo = Virtual machines provide compute resources in a virtualized environment.
        ParagraphSummary = The following table summarizes the virtual machines within the {0} environment.

        Heading = Virtual Machines
        TableHeading = Virtual Machines
        Name = Name
        PowerState = Power State
        PoweredOn = Powered On
        PoweredOff = Powered Off
        CPUCount = CPU Count
        MemoryGB = Memory (GB)
        StorageGB = Storage (GB)
        GuestOS = Guest OS
        IPAddress = IP Address
        None = None
'@

    # Storage section translations (Get-AbrStorageInfo)
    GetAbrStorageInfo = ConvertFrom-StringData @'
        InfoLevel = Storage InfoLevel set at {0}.
        Collecting = Collecting Storage information.
        ParagraphSummary = The following table summarizes the storage configuration within the {0} environment.

        Heading = Storage
        TableHeading = Storage Details
        Name = Name
        Type = Type
        CapacityGB = Capacity (GB)
        UsedGB = Used (GB)
        FreeGB = Free (GB)
        PercentUsed = Percent Used
'@
}
```

**Spanish (es-ES) example:**
```powershell title="Language file example (es-ES)"
# culture = 'es-ES'
@{
    # Traducciones principales del módulo
    InvokeAsBuiltReportVendorTechnology = ConvertFrom-StringData @'
        Connecting = Conectando a {0}.
        DefaultOrder = No se especificó un orden de sección personalizado. Usando orden predeterminado.
        CustomOrder = Usando orden de sección personalizado de la configuración JSON del informe.
        InfoLevelNotFound = InfoLevel para '{0}' no encontrado.
        SectionError = Error al procesar la sección '{0}': {1}
'@

    # Traducciones de sección de máquinas virtuales
    GetAbrVirtualMachine = ConvertFrom-StringData @'
        InfoLevel = VirtualMachine InfoLevel establecido en {0}.
        Collecting = Recopilando información de máquinas virtuales.
        SectionInfo = Las máquinas virtuales proporcionan recursos informáticos en un entorno virtualizado.
        ParagraphSummary = La siguiente tabla resume las máquinas virtuales en el entorno {0}.

        Heading = Máquinas Virtuales
        TableHeading = Máquinas Virtuales
        Name = Nombre
        PowerState = Estado de Energía
        PoweredOn = Encendido
        PoweredOff = Apagado
        CPUCount = Recuento de CPU
        MemoryGB = Memoria (GB)
        StorageGB = Almacenamiento (GB)
        GuestOS = SO Invitado
        IPAddress = Dirección IP
        None = Ninguno
'@

    # Traducciones de sección de almacenamiento
    GetAbrStorageInfo = ConvertFrom-StringData @'
        InfoLevel = Storage InfoLevel establecido en {0}.
        Collecting = Recopilando información de almacenamiento.
        ParagraphSummary = La siguiente tabla resume la configuración de almacenamiento en el entorno {0}.

        Heading = Almacenamiento
        TableHeading = Detalles de Almacenamiento
        Name = Nombre
        Type = Tipo
        CapacityGB = Capacidad (GB)
        UsedGB = Usado (GB)
        FreeGB = Libre (GB)
        PercentUsed = Porcentaje Usado
'@
}
```

**Key formatting requirements:**

- File must start with a culture comment: `# culture = 'en-US'`
- Use a hashtable structure with `@{ }` wrapping all translations
- Group translations by function name (e.g., `GetAbrVirtualMachine`)
- Each group uses `ConvertFrom-StringData @'...'@` for its translations
- Use meaningful key names that describe the content
- Use format strings (`{0}`, `{1}`) for dynamic values
- Include comments to organise sections within the file

### Implementing Language Support in Your Module

Language support is automatically initialised by the AsBuiltReport.Core module when a report is generated. The Core module loads your language files based on the available and/or configured language and makes translations available through the `$reportTranslate` global variable.

**What you need to do:**

1. Create language files in the `Language/` folder structure
2. Declare a local `$LocalizedData` variable in each function by accessing the appropriate key from the `$reportTranslate` global variable

**What the Core module handles automatically:**

- Loading the appropriate language file based on user configuration
- Falling back to parent languages or 'en-US' if needed
- Setting the `$reportTranslate` global variable
- Managing culture-specific formatting

#### Using Translations in Your Report Module

In each function, declare a local `$LocalizedData` variable at the top by accessing the matching key from `$reportTranslate`. This scopes translations to the current function and keeps the code readable.

**In the main `Invoke-AsBuiltReport` function:**

```powershell title="Declare $LocalizedData in the main function"
$LocalizedData = $reportTranslate.InvokeAsBuiltReportVendorTechnology
```

**In each private `Get-Abr*` function (in the `begin{}` block):**

```powershell title="Declare $LocalizedData in private functions"
begin {
    $LocalizedData = $reportTranslate.GetAbrVirtualMachine
    Write-PScriboMessage ($LocalizedData.InfoLevel -f $InfoLevel.VirtualMachine)
    Write-PScriboMessage $LocalizedData.Collecting
}
```

Once declared, use `$LocalizedData` throughout the function for all headings, messages, paragraphs, and table column headers:

```powershell title="Use $LocalizedData in report code"
process {
    try {
        Section -Style Heading2 $LocalizedData.Heading {

            Paragraph $LocalizedData.SectionInfo
            Paragraph ($LocalizedData.ParagraphSummary -f $System)

            $VMData = foreach ($VM in $VMs) {
                [Ordered]@{
                    $LocalizedData.Name       = $VM.Name
                    $LocalizedData.PowerState = if ($VM.PowerState -eq 'PoweredOn') {
                        $LocalizedData.PoweredOn
                    } else {
                        $LocalizedData.PoweredOff
                    }
                    $LocalizedData.CPUCount   = $VM.NumCpu
                    $LocalizedData.MemoryGB   = $VM.MemoryGB
                    $LocalizedData.StorageGB  = [Math]::Round($VM.ProvisionedSpaceGB, 2)
                    $LocalizedData.GuestOS    = $VM.GuestOS
                }
            }

            if ($VMData) {
                $TableParams = @{
                    Name         = $LocalizedData.TableHeading
                    List         = $false
                    ColumnWidths = 20, 15, 10, 12, 12, 20
                }
                if ($Report.ShowTableCaptions) {
                    $TableParams['Caption'] = "- $($TableParams.Name)"
                }
                $VMData | Sort-Object $LocalizedData.Name | Table @TableParams
            } else {
                Paragraph $LocalizedData.None
            }
        }
    } catch {
        Write-PScriboMessage -IsWarning "$($LocalizedData.ErrorMessage) $($_.Exception.Message)"
    }
}
```

### Culture Fallback System

AsBuiltReport implements intelligent culture fallback through the `Resolve-Culture` function:

**Example fallback chains:**
- `fr-CA` (French-Canada) → `fr-FR` → `en-US`
- `es-MX` (Spanish-Mexico) → `es-ES` → `en-US`
- `en-AU` (English-Australia) → `en-GB` → `en-US`
- `zh-HK` (Chinese-Hong Kong) → `zh-Hant` → `zh-TW` → `en-US`

This ensures that if a specific regional translation isn't available, the module will use the parent language before falling back to English.

### Supported Language Codes

The following language codes are supported with comprehensive fallback mappings:

| Code | Language | Code | Language |
| --- | --- | --- | --- |
| en-US | English (US) | ja-JP | Japanese |
| en-GB | English (UK) | ko-KR | Korean |
| es-ES | Spanish (Spain) | nl-NL | Dutch |
| es-MX | Spanish (Mexico) | sv-SE | Swedish |
| fr-FR | French (France) | nb-NO | Norwegian |
| fr-CA | French (Canada) | da-DK | Danish |
| de-DE | German (Germany) | fi-FI | Finnish |
| it-IT | Italian | pl-PL | Polish |
| pt-PT | Portuguese (Portugal) | cs-CZ | Czech |
| pt-BR | Portuguese (Brazil) | hu-HU | Hungarian |
| ru-RU | Russian | tr-TR | Turkish |
| ar-SA | Arabic | el-GR | Greek |
| zh-CN | Chinese (Simplified) | he-IL | Hebrew |
| zh-TW | Chinese (Traditional) | hi-IN | Hindi |
| zh-Hans | Chinese (Simplified) | th-TH | Thai |
| zh-Hant | Chinese (Traditional) | vi-VN | Vietnamese |

### Best Practices

1. **Start with en-US**: Always create the English (US) language file first as this is the fallback language
2. **Consistent Key Names**: Use descriptive, consistent key names across all language files
3. **Avoid Hardcoded Text**: Never hardcode text in your module - always use translation keys
4. **Test Fallbacks**: Test your module with various language settings to ensure fallback chains work correctly
5. **Format Strings**: Use PowerShell format strings (`{0}`, `{1}`) for dynamic values:
   ```powershell title="Format strings for dynamic values"
   # In language file:
   VMCount = Found {0} virtual machines

   # In code:
   Paragraph ($LocalizedData.VMCount -f $VMs.Count)
   ```
6. **RTL Language Support**: For right-to-left languages (Arabic, Hebrew), ensure your table layouts work correctly

### Testing Language Support

Test your module with different languages:

```powershell title="Test reports with different languages"
# Test with Spanish
New-AsBuiltReport -Report Vendor.Technology -Target server01 -Credential $cred -ReportLanguage 'es-ES'

# Test with French (uses configuration file setting)
New-AsBuiltReport -Report Vendor.Technology -Target server01 -Credential $cred -ReportConfigFilePath 'C:\Config\report-fr.json'

# Test fallback (if es-MX not available, falls back to es-ES)
New-AsBuiltReport -Report Vendor.Technology -Target server01 -Credential $cred -ReportLanguage 'es-MX'
```

### Example: Complete Language Implementation

Here's a complete example showing language support implementation:

```powershell title="Complete language implementation example"
function Invoke-AsBuiltReport.Vendor.Technology {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [String[]] $Target,

        [Parameter(Mandatory = $true)]
        [PSCredential] $Credential
    )

    $Report     = $ReportConfig.Report
    $InfoLevel  = $ReportConfig.InfoLevel
    $Options    = $ReportConfig.Options

    # Scope translations for this function from the global $reportTranslate hashtable
    $LocalizedData = $reportTranslate.InvokeAsBuiltReportVendorTechnology

    foreach ($System in $Target) {
        try {
            Write-PScriboMessage ($LocalizedData.Connecting -f $Target)

            Section -Style Heading1 $LocalizedData.Heading {
                Get-AbrVTVirtualMachine
            }
        } catch {
            Write-PScriboMessage -IsWarning ($LocalizedData.ConnectionError -f $Target, $_.Exception.Message)
        }
    }
}

function Get-AbrVTVirtualMachine {
    [CmdletBinding()]
    param ()

    begin {
        # Scope translations for this function
        $LocalizedData = $reportTranslate.GetAbrVTVirtualMachine
        Write-PScriboMessage ($LocalizedData.InfoLevel -f $InfoLevel.VirtualMachine)
        Write-PScriboMessage $LocalizedData.Collecting
    }

    process {
        try {
            $VMs = Get-VTVirtualMachine -ErrorAction Stop

            if ($VMs) {
                Section -Style Heading2 $LocalizedData.Heading {

                    Paragraph $LocalizedData.SectionInfo
                    Paragraph ($LocalizedData.ParagraphSummary -f $System)

                    $VMInfo = foreach ($VM in $VMs) {
                        [Ordered]@{
                            $LocalizedData.Name       = $VM.Name
                            $LocalizedData.PowerState = if ($VM.PowerState -eq 'PoweredOn') {
                                $LocalizedData.PoweredOn
                            } else {
                                $LocalizedData.PoweredOff
                            }
                            $LocalizedData.CPUCount   = $VM.NumCpu
                            $LocalizedData.MemoryGB   = $VM.MemoryGB
                        }
                    }

                    $TableParams = @{
                        Name         = $LocalizedData.TableHeading
                        List         = $false
                        ColumnWidths = 30, 20, 25, 25
                    }
                    if ($Report.ShowTableCaptions) {
                        $TableParams['Caption'] = "- $($TableParams.Name)"
                    }
                    $VMInfo | Sort-Object $LocalizedData.Name | Table @TableParams
                }
            } else {
                Paragraph $LocalizedData.None
            }
        } catch {
            Write-PScriboMessage -IsWarning "$($LocalizedData.ErrorMessage) $($_.Exception.Message)"
        }
    }
}
```

### Migration Guide for Existing Modules

To add language support to an existing report module:

1. **Create the language directory structure**
   - Create `Language/en-US/` folder in your module root
   - Create a .psd1 file named after your module (without dots)

2. **Extract hardcoded strings**
   - Identify all hardcoded text in your module (section titles, table headers, messages, etc.)
   - Add them to the 'en-US' language file using the hashtable structure
   - Group translations by function name for better organisation

3. **Replace hardcoded strings**
   - Declare `$LocalizedData = $reportTranslate.FunctionName` at the top of each function (or in the `begin{}` block)
   - Replace all hardcoded text with `$LocalizedData.Key` references

4. **Update JSON configuration**
   - Add the `"Language": "en-US"` property to your JSON configuration template

5. **Test thoroughly**
   - Test with 'en-US' to ensure all translations work correctly
   - Verify that no hardcoded strings remain
   - Test table formatting and column widths

6. **Add additional languages**
   - Create language folders for other languages (es-ES, fr-FR, etc.)
   - Translate all strings while maintaining the same structure and keys
   - Test fallback behaviour

7. **Update documentation**
   - Update your module's README with supported languages
   - Document any language-specific considerations
   - Include example usage with `-ReportLanguage` parameter

!!! note
    The AsBuiltReport.Core module automatically handles language initialisation - you don't need to call `Initialize-LocalizedData` in your report module.

## PowerShell Best Practices

### Naming Conventions
Follow PowerShell and .NET naming standards:

- **PascalCase** for all public members, types, and namespace names
- **Verb-Noun** pattern for function names (e.g., `Get-AbrServerInfo`)
- **Descriptive** variable names that clearly indicate purpose
- **Consistent** parameter naming across functions

### Code Organisation and Style

:octicons-check-circle-fill-16:{ .check-circle } DO
```powershell title="Good PowerShell practices"
# Use PascalCasing for functions and parameters
function Get-AbrVirtualMachine {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [String] $Server
    )

    # Use try-catch for error handling
    try {
        $VMs = Get-VM -Server $Server -ErrorAction Stop

        # Create PSCustomObjects for table data
        $VMInfo = foreach ($VM in $VMs) {
            [PSCustomObject]@{
                'VM Name' = $VM.Name
                'Power State' = $VM.PowerState
                'CPU Count' = $VM.NumCpu
                'Memory (GB)' = [Math]::Round($VM.MemoryGB, 2)
            }
        }

        # Use consistent table parameters
        $TableParams = @{
            Name = 'Virtual Machine Summary'
            List = $false
            ColumnWidths = 25, 25, 25, 25
        }

        if ($Report.ShowTableCaptions) {
            $TableParams['Caption'] = "- $($TableParams.Name)"
        }

        $VMInfo | Sort-Object 'VM Name' | Table @TableParams

    } catch {
        Write-PScriboMessage -IsWarning "Unable to collect VM information: $($_.Exception.Message)"
    }
}
```

:octicons-x-circle-fill-16:{ .x-circle-fill } DO NOT
```powershell title="Avoid these practices"
# Avoid functions within report scripts
# Avoid hardcoded credentials
# Avoid excessive global variables
# Avoid unclear variable names like $a, $temp, $data
```

### Parameter Validation
Implement robust parameter validation:

```powershell title="Parameter validation examples"
param (
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [ValidateSet('Server', 'Cluster', 'Datacenter')]
    [String] $Scope,

    [Parameter(Mandatory = $false)]
    [ValidateRange(1, 5)]
    [Int] $InfoLevel = 2,

    [Parameter(Mandatory = $true)]
    [ValidateScript({Test-Connection $_ -Count 1 -Quiet})]
    [String] $Target
)
```

### Error Handling
Implement comprehensive error handling:

```powershell title="Comprehensive error handling"
try {
    # Validate prerequisites
    if (-not (Get-Module VCF.PowerCLI -ListAvailable)) {
        throw "VCF.PowerCLI module is required but not installed"
    }

    # Attempt connection
    $Connection = Connect-VIServer -Server $Target -Credential $Credential -ErrorAction Stop

    # Collect data with nested error handling
    try {
        $Data = Get-Cluster -Server $Connection -ErrorAction Stop
    } catch {
        Write-PScriboMessage -IsWarning "Unable to collect cluster data: $($_.Exception.Message)"
        return
    }

} catch {
    Write-Error "Failed to connect to $Target : $($_.Exception.Message)"
    return
} finally {
    # Always clean up connections
    if ($Connection) {
        Disconnect-VIServer -Server $Connection -Confirm:$false
    }
}
```

## Data Collection and Formatting

### Data Collection Strategy
Follow these patterns for efficient data collection:

1. **Batch Operations**: Collect all required data at the beginning
2. **Error Resilience**: Handle individual collection failures gracefully
3. **Performance**: Use efficient cmdlets and avoid unnecessary loops
4. **Caching**: Store frequently accessed data to avoid repeated calls

### Comprehensive Module Example

Here's a complete example showing how to structure a section of an AsBuiltReport module:

```powershell title="Complete module section example"
# Virtual Machine Section Example
if ($InfoLevel.VirtualMachines -gt 0) {
    Section -Name 'Virtual Machines' -Style Heading1 {

        Write-PScriboMessage -Plugin "Module" -Message "Collecting virtual machine information..."

        try {
            # Collect VM data with error handling
            $VMs = Get-VM -Server $Connection -ErrorAction Stop | Sort-Object Name

            if ($VMs) {
                # Summary table for InfoLevel 1+
                if ($InfoLevel.VirtualMachines -ge 1) {
                    $VMSummary = [PSCustomObject]@{
                        'Total VMs' = $VMs.Count
                        'Powered On' = ($VMs | Where-Object {$_.PowerState -eq 'PoweredOn'}).Count
                        'Powered Off' = ($VMs | Where-Object {$_.PowerState -eq 'PoweredOff'}).Count
                        'Total vCPUs' = ($VMs | Measure-Object -Property NumCpu -Sum).Sum
                        'Total Memory (GB)' = [Math]::Round(($VMs | Measure-Object -Property MemoryGB -Sum).Sum, 2)
                    }

                    Section -Name 'Virtual Machine Summary' -Style Heading2 {
                        $TableParams = @{
                            Name = 'VM Summary'
                            List = $true
                            ColumnWidths = 40, 60
                        }
                        if ($Report.ShowTableCaptions) {
                            $TableParams['Caption'] = "- $($TableParams.Name)"
                        }
                        $VMSummary | Table @TableParams
                    }
                }

                # Detailed VM information for InfoLevel 2+
                if ($InfoLevel.VirtualMachines -ge 2) {
                    Section -Name 'Virtual Machine Configuration' -Style Heading2 {

                        $VMDetails = foreach ($VM in $VMs) {
                            [PSCustomObject]@{
                                'VM Name' = $VM.Name
                                'Power State' = $VM.PowerState
                                'Guest OS' = $VM.Guest.OSFullName
                                'vCPUs' = $VM.NumCpu
                                'Memory (GB)' = $VM.MemoryGB
                                'Storage Used (GB)' = [Math]::Round($VM.UsedSpaceGB, 2)
                                'VM Tools Status' = $VM.Guest.ToolsStatus
                                'Host' = $VM.VMHost.Name
                            }
                        }

                        $TableParams = @{
                            Name = 'Virtual Machine Configuration'
                            List = $false
                            ColumnWidths = 15, 12, 18, 8, 10, 12, 12, 13
                        }
                        if ($Report.ShowTableCaptions) {
                            $TableParams['Caption'] = "- $($TableParams.Name)"
                        }

                        # Apply health checks if enabled
                        if ($ReportConfig.HealthCheck.VirtualMachines.VMToolsStatus) {
                            foreach ($VM in $VMDetails) {
                                if ($VM.'VM Tools Status' -eq 'toolsNotInstalled' -or $VM.'VM Tools Status' -eq 'toolsNotRunning') {
                                    $VM | Set-Style -Style Warning -Property 'VM Tools Status'
                                }
                            }
                        }

                        $VMDetails | Sort-Object 'VM Name' | Table @TableParams
                    }
                }

                # Resource allocation details for InfoLevel 3+
                if ($InfoLevel.VirtualMachines -ge 3) {
                    Section -Name 'VM Resource Allocation' -Style Heading2 {

                        $ResourceData = foreach ($VM in $VMs) {
                            [PSCustomObject]@{
                                'VM Name' = $VM.Name
                                'CPU Reservation (MHz)' = $VM.ResourceConfiguration.CpuAllocation.Reservation
                                'CPU Limit (MHz)' = if ($VM.ResourceConfiguration.CpuAllocation.Limit -eq -1) { 'Unlimited' } else { $VM.ResourceConfiguration.CpuAllocation.Limit }
                                'Memory Reservation (GB)' = [Math]::Round($VM.ResourceConfiguration.MemoryAllocation.Reservation / 1024, 2)
                                'Memory Limit (GB)' = if ($VM.ResourceConfiguration.MemoryAllocation.Limit -eq -1) { 'Unlimited' } else { [Math]::Round($VM.ResourceConfiguration.MemoryAllocation.Limit / 1024, 2) }
                                'CPU Shares' = $VM.ResourceConfiguration.CpuAllocation.Shares.Level
                                'Memory Shares' = $VM.ResourceConfiguration.MemoryAllocation.Shares.Level
                            }
                        }

                        $TableParams = @{
                            Name = 'VM Resource Allocation'
                            List = $false
                            ColumnWidths = 20, 15, 15, 15, 15, 10, 10
                        }
                        if ($Report.ShowTableCaptions) {
                            $TableParams['Caption'] = "- $($TableParams.Name)"
                        }

                        $ResourceData | Sort-Object 'VM Name' | Table @TableParams
                    }
                }

            } else {
                Section -Name 'Virtual Machines' -Style Heading2 {
                    Paragraph "No virtual machines were found."
                }
            }

        } catch {
            Write-PScriboMessage -Plugin "Module" -IsWarning "Unable to collect virtual machine information: $($_.Exception.Message)"

            Section -Name 'Virtual Machines' -Style Heading2 {
                Paragraph "Virtual machine information could not be retrieved. Please verify connectivity and permissions."
            }
        }

        BlankLine
    }
}
```

This example demonstrates:

- **InfoLevel-based content control** (different levels show progressively more detail)
- **Proper error handling** with informative messages
- **Consistent table formatting** with appropriate column widths
- **Health check integration** with conditional styling
- **Data transformation** into readable formats
- **User feedback** during data collection
- **Graceful degradation** when data isn't available

### Health Check Implementation
Implement health checks with configurable thresholds:

```powershell title="Health check implementation"
if ($ReportConfig.HealthCheck.Infrastructure.CPUUtilisation) {
    if ($Server.CPUUsage -gt $ReportConfig.HealthCheck.Infrastructure.CPUThreshold) {
        $ServerInfo | Set-Style -Style Warning -Property 'CPU Usage'
    }
}
```

## Testing and Quality Assurance

### Code Quality Tools
Use these tools to ensure code quality:

- **PSScriptAnalyzer**: Validate PowerShell best practices
- **Pester**: Create unit tests for functions
- **Manual Testing**: Test with various target environments

### Module Testing Requirements
Test your module for:

- **Import/Export**: Module loads and functions are available
- **Dependencies**: Required modules are properly declared
- **Functionality**: Core report generation works
- **Error Handling**: Graceful handling of common error scenarios
- **Cross-Platform**: Compatibility across PowerShell editions

### Pester Test Structure

All modules must include a `Tests/` directory with Pester v5 tests. The Plaster scaffold creates the initial test files; expand them as new functions are added.

#### Required test files

| File | Purpose |
|------|---------|
| `AsBuiltReport.Vendor.Technology.Tests.ps1` | Module manifest validation, directory structure, exported functions, private function inventory, JSON config schema, PSScriptAnalyzer |
| `LocalizationData.Tests.ps1` | Validates that all language files have identical keys and that no keys are missing from non-en-US files |
| `Invoke-Tests.ps1` | Test runner — invokes Pester with project-standard settings |

#### Running tests

```powershell title="Run the test suite"
# From the module root directory
.\Tests\Invoke-Tests.ps1

# Or invoke Pester directly
Invoke-Pester -Path .\Tests\ -Output Detailed
```

#### Key test categories

```powershell title="Test categories to cover"
Describe 'Module Manifest' {
    It 'Has a valid module version' { ... }
    It 'Exports the correct Invoke-AsBuiltReport function' { ... }
    It 'Declares AsBuiltReport.Core as a required module' { ... }
}

Describe 'Module Structure' {
    It 'Has a Src\Public directory' { ... }
    It 'Has a Src\Private directory' { ... }
    It 'Has a Language\en-US directory' { ... }
    It 'Has a Tests directory' { ... }
}

Describe 'Private Functions' {
    It 'Has a Get-Abr[VendorAbbr|Technology][Resource] function for each resource type' { ... }
}

Describe 'JSON Configuration' {
    It 'Has InfoLevel values in the range 0-5' { ... }
    It 'Has boolean HealthCheck values' { ... }
}

Describe 'Localization' {
    It 'en-US language file exists' { ... }
    It 'All language files have identical keys' { ... }
}

Describe 'Code Quality' {
    It 'Passes PSScriptAnalyzer with no errors or warnings' {
        $Results = Invoke-ScriptAnalyzer -Path .\Src\ -Recurse
        $Results | Should -BeNullOrEmpty
    }
}
```

## Documentation Standards

### README.md Requirements
Include these sections in your README:

```markdown title="README template structure"
# AsBuiltReport.Vendor.Technology

## Installation
Instructions for installing required modules

## System Requirements
- PowerShell version requirements
- Platform compatibility
- Vendor module prerequisites

## Configuration
Sample configuration with explanations

## Usage Examples
Basic usage scenarios with sample commands

## Sample Reports
Links to sample output documents. Generate samples by running the completed module against a real target environment using the `-Format Word,HTML,Text` parameter and placing the output files in the `Samples/` directory.
```

### Inline Documentation
Provide comprehensive comment-based help:

- **Synopsis**: Brief function description
- **Description**: Detailed explanation
- **Parameters**: Description for each parameter
- **Examples**: Real-world usage examples
- **Notes**: Version, author, and change information
- **Links**: Related documentation URLs

## Security Considerations

### Credential Management
- Accept `PSCredential` objects for authentication
- Never hardcode credentials in scripts
- Support various authentication methods per technology
- Provide guidance on secure credential storage

### Input Validation
- Validate all user inputs
- Sanitise data before processing
- Use parameter validation attributes
- Implement proper error boundaries

### Sensitive Information
- Avoid logging credentials or sensitive data
- Provide options to exclude sensitive information from reports
- Document security considerations in README

## Performance Guidelines

### Optimisation Strategies
- **Minimise API Calls**: Batch requests when possible
- **Efficient Data Structures**: Use appropriate collection types
- **Memory Management**: Dispose of large objects when done
- **Parallel Processing**: Consider workflow parallelisation for large environments

### Performance Testing
Test your module with:

- Small environments (1-10 objects)
- Medium environments (100-1000 objects)
- Large environments (1000+ objects)

## Version Control and Maintenance

### Semantic Versioning
Use semantic versioning (`Major.Minor.Patch`):

- **Major**: Breaking changes
- **Minor**: New features, backwards compatible
- **Patch**: Bug fixes

### Change Log Maintenance
Maintain `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/) format:

```markdown title="Changelog format example"
## [1.2.0] - 2024-MM-dd
### Added
- New health check for storage utilisation

### Changed
- Improved error handling for connection failures

### Fixed
- Resolved issue with special characters in server names
```

## Community and Contribution

### Following Project Standards
- Use the project's code style and conventions
- Follow the established Git workflow (feature branches, pull requests)
- Update documentation with any changes
- Include appropriate tests for new functionality

### Getting Help
- Review existing AsBuiltReport modules for reference
- Ask questions in GitHub discussions
- Follow the [contributing guidelines](contributing.md)
- Contact the maintainers for guidance

By following these standards and guidelines, you'll create high-quality AsBuiltReport modules that integrate seamlessly with the framework and provide consistent, professional documentation for your target technologies.