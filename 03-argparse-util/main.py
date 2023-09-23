# main.py
from dataclasses import asdict
import argparse
import handler_vendor
import mlspace_client


def main():
    parser = argparse.ArgumentParser(description="Utility functions")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Vendor handler
    handler_vendor.add_parser_handler_get_vendor(subparsers)
    handler_vendor.add_parser_handler_post_vendor(subparsers)

    args = parser.parse_args()

    req = {}
    if hasattr(args, "func"):
        req = args.func(args)
    else:
        parser.print_help()

    mlspace_client.request(asdict(req))


if __name__ == "__main__":
    main()
