# Membuat kamus
data_mahasiswa = {
    "nama": "Andi",
    "umur": 21,
    "jurusan": "Teknik Informatika",
    "nilai": [85, 90, 78],  # Nilai dalam bentuk list
}

# Mengakses nilai dalam kamus
print("Nama:", data_mahasiswa["nama"])
print("Umur:", data_mahasiswa["umur"])
print("Jurusan:", data_mahasiswa["jurusan"])
print("Nilai:", data_mahasiswa["nilai"])

# Menambahkan pasangan kunci-nilai baru
data_mahasiswa["alamat"] = "Jakarta"
print("\nData setelah menambahkan alamat:", data_mahasiswa)

# Mengubah nilai pada kunci yang sudah ada
data_mahasiswa["umur"] = 22
print("\nData setelah memperbarui umur:", data_mahasiswa)

# Menghapus pasangan kunci-nilai
del data_mahasiswa["nilai"]
print("\nData setelah menghapus nilai:", data_mahasiswa)

# Mengakses semua kunci dan nilai
print("\nKunci-kunci dalam kamus:", data_mahasiswa.keys())
print("Nilai-nilai dalam kamus:", data_mahasiswa.values())

# Menggunakan loop untuk mencetak setiap pasangan kunci-nilai
for kunci, nilai in data_mahasiswa.items():
    print(f"{kunci}: {nilai}")