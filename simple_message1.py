sozluk = {"Monkey":0, "Rooster": 1, "Pig": 3, "Rat": 4, "Ox": 5, "Tiger": 6,
          "Rabbit": 7, "Dragon": 8, "Snake": 9, "Horse": 10, "Sheep": 11}
a = int(input("neçənci ildənsiniz: "))
a = a % 12
for i in sozluk:
    if a == sozluk[i]:
        print("siz " + i + " ilindənsiniz")