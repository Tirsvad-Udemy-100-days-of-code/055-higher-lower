"""Lecture step 4: decorators that wrap text in HTML tags.

@brief The make_bold, make_emphasis and make_underlined decorators, used on
the /bye route.
"""

from collections.abc import Callable
from functools import wraps

from flask import Blueprint, Flask

from higher_lower.constants import HOST, PORT


def _wrap_in_tag(function: Callable[..., str], tag: str) -> Callable[..., str]:
    """Wrap the text a function returns in an HTML tag.

    @param function The function that returns text.
    @param tag The tag name, for example b.
    @return The decorated function.
    """

    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> str:
        return f"<{tag}>{function(*args, **kwargs)}</{tag}>"

    return wrapper


def make_bold(function: Callable[..., str]) -> Callable[..., str]:
    """Wrap the text returned by a function in <b> tags.

    @param function The function that returns text.
    @return The decorated function.
    """
    return _wrap_in_tag(function, "b")


def make_emphasis(function: Callable[..., str]) -> Callable[..., str]:
    """Wrap the text returned by a function in <em> tags.

    @param function The function that returns text.
    @return The decorated function.
    """
    return _wrap_in_tag(function, "em")


def make_underlined(function: Callable[..., str]) -> Callable[..., str]:
    """Wrap the text returned by a function in <u> tags.

    @param function The function that returns text.
    @return The decorated function.
    """
    return _wrap_in_tag(function, "u")


## Blueprint that holds the views of this lecture step.
_blueprint = Blueprint("step_04_decorators", __name__)


@_blueprint.route("/")
def home() -> str:
    """Answer the home route."""
    return "Hello, World!"


@_blueprint.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye() -> str:
    """Answer /bye with bold, emphasised and underlined text."""
    return "Bye"


def create_app() -> Flask:
    """Build the Flask application of this lecture step.

    @return The configured Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(_blueprint)
    return app


if __name__ == "__main__":
    create_app().run(host=HOST, port=PORT, debug=True)
