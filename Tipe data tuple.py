# Membuat sebuah tuple
hewan = ("kucing", "anjing", "burung", "ikan")

# Menampilkan seluruh elemen tuple
print("Daftar Hewan:", hewan)

# Mengakses elemen tertentu dalam tuple berdasarkan indeks
print("Hewan pertama:", hewan[0])  # Output: kucing
print("Hewan terakhir:", hewan[-1])  # Output: ikan

# Menghitung jumlah elemen dalam tuple
jumlah_hewan = len(hewan)
print("Jumlah hewan:", jumlah_hewan)

# Menghitung frekuensi elemen tertentu
frekuensi_kucing = hewan.count("kucing")
print("Frekuensi 'kucing' dalam tuple:", frekuensi_kucing)

# Mencari indeks dari elemen tertentu
indeks_burung = hewan.index("burung")
print("Indeks 'burung':", indeks_burung)