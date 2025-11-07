This section provides information relating to common and/or known issues when generating an As Built Report.

!!! tip "Need Help Troubleshooting?"
    For guidance on diagnosing and resolving report generation problems, see the [Troubleshooting](troubleshooting.md) page. This page documents platform and framework limitations that cannot be resolved through troubleshooting.

#### Table Of Contents (TOC) is missing in Word formatted report

!!! attention

    When opening a Microsoft Word (DOCX) report for the first time, you will be prompted with the following warning;

    <img src='../../assets/images/Word_Warning.jpg'/>

    Clicking No will prevent the TOC fields from being updated, leaving the Table of Contents empty.

    Always reply Yes to this message when prompted by Microsoft Word to ensure the Table of Contents is updated.

    Save the document to prevent future prompts when opening the document.

#### Images are missing from reports generated using Linux or macOS

!!! failure "Not Supported"

    Unfortunately due to [breaking changes](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only){:target="_blank"} in .NET 6, images are no longer supported for reports generated using Linux or macOS.

For issues related to individual reports, please refer to the [report documentation pages](../user-guide/report-modules/overview.md) or the relevent report [GitHub repository](https://github.com/orgs/AsBuiltReport/repositories){:target="_blank"}.