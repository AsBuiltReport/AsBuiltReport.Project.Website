# GitHub Actions Deployment Workflow — Design Spec

**Date:** 2026-03-21
**Status:** Approved

## Overview

Automate the build and deployment of the AsBuiltReport MkDocs site from the source repository (`AsBuiltReport/AsBuiltReport.Project.Website`) to the GitHub Pages repository (`AsBuiltReport/AsBuiltReport.github.io`).

## Triggers

The workflow runs on:
- **Push to `master`** — automatically deploys on every commit to master
- **Manual dispatch (`workflow_dispatch`)** — allows triggering a deployment on demand from the GitHub Actions UI

## Build

1. Check out `AsBuiltReport/AsBuiltReport.Project.Website`
2. Set up Python (latest stable)
3. Install MkDocs Material and all required plugins:
   - `mkdocs-material`
   - `mkdocs-git-revision-date-localized-plugin`
   - `mkdocs-rss-plugin`
   - `pillow` and `cairosvg` (required for social cards)
   - `mkdocs-redirects`
4. Run `mkdocs build` with the `GOOGLE_ANALYTICS_KEY` environment variable injected from the GitHub Actions secret of the same name

## Deploy

- Use `peaceiris/actions-gh-pages` action to push the built `site/` directory to the `master` branch of `AsBuiltReport/AsBuiltReport.github.io`
- Authentication uses the PAT stored as the GitHub Actions secret `PERSONAL_ACCESS_TOKEN` on the source repository

## Secrets Required

| Secret name            | Purpose                                              | Stored on                              |
|------------------------|------------------------------------------------------|----------------------------------------|
| `GOOGLE_ANALYTICS_KEY` | GA4 Measurement ID injected during build             | `AsBuiltReport.Project.Website`        |
| `PERSONAL_ACCESS_TOKEN`| PAT for pushing to `AsBuiltReport.github.io`         | `AsBuiltReport.Project.Website`        |

## Workflow File Location

`.github/workflows/deploy.yml` in `AsBuiltReport/AsBuiltReport.Project.Website`

## Out of Scope

- Caching of pip dependencies (can be added later if build times become a concern)
- Pull request preview deployments
- Notifications on deployment success/failure
