def data_mahasiswa(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

# Memanggil fungsi dengan beberapa keyword arguments
data_mahasiswa(nama="imel", umur=19, jurusan="Sistem informasi", angkatan=2024)