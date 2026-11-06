"""Flask application of the Higher or Lower game.

@brief Routes that map a URL path to a guess and show the matching page.
"""

from flask import Flask

from higher_lower.application.guess_game import GuessGame
from higher_lower.constants import MAX_NUMBER, MIN_NUMBER
from higher_lower.infrastructure.secret_number import random_secret_number
from higher_lower.presentation.web.page import (
    HOME_PAGE,
    OUT_OF_RANGE_PAGE,
    page_for_result,
)
from higher_lower.presentation.web.view import render_page


def create_app(secret_number: int | None = None) -> Flask:
    """Build the Flask application.

    @param secret_number The number to find; None draws a random one that
        stays the same for the lifetime of the application.
    @return The configured Flask application.
    """
    if secret_number is None:
        secret_number = random_secret_number(MIN_NUMBER, MAX_NUMBER)
    game = GuessGame(secret_number)
    app = Flask(__name__)

    @app.route("/")
    def home() -> str:
        """Show the home page.

        @return The home page HTML.
        """
        return render_page(HOME_PAGE)

    @app.route("/<int:guess>")
    def guess_number(guess: int) -> str:
        """Judge the guess in the URL path.

        @param guess The number the player guessed.
        @return The page for a low, high, correct or out of range guess.
        """
        if not game.is_in_range(guess):
            return render_page(OUT_OF_RANGE_PAGE)
        return render_page(page_for_result(game.check(guess)))

    return app
