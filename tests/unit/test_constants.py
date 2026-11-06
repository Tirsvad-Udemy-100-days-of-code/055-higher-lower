"""Tests of the project constants."""

from higher_lower import constants


def test_range_is_ordered() -> None:
    assert constants.MIN_NUMBER < constants.MAX_NUMBER


def test_home_heading_names_the_range() -> None:
    assert str(constants.MIN_NUMBER) in constants.HOME_HEADING
    assert str(constants.MAX_NUMBER) in constants.HOME_HEADING


def test_answer_colours_are_different() -> None:
    colours = {
        constants.LOW_COLOUR,
        constants.HIGH_COLOUR,
        constants.CORRECT_COLOUR,
    }
    assert len(colours) == 3
