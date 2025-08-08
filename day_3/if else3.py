weight = float(input("enter your weight in kg: "))
height + float(input("enter your height in cm: "))
bmi = weight / (height**2)
if bmi > 25:
    print("over weight")
elif bmi >=18.5:
    print("normal weight")
else:
    print("under weight")