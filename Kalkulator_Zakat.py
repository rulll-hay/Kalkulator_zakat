def hitung_zakat_logam():
    print("")
    print("[-->     🪙 ANDA MASUK PERHITUNGAN ZAKAT MAL LOGAM MULIA 🪙       <--]")
    print("")
    print("Logam mulia yang dapat dizakatkan: \n1.Logam Emas\n2.Logam Perak")
    pick2 = int(input("Masukkan pilihan yang sesuai: "))
    if pick2 == 1:
        berat = float(input("💰 Masukkann berat emas yang anda miliki 💰 (gram): "))
        harga = float(input("Masukkan harga emas per gram saat ini (ANGKA): "))
        total_nilai = berat * harga
        nishab = 85 * harga
        if total_nilai >= nishab:
            zakat = 0.025 * total_nilai
            print(f"Total harta yang anda miiki: Rp.{total_nilai:,.2f}".replace(",", "."))
            print(f"Nishob: Rp.{nishab:,.2f}".replace(",", "."))
            print(f"Total harta yang anda zakat kan: Rp.{zakat:,.2f}".replace(",", "."))
        else:
            print(f"Total harta yang anda miiki: Rp.{total_nilai:,.2f}".replace(",", "."))
            print(f"Nishob: Rp.{nishab:,.2f}".replace(",", "."))
            print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")
    elif pick2 == 2:
        berat1 = float(input("💰 Masukkann berat perak yang anda miliki 💰 (gram): "))
        harga1 = float(input("Masukkan harga perak per gram saat ini: "))
        total_nilai1 = berat1 * harga1
        nishab1 = 595 * harga1
        if total_nilai1 >= nishab1:
            zakat1 = 0.025 * total_nilai1
            print(f"Total harta yang anda miiki: Rp.{total_nilai1:,.2f}".replace(",", "."))
            print(f"Nishob: Rp.{nishab1:,.2f}".replace(",", "."))
            print(f"Total harta yang anda zakat kan: Rp.{zakat1:,.2f}".replace(",", "."))
        else:
            print(f"Total harta yang anda miiki: Rp.{total_nilai1:,.2f}".replace(",", "."))
            print(f"Nishob: Rp.{nishab1:,.2f}".replace(",", "."))
            print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")
    else:
        print("Opsi tidak ada")
   
def hitung_zakat_tabungan():
    print("")
    print("[-->     🪙 ANDA MASUK PERHITUNGAN ZAKAT MAL TABUNGAN UANG 🪙       <--]")
    print("")
    harga2 = float(input("Masukkan harga emas per gram saat ini sebagai patokan nishab: "))
    total_tabungan = float(input("Masukkan tabungan uang anda: "))
    nishab = 85 * harga2
    print("Logam mulia yang dapat dizakatkan: \n1.Logam Emas\n2.Logam Perak")
    pick2 = int(input("Masukkan pilihan yang sesuai: "))
    if total_tabungan >= nishab:
        zakat = 0.025 * total_tabungan
        print(f"Total tabungan yang anda miliki: Rp.{total_tabungan:,.2f}".replace(",", "."))
        print(f"Nishob: Rp.{nishab:,.2f}".replace(",", "."))
        print(f"Total tabungan yang anda zakat kan: Rp.{zakat:,.2f}".replace(",", "."))
    else:
        print(f"Total harta yang anda miiki: Rp.{total_tabungan:.2f}".replace(",", "."))
        print(f"Nishob: Rp.{nishab:.2f}".replace(",", "."))
        print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")

