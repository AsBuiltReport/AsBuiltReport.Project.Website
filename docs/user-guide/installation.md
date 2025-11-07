Please follow these quick and simple instructions to install AsBuiltReport.

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

## Installing from GitHub Branch

To install a development version or specific branch from GitHub, follow these steps to download and install the code into your PowerShell module folder.

!!! warning "Development Code"
    Code downloaded from GitHub branches (especially development or feature branches) may be incomplete, untested, or in a non-working state. Only use this installation method if you need to test specific features or contribute to development. For production use, always install stable releases from the PowerShell Gallery.

!!! note "Report Module Naming"
    In the examples below, replace `AsBuiltReport.Vendor.Technology` with the report module name you wish to install (e.g. `AsBuiltReport.VMware.vSphere`, `AsBuiltReport.Microsoft.AD`).

### Step 1: Download the Branch

Navigate to the GitHub repository and download the desired branch as a ZIP file:

1. Go to the repository (e.g., `https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology`)
2. Click the **Code** button
3. Select the branch you want to download from the branch dropdown
4. Click **Download ZIP**

Alternatively, use Git to clone the specific branch:

```bash title="Clone specific branch using Git"
git clone -b branch-name https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology.git
```

### Step 2: Determine PowerShell Module Path

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

### Step 3: Extract and Install the Module

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

### Step 4: Verify Installation

Verify the module is installed correctly:

```powershell title="Verify module installation"
# List installed AsBuiltReport modules
Get-Module -Name 'AsBuiltReport.*' -ListAvailable

# Import the module to test
Import-Module -Name 'AsBuiltReport.Vendor.Technology' -Force
```

!!! warning "Module Version Conflicts"
    If you have the same module installed from the PowerShell Gallery, the version in `$env:PSModulePath` that appears first will take precedence. Use `Get-Module -Name Vendor.Technology -ListAvailable` to see all installed versions and their locations.