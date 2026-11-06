# Product Requirements Document (PRD)
## Website Katalog & Profil Resmi UMKM: Punakawan Space & Eatery (Colomadu, Solo Raya)

---

## 1. Informasi Umum & Identitas Proyek (Project Overview)

* **Mata Kuliah:** Digital Marketing (Tugas Akhir / UAS) — Dosen Pengampu: Ibu Nurul Sutarti
* **Topik Pilihan:** **Topik 3 — SEO & Content Marketing untuk Website Portofolio/Katalog** *(Fokus Indikator: Ranking Keywords, Click-Through Rate / CTR, dan Bounce Rate)*
* **Nama Brand Resmi:** **Punakawan Space & Eatery** *(Warmindo & Kuliner Rakyat Colomadu)*
* **Slogan / Tagline:** *"Kuliner Rakyat — Tempat Nongkrong Hangat, Kuliner Rakyat Harga Bersahabat!"*
* **Lokasi Usaha:** Colomadu, Kabupaten Karanganyar / Surakarta (Dekat kawasan kampus UMS & jalur utama Solo Raya), Jawa Tengah.
* **Kontak & Saluran Distribusi Resmi:**
  * **WhatsApp Reservasi & Take Away:** `0896 5355 7758` (`https://wa.me/6289653557758`)
  * **Tersedia 3 Opsi Merchant Pesan-Antar:** **GoFood**, **ShopeeFood**, dan **GrabFood**
  * **Instagram & TikTok Resmi:** `@punakawanspaceeatery`

### 1.1. Matriks Pembagian Tugas Kelompok (6 Tahap Wajib UAS)

| Nama Anggota & NIM | Peran Proyek | Tahapan UAS yang Dikerjakan | Output & Bukti Wajib |
| :--- | :--- | :--- | :--- |
| **Anugrah Adiantoro** (B220231008) | *Market Researcher & Content Strategist* | **Tahap 1:** Riset Pasar Digital & **Tahap 2:** Perencanaan Strategi Digital Marketing | • Grafik **Google Trends** & analisis **Social Blade**.<br>• *Buyer Persona*, analisis 3 kompetitor di Colomadu, & daftar 10 *keywords* SEO. |
| **Andri Tri Wijayanto** (B220231007) | *Project Lead & Technical SEO Specialist* | **Tahap 3:** Implementasi Kampanye Digital (Website, Vercel & Google Search Console) | • Website **Punakawan Space & Eatery** *live* di Vercel.<br>• Bukti indeks URL, `sitemap.xml`, & grafik *Ranking Keywords* serta *CTR* di GSC. |
| **Abraham Theo** (B220231041) | *Web Analytics & Conversion Optimizer* | **Tahap 4:** Monitoring & Analisis Data & **Tahap 5:** Optimasi & Evaluasi (*A/B Testing*) | • Dashboard **Google Analytics 4 (GA4)** & trafik **UTM Tracking**.<br>• Bukti perbandingan **A/B Testing (Sebelum vs Sesudah Optimasi)** untuk menekan *Bounce Rate*. |
| **Samuel Kristawan** (B220231030) | *Data Visualizer & Reporting Lead* | **Tahap 6:** Presentasi & Dashboard Akhir | • Tautan & *screenshot* **Dashboard Interaktif Google Looker Studio**.<br>• Kompilasi Laporan Akhir PDF & Slide Presentasi kelompok. |

---

## 2. Latar Belakang Masalah & Tujuan Produk (Problem & Objectives)

### 2.1. Permasalahan Mitra UMKM (Problem Statement)
1. **Belum Memiliki Website Katalog Resmi di Google:** **Punakawan Space & Eatery** memiliki tempat nongkrong semi-outdoor beratap anyaman bambu yang nyaman serta menu kuliner rakyat dengan harga sangat terjangkau (`Rp 3.000` – `Rp 20.000`), namun belum memiliki *landing page* resmi yang terindeks di mesin pencari Google saat mahasiswa atau warga mencari *"warmindo Colomadu"* atau *"tempat nongkrong murah Colomadu"*.
2. **Informasi Menu & Saluran Order Terpencar:** Pelanggan belum mengetahui secara cepat daftar **9 Menu Best Seller**, rincian **Menu Paket Gratis Es Teh**, serta kemudahan memesan dari kos/rumah karena **tersedia 3 opsi merchant resmi (GoFood, ShopeeFood, dan GrabFood)**.

