---
title: Creating a Report Style
description: Create custom style scripts using PScribo to match your corporate identity and branding
tags:
  - development
  - styling
  - customisation
  - pscribo
  - branding
  - themes
---

# Creating a Report Style

When generating an AsBuiltReport, its formatting and style is defined using a PowerShell (.ps1) script which utilises a set of [PScribo](../support/faq.md#what-is-pscribo) cmdlets.

This guide can be used to create custom style scripts which match your individual and/or corporate identities.

!!! info

    This guide assumes you have already [installed](../user-guide/installation.md) an AsBuiltReport module.

    Most of the information contained within this guide has been sourced from the official PScribo documentation.

!!! tip

    Use the [default style script](https://github.com/AsBuiltReport/AsBuiltReport.Core/blob/master/AsBuiltReport.Core.Style.ps1){:target="_blank"} as a reference for creating a new style script.

### Language Support

To support report language translations in AsBuiltReport v1.5.0 or higher, ensure the following code is added to the top of your style scripts.

```powershell title="Initialize language support in style scripts"
try {
    # Try to initialize localized data for style elements
    # Use the report language from parent scope if available, otherwise fallback to OS language
    if ($PSScriptRoot) {
        if ($FinalReportLanguage) {
            Initialize-LocalizedData -ModuleBasePath $PSScriptRoot -LanguageFile <StyleScriptName> -ModuleType 'Core' -Language $FinalReportLanguage
        } else {
            Initialize-LocalizedData -ModuleBasePath $PSScriptRoot -LanguageFile <StyleScriptName> -ModuleType 'Core'
        }
    } else {
        # Fallback if $PSScriptRoot is not available
        $StyleModulePath = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
        if ($FinalReportLanguage) {
            Initialize-LocalizedData -ModuleBasePath $StyleModulePath -LanguageFile <StyleScriptName> -ModuleType 'Core' -Language $FinalReportLanguage
        } else {
            Initialize-LocalizedData -ModuleBasePath $StyleModulePath -LanguageFile <StyleScriptName> -ModuleType 'Core'
        }
    }
} catch {
    # If localization fails, continue with default style (don't break report generation)
    Write-Warning "Could not load style localization: $($_.Exception.Message)"
}
```

### Global Document Options

The `DocumentOption` cmdlet is used to set global document options, including default font, page size, margins and orientation.

`EnableSectionNumbering` enables automatic numbering of document sections.

`PageSize` sets the page size. Available options include A4, Letter and Legal.

`DefaultFont` sets the default font. It is highly recommended to use a standard, [web-safe](https://www.w3schools.com/cssref/css_websafe_fonts.asp){:target="_blank"} font.

`MarginLeftAndRight` sets the left and right page margins to the points (pt) specified.

`MarginTopAndBottom` sets the top and bottom page margins to the points (pt) specified.

`Orientation` sets the document's default page orientation. It is highly recommended that you do not modify the `$Orientation` parameter value.

```powershell title="Additional information about DocumentOption"
get-help about_PScriboDocument
```

```powershell title="DocumentOption examples"
# Default DocumentOption
DocumentOption -EnableSectionNumbering -PageSize 'A4' -DefaultFont 'Arial' -MarginLeftAndRight 71 -MarginTopAndBottom 71 -Orientation $Orientation

# Custom DocumentOption
# Disable automatic section numbering. Set page size to Letter. Set default font to Tahoma. Set custom page margins.
DocumentOption -PageSize 'Letter' -DefaultFont 'Tahoma' -MarginLeftAndRight 74 -MarginTopAndBottom 65 -Orientation $Orientation
```


### Styles
The `Style` cmdlet defines a custom formatting style which can be applied to section headings, paragraphs and within table styles. Styles need to be defined before any formatting can be applied within a document (with the exception of paragraphs). Each style permits the setting of the font to use, the font size and colour.

```powershell title="Additional information about Styles"
get-help about_PScriboStyles
```


#### Default Styles
A style script uses a standard set of styles for a report. These styles are defined below and must be included in every style script.

```text title="Default style names and descriptions"
## Title & Heading Styles
Normal              - Default text style
Title               - Cover Page Title text style
Title 2             - Cover Page Subtitle 1 text style
Title 3             - Cover Page Subtitle 2 text style
TOC                 - Section heading Table of Contents text style
Heading 1           - Section heading level 1 text style
Heading 2           - Section heading level 2 text style
Heading 3           - Section heading level 3 text style
Heading 4           - Section heading level 4 text style
NO TOC Heading 4    - Section heading level 4 text style - Exclude From TOC
Heading 5           - Section heading level 5 text style
NO TOC Heading 5    - Section heading level 5 text style - Exclude From TOC
Heading 6           - Section heading level 6 text style
NO TOC Heading 6    - Section heading level 6 text style - Exclude From TOC
NO TOC Heading 7    - Section heading level 7 text style - Exclude From TOC

## Header & Footer Styles
Header              - Document header style
Footer              - Document footer style

## Table Heading & Row Styles
TableDefaultHeading - Table heading row style
TableDefaultRow     - Table row style
TableDefaultAltRow  - Table alternating row style

# Table Caption Style
Caption             - Table caption style

## Table Row/Cell Highlight Styles
Critical            - Table row/cell highlight style for critical alerts
Warning             - Table row/cell highlight style for warning alerts
Info                - Table row/cell highlight style for informational alerts
OK                  - Table row/cell highlight style for known good alerts
```

#### Custom Styles

Using the default style names, these styles can be customised to suit your individual requirements.

Font, Size, Color and Text alignment are just some of the style properties which can be customised to tailor a report to your liking.

Additional styles can also be defined for use in custom defined sections, paragraphs and tables.

```powershell title="Custom Style Definitions Example"
# Heading & Font Styles Formatting
Style -Name 'Title' -Size 24 -Color '072E58' -Align Center
Style -Name 'Title 2' -Size 18 -Color '204369' -Align Center
Style -Name 'Title 3' -Size 12 -Color '395879' -Align Left
Style -Name 'Heading 1' -Size 16 -Color '072E58'
Style -Name 'Heading 2' -Size 14 -Color '204369'
Style -Name 'Heading 3' -Size 13 -Color '395879'
Style -Name 'Heading 4' -Size 12 -Color '958026'
Style -Name 'NO TOC Heading 4' -Size 12 -Color '958026'
Style -Name 'Heading 5' -Size 11 -Color '009684'
Style -Name 'NO TOC Heading 5' -Size 11 -Color '009684'
Style -Name 'Heading 6' -Size 10 -Color '009683'
Style -Name 'NO TOC Heading 6' -Size 10 -Color '009683'
Style -Name 'NO TOC Heading 7' -Size 10 -Color '00EBCD' -Italic
Style -Name 'Normal' -Size 10 -Color '565656' -Default

# Header & Footer Formatting
Style -Name 'Header' -Size 10 -Color '565656' -Align Center
Style -Name 'Footer' -Size 10 -Color '565656' -Align Center

# Table of Contents Formatting
Style -Name 'TOC' -Size 16 -Color '072E58'

# Table Heading & Row Formatting
Style -Name 'TableDefaultHeading' -Size 10 -Color 'FAFAFA' -BackgroundColor '072E58'
Style -Name 'TableDefaultRow' -Size 10 -Color '565656'
Style -Name 'TableDefaultAltRow' -Size 10 -Color '000000' -BackgroundColor 'EAEAE6'

# Table Row/Cell Highlight Formatting
Style -Name 'Critical' -Size 10 -Color '565656' -BackgroundColor 'FEDDD7'
Style -Name 'Warning' -Size 10 -Color '565656' -BackgroundColor 'FFF4C7'
Style -Name 'Info' -Size 10 -Color '565656' -BackgroundColor 'E3F5FC'
Style -Name 'OK' -Size 10 -Color '565656' -BackgroundColor 'DFF0D0'

# Table Caption Formatting
Style -Name 'Caption' -Size 10 -Color '072E58' -Italic -Align Left
```

### Table Styles
The `TableStyle` cmdlet defines a custom formatting style for tables that is comprised of a heading, row and alternate row styles.

Table styles are a combination of individual styles with some additional formatting options specific to tables, i.e. borders and padding. A table style can specify a style for the heading row, a default row style and an optional alternating row style. The individual styles used by within a table style must first be defined with the `Style` cmdlet before they can be used within `TableStyle`.

Just like individual document styles, it is possible to create your own custom table styles, override the built-in style and set a different table style as the "default".

```powershell title="Table Style Definitions"
# Define Default Table Style Properties
$TableDefaultProperties = @{
    Id = 'TableDefault'
    HeaderStyle = 'TableDefaultHeading'
    RowStyle = 'TableDefaultRow'
    BorderColor = '072E58'
    Align = 'Left'
    CaptionStyle = 'Caption'
    CaptionLocation = 'Below'
    BorderWidth = 0.25
    PaddingTop = 1
    PaddingBottom = 1.5
    PaddingLeft = 2
    PaddingRight = 2
}

# Set Default Table Styles
TableStyle @TableDefaultProperties -Default
# Create a Table without a border
TableStyle -Id 'Borderless' -HeaderStyle Normal -RowStyle Normal -BorderWidth 0
```

#### Table of Contents
The `TOC` cmdlet creates a 'Table of Contents' from the document's section headings.

Each report will include a JSON configuration file which provides an option to enable/disable the Table of Contents.

```json title="Show Table of Contents Option" hl_lines="7"
{
    "Report": {
        "Name": "VMware vSphere As Built Report",
        "Version": "1.0",
        "Status": "Released",
        "Language": "en-US",
        "ShowCoverPageImage": true,
        "ShowTableOfContents": true,
        "ShowHeaderFooter": true,
        "ShowTableCaptions": true
    }
}
```

Should you wish to include an option for a Table of Contents within your style script, ensure you add the following code to the end of your script.

```powershell title="Add Table of Contents to style script"
# Set TOC, if enabled in report JSON configuration
if ($ReportConfig.Report.ShowTableOfContents) {
    # Add Table of Contents
    TOC -Name 'Table of Contents'
    PageBreak
}
```

#### Table Captions

Each report will include a JSON configuration file which provides an option to enable/disable table captions.

Ensure you configure `CaptionStyle` and `CaptionLocation` in your table properties.

```json title="Show Table Caption Option" hl_lines="9"
{
    "Report": {
        "Name": "VMware vSphere As Built Report",
        "Version": "1.0",
        "Status": "Released",
        "ShowCoverPageImage": true,
        "ShowTableOfContents": true,
        "ShowHeaderFooter": true,
        "ShowTableCaptions": true
    }
}
```

```powershell title="Caption Style & Location Definitions" hl_lines="8 9"
# Define default Table Style properties
$TableDefaultProperties = @{
    Id = 'TableDefault'
    HeaderStyle = 'TableDefaultHeading'
    RowStyle = 'TableDefaultRow'
    BorderColor = '072E58'
    Align = 'Left'
    CaptionStyle = 'Caption'
    CaptionLocation = 'Below'
    BorderWidth = 0.25
    PaddingTop = 1
    PaddingBottom = 1.5
    PaddingLeft = 2
    PaddingRight = 2
}
```

### Headers and Footers
The `Header` and `Footer` cmdlets define the document header and footer on the first and/or all pages of the document.

Each report will include a JSON configuration file which provides an option to enable/disable document headers and footers.

```json title="Show Header/Footer Option" hl_lines="8"
{
    "Report": {
        "Name": "VMware vSphere As Built Report",
        "Version": "1.0",
        "Status": "Released",
        "ShowCoverPageImage": true,
        "ShowTableOfContents": true,
        "ShowHeaderFooter": true,
        "ShowTableCaptions": true
    }
}
```

The following code should be included in your style script to utilise the report configration option. The highlighted lines can be modified to suit your requirements.

```powershell title="Add header and footer to style script" hl_lines="3 4 7 8"
# Set Header & Footer, if enabled in report JSON configuration
if ($ReportConfig.Report.ShowHeaderFooter) {
    Header -Default {
        Paragraph -Style Header -Text "$($ReportConfig.Report.Name) - v$($ReportConfig.Report.Version)"
    }

    Footer -Default {
        Paragraph -Style Footer -Text 'Page <!# PageNumber #!>'
    }
}
```

```powershell title="Additional information about Headers and Footers"
get-help Header -Detailed
get-help Footer -Detailed
```

### Images

!!! failure "Images are not supported when using Linux & macOS"

    Unfortunately due to [breaking changes](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only){:target="_blank"} in .NET 6, images are no longer supported for reports generated using Linux or macOS.

The `Image` cmdlet is used to insert images into a document. An image can be specified using the `URI` or `Base64` parameters.

Images can be converted to a Base64 string using an online image converter such as [Base64.Guru](https://base64.guru/converter/encode/image){:target="_blank"}.

`Align` and `Percent` values can be adjusted to horizontally position and size the image.

```powershell title="Additional information about Images"
get-help Image -Detailed
```
#### Cover Page

The code below should be included in a style script to set a cover image or logo. The highlighted line can be modified to suit your requirements.

```powershell title="Set Cover Page Image" hl_lines="4"
# Show Cover page image, if enabled in report JSON configuration
if ($ReportConfig.Report.ShowCoverPageImage) {
    Try {
        Image -Text 'My Image' -Align Left -Percent 50 -Base64 <Base64 string>
    } Catch {
        Write-PScriboMessage -IsWarning -Message ".NET Core is required for cover page image support. Please install .NET Core or disable 'ShowCoverPageImage' in the report JSON configuration file."
    }
}
```