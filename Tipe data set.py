# Membuat set dengan beberapa elemen
fruits = {"apel", "pisang", "jeruk", "mangga"}

# Menampilkan isi set
print("Isi set fruits:", fruits)

# Menambahkan elemen baru ke dalam set
fruits.add("anggur")
print("Setelah menambahkan 'anggur':", fruits)

# Menghapus elemen dari set
fruits.remove("pisang")
print("Setelah menghapus 'pisang':", fruits)

# Menggunakan operasi himpunan
other_fruits = {"apel", "melon", "kiwi"}

# Union: menggabungkan dua set
all_fruits = fruits.union(other_fruits)
print("Hasil union:", all_fruits)

# Intersection: mendapatkan elemen yang ada di kedua set
common_fruits = fruits.intersection(other_fruits)
print("Hasil intersection:", common_fruits)

# Difference: mendapatkan elemen yang hanya ada di satu set
unique_fruits = fruits.difference(other_fruits)
print("Hasil difference:", unique_fruits)



