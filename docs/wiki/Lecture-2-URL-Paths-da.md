[English](Lecture-2-URL-Paths) · **Dansk** · [Bahasa Melayu](Lecture-2-URL-Paths-ms)

# Lektion 2: URL-stier

![Ruten /username/Angela hilser på brugeren](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-2-url-paths.png)

Kode: `src/higher_lower/presentation/lectures/step_02_url_paths.py`.

## Det lærte vi

- En rute er en funktion, der er bundet til en URL-sti med `@app.route`.
- En variabel del som `/username/<name>` giver URL'ens tekst videre til funktionen.
- En konverter som `<int:number>` kontrollerer typen; anden tekst giver en 404-side.
- Debug-tilstand genstarter serveren ved hver ændring og viser Flask-debuggeren med variablernes værdier, når en fejl opstår.
- Brugertekst på en side skal escapes, derfor bruger koden `escape`.
