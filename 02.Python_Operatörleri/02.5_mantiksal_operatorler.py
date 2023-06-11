x = 5

hak = 5
devam = 'e'

result = 5 < x < 10

# and
# True, True => True
# True, False = False

result = x > 5 and x < 10
result = (hak > 0) and (devam == 'e')

# or
# True, False => True
# True, True => True
# False, False => False

result = (x > 0) or (x % 2 == 0)

print(result)