"""Lecture step 5: advanced decorators with *args and **kwargs.

@brief The User class and the is_authenticated decorator, which runs a function
only for a logged-in user.
"""

from collections.abc import Callable
from functools import wraps

from flask import Blueprint, Flask
from markupsafe import escape

from higher_lower.constants import HOST, PORT


class User:
    """A user with a name and a logged-in flag."""

    def __init__(self, name: str) -> None:
        """Create a user who is not logged in.

        @param name The user name.
        """
        self.name = name
        self.is_logged_in = False


def is_authenticated(function: Callable[..., str]) -> Callable[..., str | None]:
    """Run the function only when its user is logged in.

    The wrapper accepts any positional and keyword arguments (*args and
    **kwargs) and forwards them. The user is the first positional argument, or
    the keyword argument named user.

    @param function The function to protect.
    @return The decorated function; it returns None for a user who is not
        logged in.
    """

    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> str | None:
        user = args[0] if args else kwargs.get("user")
        if isinstance(user, User) and user.is_logged_in:
            return function(*args, **kwargs)
        return None

    return wrapper


@is_authenticated
def create_blog_post(user: User) -> str:
    """Create a blog post for the user.

    @param user The author of the post.
    @return The text of the new blog post.
    """
    return f"This is {user.name}'s new blog post."


## Blueprint that holds the views of this lecture step.
_blueprint = Blueprint("step_05_authenticated", __name__)


@_blueprint.route("/")
def home() -> str:
    """Show the result of create_blog_post for a user in and out."""
    lines = []
    for name, logged_in in (("Angela", True), ("Bob", False)):
        user = User(name)
        user.is_logged_in = logged_in
        state = "logged in" if logged_in else "logged out"
        post = create_blog_post(user)
        lines.append(
            f"<p>{escape(name)} is {state}: "
            f"{escape(post) if post else 'no post created'}</p>"
        )
    return "<h1>is_authenticated</h1>" + "".join(lines)


def create_app() -> Flask:
    """Build the Flask application of this lecture step.

    @return The configured Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(_blueprint)
    return app


if __name__ == "__main__":
    create_app().run(host=HOST, port=PORT, debug=True)
