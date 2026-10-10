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
       