import argparse

def handler_get_vendor(args):
    print(f"get vendor!")

def handler_post_vendor(args):
    vendor_name = args.vendor_name if args.vendor_name else "DefaultVendor"
    print(f"post vendor with name: {vendor_name}")

def main():
    parser = argparse.ArgumentParser(description="Utility functions")

    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # GET Vendor command
    get_vendor = subparsers.add_parser("get_vendor", aliases=["00"], help="GET vendors")
    get_vendor.set_defaults(func=handler_get_vendor)

    # POST Vendor command
    post_vendor = subparsers.add_parser("post_vendor", aliases=["01"], help="POST vendors")
    post_vendor.add_argument("vendor_name", type=str, nargs='?', default=None, help="Vendor name to post (optional)")
    post_vendor.set_defaults(func=handler_post_vendor)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
