# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Julia Fidaus Azzahra] | [103072400056] | [pitfall 2] |
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

## Pitfall 2: [latency is zero] — ditulis oleh [Julia Firdaus Azzahra]

**Bukti di skenario:** Tidak ada timeout sama sekali pada pemanggilan antar service.

**Kenapa ini keliru:** Karena seharusnya komunikasi antar service pasti memiliki latency. Ada proses yang harus dilewati seperti pengiriman data, pemrosesan di server, dan pengiriman respon. Pada soal dijelaskan bahwa modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu, padahal sangat tidak mungkin untuk sebuah sistem tidak memiliki latency. Pasti akan selalu membutuhkan waktu dan bisa saja mengalami keterlambatan.

**Dampak ke FoodGo:** Pada saat banyak request masuk ke server disaat bersamaan, server harus menangani banyak proses yang masih menunggu proses pembayaran yang mengakibatkan beban server meningkat sehingga aplikasi akan menjadi lambat dan dapat mengalami crash.

**Solusi desain awal:** Memberikan timeout pada komunikasi antar service agar tidak menunggu tanpa batas waktu.

**Trade-off:** Timeout yang singkat mungkin akan menyebabkan request dianggap gagal padahal sebenarnya service tujuan masih memprosesnya.
---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
