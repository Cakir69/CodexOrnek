"""Basit komut satırı hesap makinesi.

Özellikler:
- Toplama, çıkarma, çarpma, bölme
- Sayı doğrulama
- Sıfıra bölme kontrolü
"""


def sayi_al(mesaj: str) -> float:
    """Kullanıcıdan geçerli bir sayı alır."""
    while True:
        deger = input(mesaj).strip()
        try:
            return float(deger)
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")


def islem_al() -> str:
    """Kullanıcıdan geçerli bir işlem alır."""
    gecerli_islemler = {"+", "-", "*", "/"}
    while True:
        islem = input("İşlem seçin (+, -, * veya /): ").strip()
        if islem in gecerli_islemler:
            return islem
        print("Hata: Geçersiz işlem. Sadece +, -, * veya / kullanın.")


def hesapla(sayi1: float, sayi2: float, islem: str) -> float:
    """Verilen işleme göre sonucu döndürür."""
    if islem == "+":
        return sayi1 + sayi2
    if islem == "-":
        return sayi1 - sayi2
    if islem == "*":
        return sayi1 * sayi2
    if sayi2 == 0:
        raise ZeroDivisionError("Bir sayı 0'a bölünemez.")
    return sayi1 / sayi2


def main() -> None:
    print("Basit Hesap Makinesi")
    sayi1 = sayi_al("Birinci sayıyı girin: ")
    sayi2 = sayi_al("İkinci sayıyı girin: ")
    islem = islem_al()

    try:
        sonuc = hesapla(sayi1, sayi2, islem)
        print(f"Sonuç: {sonuc}")
    except ZeroDivisionError as hata:
        print(f"Hata: {hata}")


if __name__ == "__main__":
    main()