### 2.2. Tujuan Produk (Product Objectives)
1. **Dominasi Local SEO (Meningkatkan Ranking Keywords & CTR):** Mengoptimalkan struktur *On-Page SEO* (`Title`, `H1`–`H3`, `Meta Description`, `Alt Text`, dan `Schema.org Restaurant`) agar website masuk ke halaman pertama Google untuk 10 kata kunci target di area Colomadu.
2. **Menekan Bounce Rate di Bawah 35%:** Menyajikan antarmuka bertema **Warm Heritage** (Krem Hangat `#F4EFE6`, Teal Punakawan `#1E3F47`, dan Emas `#D4A857`) yang dilengkapi filter interaktif **9 Menu Best Seller**, **3 Papan Daftar Harga Resmi**, serta artikel **Content Marketing**.
3. **Mempercepat Konversi Order Online & Reservasi:** Menyediakan pintasan langsung ke **3 Opsi Merchant (GoFood, ShopeeFood, GrabFood)** serta formulir reservasi meja yang terhubung ke WhatsApp resmi `0896 5355 7758`.

---

## 3. Spesifikasi Fungsional & Struktur 7 Modul Halaman (Sesuai Desain Desktop)

Seluruh komponen website diimplementasikan mengikuti urutan vertikal pada mockup **`Punakawan Space & Eatery — Website desktop.jpg`**:

### 3.1. MOD-01: Sticky Header & Navigasi Utama (Navbar)
* **Warna Latar:** *Teal Punakawan* (`#1E3F47`) dengan garis bawah emas (`#D4A857`).
* **Identitas Kiri:** Logo huruf **`P`** emas + teks **`Punakawan`** (`#D4A857`) dan **`SPACE & EATERY`** (`#F4EFE6`).
* **Menu Navigasi Tengah:** `Home`, `Daftar Harga`, `Order`, `Suasana & Reservasi`.
* **Tombol CTA Kanan:** Tombol kapsul kuning (`#FFCC00`, teks hitam tebal `#111111`) bertuliskan **`Pesan Sekarang ↗`** yang menggulir langsung ke bagian `#order` (3 Opsi Merchant).

### 3.2. MOD-02: Hero Section (2 Kolom) & 3 Kartu Value Proposition
* **Kolom Kiri Hero:**
  * **Badge Atas:** `🏮 KULINER RAKYAT & WARMINDO NAIK KELAS DI COLOMADU`
  * **Headline Utama (`H1`):** *"Punakawan Space & Eatery – Tempat Nongkrong Hangat, Kuliner Rakyat Harga Bersahabat!"*
  * **Deskripsi SEO:** Menjelaskan keunggulan tempat nongkrong beratap bambu di Colomadu dengan 9 Menu Best Seller, Paket Nasi Kremesan Gratis Es Teh mulai Rp 12.000, Wonton Basah pedas, dan Wedang Punakawan.
  * **2 Tombol CTA Utama:**
    1. `Lihat 9 Menu Best Seller ↓` (Latar Teal `#1E3F47`, teks Kuning `#FFCC00`)
    2. `Order via Aplikasi ↗` (Latar Kuning `#FFCC00`, teks Hitam `#111111`)
  * **Baris Kepercayaan (Trust Badges):**
    * `✓ Harga Mulai Rp 3.000`
    * `✓ Paket Nasi Gratis Es Teh`
    * `✓ Tersedia 3 Opsi Merchant: GoFood, ShopeeFood & GrabFood`
* **Kolom Kanan Hero:**
  * Bingkai gambar utama (`tempat-bambu-malam.jpg` / *Clean Empty Placeholder* berbingkai garis putus-putus emas) dengan 2 *floating badges*:
    * Kiri Atas: `✨ Semi-Outdoor Bambu & Meja Kayu Cozy`
    * Kanan Bawah: `🔥 9 Menu BEST SELLER Pilihan!`
* **Seksi Value Proposition (`Kenapa Nongkrong di Punakawan Space & Eatery?`):**
  * Menampilkan 3 kartu putih sejajar: **(1) Kuliner Rakyat Ramah Kantong**, **(2) Space Nongkrong Hangat & Luas**, dan **(3) 9 Menu Best Seller Otentik**.

---

