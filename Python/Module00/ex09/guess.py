import random

class guess_game:

    def __init__(self) -> None:
        self.num = random.randint(1,99)
        print("This is an interactive guessing game!",
            "You have to enter a number between 1 and 99 to find out the secret number.",
            "Type 'exit' to end the game.",
            "Good luck!", sep="\n")
        self.guess_num()

    def guess_num(self):
        finded = False
        iteration = 0
        while finded == False:
            iteration = iteration +1
            print("What's your guess between 1 and 99?")
            num_choice = input()
            if num_choice == "exit":
                print("Goodbye!")
                break
            
            elif num_choice.isnumeric():
                if self.num == int(num_choice):
                    finded = True
                    print("Congratulations, you've got it!",
                    f"You won in {iteration} attempts!", sep="\n")

                elif self.num > int(num_choice):
                    print("Too low!")
                
                else:
                    print("Too high!")
            
            else:
                print("That's not a number.")


def main():
    test = guess_game()

main()