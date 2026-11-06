"""Constants of the Higher or Lower project.

@brief Every literal the game shows or compares lives here, in one place.
"""

## Lowest number the secret number can be.
MIN_NUMBER: int = 0
## Highest number the secret number can be.
MAX_NUMBER: int = 9

## Heading of the home page.
HOME_HEADING: str = f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}"
## Heading when the guess is lower than the secret number.
LOW_HEADING: str = "Too low, try again!"
## Heading when the guess is higher than the secret number.
HIGH_HEADING: str = "Too high, try again!"
## Heading when the guess equals the secret number.
CORRECT_HEADING: str = "You found me!"
## Heading when the guess is outside the allowed range.
OUT_OF_RANGE_HEADING: str = f"Please guess between {MIN_NUMBER} and {MAX_NUMBER}"

## Heading colour of the home page.
HOME_COLOUR: str = "magenta"
## Heading colour for a guess that is too low.
LOW_COLOUR: str = "red"
## Heading colour for a guess that is too high.
HIGH_COLOUR: str = "purple"
## Heading colour for a correct guess.
CORRECT_COLOUR: str = "green"
## Heading colour for a guess outside the range.
OUT_OF_RANGE_COLOUR: str = "orange"

## GIF of the home page.
HOME_GIF: str = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
## GIF for a guess that is too low.
LOW_GIF: str = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
## GIF for a guess that is too high.
HIGH_GIF: str = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
## GIF for a correct guess.
CORRECT_GIF: str = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

## Host the development server listens on.
HOST: str = "127.0.0.1"
## Port the development server listens on.
PORT: int = 5000

## Still picture used by the HTML rendering lecture step.
STILL_IMAGE: str = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy_s.gif"
## Width in pixels of the pictures in the HTML rendering lecture step.
LECTURE_IMAGE_WIDTH: int = 200
