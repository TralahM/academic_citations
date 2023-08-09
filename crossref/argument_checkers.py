import re
import argparse


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

work_filter_choices = [
    "alternative-id",
    "archive",
    "article-number",
    "assertion",
    "assertion-group",
    "award.funder",
    "award.number",
    "category-name",
    "citation-id",
    "clinical-trial-number",
    "container-title",
    "content-domain",
    "doi",
    "from-accepted-date",
    "from-approved-date",
    "from-awarded-date",
    "from-created-date",
    "from-deposit-date",
    "from-event-end-date",
    "from-event-start-date",
    "from-index-date",
    "from-issued-date",
    "from-online-pub-date",
    "from-posted-date",
    "from-print-pub-date",
    "from-pub-date",
    "from-update-date",
    "full-text.type",
    "full-text.application",
    "full-text.version",
    "funder",
    "funder-doi-asserted-by",
    "group-title",
    "gte-award-amount",
    "has-abstract",
    "has-affiliation",
    "has-archive",
    "has-assertion",
    "has-authenticated-orcid",
    "has-award",
    "has-clinical-trial-number",
    "has-content-domain",
    "has-description",
    "has-domain-restriction",
    "has-event",
    "has-full-text",
    "has-funder",
    "has-funder-doi",
    "has-license",
    "has-orcid",
    "has-references",
    "has-relation",
    "has-ror-id",
    "has-update",
    "has-update-policy",
    "is-update",
    "isbn",
    "issn",
    "license.url",
    "license.version",
    "license.delay",
    "lte-award-amount",
    "member",
    "orcid",
    "prefix",
    "relation.type",
    "relation.object-type",
    "relation.object",
    "ror-id",
    "type",
    "type-name",
    "until-accepted-date",
    "until-approved-date",
    "until-awarded-date",
    "until-created-date",
    "until-deposit-date",
    "until-event-end-date",
    "until-event-start-date",
    "until-index-date",
    "until-issued-date",
    "until-online-pub-date",
    "until-posted-date",
    "until-print-pub-date",
    "until-pub-date",
    "until-update-date",
    "update-type",
    "updates",
]

work_facet_choices = [
    "affiliation",
    "archive",
    "assertion",
    "assertion-group",
    "category-name",
    "container-title",
    "funder-doi",
    "funder-name",
    "issn",
    "journal-issue",
    "journal-volume",
    "license",
    "link-application",
    "orcid",
    "published",
    "publisher-name",
    "relation-type",
    "ror-id",
    "source",
    "type-name",
    "update-type",
]

works_query_field_choices = [
    "query.affiliation",
    "query.author",
    "query.bibliographic",
    "query.chair",
    "query.container-title",
    "query.contributor",
    "query.degree",
    "query.description",
    "query.editor",
    "query.event-acronym",
    "query.event-location",
    "query.event-name",
    "query.event-sponsor",
    "query.event-theme",
    "query.funder-name",
    "query.publisher-location",
    "query.publisher-name",
    "query.standards-body-acronym",
    "query.standards-body-name",
    "query.title",
    "query.translator",
]

works_sort_opts = [
    "created",
    "deposited",
    "indexed",
    "is-referenced-by-count",
    "issued",
    "published",
    "published-online",
    "published-print",
    "references-count",
    "relevance",
    "score",
    "updated",
]


def funders_filter_type(arg_val, **kwargs):
    """Validate --filter argument in funders command."""
    pattern = "location:"
    m = re.match(pattern, arg_val)
    if m is None:
        raise argparse.ArgumentTypeError(
            f"Invalid Funders Filter Field {arg_val} Required: {pattern}*",
        )
    return arg_val


def works_query_fields_type(arg_val, **kwargs):
    """Validate --query-filter arguments in pubs or works command."""
    pattern = "=|".join(works_query_field_choices)
    expected = "=\n".join(works_query_field_choices)
    m = re.match(pattern, arg_val)
    if m is None:
        raise argparse.ArgumentTypeError(
            f"Invalid Work Query Field {arg_val}\n"
            f"Required one or more of:\n{expected}",
        )
    return arg_val


def works_filter_type(arg_val, **kwargs):
    """Validate --filter arguments in pubs or works command."""
    pattern = ":|".join(work_filter_choices)
    expected = ":*\n".join(work_filter_choices)
    m = re.match(pattern, arg_val)
    if m is None:
        raise argparse.ArgumentTypeError(
            f"Invalid Work Filter Field\n {arg_val}\n"
            f"Required one or more of:\n{excepted}",
        )
    return arg_val


def works_facets_type(arg_val, **kwargs):
    """Validate --facets arguments in pubs or works command."""
    pattern = ":|".join(work_facet_choices)
    expected = ":*\n".join(work_facet_choices)
    m = re.match(pattern, arg_val)
    if m is None:
        raise argparse.ArgumentTypeError(
            f"Invalid Facet Field {arg_val}\nRequired one of:\n{expected}",
        )
    return arg_val
