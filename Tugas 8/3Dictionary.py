# Data awal
inventaris = {
    "B001": {"nama": "Laptop", "kategori": "Elektronik", "stok": 10},
    "B002": {"nama": "HP", "kategori": "Elektronik", "stok": 15},
    "B003": {"nama": "Meja", "kategori": "Furniture", "stok": 20},
    "B004": {"nama": "Kursi", "kategori": "Furniture", "stok": 12},
    "B005": {"nama": "Mouse", "kategori": "Elektronik", "stok": 25},
}

# a. Tampilkan semua data barang
for kode, data in inventaris.items():
    print(f"{kode}: [{data['nama']}] - [{data['kategori']}] (Stok: {data['stok']})")

# b. Tambahkan barang baru
inventaris["B006"] = {"nama": "Keyboard", "kategori": "Elektronik", "stok": 12}

# c. Perbarui stok barang dengan kode B002 menjadi 18
inventaris["B002"]["stok"] = 18

# d. Hapus barang dengan kode B003
inventaris.pop("B003")

# e. Tampilkan semua barang dalam kategori Elektronik
print("Barang kategori Elektronik:")
for data in inventaris.values():
    if data["kategori"] == "Elektronik":
        print(f"{data['nama']} (Stok: {data['stok']})")

# f. Hitung total stok semua barang
total_stok = sum(data["stok"] for data in inventaris.values())
print("Total Stok Semua Barang:", total_stok)