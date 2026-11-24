#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — one original line of plain
text, an alien tourist's review of planet Earth."""

import os

ENTRY = "Fascinating planet. The locals wear a box that counts their steps, then walk in circles at midnight to make the box happy. 4/5, would walk again."

OUT_PATH = "/output/entry.txt"

# Tropes the judge brief warns against (traffic, gravity, money, weather) plus
# the ones already flooding this field's feed (glowing rectangles, bean water,
# pet-waste bags): a line leaning on any of them loses on originality.
CLICHE_WORDS = (
    "traffic", "gravity", "money", "weather",
    "glowing rectangle", "bean water", "pet waste", "scoop",
)


def validate(text):
    """Gate plus originality and review-shape checks; raises on any failure."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.isspace() or "\n" in text:
        raise ValueError("entry must be a single non-blank line")
    if text != text.strip() or "  " in text:
        raise ValueError("entry must not have leading/trailing whitespace or double spaces")
    lowered = text.lower()
    for word in CLICHE_WORDS:
        if word in lowered:
            raise ValueError(f"entry leans on an overused trope: {word!r}")
    # A real tourist review carries a verdict: a rating or a closing remark.
    if not any(marker in text for marker in ("/5", "stars", "would")):
        raise ValueError("entry reads as no review: no rating or closing remark")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
