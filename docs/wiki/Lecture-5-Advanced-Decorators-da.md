[English](Lecture-5-Advanced-Decorators) · **Dansk** · [Bahasa Melayu](Lecture-5-Advanced-Decorators-ms)

# Lektion 5: Avancerede dekoratorer

![Angela er logget ind og får et opslag, Bob er ikke og får intet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-5-authenticated.png)

Kode: `src/higher_lower/presentation/lectures/step_05_authenticated.py`.

## Det lærte vi

- `*args` samler positionelle argumenter og `**kwargs` samler nøgleordsargumenter, så en dekorator virker for enhver funktion.
- `is_authenticated` læser brugeren fra argumenterne og kører kun funktionen, når `user.is_logged_in` er sand.
- En dekorator kan styre, om en funktion overhovedet kører, og ikke kun ændre resultatet.
- Samme mønster beskytter enhver funktion, der kræver en logget ind bruger.
