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
  