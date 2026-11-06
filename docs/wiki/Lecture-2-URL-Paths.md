**English** · [Dansk](Lecture-2-URL-Paths-da) · [Bahasa Melayu](Lecture-2-URL-Paths-ms)

# Lecture 2: URL paths

![The route /username/Angela greets the user](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-2-url-paths.png)

Code: `src/higher_lower/presentation/lectures/step_02_url_paths.py`.

## What we gained

- A route is a function bound to a URL path with `@app.route`.
- A variable section such as `/username/<name>` passes the text of the URL to the function.
- A converter such as `<int:number>` checks the type; other text gives a 404 page.
- Debug mode reloads the server on every change and shows the Flask debugger with the values of the variables when an error happens.
- User text in a page must be escaped, so the code uses `escape`.
