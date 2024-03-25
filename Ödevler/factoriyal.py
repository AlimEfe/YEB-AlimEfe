number = int(input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
factorial = 1
i = 1
 
if number >= 0:
    while i <= number:
        factorial *= i
        i += 1
    print(f"Girdiğiniz sayının faktöriyeli: {number}! = {factorial}")
else:
    print("Negatif sayıların faktöriyeli olmaz!")