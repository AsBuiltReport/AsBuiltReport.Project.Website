## Description

`New-AsBuiltReportConfig` creates JSON configuration files for individual As Built Reports.

## Parameters

### Report

Specifies the type of report configuration to create.

This is a mandatory parameter.

### Folderpath

Specifies the folder path to create the report JSON configuration file.

This is a mandatory parameter.

### Filename

Specifies the filename of the report JSON configuration file.

This is an optional parameter.

If a filename is not specified, a JSON configuration file will be created with a default filename `AsBuiltReport.<Vendor>.<Technology>.json`

### Force

Specifies to overwrite an existing JSON configuration.

This is an optional parameter.

## Examples

1. Creates a new NetApp ONTAP report JSON configuration file in the `C:\Reports` folder.

    ```powershell title="Example 1"
    New-AsBuiltReportConfig -Report 'NetApp.ONTAP' -Folderpath 'C:\Reports'
    ```

2. Creates a new Microsoft Active Directory report JSON configuration file named `ACME.json` in the `C:\Reports` folder.

    ```powershell title="Example 2"
    New-AsBuiltReportConfig -Report 'Microsoft.AD' -Filename 'ACME' -Folderpath 'C:\AsBuiltReport'
    ```

3. Creates a new VMware vSphere report JSON configuration file in the `C:\Reports` folder, and overwrites the existing `AsBuiltReport.VMware.vSphere.json` file.

    ```powershell title="Example 3"
    New-AsBuiltReportConfig -Report 'VMware.vSphere' -Folderpath 'C:\Reports' -Force
    ```

    ```json title="Sample VMware vSphere Report JSON Configuration"
        {
        "Report": {                                     // The Report schema provides configuration of the report information.
            "Name": "VMware vSphere As Built Report",   // The name of the As Built Report
            "Version": "1.0",                           // The report version
            "Status": "Released",                       // The report release status
            "Language": "es-ES",                        // The report content language (Default en-US)
            "ShowCoverPageImage": true,                 // Toggle to enable/disable the display of the cover page image
            "ShowTableOfContents": true,                // Toggle to enable/disable table of contents
            "ShowHeaderFooter": true,                   // Toggle to enable/disable document headers & footers
            "ShowTableCaptions": true                   // Toggle to enable/disable table captions/numbering
        },
        "Options": {                                    // The Options schema allows certain options within the report to be toggled on or off.
            "ShowLicenseKeys": false,                   // Toggle to mask/unmask vSphere license keys
            "ShowVMSnapshots": true,                    // Toggle to enable/disable reporting of VM snapshots
        },
        "InfoLevel": {                                  // The InfoLevel schema allows configuration of each section of the report at a granular level.
            "_comment_": "0 = Disabled, 1 = Enabled / Summary, 2 = Adv Summary, 3 = Detailed, 4 = Adv Detailed, 5 = Comprehensive",
            "vCenter": 3,
            "Cluster": 3,
            "ResourcePool": 3,
            "VMHost": 3,
            "Network": 3,
            "vSAN": 3,
            "Datastore": 3,
            "DSCluster": 3,
            "VM": 2,
            "VUM": 3
        },
        "HealthCheck": {                                // The Healthcheck schema is used to toggle health checks on or off.
            "vCenter": {
                "Mail": true,
                "Licensing": true,
                "Alarms": true
            },
            "Cluster": {
                "HAEnabled": true,
                "HAAdmissionControl": true,
                "HostFailureResponse": true,
                "HostMonitoring": true,
                "DatastoreOnPDL": true,
                "DatastoreOnAPD": true,
                "APDTimeOut": true,
                "vmMonitoring": true,
                "DRSEnabled": true,
                "DRSAutomationLevelFullyAuto": true,
                "PredictiveDRS": false,
                "DRSVMHostRules": true,
                "DRSRules": true,
                "vSANEnabled": false,
                "EVCEnabled": true,
                "VUMCompliance": true
            },
            "VMHost": {
                "ConnectionState": true,
                "HyperThreading": true,
                "ScratchLocation": true,
                "IPv6": true,
                "UpTimeDays": true,
                "Licensing": true,
                "Certificates": true,
                "SSH": true,
                "ESXiShell": true,
                "NTP": true,
                "StorageAdapter": true,
                "NetworkAdapter": true,
                "LockdownMode": true,
                "VUMCompliance": true
            },
            "vSAN": {},
            "Datastore": {
                "CapacityUtilization": true
            },
            "DSCluster": {
                "CapacityUtilization": true,
                "SDRSAutomationLevelFullyAuto": true
            },
            "VM": {
                "PowerState": true,
                "ConnectionState": true,
                "CpuHotAdd": true,
                "CpuHotRemove": true,
                "MemoryHotAdd": true,
                "ChangeBlockTracking": true,
                "SpbmPolicyCompliance": true,
                "VMToolsStatus": true,
                "VMSnapshots": true
            }
        }
    }
    ```