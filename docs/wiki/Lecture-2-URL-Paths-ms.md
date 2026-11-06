[English](Lecture-2-URL-Paths) · [Dansk](Lecture-2-URL-Paths-da) · **Bahasa Melayu**

# Pelajaran 2: Laluan URL

![Laluan /username/Angela menyambut pengguna](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-2-url-paths.png)

Kod: `src/higher_lower/presentation/lectures/step_02_url_paths.py`.

## Apa yang kami perolehi

- Laluan ialah fungsi yang diikat kepada laluan URL dengan `@app.route`.
- Bahagian pemboleh ubah seperti `/username/<name>` menghantar teks URL kepada fungsi.
- Penukar seperti `<int:number>` menyemak jenis; teks lain memberi halaman 404.
- Mod nyahpepijat memuat semula pelayan pada setiap perubahan dan menunjukkan penyahpepijat Flask dengan nilai pemboleh ubah apabila ralat berlaku.
- Teks pengguna dalam halaman mesti dilepaskan (escape), sebab itu kod menggunakan `escape`.
