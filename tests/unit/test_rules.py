"""Tests of the game rules."""

import pytest

from higher_lower.domain.rules import GuessResult, compare_guess


@pytest.mark.parametrize(
    ("guess", "expected"),
    [(3, GuessResult.LOW), (7, GuessResult.HIGH), (5, GuessResult.CORRECT)],
)
def test_compare_guess_classifies_guess(guess: int, expected: GuessResult) -> None:
    assert compare_guess(guess, 5) is expected


def test_compare_guess_is_correct_at_lower_boundary() -> None:
    assert compare_guess(0, 0) is GuessResult.CORRECT
