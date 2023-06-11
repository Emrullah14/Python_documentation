fruits = {'orange','apple','banana'}

#print(fruits[0]) #indekslenemez

for x in fruits:
    print(x)
    
fruits.add("cherry")#eleman ekleriz
fruits.update(['mango','grape','apple']) #apple zaten var,eklenmez

fruits.remove('mango')#mangoyu kaldırır
fruits.discard('apple')#apple'ı kaldırır

fruits.clear()#bütün elemanları siler

fruits.pop()#ilk elemanı siler.Liste yapısında son elemanı siler

print(fruits)

# myList = [1, 2, 5, 4, 4, 2, 1]
# print(myList)
# print(set(myList)) #tekrarlanan elemanları göstermez