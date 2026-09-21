# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Julia Fidaus Azzahra] | [103072400056] | [pitfall/bagian yang dikerjakan] |
| [Clarrisa Aurelia Putri Andini] | [103072400139] | [pitfall 1] |

## Pitfall 1: [synchronous] — ditulis oleh [Clarrisa Aurelia Putri Andini]

**Bukti di skenario:** Aplikasi jadi sangat lambat beberapa permintaan timeout karena lonjakan pesanan

**Kenapa ini keliru:** karena terjadi pemblokiran eksekusi kode(thread blocking) yang bisa menjadikan aplikasi berjalan lebih lambat dari biasanya

**Dampak ke FoodGo:** jika kode sinkronous pembeli akan menunggu loading lebih lama dihalaman aplikasi atau aplikasi akan tidak merespon inputan dari pengguna

**Solusi desain awal:**  
1. Menggunakan sistem cache(penyimpanan sementara) : jadi data yang sering di akses di device pengguna akan di simpan kedalam RAM, sehingga untuk waktu tunggu proses sinkronous lebih cepat

**Trade-off:** 
1. Terkadang data tidak otomatis memperbarui(berisikan data lama) dan konsumsi ruang penyimpanannya lebih banyak

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]
---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
