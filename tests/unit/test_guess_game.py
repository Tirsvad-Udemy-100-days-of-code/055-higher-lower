"""Tests of the guess game use case."""

import pytest

from higher_lower.application.guess_game import GuessGame
from higher_lower.constants import MAX_NUMBER, MIN_NUMBER
from higher_lower.domain.rules import GuessResult


def test_check_reports_low_high_and_correct() -> None:
    game = GuessGame(5)
    assert game.check(2) is GuessResult.LOW
    assert game.check(8) is GuessResult.HIGH
    assert game.check(5) is GuessResult.CORRECT


@pytest.mark.parametrize("guess", [MIN_NUMBER, MAX_NUMBER])
def test_is_in_range_accepts_limits(guess: int) -> None:
    assert GuessGame(5).is_in_range(guess)


@pytest.mark.parametrize("guess", [MIN_NUMBER - 1, MAX_NUMBER + 1])
def test_is_in_range_rejects_values_just_outside(guess: int) -> None:
    assert not GuessGame(5).is_in_range(guess)
