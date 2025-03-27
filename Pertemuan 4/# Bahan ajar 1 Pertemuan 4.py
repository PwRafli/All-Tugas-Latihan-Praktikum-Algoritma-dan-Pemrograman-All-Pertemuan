# Bahan ajar 1 Pertwmuan 4

#  input
print('Hasil Ujian')
nilai = int(input('masukkan nilai'))

# proses
if nilai >= 67 :
    status = 'Lulus'
else :
    status = 'Gagal'

# output
print('status :',status)
print('--------------------')

# Bahan ajar 1 Pertwmuan 4

# input
print('Hasil Ujian')
try:
    nilai = int(input('Masukkan nilai (0-100): '))

    # proses
    if nilai < 0 or nilai > 100:
        print('Nilai harus antara 0 dan 100.')
    else:
        if nilai >= 67:
            status = 'Lulus'
        else:
            status = 'Gagal'

        # output
        print('Status:', status)
except ValueError:
    print('Input tidak valid. Harap masukkan angka.')
print('--------------------')