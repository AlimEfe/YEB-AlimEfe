# YEB-AlimEfe

# Yamanevler Enderun Bilişim Sınava Hazırlık

# Kim Milyoner Olmak İster

## Amaç

Bu uygulamada günümüzde popüler olan Kim Milyoner Olmak İster yarışmasının kodunu yazdım ve bu yarışmanın kod kısmını gösterdim.

````python
print("Kim Milyoner Olmak İstere Hoş Geldiniz \n")
question1 = input("Galatasaray Kaç Tarihinde kurulmuştur ? \n"
                  "  A) 5 Teşrin 1905"
                  "  B) 1 Teşrin 1905"
                  "  C) 3 Mart 1905"
                  "  D) 3 Ekim 1905 \n"
                      ) 
            
question2 = input("Yamanevler Hangi Yıl Kurulmuştur ? \n"
                  "  A) 1992 "
                  "  B) 1981"
                  "  C) 1984"
                  "  D) 1923 \n"
                  )

question3 = input("Beyni Çalınan Bilim İnsan Kimdir ? \n"
                  "  A) Albert Einstein "
                  "  B) Thomas Edison"
                  "  C) Nicola Tesla"
                  "  D) Stephen Hawking \n"
                  )

if question1 == "B" and question2 == "a" and question3 == "A":
    print( "Tebrikler Kazandınız" )
else:
    print( "Maalesef Kaybettiniz" ) 
````


# Kütüphane Uygulaması

## Bu Uygulamada

Öncelikle bu tür kütüphane uygulamalarında bir main birde engine adında iki dosya gerekmektedir.

## İşte Main Kodu

````python
import movie_engine

option_show_list = "1"
option_add_movie = "2"
option_delete_movie = "3"
option_exit = "X" 


def show_menu():
    menu_text = (
            option_show_list + " = Listele\n" + option_add_movie + " = Ekleme\n" + option_delete_movie + " = Silme\n" + option_exit + " = çıkış\n")
    return input(menu_text)


print("Film kütüphanesi v1.0\n")
while True:
    choice = show_menu()

    if choice == option_show_list:
        movie_engine.show_movies()
    elif choice == option_add_movie:
        movie_engine.add_movie()
    elif choice == option_delete_movie:
        movie_engine.delete_movie()
    elif choice == option_exit:
        break

print("çıkış yapılıyor ...")
````

Burada def fonksiyonunu kullanarak bir film kütüphanesi Oluşturdum.
ve bukütüphaneyide movie.engine dosyasında kullanarak bir kütüphane uygulaması yazdım. 
## İşte engine kodları

````python
movies = {}


def show_movies():
    for movie_key in movies.keys():
        name = movies[movie_key]["movie_name"]
        director = movies[movie_key]["movie_director"]
        year = movies[movie_key]["movie_year"]
        print(movie_key, "=> Adı: ", name, " Yönetmeni: ", director, " Yılı: ", year)


def add_movie():
    name = input("Filmin adını girin\n")
    director = input("Filmin yçnetmenini girin\n")
    year = input("Filmin yılını girin\n")
    key = len(movies.items()) + 1
    movies[key] = {"movie_name": name, "movie_director": director, "movie_year": year}


def delete_movie():
    movie_key = int(input("Hangi filmi silmek istiyorsunuz\n"))
    movies.pop(movie_key)
````



# Taş , Kağıt , Makas Uygulaması

## Bu uygulamada

Bu uygulamada karşıda bir bilgisayar ile taş kağıt makas oynamaya yarayan bir python kodu yazdım.

````python
import random 
while True:
 
 oyuncu = input("ne seçmek istersiniz(taş , kağıt,makas ) ")
 
 random1 = ["taş","kağıt","makas"]
 
 random2 = random.choice(random1)
 
 print(random2)

 if oyuncu == "taş" and random2 == "taş" or oyuncu == "kağıt" and random2 == "kağıt" or oyuncu == "makas" and random2 == "makas":
  print("berabere") 

 elif oyuncu == "taş" and random2  == "makas" or oyuncu == "makas" and random2 == "kağıt" or oyuncu == "kağıt" and random2 == "taş":
  print("tebrikler kazanmayı başardınız")
 
 else:
  print("maalesef kaybettiniz ")
  break

````

# Yemek.com

