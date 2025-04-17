# Function 1: Menghitung luas tanah
def tanah(panjang, lebar):
    print("Menghitung Luas Tanah:")
    print(f"Panjang = {panjang} meter")
    print(f"Lebar   = {lebar} meter")
    luas = panjang * lebar
    print(f"Luas    = {luas} m²")
    print("------------------------")
    return luas

# Function 2: Menghitung harga jual tanah
def harga(luas, hpm):
    print("Menghitung Harga Jual:")
    print(f"Luas tanah        = {luas} m²")
    print(f"Harga per meter²  = Rp{hpm}")
    jual = luas * hpm
    print(f"Total harga jual  = Rp{jual}")
    print("------------------------")

# Memanggil function
luas_tanah = tanah(7, 4)      # 5 meter x 3 meter
harga(luas_tanah, 10000)     # Harga per m² = 1000
