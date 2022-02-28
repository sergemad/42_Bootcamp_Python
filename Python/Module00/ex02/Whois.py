import sys as sys

def whois(number: int)-> None:
    if number == 0:
        print("I'm Zero.")
    elif number%2 == 0: 
        print("I'm Even.")
    else:
        print("I'm Odd.")
        


def main():
    whois(int(sys.argv[1]))

main()
