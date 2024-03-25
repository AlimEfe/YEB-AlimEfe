ürün_listesi = {"çorba":25 , "pilav" :50 , "ayran" :5}

sepet = {}

bütçe = int(input("bütçenizi girin\n"))

while bütçe > 0:
    for isim, fiyat in ürün_listesi.items():
        print(isim,"ürünün fiyatı = ", fiyat)

    seçilen_ürün = input("ürünü seçin\n")

    if seçilen_ürün == "q":
        break

    seçilen_ürün_fiyat = ürün_listesi[seçilen_ürün]

    if seçilen_ürün_fiyat > bütçe:
        print ("ürün fiyatı yüksek")

        continue

    if seçilen_ürün in sepet.keys():

        sepet[seçilen_ürün] += 1

    else:

        sepet[seçilen_ürün] = 1

        bütçe -= seçilen_ürün_fiyat

        print("kalan bütçeniz = ", bütçe)

        for isim,miktar in sepet.items():

            print(miktar, "adet", isim)


            print("alışveriş tamamlandı")

            print("kalan bütçeniz = ", bütçe)

        for isim,miktar in sepet.items():

            print(miktar,'adet',isim)