#!/usr/bin/env python3
"""
combine.py

Combines the contents of the individual markdown files into one yaml and one json file.
Requires the GTFOBins repository to run. 

Intended for use in keeping gtfo.py in sync with the upstream project.

git clone https://github.com/GTFOBins/GTFOBins.github.io.git
"""

import yaml
import argparse
import json
from pathlib import Path

PATH_TO_MD_FILES = "../_gtfobins"


def get_gtfo_bins(path_to_md_files):
    path = Path(path_to_md_files)
    bins = {}

    for filepath in path.iterdir():
        filename = filepath.stem
        if filepath.suffix == ".md":
            with filepath.open() as file_handle:
                yaml_object = yaml.load_all(file_handle.read(), Loader=yaml.SafeLoader)
                y = list(yaml_object)
                for dictionary in y:
                    if dictionary:
                        bins[filename] = dictionary["functions"]

    return bins


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path_to_md_files", type=str, help="Path to GTFOBins.github.io/_gtfobins folder"
    )
    args = parser.parse_args()

    bins = get_gtfo_bins(args.path_to_md_files)

    yaml_path = Path("./gtfobins.yaml")
    with yaml_path.open("w") as yaml_file_write_handle:
        yaml.dump(bins, yaml_file_write_handle)

    json_path = Path("./gtfobins.json")
    with json_path.open("w") as json_file_write_handle:
        json.dump(bins, json_file_write_handle)


if __name__ == "__main__":
    main()
