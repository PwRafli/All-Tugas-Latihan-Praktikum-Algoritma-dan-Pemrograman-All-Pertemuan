#   Bahan Ajar 2 Pertemuan 8 (TUPLE) V.2

# Membuat Tuple
data_mahasiswa = ("1124102162", "Rafli Rahman.Efendy", "Teknik Informatika", 2022)

print("Data Mahasiswa:")
print(data_mahasiswa)

print("\nDetail Mahasiswa:")
print("NIM       :", data_mahasiswa[0])
print("Nama      :", data_mahasiswa[1])
print("Jurusan   :", data_mahasiswa[2])
print("Angkatan  :", data_mahasiswa[3])

print("\nMenampilkan elemen menggunakan perulangan:")
for item in data_mahasiswa:
    print(item)