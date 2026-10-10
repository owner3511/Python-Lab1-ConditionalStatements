a = float(input("Çəkinizi daxil edin: "))
b = float(input("boyunuzu yazın: "))
BMI = a/(b*b)
if BMI < 18.5:
    print("Category: Underweight")
elif 18.5 <= BMI < 25:
    print("Category: Normalweight")
elif 25 <= BMI < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")