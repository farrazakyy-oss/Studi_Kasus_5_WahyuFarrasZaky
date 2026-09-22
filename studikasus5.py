def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    if jenis_kendaraan.lower() == "mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan.lower() == "motor":
        tarif_per_jam = 3000
    else:
        tarif_per_jam = 0
        print("Jenis kendaraan tidak valid lol")

    total_biaya = tarif_per_jam * lama_parkir
    return total_biaya

jenis_kendaraan = "motor"
jam_masuk = 6
jam_keluar = 16

lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("=== Struk Parkir ===")
print("Jenis kendaraan :", jenis_kendaraan)
print("Jam masuk       :", jam_masuk)
print("Jam keluar      :", jam_keluar)
print("Lama parkir     :", lama_parkir)
print("Total biaya     :", total_biaya)

