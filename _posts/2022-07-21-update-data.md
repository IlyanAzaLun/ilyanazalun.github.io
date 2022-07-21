---
title: Update Data
tags: [Request, Data, Database]
style: 
color: 
description: When update information in database.
---

Source: [Experience]

Ketika akan update informasi pada sebuah database, diharuskan untuk mengambil semua data yang akan di ubah, dan lakukan deklarasi pada informasi yang di ambil,
primary key (`id`) akan digunakan untuk mengubah informasi yang ada di database, berdasarkan informasi yang akan di ubah.


## Contoh Persiapan 
Request berdasarkan kode item
```
SELECT * FROM tbl where kode_item = kode_item
```
lakukan deklarasi pada hasil request pada database, dan
ubah informasi hasil deklarasi yang di dapatkan dari hasil request tersebut,
## Contoh Hasil Request
``
{
	brand: "BED",
	brands: null,
	category: "ACC",
	id: "11",
	is_active: "1",
	item_broken: "0",
	item_capital_price: "35000",
	item_code: "ACC-000011",
	item_name: "AWT BATTERY GREEN 2400MAH",
	item_quantity: "0",
	item_selling_price: "40000",
	item_unit: "PCS",
	note: "BED 2022",
	weight: 0
}
``
## Contoh Request Ubah Data
``
{
	id: "11",
	item_name: "AWT BATTERY GREEN 2400MAH NEW",
	item_quantity: "123",
	item_selling_price: "41000",
}
``