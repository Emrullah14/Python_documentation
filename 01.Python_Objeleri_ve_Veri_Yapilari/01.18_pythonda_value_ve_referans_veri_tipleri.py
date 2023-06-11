# value types => string, number
x = 5
y = 25

x = y

y = 10 # y değişkeninde yapılan değişiklik x'i etkilemez

#print(x,y)

# reference types => list
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape" # b'de yapılan değişiklik a'yı da etkiledi
# Bunun sebebi eşitleme yapılırken adres kopyalanmasıdır

print(a, b)
