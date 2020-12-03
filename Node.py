import Term
#
#   This class implements a linked list node that contains a Term instance
#
#   @author runb-cs112 (in Java)
#   @translator Brenton Bongcaron (in Python)
#
class Node:
    def __init__(self, coeff, degree, next):
        self.term = Term.Term(float(coeff), degree)
        self.next = next
