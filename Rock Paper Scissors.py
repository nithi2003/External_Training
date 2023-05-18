import random
ai = 0
u = 0
while True:
    actions = ["rock","paper","scissors"]
    computer = random.choice(actions)
    user = input("Enter Choice from [rock,paper,scissors] : ")
    if user not in actions:
        print("Invalid Input. Enter Again")
    else:
        print("AI chosen : ",computer)
    if user=="rock":
        if computer=="rock":
            print("DRAW")
            print("User : ",u,"AI : ",ai)
        elif computer=="paper":
            ai+=1
            print("computer has won")
            print("User : ",u,"AI : ",ai)
        else:
            u+=1
            print("user has won")
            print("User : ",u,"AI : ",ai)
    elif user=="paper":
        if computer=="rock":
            u+=1
            print("computer has won")
            print("User : ",u,"AI : ",ai)
        elif computer=="paper":
            print("DRAW")
            print("User : ",u,"AI : ",ai)
        else:
            ai+=1
            print("user has won")
            print("User : ",u,"AI : ",ai)
    else:
        if computer=="rock":
            ai+=1
            print("Computer has won")
            print("User : ",u,"AI : ",ai)
        elif computer=="paper":
            u+=1
            print("user has won")
            print("User : ",u,"AI : ",ai)
        else:
            print("DRAW")
            print("User : ",u,"AI : ",ai)
    if u==5 or ai==5:
        if u==5 and u>ai:
            print("USER Has won the game")
            break
        else:
            print("Computer has won the game")
            break
