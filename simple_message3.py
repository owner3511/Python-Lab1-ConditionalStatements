try:
    istek = int(input("BMI Hesaplayıcı icin 1 girin, Çin Burcu Hesaplayıcı icin 2 girin, "
                      "Doğum Günü Oyunu icin 3 girin: "))
    if istek == 1:
        try:
            a = float(input("Çəkinizi daxil edin: "))
            b = float(input("boyunuzu yazın: "))
            BMI = a / (b * b)
            if BMI < 18.5:
                print("Category: Underweight")
            elif 18.5 <= BMI < 25:
                print("Category: Normalweight")
            elif 25 <= BMI < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")
        except ValueError:
            print("Xəta: Zəhmət olmasa rəqəm daxil edin (hərf və ya boşluq yazmayın).")
    elif istek == 2:
        try:
            sozluk = {"Monkey": 0, "Rooster": 1, "Dog": 2, "Pig": 3, "Rat": 4, "Ox": 5, "Tiger": 6,
                      "Rabbit": 7, "Dragon": 8, "Snake": 9, "Horse": 10, "Sheep": 11}
            a = int(input("neçənci ildənsiniz: "))
            a = a % 12
            for i in sozluk:
                if a == sozluk[i]:
                    print("siz " + i + " ilindənsiniz")
        except ValueError:
            print("Xəta: Zəhmət olmasa düzgün il (rəqəm) daxil edin.")
    elif istek == 3:
        try:
            dogum_gunu = 0
            print("Set 1: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31")
            cevap = int(input("Doğum günün bu sette var mı? (Evet için 1, Hayır için 0): "))
            if cevap == 1:
                dogum_gunu += 1
            print("Set 2: 2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31")
            cevap = int(input("Doğum günün bu sette var mı? (Evet için 1, Hayır için 0): "))
            if cevap == 1:
                dogum_gunu += 2
            print("Set 3: 4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31")
            cevap = int(input("Doğum günün bu sette var mı? (Evet için 1, Hayır için 0): "))
            if cevap == 1:
                dogum_gunu += 4
            print("Set 4: 8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31")
            cevap = int(input("Doğum günün bu sette var mı? (Evet için 1, Hayır için 0): "))
            if cevap == 1:
                dogum_gunu += 8
            print("Set 5: 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31")
            cevap = int(input("Doğum günün bu sette var mı? (Evet için 1, Hayır için 0): "))
            if cevap == 1:
                dogum_gunu += 16
            print("Tahmin edilen doğum günün:", dogum_gunu)
        except ValueError:
            print("Xəta: Zəhmət olmasa yalnız 1 və ya 0 daxil edin.")
except ValueError:
    print("Xəta: Zəhmət olmasa yalniz 1, 2 ve ya 3 daxil edin")