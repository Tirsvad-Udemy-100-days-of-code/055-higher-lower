**English** · [Dansk](Lecture-5-Advanced-Decorators-da) · [Bahasa Melayu](Lecture-5-Advanced-Decorators-ms)

# Lecture 5: Advanced decorators

![Angela is logged in and gets a post, Bob is not and gets none](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-5-authenticated.png)

Code: `src/higher_lower/presentation/lectures/step_05_authenticated.py`.

## What we gained

- `*args` collects positional arguments and `**kwargs` collects keyword arguments, so a decorator works for any function.
- `is_authenticated` reads the user from the arguments and runs the function only when `user.is_logged_in` is true.
- A decorator can control whether a function runs at all, not only change its result.
- The same pattern protects any function that needs a logged-in user.
