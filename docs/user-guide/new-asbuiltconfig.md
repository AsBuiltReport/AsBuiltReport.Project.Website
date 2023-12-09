## Description

`New-AsBuiltConfig` starts a menu-driven procedure in the PowerShell console asking the user a series of questions to create a JSON configuration file. The JSON configuration file may be saved and referenced by the `AsBuiltConfigPath` parameter in `New-AsBuiltReport`.

`New-AsBuiltConfig` is automatically called by `New-AsBuiltReport` if the `AsBuiltConfigPath` parameter is not specified. If a user wishes to generate a new As Built Report configuration without generating a new report, this command can be called as a standalone cmdlet.

## Parameters

There are no additional parameters for this command.

## Examples

1. Starts a menu-driven procedure to create an As Built Report configuration file.

    ```powershell title="Example 1"
    New-AsBuiltConfig
    ```

    !!! example " New-AsBuiltConfig Sample Output"
        **As Built Report Information**

        Enter the name of the Author for this As Built Report [Tim]: `Tim Carman`

        **Company Information**

        Would you like to enter Company information for the As Built Report? (y/n): `y`

        Enter the Full Company Name: `ACME Inc`

        Enter the Company Short Name: `ACME`

        Enter the Company Contact: `Wile E. Coyote`

        Enter the Company Email Address: `wile.e.coyote@acme.inc`

        Enter the Company Phone: `555-555-5555`

        Enter the Company Address: `1 Looney Tunes Street`

        **Email Configuration**

        Would you like to enter SMTP configuration? (y/n): `y`

        Enter the mail server FQDN / IP address: `172.16.10.30`

        Enter the mail server port number [25]: `25`

        Use SSL for mail server connection? (true/false): `true`

        Require mail server authentication? (true/false): `false`

        Enter the mail sender address: `support@asbuiltreport.com`

        Enter the mail server recipient address: `wile.e.coyote@acme.inc`

        Do you want to enter another recipient? (y/n): `n`

        Enter the email message body content: `As Built Report attached`

        **As Built Report Configuration**

        Would you like to save the As Built Report configuration file? (y/n): `y`

        Enter a name for the As Built Report configuration file [AsBuiltReport]: `ACME`

        Enter the path to save the As Built Report configuration file [C:\Users\Tim\AsBuiltReport]: `C:\Documents\Clients\ACME\AsBuiltReport`

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
                "Body": "As Built Report attached",
                "UseSSL": true,
                "To": [
                "wile.e.coyote@acme.inc"
                ],
                "Credentials": false,
                "From": "support@asbuiltreport.com"
            },
            "UserFolder": {
                "Path": "C:\\Documents\\Clients\\ACME\\AsBuiltReport"
            },
            "Company": {
                "ShortName": "ACME",
                "Phone": "555-555-5555",
                "Contact": "Wile E. Coyote",
                "Email": "wile.e.coyote@acme.inc",
                "Address": "1 Looney Tunes Street",
                "FullName": "ACME Inc"
            },
            "Report": {
                "Author": "Tim Carman"
            }
        }
    ```