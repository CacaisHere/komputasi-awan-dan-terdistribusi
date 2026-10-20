# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: ...

## Skenario 1: Start normal
- Leader yang terpilih: node 5
- Log/observasi: Kami menjalankan lima node di terminal berbeda dan setiap node saling mengirim pesan untuk pemilihan leader. Dari hasil pengujian, node 5 terpilih sebagai leader karena memiliki ID paling tinggi. Untuk node lainnya menerima pesan COORDINATOR dan mencatat kalau node 5 adalah leader saat ini. Jadi, node 5 terpilih karena konsep dari bully algorithm sendiri yaitu node aktif dengan ID tertinggi akan menjadi leader.

![hasil pengujian start normal](bukti/1.png)

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: node 4
- Berapa lama waktu sampai leader baru terdeteksi: ...

![hasil pengujian setelah leader dimatikan](bukti/2.png)

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