## Bu uygulamada

Sizden önce bütçenizi isteyen sonrada size menüyü sunan satın aldığınız ürünün fiyatına görede bütçe fiyatınızı azaltan bir python kodu  

````python
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
````
# Zar Uygulaması

## Bu uygulamada 

Sizden 1'den 6'ya kadar sayı alan ve aynı bir zar gibi tamamiyle sizin şansınıza kalmış olan rastgele bir sayı veren python programı.

````python
import random

def zar_at():
    kaç_atış = int(input("Kaç Atış İstiyorsun: "))
    zarın_yüzeyi = [1, 2, 3, 4, 5, 6]

    for _ in range(kaç_atış):
        atış = random.choice(zarın_yüzeyi)
        print("Zar atıldı, sonuç:", atış)

zar_at()
````









csharp_-dev_2
#Alim Efe

# Ödev 1
Kullanıcıdan iki sayı ve bir işlem (+, -, x, /) isteyen ve ardından işlemi hesaplayıp sonucunu izleyen bir C# programı yazıyorsunuz. Eğer işlem sembolü önceki sembollerden farklıysa, "Tanınmayan karakter" metnni gösteriminiz.
Console.WriteLine("birinci sayı girin:");
    int s1 = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("ikinci sayı girin:");
    int s2 = Convert.ToInt32(Console.ReadLine());
````c#
    Console.WriteLine("hangi işlemi yapmak istersiniz:\n toplam= 1\n çıkarma= 2\n çarpma= 3\n bölme= 4 ");
    int process = Convert.ToInt32(Console.ReadLine());

    int total= (s1+s2);
    int minus = (s1-s2);
    int impact = (s1*s2);
    int divide = (s1/s2);
    if (process==1)
    {
        Console.WriteLine("girdiğiniz sayıların toplamı:"+total);
    }
    else if (process==2)
    {
        Console.WriteLine("girdiğiniz sayıların çıkması:"+minus);
    }
    else if (process==3)
    {
        Console.WriteLine("girdiğiniz sayıların çarpımı:"+impact);
    }
    else if (process==4)
    {
        Console.WriteLine("girdiğiniz sayıların bölmü:"+divide);
    }
    else
    {
        Console.WriteLine("lütfen geçerli bir işlem giriniz");
    }
