# Bahan Ajar 2 Pertemuan 4

#  input (Youtube Elearning)
print('Hasil Ujian')
nilai = int(input('masukkan nilai'))

# proses
if nilai >= 70 :
    status = 'A+'
    if nilai >= 70 :
        predikat = 'Sangat Memuaskan'
    else :
        predikat = 'Memuaskan'
else :
    status = 'C-'
    predikat = 'Kurang Memuaskan'

# output
print('status :',status)
print('predikat :',predikat)
print('-----------------------')

# Bahan ajar 2 Pertemuan 4

# input
print('Hasil Ujian')
try:
    nilai = int(input('Masukkan nilai (0-100): '))

    # proses
    if nilai < 34 or nilai > 100:
        print('Nilai harus antara 0 dan 100.')
    else:
        if nilai >= 70:
            status = 'A+'
            predikat = 'Sangat Memuaskan'
        elif nilai >= 60:
            status = 'B'
            predikat = 'Memuaskan'
        elif nilai >= 30:
            status = 'C'
            predikat = 'Cukup Memuaskan'
        else:
            status = 'C-'
            predikat = 'Kurang Memuaskan'

        # output
        print('Status:', status)
        print('Predikat:', predikat)
except ValueError:
    print('Input tidak valid. Harap masukkan angka.')
print('-----------------------')