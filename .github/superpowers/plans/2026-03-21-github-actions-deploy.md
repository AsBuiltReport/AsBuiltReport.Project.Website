# GitHub Actions Deployment Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a GitHub Actions workflow that automatically builds the MkDocs site and deploys it to `AsBuiltReport/AsBuiltReport.github.io` on every push to `master`, and on demand.

**Architecture:** A single workflow file in `.github/workflows/deploy.yml` handles both build and deploy in one job. The build step runs `mkdocs build` with the GA key injected from a secret. The deploy step uses `peaceiris/actions-gh-pages@v4` to push the built `site/` directory to the target repo using a PAT secret.

**Tech Stack:** GitHub Actions, MkDocs Material, peaceiris/actions-gh-pages@v4, Python 3.12, Ubuntu runner

---

## File Map

| Action   | Path                                    | Responsibility                            |
|----------|-----------------------------------------|-------------------------------------------|
| Create   | `.github/workflows/deploy.yml`          | Full build-and-deploy workflow definition |

---

### Task 1: Add secrets to the source repository

Before any workflow can run, both secrets must exist on `AsBuiltReport/AsBuiltReport.Project.Website`.

- [ ] **Step 1: Open the repository secrets page**

  Navigate to: `https://github.com/AsBuiltReport/AsBuiltReport.Project.Website/settings/secrets/actions`

- [ ] **Step 2: Add `GOOGLE_ANALYTICS_KEY`**

  Click **New repository secret**.
  - Name: `GOOGLE_ANALYTICS_KEY`
  - Value: your GA4 Measurement ID (starts with `G-`)

- [ ] **Step 3: Add `PERSONAL_ACCESS_TOKEN`**

  Click **New repository secret**.
  - Name: `PERSONAL_ACCESS_TOKEN`
  - Value: your existing PAT (must have `repo` scope to push to `AsBuiltReport/AsBuiltReport.github.io`)

- [ ] **Step 4: Verify both secrets appear in the list**

  The secrets page should now show both `GOOGLE_ANALYTICS_KEY` and `PERSONAL_ACCESS_TOKEN` listed under Repository secrets.

---

### Task 2: Create the workflow file

- [ ] **Step 1: Create the `.github/workflows/` directory**

  ```bash
  mkdir -p .github/workflows
  ```

- [ ] **Step 2: Create `.github/workflows/deploy.yml` with the following content**

  ```yaml
  name: Deploy MkDocs to GitHub Pages

  on:
    push:
      branches:
        - master
    workflow_dispatch:

  concurrency:
    group: deploy
    cancel-in-progress: true

  jobs:
    deploy:
      runs-on: ubuntu-latest

      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Set up Python 3.12
          uses: actions/setup-python@v5
          with:
            python-version: '3.12'

        - name: Install system dependencies
          run: |
            sudo apt-get update
            sudo apt-get install -y \
              libcairo2-dev \
              libfreetype6-dev \
              libffi-dev \
              libjpeg-dev \
              libpng-dev \
              zlib1g-dev

        - name: Install Python dependencies
          run: |
            pip install \
              mkdocs-material \
              mkdocs-git-revision-date-localized-plugin \
              mkdocs-rss-plugin \
              pillow \
              cairosvg \
              mkdocs-redirects

        - name: Build MkDocs site
          env:
            GOOGLE_ANALYTICS_KEY: ${{ secrets.GOOGLE_ANALYTICS_KEY }}
          run: mkdocs build

        - name: Deploy to GitHub Pages
          uses: peaceiris/actions-gh-pages@v4
          with:
            personal_token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
            external_repository: AsBuiltReport/AsBuiltReport.github.io
            publish_branch: master
            publish_dir: ./site
  ```

- [ ] **Step 3: Commit and push**

  ```bash
  git add .github/workflows/deploy.yml
  git commit -m "feat: add GitHub Actions workflow to build and deploy MkDocs site"
  git push origin master
  ```

---

### Task 3: Verify the first workflow run

- [ ] **Step 1: Watch the workflow run**

  Navigate to: `https://github.com/AsBuiltReport/AsBuiltReport.Project.Website/actions`

  You should see a workflow run triggered by the push. Click into it to follow the live logs.

- [ ] **Step 2: Confirm all steps pass**

  All six steps should show green:
  - Checkout repository
  - Set up Python 3.12
  - Install system dependencies
  - Install Python dependencies
  - Build MkDocs site
  - Deploy to GitHub Pages

  If any step fails, read the log output for that step — the error message will identify the cause.

- [ ] **Step 3: Verify the target repo was updated**

  Navigate to: `https://github.com/AsBuiltReport/AsBuiltReport.github.io`

  The most recent commit should be a new automated commit from the workflow (author will be `github-actions[bot]`).

- [ ] **Step 4: Verify the live site**

  Open `https://www.asbuiltreport.com` and confirm the latest content is live.

- [ ] **Step 5: Verify Google Analytics is present**

  In your browser, view the page source of `https://www.asbuiltreport.com` and search for `gtag`. You should find a `<script>` tag referencing `googletagmanager.com` with your `G-` Measurement ID embedded.
