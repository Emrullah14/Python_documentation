message = " Hello There. My name is Sadık Turan "

#message değişkenindeki karakterleri büyük harfe dönüştürelim.
#message = message.upper()

#bütün karakterleri küçültelim
#message = message.lower()

#her kelimenin ilk harfi büyük olsun
#message = message.title()

#sadece ilk harfi büyük olsun
#message = message.capitalize()

#string ifadesinin başında veya sonunda boşluk varsa kaldıralım
#message = message.strip()

#Cümleyi boşluğu baz alarak parçalayalım
#message = message.split()

#Cümleyi noktayı baz alarak parçalayalım
#message = message.split(".")

#Parçalanmış cümleyi boşlukları kullanarak birleştirelim
#message = " ".join(message)

#Cümle içinde aradığımız bir kelimenin kaçıncı indekte başladığını bulalım
#index = message.find("Sadık")
#Eğer -1 yazdırırsa aranılan kelime cümlede yoktur demektir.
#print(index)

#Cümlenin H harfi ile başlayıp başlamadığını kontrol edelim
#isFound = message.startswith("H")
#Cümlenin n harfi ile bitip bitmediğini kontrol edelim
#isFound = message.endswith("n")

#Cümle içindeki karakterleri değiştirelim
#message = message.replace("Sadık","Çınar")

#Cümleyi 100 karakterlik bir alanda merkeze alır(ortalar)
#message = message.center(100)


print(message)