### 3.3. MOD-03: Showcase 9 Menu "BEST SELLER" di Halaman Home (`#bestseller`)

* **Aturan Bisnis Wajib:**
  1. Terdiri atas **3 Menu Makanan**, **3 Menu Minuman**, dan **3 Menu Snack** (total **9 kartu**).
  2. Seluruh 9 kartu di halaman utama wajib menggunakan pita pojok kanan atas bertuliskan **`BEST SELLER`** (warna hitam `#111111` & kuning `#FFCC00`) dan **tidak menggunakan kata *"Must Try"***.
  3. Dilengkapi 4 tombol filter interaktif: `Semua Best Seller (9)`, `3 Menu Makanan`, `3 Menu Minuman`, dan `3 Menu Snack`.
  4. Selama tahap awal sebelum foto asli dimasukkan, area gambar menggunakan **Slot Kosong Terstruktur (`3:4`)** agar tata letak tidak berantakan.

| No | Kategori | Nama Menu (`H3`) | Deskripsi Singkat | Harga Resmi | Label Pita Wajib | Nama File Aset Gambar |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `MAKANAN (1/3)` | **Mie Goreng Spesial Punakawan** | Mie goreng rempah lengkap dengan telur ceplok, sosis, suwiran ayam, dan ati ampela. | **Rp 12.000** | `BEST SELLER` | `menu-mie-goreng.jpg` |
| **2** | `MAKANAN (2/3)` | **Nasi Goreng Spesial Punakawan** | Nasi goreng rempah khas Jawa disajikan dengan telur ceplok, kerupuk, timun, dan tomat. | **Rp 13.000** | `BEST SELLER` | `menu-nasi-goreng.jpg` |
| **3** | `MAKANAN (3/3)` | **Spagheti (Carbonara & Bolognese)** | Spagheti hangat varian saus Carbonara & Bolognese dengan sosis sapi dan taburan keju. | **Rp 15.000** | `BEST SELLER` | `menu-spagheti.jpg` |
| **4** | `MINUMAN (1/3)` | **Wedang Punakawan (Rempah Asli)** | Seduhan jahe geprek bakar, serai wangi, dan jeruk nipis segar penghangat badan. | **Rp 10.000** | `BEST SELLER` | `menu-wedang-punakawan.jpg` |
| **5** | `MINUMAN (2/3)` | **Es Teh Tarik Spesial** | Perpaduan teh wangi khas Solo dan susu kental gurih yang ditarik hingga berbusa lembut. | **Rp 5.000** | `BEST SELLER` | `menu-es-teh-tarik.jpg` |
| **6** | `MINUMAN (3/3)` | **Badak + Es Batu (Sarsaparilla)** | Minuman soda sarsaparilla legendaris Cap Badak disajikan dingin dengan es batu kristal. | **Rp 17.000** | `BEST SELLER` | `menu-badak-es.jpg` |
| **7** | `SNACK (1/3)` | **Wonton Basah Kuah Pedas** | Pangsit ayam lembut disiram kuah pedas gurih dengan sawi pakcoy dan pangsit goreng. | **Rp 12.000** | `BEST SELLER` | `menu-wonton-basah.jpg` |
| **8** | `SNACK (2/3)` | **Pisang Goreng Punakawan** | Pisang goreng crispy spesial dengan lelehan coklat dan taburan keju parut melimpah. | **Rp 10.000** | `BEST SELLER` | `menu-pisang-goreng.jpg` |
| **9** | `SNACK (3/3)` | **Kentang Goreng Crispy** | Kentang goreng renyah gurih disajikan hangat dengan saus sambal dan tomat cocolan. | **Rp 8.000** | `BEST SELLER` | `menu-kentang-goreng.jpg` |

---

### 3.4. MOD-04: Katalog Lengkap — 3 Papan Daftar Harga Resmi (`#daftar-harga`)

Menampilkan 3 papan menu berlatar *Teal Punakawan* (`#1E3F47`) dan berbingkai emas (`#D4A857`) sesuai poster daftar harga asli:

