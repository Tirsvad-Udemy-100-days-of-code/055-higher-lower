[English](Lecture-5-Advanced-Decorators) · [Dansk](Lecture-5-Advanced-Decorators-da) · **Bahasa Melayu**

# Pelajaran 5: Penghias lanjutan

![Angela telah log masuk dan mendapat catatan, Bob tidak dan tidak mendapat apa-apa](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/raw/branch/main/docs/screenshots/lecture-5-authenticated.png)

Kod: `src/higher_lower/presentation/lectures/step_05_authenticated.py`.

## Apa yang kami perolehi

- `*args` mengumpul argumen kedudukan dan `**kwargs` mengumpul argumen kata kunci, jadi penghias berfungsi untuk mana-mana fungsi.
- `is_authenticated` membaca pengguna daripada argumen dan menjalankan fungsi hanya apabila `user.is_logged_in` benar.
- Penghias boleh mengawal sama ada fungsi dijalankan langsung, bukan sekadar mengubah hasilnya.
- Corak yang sama melindungi mana-mana fungsi yang memerlukan pengguna yang telah log masuk.
