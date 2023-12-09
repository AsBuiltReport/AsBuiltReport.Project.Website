When generating an As Built Report, its formatting and style is defined using a PowerShell (.ps1) script which utilises a set of [PScribo](../support/faq.md#what-is-pscribo) cmdlets.

When creating a report style for a new report module, the default colours and logos (if permitted) should align to a vendor's branding guidelines. Most vendors will publish their branding guidelines on their website. A simple Google search should reveal all the information you need to create a report style for a particular vendor. Where a report module already exists for a particular vendor, please ensure you include the existing vendor report style in the new report module.

This guide may also be used to create custom style scripts which match your individual and/or corporate identities.

!!! info

    This guide assumes you have already [installed](../user-guide/installation.md) an AsBuiltReport module.

    Most of the information contained within this guide has been sourced from the official PScribo documentation.

!!! tip

    Use any report's default style script as a reference for creating a new style script, or download some sample styles from our [GitHub repository](https://github.com/AsBuiltReport/AsBuiltReport.Core/tree/dev/Samples){:target="_blank"}.

    A report's default style script is located in the report module root folder and is named `AsBuiltReport.<Vendor>.<Product>.Style.ps1`

### Global Document Options

The `DocumentOption` cmdlet is used to set global document options, including default font, page size, margins and orientation.

`EnableSectionNumbering` enables automatic numbering of document sections.

`PageSize` sets the page size. Available options include A4, Letter and Legal.

`DefaultFont` sets the default font. It is highly recommended to use a standard, [web-safe](https://www.w3schools.com/cssref/css_websafe_fonts.asp){:target="_blank"} font.

`MarginLeftAndRight` sets the left and right page margins to the points (pt) specified.

`MarginTopAndBottom` sets the top and bottom page margins to the points (pt) specified.

`Orientation` sets the document's default page orientation. It is highly recommended that you do not modify the `$Orientation` parameter value.

```powershell title="Additonal Information"
get-help about_PScriboDocument
```

```powershell title="DocumentOption"
# Default DocumentOption
DocumentOption -EnableSectionNumbering -PageSize 'A4' -DefaultFont 'Arial' -MarginLeftAndRight 71 -MarginTopAndBottom 71 -Orientation $Orientation

# Custom DocumentOption
# Disable automatic section numbering. Set page size to Letter. Set default font to Tahoma. Set custom page margins.
DocumentOption -PageSize 'Letter' -DefaultFont 'Tahoma' -MarginLeftAndRight 74 -MarginTopAndBottom 65 -Orientation $Orientation
```


### Styles
The `Style` cmdlet defines a custom formatting style which can be applied to section headings, paragraphs and within table styles. Styles need to be defined before any formatting can be applied within a document (with the exception of paragraphs). Each style permits the setting of the font to use, the font size and colour.

```powershell title="Additonal Information"
get-help about_PScriboStyles
```


#### Default Styles
A style script uses a standard set of styles for a report. These styles are defined below and must be included in every style script.

```text title=""
Normal              - Default text style
Title               - Cover Page Title text style
Title 2             - Cover Page Subtitle 1 text style
Title 3             - Cover Page Subtitle 2 text style
TOC                 - Section heading Table of Contents text style
Heading1            - Section heading level 1 text style
Heading2            - Section heading level 2 text style
Heading3            - Section heading level 3 text style
Heading4            - Section heading level 4 text style
Heading5            - Section heading level 5 text style
Heading6            - Section heading level 6 text style
TableDefaultHeading - Table heading row style
TableDefaultRow     - Table row style
TableDefaultAltRow  - Table alternating row style
Caption             - Table caption style
Header              - Document header style
Footer              - Document footer style
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
Style -Name 'Title' -Size 24 -Color '00785F' -Align Left
Style -Name 'Title 2' -Size 18 -Color '00A956' -Align Left
Style -Name 'Title 3' -Size 12 -Color '006A91' -Align Left
Style -Name 'Heading 1' -Size 16 -Color '00785F'
Style -Name 'Heading 2' -Size 14 -Color '004B6B'
Style -Name 'Heading 3' -Size 12 -Color '00567A'
Style -Name 'Heading 4' -Size 11 -Color '00648F'
Style -Name 'Heading 5' -Size 10 -Color '0072A3'
Style -Name 'Normal' -Size 10 -Color '000000' -Default

# Header & Footer Formatting
Style -Name 'Header' -Size 10 -Color '000000' -Align Left
Style -Name 'Footer' -Size 10 -Color '000000' -Align Right

# Table of Contents Formatting
Style -Name 'TOC' -Size 16 -Color '00785F'

# Table Heading & Row Formatting
Style -Name 'TableDefaultHeading' -Size 10 -Color 'FAFAFA' -BackgroundColor '00785F'
Style -Name 'TableDefaultRow' -Size 10 -Color '000000'
Style -Name 'TableDefaultAltRow' -Size 10 -Color '000000' -BackgroundColor 'EAEAE6'

# Table Row/Cell Highlight Formatting
Style -Name 'Critical' -Size 10 -Color '000000' -BackgroundColor 'FEDDD7'
Style -Name 'Warning' -Size 10 -Color '000000' -BackgroundColor 'FFF4C7'
Style -Name 'Info' -Size 10 -Color '000000' -BackgroundColor 'E3F5FC'
Style -Name 'OK' -Size 10 -Color '000000' -BackgroundColor 'DFF0D0'

# Table Caption Formatting
Style -Name 'Caption' -Size 10 -Color '000000' -Align Left
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
    AlternateRowStyle = 'TableDefaultAltRow'
    BorderColor = '00785F'
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
        "ShowCoverPageImage": true,
        "ShowTableOfContents": true,
        "ShowHeaderFooter": true,
        "ShowTableCaptions": true
    }
}
```

Should you wish to include an option for a Table of Contents within your style script, ensure you add the following code to the end of your script.

```powershell title=""
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
    BorderColor = '00785F'
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

```powershell title="" hl_lines="3 4 7 8"
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

```powershell title="Additional Information"
get-help Header -Detailed
get-help Footer -Detailed
```

### Images

!!! failure "Images are not supported when using Linux & macOS"

    Unfortunately due to [breaking changes](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only){:target="_blank"} in .NET 6, images are no longer supported for reports generated using Linux or macOS.

The `Image` cmdlet is used to insert images into a document. An image can be specified using the `URI` or `Base64` parameters.

Images can be converted to a Base64 string using an online image converter such as [Base64.Guru](https://base64.guru/converter/encode/image){:target="_blank"}.

`Align` and `Percent` values can be adjusted to horizontally position and size the image.

```powershell title="Additional Information"
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