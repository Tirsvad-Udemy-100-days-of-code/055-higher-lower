"""Flask application of the Higher or Lower game.

@brief Routes that map a URL path to a guess and show the matching page.
"""

from flask import Blueprint, Flask, current_app

from higher_lower.application.guess_game import GuessGame
from higher_lower.constants import MAX_NUMBER, MIN_NUMBER
from higher_lower.infrastructure.secret_number import random_secret_number
from higher_lower.presentation.web.page import (
    HOME_PAGE,
    OUT_OF_RANGE_PAGE,
    page_for_result,
)
from higher_lower.presentation.web.view import render_page

## Key under which the game is stored in the Flask extensions registry.
_GAME_KEY = "guess_game"

## Blueprint that holds the views of the game.
_blueprint = Blueprint("higher_lower", __name__)


def _current_game() -> GuessGame:
    """Find the game stored in the running application.

    @return The game created by create_app.
    """
    game: GuessGame = current_app.extensions[_GAME_KEY]
    return game


@_blueprint.route("/")
def home() -> str:
    """Show the home page.

    @return The home page HTML.
    """
    return render_page(HOME_PAGE)


@_blueprint.route("/<int:guess>")
def guess_number(guess: int) -> str:
    """Judge the guess in the URL path.

    @param guess The number the player guessed.
    @return The page for a low, high, correct or out of range guess.
    """
    game = _current_game()
    if not game.is_in_range(guess):
        return render_page(OUT_OF_RANGE_PAGE)
    return render_page(page_for_result(game.check(guess)))


def create_app(secret_number: int | None = None) -> Flask:
    """Build the Flask application.

    @param secret_number The number to find; None draws a random one that
        stays the same for the lifetime of the application.
    @return The configured Flask application.
    """
    if secret_number is None:
        secret_number = random_secret_number(MIN_NUMBER, MAX_NUMBER)
    app = Flask(__name__)
    app.extensions[_GAME_KEY] = GuessGame(secret_number)
    app.register_blueprint(_blueprint)
    return app