````
# Ödev 2
Kullanıcıdan iki sayı ve bir işlem (+, -, x, /) sembolü isteyen ve ardından işlem hesaplayıp sonucunu izleyen bir C# programı yazınız. Eğer işlem sembolü öncek< sembollerden farklıysa, "Tanınmayan karakter" ifadesini gösterirsiniz.
Console.WriteLine("birinci sayı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("ikinci sayı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
````c#
        Console.WriteLine("hangi işlemi yapmak istersiniz:\n toplam= 1\n çıkarma= 2\n çarpma= 3\n bölme= 4 ");
        int process = Convert.ToInt32(Console.ReadLine());

        int total= (s1+s2);
        int minus = (s1-s2);
        int impact = (s1*s2);
        int divide = (s1/s2);

        switch (process)
        {
            case 1:
                Console.WriteLine("girdiğiniz sayıların toplamı:"+total);
                break;
            case 2:
                Console.WriteLine("girdiğiniz sayıların çıkması:"+minus);
                break;
            case 3:
                Console.WriteLine("girdiğiniz sayıların çarpımı:"+impact);
                break;
            case 4:
                Console.WriteLine("girdiğiniz sayıların bölmü:"+divide);
                break;
            default:
                Console.WriteLine("lütfen geçerli bir işlem giriniz");
                break;
        }
````
# Ödev 3
Bir sayı (x) isteyen ve bu sayının pozitif mi yoksa negatif mi olduğunu yanıtlayan bir C# programı yazın.
````c#
Console.WriteLine("bir sayı girin: ");
        int s1 = Convert.ToInt32(Console.ReadLine());
        if (s1 < 0)
        {
            Console.WriteLine(s1 + "sayısı negatifdir");
        }
        else if (s1 > 0)
        {
            Console.WriteLine(s1 +" " +"sayısı pozitifdir");
        }
````
# Ödev 4
C# dilinde üç sayıyı (x, y, z) isteyen ve en büyüğünü görüntüleyen bir program yazın.

Console.WriteLine("birinci sayı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("ikinci sayı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("üçüncü sayıyı girin:");
        int s3 = Convert.ToInt32(Console.ReadLine());
````c#
        if (s1 > s2 && s1> s3)
        {
            Console.WriteLine("girdiğiniz sayılardan en büyük olanı sayı"+" "+s1);
        }
        else if (s2> s1 && s2> s3)
        {
            Console.WriteLine("girdiğiniz sayılardan en büyük olanı sayı"+" "+s2);
        }
        else if (s3> s1 && s3> s2)
        {
            Console.WriteLine("girdiğiniz sayılardan en büyük olanı sayı "+" "+s3);
        }
````
# Ödev 5
C#'ta bir sayı (x) isteyen ve 10 * x'< görüntüleyen bir programdan oluşur. Kullanıcı 0 girene kadar tekrarlanmalıdır.

````c#
while (true)
        {
        Console.WriteLine("birinci sayı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());
        int çarpam =(s1 * 10);
        Console.WriteLine(çarpam);
        if (s1 == 0)
        {
            break;
        }

        }

````
# Ödev 6
Kullanıcıdan bir dizi sayı (x, y) talep eden ve bunları ekranda görüntüleyen bir C# programı oluşturur.
````c#
        Console.WriteLine("birinci sayı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("ikinci sayı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
        while (s1 <= s2)
        {
            Console.WriteLine(s1++);

        }
````
# Ödev 7
C# dilinde sayı isteyen ve toplamlarını gösteren bir program yazın. Kullanıcı 0 girene kadar numara ister ve program biterse Bitti gösterilir.
````c#
int toplam= 0 ;
        while (true)
        {
            Console.WriteLine("sayı girin:");
            int sayı1 = Convert.ToInt32(Console.ReadLine());
            toplam += sayı1;
            if (sayı1 == 0)
            {
                Console.WriteLine(toplam);
                break;
            }
            else
            {
            Console.WriteLine(toplam);
            }
        }
````
# Ödev 8
Matematiksel istatistik (Zorluk: Orta) Kullanıcıdan 5 tam sayı isteyen ve takip edilen istatistikler ekranda görüntüleyen bir C# programı oluşturur:

5 sayısının toplamı
Aritmetik ortalama
Maksimum sayı
minimum sayı
````c#
       Console.WriteLine("1. sayıyı girin:");
       int s1 = Convert.ToInt32(Console.ReadLine());
       
        Console.WriteLine("2. sayıyı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
        
        Console.WriteLine("3. sayıyı girin:");
        int s3 = Convert.ToInt32(Console.ReadLine());
        
        Console.WriteLine("4. sayıyı girin:");
        int s4 = Convert.ToInt32(Console.ReadLine());
        
        Console.WriteLine("5. sayıyı girin:");
        int s5 = Convert.ToInt32(Console.ReadLine());
        
        int toplam = (s1 + s2 + s3 + s4 + s5);
        Console.WriteLine("girdiğiniz sayıların toplamı:"+toplam);
        
        int ortalama = (s1 + s2 + s3 + s4 + s5)/5;
        Console.WriteLine("girdiğiniz sayıların ortalaması:"+ortalama);
      
        int max = s1;
        int min = s1;
        
        if (s1 > s2 && s1 > s3 && s1 > s4 && s1 > s5)
        {
        
            max = s1 ;
        }
        else if (s2 > s1 && s2 > s3 && s2 > s4 && s2 > s5)
        {
            max = s2;
        }
        else if (s3 > s1 && s3 > s2 &&  s3 > s4 && s3 > s5)
        {
            max = s3;
        }
        else if (s4 > s1 && s4 > s2 && s4 > s3 && s4 > s5)
        {
            max = s4;
        }
        else if (s5 > s1 && s5 > s2 && s5 > s3 && s5 > s4)
        {
            max = s5;
        }
        if (s1 < s2 && s1 < s3 && s1 < s4 && s1 < s5)
        {
            min = s1;
        }
        else if (s2 < s1 && s2 < s3 && s2 < s4 && s2 < s5)
        {
            min = s2;
        }
        else if (s3 < s1 && s3 < s2 && s3 < s4 && s3 < s5)
        {
            min = s3;
        }
        else if (s4 < s1 && s4 < s2 && s4 < s3 && s4 < s5)
        {
            min = s4;
        }
        else if (s5 < s1 && s5 < s2 && s5 < s3 && s5 < s4)
        {
            min = s5;
        }
        Console.WriteLine("girdiğiniz sayıların en büyük sayı:"+max);
        Console.WriteLine("girdiğiniz sayıların en küçük sayı:"+min);
    ````
# Ödev 9

````c#
C# dilinde bir sayı (x) ve bir miktar (y) isteyen bir program yazın. Bu sayıyı mitarın (y) katılaşana kadar devam eder.

    Console.WriteLine("x sayısını girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("y miktarını  girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
            for (int j = 1; j <= s2; j++)
        {
            Console.Write(s1);
        }
````
# Ödev 10
1'den 500'e kadar 3'ün ve 5'in katları olan parçayı gösteren bir C# programı oluşturulur.
````c#
        int x = 0;
        while(x < 500)
        {
            Console.WriteLine(x);
            x+=15;
        }
````
# Ödev 11
C# dilinde kullanıcıdan kullanıcı adı ve şifre isteyen bir erişim girişi yazın. İkisi de tamsayı olmalı ve giriş 12 ve şifre 1234 olduğunda "giriş başarılı yazmalı" yanlışsa ve en fazla 3 deneme yapana kadar tekrarlanmalıdırKullanıcı adı ve şifre doğruysa Giriş başarılı mesajını gösterir, aksi halde Giriş mesajını gösterir
````c#
        int deneme_hakkı =3;
        while (true )
        {
            if (deneme_hakkı == 0){
               Console.WriteLine("hakkınızz bitti :");
                break;
            }
            else
            {
            Console.WriteLine("giriş yapınız : ");
            int giriş = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("şifre giriniz : ");
            int şifre = Convert.ToInt32(Console.ReadLine());

            if (giriş == 12 && şifre == 1234)
            {
                Console.WriteLine("giriş başarılı ");
                break;
            }
            else
            {
                Console.WriteLine("giriş başarısız");
                deneme_hakkı--;
            }
            }
        }
````
# Ödev 12
C# dilinde kullanıcıdan iki sayı isteyen ve bölme işlemi ile bölmenin geri kalanını
gösterilen bir program yazın. İkinci sayı olarak 0 girilirse kişisel bildirim yapın ve ilk sayı olarak 0 girilirse programı sonlandırın.
````c#
while (true)
        {
        Console.WriteLine("1. sayıyı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("2. sayıyı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());

        if (s1 == 0)
        {
            break;
        }

         else if (s2 == 0)
        {
            Console.WriteLine("sıfır ile sayı bölünmez");

        }
        else{
        int işlem = s1 /s2;
        Console.WriteLine("sayıların bölülü:"+işlem);

        int kalan = s1 % s2;
        Console.WriteLine("kalan:"+kalan);}
        }
````
# Ödev 13
Kullanıcıdan bir sayı aralığı (x, y) <steyen ve x'ten y'ye kadar çarpım tablosunu görüntüleyen b<r C# programı oluşturur.
````c#
Console.WriteLine("Bir X Sayısı Giriniz");
         int x = Convert.ToInt32(Console.ReadLine());

         Console.WriteLine("Bir Y Sayısı Giriniz");
         int y = Convert.ToInt32(Console.ReadLine());

        for (int i = x; i <= y; i++)
        {
         Console.WriteLine($"Çarpım tablosu {i} için:");
        for (int j = 1; j <= 10; j++)
          {
         Console.WriteLine($"{i} x {j} = {i * j}");
        }
        Console.WriteLine();
            }

            Console.ReadLine();
````
#  Ödev 14
Bir öğrencinin notunu bir tamsayıdan hesaplayan bir C# programı oluşturur. Kullanıcıdan bir sayıdan (x) isteyin ve aşağıdakileri yanıtlayın:

````c#
Console.WriteLine("notu giriniz: ");
        int sayı = Convert.ToInt32(Console.ReadLine());
        switch (sayı)
        {
            case 10:
                Console.WriteLine("A+");
                break;
            case 9:
                Console.WriteLine("A");
                break;
            case 8:
                Console.WriteLine("B+");
                break;
            case 7:
                Console.WriteLine("B");
                break;
            case 6:
                Console.WriteLine("C");
                break;
            case 5:
                Console.WriteLine("E");
                break;
            case 4:
                Console.WriteLine("F");
                break;
            case 3:
                Console.WriteLine("F");
                break;
            case 2:
                Console.WriteLine("F");
                break;
            case 1:
                Console.WriteLine("F");
                break;
            case 0:
                Console.WriteLine("F");
                break;
            default:
                Console.WriteLine("böyle bir not yok");
                break;

        }
````
# Ödev 15
Kullanıcıdan iki tamsayı (x, y) <steyen ve bu yapısaln aralığını (iki sayı da dahil olmak üzere) üç farklı oturum gösteren bir C# programı oluşturuldu:
````c#
        madde1
        Console.WriteLine("1. sayıyı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("2. sayıyı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
        for (int i = 1; s1 <= s2; i++)
        {
        Console.Write(s1 ++);
        }*/
        /*madde2
        Console.WriteLine("1. sayıyı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("2. sayıyı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());

        while(s1<s2)
        {
            Console.Write(s1 ++);
        }
        */
        /*madde3
        Console.WriteLine("1. sayıyı girin:");
        int s1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("2. sayıyı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
        do
        {
            Console.Write(s1 ++);
        }while (s1<s2);
````
# Ödev 16
Pozitif bir tamsayının kaç basamağı olduğunu hesaplayan programı c# ile hazırlayın. Kullanıcı negatif bir tamsayı kayıtlı, program uyarı mesajı gösterilmiyor ve buna karşılık gelen pozitif sayı ile devam ediliyor.
````c#
while (true)
        {
        Console.WriteLine("Sayı giriniz");
        int s1 = Convert.ToInt32(Console.ReadLine());
        int sayaç = 0;
        if (s1 < 0)
        {
        Console.WriteLine("hata sayı negatıf");
        s1 *= -1;
        while (s1 > 0)
        {
        s1 /= 10;
        sayaç++;
        }
        Console.WriteLine(sayaç+" Basamaklı");
        }
        else
        {
        while (s1 > 0)
        {
        s1 /= 10;
        sayaç++;
        }
        Console.WriteLine(sayaç+" Basamaklı");
        }
        }
````

# Ödev 17
Sadece bir dağılım ve karakter değişkenleri için alfabenin büyük harflerini kullanarak bir C# programı yazın.
````c#
for (char i = 'A'; i <= 'Z'; i++)
        {
        Console.Write(i);
        }
````


# Ödev 18
C# dilinde, bir sayının mutlak değerini hesaplayıp gösteren bir program yazın. Eğer sayı pozitifse, mutlak değer tam olarak sayı x'tir. Eğer sayı negatifse, mutlak değer -x'tir."
````c#
 Console.WriteLine("Sayı giriniz");
        int s1 = Convert.ToInt32(Console.ReadLine());
        if (s1 > 0)
        {
            Console.WriteLine("sayının mutlak değerden çıkmış hali" + " " + s1);
        }
        else if (s1 < 0)
        {
            Console.WriteLine("sayının mutlak değerden çıkmış hali" + " " + s1);
        }

        Console.WriteLine("1. sayıyı girin:");
        int sa1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("2. sayıyı girin:");
        int s2 = Convert.ToInt32(Console.ReadLine());
        int toplam = 0;
        for (int i = 1; i <= s1; i++)
        {
            toplam += s2;
        }

        Console.WriteLine(toplam);
````
# Ödev 19
C# dilinde, kullanıcıdan iki tamsayı isteyen ve çarpımlarını gösteriliyor, ancak * operatörünü kullanmadan gerçekleştiren bir program birleştirilebilir. Ardışık toplamalarını kullanmalısınız.

Console.WriteLine("1. Sayıyı Giriniz :");
    int s1 = Convert.ToInt32(Console.ReadLine());
````c#
    Console.WriteLine("2. Sayıyı Giriniz :");
    int s2 = Convert.ToInt32(Console.ReadLine());


    for (int i = 0; i < 1; i++)
    {
        
    }
*/


    Console.WriteLine("Bir sayı girniz :");
    int s1 = Convert.ToInt32(Console.ReadLine());

    for (int i = 0; i < 9; i++)
    {
        
    }
````



# Sayı  Tahmin Etme Oyunu 

## Hedefler
- Koşullu ,fadeler
- lex,cal scop,ng bel,rlemeyle ,lg,l, daha fazla prat,k
- Döngüler
- B,r problem b,ld,r,m, nasıl anal,z ed,l,r
-Genel Bakış
Bu ödevde hal6hazırda öğrend6ğ6n6z becer6ler6 kullanarak b6r program
yazacaksınız. 1 6le 100 arasında (yan6 1 6le 100 dah6l ed6lmel6d6r) rastgele b6r
sayı üreten b6r sayı tahm6n oyunu yazın. B6r sayı oluşturulduktan sonra
kullanıcıdan bu sayıyı tahm6n etmes6n6 6stey6n ve doğru sayıyı tahm6n edene
kadar sormaya devam ed6n. Kullanıcıya tahm6nler6n6n çok yüksek veya çok
düşük olduğunu söylemek g6b6 6puçları vereceks6n6z.
Hedeflere Ulaşmak 2ç2n Aşağıdak2 Görevler2 Tamamlayın
Yen6 b6r proje oluşturun ve bunu Say6Tahm6nOyunu olarak adlandırın
Programınız şunları yapmalıdır:
- Tekrarlama döngüsünü kullanın, böylece oyun b6tene kadar oyun devam
eder.
- Kullanıcıların tahm6nler6n6n rastgele sayıdan küçük, büyük veya ona eş6t
olup olmadığını bel6rlemek 6ç6n b6r koşula sah6p olun.
- Kullanıcıdan 1 6le 100 arasında b6r sayı g6rmes6n6 6stey6n.

````c#
Random random = new Random();
int rastgeleSayi = random.Next(1, 101);
int tahmin = 0;

while (tahmin != rastgeleSayi)
{
    Console.WriteLine("Bir sayı tahmin ediniz:");
    tahmin = Convert.ToInt32(Console.ReadLine());

    if (tahmin > rastgeleSayi)
    {
        Console.WriteLine("Daha Küçük Bir Sayı Giriniz");
    }
    else if (tahmin < rastgeleSayi)
    {
        Console.WriteLine("Daha Büyük Bir Sayı Giriniz");
    }
}

Console.WriteLine("Doğru Bildiniz !!!!");
Console.WriteLine("Oyun Bitti");
````







# Seyahat Acentası

## SEYEHAT UYGULAMASI
### Hedefler
- Koşul ,fadeler,yle daha fazla prat,k yapın
- lex,cal scop,ng bel,rlemeyle ,lg,l, daha fazla prat,k
- Düz Türkçede problem ,fadeler, nasıl anal,z ed,l,r
Genel Bakış
Bir seyahat acentesının müşterilere tatil paketleri rezervasyonu yapması için küçük bir seyahat rezervasyon programı yazın. 

Program, kullanıcıdan uçuşlar için sunulan hedeflerden b.r.n. seçmes.n. ve b.r otel odası
rezervasyonu yapma seçeneğ.n. .steyecekt.r. Rezervasyon .şlem.n.n
sonunda program kullanıcıya tüm rezervasyon b.lg.ler.n. sağlayacaktır. Yeni bir proje oluşturun ve adını Seyahat olarak adlandırın.

## Açıklama
İstanbul’dak. küçük bir seyahat acentesı, İstanbul bölgesindeki müşterilere
tatil paketler. sunuyor. Seyahat acentes. küçük olduğundan, seçilen yerler
yalnızca az sayıda yer ve otel sunmaktadır. Seyahat acentesının  müşterileri için uçuş ve otel rezervasyonları yapmasına yardımcı olacak bir program yazın.
Seyahat acentesı, seyahate çıkmayı planlayan yolcuların sayısını bilmek
istiyor. Müşteriye seyahat edecek kişi sayısını sorun. Program yalnızca bir
veya daha fazla yolcunun giriş değerini kabul etmelidir. Yolcu sayısında
herhangi bir sınırlama yoktur. İstemci sıfır veya daha düşük bir değer girerse
program değeri bir gezgine sıfırlamalı ve istemciye bir hata bildirmelidir.
Kullanıcı yolcu sayısını girdikten sonra program , müşterinin gidiş-dönüş
uçuş rezervasyonu yapması için her varış noktası için bir fiyat (kişi başı) .ile
birlikte teklif edilen varış noktalarının bir listesin. sunmalıdır. Bir tamsayı
değeri girerek istemciden bir hedef numara seçmesini isteyini Program
hangi varış noktasının alınacağını ve doğru şehir adı ve fiyatının
kaydedileceğini belirleyecektiri Fiyatların yer aldığı şehrilerin listesi
aşağıdaki tabloda gösterilmektedir:


- Müşteri üç otel türünden herhangi biri için doğru bir tamsayı değeri
girmezse program, otel türünü Standart Otel'e ve fiyatı da 98,50 ABD Doları'na otomatik olarak sıfırlayacaktır.
- Müşteriden birkaç otel odasına girmesini isteyini Giriş sıfır veya daha azsa
otel odası sayısı bire sıfırlanacaktır.
- Müşteriden otelde kalacağı gece sayısını girmesini isteyini Giriş sıfır veya daha azsa gece sayısı bir olacaktır.
- Toplam otel fiyatını otel fiyatı, oda sayısı ve gece sayısı ile hesaplayın.
- Hem uçuş hem de otel rezervasyonu yapılmışsa program, uçuşların ve
otelin toplam fiyatını hesaplayacak ve uçuşlar, otel bilgileri ve toplam fiyatı
.çeren paket ayrıntılarını çıkaracaktır.
- Uçuşlar yalnızca rezerve edilmişse ve otel seçeneği seçilmemişse, program uçuş güzergahı ayrıntılarını bilgi ve fiyatla birlikte görüntüleyecektir.
- Uçuşlara rezervasyon yapılmamışsa program, rezervasyon yapılmadığını
duyuracaktır.

## Uçuşlar ve Otel Rezervasyonu
````c#
1. Seyahat acentesine hoş geldiniz. Tatil destinasyonlarınız için seyahat paketleri
sunuyorsunuz.
2. [Giriş İletişim Kutusu] Kaç kişi seyahat edecek? 4
3. Uçuş rezervasyonu yapmak için destinasyonlardan birini seçin: 1 - Chicago (200 $), 2 - Los
Angeles (360 $), 3 - Miami (320 $), 4 - Orlando (310 $), 5 - Seattle (330 $)
4. [Giriş İletişim Kutusu] Hedef numarayı girin: 3
5. [Giriş İletişim Kutusu] Paketinize oteli dahil etmek ister misiniz (E/H)? e
6. Ne tür bir otele rezervasyon yaptırmak istersiniz? 1 - Motel (49,99 $), 2 - Standart Otel
(98,50 $), 3 - Lüks Otel (199,75 $)
7. [Giriş İletişim Kutusu] Otel numarasını girin: 2
8. [Giriş İletişim Kutusu] Otel odası sayısını girin: 1
9. [Giriş İletişim Kutusu] Otelde kalınacak gece sayısını girin: 3
10. Uçak ve otel rezervasyonları yapıldı.
11. 4 gezgin için Miami'ye toplam uçuş fiyatı $1280.0
12. Standart Otel'de 3 gecelik 1 oda için toplam otel fiyatı $295.5
13. Uçak ve otel toplam paket fiyatı 1575,5$'dır.
````

## Yalnızca Uçuş Rezervasyonu

````c#
1. Seyahat acentesine hoş geldiniz. Tatil destinasyonlarınız için seyahat paketleri sunuyorsunuz.
2. [Giriş İletişim Kutusu] Kaç kişi seyahat edecek? 3
3. Uçuş rezervasyonu yapmak için destinasyonlardan birini seçin: 1 - Chicago (200 $), 2 - Los
Angeles (360 $), 3 - Miami (320 $), 4 - Orlando (310 $), 5 - Seattle (330 $)
4. [Giriş İletişim Kutusu] Hedef numarayı girin: 5
5. [Giriş İletişim Kutusu] Paketinize oteli dahil etmek ister misiniz (E/H)? N
6. Uçuş rezervasyonu yapıldı.
7. 3 gezgin için Seattle'a toplam uçuş fiyatı $990.0
8.
````

## Rezervasyon Yok

````c#
1. Seyahat acentesine hoş geldiniz. Tatil destinasyonlarınız için seyahat paketleri sunuyorsunuz.
2. [Giriş İletişim Kutusu] Kaç kişi seyahat edecek? 1
3. Uçuş rezervasyonu yapmak için destinasyonlardan birini seçin: 1 - Chicago (200 $), 2 - Los
Angeles (360 $), 3 - Miami (320 $), 4 - Orlando (310 $), 5 - Seattle (330 $)
4. [Giriş İletişim Kutusu] Hedef numarasını girin: 6
5. Rezervasyon yapılmadı. Lütfen tekrar gelin!
6.
````

## Hatalı ve Otomatik Sıfırlamalı Rezervasyon

````c#
1. Seyahat acentesine hoş geldiniz. Tatil destinasyonlarınız için seyahat paketleri
sunuyorsunuz.
2. [Giriş İletişim Kutusu] Kaç kişi seyahat edecek? 0
3. Hata: Yolcu sayısı 1'e sıfırlandı. 0 girdiniz
4. Uçuş rezervasyonu yapmak için destinasyonlardan birini seçin: 1 - Chicago (200 $), 2 - Los
Angeles (360 $), 3 - Miami (320 $), 4 - Orlando (310 $), 5 - Seattle (330 $)
5. [Giriş İletişim Kutusu] Hedef numarayı girin: 1
6. [Giriş İletişim Kutusu] Paketinize oteli dahil etmek ister misiniz (E/H)? e
7. Ne tür bir otele rezervasyon yaptırmak istersiniz? 1 - Motel (49,99 $), 2 - Standart Otel
(98,50 $), 3 - Lüks Otel (199,75 $)
8. [Giriş İletişim Kutusu] Otel numarasını girin: 4
9. Hata: Otel türü (2) Standart Otel'e atandı. 4 girdiniz
10. [Giriş İletişim Kutusu] Otel odası sayısını girin: 0
11. Hata: Otel odası sayısı 1'e sıfırlandı. 0 girdiniz
12. [Giriş İletişim Kutusu] Otelde kalınacak gece sayısını girin: -1
13. Hata: Gece sayısı 1'e sıfırlandı. -1 girdiniz
14. Uçak ve otel rezervasyonları yapıldı.
15. 1 gezgin(ler) için Chicago'ya toplam uçuş fiyatı: $200.0
16. Standart Otel'de 1 oda (lar) için 1 gecelik toplam otel fiyatı $98,5
17. Uçak ve otel toplam paket fiyatı 298,5$
18.
````

````c#
Console.WriteLine("Seyahat Acentesine Hoş Geldiniz");

Console.Write("Kaç Kişi Seyahat Edeceksiniz: ");
int kisi = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Uçuş Rezervasyonu Yapmak İçin Destinasyonlardan Birini Seçiniz:");
Console.WriteLine("1. Chicago (200$)    2. Los Angeles (360$)    3. Miami (320$)     4. Orlando (310$)    5. Seattle (330$)");

int secim = Convert.ToInt32(Console.ReadLine());
int total = 0;

if (secim == 1)
{
    total += 200;
}

else if  (secim == 2)
{
    total += 360;
}

else if (secim == 3)
{
    total += 320;
}

else if (secim == 4)
{
    total += 310;
}

//-------------------otel kısmı-----------------------------
Console.WriteLine("Pakete Oteli Eklemek İstermisiniz? (e/h)");
string otel = Console.ReadLine();



if (otel == "e" || otel == "E")
{

    Console.WriteLine("1. Motel (50$), 2. Standart Otel (99$), 3. Lüküs Otel (200$)");
    int otelNumarası = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("Otel odası sayısını girin:");
    int odaSayısı = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("Otel kalınacak gece sayısını girin:");
    int geceSayısı = Convert.ToInt32(Console.ReadLine());


    if (otelNumarası == 1)
    {
        total += 50;
    }

    else if (otelNumarası == 2)
    {
        total += 99;
    }

    else if (otelNumarası == 3)
    {
        total += 200;
    }


    int odenecektutar = (odaSayısı * total * geceSayısı + kisi * total);
        Console.WriteLine("Uçuş ve Otel Kayıtlarınız Oluşturuldu.");
        Console.WriteLine($"Ödenecek Tutar. {odenecektutar}$");
}
int cıkıstoplam = (total * kisi);

if (otel == "h" || otel == "H")
{
    Console.WriteLine($"Ödenecek Tutar {cıkıstoplam}$");
}
````
