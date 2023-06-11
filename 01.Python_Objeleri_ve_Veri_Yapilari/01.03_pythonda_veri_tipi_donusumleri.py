"""
#input ile kullanıcıdan veri alabiliyoruz
x = input("1.sayı: ")
y = input("2.sayı: ")

#x ve y değişkenlerinin veri tipini kontrol ediyoruz
print(type(x))
print(type(y))

#toplama işlemi yapabilmek için veri tiplerini integer'a çeviriyoruz
toplam = int(x)+int(y)
print(toplam)

"""
#Aşağıdaki değişkenlerin veri tiplerini inceleyelim
x = 5           #int
y = 2.5         #float
name = "Çınar"  #str
isOnline = True #bool

"""
print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))
"""

#Type-conversion(Veri dönüşümleri)
#int to float
#x = float(x)
#print(x)
#print(type(x))

#float to int
#y = int(y)
#print(y)
#print(type(y))

#bool to str
#isOnline = str(isOnline)
#print(isOnline)
#print(type(isOnline))

#bool to int
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))


