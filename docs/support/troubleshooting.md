# Troubleshooting

This page provides guidance on troubleshooting common issues when generating AsBuiltReport reports.

!!! tip "Installation Issues?"
    For help with installation, module updates, or uninstallation issues, please see the [Installation Troubleshooting](../user-guide/installation.md#troubleshooting) section.

## Report Generation Issues

### Enable Verbose Output

The first step in troubleshooting report generation issues is to enable verbose output. This provides detailed information about what the report is doing at each step.

Use the `-Verbose` parameter when running `New-AsBuiltReport`:

```powershell title="Generate report with verbose output"
New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Username 'admin' -Password 'S3cureP@ssword' -Format HTML -Verbose
```

The verbose output will show:

- Connection attempts and authentication status
- Which sections of the report are being processed
- Data collection progress for each component
- Any warnings or errors encountered
- Performance timing information

!!! example "Analyzing Verbose Output"
    Look for error messages or warnings in the verbose output. Common patterns include:

    - **"Access Denied"** - Insufficient permissions
    - **"Unable to connect"** - Network or credential issues
    - **"Null valued expression"** - Missing or unavailable data
    - **"Method invocation failed"** - API or cmdlet compatibility issues

### Use InfoLevel to Isolate Issues

If a report fails or hangs during generation, use the `InfoLevel` settings in the report JSON configuration file to isolate which section is causing the problem.

#### Understanding InfoLevel

Each report section has an associated `InfoLevel` setting that controls the depth of information collected:

- **InfoLevel 0**: Minimal information (summary only)
- **InfoLevel 1**: Basic information
- **InfoLevel 2**: Detailed information
- **InfoLevel 3+**: Comprehensive information (varies by report)

Higher InfoLevels collect more data but take longer to process and may be more prone to errors.

#### Step-by-Step Troubleshooting with InfoLevel

1. **Create or locate your report JSON configuration file:**

    ```powershell title="Create a report configuration file"
    New-AsBuiltReportConfig -Report VMware.vSphere -Path C:\Reports
    ```

    This creates a JSON file (e.g., `AsBuiltReport.VMware.vSphere.json`) in the specified path.

2. **Open the JSON configuration file in a text editor:**

    ```json title="Example InfoLevel section"
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
      },
      "InfoLevel": {
        "_comment_": "0 = Disabled, 1 = Enabled / Summary, 2 = Adv Summary, 3 = Detailed, 4 = Adv Detailed, 5 = Comprehensive",
        "vCenter": 3,
        "Cluster": 3,
        "VMHost": 3,
        "VM": 3,
        "Network": 3,
        "vSAN": 3,
        "Datastore": 3
      }
    }
    ```

3. **Set ALL InfoLevels to 0:**

    ```json title="Set all InfoLevels to 0"
    {
      "InfoLevel": {
        "_comment_": "0 = Disabled, 1 = Enabled / Summary, 2 = Adv Summary, 3 = Detailed, 4 = Adv Detailed, 5 = Comprehensive",
        "vCenter": 0,
        "Cluster": 0,
        "VMHost": 0,
        "VM": 0,
        "Network": 0,
        "vSAN": 0,
        "Datastore": 0
      }
    }
    ```

4. **Run the report with the modified configuration:**

    ```powershell title="Run report with InfoLevel 0 configuration"
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Username admin -Password (ConvertTo-SecureString 'P@ssw0rd' -AsPlainText -Force) -AsBuiltConfigFilePath C:\Reports\AsBuiltReport.VMware.vSphere.json -Format HTML -Verbose
    ```

5. **If the report succeeds with InfoLevel 0, gradually increase levels:**

    Incrementally increase the InfoLevel for each section to identify which one causes the issue:

    ```json title="Incrementally test each section"
    {
      "InfoLevel": {
        "_comment_": "0 = Disabled, 1 = Enabled / Summary, 2 = Adv Summary, 3 = Detailed, 4 = Adv Detailed, 5 = Comprehensive",
        "vCenter": 1,    // Test with 1, then 2, then 3
        "Cluster": 0,    // Keep others at 0 while testing
        "VMHost": 0,
        "VM": 0,
        "Network": 0,
        "vSAN": 0,
        "Datastore": 0
      }
    }
    ```

6. **Identify the problematic section:**

    Once you identify which section causes the failure, you can:
    - Report the issue on the module's GitHub repository
    - Use a lower InfoLevel for that section to work around the issue
    - Investigate specific permissions or data that might be causing the problem

!!! tip "Testing Strategy"
    Test sections in order of priority. Start with the sections most important to your documentation needs. This way, you can generate a partial report while the issue is being resolved.

### Common Report Generation Errors

#### Authentication Failures

**Symptoms:**

- "Login failed" or "Access Denied" errors
- Report fails immediately after starting

**Solutions:**

1. Verify credentials are correct

2. Check account has sufficient permissions (typically read-only access is sufficient)

3. For AD accounts, use domain\\username format:

    ```powershell
    -Username "DOMAIN\username"
    ```

4. Use credential objects for complex passwords:

    ```powershell
    $Credential = Get-Credential
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential $Credential
    ```

5. Check if the account is locked or password expired

#### Connection Timeouts

**Symptoms:**

- Report hangs or times out during data collection
- "Connection timed out" errors

**Solutions:**

1. Verify network connectivity to the target system:

    ```powershell
    Test-Connection -ComputerName vcenter.example.com
    ```

2. Check firewall rules allow the required ports

3. For large environments, increase timeout values (if supported by the report module)

4. Reduce InfoLevel to decrease data collection time

#### Missing or Incomplete Data

**Symptoms:**

- Report generates but sections are empty
- "No data available" messages in report

**Solutions:**

1. Verify the account has permissions to view the data

2. Check if the feature/component is actually configured in your environment

3. Use verbose output to see if data collection encountered errors:

    ```powershell
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential $Cred -Verbose
    ```

4. Verify the target system version is supported by the report module

#### Out of Memory Errors

**Symptoms:**

- PowerShell crashes during report generation
- "Out of Memory" or "Insufficient Memory" errors

**Solutions:**

1. Close other applications to free up memory

2. Reduce InfoLevel settings to collect less data

3. Generate reports for smaller scopes (e.g., individual clusters instead of entire vCenter)

4. Increase PowerShell memory limits (64-bit PowerShell recommended)

5. Run the report on a machine with more RAM

#### Report Hangs or Takes Too Long

**Symptoms:**

- Report appears to hang during generation
- Report takes hours to complete

**Solutions:**

1. Enable verbose output to see where it's hanging:

    ```powershell
    New-AsBuiltReport -Report VMware.vSphere -Target vcenter.example.com -Credential $Cred -Verbose
    ```

2. Use InfoLevel isolation (described above) to identify the slow section

3. Reduce InfoLevel for time-consuming sections

4. For large environments, consider:
    - Generating reports per cluster/location instead of entire environment
    - Scheduling reports during off-peak hours
    - Running on a more powerful machine

5. Check if antivirus is scanning PowerShell processes (add exclusions if needed)

### Module-Specific Issues

Each report module may have unique requirements and known issues. Always check:

1. **Module README**: Visit the module's GitHub repository (linked from [Report Modules](../user-guide/report-modules/overview.md))

2. **Module Version**: Ensure you're using the latest version:

    ```powershell
    Update-Module -Name AsBuiltReport.VMware.vSphere
    ```

3. **System Requirements**: Verify all prerequisites are met (PowerShell version, required modules, etc.)

4. **Known Issues**: Check the module's GitHub Issues page for reported problems

## Getting Additional Help

If you continue to experience issues after trying these troubleshooting steps:

### 1. Gather Diagnostic Information

Before seeking help, collect the following information:

```powershell title="Gather diagnostic information"
# PowerShell version
$PSVersionTable

# Module versions
Get-Module -Name AsBuiltReport.* -ListAvailable | Select-Object Name, Version

# Full error message (if available)
$Error[0] | Format-List -Force
```

### 2. Check Existing Resources

- Review the [FAQ](faq.md) for common questions
- Check [Known Issues](known-issues.md) for documented problems
- Search the [GitHub Discussions](https://github.com/orgs/AsBuiltReport/discussions) for similar issues

### 3. Report the Issue

If you've found a bug or need assistance:

1. Visit the specific report module's GitHub repository
2. Search existing Issues to see if it's already reported
3. If not found, open a new Issue with:
    - Detailed description of the problem
    - Steps to reproduce
    - PowerShell version (`$PSVersionTable`)
    - Module versions
    - Verbose output (sanitise sensitive information)
    - Relevant error messages

### 4. Community Support

Join the community discussion board for general questions and support:

- [AsBuiltReport Discussions](https://github.com/orgs/AsBuiltReport/discussions)

## Best Practices for Reliable Reports

To minimise issues when generating reports:

1. **Keep modules updated**: Regularly update AsBuiltReport.Core and report modules
2. **Test in non-production first**: Validate reports in test environments
3. **Use read-only accounts**: Dedicated service accounts with appropriate read permissions
4. **Start with low InfoLevels**: Begin with InfoLevel 0-1 and increase as needed
5. **Monitor resource usage**: Ensure adequate CPU, memory, and network bandwidth
6. **Schedule appropriately**: Run large reports during maintenance windows or off-peak hours
7. **Maintain configurations**: Keep your JSON configuration files version-controlled
8. **Document customisations**: Note any InfoLevel adjustments or workarounds for future reference
