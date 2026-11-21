"""Build hook: look up the latest AsBuiltReport.Core release.

Sets config.extra.core_version, shown as the Revision in the footer title
block. Set extra.core_version in properdocs.yml to pin a value instead.
If GitHub can't be reached the build carries on without a version number.
"""

import json
import logging
import os
import urllib.request

log = logging.getLogger("mkdocs.hooks.core_version")

RELEASE_URL = "https://api.github.com/repos/AsBuiltReport/AsBuiltReport.Core/releases/latest"
_cached = None


def _latest_release():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "asbuiltreport-website",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(RELEASE_URL, headers=headers)
    with urllib.request.urlopen(request, timeout=5) as response:
        return json.load(response)["tag_name"].lstrip("vV")


def on_config(config, **kwargs):
    global _cached
    extra = config["extra"]
    if extra.get("core_version"):
        return config
    if _cached is None:
        try:
            _cached = _latest_release()
            log.info("AsBuiltReport.Core latest release: %s", _cached)
        except Exception as error:  # network or API failure must not stop the build
            log.info("Could not look up the AsBuiltReport.Core release: %s", error)
            _cached = ""
    if _cached:
        extra["core_version"] = _cached
    return config
