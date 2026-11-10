print("=== APOTEK SEHAT ===")

daftar_beli = []
total_semua = 0

while True:
    print("\nDAFTAR OBAT")
    print("1. Paracetamol - 5000")
    print("2. Amoxicillin - 12000")
    print("3. Vitamin C - 8000")
    print("4. Antasida - 6000")
    print("5. OBH - 10000")
    print("6. Ibuprofen - 9000")
    print("7. CTM - 4000")
    print("8. Antalgin - 7000")
    print("9. Betadine - 11000")
    print("10. Oralit - 3000")

    pilihan = int(input("\nPilih obat (1-10): "))
    jumlah = int(input("Jumlah obat: "))

    if pilihan == 1:
        nama = "Paracetamol"
        harga = 5000
    elif pilihan == 2:
        nama = "Amoxicillin"
        harga = 12000
    elif pilihan == 3:
        nama = "Vitamin C"
        harga = 8000
    elif pilihan == 4:
        nama = "Antasida"
        harga = 6000
    elif pilihan == 5:
        nama = "OBH"
        harga = 10000
    elif pilihan == 6:
        nama = "Ibuprofen"
        harga = 9000
    elif pilihan == 7:
        nama = "CTM"
        harga = 4000
    elif pilihan == 8:
        nama = "Antalgin"
        harga = 7000
    elif pilihan == 9:
        nama = "Betadine"
        harga = 11000
    elif pilihan == 10:
        nama = "Oralit"
        harga = 3000
    else:
        nama = ""
        harga = 0

    if pilihan >= 1 and pilihan <= 10 and jumlah >= 1:
        subtotal = harga * jumlah

        daftar_beli.append([nama, jumlah, harga, subtotal])
        total_semua = total_semua + subtotal

        print("Obat berhasil ditambahkan!")
    else:
        print("Pilihan atau jumlah tidak valid")

    tambah = input("\nIngin membeli lagi? (ya/tidak): ")

    if tambah.lower() != "ya":
        break

# STRUK AKHIR
print("\n===== STRUK PEMBELIAN =====")

for data in daftar_beli:
    print("Nama obat:", data[0])
    print("Jumlah:", data[1])
    print("Harga:", data[2])
    print("Subtotal: Rp", data[3])
    print("----------------------")

print("Total belanja: Rp", total_semua)

if total_semua >= 50000:
    diskon = total_semua * 5 / 100
    print("Diskon 5%: Rp", int(diskon))
else:
    diskon = 0
    print("Diskon: Rp 0")

bayar = total_semua - diskon

print("Total bayar: Rp", int(bayar))
print("==========================")
print("Terima kasih telah berbelanja!")