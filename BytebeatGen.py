from random import *

math = [">>", "+", "-", "/", "*"]
math2 = ["+", "-", "*"]

def main():
    print("t" + choice(math) + str(randrange(99)) + " " + choice(math2) + " t" + choice(math) + str(randrange(99)))
    again=input("Do you want to generate another bytebeat? Choose by using y/n\n").lower()
    if again == "y":
        main()
    else:
        return
 
main()