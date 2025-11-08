---
title: New-AsBuiltConfig
description: Create AsBuiltReport core configuration files for company information, branding, and email settings
tags:
  - command
  - cmdlet
  - configuration
  - setup
  - json
---

## Description

`New-AsBuiltConfig` starts a menu-driven procedure in the PowerShell console asking the user a series of questions to create a JSON configuration file. The JSON configuration file may be saved and referenced by the `AsBuiltConfigFilePath` parameter in `New-AsBuiltReport`.

`New-AsBuiltConfig` is automatically called by `New-AsBuiltReport` if the `AsBuiltConfigFilePath` parameter is not specified. If a user wishes to generate a new AsBuiltReport configuration without generating a new report, this command can be called as a standalone cmdlet.

## When to Use This Command

| Scenario | Recommended Approach |
|----------|---------------------|
| **First Time User** | Let `New-AsBuiltReport` prompt you automatically |
| **Multiple Clients/Sites** | Run `New-AsBuiltConfig` to create separate configs for each |
| **Corporate Branding** | Create a config once, reuse for all reports |
| **Email Distribution** | Configure SMTP settings once, use across all reports |
| **Quick Test** | Skip this - just run `New-AsBuiltReport` and answer prompts |

!!! tip "Configuration Reuse"
    Create configuration files for different scenarios:

    - **Client-specific**: `ACME-Config.json`, `WayneCorp-Config.json`
    - **Environment-specific**: `Production-Config.json`, `Development-Config.json`
    - **Purpose-specific**: `Audit-Config.json`, `Documentation-Config.json`

    Then reference them with: `-AsBuiltConfigFilePath 'C:\Configs\ACME-Config.json'`

## Parameters

There are no additional parameters for this command.

## Examples

1. Starts a menu-driven procedure to create an AsBuiltReport configuration file.

    ```powershell title="Example 1"
    New-AsBuiltConfig
    ```

    !!! example " New-AsBuiltConfig Sample Output"
        **AsBuiltReport Information**

        Enter the name of the Author for this AsBuiltReport [Tim]: `Tim Carman`

        **Company Information**

        Would you like to enter Company information for the AsBuiltReport? (y/N): `y`

        Enter the Full Company Name: `Wayne Enterprises`

        Enter the Company Short Name: `WayneCorp`

        Enter the Company Contact: `Bruce Wayne`

        Enter the Company Email Address: `bruce.wayne@waynecorp.com`

        Enter the Company Phone: `555-555-5555`

        Enter the Company Address: `Wayne Tower, Gotham City`

        **Email Configuration**

        Would you like to enter SMTP configuration? (y/N): `y`

        Enter the mail server FQDN / IP address: `172.16.10.30`

        Enter the mail server port number [25]: `25`

        Use SSL for mail server connection? (true/false): `true`

        Require mail server authentication? (true/false): `false`

        Enter the mail sender address: `support@asbuiltreport.com`

        Enter the mail server recipient address: `bruce.wayne@waynecorp.com`

        Do you want to enter another recipient? (y/N): `n`

        Enter the email message body content: `AsBuiltReport attached`

        **AsBuiltReport Configuration**

        Would you like to save the AsBuiltReport configuration file? (Y/n): `y`

        Enter a name for the AsBuiltReport configuration file [AsBuiltReport]: `WayneCorp`

        Enter the path to save the AsBuiltReport configuration file [C:\Users\Tim\AsBuiltReport]: `C:\Documents\Clients\WayneCorp\AsBuiltReport`

        | Name       | Value                               |
        |------------|-------------------------------------|
        | Email      | {Port, Server, Body, UseSSL…}       |
        | UserFolder | {Path}                              |
        | Company    | {ShortName, Phone, Contact, Email…} |
        | Report     | {Author}                            |

    ```json title="New-AsBuiltConfig Sample JSON Configuration"
        {
            "Email": {
                "Port": "25",
                "Server": "172.16.10.30",
                "Body": "AsBuiltReport attached",
                "UseSSL": true,
                "To": [
                "bruce.wayne@waynecorp.com"
                ],
                "Credentials": false,
                "From": "support@asbuiltreport.com"
            },
            "UserFolder": {
                "Path": "C:\\Documents\\Clients\\ACME\\AsBuiltReport"
            },
            "Company": {
                "ShortName": "WayneCorp",
                "Phone": "555-555-5555",
                "Contact": "Bruce Wayne",
                "Email": "bruce.wayne@waynecorp.com",
                "Address": "Wayne Tower, Gotham City",
                "FullName": "Wayne Enterprises"
            },
            "Report": {
                "Author": "Tim Carman"
            }
        }
    ```

!!! warning "SMTP Credentials Security"
    If your SMTP server requires authentication (`"Credentials": true`), you will be prompted for credentials when running `New-AsBuiltReport`. These credentials are not stored in the configuration file. For automated/scheduled reports, consider:

    - Using an SMTP server that doesn't require authentication (internal relay)
    - Configuring SMTP to allow sending from your server without authentication
    - Using application-specific passwords or service accounts

## Using Configuration Files

Once created, reference your configuration file when generating reports:

```powershell title="Using a saved configuration"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com `
-Credential $Cred -AsBuiltConfigFilePath 'C:\Configs\WayneCorp.json' `
-OutputFolderPath 'C:\Reports'
```

You can create and maintain multiple configuration files for different purposes:

```powershell title="Multiple configurations example"
# Client A - Full branding and email
New-AsBuiltReport -Report VMware.vSphere -Target vcenter-clienta.com `
-Credential $Cred -AsBuiltConfigFilePath 'C:\Configs\ClientA.json'

# Client B - Different branding and email
New-AsBuiltReport -Report VMware.vSphere -Target vcenter-clientb.com `
-Credential $Cred -AsBuiltConfigFilePath 'C:\Configs\ClientB.json'
```

## See Also

- [New-AsBuiltReport](new-asbuiltreport.md) - Generate as-built configuration reports
- [New-AsBuiltReportConfig](new-asbuiltreportconfig.md) - Create report-specific configuration files
- [FAQ - How do I schedule reports?](../support/faq.md#how-do-i-schedule-reports-to-run-automatically) - Automating report generation