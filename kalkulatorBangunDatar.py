def menu() :
    print("Menu Utama:")
    print("1. Informasi Kalkulator")
    print("2. Kalkulator Matematika")
    print("3. Kalkulator Konversi Suhu")
    print("4. Kalkulator Menghitung Luas")
    print("\t a. Persegi")
    print("\t b. Persegi Panjang")
    print("\t c. Segitiga")
    print("5. Kalkulator Bilangan Prima")
    print("6. Keluar")
    
def informasi() :
    def waktu() :
        return "19 Januari 2023"
    def nama() :
        return "Febriana"
    def nim() :
        return "22SA31A116"
    def kelas() :
        return "TI 22C"
    
    while True:
        print("\nKalkulator ini dibuat pada : ", waktu())
        print("Kalkulator ini dibuat oleh :")
        print("- Nama \t: ", nama())
        print("- NIM \t: ", nim())
        print("- Kelas : ", kelas())
        reset = input("\nApakah Anda ingin melihat informasi tentang kalkulator ini lagi ? (Ya/Tidak)")
        if reset == ("Tidak"):
            print()
            print("=================================================================================")
            print()
            menu()
            break
            
def matematika():
    def tambah (a, b) :
        return a + b
    def kurang (a, b) :
        return a - b
    def kali (a, b) :
        return a * b
    def bagi(a, b) :
        return a / b

    while True :
        a = float(input("\nMasukkan bilangan pertama \t:"))
        b = float(input("Masukkan bilangan kedua \t:"))
        operator = input("Pilih operator (+, -, *, /) \t:")
    
        try :
            if operator == "+" :
                hasil1 = a + b
                print("\n%.2f + %.2f = %.2f" % (a, b, hasil1))
            
            elif operator == "-" :
                hasil2 = a - b
                print("\n%.2f - %.2f = %.2f" % (a, b, hasil2))
            
            elif operator == "*" :
                hasil3 = a * b
                print("\n%.2f * %.2f = %.2f" % (a, b, hasil3))
        
            elif operator == "/" :
                hasil4 = a / b
                print("\n%.2f / %.2f = %.2f" % (a, b, hasil4))
        
            else :
                print("\nOperator tidak dikenali oleh sistem.")
            
        except ZeroDivisionError:
            print("\n%2.f / %2.f = Tak Hingga" % (a, b,))
        
        reset = input("\nApakah Anda akan menghitung kembali ? (Ya/Tidak)")
        if reset == "Tidak" :
            print()
            print("==============================================================")
            print()
            menu()
            break

def konversisuhu():
    def rearmur (c) :
        return 4/5 * c
    def fahrenheit (c) :
        return (c * 9/5) + 32
    def kelvin (c) :
        return c + 273.15
    
    while True :
        c = float(input("\nMasukkan nilai suhu celcius: "))
        print("\nNilai suhu Celcius :", c, "C")
        print("Nilai dalam Rearmur :%.2f" % rearmur (c), "R")
        print("Nilai dalam Fahrenheit :%.2f" % fahrenheit (c), "F")
        print("Nilai dalam Kelvin :%.2f" % kelvin (c), "K")
        reset2 = input("\nApakah Anda ingin mengonversi kembali ? (Ya/Tidak)")
        if reset2 == "Tidak" :
            print()
            print("==============================================================")
            print()
            menu()
            break
        
def menghitungluas() :
    while True :
        print("\nBentuk Geometri :")
        print("a. Persegi")
        print("b. Persegi Panjang")
        print("c. Segitiga")
        bentuk = input("\nPilih bentuk geometri :")
        
        if bentuk == "a" :
            print("\nBentuk Geometri Persegi")
            sisi = float(input("Masukkan panjang sisi :"))
            luas1 = sisi*sisi
            print("Luas persegi adalah %.1f * %.1f = %.1f" % (sisi, sisi, luas1))
        elif bentuk == "b" :
            print("\nBentuk Geometri Persegi Panjang")
            panjang = float(input("Masukkan panjang :"))
            lebar = float(input("Masukkan lebar :"))
            luas2 = panjang * lebar
            print("Luas persegi panjang adalah %.1f * %1.f = %.1f" % (panjang, lebar, luas2))
        elif bentuk == "c" :
            print("\nBentuk Geometri Segitiga")
            alas = float(input("Masukkan alas :"))
            tinggi = float(input("Masukkan tinggi :"))
            luas3 = alas * tinggi /2
            print("Luas segitiga adalah %.1f * %.1f / 2 = %.1f" % (alas, tinggi, luas3))
        else :
            print("\nBentuk geometri tidak dikenali")
        reset3 = input("\nApakah Anda ingin menghitung luas kembali ? (Ya/Tidak)")
        if reset3 == "Tidak" :
            print()
            print("==============================================================")
            print()
            menu()
            break
def bilanganprima() :
    while True :
        y = int(input("\nMasukkan bilangan awal :"))
        z = int(input("Masukkan bilangan akhir :"))

        list_bilangan = [i for i in range(y, z +1)]

        bilangan_prima = []
        for i in list_bilangan :
            if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
                bilangan_prima.append(i)
        print(bilangan_prima)
        reset4 = input("\nApakah Anda ingin menampilkan bilagan prima lagi ? (Ya/Tidak)")
        if reset4 == "Tidak" :
            print()
            print("==================================================================")
            print()
            menu()
            break

    
def keluar() :
    print("\n===========================================================")
    print("Terima kasih telah menggunakan Aplikasi Kalkulator 'Moon'.\n\t       Semoga harimu menyenangkan.")
    print("===========================================================")

print("Selamat datang di Aplikasi Kalkulator 'Moon'")
print()
print("============================================")
print()
while True :
    mulai = input("Apakah Anda ingin melanjutkan menggunakan kalkulator ini ? (Ya/Tidak)")
    if mulai == "Ya" :
        print()
        menu()
        break

while 1 :
    pilih = input("\nMasukkan pilihan menu :")
    if pilih == "1" :
        informasi()
    elif pilih == "2" :
        matematika()
    elif pilih == "3" :
        konversisuhu()
    elif pilih == "4" :
        menghitungluas()
    elif pilih == "5" :
        bilanganprima()
    elif pilih == "6" :
        keluar()
        break
    else :
        print("Pilihan tidak dikenali oleh sistem")