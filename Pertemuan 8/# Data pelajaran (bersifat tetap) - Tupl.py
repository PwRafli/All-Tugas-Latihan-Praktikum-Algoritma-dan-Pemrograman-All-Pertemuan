# Data pelajaran (bersifat tetap) - Tuple
pelajaran_master = (
    ("P001", "Matematika"),
    ("P002", "Bahasa Indonesia"),
    ("P003", "Fisika"),
    ("P004", "Kimia"),
    ("P005", "Biologi"),
)

# Fungsi untuk menampilkan pelajaran
def tampilkan_pelajaran():
    print("Daftar Pelajaran:")
    for kode, nama in pelajaran_master:
        print(f"{kode} - {nama}")
    print()

# Data siswa dan pelajaran yang mereka ambil - List
data_siswa = [
    {"nama": "Adit", "pelajaran": ["P001", "P002", "P003"]},
    {"nama": "Bella", "pelajaran": ["P001", "P004", "P005"]},
    {"nama": "Citra", "pelajaran": ["P002", "P003", "P005"]},
]

# Fungsi untuk menampilkan data siswa dan pelajaran yang diambil
def tampilkan_data_siswa():
    print("Data Siswa dan Pelajaran:")
    for siswa in data_siswa:
        pelajaran = ', '.join(siswa['pelajaran'])
        print(f"{siswa['nama']}: {pelajaran}")
    print()

# Fungsi untuk mencari nama pelajaran dari kode
def cari_nama_pelajaran(kode):
    for k, nama in pelajaran_master:
        if k == kode:
            return nama
    return "Tidak Diketahui"

# Menggunakan Set untuk menghitung pelajaran unik
def pelajaran_unik():
    semua_pelajaran = set()
    for siswa in data_siswa:
        semua_pelajaran.update(siswa['pelajaran'])  # Tambah ke Set
    return semua_pelajaran

# Main Program
tampilkan_pelajaran()
tampilkan_data_siswa()

# Menampilkan pelajaran unik
unik = pelajaran_unik()
print("Pelajaran unik yang diambil oleh semua siswa:")
for kode in unik:
    print(f"{kode} - {cari_nama_pelajaran(kode)}")
