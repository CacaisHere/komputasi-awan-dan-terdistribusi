# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): -
- Cara memperbaikinya: -

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: ![nodeBaru](bukti/nodebaru.png)
- Hasil sebelum & sesudah node keluar: ![nodeKeluar](bukti/nodeKeluar.png)

## Tugas Analisis
1. DHT/Chord lebih cocok karena IP kurir sering berubah jadi pemetaan ID kurir ke IP dapat diperbarui dengan flesibel. Berbeda dengan tabel pusat yang bergantung pada satu server, chord menyimpan data secara terdistribusi pada beberpa node.Chord juga lebih mudah untuk menyesuaikan perubahan node melalui join dan leave, jadi tanggung jawab penyimpanan data dapat dialihkan ke node lain tanpa bergantu pada satu server pusat.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 03/11/2026 | ChatGPT | Jelaskan konsep DHT dan algoritma chord dalam komputasi awan | AI menjelaskan konsep hashing, ring, node, dan successor. | penjelasana tersebut digunakan untuk memahami konsep DHT agar bisa mengimplementasikan program |
