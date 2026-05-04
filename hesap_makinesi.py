print("Basit Hesap Makinesi")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("İşlem seçin (+, -, * veya /): ")

if islem == "+":
    sonuc = sayi1 + sayi2
    print(f"Sonuç: {sonuc}")
elif islem == "-":
    sonuc = sayi1 - sayi2
    print(f"Sonuç: {sonuc}")
elif islem == "*":
    sonuc = sayi1 * sayi2
    print(f"Sonuç: {sonuc}")
elif islem == "/":
    if sayi2 == 0:
        print("Hata: Bir sayı 0'a bölünemez.")
    else:
        sonuc = sayi1 / sayi2
        print(f"Sonuç: {sonuc}")
else:
    print("Geçersiz işlem seçtiniz.")
