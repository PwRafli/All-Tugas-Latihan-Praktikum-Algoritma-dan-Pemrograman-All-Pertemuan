#   Bahan Ajar 3 Pertemuan 8 (SET) V.2

# Membuat set
mySet = set()

# Menambahkan item ke set
mySet.add("KEYCAPS")
mySet.add("KEYBOARD")
mySet.add("SWICHT")
mySet.add("BERBON")  # Item duplikat, tidak akan ditambahkan

# Menampilkan isi set
print("Isi dari mySet:")
for buah in mySet:
    print(buah)

# Menghapus item dari set
mySet.remove("SWICHT")

# Menampilkan set setelah penghapusan
print("\nSetelah menghapus 'SWICHT':")
print(mySet)

# Menampilkan jumlah item unik
print(f"\nJumlah item unik dalam mySet: {len(mySet)}")
