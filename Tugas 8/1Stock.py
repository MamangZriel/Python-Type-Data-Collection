# Data awal
barang = ["Laptop", "HP", "Headphone", "Mouse", "Keyboard"]
stok = [10, 20, 15, 25, 30]

# a. Tambahkan barang baru bernama "Monitor" dengan stok awal 12 ke dalam list
barang.append("Monitor")
stok.append(12)

# b. Hapus barang "Mouse" dari daftar barang dan stoknya
index_mouse = barang.index("Mouse")
barang.pop(index_mouse)
stok.pop(index_mouse)

# c. Perbarui stok untuk barang "Keyboard" menjadi 40
index_keyboard = barang.index("Keyboard")
stok[index_keyboard] = 40

# d. Hitung total stok semua barang
total_stok = sum(stok)

# Output hasil
print("Daftar Barang:", barang)
print("Daftar Stok:", stok)
print("Total Stok Semua Barang:", total_stok)