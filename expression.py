
from uncertainties.umath import *
from uncertainties import ufloat_fromstr

permitted_func_strings = {"acos", "acosh", "asin", "asinh",
                          "atan", "atanh", "ceil",
                          "cos", "cosh", "erf", "erfc",
                          "exp", "fabs", "factorial",
                          "floor", "gamma", "hypot", "lgamma",
                          "log", "modf", "pow",
                          "sin", "sinh", "sqrt", "tan",
                          "tanh", "trunc"}


def parse_expr(expr) -> set:
    """Returns a list of every contiguous sequence of letters in expr"""
    if len(expr) == 0:
        return set([])
    word = []
    words = []
    for c in (expr + '_'):
        if c.isalpha():
            word.append(c)
        else:
            word_str = "".join(word)
            if word_str != "":
                words.append(word_str)
            word.clear()
    return set(words)


class Expression:
    """Object representation of the expression input by user"""

    def __init__(self, expr_str):
        self.expr_str = expr_str.replace(" ", "")
        self.words = parse_expr(expr_str)

    def get_variables(self) -> set:
        """Returns all the variables in the expression."""
        result = []

        for word in self.words:
            if len(word) == 1:
                result.append(word)

        return set(result)

    def is_safe_to_exec(self) -> bool:
        """Must return true before using propagate_uncertainty()

        Ensures that the expression supplied by the user doesn't contain malicious code
        by checking contiguous characters against the list of permitted functions.
        """
        for word in self.words:
            if len(word) > 1 and word not in permitted_func_strings:
                return False
        return True

    def propagate_uncertainty(self, values) -> tuple:
        """Returns the value of the expression with uncertainty."""
        # x = ufloat_fromstr("0.20+/-0.01")
        # x = ufloat(1, 0.1)

        pass
