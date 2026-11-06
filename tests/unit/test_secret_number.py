"""Tests of the secret number source."""

from higher_lower.infrastructure.secret_number import random_secret_number

DRAWS = 500


def test_random_secret_number_stays_in_range() -> None:
    draws = [random_secret_number(0, 9) for _ in range(DRAWS)]
    assert all(0 <= value <= 9 for value in draws)


def test_random_secret_number_returns_the_only_possible_value() -> None:
    assert random_secret_number(4, 4) == 4
