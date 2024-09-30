#login sederhana dengan nama, nim, pin
print("-------- LOGIN --------")
while True:
    try:
        Username = int(input("Masukkan NIM anda: "))
        pin = int(input("Masukkan Pin anda: "))
        if Username == 2409116002 and pin == 827660:
            print("----- Selamat datang Nurhidayah! -----")
        else: 
            print("----- Username & Password Tidak Sesuai -----")
        break
    except ValueError:
        print("Username dan Passworsd Salah! Silahkan coba lagi")

while True:
    print("--- Tampilan Awal ---")
    print("A. Selanjutnya")
    print("B. Keluar")

    pilih = input("Pilihan (A atau B): ")

    if pilih == "A":
        #Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian
        barang_yang_dibeli = int(input("Masukkan harga barang (Rp.): "))
        jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
        
        total = barang_yang_dibeli * jumlah_pembelian
        
        if  total > 250000:
            diskon = total * 0.25
            total_harga_setelah_mendapatkan_diskon = total - diskon
            print(f"Selamat! Anda telah mendapatkan diskon sebesar 25%! Total harga setelah mendapatkan diskon = {total_harga_setelah_mendapatkan_diskon}: ")
        else:
            print(f"Total harga : Rp. {total}")
            print("Sayang sekali anda tidak mendapatkan diskon, silahkan coba dilain waktu terimakasih!")
        break
    elif pilih == "B":
        print("Terimakasih telah berbelanja di toko ini. Sampai jumpa!")
        break
    else:
        print("Error")