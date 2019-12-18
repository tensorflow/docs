# Contribution guideline

## Directory structure

Struktur direktori dokumen :

```
site
├── en
│   ├── ...
│   ├── ...
│   └── ...
├── id
│   ├── ...
│   ├── ...
│   └── ...
├── ...
└── ...
```

Dokumen di bawah `situs / en` adalah dokumen yang belum diterjemahkan.
Terjemahkan dapat diletakkan di bawah `site / id` dalam konfigurasi yang sama
dengan` site / en` dan kirim pull request.

## Pull request title

Disarankan bahwa judul (title) pull request adalah "ID: ...".

Sehingga Peninjau (reviewer) dapat menggunakan kata kunci "ID" untuk mencarinya,
jadi diharapkan kerja samanya untuk proses peninjauan dokumen.

## Pull request size

Disarankan untuk membuat pull request dengan membaginya menjadi 1 file untuk 1
pull request. Ini untuk mengurangi beban peninjau dan untuk mempermudah proses
penyatuan kode, jadi dimohon kerja samanya.

## Proofreading tool

[Proofing tool] (https://github.com/tfug/proofreading) digunakan sebagai
penanggulangan fluktuasi notasi kata maupun ejaan, dikarenakan otomatisasi
beberapa ulasan dan terjemahan oleh banyak orang.

Ini tidak begitu penting, karena peninjau juga memeriksa pada saat proses
peninjauan, tetapi jika Anda memeriksanya terlebih dahulu, Anda akan memerlukan
lebih sedikit koreksi pada proses pull request.

Kami juga menerima pull request ke Proofing tool.

## Frequently asked questions

### Haruskah saya menerjemahkan komentar dalam kode sumber?

Disarankan untuk menerjemahkan juga bagian komentar dalam kode sumber.

### Dokumen mana yang harus saya terjemahkan?

[Terjemahan TF 1.0 telah dinyatakan sebagai akhir pembaruan](https://groups.google.com/a/tensorflow.org/forum/#!msg/docs/vO0gQnEXcSM/YK_ybv7tBQAJ)
Jadi tolong terjemahkan dokumentasi TF 2.0. Tidak ada batasan lain.

### Dapatkah saya melihat siapa yang menerjemahkan dokumen mana?

Sulit untuk mengetahui dengan pasti, jadi mohon periksa beberapa hal berikut :

* Cari keyword "ID" untuk mencari tahu apa yang sedang dibuat 
* Jika Ada yang ingin di diskusikan, hubungi via Slack atau lainnya.

### Bagaimana saya bisa menjadi peninjau dokumen ini ?

Saat ini sedang dibahas kriteria kriteria nya, beberapa kriteria yang sudah ada :

* Dokumen sudah diterjemahkan dan pull request telah dilakukan

Jika Anda memenuhi persyaratan di atas dan ingin menjadi peninjau
[REVIEWERS](https://github.com/tensorflow/docs/blob/master/site/ja/REVIEWERS)
Tambahkan ID GitHub Anda ke dan kirim pull request.

### Apa yang harus saya lakukan jika sisi dokumen bahasa Inggris adalah tautan ke repositori eksternal?

Tempatkan di dalam `site / id` dengan konfigurasi yang sama dengan repositori
yang ditautkan.
