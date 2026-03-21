# GitHub Actions Deployment Workflow — Design Spec

**Date:** 2026-03-21
**Status:** Approved

## Overview

Automate the build and deployment of the AsBuiltReport MkDocs site from the source repository (`AsBuiltReport/AsBuiltReport.Project.Website`) to the GitHub Pages repository (`AsBuiltReport/AsBuiltReport.github.io`).

## Triggers

The workflow runs on:
- **Push to `master`** — automatically deploys on every commit to master
- **Manual dispatch (`workflow_dispatch`)** — allows triggering a deployment on demand from the GitHub Actions UI

## Concurrency

A `concurrency` group keyed on the workflow name with `cancel-in-progress: true` must be set. This prevents two simultaneous deployments racing to overwrite each other if commits land in quick succession on `master`.

## Build

1. Check out `AsBuiltReport/AsBuiltReport.Project.Website` with **`fetch-depth: 0`** (full git history required by the `git-revision-date-localized` plugin — without it, every page silently falls back to the build date instead of the actual revision date)
2. Set up **Python 3.12** (pinned for reproducibility)
3. Install system-level native libraries required by the `social` plugin's Cairo/FreeType rendering:
   - `libcairo2-dev`
   - `libfreetype6-dev`
   - `libffi-dev`
   - `libjpeg-dev`
   - `libpng-dev`
   - `zlib1g-dev`
4. Install Python dependencies via pip (unpinned for now — accepted trade-off in favour of simplicity; a `requirements.txt` with pinned versions can be introduced later if plugin breakage becomes a problem):
   - `mkdocs-material`
   - `mkdocs-git-revision-date-localized-plugin`
   - `mkdocs-rss-plugin`
   - `pillow`
   - `cairosvg`
   - `mkdocs-redirects`
5. Run `mkdocs build` with the `GOOGLE_ANALYTICS_KEY` environment variable injected from the GitHub Actions secret of the same name (confirmed: `mkdocs.yml` line 41 reads `!ENV GOOGLE_ANALYTICS_KEY`, so the names match exactly)

## Deploy

- Use **`peaceiris/actions-gh-pages@v4`** (pinned to major version tag) to push the built `site/` directory to the `master` branch of `AsBuiltReport/AsBuiltReport.github.io`
- Authentication uses the PAT stored as the GitHub Actions secret `PERSONAL_ACCESS_TOKEN` on the source repository
- The `site_url` in `mkdocs.yml` is already set to `https://www.asbuiltreport.com`, so the social cards plugin will generate correct absolute URLs with no additional configuration

## Verification

After the first successful run, manually verify:
- The `AsBuiltReport/AsBuiltReport.github.io` repo has been updated with the new build
- The live site at `https://www.asbuiltreport.com` reflects the latest content
- Google Analytics is present in the page source (`gtag.js` script tag with the correct ID)

## Secrets Required

| Secret name             | Purpose                                              | Stored on                       |
|-------------------------|------------------------------------------------------|---------------------------------|
| `GOOGLE_ANALYTICS_KEY`  | GA4 Measurement ID injected during build             | `AsBuiltReport.Project.Website` |
| `PERSONAL_ACCESS_TOKEN` | PAT for pushing to `AsBuiltReport.github.io`         | `AsBuiltReport.Project.Website` |

## Workflow File Location

`.github/workflows/deploy.yml` in `AsBuiltReport/AsBuiltReport.Project.Website`

## Out of Scope

- Pinned `requirements.txt` (can be added later if build stability becomes a concern)
- Pull request preview deployments
- Automated post-deploy smoke tests or notifications
