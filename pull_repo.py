#!/usr/bin/env python3
"""
🔄 Pyto iOS Repository Sync Script
Downloads and synchronizes the latest code from GitHub into local storage on iPhone.
"""

import os
import shutil
import urllib.request
import zipfile

GITHUB_USER = "a360n"
GITHUB_REPO = "IOSPytoTesy"
BRANCH = "main"

ZIP_URL = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/archive/refs/heads/{BRANCH}.zip"
TARGET_DIR = GITHUB_REPO


def sync_repository(token: str = None):
    zip_temp = "repo_archive.zip"
    extract_temp = "temp_extracted"

    print(f"🔄 Pulling latest updates from: {GITHUB_USER}/{GITHUB_REPO} ({BRANCH})...")

    try:
        req = urllib.request.Request(
            ZIP_URL,
            headers={
                "User-Agent": "Pyto-iOS-Sync",
                **({"Authorization": f"token {token}"} if token else {}),
            },
        )

        with (
            urllib.request.urlopen(req) as response,
            open(zip_temp, "wb") as out_file,
        ):
            shutil.copyfileobj(response, out_file)
        print("📦 Download complete. Extracting and updating files...")

        with zipfile.ZipFile(zip_temp, "r") as zip_ref:
            zip_ref.extractall(extract_temp)

        inner_folder = os.path.join(extract_temp, f"{GITHUB_REPO}-{BRANCH}")

        if os.path.exists(TARGET_DIR):
            shutil.rmtree(TARGET_DIR)
        shutil.move(inner_folder, TARGET_DIR)

        if os.path.exists(zip_temp):
            os.remove(zip_temp)
        if os.path.exists(extract_temp):
            shutil.rmtree(extract_temp)

        print(f"✨ Folder '{TARGET_DIR}' updated successfully!")
        print(f"📂 Current directory contents: {os.listdir(TARGET_DIR)}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ Error 404: Check branch name or verify if repository is Private.")
            print("💡 If private, pass a Personal Access Token: sync_repository('YOUR_TOKEN')")
        else:
            print(f"❌ Connection error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    sync_repository()