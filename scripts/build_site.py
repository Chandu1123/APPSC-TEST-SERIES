#!/usr/bin/env python3
"""
GitHub Pages Website Builder for APPSC Group-I & Group-II Test Series
=====================================================================
1. Runs generate_test_series.py (32 core APPSC Group 1 & Group 2 exams)
2. Runs pib_scraper.py (Live PIB & Government Portal exam generator)
3. Generates data/tests_db.js so the GitHub Pages website (and local index.html)
   loads all 33+ exams & 1,830+ explained questions instantaneously.
"""

import json
import os
import shutil
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def build_website():
    os.makedirs(DATA_DIR, exist_ok=True)

    print("[1/3] Generating 32 APPSC Group-I & Group-II Exam Test Series...")
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "generate_test_series.py")], check=True)

    print("[2/3] Running Live PIB (pib.gov.in) & Govt Portal Scraper...")
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "pib_scraper.py"), "--questions", "30"], check=True)

    db_json_path = os.path.join(DATA_DIR, "tests_db.json")
    db_js_path = os.path.join(DATA_DIR, "tests_db.js")

    print("[3/3] Building data/tests_db.js bundle for GitHub Pages website...")
    with open(db_json_path, "r", encoding="utf-8") as f:
        raw_json = f.read()

    with open(db_js_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated APPSC Group 1 & Group 2 Test Series Database (33+ Exams)\n")
        f.write("window.APPSC_TESTS_DB = ")
        f.write(raw_json)
        f.write(";\n")

    # Remove old .exe / C# build artifacts if present so the GitHub Website repo is clean and fast
    for old_folder in ["dist", "build_tmp", "src"]:
        p = os.path.join(BASE_DIR, old_folder)
        if os.path.exists(p):
            shutil.rmtree(p, ignore_errors=True)

    print("\n=====================================================================")
    print("GITHUB PAGES WEBSITE READY!")
    print(f"• Main Entry Point : {os.path.join(BASE_DIR, 'index.html')}")
    print(f"• JS Database      : {db_js_path}")
    print(f"• JSON Database    : {db_json_path}")
    print("=====================================================================")


if __name__ == "__main__":
    build_website()
