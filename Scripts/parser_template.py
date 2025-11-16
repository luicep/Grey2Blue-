#!/usr/bin/env python3

"""
Simple log parsing template for Grey2Blue.
Adjust the keyword, file name, or add regex as needed.
"""

LOG_FILE = "log.txt"
KEYWORD = "failed"

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if KEYWORD.lower() in line.lower():
            print(line.strip())