def hitung_sapi():
    moo = int(input("Masukkan total sapi yang sudah anda ternak selama 1 tahun: "))
    if moo < 30:
        print("Jumlah sapi anda kurang dari nishob, tidak wajib zakat mal")
    if moo >= 30 and moo <= 39:
        print("Sapi yang anda zakatkan sebanyak 1 ekor sapi jantan atau betina berumur 1 tahun")
    elif moo >= 40 and moo <= 59:
        print("Sapi yang anda zakatkan sebanyak 1 ekor sapi jantan atau betina berumur 2 tahun")
    elif moo >= 60 and moo <= 69:
        print("Sapi yang anda zakatkan sebanyak 2 ekor sapi jantan atau betina berumur 1 tahun")
    elif moo >= 70 and moo <= 79:
        print("Sapi yang anda zakatkan sebanyak 1 ekor sapi jantan atau betina berumur 2 tahun dan \n1 ekor sapi jantan atau betina berumur 1 tahun")
    elif moo >= 80 and moo <= 89:
        print("Sapi yang anda zakatkan sebanyak 2 ekor sapi jantan atau betina berumur 2 tahun")
    elif moo >= 90 and moo <= 99:
        print("Sapi yang anda zakatkan sebanyak 3 ekor sapi jantan atau betina berumur 1 tahun")
    elif moo >= 100 and moo <= 109:
        print("Sapi yang anda zakatkan sebanyak 2 ekor sapi jantan atau betina berumur 2 tahun")
    elif moo >= 110 and moo <= 119:
        print("Sapi yang anda zakatkan sebanyak 1 ekor sapi jantan atau betina berumur 1 tahun dan \n2 ekor sapi jantan atau betina berumur 2 tahun")
    elif moo >= 120 and moo <= 129:
        print("Sapi yang anda zakatkan sebanyak 4 ekor sapi jantan atau betina berusia 1 tahun dan \n3 ekor sapi jantan atau betina berumur 2 tahun")
    elif moo >= 130 :
        devide1 = moo // 30
        sisa = moo % 30
        if sisa >= 40:
            devide2 = sisa // 40
        else:
            devide2 = 0
        print("Sapi yang anda zakatkan sebanyak: ")
        if devide1 > 0:
            print(f"-{devide1} ekor jantan atau betina berumur 1 tahun")
        if devide2 > 0:
            print(f"-{devide2} ekor jantan atau betina berumur 2 tahun")
    else:
        print("Opsi tidak ada")
        
        
        
