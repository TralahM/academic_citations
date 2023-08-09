from argument_checkers import select_opts


def parse_sort_args(args):
    """Parse Sort Args."""
    if args.sortby is not None:
        if args.order is None:
            args.order = "asc"
        return {
            "sort": args.sortby,
            "order": args.order,
        }
    else:
        return {}


def parse_select_args(args):
    """Parse Select Args."""
    select = {}
    if args.select is not None:
        if len(args.select) > 0:
            select.update(
                {
                    "select": ",".join(args.select),
                }
            )
    return select


def parse_exclude_args(args):
    """Parse Exclude Args."""
    select = {}
    if args.exclude is not None:
        if len(args.exclude) > 0:
            exclude = args.exclude
            select.update(
                {
                    "select": ",".join([x for x in select_opts if x not in exclude]),
                }
            )
    return select


def parse_query_field_args(args):
    """Parse Query Field Args."""
    query_fields = {}
    if args.query_fields is not None:
        for qf in args.query_fields:
            k, v = tuple(qf.split("="))
            query_fields[k] = v
    return query_fields


def parse_filter_args(args):
    """Parse Filter Args."""
    filters = {}
    if args.filters is not None:
        if len(args.filters) > 0:
            filters.update(
                {
                    "filter": ",".join(args.filters),
                }
            )
    return filters


def parse_facet_args(args):
    """Parse Facet Args."""
    facets = {}
    if args.facets is not None:
        if len(args.facets) > 0:
            facets.update(
                {
                    "facet": ",".join(args.facets),
                }
            )
    return facets


def parse_pagination_args(args):
    """Parse Pagination Args."""
    rows = args.rows if args.rows <= 1000 else 1000
    if args.offset is not None:
        offset = args.offset if args.offset <= 10000 else 10000
        return {
            "offset": offset,
            "rows": rows,
        }
    elif args.cursor is not None:
        return {
            "cursor": args.cursor,
            "rows": rows,
        }
    elif args.sample is not None:
        return {
            "sample": args.sample,
        }
    else:
        return {
            "rows": rows,
        }
