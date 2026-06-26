import random

print("""Welcome to Rock-Paper-Scisscors!
      press 1 to keep playing,
      press 2 to exit.""")

while True:
    a = int(input('Enter either "1" or "2":'))
    if a == 1:
        n = random.randint(1, 3)
        z = int(input("Enter 1 for rock, 2 for paper, 3 for scisscors:"))
        if z == n:
            print("Draw!")
            continue
        elif z == 1 and n == 2:
            print("I played paper, you lose!")
        elif z == 1 and n == 3:
            print("I played scisscors, I lose! :(")

        elif z == 2 and n == 3:
            print("I played scisscors, you lose! :(")
        elif z == 2 and n == 1:
            print("I played rock, you win! :(")

        elif z == 3 and n == 2:
            print("I played paper, you win!")
        elif z == 3 and n == 1:
            print("I played rock, you lose! :(")
        print()

    if a == 2:
        print("Exited.")
        break
