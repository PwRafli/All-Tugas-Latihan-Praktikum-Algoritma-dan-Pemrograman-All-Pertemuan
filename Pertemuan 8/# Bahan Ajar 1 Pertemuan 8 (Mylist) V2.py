#   Bahan Ajar 1 Pertemuan 8 (Mylist) V.2

# Inisialisasi list
mylist = []

mylist.append("Andi")
mylist.append("Budi")
mylist.append("Citra")

print("Daftar Nama dalam mylist:")
for nama in mylist:
    print(nama)

mylist.remove("Budi")

print("\nSetelah 'Budi' dihapus:")
for nama in mylist:
    print(nama)

print(f"\nTotal nama dalam mylist: {len(mylist)}")