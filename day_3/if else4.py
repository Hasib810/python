print("welcome to pizza hut")
pizza = input("what size of pizza do you want? 10inch, 12inch or 14inch? ")
paper = input("do yo want paperoni? yes or no: ")
cheese = input("do you want extra cheese? yes or no: ")
#bill for size
bill = 0
if pizza == "10inch":
    bill += 300 
elif pizza == "12inch":
    bill += 500
elif pizza == "14inch":
    bill += 700 
#bill for paperoni
if paper == "yes":
    bill += 50
#bill for cheese
if cheese == "yes":
    bill += 100
print(f"your total bill is: ${bill}.")