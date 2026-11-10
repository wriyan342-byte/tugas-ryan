print("=== RUMAH SAKIT SEHAT ===")
print("DAFTAR PENYAKIT PASIEN")

print("1. Asma")
print("2. DBD")
print("3. Tifus")
print("4. Diabetes")
print("5. Hipertensi")
print("6. Anemia")
print("7. Maag")
print("8. Pneumonia")
print("9. TBC")
print("10. Usus Buntu")

pilihan = int(input("Pilih penyakit (1-10): "))
lama = int(input("Lama opname (hari): "))

if pilihan == 1:
    penyakit = "Asma"
    harga = 500000
elif pilihan == 2:
    penyakit = "DBD"
    harga = 700000
elif pilihan == 3:
    penyakit = "Tifus"
    harga = 600000
elif pilihan == 4:
    penyakit = "Diabetes"
    harga = 800000
elif pilihan == 5:
    penyakit = "Hipertensi"
    harga = 500000
elif pilihan == 6:
    penyakit = "Anemia"
    harga = 450000
elif pilihan == 7:
    penyakit = "Maag"
    harga = 400000
elif pilihan == 8:
    penyakit = "Pneumonia"
    harga = 750000
elif pilihan == 9:
    penyakit = "TBC"
    harga = 650000
elif pilihan == 10:
    penyakit = "Usus Buntu"
    harga = 3000000
else:
    penyakit = ""
    harga = 0

if pilihan >= 1 and pilihan <= 10 and lama >= 1:
    total = harga * lama

    print("\n=== DATA PASIEN ===")
    print("Penyakit:", penyakit)
    print("Lama opname:", lama, "hari")
    print("Biaya per hari: Rp", harga)
    print("Total biaya: Rp", total)

    if lama > 7:
        print("Status: Opname lama")
    else:
        print("Status: Opname normal")
else:
    print("Data tidak valid")