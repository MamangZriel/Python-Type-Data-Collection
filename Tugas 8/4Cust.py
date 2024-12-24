# Data pelanggan
pelanggan_hari_1 = {"Alif", "Budi", "Citra", "Dina", "Eka"}
pelanggan_hari_2 = {"Budi", "Citra", "Fahmi", "Gina", "Eka"}
pelanggan_hari_3 = {"Alif", "Gina", "Henry", "Eka", "Fahmi"}

# a. Tampilkan daftar pelanggan yang datang pada hari pertama saja
pelanggan_hari_1_saja = pelanggan_hari_1 - pelanggan_hari_2 - pelanggan_hari_3
print("Pelanggan hari pertama saja:", pelanggan_hari_1_saja)

# b. Tampilkan daftar pelanggan yang datang pada semua hari
pelanggan_semua_hari = pelanggan_hari_1 & pelanggan_hari_2 & pelanggan_hari_3
print("Pelanggan yang datang pada semua hari:", pelanggan_semua_hari)

# c. Tampilkan daftar pelanggan yang datang pada minimal dua hari
pelanggan_dua_hari = (pelanggan_hari_1 & pelanggan_hari_2) | \
                     (pelanggan_hari_2 & pelanggan_hari_3) | \
                     (pelanggan_hari_1 & pelanggan_hari_3)
print("Pelanggan yang datang minimal dua hari:", pelanggan_dua_hari)

# d. Tambahkan pelanggan baru bernama "Irma" ke hari kedua
pelanggan_hari_2.add("Irma")
print("Pelanggan hari kedua setelah ditambah:", pelanggan_hari_2)

# e. Hitung total pelanggan unik yang datang selama tiga hari
pelanggan_unik = pelanggan_hari_1 | pelanggan_hari_2 | pelanggan_hari_3
print("Total pelanggan unik selama tiga hari:", len(pelanggan_unik))