#!/usr/bin/env python3
"""List uploads from an ARKCloud logged-in client session."""

from __future__ import annotations

import argparse
import os

from arkcloud_common import base_url, endpoint, fail, print_json, request_json


def main() -> None:
    parser = argparse.ArgumentParser(description="List ARKCloud IPFS uploads.")
    parser.add_argument("--base-url", default=None, help="ARKCloud base URL")
    args = parser.parse_args()

    cookie = os.environ.get("ARKCLOUD_CLIENT_COOKIE")
    if not cookie:
        fail("Listing uploads requires ARKCLOUD_CLIENT_COOKIE from a logged-in client session")

    payload = request_json(
        "GET",
        endpoint(base_url(args.base_url), "/api/client/uploads"),
        headers={"Cookie": cookie},
    )
    print_json({"ok": True, "uploads": payload})


if __name__ == "__main__":
    main()

