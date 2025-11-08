---
title: Installation Guide
description: Complete guide for installing AsBuiltReport modules from PowerShell Gallery, offline, or from GitHub
tags:
  - installation
  - getting-started
  - setup
  - powershell-gallery
  - offline
  - github
---

Please follow these quick and simple instructions to install AsBuiltReport.

## Installation Method Comparison

Choose the installation method that best fits your needs:

| Installation Method | When to Use | Stability | Internet Required |
|-------------------|-------------|-----------|-------------------|
| **[Online Installation](#online-installation)** | Standard installation with internet access | Stable releases | Yes |
| **[Offline Installation](#offline-installation)** | Air-gapped or restricted environments | Stable releases | No (after download) |
| **[GitHub Releases](#installing-from-github-releases)** | Cannot access PowerShell Gallery | Stable releases | Yes |
| **[GitHub Branches](#installing-from-github-branches)** | Testing features or contributing to development | Unstable/Development | Yes |

!!! tip "Recommended for Most Users"
    Use **Online Installation** from the PowerShell Gallery for the easiest and most reliable installation experience.

## System Requirements

AsBuiltReport will generally support both Windows PowerShell 5.1 and PowerShell 7, however each individual report will have its own system requirements.

Please refer to the [report module user guides](../user-guide/report-modules/overview.md) for PowerShell compatibility and system requirements.

### PowerShell Version

Open a PowerShell console and run the following command to determine your version of PowerShell.

```powershell title="Check PowerShell version"
$PSVersionTable
```

!!! example "$PSVersionTable Sample Output"
    | Name                      | Value                        |
    |---------------------------|------------------------------|
    | PSVersion                 | 7.2.5                        |
    | PSEdition                 | Core                         |
    | GitCommitId               | 7.2.5                        |
    | OS                        | Microsoft Windows 10.0.22000 |
    | Platform                  | Win32NT                      |
    | PSCompatibleVersions      | {1.0, 2.0, 3.0, 4.0…}        |
    | PSRemotingProtocolVersion | 2.3                          |
    | SerializationVersion      | 1.1.0.1                      |
    | WSManStackVersion         | 3.0                          |

### PowerShell Execution Policy

PowerShell's execution policy must allow running scripts. If you encounter errors about execution policy, run the following command:

```powershell title="Set execution policy for current user"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

!!! info "Execution Policy"
    This setting allows you to run local scripts and signed remote scripts. For more information, see [about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies).

### Module Dependencies

!!! warning "AsBuiltReport.Core Required"
    All AsBuiltReport report modules require **AsBuiltReport.Core** to be installed first. The Core module provides the framework that all report modules depend on.

    ```powershell title="Install AsBuiltReport.Core"
    Install-Module -Name 'AsBuiltReport.Core' -Scope 'CurrentUser'
    ```

    When installing from the PowerShell Gallery using `Install-Module`, dependencies are automatically installed. For manual installations (GitHub, offline), you must ensure AsBuiltReport.Core is installed first.

### Third Party PowerShell Modules

Please refer to the [report module user guide](../user-guide/report-modules/overview.md) to check the system requirements for each report. Please follow the report module instructions to install any third party PowerShell modules which may be required.

```powershell title="Install third party PowerShell modules"
# Install third party PowerShell module examples
Install-Module -Name 'VCF.PowerCLI' -Scope 'CurrentUser' -AllowClobber -SkipPublisherCheck
Install-Module -Name 'PureStoragePowerShellSDK' -Scope 'CurrentUser'
```

## Online Installation

For an online installation, install AsBuiltReport modules using the [PowerShell Gallery](https://www.powershellgallery.com/packages?q=Asbuiltreport*){:target="_blank"};

```powershell title="Find and install AsBuiltReport modules"
# Find AsBuiltReport modules published in the PowerShell Gallery
Find-Module -Name 'AsBuiltReport.*' -Repository 'PSGallery'

# Install AsBuiltReport module example
Install-Module -Name 'AsBuiltReport.VMware.vSphere' -Scope 'CurrentUser'
```

## Offline Installation

For an offline installation, perform the following steps from a machine with internet connectivity;

Save the required modules to a specified folder.

```powershell title="Find and save AsBuiltReport modules"
# Find AsBuiltReport modules published in the PowerShell Gallery
Find-Module -Name 'AsBuiltReport.*' -Repository 'PSGallery'

# Save AsBuiltReport module example
Save-Module -Name 'AsBuiltReport.VMware.vSphere' -Path 'C:\Path\To\Specified\Folder'
```

Copy the downloaded PowerShell module folders to a location that can be made accessible to the offline system.
e.g. USB Flash Drive, Internal File Share etc.

On the offline system, open a PowerShell console window and run the following command to determine the PowerShell module path.

**Windows**

```powershell title="View PowerShell module paths on Windows"
$env:PSModulePath -Split ';'
```

**macOS & Linux**

```powershell title="View PowerShell module paths on macOS & Linux"
$env:PSModulePath -Split ':'
```

Copy the downloaded PowerShell module folders to a folder specified in the `$env:PSModulePath` output.

## GitHub Installation

### Installing from GitHub Releases

GitHub Releases contain the same stable code versions published to the PowerShell Gallery. This method is useful when you cannot access the PowerShell Gallery or prefer to download modules directly from GitHub.

!!! info "When to Use This Method"
    Use GitHub Releases when:

    - You cannot access the PowerShell Gallery
    - You want to verify the source code before installation
    - You need to maintain a local archive of module versions

    For most users, installing from the PowerShell Gallery is simpler and recommended.

!!! note "Report Module Naming"
    In the examples below, replace `AsBuiltReport.Vendor.Technology` with the report module name you wish to install (e.g. `AsBuiltReport.VMware.vSphere`, `AsBuiltReport.Microsoft.AD`).

**Step 1: Download the Release**

**Via GitHub Web Interface:**

1. Navigate to the repository (e.g., `https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology`)
2. Click on **Releases** in the right sidebar (or go to `https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology/releases`)
3. Find the release version you want to install
4. Under **Assets**, download the ZIP file (usually named `AsBuiltReport.Vendor.Technology-vX.X.X.zip`)

**Via GitHub CLI:**

```bash title="Download release using GitHub CLI"
# List available releases
gh release list --repo AsBuiltReport/AsBuiltReport.Vendor.Technology

# Download specific release (replace v1.0.0 with desired version)
gh release download v1.0.0 --repo AsBuiltReport/AsBuiltReport.Vendor.Technology
```

**Via PowerShell:**

```powershell title="Download release using PowerShell"
# Set variables
$repo = "AsBuiltReport/AsBuiltReport.Vendor.Technology"
$version = "v1.0.0"  # Replace with desired version

# Get the release download URL
$release = Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/releases/tags/$version"
$asset = $release.assets | Where-Object { $_.name -like "*.zip" } | Select-Object -First 1

# Download the release
Invoke-WebRequest -Uri $asset.browser_download_url -OutFile "$env:TEMP\$($asset.name)"
```

**Step 2: Determine PowerShell Module Path**

Open a PowerShell console and run the following command to find your PowerShell module paths:

**Windows**

```powershell title="View PowerShell module paths on Windows"
$env:PSModulePath -Split ';'
```

**macOS & Linux**

```powershell title="View PowerShell module paths on macOS & Linux"
$env:PSModulePath -Split ':'
```

!!! tip "Recommended Module Path"
    For user-specific installations, use the path containing your user profile:

    - **Windows**: `C:\Users\YourUsername\Documents\PowerShell\Modules` (PowerShell 7) or `C:\Users\YourUsername\Documents\WindowsPowerShell\Modules` (Windows PowerShell 5.1)
    - **macOS**: `~/.local/share/powershell/Modules`
    - **Linux**: `~/.local/share/powershell/Modules`

**Step 3: Extract and Install the Module**

**Windows Example:**

```powershell title="Install module from GitHub release on Windows"
# Extract ZIP file (adjust paths and module name as needed)
$moduleName = "AsBuiltReport.Vendor.Technology"
$zipPath = "$env:TEMP\$moduleName-v1.0.0.zip"
$extractPath = "$env:TEMP\$moduleName"

Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force

# Copy module folder to PowerShell modules directory
$destination = "$HOME\Documents\PowerShell\Modules\$moduleName"
Copy-Item -Path "$extractPath\*" -Destination $destination -Recurse -Force
```

**macOS & Linux Example:**

```bash title="Install module from GitHub release on macOS & Linux"
# Extract ZIP file (adjust paths and module name as needed)
unzip ~/Downloads/AsBuiltReport.Vendor.Technology-v1.0.0.zip -d /tmp/module

# Copy module folder to PowerShell modules directory
cp -r /tmp/module/* ~/.local/share/powershell/Modules/AsBuiltReport.Vendor.Technology/
```

**Step 4: Verify Installation**

Verify the module is installed correctly:

```powershell title="Verify module installation"
# List installed AsBuiltReport modules
Get-Module -Name 'AsBuiltReport.*' -ListAvailable

# Import the module to test
Import-Module -Name 'AsBuiltReport.Vendor.Technology' -Force

# Check the module version
Get-Module -Name 'AsBuiltReport.Vendor.Technology'
```

### Installing from GitHub Branches

!!! warning "Development Code"
    Code downloaded from GitHub branches (especially development or feature branches) may be incomplete, untested, or in a non-working state. Only use this installation method if you need to test specific features or contribute to development. For production use, always install stable releases from the PowerShell Gallery.

To install a development version or specific branch from GitHub, follow these steps to download and install the code into your PowerShell module folder.

!!! note "Report Module Naming"
    In the examples below, replace `AsBuiltReport.Vendor.Technology` with the report module name you wish to install (e.g. `AsBuiltReport.VMware.vSphere`, `AsBuiltReport.Microsoft.AD`).

**Step 1: Download the Branch**

Navigate to the GitHub repository and download the desired branch as a ZIP file:

1. Go to the repository (e.g., `https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology`)
2. Click the **Code** button
3. Select the branch you want to download from the branch dropdown
4. Click **Download ZIP**

Alternatively, use Git to clone the specific branch:

```bash title="Clone specific branch using Git"
git clone -b branch-name https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology.git
```

**Installing from Pull Requests**

!!! info "Installing from Pull Requests"
    When installing from a pull request, you're testing code submitted by a contributor that hasn't been merged yet. This is useful for testing proposed changes or bug fixes before they're officially released. The code comes from the contributor's fork repository, not the main AsBuiltReport repository.

1. Navigate to the pull request on GitHub
2. Scroll to the bottom and find the branch name (e.g., `username:feature-branch`)
3. Click on the branch name to go to the fork repository
4. Follow the download steps above from the fork's branch

Alternatively, use the GitHub CLI to check out a pull request locally:

```bash title="Check out a pull request using GitHub CLI"
# Install GitHub CLI first: https://cli.github.com/
gh pr checkout 123
```

Or use Git to fetch and check out the pull request:

```bash title="Fetch and checkout a pull request using Git"
# Fetch the pull request (replace 123 with PR number)
git fetch origin pull/123/head:pr-123

# Checkout the pull request branch
git checkout pr-123
```

**Step 2: Determine PowerShell Module Path**

Open a PowerShell console and run the following command to find your PowerShell module paths:

**Windows**

```powershell title="View PowerShell module paths on Windows"
$env:PSModulePath -Split ';'
```

**macOS & Linux**

```powershell title="View PowerShell module paths on macOS & Linux"
$env:PSModulePath -Split ':'
```

!!! tip "Recommended Module Path"
    For user-specific installations, use the path containing your user profile:

    - **Windows**: `C:\Users\YourUsername\Documents\PowerShell\Modules` (PowerShell 7) or `C:\Users\YourUsername\Documents\WindowsPowerShell\Modules` (Windows PowerShell 5.1)
    - **macOS**: `~/.local/share/powershell/Modules`
    - **Linux**: `~/.local/share/powershell/Modules`

**Step 3: Extract and Install the Module**

**If you downloaded a ZIP file:**

1. Extract the ZIP file contents
2. Locate the module folder (it should contain a `.psd1` manifest file)
3. Copy the module folder to one of the paths from Step 2

**Windows Example:**

```powershell title="Install module from downloaded ZIP on Windows"
# Extract ZIP file (adjust paths as needed)
Expand-Archive -Path "C:\Downloads\AsBuiltReport.Vendor.Technology-dev.zip" -DestinationPath "C:\Temp"

# Copy module folder to PowerShell modules directory
Copy-Item -Path "C:\Temp\AsBuiltReport.Vendor.Technology-dev" -Destination "$HOME\Documents\PowerShell\Modules\AsBuiltReport.Vendor.Technology" -Recurse -Force
```

**macOS & Linux Example:**

```bash title="Install module from downloaded ZIP on macOS & Linux"
# Extract ZIP file (adjust paths as needed)
unzip ~/Downloads/AsBuiltReport.Vendor.Technology-dev.zip -d /tmp

# Copy module folder to PowerShell modules directory
cp -r /tmp/AsBuiltReport.Vendor.Technology-dev ~/.local/share/powershell/Modules/AsBuiltReport.Vendor.Technology
```

**If you cloned with Git:**

Simply copy or move the cloned repository folder to your PowerShell modules directory:

```powershell title="Install module from Git clone"
# Copy cloned repository to PowerShell modules directory
Copy-Item -Path "./AsBuiltReport.Vendor.Technology" -Destination "$HOME/.local/share/powershell/Modules/AsBuiltReport.Vendor.Technology" -Recurse -Force
```

**Step 4: Verify Installation**

Verify the module is installed correctly:

```powershell title="Verify module installation"
# List installed AsBuiltReport modules
Get-Module -Name 'AsBuiltReport.*' -ListAvailable

# Import the module to test
Import-Module -Name 'AsBuiltReport.Vendor.Technology' -Force
```

!!! warning "Module Version Conflicts"
    If you have the same module installed from the PowerShell Gallery, the version in `$env:PSModulePath` that appears first will take precedence. Use `Get-Module -Name Vendor.Technology -ListAvailable` to see all installed versions and their locations.

## Updating Modules

### Update from PowerShell Gallery

To update modules installed from the PowerShell Gallery:

```powershell title="Update AsBuiltReport modules"
# Update all AsBuiltReport modules
Update-Module -Name 'AsBuiltReport.*'

# Update a specific module
Update-Module -Name 'AsBuiltReport.VMware.vSphere'

# Check for available updates without installing
Find-Module -Name 'AsBuiltReport.*' | Select-Object Name, Version
Get-Module -Name 'AsBuiltReport.*' -ListAvailable | Select-Object Name, Version
```

!!! tip "Update Best Practices"
    - Always update AsBuiltReport.Core first before updating report modules
    - Review release notes before updating to check for breaking changes
    - Test updated modules in a non-production environment first

### Update from GitHub

For modules installed from GitHub, follow these steps:

1. Download the new version using the same method you used for installation ([GitHub Releases](#installing-from-github-releases) or [GitHub Branches](#installing-from-github-branches))
2. Remove the old version (see [Uninstalling Modules](#uninstalling-modules))
3. Install the new version following the installation steps

Alternatively, if you cloned with Git:

```bash title="Update module from Git"
# Navigate to the cloned repository
cd path/to/AsBuiltReport.Vendor.Technology

# Pull the latest changes
git pull origin main

# Or switch to a different branch
git fetch
git checkout branch-name
```

## Uninstalling Modules

### Uninstall from PowerShell Gallery

To remove modules installed from the PowerShell Gallery:

```powershell title="Uninstall AsBuiltReport modules"
# Uninstall a specific module
Uninstall-Module -Name 'AsBuiltReport.VMware.vSphere'

# Uninstall a specific version
Uninstall-Module -Name 'AsBuiltReport.VMware.vSphere' -RequiredVersion '1.2.0'

# Uninstall all versions
Uninstall-Module -Name 'AsBuiltReport.VMware.vSphere' -AllVersions

# Force uninstall (if module is in use)
Uninstall-Module -Name 'AsBuiltReport.VMware.vSphere' -Force
```

!!! warning "Uninstall Order"
    If you're uninstalling all AsBuiltReport modules, uninstall report modules first, then AsBuiltReport.Core last, since report modules depend on Core.

### Uninstall Manually Installed Modules

For modules installed manually (GitHub, offline):

1. Find the module location:

```powershell title="Find module installation path"
Get-Module -Name 'AsBuiltReport.Vendor.Technology' -ListAvailable | Select-Object Path
```

2. Delete the module folder:

**Windows:**

```powershell title="Remove module folder on Windows"
$modulePath = (Get-Module -Name 'AsBuiltReport.Vendor.Technology' -ListAvailable).ModuleBase
Remove-Item -Path $modulePath -Recurse -Force
```

**macOS & Linux:**

```bash title="Remove module folder on macOS & Linux"
rm -rf ~/.local/share/powershell/Modules/AsBuiltReport.Vendor.Technology
```

### Verify Removal

After uninstalling, verify the module is removed:

```powershell title="Verify module removal"
Get-Module -Name 'AsBuiltReport.Vendor.Technology' -ListAvailable
```

If the command returns no results, the module has been successfully removed.

## Troubleshooting

### Common Installation Issues

#### Cannot Install Modules - Execution Policy Error

```text title="Error Message"
File cannot be loaded because running scripts is disabled on this system.
```

**Solution:**
Set the execution policy for the current user (see [PowerShell Execution Policy](#powershell-execution-policy)):

```powershell title="Set execution policy"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Module Not Found After Installation

**Symptoms:**
- Module installed but not visible with `Get-Module -ListAvailable`
- Import-Module returns "module not found" error

**Solution:**

1. Verify the module is in the correct location:

    ```powershell title="Check module paths"
    $env:PSModulePath -Split ';'  # Windows
    $env:PSModulePath -Split ':'  # macOS/Linux
    ```

2. Ensure the module folder name matches the module name in the `.psd1` file

3. Refresh the module cache:

    ```powershell title="Refresh module cache"
    Get-Module -ListAvailable -Refresh
    ```

#### Module Import Fails - Dependency Error

```text title="Error Message"
The specified module 'AsBuiltReport.Core' was not loaded because no valid module file was found
```

**Solution:**
Install AsBuiltReport.Core first (see [Module Dependencies](#module-dependencies)):

```powershell title="Install AsBuiltReport.Core"
Install-Module -Name 'AsBuiltReport.Core' -Scope 'CurrentUser'
```

#### Cannot Connect to PowerShell Gallery

```text title="Error Message"
Unable to resolve package source 'https://www.powershellgallery.com/api/v2'
```

**Solutions:**

1. Check internet connectivity

2. Configure TLS 1.2:

    ```powershell title="Configure TLS 1.2"
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    ```

3. Use a proxy if required:

    ```powershell title="Install via proxy"
    Install-Module -Name 'AsBuiltReport.Core' -Proxy 'http://proxy.company.com:8080'
    ```

4. If PowerShell Gallery is blocked, use [GitHub Releases](#installing-from-github-releases) or [Offline Installation](#offline-installation)

#### Multiple Module Versions Conflict

**Symptoms:**
- Wrong version is loaded
- Unexpected behavior after installing new version

**Solution:**

1. List all installed versions:

    ```powershell title="List all module versions"
    Get-Module -Name 'AsBuiltReport.VMware.vSphere' -ListAvailable
    ```

2. Remove unwanted versions:

    ```powershell title="Remove specific module versions"
    # Remove specific version
    Uninstall-Module -Name 'AsBuiltReport.VMware.vSphere' -RequiredVersion '1.0.0'

    # Or remove all and reinstall
    Uninstall-Module -Name 'AsBuiltReport.VMware.vSphere' -AllVersions
    Install-Module -Name 'AsBuiltReport.VMware.vSphere'
    ```

3. Import specific version explicitly:

    ```powershell title="Import specific module version"
    Import-Module -Name 'AsBuiltReport.VMware.vSphere' -RequiredVersion '1.2.0'
    ```

#### Access Denied During Installation

```text title="Error Message"
Access to the path is denied
```

**Solutions:**

1. Install to CurrentUser scope instead of AllUsers:

    ```powershell title="Install to CurrentUser scope"
    Install-Module -Name 'AsBuiltReport.Core' -Scope 'CurrentUser'
    ```

2. If manually copying files, ensure you have write permissions to the target directory

3. Close any PowerShell sessions that might have the module loaded

#### Module Version Not Compatible

```text title="Error Message"
This module requires PowerShell version X.X
```

**Solution:**

1. Check your PowerShell version:

    ```powershell title="Check PowerShell version"
    $PSVersionTable.PSVersion
    ```

2. Install the required PowerShell version:
   - **PowerShell 7+**: Download from [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)
   - **Windows PowerShell 5.1**: Included with Windows 10/11, update older systems via Windows Management Framework

3. Check module-specific requirements in the [report module user guides](../user-guide/report-modules/overview.md)

### Getting Help

If you continue to experience issues:

1. Check the [FAQ](../support/faq.md) for additional guidance
2. Review [known issues](../support/known-issues.md)
3. Search existing GitHub Issues
4. Open a new issue with detailed error messages and PowerShell version information
5. Join the community [discussions](https://github.com/orgs/AsBuiltReport/discussions) on GitHub