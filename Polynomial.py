from Term import Term
from Node import Node
##
#   This class implements evaluate, add and multiply for polynomials.
#
#   @author runb-cs112
#   @translator Brenton Bongcaron
##

##
#   Reads a polynomial from an input stream (file or keyboard). The storage format
#   of the polynomial is:
#   <pre>
#       <coeff> <degree>
#        <coeff> <degree>
#       ...
#       <coeff> <degree>
#   </pre>
#   with the guarantee that degrees will be in descending order. For example:
#   <pre>
#        4 5
#       -2 3
#        2 1
#        3 0
#   </pre>
#   which represents the polynomial:
#   <pre>
#       4*x^5 - 2*x^3 + 2*x + 3
#   </pre>
#
#   @param sc File name from which a polynomial is to be read
#   @return The polynomial linked list (front node) constructed from coefficients and
#           degrees read from scanner
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
#   @return A new polynomial which is the sum of the input polynomials - the returned node
#           is the front of the result polynomial
##
def add(poly1, poly2):
    front = None
    tail = None
    ptr1 = poly1
    ptr2 = poly2
    newNode = None
    did_First_Addition = False

    while ptr1 != None or ptr2 != None:
        if ptr1 == None:
            # Check: No more terms are left in poly1
            # Action: Create Nodes containing the remaining Terms in poly2's linked list
            newNode = Node(ptr2.term.coeff, ptr2.term.degree, None)
            ptr2 = ptr2.next
        elif ptr2 == None:
            # Check: No more terms are left in poly1
            # Action: Create Nodes containing the remaining Terms in poly1's linked list
            newNode = Node(ptr1.term.coeff, ptr1.term.degree, None)
            ptr1 = ptr1.next
        elif ptr1.term.degree < ptr2.term.degree:
            # Check: poly1's pointer is pointed at the smaller degree term
            # Action: Create a new Node containing this poly1 Node's term
            newNode = Node(ptr1.term.coeff, ptr1.term.degree, None)
            ptr1 = ptr1.next
        elif ptr1.term.degree > ptr2.term.degree:
            # Check: poly2's pointer is pointed at the smaller degree term
            # Action: Create a new Node containing this poly2 Node's term
            newNode = Node(ptr2.term.coeff, ptr2.term.degree, None)
            ptr2 = ptr2.next
        else: # ptr1.term.degree == ptr2.term.degree
            # Action: Sum the coefficients of these terms and create a new Node containing
            # a Term of the common degree & coefficient sum
            newNode = Node(ptr1.term.coeff + ptr2.term.coeff, ptr1.term.degree, None)
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if newNode.term.coeff == 0:
            # Terms with a 0 coefficient should be omitted
            continue

        if not did_First_Addition:
            # Initialize front when first Node is created
            front = newNode
            did_First_Addition = True

        if tail == None:
            # When the first result Node is created, set the tail to be that Node
            tail = newNode
        else:
            # Append newNode to the end of front linked list (tail)
            tail.next = newNode
            # Update linked list's new tail
            tail = tail.next
    return front
##
#   Returns the product of two polynomials - DOES NOT change either of the input polynomials.
#   The returned polynomial MUST have all new nodes. In other words, none of the nodes
#   of the input polynomials can be in the result.
#
#   @param poly1 First input polynomial (front of polynomial linked list)
#   @param poly2 Second input polynomial (front of polynomial linked list)
#   @return A new polynomial which is the product of the input polynomials - the returned node
#           is the front of the result polynomial
##
def mult(poly1, poly2):
    if poly1 == None or poly2 == None:
        # 0 times any polynomial is 0
        return None

    front = None
    tail = None
    ptr1 = poly1

    while ptr1 != None:
        ptr2 = poly2
        tempFront = None
        tempTail = None
        newNode = None
        did_First_Distribution = False
        while ptr2 != None:
            # Action: Multiply coefficients, add degrees
            newNode = Node(ptr1.term.coeff*ptr2.term.coeff, ptr1.term.degree + ptr2.term.degree, None)
            ptr2 = ptr2.next

            if not did_First_Distribution:
                # Initialize tempFront when first Node is created
                tempFront = newNode
                did_First_Distribution = True

            if tempTail == None:
                # When the first tempFront Node is created, set the tail to be that Node
                tempTail = newNode
            else:
                # Append newNode to the end of tempFront linked list (tail)
                tempTail.next = newNode
                # Update linked list's new tail
                tempTail = tempTail.next
        if front == None:
            # Initialize front to be resulting polynomial of the first distribution
            front = tempFront
        else:
            # Add current resulting distribution polynomial to front
            front = add(front, tempFront)
        ptr1 = ptr1.next
    return front
##
#   Evaluates a polynomial at a given value.
#
#   @param poly Polynomial (front of linked list) to be evaluated
#   @param x Value at which evaluation is to be done
#   @return Value of polynomial p at x
##
def evaluate(poly, x):
    eval = float(0)
    ptr = poly
    while (ptr != None):
        eval += float(ptr.term.coeff*pow(x, ptr.term.degree))
        ptr = ptr.next
    return str(eval)
##
#   Returns string representation of a polynomial
#
#   @param poly Polynomial (front of linked list)
#   @return String representation, in descending order of degrees
##
def toString(poly):
    if poly == None:
        return "0"
    returnValue = poly.term.toString()
    current = poly.next
    while current != None:
        returnValue = current.term.toString() + " + " + returnValue
        current = current.next
    return returnValue
