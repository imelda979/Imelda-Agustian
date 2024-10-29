# Membuat sebuah list
buah = ["apel", "jeruk", "mangga", "anggur"]

# Menampilkan seluruh elemen list
print("Daftar Buah:", buah)

# Mengakses elemen tertentu dalam list berdasarkan indeks
print("Buah pertama:", buah[0])  # Output: apel
print("Buah terakhir:", buah[-1])  # Output: anggur

# Menambahkan elemen baru ke dalam list
buah.append("pisang")
print("Daftar Buah setelah ditambah:", buah)

# Mengubah elemen dalam list
buah[1] = "lemon"
print("Daftar Buah setelah diubah:", buah)

# Menghapus elemen dari list
buah.remove("mangga")
print("Daftar Buah setelah dihapus:", buah)

# Mengurutkan list
buah.sort()
print("Daftar Buah setelah diurutkan:", buah)