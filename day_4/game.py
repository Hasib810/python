import random
choice = int(input("what will be your choice? '1' for stone, '2' for paper, '3' for scissor\n"))
computer_choice = random.randint(1, 3)
print(f"computer choice is {computer_choice}")

if choice >=3 or choice <1:
    print("invalid choice, you lose")
elif choice == "1" and computer_choice == "3":
    print("you win")
elif computer_choice == "1" and choice == "3":
    print("you lose")
elif choice == computer_choice:
    print("draw")
elif choice < computer_choice:
    print("you lose")
elif choice > computer_choice:
    print("you win")
