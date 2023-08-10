#!/usr/bin/env python
from argparse import ArgumentParser
from crossref.argument_checkers import (
    select_opts,
    works_sort_opts,
    works_query_fields_type,
    works_facets_type,
    works_filter_type,
    funders_filter_type,
)
from crossref.command_handlers import (
    get_citations,
    get_funder,
    get_journal,
    get_member,
    get_prefix,
    get_type,
    get_work,
    list_funders,
    list_journals,
    list_licenses,
    list_members,
    list_types,
    search_works,
)


def usage(args):
    """Print Usage."""
    return args.help_func()


def epilog(*args, **kwargs):
    """Return Epilog."""
    author = "Tralah M Brian (TralahM) " + "<briantralah@gmail.com>"
    github = "https://github.com/TralahM/academic_citations"
    return f"""Author:  {author}. Project:  <{github}>"""


def main():
    """Main CLI EntryPoint."""
    parser = ArgumentParser(
        epilog=epilog(),
    )

    parser.set_defaults(
        func=usage,
        parser=parser,
        help_func=parser.print_help,
    )

    parser.add_argument(
        "--mailto",
        dest="mailto",
        default=None,
        help="mailto address for polite users",
        type=str,
    )

    parser.add_argument(
        "--auth-token",
        dest="auth_token",
        default=None,
        help="auth token for authenticated (Plus) users",
        type=str,
    )

    parser.add_argument(
        "--api-version",
        dest="api_version",
        default="v1",
        help="API version to use (default=v1)",
        type=str,
    )

    parser.add_argument(
        "-o",
        dest="outfile",
        default=None,
        help="Json filename to also store the output",
        type=str,
    )

    parser.add_argument(
        "--rows",
        dest="rows",
        default=20,
        help="Number of Rows to return (default=20)",
        type=int,
    )

    parser.add_argument(
        "--format-on",
        action="store_true",
        dest="format_on",
        default=False,
        help="Format json output using pygments syntax highlighting?",
    )

    mutexg = parser.add_mutually_exclusive_group(
        required=False,
    )

    mutexg.add_argument(
        "--sample",
        action="store",
        default=None,
        dest="sample",
        type=int,
        help="Sample size",
    )

    mutexg.add_argument(
        "--offset",
        action="store",
        default=None,
        dest="offset",
        type=int,
        help="Offset",
    )

    mutexg.add_argument(
        "--cursor",
        action="store",
        default=None,
        dest="cursor",
        type=str,
        help="Cursor parameter",
    )

    subparsers = parser.add_subparsers(
        title="commands",
    )

    pub_parser = subparsers.add_parser(
        "pubs",
        help=search_works.__doc__,
        aliases=[
            "works",
            "publications",
            "w",
            "p",
        ],
    )

    srch_parsers = pub_parser.add_subparsers(
        title="commands",
    )

    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Publication DOI",
        aliases=["details", "info"],
    )

    srch_parser.add_argument(
        "doi",
        action="store",
        help="DOI id to get details for",
    )

    srch_parser.set_defaults(
        func=get_work,
    )

    pub_parser.add_argument(
        "--select",
        action="store",
        dest="select",
        default=[],
        nargs="*",
        choices=select_opts,
        type=str,
        help="Subset of Elements to select if unspecified all elements are returned",
    )

    pub_parser.add_argument(
        "-x",
        "--exclude",
        action="store",
        dest="exclude",
        default=[],
        nargs="*",
        choices=select_opts,
        type=str,
        help="Subset of Elements to exclude if unspecified all elements are returned",
    )

    pub_parser.add_argument(
        "-q",
        "--query",
        action="store",
        dest="query",
        default=None,
        type=str,
        help="search query",
    )

    pub_parser.add_argument(
        "-qf",
        "--query-fields",
        action="store",
        dest="query_fields",
        default=[],
        nargs="*",
        help="search using query fields",
        type=works_query_fields_type,
    )

    pub_parser.add_argument(
        "-s",
        "--sortby",
        action="store",
        dest="sortby",
        default=None,
        type=str,
        choices=works_sort_opts,
        help="Sort by element",
    )

    pub_parser.add_argument(
        "-o",
        "--order",
        action="store",
        dest="order",
        default="desc",
        type=str,
        help="Sort Order",
        choices=["asc", "desc"],
    )

    pub_parser.add_argument(
        "-f",
        "--filters",
        action="store",
        dest="filters",
        nargs="*",
        default=[],
        type=works_filter_type,
        help="Filters Fields Queries",
    )

    pub_parser.add_argument(
        "-fs",
        "--facets",
        action="store",
        dest="facets",
        default=[],
        nargs="*",
        type=works_facets_type,
        help="Facets Fields Queries",
    )

    pub_parser.set_defaults(
        func=search_works,
        help=search_works.__doc__,
    )

    journals_parser = subparsers.add_parser(
        "journals",
        help=list_journals.__doc__,
        aliases=["journal", "jnl", "j"],
    )

    srch_parsers = journals_parser.add_subparsers(
        title="commands",
    )

    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Journal ISSN",
        aliases=["details", "info", "issn"],
    )

    srch_parser.add_argument(
        "id",
        action="store",
        help="ISSN id to get details for",
    )

    srch_parser.set_defaults(
        func=get_journal,
    )

    journals_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        default=True,
        help="List all",
    )

    journals_parser.set_defaults(
        func=list_journals,
        help=list_journals.__doc__,
    )

    members_parser = subparsers.add_parser(
        "members",
        help=list_members.__doc__,
        aliases=["member", "m"],
    )

    srch_parsers = members_parser.add_subparsers(
        title="commands",
    )

    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Member ID",
        aliases=["details", "info", "id"],
    )

    srch_parser.add_argument(
        "id",
        action="store",
        help="Member id to get details for",
    )

    srch_parser.set_defaults(
        func=get_member,
    )

    members_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        default=True,
        help="List all",
    )

    members_parser.set_defaults(
        func=list_members,
        help=list_members.__doc__,
    )

    funders_parser = subparsers.add_parser(
        "funders",
        help=list_funders.__doc__,
        aliases=["funder", "f"],
    )

    srch_parsers = funders_parser.add_subparsers(
        title="commands",
    )

    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Funders ID",
        aliases=["details", "info", "id"],
    )

    srch_parser.add_argument(
        "id",
        action="store",
        help="Funder id to get details for",
    )

    srch_parser.set_defaults(
        func=get_funder,
    )

    funders_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        default=True,
        help="List all",
    )

    funders_parser.add_argument(
        "-q",
        "--query",
        action="store",
        dest="query",
        default="",
        type=str,
        help="search query",
    )

    funders_parser.add_argument(
        "--filters",
        action="store",
        dest="filters",
        type=funders_filter_type,
        help="Filters Fields Queries",
    )

    funders_parser.set_defaults(
        func=list_funders,
        help=list_funders.__doc__,
    )

    types_parser = subparsers.add_parser(
        "types",
        help=list_types.__doc__,
        aliases=["type", "t"],
    )

    types_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        default=True,
        help="List all",
    )

    srch_parsers = types_parser.add_subparsers(
        title="commands",
    )

    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Type ID",
        aliases=["details", "info", "id"],
    )

    srch_parser.add_argument(
        "id",
        action="store",
        help="Type ID",
    )

    srch_parser.set_defaults(
        func=get_type,
    )

    types_parser.set_defaults(
        func=list_types,
        help=list_types.__doc__,
    )

    licenses_parser = subparsers.add_parser(
        "licenses",
        help=list_licenses.__doc__,
        aliases=["license", "lc", "lcs"],
    )

    licenses_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        default=True,
        help="List all",
    )

    licenses_parser.add_argument(
        "-q",
        "--query",
        action="store",
        dest="query",
        default=None,
        type=str,
        help="search query",
    )

    licenses_parser.set_defaults(
        func=list_licenses,
        help=list_licenses.__doc__,
    )

    cite_parser = subparsers.add_parser(
        "cite",
        help=get_citations.__doc__,
        aliases=[
            "citation",
            "citations",
            "ref",
            "refs",
            "reference",
            "references",
        ],
    )

    cite_parser.add_argument(
        "style",
        help="Citation Styles to Return. defaults(apa, bibtex, mla).",
        nargs="*",
        default=["apa", "bibtex", "mla"],
    )

    cite_parser.add_argument(
        "doi",
        help="DOI of the document to search for.",
    )

    cite_parser.set_defaults(func=get_citations)

    prefix_parser = subparsers.add_parser(
        "prefix",
        help=list_types.__doc__,
        aliases=["pre", "px"],
    )

    prefix_parser.add_argument(
        "id",
        action="store",
        help="Prefix DOI owner prefix e.g 10.1016",
    )

    prefix_parser.set_defaults(
        func=get_prefix,
    )

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
