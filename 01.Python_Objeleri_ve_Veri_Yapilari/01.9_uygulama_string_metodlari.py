website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'Hello World' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
#a = " Hello World "
#a = a.strip()
#a = a.lstrip() #Soldan siler
#a = a.rstrip() #sağdan siler
#a = a.lstrip("/:pth") #Soldaki bazı karakterleri siler
#print(a)
# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
#a = "www.sadikturan.com"
#a = a.strip("w.com")
#print(a)
# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
#course = course.lower()
#print(course)
# 4- 'website' içinde kaç tane a karakteri vardır?
#website = website.count("a")
#website = website.count("a",0,10) #0 ile 10.indek arasındakileri sayar
#print(website)
# 5- 'website' 'www' ile başlayıp com ile bitiyor mu?
#website = website.startswith("www")
#website = website.endswith("com")
#print(website)
# 6- 'website' içinde '.com' ifadesi var mı?
#website = website.find(".com")
#print(website)
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi?
#course = course.isalpha()
#course = course.isdigit()
#print(course)
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
#a = "Contents"
#a = a.center(50,"*")
#print(a)
# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
#course = course.replace(" ","-")
#print(course)
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
#a = "Hello World"
#a = a.replace("World","There")
#print(a)
# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.
course = course.split()
print(course)