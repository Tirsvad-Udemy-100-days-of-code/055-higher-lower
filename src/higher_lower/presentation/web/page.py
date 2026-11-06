"""Page view model of the web presentation.

@brief Plain data for one page, built from a guess result.
"""

from dataclasses import dataclass

from higher_lower.constants import (
    CORRECT_COLOUR,
    CORRECT_GIF,
    CORRECT_HEADING,
    HIGH_COLOUR,
    HIGH_GIF,
    HIGH_HEADING,
    HOME_COLOUR,
    HOME_GIF,
    HOME_HEADING,
    LOW_COLOUR,
    LOW_GIF,
    LOW_HEADING,
    OUT_OF_RANGE_COLOUR,
    OUT_OF_RANGE_HEADING,
)
from higher_lower.domain.rules import GuessResult


@dataclass(frozen=True, slots=True)
class PageViewModel:
    """@brief What a page shows: a coloured heading and a picture."""

    heading: str
    colour: str
    gif: str


HOME_PAGE = PageViewModel(HOME_HEADING, HOME_COLOUR, HOME_GIF)
OUT_OF_RANGE_PAGE = PageViewModel(OUT_OF_RANGE_HEADING, OUT_OF_RANGE_COLOUR, HOME_GIF)

_PAGES_BY_RESULT: dict[GuessResult, PageViewModel] = {
    GuessResult.LOW: PageViewModel(LOW_HEADING, LOW_COLOUR, LOW_GIF),
    GuessResult.HIGH: PageViewModel(HIGH_HEADING, HIGH_COLOUR, HIGH_GIF),
    GuessResult.CORRECT: PageViewModel(CORRECT_HEADING, CORRECT_COLOUR, CORRECT_GIF),
}


def page_for_result(result: GuessResult) -> PageViewModel:
    """Build the page that tells the player how the guess went.

    @param result The outcome of the guess.
    @return The page view model for that outcome.
    """
    return _PAGES_BY_RESULT[result]
