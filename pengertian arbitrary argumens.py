def total(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

# Memanggil fungsi dengan beberapa argumen
print(total(5, 10))           # Output: 15
print(total(2, 4, 6, 8))      # Output: 20
print(total(1, 2, 3, 4, 5))   # Output: 15