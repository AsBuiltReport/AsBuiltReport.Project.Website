---
title: Document Your Datacenter With PowerShell
---

<h1 align="center" style="background-image: url('../../assets/images/background.jpg');color:white;">
    <br>
    <img src='../../assets/images/logos/AsBuiltReport.png' width="15%" height="15%" />
    <br>AsBuiltReport
    <br><br>Document Your Datacenter
    <br>With PowerShell
    <br><br>
</h1>

AsBuiltReport is an open source configuration document framework which utilises Microsoft PowerShell to produce as-built documentation in multiple document formats for multiple vendors and technologies. The framework allows users to easily generate clear and consistent documentation, for any environment which supports Microsoft PowerShell and/or a RESTful API.

## **Features**
<div class="grid cards" markdown>

-   :octicons-log-16: **Multiple Document Formats**

    ---

    Generate reports in one or more document formats, including DOCX, HTML, and Text.

-   :octicons-sliders-16: **Granular Information Level**

    ---

    Configure the information level for each report section. You can create a summary report, a fully comprehensive report, or something in between.

-   :octicons-paintbrush-16: **Customised Styling**

    ---

    Use the default style or [create your own](dev-guide/creating-a-report-style.md) to match your corporate identity. Set page orientation, text and table formatting with fonts, colours, borders and highlighted cells and rows.

-   :octicons-apps-16: **Modular Architecture**

    ---

    The modular architecture and core framework enables users to use the same in-built commands to generate as-built configuration reports from a library of technology vendors.

-   :octicons-pulse-16: **Health Checks**

    ---

    Enable health checks to highlight configuration issues within a report. Toggle individual health checks on or off as required.

-   :octicons-mail-16: **Email Reports**

    ---

    Attach and send reports via email to one or more recipients.

</div>


<!--
<p align="center" style="background-image: url('../../assets/images/laptop.png');background-size: 100% 100%;color:white;">
    <br><br>
    <br>AsBuiltReport is an open source configuration document framework which utilises
    <br>Microsoft PowerShell to produce as-built documentation in multiple document formats
    <br>for multiple vendors and technologies.
    <br><br>The framework allows users to easily generate clear and consistent documentation,
    <br>for any environment which supports Microsoft PowerShell and/or a RESTful API.
    <br><br><br><br>
</p>
-->

## **Components**
<div class="grid cards" markdown>

-   :simple-hackthebox: **Core Module**

    ---

    The core module provides the framework for each individual report module. It provides the [base commands](user-guide/new-asbuiltreport.md) and default style script used to generate each individual report.

-   :simple-hackthebox: **Reports Module**

    ---

    The report module is specific to each vendor and/or technology and is used to extract information from the specific environment.<br><br>The report module will be written to utilise PowerShell modules or RESTful APIs which the vendor/technology provides.

-   :material-code-json: **Core Module Configuration**

    ---

    The core module configuration is a JSON file which stores information relating to the author’s name, company information & SMTP mail server configuration.<br><br>Individual core module configuration files can be saved and specified when generating reports.

-   :material-code-json: **Reports Module Configuration**

    ---

    The reports module configuration is a JSON file which stores information specific to the related report. It holds information such as the report name, version, and release status.<br><br>The report configuration can also provide functionality such as configurable report options, health checks and granular information levels.<br><br>Individual report module configuration files can be saved and specified when generating reports.

-   :material-powershell: **Styles Script**

    ---

    The styles script sets the default layout, fonts, colours and sizes used within the report.<br><br>Style scripts can be used to layout cover pages, table of contents and other unique tables or sections.<br><br>Custom style scripts can be [created](dev-guide/creating-a-report-style.md) to format reports to match your corporate identity.

</div>

## **Report Modules**

Click each vendor logo to view available report modules and associated documentation.

<table width="100%">
    <tr>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=VMware&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/VMware.png" width="75%" height="75%" /></a></td>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=Microsoft&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/Microsoft.png" width="75%" height="75%" /></a></td>
    </tr>
    <tr>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=DellEMC&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/Dell_EMC.png" width="75%" height="75%" /></a></td>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=NetApp&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/NetApp.png" /></a></td>
    </tr>
    <tr>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=Nutanix&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/Nutanix.png" width="85%" height="85%" /></a></td>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=PureStorage&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/PureStorage.jpg" width="85%" height="85%" /></a></td>
    </tr>
    <tr>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=Veeam&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/Veeam.png" width="75%" height="75%" /></a></td>
        <td align="center" valign="middle" width="50%"><a href="https://github.com/orgs/AsBuiltReport/repositories?q=Rubrik&type=all&language=&sort=" target="_blank"><img src="../assets/images/logos/Rubrik.png" width="75%" height="75%" /></a></td>
    </tr>
</table>