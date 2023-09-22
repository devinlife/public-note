# GET vendor
def handler_get_vendor(_):
    print("get vendor!")


def add_parser_handler_get_vendor(subparsers):
    parser = subparsers.add_parser("get_vendor", aliases=["00"], help="GET vendors")
    parser.set_defaults(func=handler_get_vendor)


# POST vendor
def handler_post_vendor(args):
    vendor_name = args.vendor_name if args.vendor_name else "DefaultVendor"
    print(f"post vendor with name: {vendor_name}")


def add_parser_handler_post_vendor(subparsers):
    parser = subparsers.add_parser("post_vendor", aliases=["01"], help="POST vendors")
    parser.add_argument("vendor_name", type=str, nargs="?", default=None, help="Vendor name to post (optional)")
    parser.set_defaults(func=handler_post_vendor)
