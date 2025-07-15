#count BMI

print("welcome to count program BMI")

weight = float(input("enter weight for count BMI"))
height = float(input("enter height for count BMI"))


BMI = weight / height ** 2


if BMI < 18.5:
    print("Under weight")
    print(f"your weight {BMI}")

elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight")
    print(f"your weight {BMI}")

elif BMI >= 25.0 and BMI <= 29.9:
    print("Over weight")
    print(f"your weight {BMI}")

else:
    print("30.0 and above: Obese")
    print(f"your weight {BMI}")



