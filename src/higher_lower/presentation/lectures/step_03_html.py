"""Lecture step 3: rendering HTML elements with Flask.

@brief A route that returns a heading, a paragraph and two images as HTML.
"""

from flask import Blueprint, Flask

from higher_lower.constants import HOST, LECTURE_IMAGE_WIDTH, PORT, STILL_IMAGE

## Animated version of the still picture.
ANIMATED_IMAGE: str = STILL_IMAGE.replace("_s.gif", ".gif")


## Blueprint that holds the views of this lecture step.
_blueprint = Blueprint("step_03_html", __name__)


@_blueprint.route("/")
def home() -> str:
    """Return structured HTML instead of a plain string.

    The Python string uses double quotes and the HTML attributes use single
    quotes, so the two never end each other.

    @return A centred heading, a paragraph, a still picture and a GIF.
    """
    return (
        "<h1 style='text-align: center'>Hello, World!</h1>"
        "<p>This is a paragraph.</p>"
        f"<img src='{STILL_IMAGE}' width={LECTURE_IMAGE_WIDTH}>"
        f"<img src='{ANIMATED_IMAGE}' width={LECTURE_IMAGE_WIDTH}>"
    )


def create_app() -> Flask:
    """Build the Flask application of this lecture step.

    @return The configured Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(_blueprint)
    return app


if __name__ == "__main__":
    create_app().run(host=HOST, port=PORT, debug=True)
