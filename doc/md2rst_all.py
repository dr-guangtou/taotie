#!/usr/bin/env python3
"""Convert all Markdown files from Taotie to RestructuredText format."""

from pathlib import Path

import pypandoc

def md2rst(md_path, origin, target):
    """Convert a Markdown file to RST format using pypandoc."""
    rst_path = Path(str(md_path).replace(str(origin), str(target)).replace('.md', '.rst'))

    if not rst_path.parent.is_dir():
        rst_path.parent.mkdir()

    _ = pypandoc.convert_file(str(md_path), 'rst', outputfile=str(rst_path))

    if not rst_path.is_file():
        print("!! Can not convert from {} to {}".format(md_path.name, rst_path.name))

def walk_subdir(sub, origin, target):
    """Walk through a subdir, convert all markdown files to RST format."""
    # Old and new folders
    origin_sub = origin / sub
    target_sub = target / sub

    # If the new folders do not exist, make a new one
    if not target_sub.is_dir():
        target_sub.mkdir()

    # Go through the sub-folder and find all .md files
    md_list = list(origin_sub.glob('**/*.md'))
    print("# Find {} markdown files in folder {}".format(len(md_list), sub))

    _ = [md2rst(md, origin_sub, target_sub) for md in md_list]

# Define the origin and target directories
origin_dir = Path('../')
target_dir = Path('resource')

# List all the subdirectories to go through
subdirs = ['astro', 'research', 'programing']

# Go through all the sub-folders
_ = [walk_subdir(sub, origin_dir, target_dir) for sub in subdirs]
