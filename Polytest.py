from Term import Term
from Node import Node
import Polynomial

def main():
    file1 = input("Enter the name of the polynomial file => ")
    poly = Polynomial.read(file1)
    print("\n" + Polynomial.toString(poly), end = "\n")

if __name__ == '__main__':
    main()
