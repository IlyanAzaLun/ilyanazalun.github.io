---
name: Inventory Management
tools: [Codeigniter, PHP, MariaDB, JavaScript]
image: https://ilyanazalun.github.io/assets/image/management-inventory/screenshot-management.local-2021.11.14-11_14_05.png
description: Membangun sebuah website inventory online berbasis web.
external_url: #
---

## Item management
fitur manajemen barang, input brang yang belum tersedia. ubah data, menampilkan data barang.
![preview]({{'/assets/image'|relative_url}}/management-inventory/screenshot-management.local-2021.12.02-12_26_21.png)
kondisi untuk category ``LIQUID`` field akan ditambahkan
![preview]({{'/assets/image'|relative_url}}/management-inventory/screenshot-management.local-2021.12.02-12_27_46.png)
``controller`` yang digunakan pada fitur ini yaitu ``Item``

### History item
pada fitur ini di perlihatkan informasi riwayat pemasukan dan pengeluaran barang.


## User management
fitur manajemen pengguna, dibagi menjadi 3 bagian yaitu customer(pelanggan) dan supplier(pemasok), dan user(pengguna). dari user (pengguna) yang dapat mengakses aplikasi dibagi menjadi beberapa level, berdasarkan izin untuk mengakes halaman.

## Role management
menampilkan informasi yang terseida, peran pengguna di tampilkan berdasarkan halaman yand dapat dakses tiap peran user (pengguna)

## Menu management
manajemen menu, untuk siapasaja menu tersebut dapat diakses.

## List User
menamplkan user (pengguna) yang dapat mengakses aplikasi.

## Invoice
invoice dibagi menjadi 2 halaman yaitu, halaman invoice pembelian, dan invoice penjualan.

### Invoice purchase
invoice pembelian digunakan untuk mencatat barang yang telah dipesan. persediaan barang (stock item) akan berambah, jika invoice ditambahkan.

### Invoice sale
invoice penjualan digunakan untuk mencatat barang yang akan dijual, diambil dari data master barang, (stok item) akan berkurang, jika invoice ditambahkan

### Return
pengembalian / batal transaksi, persediaan akan kembali pada sebelum invoice di buat.

![preview]({{'/assets/image'|relative_url}}/management-inventory/screenshot-management.local-2021.11.14-11_15_44.png)