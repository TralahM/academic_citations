from pygments import highlight, lexers, formatters, styles
from crossref import CrossRefAPIClient


def create_api_client(args):
    """Create an API Client."""
    client = CrossRefAPIClient(
        api_version=args.api_version,
        api_mailto=args.mailto,
        api_auth_token=args.auth_token,
    )
    return client


def print_colored_json(
    formatted_json: str,
    format_on: bool = False,
    formatter=formatters.Terminal256Formatter(
        style=styles.get_style_by_name("rainbow_dash"),
    ),
):
    """Print Colored JSON."""
    colored = highlight(
        formatted_json,
        lexer=lexers.JsonLexer(),
        formatter=formatter if format_on else formatters.NullFormatter(),
    )
    print(colored)
    return colored
