import random

print("="*45)
print("----Welcome to Snake🐍- Water💧- Gun🔫----")
print("="*45)
print("Rules:")
print("- Snake drinks Water (Snake Wins)")
print("- Water ruins Gun (Water Wins)")
print("- Gun shoots Snake (Gun Wins)")
print("- Same choice is a Draw")
print("\nPress 'q' anytime to quit the game.\n")

user_score=0
comp_score=0
draw=0

youdict = {"s": 1, "w": 2, "g": 0}
rdict = {1: "Snake", 2: "Water", 0: "Gun"}

while True:

    youstr=input("Enter your choice (s , w ,g) : ")

    if youstr=='q':
        print(f"\nFinal score - You:{user_score} | Computer: {comp_score} | Draw: {draw} ")
        print("Thank you for playing")
        break

    if youstr not in ("s","w","g"):
        print("Invalid input.Please try again.\n")
        continue

    you=youdict[youstr]
    computer=random.choice([1,2,0])

    print(f"You chose {rdict[you]}")
    print(f"Computer chose {rdict[computer]}")

    if computer==you:
        print("Its a draw!\n")
        draw+=1

    else:
        if computer==2 and you==1:
            print("You Win!\n")
            user_score+=1

        elif computer==2 and you==0:
            print("You Lose!\n")
            comp_score += 1
        elif computer==1 and you==2:
            print("You Lose!\n")
            comp_score += 1
        elif computer == 1 and you == 0:
            print("You Win!\n")
            user_score += 1
        elif computer == 0 and you == 2:
            print("You Win!\n")
            user_score += 1
        elif computer == 0 and you == 1:
            print("You Lose!\n")
            comp_score += 1
        else:
            print("Something went wrong!\n")
