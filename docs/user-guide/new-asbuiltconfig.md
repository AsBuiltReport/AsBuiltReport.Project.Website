## Description

`New-AsBuiltConfig` starts a menu-driven procedure in the PowerShell console asking the user a series of questions to create a JSON configuration file. The JSON configuration file may be saved and referenced by the `AsBuiltConfigFilePath` parameter in `New-AsBuiltReport`.

`New-AsBuiltConfig` is automatically called by `New-AsBuiltReport` if the `AsBuiltConfigFilePath` parameter is not specified. If a user wishes to generate a new AsBuiltReport configuration without generating a new report, this command can be called as a standalone cmdlet.

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

        Would you like to enter Company information for the AsBuiltReport? (y/n): `y`

        Enter the Full Company Name: `Wayne Enterprises`

        Enter the Company Short Name: `WayneCorp`

        Enter the Company Contact: `Bruce Wayne`

        Enter the Company Email Address: `bruce.wayne@waynecorp.com`

        Enter the Company Phone: `555-555-5555`

        Enter the Company Address: `Wayne Tower, Gotham City`

        **Email Configuration**

        Would you like to enter SMTP configuration? (y/n): `y`

        Enter the mail server FQDN / IP address: `172.16.10.30`

        Enter the mail server port number [25]: `25`

        Use SSL for mail server connection? (true/false): `true`

        Require mail server authentication? (true/false): `false`

        Enter the mail sender address: `support@asbuiltreport.com`

        Enter the mail server recipient address: `bruce.wayne@waynecorp.com`

        Do you want to enter another recipient? (y/n): `n`

        Enter the email message body content: `AsBuiltReport attached`

        **AsBuiltReport Configuration**

        Would you like to save the AsBuiltReport configuration file? (y/n): `y`

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