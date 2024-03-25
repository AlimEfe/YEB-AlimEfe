import os

toplam = 0

for sayi in range(1, 1000):
    if sayi % 3 == 0 or sayi % 5 == 0:
        toplam += sayi

print("1 ile 1000 arasındaki 3 ile 5'in katlarının toplamı:" , toplam )     