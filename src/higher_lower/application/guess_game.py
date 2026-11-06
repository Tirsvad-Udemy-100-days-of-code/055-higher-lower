"""Use case of the Higher or Lower game.

@brief Holds the secret number and judges guesses against it.
"""

from higher_lower.constants import MAX_NUMBER, MIN_NUMBER
from higher_lower.domain.rules import GuessResult, compare_guess


class GuessGame:
    """@brief One game with a fixed secret number."""

    def __init__(self, secret_number: int) -> None:
        """Start a game.

        @param secret_number The number the player has to find.
        """
        self._secret_number = secret_number

    def check(self, guess: int) -> GuessResult:
        """Judge a guess.

        @param guess The number the player guessed.
        @return Whether the guess is low, high or correct.
        """
        return compare_guess(guess, self._secret_number)

    def is_in_range(self, guess: int) -> bool:
        """Tell whether a guess is inside the allowed range.

        @param guess The number the player guessed.
        @return True when the guess is between the minimum and maximum number.
        """
        return MIN_NUMBER <= guess <= MAX_NUMBER
