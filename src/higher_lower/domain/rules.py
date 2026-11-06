"""Rules of the Higher or Lower game.

@brief Pure comparison of a guess with the secret number.
"""

from enum import Enum


class GuessResult(Enum):
    """@brief Outcome of comparing a guess with the secret number."""

    LOW = "low"
    HIGH = "high"
    CORRECT = "correct"


def compare_guess(guess: int, secret: int) -> GuessResult:
    """Compare a guess with the secret number.

    @param guess The number the player guessed.
    @param secret The number to find.
    @return LOW if the guess is below the secret, HIGH if above, else CORRECT.
    """
    if guess < secret:
        return GuessResult.LOW
    if guess > secret:
        return GuessResult.HIGH
    return GuessResult.CORRECT
