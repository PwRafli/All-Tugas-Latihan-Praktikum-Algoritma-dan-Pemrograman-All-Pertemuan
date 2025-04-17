# PARAMETER FUNCTION Bahan Ajar 2 Pertemuan 6

def sapa(user):
    print("Please Log-in")
    print("Administrasi~")
    print("WELLCOME Back",user)
    print("----")
sapa('Doctor')

# contoh 2
def jumlah(angka1, angka2):
    hasil = angka1 + angka2
    print('➕ Hasil penjumlahan:', hasil)
    print('---------------------')

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print('➖ Hasil pengurangan:', hasil)
    print('---------------------')

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print('✖️ Hasil perkalian:', hasil)
    print('---------------------')

# Panggil fungsi
jumlah(34, 5)
kurang(10, 7)
kali(14, 7)