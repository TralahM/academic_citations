from pygments import highlight, lexers, formatters, styles

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
