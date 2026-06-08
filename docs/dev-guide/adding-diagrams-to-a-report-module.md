---
title: Adding Diagrams to a Report Module
description: How to integrate AsBuiltReport.Diagram into report modules to add infrastructure topology diagrams using PSGraph and Graphviz
tags:
  - development
  - report-modules
  - diagrams
  - visualisation
  - powershell
  - graphviz
---

# Adding Diagrams to a Report Module

AsBuiltReport.Diagram is an optional PowerShell module that provides infrastructure diagram generation capabilities for AsBuiltReport report modules. It wraps the [PSGraph](https://github.com/KevinMarquette/PSGraph) module — a PowerShell DSL for [Graphviz](https://graphviz.org/) — and adds icon support, HTML node tables, subgraph containers, watermarks, themed styling, and direct integration with the PScribo document framework.

Diagrams are generated in memory as base64-encoded images and embedded into the report using PScribo's `Image` cmdlet. They can also be exported to disk as standalone files (PNG, SVG, PDF) alongside the report.

!!! info "Prerequisite Reading"
    This guide assumes you are already familiar with creating AsBuiltReport report modules. If not, read the [Creating a Report Module](creating-a-report-module.md) guide first.

## Prerequisites

### PSGraph

AsBuiltReport.Diagram requires the PSGraph module. Install it from the PowerShell Gallery:

```powershell title="Install PSGraph"
Install-Module -Name PSGraph -Scope CurrentUser
```

### Graphviz

On **Windows**, Graphviz is bundled with PSGraph and requires no separate installation. On **Linux** and **macOS**, install Graphviz using your package manager:

=== "Debian / Ubuntu"
    ```bash
    sudo apt install graphviz
    ```

=== "Fedora / RHEL / CentOS"
    ```bash
    sudo dnf install graphviz
    ```

=== "macOS (Homebrew)"
    ```bash
    brew install graphviz
    ```

=== "macOS (MacPorts)"
    ```bash
    sudo port install graphviz
    ```

### Icons

Diagrams typically use PNG icons to represent infrastructure components (servers, switches, storage, etc.). Icons are referenced by a hashtable that maps semantic names to filenames, and resolved from a directory you specify at diagram generation time. Icon images should be 100×150 pixels for consistent rendering.

## Installation

Install AsBuiltReport.Diagram from the PowerShell Gallery:

```powershell title="Install AsBuiltReport.Diagram"
Install-Module -Name AsBuiltReport.Diagram -Scope CurrentUser
```

## Declaring the Dependency

Add `AsBuiltReport.Diagram` to the `RequiredModules` array in your module manifest (`.psd1`):

```powershell title="Module manifest (.psd1) — RequiredModules"
RequiredModules = @(
    @{
        ModuleName    = 'AsBuiltReport.Core'
        ModuleVersion = '1.6.1'
    }
    @{
        ModuleName    = 'PSGraph'
        ModuleVersion = '2.1.38.27'
    }
    @{
        ModuleName    = 'AsBuiltReport.Diagram'
        ModuleVersion = '1.0.7'
    }
)
```

## JSON Configuration

Diagrams are controlled by `Options` keys in the report JSON configuration file rather than `InfoLevel`, since diagrams represent an optional capability rather than a depth-of-detail setting. Add the following keys to the `Options` section of your module's JSON template:

```json title="Report configuration JSON — Options for diagrams"
{
  "Options": {
    "EnableDiagrams": false,
    "ExportDiagrams": false,
    "ExportDiagramsFormat": ["pdf", "png"],
    "DiagramTheme": "White",
    "DiagramWaterMark": ""
  }
}
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `EnableDiagrams` | Boolean | `false` | Embed diagram images in the report |
| `ExportDiagrams` | Boolean | `false` | Export standalone diagram files alongside the report |
| `ExportDiagramsFormat` | Array | `["pdf", "png"]` | Standalone export formats: `pdf`, `png`, `svg`, `jpg` |
| `DiagramTheme` | String | `"White"` | Diagram colour theme: `White`, `Black`, or `Neon` |
| `DiagramWaterMark` | String | `""` | Optional watermark text (e.g. `"CONFIDENTIAL"`) |

## How Diagrams Are Embedded

Diagrams are generated with `-Format base64`, which returns the diagram as a base64-encoded string rather than writing a file to disk. This string is embedded into the report using PScribo's `Image` cmdlet.

The `Get-BestImageAspectRatio` function (provided by AsBuiltReport.Diagram) calculates the optimal width and height to fit the diagram within your target bounds while preserving the original aspect ratio.

```powershell title="Core diagram embedding pattern"
if ($Options.EnableDiagrams) {
    try {
        $Graph = Get-AbrVT[DiagramType] -Format base64
    } catch {
        Write-PScriboMessage -IsWarning "Diagram generation: $($_.Exception.Message)"
    }

    if ($Graph) {
        $BestAspectRatio = Get-BestImageAspectRatio -GraphObj $Graph -MaxWidth 600 -MaxHeight 600

        Section -Style Heading3 'Infrastructure Diagram' {
            Image -Base64 $Graph -Text 'Infrastructure Diagram' `
                  -Align Center `
                  -Width $BestAspectRatio.Width `
                  -Height $BestAspectRatio.Height
            PageBreak
        }
    }
}
```

!!! note
    `PageBreak` is called immediately after the `Image` cmdlet so the diagram occupies its own page in Word output. Omit `PageBreak` if you prefer the diagram to flow inline with surrounding content.

## Repository Structure for Diagrams

Diagram functions are kept in a dedicated subfolder under `Src/Private/` to separate diagram-generation code from report-section code:

```text title="Recommended folder structure for diagram files"
AsBuiltReport.Vendor.Technology/
└── Src/
    ├── Private/
    │   ├── Diagram/
    │   │   ├── Get-AbrVT[DiagramType].ps1      # Diagram orchestration function
    │   │   └── New-AbrVTDiagram.ps1             # PSGraph node/edge assembly
    │   └── Get-Abr[VendorAbbr][Resource].ps1   # Report section functions
    └── Public/
        └── Invoke-AsBuiltReport.Vendor.Technology.ps1
```

## Building a Diagram

### Icon Mapping

Diagrams use PNG icons to represent infrastructure components. Define a `$script:Images` hashtable that maps semantic names to icon filenames. The icon files must exist in the path passed to `New-AbrDiagram` via `-IconPath`.

```powershell title="Define the icon mapping hashtable"
$script:Images = @{
    'Main_Logo'    = 'AsBuiltReport.png'
    'Server'       = 'Server.png'
    'Database'     = 'Database.png'
    'Firewall'     = 'Firewall.png'
    'LoadBalancer' = 'LoadBalancer.png'
    'Storage'      = 'Storage.png'
}
```

Using `$script:` scope makes the hashtable available to all private diagram functions called from the main diagram assembly without passing it as a parameter.

### Graph Structure

PSGraph uses scriptblocks to define the diagram hierarchy. Node and edge default attributes — shape, font, colour — are declared once at the top of the `Graph {}` block and inherited by all nodes and edges unless overridden.

```powershell title="Graph with node and edge defaults"
$DiagramGraph = Graph -Name 'VendorTechnology' -Attributes @{
    pad        = 1.0
    rankdir    = 'TB'          # TB = top-to-bottom; LR = left-to-right
    splines    = 'polyline'
    penwidth   = 1.5
    fontname   = 'Segoe Ui Black'
    fontcolor  = '#565656'
    fontsize   = 32
    style      = 'dashed'
    labelloc   = 't'
    imagepath  = $IconPath
    nodesep    = 0.60
    ranksep    = 0.75
    bgcolor    = 'White'
} {
    # Default attributes for all nodes
    Node @{
        shape     = 'none'
        labelloc  = 't'
        style     = 'filled'
        fillColor = 'transparent'
        fontsize  = 14
        imagescale = $true
    }

    # Default attributes for all edges
    Edge @{
        style     = 'dashed'
        dir       = 'both'
        arrowtail = 'dot'
        color     = '#71797E'
        penwidth  = 2
        arrowsize = 1
    }

    SubGraph MainGraph -Attributes @{
        Label   = ''
        penwidth = 0
        bgcolor = 'transparent'
    } {
        # Nodes and edges go here
    }
}
```

### Adding Individual Nodes

Use `Add-NodeIcon` to create a node with an icon and optional metadata table beneath it. The returned label is then assigned to a PSGraph `Node` using `shape = 'plain'`.

```powershell title="Adding a node with an icon"
$ServerInfo = [PSCustomObject][ordered]@{
    'OS'      = 'Windows Server 2022'
    'Version' = '21H2'
    'IP'      = '192.168.1.10'
    'Role'    = 'Application Server'
}

$ServerLabel = Add-NodeIcon `
    -Name 'App-Server-01' `
    -IconType 'Server' `
    -AditionalInfo $ServerInfo `
    -ImagesObj $script:Images `
    -Align 'Center' `
    -FontSize 16 `
    -DraftMode:$DraftMode

Node -Name AppServer01 -Attributes @{
    Label     = $ServerLabel
    shape     = 'plain'
    fillColor = 'transparent'
    fontsize  = 14
}
```

The `-DraftMode` switch renders placeholder boxes instead of real icons during development, making it faster to iterate on layout without needing all icon files in place.

### Adding Server Farms and Collections

Use `Add-HtmlNodeTable` when you want to display a group of similar objects (e.g. a proxy server farm, a repository list) in a multi-column grid with a subgraph border around them.

```powershell title="Adding a server farm with Add-HtmlNodeTable"
$ProxyServers = @(
    @{
        Name           = 'proxy-01.example.com'
        AdditionalInfo = [PSCustomObject][ordered]@{
            'OS'   = 'Windows Server 2022'
            'Mode' = 'Automatic'
            'IP'   = '192.168.1.20'
        }
    },
    @{
        Name           = 'proxy-02.example.com'
        AdditionalInfo = [PSCustomObject][ordered]@{
            'OS'   = 'Windows Server 2022'
            'Mode' = 'Manual'
            'IP'   = '192.168.1.21'
        }
    }
)

Add-HtmlNodeTable `
    -Name 'ProxyFarm' `
    -ImagesObj $script:Images `
    -InputObject $ProxyServers.Name `
    -IconType 'Server' `
    -ColumnSize 3 `
    -AditionalInfo $ProxyServers.AdditionalInfo `
    -Subgraph `
    -SubgraphLabel 'Proxy Servers' `
    -SubgraphLabelPos 'top' `
    -SubgraphTableStyle 'dashed,rounded' `
    -TableBorderColor '#71797E' `
    -TableBorder '1' `
    -SubgraphLabelFontSize 18 `
    -FontSize 14 `
    -FontBold `
    -SubgraphFontBold `
    -DraftMode:$DraftMode `
    -NodeObject
```

### Connecting Nodes

Use `Add-NodeEdge` to draw labelled connections between nodes:

```powershell title="Connecting nodes with Add-NodeEdge"
Add-NodeEdge `
    -From 'AppServer01' `
    -To 'ProxyFarm' `
    -EdgeLabel 'HTTPS' `
    -EdgeColor '#71797E' `
    -EdgeLabelFontSize 12 `
    -EdgeLabelFontColor '#565656'
```

### Controlling Layout

Use `Rank` to force nodes onto the same horizontal level:

```powershell title="Aligning nodes to the same rank"
# Force all proxy nodes to render at the same vertical position
Rank 'proxy-01.example.com', 'proxy-02.example.com', 'proxy-03.example.com'
```

### Grouping with SubGraph

Use `SubGraph` to draw a labelled border around a logical group of nodes:

```powershell title="Grouping nodes in a SubGraph"
SubGraph 'DataTier' -Attributes @{
    Label    = 'Database Tier'
    fontsize = 18
    penwidth = 1.5
    labelloc = 't'
    style    = 'dashed,rounded'
    color    = '#71797E'
} {
    # Nodes inside this group
    Node -Name DbPrimary -Attributes @{ Label = $DbPrimaryLabel; shape = 'plain' }
    Node -Name DbReplica -Attributes @{ Label = $DbReplicaLabel; shape = 'plain' }
    Rank 'DbPrimary', 'DbReplica'
}
```

## Generating the Diagram

Once the PSGraph structure is assembled, pass it to `New-AbrDiagram` to render the output:

```powershell title="Calling New-AbrDiagram"
New-AbrDiagram `
    -InputObject $DiagramGraph `
    -OutputFolderPath $OutputFolderPath `
    -Filename 'VendorTechnology-Infrastructure' `
    -Format @('base64') `
    -MainDiagramLabel 'Vendor Technology Infrastructure' `
    -IconPath $IconPath `
    -ImagesObj $script:Images `
    -LogoName 'Main_Logo' `
    -Direction 'top-to-bottom' `
    -MainGraphBGColor $MainGraphBGColor `
    -Fontcolor $Fontcolor `
    -Fontname 'Segoe Ui Black'
```

To also export standalone files alongside the base64 output, pass additional formats:

```powershell title="Generating base64 and standalone export files"
New-AbrDiagram `
    -InputObject $DiagramGraph `
    -OutputFolderPath $OutputFolderPath `
    -Filename 'VendorTechnology-Infrastructure' `
    -Format @('base64', 'pdf', 'png') `
    -MainDiagramLabel 'Vendor Technology Infrastructure' `
    -IconPath $IconPath `
    -ImagesObj $script:Images `
    -LogoName 'Main_Logo'
```

## Diagram Themes

AsBuiltReport.Diagram supports three built-in colour themes. Apply a theme by setting colours based on `$Options.DiagramTheme` before building the graph:

```powershell title="Applying a diagram theme"
switch ($Options.DiagramTheme) {
    'Black' {
        $MainGraphBGColor = 'Black'
        $TableBorderColor = 'White'
        $Edgecolor        = 'White'
        $Fontcolor        = 'White'
        $NodeFontcolor    = 'White'
    }
    'Neon' {
        $MainGraphBGColor = 'grey14'
        $TableBorderColor = 'gold2'
        $Edgecolor        = 'gold2'
        $Fontcolor        = 'gold2'
        $NodeFontcolor    = 'gold2'
    }
    default {
        $MainGraphBGColor = 'White'
        $TableBorderColor = '#71797E'
        $Edgecolor        = '#71797E'
        $Fontcolor        = '#565656'
        $NodeFontcolor    = '#565656'
    }
}
```

## Watermarks and Signatures

`New-AbrDiagram` supports optional watermarks and footer signatures:

```powershell title="Watermark and signature parameters"
New-AbrDiagram `
    -InputObject $DiagramGraph `
    -Format @('png') `
    -OutputFolderPath $OutputFolderPath `
    # Watermark
    -WaterMarkText $Options.DiagramWaterMark `
    -WaterMarkColor 'Gray' `
    -WaterMarkFontOpacity 0.3 `
    # Footer signature
    -Signature `
    -AuthorName 'Tim Carman' `
    -CompanyName 'Contoso'
```

## Complete Private Function Example

The following shows a complete diagram orchestration function that collects infrastructure data, assembles the PSGraph structure, generates the diagram, and returns a base64 string for embedding in the report.

```powershell title="Src/Private/Diagram/Get-AbrVTInfrastructureDiagram.ps1"
function Get-AbrVTInfrastructureDiagram {
    <#
    .SYNOPSIS
        Used by As Built Report to generate a Vendor Technology infrastructure diagram.
    .DESCRIPTION
        Documents the configuration of Vendor Technology in Word/HTML/Text formats using PScribo.
    .NOTES
        Version:    0.1.0
        Author:     Your Name
    .LINK
        https://github.com/AsBuiltReport/AsBuiltReport.Vendor.Technology
    #>
    [CmdletBinding()]
    param (
        [ValidateSet('pdf', 'svg', 'png', 'base64', 'jpg')]
        [string] $Format = 'base64',

        [ValidateSet('top-to-bottom', 'left-to-right')]
        [string] $Direction = 'top-to-bottom',

        [bool] $DraftMode = $false
    )

    begin {
        Write-PScriboMessage "Collecting data for infrastructure diagram."

        # Map semantic icon names to PNG filenames in your module's icons folder
        $script:Images = @{
            'Main_Logo'    = 'AsBuiltReport.png'
            'AppServer'    = 'Server.png'
            'Database'     = 'Database.png'
            'LoadBalancer' = 'LoadBalancer.png'
        }

        # Icon files are stored under the module's root in an Icons/ folder
        $IconPath = Join-Path -Path (Split-Path $PSScriptRoot -Parent) -ChildPath 'Icons'

        # Resolve layout direction to Graphviz rankdir value
        $Dir = switch ($Direction) {
            'top-to-bottom' { 'TB' }
            'left-to-right' { 'LR' }
        }

        # Apply theme colours
        switch ($Options.DiagramTheme) {
            'Black' {
                $MainGraphBGColor = 'Black'
                $Edgecolor        = 'White'
                $Fontcolor        = 'White'
            }
            'Neon' {
                $MainGraphBGColor = 'grey14'
                $Edgecolor        = 'gold2'
                $Fontcolor        = 'gold2'
            }
            default {
                $MainGraphBGColor = 'White'
                $Edgecolor        = '#71797E'
                $Fontcolor        = '#565656'
            }
        }
    }

    process {
        try {
            # Collect data from the target system
            $AppServers    = Get-VTApplicationServer -ErrorAction Stop
            $Databases     = Get-VTDatabase -ErrorAction Stop
            $LoadBalancers = Get-VTLoadBalancer -ErrorAction Stop

            if (-not ($AppServers -or $Databases -or $LoadBalancers)) {
                Write-PScriboMessage -IsWarning "No infrastructure data available for diagram."
                return
            }

            # Assemble the PSGraph structure
            $DiagramGraph = Graph -Name 'VendorTechnology' -Attributes @{
                pad       = 1.0
                rankdir   = $Dir
                splines   = 'polyline'
                penwidth  = 1.5
                fontname  = 'Segoe Ui Black'
                fontcolor = $Fontcolor
                fontsize  = 32
                style     = 'dashed'
                labelloc  = 't'
                imagepath = $IconPath
                nodesep   = 0.60
                ranksep   = 0.75
                bgcolor   = $MainGraphBGColor
            } {
                Node @{
                    shape      = 'none'
                    labelloc   = 't'
                    style      = 'filled'
                    fillColor  = 'transparent'
                    fontsize   = 14
                    imagescale = $true
                }

                Edge @{
                    style     = 'dashed'
                    dir       = 'both'
                    arrowtail = 'dot'
                    color     = $Edgecolor
                    penwidth  = 2
                    arrowsize = 1
                    fontcolor = $Edgecolor
                }

                SubGraph MainGraph -Attributes @{Label = ''; penwidth = 0; bgcolor = 'transparent'} {

                    # Load balancer nodes
                    foreach ($LB in $LoadBalancers) {
                        $LBInfo = [PSCustomObject][ordered]@{
                            'IP'        = $LB.IPAddress
                            'Algorithm' = $LB.Algorithm
                        }
                        $LBLabel = Add-NodeIcon `
                            -Name $LB.Name `
                            -IconType 'LoadBalancer' `
                            -AditionalInfo $LBInfo `
                            -ImagesObj $script:Images `
                            -Align 'Center' `
                            -FontSize 14 `
                            -DraftMode:$DraftMode

                        Node -Name ($LB.Name -replace '[^a-zA-Z0-9]', '') -Attributes @{
                            Label     = $LBLabel
                            shape     = 'plain'
                            fillColor = 'transparent'
                        }
                    }

                    # Application server farm
                    if ($AppServers) {
                        $AppServerTable = $AppServers | ForEach-Object {
                            @{
                                Name           = $_.Name
                                AdditionalInfo = [PSCustomObject][ordered]@{
                                    'OS'   = $_.OperatingSystem
                                    'IP'   = $_.IPAddress
                                    'Role' = $_.Role
                                }
                            }
                        }

                        Add-HtmlNodeTable `
                            -Name 'AppServerFarm' `
                            -ImagesObj $script:Images `
                            -InputObject $AppServerTable.Name `
                            -IconType 'AppServer' `
                            -ColumnSize 3 `
                            -AditionalInfo $AppServerTable.AdditionalInfo `
                            -Subgraph `
                            -SubgraphLabel 'Application Servers' `
                            -SubgraphLabelPos 'top' `
                            -SubgraphTableStyle 'dashed,rounded' `
                            -TableBorderColor $Edgecolor `
                            -TableBorder '1' `
                            -SubgraphLabelFontSize 18 `
                            -FontSize 14 `
                            -FontBold `
                            -SubgraphFontBold `
                            -DraftMode:$DraftMode `
                            -NodeObject
                    }

                    # Database nodes
                    foreach ($DB in $Databases) {
                        $DBInfo = [PSCustomObject][ordered]@{
                            'Engine'  = $DB.Engine
                            'Version' = $DB.Version
                            'IP'      = $DB.IPAddress
                        }
                        $DBLabel = Add-NodeIcon `
                            -Name $DB.Name `
                            -IconType 'Database' `
                            -AditionalInfo $DBInfo `
                            -ImagesObj $script:Images `
                            -Align 'Center' `
                            -FontSize 14 `
                            -DraftMode:$DraftMode

                        Node -Name ($DB.Name -replace '[^a-zA-Z0-9]', '') -Attributes @{
                            Label     = $DBLabel
                            shape     = 'plain'
                            fillColor = 'transparent'
                        }
                    }

                    # Edges: load balancer → app servers → databases
                    foreach ($LB in $LoadBalancers) {
                        $LBNodeName = $LB.Name -replace '[^a-zA-Z0-9]', ''
                        Add-NodeEdge -From $LBNodeName -To 'AppServerFarm' -EdgeLabel 'HTTP/S'
                    }
                    foreach ($DB in $Databases) {
                        $DBNodeName = $DB.Name -replace '[^a-zA-Z0-9]', ''
                        Add-NodeEdge -From 'AppServerFarm' -To $DBNodeName -EdgeLabel 'SQL'
                    }
                }
            }

            # Determine output formats: always include base64 for report embedding;
            # add export formats if ExportDiagrams is enabled
            $Formats = @($Format)
            if ($Options.ExportDiagrams -and $script:OutputFolderPath) {
                $Formats += $Options.ExportDiagramsFormat
            }

            $DiagramResult = New-AbrDiagram `
                -InputObject $DiagramGraph `
                -Format $Formats `
                -OutputFolderPath $script:OutputFolderPath `
                -Filename 'VendorTechnology-Infrastructure' `
                -MainDiagramLabel 'Vendor Technology — Infrastructure' `
                -IconPath $IconPath `
                -ImagesObj $script:Images `
                -LogoName 'Main_Logo' `
                -WaterMarkText $Options.DiagramWaterMark

            # Return only the base64 portion for PScribo embedding
            return ($DiagramResult | Where-Object { $_ -match '^[A-Za-z0-9+/=]+$' })

        } catch {
            Write-PScriboMessage -IsWarning "Infrastructure Diagram: $($_.Exception.Message)"
        }
    }
    end {}
}
```

### Calling the diagram function from Invoke-AsBuiltReport

In your main `Invoke-AsBuiltReport.*` function, call the diagram function and embed the result immediately before the main report sections:

```powershell title="Embedding a diagram in the main report function"
foreach ($System in $Target) {
    try {
        $script:Connection = Connect-VendorSystem -Server $System -Credential $Credential -ErrorAction Stop
        $script:OutputFolderPath = $OutputFolderPath

        Section -Style Heading1 $System {

            # Diagram section (before all data sections)
            if ($Options.EnableDiagrams) {
                try {
                    $Graph = Get-AbrVTInfrastructureDiagram -Format base64 -Direction $Options.DiagramDirection
                } catch {
                    Write-PScriboMessage -IsWarning "Infrastructure Diagram: $($_.Exception.Message)"
                }

                if ($Graph) {
                    $BestAspectRatio = Get-BestImageAspectRatio -GraphObj $Graph -MaxWidth 600 -MaxHeight 600

                    Section -Style Heading2 'Infrastructure Diagram' {
                        Image -Base64 $Graph `
                              -Text 'Vendor Technology Infrastructure Diagram' `
                              -Align Center `
                              -Width $BestAspectRatio.Width `
                              -Height $BestAspectRatio.Height
                        PageBreak
                    }
                }
            }

            # Data sections follow
            Get-AbrVTApplicationServer
            Get-AbrVTDatabase
            Get-AbrVTNetwork
        }
    } catch {
        Write-PScriboMessage -IsWarning ($LocalizedData.ConnectionError -f $System, $_.Exception.Message)
    }
}
```

## Standalone Diagram Export

If your module includes multiple diagram types, consider exporting a public `Export-AsBuiltReport[VendorTechnology]Diagram` function that allows users to generate diagrams without running a full report:

```powershell title="Src/Public/Export-AsBuiltReportVTDiagram.ps1"
function Export-AsBuiltReportVTDiagram {
    <#
    .SYNOPSIS
        Exports Vendor Technology infrastructure diagrams without generating a full report.
    .EXAMPLE
        Export-AsBuiltReportVTDiagram -Target 'server01.example.com' -Credential $cred `
            -DiagramType 'Infrastructure' -Format 'pdf','svg' -OutputFolderPath 'C:\Diagrams'
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [String[]] $Target,

        [Parameter(Mandatory = $true)]
        [PSCredential] $Credential,

        [ValidateSet('Infrastructure', 'Network', 'Storage')]
        [String[]] $DiagramType = 'Infrastructure',

        [ValidateSet('pdf', 'svg', 'png', 'jpg')]
        [String[]] $Format = @('pdf', 'png'),

        [String] $OutputFolderPath = (Get-Location).Path,

        [ValidateSet('White', 'Black', 'Neon')]
        [String] $DiagramTheme = 'White',

        [Switch] $Signature,
        [String] $AuthorName,
        [String] $CompanyName
    )

    foreach ($System in $Target) {
        try {
            $script:Connection = Connect-VendorSystem -Server $System -Credential $Credential -ErrorAction Stop

            # Build a minimal $Options object so the diagram functions can read it
            $script:Options = [PSCustomObject]@{
                EnableDiagrams        = $true
                ExportDiagrams        = $true
                ExportDiagramsFormat  = $Format
                DiagramTheme          = $DiagramTheme
                DiagramWaterMark      = ''
            }
            $script:OutputFolderPath = $OutputFolderPath

            foreach ($Type in $DiagramType) {
                switch ($Type) {
                    'Infrastructure' { Get-AbrVTInfrastructureDiagram -Format $Format -Direction 'top-to-bottom' }
                    'Network'        { Get-AbrVTNetworkDiagram -Format $Format }
                    'Storage'        { Get-AbrVTStorageDiagram -Format $Format }
                }
            }
        } catch {
            Write-Error "Failed to connect to $System : $($_.Exception.Message)"
        } finally {
            Disconnect-VendorSystem -Connection $script:Connection -Confirm:$false -ErrorAction SilentlyContinue
        }
    }
}
```

## Localising Diagram Section Titles

Store diagram section headings and `Image` alt-text in your module's language file alongside other translated strings:

```powershell title="Language file entries for diagram sections (en-US)"
InvokeAsBuiltReportVendorTechnology = ConvertFrom-StringData @'
    Connecting                    = Connecting to {0}.
    ConnectionError               = Failed to connect to {0}: {1}
    InfrastructureDiagram         = Infrastructure Diagram
    InfrastructureDiagramAltText  = Vendor Technology infrastructure topology diagram
    NetworkDiagram                = Network Diagram
    NetworkDiagramAltText         = Vendor Technology network topology diagram
'@
```

```powershell title="Using $LocalizedData for diagram section titles"
if ($Options.EnableDiagrams -and $Graph) {
    Section -Style Heading2 $LocalizedData.InfrastructureDiagram {
        Image -Base64 $Graph `
              -Text $LocalizedData.InfrastructureDiagramAltText `
              -Align Center `
              -Width $BestAspectRatio.Width `
              -Height $BestAspectRatio.Height
        PageBreak
    }
}
```

## Common Parameters Reference

### New-AbrDiagram

| Parameter | Type | Description |
|-----------|------|-------------|
| `-InputObject` | PSGraph object | The assembled `Graph {}` scriptblock result |
| `-Format` | String[] | Output formats: `pdf`, `svg`, `png`, `jpg`, `dot`, `base64` |
| `-OutputFolderPath` | DirectoryInfo | Folder for file-based output formats |
| `-Filename` | String | Base filename (without extension) |
| `-MainDiagramLabel` | String | Title displayed at the top of the diagram |
| `-IconPath` | String | Directory containing icon PNG files |
| `-ImagesObj` | Hashtable | Maps icon names to filenames in `-IconPath` |
| `-LogoName` | String | Key from `-ImagesObj` to use as the header logo |
| `-Direction` | String | `top-to-bottom` or `left-to-right` |
| `-MainGraphBGColor` | String | Background colour (named or hex) |
| `-Fontcolor` | String | Default font colour |
| `-Fontname` | String | Font family (e.g. `Segoe Ui Black`) |
| `-WaterMarkText` | String | Watermark text |
| `-WaterMarkColor` | String | Watermark colour |
| `-WaterMarkFontOpacity` | Double | Watermark opacity (0.0–1.0) |
| `-Signature` | Switch | Add footer signature |
| `-AuthorName` | String | Signature author name |
| `-CompanyName` | String | Signature company name |
| `-DraftMode` | Switch | Render placeholder boxes instead of icons |

### Add-NodeIcon

| Parameter | Type | Description |
|-----------|------|-------------|
| `-Name` | String | Display label for the node |
| `-IconType` | String | Key from `-ImagesObj` for the icon |
| `-ImagesObj` | Hashtable | Icon name-to-filename mapping |
| `-AditionalInfo` | PSCustomObject | Properties to display below the icon |
| `-Align` | String | Text alignment: `Left`, `Center`, `Right` |
| `-FontSize` | Int | Label font size |
| `-DraftMode` | Switch | Render placeholder instead of icon |

### Add-HtmlNodeTable

| Parameter | Type | Description |
|-----------|------|-------------|
| `-Name` | String | Internal node name |
| `-ImagesObj` | Hashtable | Icon name-to-filename mapping |
| `-InputObject` | String[] | Node display names |
| `-IconType` | String | Icon key for all nodes (or array for `-MultiIcon`) |
| `-ColumnSize` | Int | Number of columns in the node grid |
| `-AditionalInfo` | PSCustomObject[] | Per-node property objects |
| `-Subgraph` | Switch | Wrap nodes in a labelled border |
| `-SubgraphLabel` | String | Subgraph border title |
| `-SubgraphTableStyle` | String | Border style: `dashed,rounded`, `solid,rounded` |
| `-MultiIcon` | Switch | Allow different icon types per node |
| `-NodeObject` | Switch | Return the node object for use in edges |
| `-DraftMode` | Switch | Render placeholders instead of icons |

### Add-NodeEdge

| Parameter | Type | Description |
|-----------|------|-------------|
| `-From` | String | Source node name |
| `-To` | String | Target node name |
| `-EdgeLabel` | String | Label displayed on the connection |
| `-EdgeColor` | String | Line colour |
| `-EdgeLabelFontSize` | Int | Label font size |
| `-EdgeLabelFontColor` | String | Label font colour |
| `-EdgeStyle` | String | Line style: `dashed`, `solid` |
| `-EdgeThickness` | Int | Line width |
| `-Arrowhead` | String | Arrowhead style: `normal`, `none` |

### Get-BestImageAspectRatio

| Parameter | Type | Description |
|-----------|------|-------------|
| `-GraphObj` | String | The base64 diagram string |
| `-MaxWidth` | Int | Maximum width in pixels |
| `-MaxHeight` | Int | Maximum height in pixels |

Returns a hashtable with `Width` and `Height` keys containing the optimal dimensions.

## Summary of Best Practices

- **Separate diagram code from report code** — place diagram functions in `Src/Private/Diagram/` so they are easy to locate and test independently.
- **Guard with `$Options.EnableDiagrams`** — diagrams depend on Graphviz and are slow to generate; always make them opt-in.
- **Always use `-Format base64` for report embedding** — pass additional format strings to `-Format` when `-ExportDiagrams` is enabled, rather than making two separate calls.
- **Use `Get-BestImageAspectRatio`** — pass the base64 string through this function before `Image` so the diagram scales correctly in both HTML and Word output.
- **Call `PageBreak` after `Image`** — this ensures the diagram occupies its own page in Word documents and does not push headings or tables off the page.
- **Use `$script:` scope for `$Images` and `$Connection`** — this avoids passing large objects as parameters through multiple private function calls.
- **Sanitise node names** — Graphviz node names must not contain special characters; use `-replace '[^a-zA-Z0-9]', ''` on any strings used as node identifiers.
- **Use `DraftMode` during development** — set `-DraftMode:$true` to render placeholder boxes while building layout, then switch to real icons when the structure is finalised.
- **Apply themes consistently** — read `$Options.DiagramTheme` once in the `begin{}` block and store the resolved colours in variables used throughout the graph assembly.
- **Localise section titles and alt-text** — store diagram heading strings and `Image` alt-text in your language file alongside other translatable strings.
