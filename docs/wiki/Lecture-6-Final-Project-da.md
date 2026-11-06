[English](Lecture-6-Final-Project) · **Dansk** · [Bahasa Melayu](Lecture-6-Final-Project-ms)

# Lektion 6: Slutprojekt

![3 er for lavt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-6-too-low.png)
![7 er for højt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-6-too-high.png)
![5 er rigtigt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-6-correct.png)

Kode: `server.py` og `src/higher_lower/`.

## Det lærte vi

- Alt fra dagen i ét program: ruter, en variabel URL-del, HTML, typografi og GIF'er.
- Det hemmelige tal vælges én gang, når appen starter; `/<int:guess>` sammenligner gættet med det.
- Hvert svar har sin egen overskriftsfarve og GIF. Overskrifter, farver og GIF-adresser ligger i `constants.py`.
- Reglen, der sammenligner to tal, er en almindelig funktion i `domain`-laget, så testene ikke behøver Flask.
- Testene bruger Flask-testklienten med et fast hemmeligt tal og behøver ikke netværk.
