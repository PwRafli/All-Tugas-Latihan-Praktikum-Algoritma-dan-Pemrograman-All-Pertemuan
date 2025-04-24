# Fuction 1 bahan ajar 1 pertemuan 7
# Function Pembagian
def bagi(angka1, angka2):
    if angka2 == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        hasil = angka1 / angka2
        print('hasil pembagian :', hasil)
    print('---------------------------')

# Function Perkalian
def kali(angka1, angka2):
    hasil = angka1 * angka2
    print('hasil perkalian :', hasil)
    print('---------------------------')


# Fuction 2
# Function Perkalian lalu Ditambah
def kali_dan_tambah(angka1, angka2, tambah):
    hasil = (angka1 * angka2) + tambah
    print('hasil (perkalian + tambah) :', hasil)
    print('---------------------------')