"""
List ve Tuple hemen hemen aynıdır
Farkı; Tuple'da eleman silme,ekleme,değiştirme 
işlemleri yapılamaz
"""
list = [1, 2, 3]

tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(tuple))
print(len(list))

list = ["ali","veli"]
tuple = ("damlar","ayşe")

list[0] = "ahmet"
tuple[0] = "deniz"#Hata verir.Tuple'da tek bir eleman değiştirilemez

print(list)
print(tuple)