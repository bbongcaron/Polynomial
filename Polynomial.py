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
	# @return The polynomial linked list (front node) constructed from coefficients and
	#         degrees read from scanner
	##
def read(in_file_name):
    poly = None
    input1 = open(in_file_name, "r")
    for line in input1:
        coeff, degree = (int(num) for num in line.split(" "))
        poly = Node(coeff, degree, poly)
    return poly

def toString(poly):
    if poly == None:
        return 0
    returnValue = poly.term.toString()
    current = poly.next
    while current != None:
        returnValue = current.term.toString() + " + " + returnValue
        current = current.next
    return returnValue
