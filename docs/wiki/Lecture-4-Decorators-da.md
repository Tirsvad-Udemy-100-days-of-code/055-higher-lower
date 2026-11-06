[English](Lecture-4-Decorators) · **Dansk** · [Bahasa Melayu](Lecture-4-Decorators-ms)

# Lektion 4: Dekoratorer

![Ruten /bye i fed, fremhævet og understreget tekst](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-4-decorators.png)

Kode: `src/higher_lower/presentation/lectures/step_04_decorators.py`.

## Det lærte vi

- En dekorator er en funktion, der tager en funktion og returnerer en ny funktion.
- `make_bold`, `make_emphasis` og `make_underlined` tilføjer `<b>`, `<em>` og `<u>` ét sted, så ingen rute gentager tags.
- Dekoratorer kan stables: den nærmest funktionen kører først.
- `functools.wraps` bevarer funktionens navn, som Flask har brug for til hver rute.
