# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: 42
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Soalnya thread menguabah dan mengakses processed_count dengan bersamaan. Jadi 2 thread membaca nilai count yang sama sebelum salah satun nilainya diperbarui. Habis itu keduanya melakukan increment 1 dan menyimpan hasil yang sama, sehingga salah satu dari penambahan itu tidak tercatar dan jumlah processed_count jadi lebih kecil dari jumlah pesanan yang asli yaitu 100
![percobaan non lock](bukti/OutputPogramTanpaLock.png)

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: ...

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
