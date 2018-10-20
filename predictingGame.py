# Learning-Phyton
from random import randint

guess = randint(1, 10)
sayac = 0
while True:
    sayac += 1
    sayı = int(input("1 ila 10 arası bir sayı giriniz"))
    if sayı < guess:
        print("daha yüksek bir sayı giriniz")
        continue
    elif sayı > guess:
        print("daha düşük bir sayı giriniz")
        continue
    elif sayı == guess:
        print("tahmin sayınız{0}!".format(sayac))
        print("kazanılan puan:-{0}".format(sayac))
        break
    else:
        print("rastgele seçilen sayı 0 or bigger than 10")


