"""Sticky Notes Local — Keep plain-text sticky notes in a folder and list the latest."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='sticky_notes_local',
        description='Keep plain-text sticky notes in a folder and list the latest.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Sticky Notes Local')
    print('Notes that are just files.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