1. **Papan 1 — MENU PAKET (Nasi Putih, Kremesan, Sambal, Lalapan & Teh/Es Teh):**
   * `Ati Ampela` (**12.000**), `Kepala Ayam` (**12.000**), `Bandeng Goreng` (**12.000**), `Lele Goreng` (**15.000**), `Ayam Goreng` (**18.000**), `Nila Goreng` (**20.000**).
   * **Extra:** `Telur` (**3.000**), `Nasi Putih` (**3.000**), `Kremesan` (**2.000**), `Pedas` (**1.000**).
   * *Footer Papan:* `TAMBAHAN RP. 2000,- UNTUK PACKING TAKE AWAY`.
2. **Papan 2 — SNACK (11 Menu Camilan):**
   * `Pangsit Goreng` (**10.000**), `Wonton Basah [BEST SELLER]` (**12.000**), `Wonton Goreng` (**12.000**), `Kentang Goreng [BEST SELLER]` (**8.000**), `Singkong Goreng [BEST SELLER]` (**8.000**), `Pisang Goreng Keju` (**8.000**), `Pisang Goreng Coklat` (**8.000**), `Pisang Goreng Punakawan [BEST SELLER]` (**10.000**), `Tahu` (**6.000**), `Tempe Mendoan` (**6.000**), `Otak-Otak` (**8.000**).
   * *Footer Papan:* `TAMBAHAN RP. 2000,- UNTUK PACKING TAKE AWAY`.
3. **Papan 3 — MINUMAN (26 Menu Minuman):**
   * `Teh Panas` (**3.000**), `Es Teh` (**3.000**), `Teh Kampul` (**4.000**), `Es Teh Kampul` (**4.000**), `Teh Tarik` (**5.000**), `Es Teh Tarik [BEST SELLER]` (**5.000**), `Jeruk Panas` (**5.000**), `Es Jeruk` (**5.000**), `Kopi Hitam` (**5.000**), `Wedang Jahe` (**7.000**), `Wedang Susu Jahe` (**9.000**), `Es Susu Jahe` (**9.000**), `Wedang Punakawan [BEST SELLER]` (**10.000**), `Beng-Beng` (**4.000**), `Chocolatos` (**4.000**), `Nutrisari` (**3.000**), `Hilo` (**5.000**), `Milo` (**5.000**), `Dancow` (**6.000**), `Susu Putih` (**5.000**), `Susu Coklat` (**5.000**), `Coffeemix` (**4.000**), `Good Day` (**4.000**), `Air Mineral` (**4.000**), `Teh Pucuk` (**5.000**), `Badak + Es Batu [BEST SELLER]` (**17.000**).

---

### 3.5. MOD-05: Seksi Order Online — Tersedia 3 Opsi Merchant: GoFood, ShopeeFood, GrabFood (`#order`)

Bagian ini dirancang khusus untuk memfasilitasi pemesanan pesan-antar (*delivery*) melalui **3 Opsi Merchant Resmi** ditambah banner reservasi/Take Away via WhatsApp:

* **Sub-label Seksi:** `🛵 TERSEDIA 3 OPSI MERCHANT: GOFOOD, SHOPEEFOOD & GRABFOOD`
* **Judul Seksi (`H2`):** `Order Menu Punakawan di Aplikasi Favoritmu!`
* **Grid 3 Kartu Merchant Resmi (3 Kolom Sejajar pada Desktop):**

| Urutan Kartu | Nama Merchant | Warna Identitas & Badge | Judul Kartu (`H3`) | Tombol Aksi (CTA) |
| :--- | :--- | :--- | :--- | :--- |
| **Opsi Merchant 1** | **GoFood** | Merah GoFood (`#EE2737`)<br>*Badge:* `Pengantaran Cepat & Hangat` | **Pesan via GoFood** | **`Buka GoFood Sekarang ↗`** |
| **Opsi Merchant 2** | **ShopeeFood** | Oranye-Merah (`#EE4D2D`)<br>*Badge:* `Voucher Diskon & Gratis Ongkir` | **Pesan via ShopeeFood** | **`Buka ShopeeFood Sekarang ↗`** |
| **Opsi Merchant 3** | **GrabFood** | Hijau Grab (`#00B14F`)<br>*Badge:* `Promo Makan Bareng Teman` | **Pesan via GrabFood** | **`Buka GrabFood Sekarang ↗`** |

* **Banner Horizontal Bawah 3 Merchant (Latar Teal `#1E3F47`, Border Emas `#D4A857`):**
  * Teks Kiri: `🍱 Mau pesan Take Away tanpa antre atau booking meja untuk kumpul komunitas/bukber di Colomadu?`
  * Tombol Kanan (`#FFCC00`): **`Pesan & Reservasi via WhatsApp (0896-5355-7758) ↗`**

