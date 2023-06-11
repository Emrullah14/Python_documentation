# x = 5
# y = 10
# z = 20

#x, y, z = 5, 16, 20

# x, y = y, x 
# x = x + 5
# x += 5 # x = x + 5
# x -= 5 # x = x - 5
# x *= 5 # x = x * 5
# x /= 5 # x = x / 5
# x %= 5 # x = x % 5
# y //= 5 # y = y // 5
# y **= z # y = y ** z

# print(x, y, z)

values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values # z'yi bir tuple'a dönüştürür

print(x, y, z)
print(x, y, z[0])