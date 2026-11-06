"""Tests of the web application through the Flask test client."""

import pytest
from flask.testing import FlaskClient

from higher_lower import constants
from higher_lower.presentation.web.app import create_app

SECRET = 5


@pytest.fixture
def client() -> FlaskClient:
    return create_app(SECRET).test_client()


def _body(client: FlaskClient, path: str) -> str:
    return client.get(path).get_data(as_text=True)


def _expected(heading: str, colour: str, gif: str) -> str:
    return f'<h1 style="color: {colour}">{heading}</h1><img src="{gif}">'


def test_home_page_shows_home_heading_colour_and_gif(client: FlaskClient) -> None:
    expected = _expected(
        constants.HOME_HEADING, constants.HOME_COLOUR, constants.HOME_GIF
    )
    assert _body(client, "/") == expected


def test_guess_below_secret_shows_too_low_page(client: FlaskClient) -> None:
    expected = _expected(constants.LOW_HEADING, constants.LOW_COLOUR, constants.LOW_GIF)
    assert _body(client, "/3") == expected


def test_guess_above_secret_shows_too_high_page(client: FlaskClient) -> None:
    expected = _expected(
        constants.HIGH_HEADING, constants.HIGH_COLOUR, constants.HIGH_GIF
    )
    assert _body(client, "/7") == expected


def test_guess_equal_to_secret_shows_correct_page(client: FlaskClient) -> None:
    expected = _expected(
        constants.CORRECT_HEADING, constants.CORRECT_COLOUR, constants.CORRECT_GIF
    )
    assert _body(client, "/5") == expected


def test_pages_use_distinct_colours() -> None:
    colours = {
        constants.HOME_COLOUR,
        constants.LOW_COLOUR,
        constants.HIGH_COLOUR,
        constants.CORRECT_COLOUR,
        constants.OUT_OF_RANGE_COLOUR,
    }
    assert len(colours) == 5


def test_guess_above_range_shows_out_of_range_page_with_home_gif(
    client: FlaskClient,
) -> None:
    response = client.get("/10")
    expected = _expected(
        constants.OUT_OF_RANGE_HEADING,
        constants.OUT_OF_RANGE_COLOUR,
        constants.HOME_GIF,
    )
    assert response.status_code == 200
    assert response.get_data(as_text=True) == expected


@pytest.mark.parametrize("path", ["/-1", "/abc"])
def test_negative_or_text_path_is_not_found(client: FlaskClient, path: str) -> None:
    assert client.get(path).status_code == 404


def test_app_without_secret_keeps_one_random_secret() -> None:
    client = create_app().test_client()
    numbers = range(constants.MIN_NUMBER, constants.MAX_NUMBER + 1)
    first = [_body(client, f"/{n}") for n in numbers]
    second = [_body(client, f"/{n}") for n in numbers]
    correct = _expected(
        constants.CORRECT_HEADING, constants.CORRECT_COLOUR, constants.CORRECT_GIF
    )
    assert first == second
    assert first.count(correct) == 1
