name = "Emrullah"
surname = "URGAN"
age = 24

#Üstteki değişkenleri tek bir string ifadesinde yazdıralım
greeting ="My name is "+name+" "+surname+" and \nI am "+str(age)+" years old."
#print(greeting)

#Greeting karakter dizisinin 0.indeksine ulaşalım
print(greeting[0])
print(greeting[3])

#Greeting ifadesinde kaç karakter olduğunu öğrenelim
length = len(greeting)
print(length)
print(greeting[length-2])
print(greeting[-2])

#Greeting'deki sadece 'name' ifadesini yazdıralım
print(greeting[3:7])
