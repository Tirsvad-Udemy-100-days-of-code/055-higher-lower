"""Tests of lecture step 2."""

from flask.testing import FlaskClient

from higher_lower.presentation.lectures.step_02_url_paths import create_app


def _client() -> FlaskClient:
    return create_app().test_client()


def test_home_says_hello() -> None:
    assert _client().get("/").get_data(as_text=True) == "Hello, World!"


def test_bye_route_says_bye() -> None:
    assert _client().get("/bye").get_data(as_text=True) == "Bye"


def test_variable_section_is_used_in_greeting() -> None:
    body = _client().get("/username/Angela").get_data(as_text=True)
    assert body == "Hello there Angela!"


def test_variable_section_is_escaped() -> None:
    body = _client().get("/username/<b>").get_data(as_text=True)
    assert "<b>" not in body


def test_int_converter_accepts_a_number() -> None:
    body = _client().get("/username/Angela/25").get_data(as_text=True)
    assert body == "Hello there Angela, you are 25 years old!"


def test_int_converter_rejects_text() -> None:
    assert _client().get("/username/Angela/old").status_code == 404
