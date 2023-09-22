# main.py
import argparse
import handler_vendor


def main():
    parser = argparse.ArgumentParser(description="Utility functions")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Vendor handler
    handler_vendor.add_parser_handler_get_vendor(subparsers)
    handler_vendor.add_parser_handler_post_vendor(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
