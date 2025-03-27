# Bahan Ajar 3 Pertemuan 4

#  input (Youtube Elearning)
print('Hasil Ujian')
nilai = int(input('masukkan nilai'))

# proses
if nilai > 90 :
    Transkip = 'A+'
elif nilai > 80 :
    Transkip = 'A+'
elif nilai > 70 :
    Transkip = 'A+'
elif nilai > 60 :
    Transkip = 'B-'
elif nilai > 50 :
    Transkip = 'C-'
elif nilai > 40 :
    Transkip = 'D'
elif nilai > 30 :
    Transkip = 'E'
elif nilai : 
    Transkip = 'F'

# output
print('Transkip :',Transkip)
print('-----------------------')

# Bahan Ajar 3 Pertemuan 4

#  input
print('Hasil Ujian')
try:
    nilai = int(input('Masukkan nilai (0-100): '))

    # Proses
    if 30 <= nilai <= 100:
        if nilai > 90:
            transkrip = 'A+'
        elif nilai > 80:
            transkrip = 'A'
        elif nilai > 70:
            transkrip = 'B+'
        elif nilai > 60:
            transkrip = 'B'
        elif nilai > 50:
            transkrip = 'C'
        elif nilai > 40:
            transkrip = 'D'
        else:
            transkrip = 'E'
        
        # Output
        print(f'Transkrip: {transkrip}')
    else:
        print('Nilai harus antara 0 dan 100.')
except ValueError:
    print('Input tidak valid. Harap masukkan angka.')
print('-----------------------')
