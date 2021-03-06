---
name: Inventory Management
tools: [Codeigniter, PHP, MariaDB, JavaScript]
image: https://ilyanazalun.github.io/assets/image/inventory-management/Dashboard.png
description: Membangun sebuah website inventory online berbasis web.
external_url: #
---

## Manajemen barang
Halaman ini hanya dapat diakses oleh: <code>ADMIN</code>
fitur manajemen barang, input brang yang belum tersedia. ubah data, menampilkan data barang.
![preview]({{'/assets/image'|relative_url}}/inventory-management/1.Manajemen barang.png)
pilih kategori untuk barang. kondisi untuk category ``LIQUID`` field akan ditambahkan, yaitu kebutuhan-kebutuhan untuk informasi liquid,
lengkapi form yang ada.
### Tambah persediaan barang
Halaman ini hanya dapat diakses oleh: <code>ADMIN</code>
tambah persediaan barang, digunakan setelah input barang, pilih terlebih dahulu barang yang dilakukan persediaan.
![preview]({{'/assets/image'|relative_url}}/inventory-management/2.Manajemen persediaan barang.png)
variabel yang diubah yaitu hanya jumlah barang.
![preview]({{'/assets/image'|relative_url}}/inventory-management/3.Manajemen persediaan barang (1).png)


## Manajemen pelanggan
Halaman ini hanya dapat diakses oleh: <code>ADMIN</code>
tambah pelanggan, lengkapi form field isian pada form tambah data pelanggan, kemudian simpan untuk menyimpan data pelanggan. data yang tersimpan akan ditampilkan pada, daftar pelanggan.  
![preview]({{'/assets/image'|relative_url}}/inventory-management/1.Manajemen pelanggan.png)
data yang telah disimpan, dapat diubah kembali sesuai informasi yang dibutuhkan. Pelanggan yang di nonaktifkan tidak akan digunakan dalam aplikasi.


<h2 id="notifikasi" style="color:#ed143d">Notifikasi</h2>
Semua halaman, dan semua intruksi akan menampilkan notifikasi di pojok kanan atas.
![preview]({{'/assets/image'|relative_url}}/inventory-management/4.Notifikasi.png)

## Gudang: buat antrian pemesanan barang
untuk membuat antrian barang. pengguna diharuskan mengisi form informasi terlebih dahulu, yaitu:
<li>Informasi pelanggan:</li>
informasi pelanggan diharuskan diinput terlebih dahulu di halaman "MANAJEMEN PELANGGAN", sehingga dapat digunakan di halaman ini.
<li>Informasi barang:</li>
informasi barang juga diharuskan diinput terlebih dahulu di halaman "MANAJEMEN BARANG", dan pastikan stok barang sudah di ubah di halaman "TAMBAH PERSEDIAAN BARANG" sehingga dapat digunakan di halaman ini.
![preview]({{'/assets/image'|relative_url}}/inventory-management/5.Buat antrian pesanan barang.png)
Data yang sudah di simpan akan di tampilkan di bagian ``Daftar pesanan keluar``, di bagian ``Daftar pesanan keluar``.
fitur yang di sediakan yaitu:
<li>Lihat informasi pesanan juga akan ditampilkan di halaman "SHIPPING", dan batal pesanan jika ada kesalahan pada pemesanan.</li>
<li>Batal pesanan.</li>
<li>Ubah status pesanan, yang seharusnya di gunakan oleh pihak pengiriman.</li>
pada bagian ``Daftar barang kembali, dari pengiriman``, yaitu informasi tentang barang kurang atau barang lebih.
pihak gudang diharuskan memeriksa jumlah barang yang di tampilkan pada layar ``informasi pengembalian barang``. setelah informasi dan barang di terima pihak gudang dapat melakukan ``konfirmasi pengembalian barang``.

## Gudang: detail informasi pemesanan dan pengembalian barang
tampilan untuk detail informasi pemaesanan dan pengembalian barang.
![preview]({{'/assets/image'|relative_url}}/inventory-management/5.Buat antrian pesanan barang (1).png)

## Pengemasan dan Pengiriman
pada halaman daftar antrian pesanan, terdapat bagian
<li>Daftar pemesanan keluar, bagian ini informasi pemesanan yang dibuat oleh gudang dan</li>
bila informasi sudah sesuai dengan barang yang di terima dari pihak gudang, bagian pengemasan dapat melakukan konformasi.
<li>Daftar barang kembali, dari pengemasan dan pengiriman, dibuat oleh bagian pengemasan</li>
daftar laporan barang kembali, merupakan perubahan kesalahan atau perubahan pada input barang.
![preview]({{'/assets/image'|relative_url}}/inventory-management/5.Buat antrian pesanan barang (1).png)

## Detail informasi pemesanan
tampilan untuk detail informasi pemaesanan barang.
![preview]({{'/assets/image'|relative_url}}/inventory-management/6.Daftar antrian pesanan barang dari gudang (1).png)
bila informasi tidak sesuai atau ada perubahan jumlah barang, maka dilakukan perubahan pemesanan., namun bila barang yang datang sudah sesuai maka pihak pengemasan dapa melakukan konfirmasi.

## Ubah informasi pemesanan
perubahan informasi pemesanan barang dilakukan oleh pihak pengemasan. dapat disesuaikan bedasarkan invoice dari marketing atau yang lainnya.
![preview]({{'/assets/image'|relative_url}}/inventory-management/7.Buat pengembalian barang ke gudang.png)
bila barang dari pemesanan kurang, penulisan yang benar yaitu di dahului  tanda (-) minus/negatif, yang artinya pihak pengemasan memerlukan barang lagi, namun <br>
bila barang dari pemesanan jumlahnya lebih dari permintaan, penulisan yang benar yaitu tanpa tanda, yang artinya pihak pengemasan mengembalikan barang kepihak gudang.