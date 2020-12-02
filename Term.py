#
#   This class implements a term of a polynomial
#
#   @author runb-cs112 (in Java)
#   @translator Brenton Bongcaron (in Python)
#

class Term:
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree

    def equals(self, other):
        return other != None and isinstance(other, Term) and self.coeff == t2.coeff and self.degree == t2.degree

    def toString(self):
        if self.degree == 0:
            return str(self.coeff) + ""
        elif self.degree == 1:
            return str(self.coeff) + "x";
        else:
            return str(self.coeff) + "x^" + str(self.degree)
