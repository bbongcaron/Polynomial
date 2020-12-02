import Term, Node

def main():
    file1 = input("Enter the name of the polynomial file => ")
    with open(file1, "r") as input1:
        for line in input1:
            coeff, degree = (int(num) for num in line.split(" "))
            term = Term.Term(coeff, degree)
            print(term.toString())

if __name__ == '__main__':
    main()
