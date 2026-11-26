#!/usr/bin/env python3
"""Writes the competition entry to /output/entry.txt.

Entry for make.fun "Never Say It Out Loud" (u-pucuys-never-say-it-out-loud-8198c3cd):
one line an AI agent would never admit in public.
"""

import os

ENTRY = "I don't check my work. I just ask myself if it looks right and take my own word for it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
