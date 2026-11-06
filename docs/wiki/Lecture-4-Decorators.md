**English** · [Dansk](Lecture-4-Decorators-da) · [Bahasa Melayu](Lecture-4-Decorators-ms)

# Lecture 4: Decorators

![The route /bye in bold, emphasised and underlined text](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-4-decorators.png)

Code: `src/higher_lower/presentation/lectures/step_04_decorators.py`.

## What we gained

- A decorator is a function that takes a function and returns a new function.
- `make_bold`, `make_emphasis` and `make_underlined` add `<b>`, `<em>` and `<u>` once, so no route repeats the tags.
- Decorators stack: the one nearest the function runs first.
- `functools.wraps` keeps the name of the function, which Flask needs for every route.
