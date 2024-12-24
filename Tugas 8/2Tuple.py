# Data pesanan
pesanan = [
    (101, "Laptop", 4, 15000000),
    (102, "HP", 2, 3000000),
    (103, "Headphone", 1, 500000),
    (104, "Keyboard", 4, 400000),
    (105, "Mouse", 5, 100000)
]

# a. Tampilkan semua data pesanan
for p in pesanan:
    print(f"ID Pesanan: {p[0]}, Nama Barang: {p[1]}, Jumlah: {p[2]}, Harga per Unit: {p[3]}")

# b. Hitung total harga untuk setiap pesanan dan tampilkan
for p in pesanan:
    total_harga = p[2] * p[3]
    print(f"ID Pesanan {p[0]} - Total Harga: {total_harga}")

# c. Cari pesanan dengan ID 103 dan tampilkan
for p in pesanan:
    if p[0] == 103:
        print(f"Pesanan dengan ID 103: {p}")

# d. Hitung total harga dari semua pesanan
total_semua_harga = sum(p[2] * p[3] for p in pesanan)
print("Total Harga Semua Pesanan:", total_semua_harga)