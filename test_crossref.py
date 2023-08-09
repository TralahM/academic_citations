#!/usr/bin/env python

from crossref import *
from argparse import ArgumentParser
from pprint import pprint as pp
import json

test_issns = [
    "0360-4012",
    "1097-4547",
    "0364-5134",
    "1099-0739",
]

citation_styles = [
    "bibtex",
    "apa",
    "mla",
]

test_member_ids = [
    1,
    2,
    3,
]

test_prefixes = [
    "10.15530",
    "10.1306",
    "10.1119",
]

test_types = [
    "journal-article",
    "book",
    "standard",
    "monograph",
]

test_funder_ids = [
    "100000001",
    "100000005",
    "100000003",
]

test_dois = [
    "10.5621/sciefictstud.40.2.0382",
    "10.1093/ww/9780199540884.013.u52741",
    "10.1007/978-981-19-8692-5_3",
]


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--lw",
        dest="lw",
        action="store_true",
        default=False,
        help="test list works",
    )
    parser.add_argument(
        "--lf",
        dest="lf",
        action="store_true",
        default=False,
        help="test list funders",
    )
    parser.add_argument(
        "--lj",
        dest="lj",
        action="store_true",
        default=False,
        help="test list journals",
    )
    parser.add_argument(
        "--lm",
        dest="lm",
        action="store_true",
        default=False,
        help="test list members",
    )
    parser.add_argument(
        "--lt",
        dest="lt",
        action="store_true",
        default=False,
        help="test list types",
    )
    parser.add_argument(
        "--ll",
        dest="ll",
        action="store_true",
        default=False,
        help="test list licenses",
    )
    parser.add_argument(
        "--tw",
        dest="tw",
        action="store_true",
        default=False,
        help="test work",
    )
    parser.add_argument(
        "--twr",
        dest="twr",
        action="store_true",
        default=False,
        help="test work references",
    )
    parser.add_argument(
        "--tf",
        dest="tf",
        action="store_true",
        default=False,
        help="test funder",
    )
    parser.add_argument(
        "--tfw",
        dest="tfw",
        action="store_true",
        default=False,
        help="test funder works",
    )
    parser.add_argument(
        "--tj",
        dest="tj",
        action="store_true",
        default=False,
        help="test journal",
    )
    parser.add_argument(
        "--tjw",
        dest="tjw",
        action="store_true",
        default=False,
        help="test journal works",
    )
    parser.add_argument(
        "--tm",
        dest="tm",
        action="store_true",
        default=False,
        help="test member",
    )
    parser.add_argument(
        "--tmw",
        dest="tmw",
        action="store_true",
        default=False,
        help="test member works",
    )
    parser.add_argument(
        "--tt",
        dest="tt",
        action="store_true",
        default=False,
        help="test type",
    )
    parser.add_argument(
        "--ttw",
        dest="ttw",
        action="store_true",
        default=False,
        help="test type works",
    )
    parser.add_argument(
        "--tp",
        dest="tp",
        action="store_true",
        default=False,
        help="test prefix",
    )
    parser.add_argument(
        "--tpw",
        dest="tpw",
        action="store_true",
        default=False,
        help="test prefix works",
    )
    parser.add_argument(
        "--search",
        dest="search",
        action="store_true",
        default=False,
        help="search for a query",
    )
    parser.add_argument(
        "-q",
        dest="query",
        action="store",
        default="",
        help="query term",
    )
    parser.add_argument(
        "-r",
        dest="rows",
        action="store",
        default=2,
        type=int,
        help="Number of rows",
    )

    client = CrossRefAPIClient(
        api_mailto=None,
    )
    args = parser.parse_args()

    if args.lw:
        works = client.get_works(
            {
                "rows": args.rows,
                "query": args.query,
            }
        )
        print(json.dumps(works.json()))

    if args.lf:
        funders = client.get_funders(
            {
                "rows": args.rows,
            }
        )
        pp(funders.json())

    if args.lj:
        journals = client.get_journals(
            {
                "rows": args.rows,
            }
        )
        pp(journals.json())

    if args.lm:
        members = client.get_members(
            {
                "rows": args.rows,
            }
        )
        pp(members.json())

    if args.lt:
        types = client.get_types(
            {
                "rows": args.rows,
            }
        )
        pp(types.json())

    if args.ll:
        licenses = client.get_licenses(
            {
                "rows": args.rows,
            }
        )
        pp(licenses.json())

    if args.tw:
        print("===" * 21)
        for doi in test_dois:
            pp(client.get_work(doi).json())
            print()
            print("===" * 21)

    if args.twr:
        for doi in test_dois:
            print("---" * 21)
            for style in citation_styles:
                print(f"Style: {style} :")
                print(str(client.get_work_reference(doi, style).text))
                print()
            print("---" * 21)

    if args.tj:
        for issn in test_issns:
            pp(client.get_journal(issn).json())
            print()
            print("===" * 21)

    if args.tjw:
        for issn in test_issns:
            pp(client.get_journal_works(issn, {"rows": 2}).json())
            print()
            print("===" * 21)

    if args.tf:
        for funder_id in test_funder_ids:
            pp(client.get_funder(funder_id).json())
            print()
            print("===" * 21)

    if args.tfw:
        for funder_id in test_funder_ids:
            pp(client.get_funder_works(funder_id, {"rows": 2}).json())
            print()
            print("===" * 21)

    if args.tm:
        for member_id in test_member_ids:
            pp(client.get_member(member_id).json())
            print()
            print("===" * 21)

    if args.tmw:
        for member_id in test_member_ids:
            pp(client.get_member_works(member_id, {"rows": 2}).json())
            print()
            print("===" * 21)

    if args.tt:
        for type_id in test_types:
            pp(client.get_type(type_id).json())
            print()
            print("===" * 21)

    if args.ttw:
        for type_id in test_types:
            pp(client.get_type_works(type_id, {"rows": 2}).json())
            print()
            print("===" * 21)

    if args.tp:
        for prefix_id in test_prefixes:
            pp(client.get_prefix_metadata(prefix_id).json())
            print()
            print("===" * 21)

    if args.tpw:
        for prefix_id in test_prefixes:
            pp(client.get_prefix_works(prefix_id, {"rows": 2}).json())
            print()
            print("===" * 21)

    if args.search:
        results = client.get_works({"rows": 5, "query": args.query}).json()
        for result in results.get("message", {}).get("items", []):
            pp(result)


if __name__ == "__main__":
    main()