def hitung_kambing():
    mbek = int(input("Masukkan total kambing yang sudah anda ternak selama 1 tahun: "))
    if mbek < 40:
        print("Jumlah kambing kurang dari nishob, tidak wajib zakat mal")
    elif mbek >= 40 and mbek <= 120:
        print("Kambing yang anda zakatkan sebanyak 1 ekor kambing betina berumur 1 tahun")
    elif mbek >= 121 and mbek <= 200:
        print("Kambing yang anda zakatkan sebanyak 2 ekor kambing betina berumur 1 tahun")
    elif mbek >= 201 and mbek <= 300:
        print("Kambing yang anda zakatkan sebanyak 3 ekor kambing betina berumur 1 tahun")
    elif mbek > 300:
        devide2 = int(mbek // 100)
        print(f"Kambing yang anda zakatkan sebanyak {devide2} ekor kambing betina berumur 1 tahun")
        
def hitung_unta():
    hee = int(input("Masukkan jumlah unta yan anda miliki: "))
    if hee < 5:
        print("Jumlah unta kurang dari nishob, tidak wajib zakat mal")
    elif hee >= 5 and hee <= 9:
        print("Jumlah yang anda zakatkan sebanyak 1 ekor kambing berumur 1 tahun ")
    elif hee >= 10 and hee <= 14:  
        print("Jumlah yang anda zakatkan sebanyak 2 ekor kambing berumur 1 tahun ")
    elif hee >= 15 and hee <= 19:   
        print("Jumlah yang anda zakatkan sebanyak 3 ekor kambing berumur 1 tahun ")
    elif hee >= 20 and hee <= 24:  
        print("Jumlah yang anda zakatkan sebanyak 4 ekor kambing berumur 1 tahun ")
    elif hee >= 25 and hee <= 35:   
        print("Jumlah Unta yang anda zakatkan sebanyak 1 ekor Unta berumur 2 tahun ")
    elif hee >= 36 and hee <= 45:
        print("Jumlah Unta yang anda zakatkan sebanyak 1 ekor Unta berumur 3 tahun ")  
    elif hee >= 46 and hee <= 60:
        print("Jumlah Unta yang anda zakatkan sebanyak 1 ekor Unta berumur 4 tahun ")
    elif hee >= 61 and hee <= 75:
        print("Jumlah Unta yang anda zakatkan sebanyak 1 ekor Unta berumur 5 tahun ")
    elif hee >= 76 and hee <= 90:
        print("Jumlah Unta yang anda zakatkan sebanyak 2 ekor Unta berumur 2 tahun ")
    elif hee >= 91 and hee <= 120:
        print("Jumlah Unta yang anda zakatkan sebanyak 2 ekor Unta berumur 3 tahun ")
    elif hee >= 121:
        hasilA = hee // 50
        sisa = hee % 50
        if sisa >= 40:
            hasilB = sisa // 40
        else:
            hasilB = 0
        print("Jumlah Unta yang anda zakatkan sebanyak:")
        if hasilA > 0:
            print(f"- {hasilA} ekor Unta betina umur 3 tahun ")
        if hasilB > 0:
            print(f"- {hasilB} ekor Unta betina umur 2 tahun ")
            
            
def hitung_zakat_ternak():
     print("")
     print("[-->     🪙 ANDA MASUK PERHITUNGAN ZAKAT MAL TERNAK 🪙       <--]")
     print("")
     print("Syarat ternak yang wajib dizakatkan:\n1. MENCAPAI NISHOB\n2. DIMILIKI SELAMA 1 TAHUN HIJRIAH\n3. MILIK PRIBADI\n4. BUKAN HEWAN PEKERJA")
     print("Apakah semua syarat tersebut terpenuhi? ")
     verif1 = input("Masukkan jawaban (sudah/belum): ").lower()
     if verif1 == "belum":
         print("Anda belum wajib membayar zakat mal")
     elif verif1 == "sudah":
         print ("")
         print("==============     ANDA BISA MEMBAYAR ZAKAT MAL HEWAN TERNAK     ==============")
         print("Hewan ternak yang dapat dizakatkan di zakat mal\n1. Sapi 🐄\n2. Kambing 🐏\n3. Unta 🐪")
         list2 = int(input("Masukkan pilihan hewan yang akan dizakatkan(angka): "))
         match list2:
            case 1:
             print ("")
             print("==============     Hewan yang anda akan zakatkan adalah SAPI 🐄     ==============")
             print("Apakah sapi anda sudah memenuhi syarat zakat mal?")
             verif = (input("Masukkan pilihan yang sesuai: ")).lower()
             if verif == "belum":
                 print("Maaf, anda belum bisa melakukan zakat karena ada syarat yang tidak terpenuhi")
             elif verif == "sudah":
                 hitung_sapi()
            
            case 2:
             print("")
             print("==============     Hewan yang anda akan zakatkan adalah KAMBING 🐏     ==============")
             print("Apakah kambing anda sudah memenuhi syarat zakat mal?")
             verif = (input("Masukkan pilihan yang sesuai (sudah/belum): ")).lower()
             if verif == "belum":
                 print("Maaf, anda belum bisa melakukan zakat karena ada syarat yang tidak terpenuhi")
             elif verif == "sudah":
                 hitung_kambing()
            
            case 3:
             print("")
             print("==============     Hewan yang anda akan zakatkan adalah UNTA 🐪     ==============")
             print("Apakah Unta anda sudah memenuhi syarat zakat mal?")
             verif = (input("Masukkan pilihan yang sesuai (sudah/belum): ")).lower()
             if verif == "belum":
                 print("Maaf, anda belum bisa melakukan zakat karena ada syarat yang tidak terpenuhi")
             elif verif == "sudah":
                 hitung_unta()
     
     else:
         print("Opsi tidak ada")

def hitung_zakat_panen():
    print("")
    print("[-->     🪙 ANDA MASUK PERHITUNGAN ZAKAT MAL HASIL PANEN 🪙       <--]")
    print("")
    verif = input("Apakah yang anda tanam termasuk makanan pokok? (ya/tidak): ").lower()
    if verif == "ya":
        food = input("Masukkan nama tumbuhan yang anda panen: ")
        panen = float(input(f"Masukan berat {food} yang anda panen (kg): "))
        harga1 = float(input(f"Masukkan harga {food} per kg saat ini: "))
        beras = float(input("Masukkan harga beras per kg saat ini sebagai patokan: "))
        mass = beras * 653
        total_panen = panen * harga1
        if total_panen >= mass :
            print("""Jenis - jenis pengairan pada sawah:\n
            1. Pengairan alami: Air Hujan, Sungai atau irigasi alam, Mata air yang mengalir sendiri\n
            2. Pengairan buatan: Pompa air, Pompa diesel, Tenaga Manusia\n
            3. Pengairan campuran: memakai alami dan buatan dalam satu masa tanam""")
            print("")
            pick2 = int(input("Masukkan pilihan yang sesuai dengan pengairan sawah yang anda pakai (ANGKA): "))
            match pick2:
                case 1:
                    print("")
                    print("Pengairan disawah anda menggunakan pengairan alami\nKadar zakat anda 10%.")
                    hasil1 = total_panen * 0.1
                    print(f"Total hasil panen anda dalam rupiah: Rp.{total_panen}, dengan berat {food} seberat {panen} kg.")
                    print(f"Nishob: Rp.{mass:,.2f}".replace(",","."))
                    print(f"Jumlah nominal pada panen {food} yang anda zakatkan ini sebesar Rp.{hasil1:,.2f}".replace(",","."))
                case 2:
                    print("")
                    print("Pengairan disawah anda menggunakan pengairan buatan\nKadar zakat anda 5%.")
                    hasil2 = total_panen * 0.05
                    print(f"Total hasil panen anda dalam rupiah: Rp.{total_panen}, dengan berat {food} seberat {panen} kg.")
                    print(f"Nishob: Rp.{mass:,.2f}".replace(",","."))
                    print(f"Jumlah nominal pada panen {food} yang anda zakatkan ini sebesar Rp.{hasil2:,.2f}".replace(",","."))
                case 3:
                    print("")
                    print("Pengairan disawah anda menggunakan pengairan campuran\nKadar zakat anda 7.5%.")
                    hasil3 = total_panen * 0.075
                    print(f"Total hasil panen anda dalam rupiah: Rp.{total_panen}, dengan berat {food} seberat {panen} kg.")
                    print(f"Nishob: Rp.{mass:,.2f}".replace(",","."))
                    print(f"Jumlah nominal pada panen {food} yang anda zakatkan ini sebesar Rp.{hasil3:,.2f}".replace(",","."))    
                case _:
                    print("Opsi tidak ada")
        else:
            print(f"Total panen anda sebesar Rp.{total_panen:,.2f}".replace(",","."))
            print(f"Nominal Nishob sebesar Rp.{mass:,.2f}".replace(",","."))
            print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")
    
    elif verif == "tidak":
        food1 = input("Masukkan nama tumbuhan yang anda panen: ")
        panen2 = float(input(f"Masukan berat {food1} yng anda panen (kg): "))
        bill = float(input(f"Masukkan harga {food1} per kg: "))
        b_oper = float(input(f"Masukkan biaya operasional anda selama membudidayakan {food1} ini: "))
        p_kot = float(input(f"Masukkan pendapatan kotor anda dari hasil panen {food1} ini: "))
        gold = float(input("Masukkan harga emas 1 gram saat ini sebagai patokan nishob: "))
        nisob = 85 * gold
        p_bersih = p_kot - b_oper
        if nisob <= p_bersih:
            zakat = 0.025 * p_bersih
            print(f"Pendapatan bersih anda sebesar Rp.{p_bersih:,.2f}".replace(",","."))
            print(f"Nominal Nishob sebesar Rp.{nisob:,.2f}".replace(",","."))
            print(f"Jumlah zakat yang anda keluarkan sebesar Rp.{zakat:,.2f}".replace(",","."))
        else:
            print(f"Pendapatan bersih anda sebesar Rp.{p_bersih:,.2f}".replace(",","."))
            print(f"Nominal Nishob sebesar Rp.{nisob:,.2f}".replace(",","."))
            print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")
            
def hitung_zakat_perdagangan():
    print("")
    print("[-->     🪙 ANDA MASUK PERHITUNGAN ZAKAT MAL PERDAGANGAN 🪙       <--]")
    print("")
    hutang = float(input("Masukkan hutang anda dalam jangka pendek untuk berdagang (Jika tidak ada isi 0): "))
    stok = float(input("Masukkan total kas dan total nominal harga barang dagang yang tersedia: "))
    gold = float(input("Masukkan harga emas 1 gram saat ini sebagai patokan nishab: "))
    nisab = 85 * gold
    harta_bersih = stok - hutang
    if harta_bersih >= nisab:
        hasil1 = 0.025 * harta_bersih
        print(f"Total harta bersih yang anda miliki: Rp.{harta_bersih:,.2f}".replace(",", "."))
        print(f"Nishob: Rp.{nisab:,.2f}".replace(",", "."))
        print(f"Jumlah zakat yang anda bayar sebesar Rp.{hasil1:,.2f}".replace(",","."))
    else:
        print(f"Total harta bersih yang anda miliki: Rp.{harta_bersih:,.2f}".replace(",", "."))
        print(f"Nishob: Rp.{nisab:,.2f}".replace(",", "."))
        print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")
        
def hitung_zakat_penghasilan():
    print("")
    print("[-->     🪙 ANDA MASUK PERHITUNGAN ZAKAT MAL PENGHASILAN 🪙       <--]")
    print("")
    gaji = float(input("Masukkan gaji anda dalam setahun: "))
    gold = float(input("Masukkan harga emas 1 gram saat ini sebagai patokan nishab: "))
    nisab = 85 * gold
    if gaji >= nisab:
        zakat = 0.025 * gaji
        print(f"Total gaji yang anda dapat per tahun: Rp.{gaji:,.2f}".replace(",", "."))
        print(f"Nishob: Rp.{nisab:,.2f}".replace(",", "."))
        print(f"Jumlah zakat yang anda bayar sebesar Rp.{zakat:,.2f} / tahun ".replace(",","."))
    else:
        print(f"Total gaji yang anda dapat per tahun: Rp.{gaji:,.2f}".replace(",", "."))
        print(f"Nishob: Rp.{nisab:,.2f}".replace(",", "."))
        print("Anda belum bisa dan belum wajib melakukan zakat mol karena kurang dari nishob")
    
    
while True:
    print ("")            
    print("------------------------     SELAMAT DATANG DI KALKULATOR ZAKAT MAL      ------------------------")
    print("")
    print("--> Zakat mal adalah zakat yang dikenakan atas harga yang dimiliki seseorang apabila telah mencapai nishab dan haul. ")
    print("--> Nishab adalah batas minimal harta atau barang yang wajib dizakatkan. ")
    print("--> Haul adalah waktu minimal kepemilikan harta sebelum zakat wajib dikeluarkan. ")
    print("")
    print("Apakah harta atau hewan ternak anda sudah 1 tahun / memenuhi Haul?\n1.Sudah\n2.Belum")
    pick = int(input("Masukkan pilihan (ANGKA): "))
    print("")

    if pick == 1:
        print("========         ANDA BISA MELAKUKAN ZAKAT MAL           =========")
        print("Macam - macam bentuk zakat yang disetorkan di zakat mal: ")
        print("1. Zakat Logam Mulia\n2. Zakat Uang Tabungan\n3. Zakat Hewan Ternak\n4. Zakat Hasil Panen\n5. Zakat Perdagangan\n6. Zakat Penghasilan")
        list = int(input("Masukkan pilihan bentuk zakat yang ingin anda setorkan (ANGKA): "))
        match list:
            case 1:
                hitung_zakat_logam()
            case 2:
                hitung_zakat_tabungan()
            case 3:
                hitung_zakat_ternak()
            case 4:
                hitung_zakat_panen()
            case 5:
                hitung_zakat_perdagangan()
            case 6:
                hitung_zakat_penghasilan()
            case _:
                print("Opsi tidak ada")
                
        
    elif pick == 2:
        print("Anda belum bisa melakukan zakat mal")
    else:
        ("Pilihan tidak valid")
    print("")
    repeat = input("Apakah anda ingin menghitung lagi (Y/T): ").lower()
    if repeat == "t":
        print ("TERIMA KASIH :)")
        break
