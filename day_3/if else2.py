print("welcome to real madrid fc")
height = float(input("enter your height in cm: "))
if height >=170:
    print("you are eligible to play for madrid")
else:
    print("you are not eligible to play for madrid")
age = int(input("whats your age? "))
if age<=18:
    print("you can play in under 19 team")
elif age <=21:
    print("you can play in main team")
else:
    print("you are too old to play for madrid")