from Term import Term
from Node import Node
import Polynomial

ADD = 1
MULTIPLY = 2
EVALUATE = 3
QUIT = 4

def getChoice():
    print()
    print(str(ADD) + ". ADD polynomial")
    print(str(MULTIPLY) + ". MULTIPLY polynomial")
    print(str(EVALUATE) + ". EVALUATE polynomial")
    print(str(QUIT) + ". QUIT")
    return int(input("\tEnter Choice # => "))

def add():
    file2 = input("Enter the file containing the polynomial to add => ")
    poly2 = Polynomial.read(file2)
    print("\n" + Polynomial.toString(poly2))
    print("Sum: " + Polynomial.toString(Polynomial.add(poly1, poly2)))

def multiply():
    file2 = input("Enter the file containing the polynomial to multiply => ")
    poly2 = Polynomial.read(file2)
    print("\n" + Polynomial.toString(poly2))
    print("Product: " + Polynomial.toString(Polynomial.multiply(poly1, poly2)))

def evaluate():
    x = float(input("Enter the evaluation point x => "))
    print("Value at " + str(x) + ": " + Polynomial.evaluate(poly1, x))

def main():
    file1 = input("Enter the name of the polynomial file => ")
    global poly1
    poly1 = Polynomial.read(file1)
    print("\n" + Polynomial.toString(poly1))
    choice = getChoice()
    while (choice != QUIT):
        if choice < ADD or choice > QUIT:
            print("\tIncorrect choice " + str(choice))
        else:
            if choice == ADD:
                add()
            elif choice == MULTIPLY:
                multiply()
            elif choice == EVALUATE:
                evaluate()
        choice = getChoice()

if __name__ == '__main__':
    main()
