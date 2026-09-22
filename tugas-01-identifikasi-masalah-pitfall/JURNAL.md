# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [21 September 2026]
- Peserta: [Julia, Clarrisa]
- Poin diskusi: menentukan pitfall dan menentukan alasannya
- Perbedaan pendapat (jika ada): -

## [22 September 2026]
- Peserta: [Julia, Clarrisa]
- Poin diskusi: menentukan pitfall ketiga dan saling meriview
- Perbedaan pendapat (jika ada): -

## Review Silang
- [Clarrisa Aurelia] mengomentari analisis [Julia Firdaus]: Menurut saya untuk pitfall 2 sudah sesuai dengan memilih latency is zero karena modul pesanan memanggil modul pembayaran tanpa menunggu batas waktu padahal sangat tidak mungkin kalau latensi bisa 0ms dan julia menjelaskan dampaknya terhadap aplikasi foodGo dengan runtut

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 21/09/2026 | chatgpt | Apa saja solusi dari syncronous pitfall | synchronous pitfall bisa diatasi dengan asynchronous communication, timeout, retry, message queue, caching, circuit breaker, dan parallel processing. |dari jawaban yang telah diberikan oleh AI kami memilih salah satu solusi dari pitfall synchronous yaitu caching karena data yang sering diakses disimpan di RAM sehingga tidak selalu meminta ke server|
