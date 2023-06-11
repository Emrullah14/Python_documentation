"""
    Dairenin Alanı   : πr²
    Dairenin Çevresi : 2πr
    
    *Yarı çapı verilen bir dairenin alan ve çevresini
    hesaplayınız. (r: 3.14)
"""

x = input("Yarı çapı giriniz: ")
x = float(x)
pi_sayisi = 3.14
dairenin_alani = pi_sayisi*(x**2)
print("Dairenin Alanı:",dairenin_alani)
dairenin_cevresi = 2*pi_sayisi*x
print("Dairenin Çevresi:",dairenin_cevresi)
