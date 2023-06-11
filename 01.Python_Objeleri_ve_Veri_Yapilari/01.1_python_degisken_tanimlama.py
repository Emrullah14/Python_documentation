#Ali'nin brüt maaşı
maasAli = 5000

#Ahmet'in brüt maaşı
maasAhmet = 4000

#Vergi oranı
vergi = 0.27

#Ali'nin net maaşını hesaplıyoruz
print(maasAli - (maasAli * vergi))

#Ahmet'in net maaşını hesaplıyoruz
print(maasAhmet - (maasAhmet * vergi))



#Değişken tanımlama kuralları

#Değişken rakam ile başlayamaz
#Değişken en son tanımlanan değeri döndürür, öncekileri dikkate almaz
number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

#Büyük küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

#Türkçe karakter kullanmayalım

yas = 20
_age = 20

#Veri tipleri örnekleri
x = 1               #int
y = 2.3             #float
name = "Çınar"      #string
isStudent = True    #bool
#Bu veri tiplerini tek satırda tanımlayabiliriz
#x, y, name, isStudent = (1, 2.3, "Çınar", True)

#Aşağıdaki işlemde string ifade olduğu için toplama yapılmaz
a = "10"
b = "20"
print(a+b) #30 => 1020

#Değişkenin içinde boşluk olamaz
firstName = "Sadık"
last_Name = "Turan"
print(firstName+last_Name) #SadıkTuran