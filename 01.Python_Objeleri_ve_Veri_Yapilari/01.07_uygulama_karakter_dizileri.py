website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
#print(len(course))
# 2- 'website' içinden www karakterlerini alın.
#print(website[7:10])
# 3- 'website' içinden com karakterlerini alın.
#print(website[-3:])
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
#print(course[:15]+course[-15:])
# 5- 'course' ifadesindeki karakterleri tersten yazdırın
#print(course[::-1])
name, surname, age, job = "Bora", "Yılmaz", 32, "Mühendis"
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
#print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")
# 7- 'Hello world' ifadesindeki w harfini 'w' ile değiştirin.
#result = "Hello world"
#1.yol
#result = result[0:6] + "W" + result[-4:]
#2.yol
#result.replace("w","W")
#print(result)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = "abc"
print(result*3)
