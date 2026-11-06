"""Tests of lecture step 3."""

from higher_lower import constants
from higher_lower.presentation.lectures.step_03_html import create_app


def test_home_returns_centred_heading() -> None:
    body = create_app().test_client().get("/").get_data(as_text=True)
    assert "<h1 style='text-align: center'>Hello, World!</h1>" in body


def test_home_returns_paragraph_and_two_images() -> None:
    body = create_app().test_client().get("/").get_data(as_text=True)
    assert "<p>This is a paragraph.</p>" in body
    assert body.count("<img ") == 2
    assert f"width={constants.LECTURE_IMAGE_WIDTH}" in body
