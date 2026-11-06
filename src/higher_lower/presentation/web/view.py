"""HTML view of the web presentation.

@brief Renders a page view model as HTML.
"""

from html import escape

from higher_lower.presentation.web.page import PageViewModel


def render_page(page: PageViewModel) -> str:
    """Render a page as HTML, escaping every value.

    @param page The page to show.
    @return A heading in the page colour followed by the picture.
    """
    colour = escape(page.colour)
    heading = escape(page.heading)
    gif = escape(page.gif)
    return f'<h1 style="color: {colour}">{heading}</h1><img src="{gif}">'
