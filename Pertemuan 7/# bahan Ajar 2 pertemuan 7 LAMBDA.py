# bahan Ajar 2 pertemuan 7 LAMBDA

# fuction
def hitungan(p, l):
    luas = p + l
    return luas

print('luas tanah (function):', hitungan(345, 12))

# Lambda function
luas = lambda p, l: p + l
print('luas tanah (lambda):', luas(23, 780))

# Menyimpan lambda ke variabel sebelum dicetak
luas2 = lambda p, l: p + l
print('luas tanah (lambda_2):', luas2(100, 50))