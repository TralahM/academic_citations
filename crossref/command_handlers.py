import json
from utils import (
    print_colored_json,
)
from __init__ import (
    create_api_client,
)
from argument_parsers import (
    parse_exclude_args,
    parse_facet_args,
    parse_filter_args,
    parse_query_field_args,
    parse_select_args,
    parse_sort_args,
    parse_pagination_args,
)


def get_citations(args):
    """Get Citation/ Reference Text of the given DOI In the Specified Style
    (apa, mla, bibtex, etc).
    """
    client = create_api_client(args)
    citations = {}
    for style in args.style:
        res = client.get_work_reference(args.doi, style)
        res = res.content.decode()
        citations[style] = res.strip()
    print_colored_json(
        json.dumps(citations, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def search_works(args):
    """Interact with the Works API. Supports the following parameters:

    - Queries: (query) and (query.field(s))

    - Filters: (filter=type-name:filter)(s) or dot filters (filter=type-name.field-name:filter)(s)

    - Pagination with offsets: (offset) and (rows)

    - Deep paging: (cursor=*) initially and (cursor=next-cursor) in subsequent requests

    - Elements: (select=field-name(s))

    - Sort: (sort) and (order)

    - Facets: (facet=type-name:*)

    - Sample: (sample)

    And returns a list of works (journal articles, conference proceedings,
    books, components, etc), or a single work (if you specify a DOI).
    """
    client = create_api_client(args)

    params = {
        "query": args.query,
        "rows": args.rows,
    }
    pagination_args = parse_pagination_args(args)
    params.update(pagination_args)
    sort_args = parse_sort_args(args)
    params.update(sort_args)
    filter_args = parse_filter_args(args)
    params.update(filter_args)
    facet_args = parse_facet_args(args)
    params.update(facet_args)
    query_field_args = parse_query_field_args(args)
    params.update(query_field_args)
    select_args = parse_select_args(args)
    params.update(select_args)
    exclude_args = parse_exclude_args(args)
    params.update(exclude_args)
    res = client.get_works(params).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def get_work(args):
    """doi."""
    client = create_api_client(args)
    res = client.get_work(
        doi=args.doi,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def list_journals(args):
    """Interact with the Journals API. Supports the following parameters:
    - Queries: (query) and (query.field(s))

    - Pagination with offsets: (offset) and (rows)

    - Deep paging: (cursor=*) initially and (cursor=next-cursor) in subsequent requests
    """
    client = create_api_client(args)
    params = {
        "query": args.query,
        "rows": args.rows,
    }
    pagination_args = parse_pagination_args(args)
    params.update(pagination_args)
    res = client.get_journals(
        params,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def get_journal(args):
    """issn."""
    client = create_api_client(args)
    res = client.get_journal(
        issn=args.id,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def list_members(args):
    """Interact with the Members API. Supports the following parameters:
    - Queries: (query) and (query.field(s))

    - Pagination with offsets: (offset) and (rows)

    - Deep paging: (cursor=*) initially and (cursor=next-cursor) in subsequent requests

    - Filters: (filter=type-name:filter)(s) or dot filters (filter=type-name.field-name:filter)(s)
    """
    client = create_api_client(args)
    params = {
        "query": args.query,
        "rows": args.rows,
    }
    pagination_args = parse_pagination_args(args)
    params.update(pagination_args)
    res = client.get_members(
        params,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def get_member(args):
    """
    id.
    """
    client = create_api_client(args)
    res = client.get_member(
        member_id=args.id,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def list_funders(args):
    """Interact with the Funders API. Supports the following parameters:
    - Queries: (query) and (query.field(s))

    - Pagination with offsets: (offset) and (rows)

    - Deep paging: (cursor=*) initially and (cursor=next-cursor) in subsequent requests

    - Filters: (filter=location:filter)
        - location = funders located in given country
    """
    client = create_api_client(args)
    params = {
        "query": args.query,
        "rows": args.rows,
    }
    pagination_args = parse_pagination_args(args)
    params.update(pagination_args)
    filter_args = parse_filter_args(args)
    params.update(filter_args)
    res = client.get_funders(
        params,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def get_funder(args):
    """
    Id.
    """
    client = create_api_client(args)
    res = client.get_funder(
        funder_id=args.id,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def list_licenses(args):
    """Interact with the Licenses API. Supports the following parameters:
    - Queries: (query) and (query.field(s))

    - Pagination with offsets: (offset) and (rows)

    - Deep paging: (cursor=*) initially and (cursor=next-cursor) in subsequent requests
    """
    client = create_api_client(args)
    if args.query is None:
        args.query = ""
    params = {
        "query": args.query,
        "rows": args.rows,
    }
    pagination_args = parse_pagination_args(args)
    params.update(pagination_args)
    res = client.get_licenses(
        params,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def list_types(args):
    """Interact with the Types API. Supports the following parameters:

    - Pagination with offsets: (offset) and (rows)
    """
    client = create_api_client(args)
    params = {
        "query": args.query,
        "rows": args.rows,
    }
    pagination_args = parse_pagination_args(args)
    params.update(pagination_args)
    res = client.get_types(
        params,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def get_type(args):
    """id."""
    client = create_api_client(args)
    res = client.get_type(
        type_id=args.id,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass


def get_prefix(args):
    """id which is the doi_prefix."""
    client = create_api_client(args)
    res = client.get_prefix_metadata(
        prefix_id=args.id,
    ).json()
    print_colored_json(
        json.dumps(res, indent=2, sort_keys=True),
        format_on=args.format_on,
    )
    pass
