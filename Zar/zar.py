import random

def zar_at():
    kaç_atış = int(input("Kaç Atış İstiyorsun: "))
    zarın_yüzeyi = [1, 2, 3, 4, 5, 6]

    for _ in range(kaç_atış):
        atış = random.choice(zarın_yüzeyi)
        print("Zar atıldı, sonuç:", atış)

zar_at()