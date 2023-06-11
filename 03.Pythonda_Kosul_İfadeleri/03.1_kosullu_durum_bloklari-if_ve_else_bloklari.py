username = input("Email: ")
password = input("Parola: ")

# Birinci koşulu belirtiyoruz
if (username == "emrullahurgan"):
    # İkinci koşulu belirtiyoruz
    if (password == "1234"):
        print("Hoş geldiniz")
    else:
        # ikinci koşul sağlamadığında
        print("Parola yanlış")
else:
    # birinci koşul sağlamadığında
    print("Email yanlış")