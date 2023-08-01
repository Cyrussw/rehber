import os

# Hayata temiz bir sayfa
os.system("cls")

kisiler = []
kisiSayi = 0
# Menüyü gösterelim

print(
    """
===== CYR Rehber'e Hoş Geldiniz. =====

1) Kişi Ekle
2) Kişi Sil
3) Kişileri Göster
4) Kişileri Tamamen Sil
0) Programı Sonlandır

======================================
"""
)

while True:  # Her seferinde tekrarla
    user = str(input("Seçenek: "))  # Kullanıcıdan veri al

    if not user:  # Kullanıcı boş veri gönderirse
        print("Lütfen bir işlem giriniz.")
    elif user == "1":  # Kullanıcı 1 yazarsa
        print("Lütfen kişi bilgilerini giriniz.")
        kisiAdi = input("Kişi adı: ")

        if not kisiAdi:
            print("Lütfen kişi adı giriniz.")
        else:
            kisiNo = input("Kişi numarası: ")
            if not kisiNo:
                print("Lütfen kişi numarası giriniz.")
            else:
                kisiSayi = kisiSayi + 1
                kisiler.append([kisiSayi, kisiAdi, kisiNo])

    elif user == "2":  # Kullanıcı 2 yazarsa
        print("Lütfen kişinin tablodaki konumunun sayısını giriniz.")
        kisiNo = int(input("Kişi sayısı: "))

        if not kisiNo:
            print("Lütfen kişinin tablodaki konumunun sayısını giriniz.")
        else:
            kisiler.pop(kisiNo - 1)
    elif user == "3":  # Kullanıcı 3 yazarsa
        if kisiler == []:
            print("Kişi bulunamadı.")

        for kisi in kisiler:
            print("=====================")
            print(f"Kişi Adı: {kisi[1]}\nKişi Numarası: {kisi[2]}")
    elif user == "4":
        if kisiler == []:
            print("Kişi bulunamadı.")
        else:
            print("Kişiler tamamen silinmiştir.")
            kisiler.clear()
    elif user == "0":
        print("Uygulamadan çıkılıyor görüşmek üzere!")
        break
