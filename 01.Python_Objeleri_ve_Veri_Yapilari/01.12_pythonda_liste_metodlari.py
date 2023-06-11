numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)#en küçük sayıyı yazar
val = max(numbers)#en büyük sayıyı yazar
val = max(letters)#en son harfi yazar
val = min(letters)#en ilk harfi yazar

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49)#listenin en sonuna 49 elemanı eklenir
numbers.insert(3, 78)#3.indekse 78'i ekler

numbers.pop()#en son elemanı siler
numbers.pop(0)#0.indeksi siler

numbers.remove(59)#59 elemanını siler
numbers.sort()#liste küçükten büyüğe sıralanır
numbers.reverse()#liste büyükten küçüğe sıralanır

print(numbers.count(10))#kaç tane 10 sayısı olduğunu bulur
print(letters.count("a"))#kaç tane a harfi olduğunu bulur
