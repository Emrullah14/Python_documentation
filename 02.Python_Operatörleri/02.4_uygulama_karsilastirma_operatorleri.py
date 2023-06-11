# 1- Girilen 2 sayıdan hangisi büyüktür?
# a = int(input('a: '))
# b = int(input('b: '))
# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# x = float(input('1.vize: '))
# y = float(input('2.vize: '))
# z = float(input('final: '))
# ortalama = 0.6*(x+y)+0.4*z
# result = (ortalama >= 50)
# print(f"Öğrenci geçti: {result}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# sayi = int(input('Sayı: '))
# tekcift = (sayi % 2 == 0)
# print(f"Girilen sayı çift olma durumu: {tekcift}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# sayi = int(input('Sayı: '))
# result = (sayi > 0)
# print(f"Girilen sayı pozitif olma durumu: {result}") 

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#   (email: email@sadikturan.com  parola: abc123 )
email = "email@sadikturan.com"
parola = "abc123"
a = input("email: ")
b = input("parola: ")
result = (a == email) & (b == parola)
print(f"Bilgilerin doğru olma durumu: {result}")