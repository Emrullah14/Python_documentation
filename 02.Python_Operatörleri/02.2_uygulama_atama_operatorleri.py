x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# a = input("1.sayı: ")
# b = input("2.sayı: ")
# carpim = int(a)*int(b)
# toplam = x+y+z
# fark = carpim - toplam
# print(fark)

# 2- y'nin x'e kalansız bölümünü hesaplayınız
#print(y//x)

# 3- (x,y,z) toplamının mod 3'ü nedir?
#a = x+y+z
#print(a%3)

# 4- y'nin x.kuvvetini hesaplayınız.
#print(y**x)

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
# x, *y, z = numbers
# print(z**3)

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x, *y, z = numbers
a = y[0]+y[1]+y[2]
print(a)