---

### 3.6. MOD-06: Galeri Suasana Tempat & Formulir Reservasi WhatsApp (`#suasana`)
* **2 Kartu Spot Foto Tempat Asli (Atas):**
  1. **Area Semi-Outdoor Atap Bambu & Meja Kayu** (`tempat-bambu-malam.jpg` / Slot Kosong 1)
  2. **Area Kasir & Kapasitas Meja Rombongan** (`tempat-area-kasir.jpg` / Slot Kosong 2)
* **Layout 2 Kolom Informasi Lokasi & Formulir Interaktif (Bawah):**
  * **Kolom Kiri:** Informasi keunggulan ruang nongkrong, lokasi di Colomadu, WhatsApp `0896 5355 7758`, serta Instagram & TikTok `@punakawanspaceeatery`.
  * **Kolom Kanan (Kartu Formulir `Reservasi Meja / Pesan Partai`):** Input *Nama Pemesan / Komunitas*, *Jumlah Orang / Porsi*, *Pilihan Keperluan* (`Reservasi Meja Nongkrong`, `Pesan Take Away`, `Booking Acara / Kumpul Komunitas`), dan *Catatan Menu / Jam Kedatangan* yang langsung terformat otomatis ke WhatsApp `6289653557758`.

### 3.7. MOD-07: Artikel Edukasi SEO (Content Marketing) & Footer
* **Artikel Content Marketing (2 Kolom):** Berjudul *"Rekomendasi Tempat Nongkrong & Kuliner Rakyat Murah di Colomadu: Kenapa Punakawan Space & Eatery Wajib Masuk Daftar Favoritmu"* untuk meningkatkan *Average Engagement Time* dan menurunkan *Bounce Rate*.
* **Footer Resmi:** Menampilkan identitas Punakawan Space & Eatery, tautan navigasi cepat, serta tautan langsung ke **3 Opsi Merchant (GoFood, ShopeeFood, GrabFood)** dan sosial media resmi.

---

## 4. Strategi SEO, Skenario A/B Testing & Target KPI (Topik 3 UAS)

### 4.1. Daftar 10 Target Keywords SEO Lokal
1. `punakawan space and eatery` (*Navigational*)
2. `warmindo punakawan colomadu` (*Local Navigational*)
3. `kuliner rakyat colomadu` (*Commercial*)
4. `tempat nongkrong murah colomadu` (*Local Transactional*)
5. `mie goreng punakawan` (*Commercial*)
6. `wedang punakawan` (*Commercial*)
7. `wonton basah colomadu` (*Transactional*)
8. `paket nasi gratis es teh colomadu` (*Transactional*)
9. `gofood shopeefood grabfood punakawan colomadu` (*Transactional Delivery*)
10. `tempat nongkrong dekat ums colomadu` (*Informational / Content Marketing*)

### 4.2. Skenario A/B Testing (Tahap 5 — Optimasi Sebelum vs Sesudah)
* **Versi A (Sebelum Optimasi):** Halaman statis sederhana tanpa filter kategori pada 9 Menu Best Seller, tanpa rincian 3 papan harga lengkap, dan tanpa kartu 3 opsi merchant (*Bounce Rate* awal tinggi di kisaran $68\% - 74\%$).
* **Versi B (Sesudah Optimasi — Desain Saat Ini):** Penambahan filter interaktif **9 Menu Best Seller**, **3 Papan Daftar Harga Resmi**, **3 Opsi Merchant (GoFood, ShopeeFood, GrabFood)**, formulir reservasi WA, dan artikel SEO (*Bounce Rate* turun signifikan ke kisaran $25\% - 32\%$).

### 4.3. Rumus Pengukuran KPI Utama
* **Click-Through Rate ($CTR$ Organik — Google Search Console):**
  $$\text{CTR} = \left( \frac{\text{Total Klik Organik}}{\text{Total Tayangan (Impressions)}} \right) \times 100\%$$
* **Bounce Rate ($BR$ — Google Analytics 4):**
  $$\text{Bounce Rate} = \left( \frac{\text{Sesi Satu Halaman Tanpa Interaksi}}{\text{Total Sesi Pengunjung}} \right) \times 100\%$$