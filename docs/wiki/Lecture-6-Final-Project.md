**English** · [Dansk](Lecture-6-Final-Project-da) · [Bahasa Melayu](Lecture-6-Final-Project-ms)

# Lecture 6: Final project

![3 is too low](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-6-too-low.png)
![7 is too high](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-6-too-high.png)
![5 is correct](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-6-correct.png)

Code: `server.py` and `src/higher_lower/`.

## What we gained

- Everything of the day in one program: routes, a variable URL section, HTML, styles and GIFs.
- The secret number is chosen once when the app starts; `/<int:guess>` compares the guess with it.
- Each answer has its own heading colour and GIF. The headings, colours and GIF addresses live in `constants.py`.
- The rule that compares two numbers is a plain function in the `domain` layer, so tests do not need Flask.
- Tests use the Flask test client with a fixed secret number and need no network.
