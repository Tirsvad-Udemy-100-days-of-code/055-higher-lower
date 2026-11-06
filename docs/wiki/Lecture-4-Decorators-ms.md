[English](Lecture-4-Decorators) · [Dansk](Lecture-4-Decorators-da) · **Bahasa Melayu**

# Pelajaran 4: Penghias

![Laluan /bye dengan teks tebal, ditekankan dan bergaris bawah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-4-decorators.png)

Kod: `src/higher_lower/presentation/lectures/step_04_decorators.py`.

## Apa yang kami perolehi

- Penghias (decorator) ialah fungsi yang menerima fungsi dan memulangkan fungsi baharu.
- `make_bold`, `make_emphasis` dan `make_underlined` menambah `<b>`, `<em>` dan `<u>` di satu tempat, jadi tiada laluan mengulang teg.
- Penghias boleh disusun: yang paling hampir dengan fungsi dijalankan dahulu.
- `functools.wraps` mengekalkan nama fungsi, yang diperlukan Flask untuk setiap laluan.
