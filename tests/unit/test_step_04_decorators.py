"""Tests of lecture step 4."""

from higher_lower.presentation.lectures.step_04_decorators import (
    create_app,
    make_bold,
    make_emphasis,
    make_underlined,
)


def _text() -> str:
    return "Bye"


def test_make_bold_wraps_in_b() -> None:
    assert make_bold(_text)() == "<b>Bye</b>"


def test_make_emphasis_wraps_in_em() -> None:
    assert make_emphasis(_text)() == "<em>Bye</em>"


def test_make_underlined_wraps_in_u() -> None:
    assert make_underlined(_text)() == "<u>Bye</u>"


def test_decorator_forwards_arguments() -> None:
    def greet(name: str, punctuation: str = "!") -> str:
        return f"Hi {name}{punctuation}"

    assert make_bold(greet)("Ann", punctuation="?") == "<b>Hi Ann?</b>"


def test_bye_route_is_bold_emphasised_and_underlined() -> None:
    body = create_app().test_client().get("/bye").get_data(as_text=True)
    assert body == "<b><em><u>Bye</u></em></b>"
