"""Entry point of the Higher or Lower URLs project.

@brief Composition root: builds the web application and runs it.
"""

from higher_lower.constants import HOST, PORT
from higher_lower.presentation.web.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
