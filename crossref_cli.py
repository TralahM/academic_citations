#!/usr/bin/env python
from crossref import CrossRefAPIClient
from argparse import ArgumentParser
import json

select_opts = [
    "DOI",
    "ISBN",
    "ISSN",
    "URL",
    "abstract",
    "accepted",
    "alternative-id",
    "approved",
    "archive",
    "article-number",
    "assertion",
    "author",
    "chair",
    "clinical-trial-number",
    "container-title",
    "content-created",
    "content-domain",
    "created",
    "degree",
    "deposited",
    "editor",
    "event",
    "funder",
    "group-title",
    "indexed",
    "is-referenced-by-count",
    "issn-type",
    "issue",
    "issued",
    "license",
    "link",
    "member",
    "original-title",
    "page",
    "posted",
    "prefix",
    "published",
    "published-online",
    "published-print",
    "publisher",
    "publisher-location",
    "reference",
    "references-count",
    "relation",
    "score",
    "short-container-title",
    "short-title",
    "standards-body",
    "subject",
    "subtitle",
    "title",
    "translator",
    "type",
    "update-policy",
    "update-to",
    "updated-by",
    "volume",
]


def epilog(*args, **kwargs):
    """Return Epilog."""
    author = "Tralah M Brian (TralahM) " + "<briantralah@gmail.com>"
    github = "https://github.com/TralahM/academic_citations"
    return f"""Author:  {author}. Project:  <{github}>"""


def get_citation(args):
    """
    Get Citation/ Reference Text In the Specified Style (apa, mla, bibtex, etc).
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_work_reference(args.doi, args.style).text
    print(res)
    pass


def search_works(args):
    """
    Returns a list of all works (journal articles, conference proceedings, books, components, etc), 20 per page.

    Queries:
    Sort:
    Facets:
    Filters:
    Elements:
    Pagination with offsets:
    Deep paging:
    Sample:
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    params = {
        "query": args.query,
        "rows": args.rows,
    }
    if len(args.select) > 0:
        params.update(
            {
                "select": ",".join(args.select),
            }
        )
    res = client.get_works(params).json()
    print(json.dumps(res))
    pass


def get_work(args):
    """doi."""
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_work(
        doi=args.doi,
    ).json()
    print(json.dumps(res))
    pass


def list_journals(args):
    """
    Queries
    Pagination with offsets
    Deep paging
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_journals(
        {
            "query": args.query,
            "rows": args.rows,
        }
    ).json()
    print(json.dumps(res))
    pass


def get_journal(args):
    """issn."""
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_journal(
        issn=args.id,
    ).json()
    print(json.dumps(res))
    pass


def list_members(args):
    """
    Queries:

    Filters:

    Pagination with offsets:

    Deep paging:
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_members(
        {
            "query": args.query,
            "rows": args.rows,
        }
    ).json()
    print(json.dumps(res))
    pass


def get_member(args):
    """
    id.
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_member(
        member_id=args.id,
    ).json()
    print(json.dumps(res))
    pass


def list_funders(args):
    """
    Queries:

    Filters:
        - location - funders located in given country

    Pagination with offsets:

    Deep Paging:
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_funders(
        {
            "query": args.query,
            "rows": args.rows,
        }
    ).json()
    print(json.dumps(res))
    pass


def get_funder(args):
    """
    Id.
    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_funder(
        funder_id=args.id,
    ).json()
    print(json.dumps(res))
    pass


def list_licenses(args):
    """
    Queries
    Pagination with offsets
    Deep paging

    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_licenses(
        {
            "rows": args.rows,
        }
    ).json()
    print(json.dumps(res))
    pass


def list_types(args):
    """
    Pagination with offsets.

    """
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_types(
        {
            "rows": args.rows,
        }
    ).json()
    print(json.dumps(res))
    pass


def get_type(args):
    """id."""
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    res = client.get_type(
        type_id=args.id,
    ).json()
    print(json.dumps(res))
    pass


def usage(args):
    return epilog()


def main():
    parser = ArgumentParser(
        epilog=epilog(),
    )
    parser.set_defaults(
        func=usage,
        parser=parser,
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
        "--rows",
        dest="rows",
        default=20,
        help="Number of Rows to return",
        type=int,
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
        title="subcommands",
    )
    pub_parser = subparsers.add_parser(
        "pubs",
        help=search_works.__doc__,
    )
    srch_parsers = pub_parser.add_subparsers(
        title="commands",
    )
    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Publication DOI",
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
        default=None,
        nargs="*",
        choices=select_opts,
        type=str,
        help="Subset of Elements to select",
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
        "--sortby",
        action="store",
        dest="sortby",
        default=None,
        type=str,
        help="Sort by element",
    )
    pub_parser.add_argument(
        "--sortorder",
        action="store",
        dest="sortorder",
        default="desc",
        type=str,
        help="Sort Order",
        choices=["asc", "desc"],
    )
    pub_parser.add_argument(
        "--filters",
        action="store",
        dest="filters",
        nargs="?",
        type=str,
        help="Filters",
    )
    pub_parser.add_argument(
        "--facets",
        action="store",
        dest="facets",
        default=None,
        type=str,
        help="Facets",
    )
    pub_parser.set_defaults(
        func=search_works,
        help=search_works.__doc__,
    )

    journals_parser = subparsers.add_parser(
        "journals",
        help=list_journals.__doc__,
    )
    srch_parsers = journals_parser.add_subparsers(
        title="commands",
    )
    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Journal ISSN",
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
    )
    srch_parsers = members_parser.add_subparsers(
        title="commands",
    )
    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Member ID",
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
    )
    srch_parsers = funders_parser.add_subparsers(
        title="commands",
    )
    srch_parser = srch_parsers.add_parser(
        "get",
        help="Get Details for this Funders ID",
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
    funders_parser.set_defaults(
        func=list_funders,
        help=list_funders.__doc__,
    )

    types_parser = subparsers.add_parser(
        "types",
        help=list_types.__doc__,
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
        help="Get Details for this Type",
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
    )
    licenses_parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        default=True,
        help="List all",
    )
    licenses_parser.set_defaults(
        func=list_licenses,
        help=list_licenses.__doc__,
    )

    cite_parser = subparsers.add_parser(
        "cite",
        help=get_citation.__doc__,
    )
    cite_parser.add_argument(
        "doi",
        help="DOI of the document to search for.",
    )
    cite_parser.add_argument(
        "style",
        help="Citation Style to Return.",
        choices=["apa", "bibtex", "mla"],
    )
    cite_parser.set_defaults(func=get_citation)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
