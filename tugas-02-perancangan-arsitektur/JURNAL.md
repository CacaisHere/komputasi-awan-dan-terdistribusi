# Jurnal Proses — Tugas 2

## [28 September 2026]
- Opsi arsitektur yang dipertimbangkan: SOA + Pub-Sub
- Kenapa akhirnya pilih [SOA/Pub-Sub]: ...
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

```mermaid
graph LR
  Client[Pelanggan] --> KatOrder[Katalog]
  KatOrder-->|HTTP request pesan| OrderSvc[Service Pesanan]
  OrderSvc -->|publish event OrderCreated| Broker[(Message Broker)]
  Broker -->|subscribe| PaymentSvc[Service Pembayaran]
  PaymentSvc -->|publish event PaymentCreated| BrokerM[(Message Broker)]
  BrokerM -->|subscribe| NotifSvc[Service Notifikasi Kurir]

```
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
