from Term import Term
from Node import Node
#
#   This class implements evaluate, add and multiply for polynomials.
#
#   @author runb-cs112
#   @translator Brenton Bongcaron
#

##
# Reads a polynomial from an input stream (file or keyboard). The storage format
# of the polynomial is:
# <pre>
#     <coeff> <degree>
#     <coeff> <degree>
#     ...
#     <coeff> <degree>
# </pre>
# with the guarantee that degrees will be in descending order. For example:
# <pre>
#      4 5
#     -2 3
#      2 1
#      3 0
# </pre>
# which represents the polynomial:
# <pre>
#      4*x^5 - 2*x^3 + 2*x + 3
# </pre>
#
# @param sc Scanner from which a polynomial is to be read
# @throws IOException If there is any input error in reading the polynomial
# @return The polynomial linked list (front node) constructed from coefficients and degrees read from scanner
##
def read(in_file_name):
    poly = None
    input1 = open(in_file_name, "r")
    for line in input1:
        coeff, degree = (int(num) for num in line.split(" "))
        poly = Node(coeff, degree, poly)
    return poly
##
#   Returns the sum of two polynomials - DOES NOT change either of the input polynomials.
#   The returned polynomial MUST have all new nodes. In other words, none of the nodes
#   of the input polynomials can be in the result.
#
#   @param poly1 First input polynomial (front of polynomial linked list)
#   @param poly2 Second input polynomial (front of polynomial linked list
#   @return A new polynomial which is the sum of the input polynomials - the returned node is the front of the result polynomial
##
def add(poly1, poly2):
    poly3 = None
    # code here
    return poly3
##
#   Returns the product of two polynomials - DOES NOT change either of the input polynomials.
#   The returned polynomial MUST have all new nodes. In other words, none of the nodes
#   of the input polynomials can be in the result.
#
#   @param poly1 First input polynomial (front of polynomial linked list)
#   @param poly2 Second input polynomial (front of polynomial linked list)
#   @return A new polynomial which is the product of the input polynomials - the returned node is the front of the result polynomial
##
def mult(poly1, poly2):
    poly3 = None
    # code here
    return poly3
##
#   Evaluates a polynomial at a given value.
#
#   @param poly Polynomial (front of linked list) to be evaluated
#   @param x Value at which evaluation is to be done
#   @return Value of polynomial p at x
##
def evaluate(poly, x):
    eval = 0
    # code here
    return eval
##
#   Returns string representation of a polynomial
#
#   @param poly Polynomial (front of linked list)
#   @return String representation, in descending order of degrees
##
def toString(poly):
    if poly == None:
        return 0
    returnValue = poly.term.toString()
    current = poly.next
    while current != None:
        returnValue = current.term.toString() + " + " + returnValue
        current = current.next
    return returnValue