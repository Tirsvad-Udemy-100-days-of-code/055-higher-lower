"""Lecture step 2: URL paths, variable sections and the Flask debugger.

@brief Routes that read the URL path, including a variable section and a URL
converter.
"""

from flask import Blueprint, Flask
from markupsafe import escape

from higher_lower.constants import HOST, PORT

## Blueprint that holds the views of this lecture step.
_blueprint = Blueprint("step_02_url_paths", __name__)


@_blueprint.route("/")
def home() -> str:
    """Answer the home route."""
    return "Hello, World!"


@_blueprint.route("/bye")
def say_bye() -> str:
    """Answer the fixed route /bye."""
    return "Bye"


@_blueprint.route("/username/<name>")
def greet(name: str) -> str:
    """Greet the user whose name is the variable section of the URL.

    @param name The text found in the URL after /username/.
    @return The greeting, with the name escaped so it cannot inject HTML.
    """
    return f"Hello there {escape(name)}!"


@_blueprint.route("/username/<name>/<int:number>")
def greet_with_number(name: str, number: int) -> str:
    """Greet the user and use the converter <int:number> for a number.

    @param name The text found in the URL after /username/.
    @param number The integer found after the name; other text gives 404.
    @return The greeting that repeats the name and the number.
    """
    return f"Hello there {escape(name)}, you are {number} years old!"


def create_app() -> Flask:
    """Build the Flask application of this lecture step.

    @return The configured Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(_blueprint)
    return app


if __name__ == "__main__":
    # Debug mode reloads the server on every code change and shows the debugger.
    create_app().run(host=HOST, port=PORT, debug=True)
