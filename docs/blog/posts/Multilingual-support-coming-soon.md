---
draft: false
date: 2025-09-05
authors:
  - Tim
categories:
  - Features
  - Announcements
tags:
  - multilingual
  - localisation
  - powershell
  - new feature
slug: Multilingual-support
---

# Multilingual support now available for AsBuiltReport

Today I can announce that **multilingual support** for the AsBuiltReport framework is now available!

![multilingual](../../assets/images/blog/multilingual.jpg){ loading=lazy }

## Key Features


**🌐 Comprehensive Localization Framework**

- Implementation of PowerShell's built-in localization capabilities

- Option for differing UI localization and report localization

**📝 Standardised Translation Structure**

- Standardised folder structures for simple multilingual support adoption

- Support for resource files containing translated strings for AsBuiltReport core and report modules

- Automated string extraction and translation

**💻 New Commandline Parameters**

- Dynamic language selection - language selection is determined by what each AsBuiltReport module supports

- Support for standard locale codes (en-US, es-ES, fr-FR, de-DE, etc.)

- Fallback mechanism to ensure reports generate even with incomplete translations

**:gear: Report Module Integration**

- Documentation and templates for new and existing report modules to add multilingual support

- Backward compatibility ensuring existing English-only workflows continue to work

- Progressive enhancement allowing modules to adopt localization incrementally

<!-- more -->

## Technical Implementation
Multilingual support has been implemented using PowerShell's native localization features, including:

- **Resource Files**: Utilising `.psd1` resource files for each supported language

- **String Localization**: Converting hard-coded English strings to localizable resource keys

- **Cultural Formatting**: Ensuring dates, numbers, and other culture-specific elements display correctly

- **Encoding Support**: Proper handling of character encodings for various languages

## Timeline and Current Status
**Development Status**: Active development in progress

1. ✅ Localization framework design (complete)
2. ✅ Resource file and folder structures (complete)
3. ✅ Documentation and templates (complete)
4. ✅ AsBuiltReport Core module implementation and testing (complete)
5. 🔄 AsBuiltReport report module implementation and testing (in progress)
6. 🔄 Community translation coordination (in progress)

**Target Completion**: The foundational work for multilingual support is now complete. Work is now underway to add support for additional languages to individual report modules.

## How You Can Help

As an open-source project, AsBuiltReport thrives on community contributions. Here's how you can get involved with the multilingual initiative:

### For Developers
- Review the [`dev`](https://github.com/AsBuiltReport/AsBuiltReport.Core/tree/dev){:target="_blank"} branch and provide feedback
- Download the latest `AsBuiltReport.Core` module

    `Install-Module AsBuiltReport.Core -MinimumVersion 1.5.0 -Repository PSGallery`

- Download the `AsBuiltReport.System.Resources` report module to use for testing the new report language features

    `Install-Module AsBuiltReport.System.Resources -Repository PSGallery`

- Help test the new localization features
- Contribute code improvements or bug fixes
- [Update existing report modules](../../dev-guide/creating-a-report-module.md#language-support-implementation) to support the new framework

### For Translators and Linguists
- Express interest in translating AsBuiltReport modules to your language
- Use our GitHub [discussion board](https://github.com/orgs/AsBuiltReport/discussions){:target="_blank"} to share your ideas and feedback

### For Users
- Share your language requirements and use cases
- Test preview releases when available
- Provide feedback on the user experience
- Spread the word at your work and in your local IT communities

## Looking Ahead

The introduction of multilingual support represents a significant milestone for AsBuiltReport as it will:

- **Expand Global Reach**: Enable organisations worldwide to generate localized documentation
- **Enhance Professionalism**: Allow organisations to present documentation in their preferred language
- **Foster Community Growth**: Encourage contributions from more of the global user base

## Stay Connected

We're committed to keeping the community informed about our progress. To stay updated on the multilingual support development:

- **Watch the Repository**: Star and watch the [AsBuiltReport.Core repository](https://github.com/AsBuiltReport/AsBuiltReport.Core){:target="_blank"} for updates
- **Join Discussions**: Participate in the [GitHub discussion](https://github.com/orgs/AsBuiltReport/discussions/1){:target="_blank"} to share your ideas and feedback
- **Follow the Project**: Check the project [website](https://www.asbuiltreport.com) and [social channels](../../about/contact.md) for regular updates

## Acknowledgments

Thanks to all the users and contributors who requested this feature, those who provide feedback, and to everyone who has made AsBuiltReport what it is today. As always, AsBuiltReport remains committed to being a community-driven, open-sourced project, that serves the needs of IT professionals worldwide.

---