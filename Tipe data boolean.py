# Mendefinisikan variabel Boolean
is_raining = True
is_sunny = False

# Menggunakan Boolean dalam percabangan
if is_raining:
    print("Bawa payung, hujan sedang turun.")
else:
    print("Tidak perlu payung, cuaca cerah.")

# Operasi logika dengan Boolean
if is_raining and not is_sunny:
    print("Hujan, tetapi tidak ada matahari.")
elif is_raining and is_sunny:
    print("Hujan sambil terik, mungkin hujan matahari.")
else:
    print("Cuaca tenang.")

# Output dari variabel Boolean
print("is_raining:", is_raining)
print("is_sunny:", is_sunny)