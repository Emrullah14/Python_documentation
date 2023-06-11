# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#   durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#   lise ya da üniversite olmalıdır.

# isim = input("İsminiz: ")
# yas = int(input("Yaşınız: "))
# print("İlkokul:    1")
# print("Lise:       2")
# print("Üniversite: 3")
# print("Okumadım:   4")
# egitim = int(input("Eğitim durum no: "))
# if yas >= 18:
#     if egitim == 1:
#         print(f"{isim} ehliyet alabilir")
#     elif egitim == 2:
#         print(f"{isim} ehliyet alabilir")
#     elif egitim == 3:
#         print(f"{isim} ehliyet alabilir")
#     elif egitim == 4:
#         print(f"{isim} eğitimden dolayı ehliyet alamaz")
#     else:
#         print("Hatalı giriş yaptınız")
# elif yas < 18:
#     print(f"{isim} yaştan dolayı ehliyet alamaz")
# else:
#     print("Hatalı giriş yaptınız")

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#   not aralığına karşılık gelen not bilgisini yazdırınız.
#   0 -24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100=> 5

# yazili1 = int(input("1.yazılı notu: "))
# yazili2 = int(input("2.yazılı notu: "))
# sozlu = int(input("Sözlü notu: "))
# ortalama = (yazili1+yazili2+sozlu)/3
# if (ortalama >= 0) and (ortalama <= 24):
#     print("Puan durumunuz: 0")
# elif (ortalama >= 25) and (ortalama <= 44):
#     print("Puan durumunuz: 1")
# elif (ortalama >= 45) and (ortalama <= 54):
#     print("Puan durumunuz: 2")
# elif (ortalama >= 55) and (ortalama <= 69):
#     print("Puan durumunuz: 3")
# elif (ortalama >= 70) and (ortalama <= 84):
#     print("Puan durumunuz: 4")
# elif (ortalama >= 85) and (ortalama <= 100):
#     print("Puan durumunuz: 5")
# else:
#     print("Hatalı giriş yaptınız...")

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#   göre hesaplayınız.
#   1. Bakım => 1.yıl
#   2. Bakım => 2.yıl
#   3. Bakım => 3.yıl
#   ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#   *** datetime modülünü kullanmanız gerekiyor.

import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı (2023/6/8): ")
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1.servis aralığı")
elif days > 365 and days <= 365*2:
    print("2.servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3.servis aralığı")
else:
    print("Hatalı süre")