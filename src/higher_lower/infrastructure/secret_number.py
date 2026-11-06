"""Source of the secret number.

@brief The only place in the project that uses randomness.
"""

import random


def random_secret_number(minimum: int, maximum: int) -> int:
    """Draw a secret number.

    @param minimum Lowest possible number.
    @param maximum Highest possible number.
    @return A random integer from minimum to maximum, both included.
    """
    return random.randint(minimum, maximum)
