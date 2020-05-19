#!/usr/bin/env python3
"""
gtfo.py

usage: 
python3 gtfo.py [--function={suid...}] name
e.g. 
python3 gtfo.py --function=sudo vim
"""
import yaml
import argparse
from pathlib import Path

GREEN_START = "\033[0;32m"
CYAN_START = "\033[1;36m"
RESET = "\033[0;0m"

CURRRENT_FILE_DIR = Path(__file__).resolve().parent


def _print_green(text):
    print(f"{GREEN_START}{text}{RESET}")


def _print_cyan(text):
    print(f"{CYAN_START}{text}{RESET}")


def _print_details(function_name, blob):
    _print_cyan(function_name)
    for items in blob:
        if "description" in items:
            print(items["description"])
        if "code" in items:
            _print_green("\t" + items["code"].replace("\n", "\n\t"))


def load_bins():
    path = Path(CURRRENT_FILE_DIR / "data" / "gtfobins.yaml")
    with path.open() as file_handle:
        yaml_object = yaml.load_all(file_handle.read(), Loader=yaml.SafeLoader)
        bins = list(yaml_object)[0]
    return bins


def search(search_term, gtfo_bins, function=None):
    keyword = search_term.lower()
    if keyword in gtfo_bins:
        gtfo_bin = gtfo_bins[keyword]
        if function:
            for function_name, blob in gtfo_bin.items():
                if function_name.lower() == function.lower():
                    _print_details(function_name, blob)
        else:
            for function_name, blob in gtfo_bin.items():
                _print_details(function_name, blob)

                # Add some spacing between functions
                print("")
    else:
        print(f"Not found: {search_term}")


def main():
    gtfo_functions = [
        "shell",
        "command",
        "reverse-shell",
        "non-interactive-reverse-shell",
        "bind-shell",
        "non-interactive-bind-shell",
        "file-upload",
        "file-download",
        "file-write",
        "file-read",
        "library-load",
        "suid",
        "sudo",
        "capabilities",
        "limited-suid",
    ]

    gtfo_bins = load_bins()
    binary_names = gtfo_bins.keys()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "name", type=str, choices=binary_names, help="name of binary to search for"
    )
    parser.add_argument(
        "-f",
        "--function",
        type=str,
        choices=gtfo_functions,
        help="only output specified function",
    )
    args = parser.parse_args()

    search(args.name, gtfo_bins, args.function)


if __name__ == "__main__":
    main()

