# Bahan Ajar 1 pertemuan 5

# WHILE LOOP(Youtube Elearning)
nilaiawal = 1
while nilaiawal <= 200 :
    print('pengulangan ke :',nilaiawal)
    nilaiawal += 1

# Bahan Ajar 1 pertemuan 5

# WHILE LOOP
password = ""
while password != "apolo3456":
    password = input("Masukkan password: ")
print("Password benar, akses diberikan!")

# WHILE LOOP
num = 0
while num < 60:
    num += 1
    if num == 10:
        continue  # Lewati angka 10
    if num == 50:
        break  # Hentikan loop saat angka 50
    print("Angka:", num)