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
Install-Module -Name 'VMware.PowerCLI' -Scope 'CurrentUser'
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

```powershell title=""
$env:PSModulePath -Split ';'
```

**macOS & Linux**

```powershell title=""
$env:PSModulePath -Split ':'
```

Copy the downloaded PowerShell module folders to a folder specified in the `$env:PSModulePath` output.