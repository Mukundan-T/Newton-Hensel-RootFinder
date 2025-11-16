from sympy import diff, Rational
from sympy.abc import x
from newton_helpers import function_value

def hensel_new_guess(polynomial, old_guess, prime):
    """
    Given a polynomial f(x), a previous guess value a_n, and a prime p, compute the
    new consecutive guess as given by Hensel's lemma and return it. This applies the
    formula

    a_{n+1} = a_n - [f(a_n)]/[f'(a_n)].

    If f'(a_n) is 0, the next guess is undefined; as such, return None.

    :param polynomial: a polynomial with p-adic integer coefficients
    :param old_guess: the previous guess computed through the iteration
    :param prime: a prime number p
    :return: the next consecutive guess if defined; else None
    """
    if hensel_derivative_is_zero(polynomial, prime, old_guess):
        return None
    
    numerator = function_value(polynomial, old_guess)
    denominator = function_value(diff(polynomial, x), old_guess)
    return Rational(old_guess, 1) - numerator / denominator

def hensel_derivative_is_zero(polynomial, prime, value):
    """
    Return true if the derivative of the given polynomial at the given value is
    zero mod p, and false otherwise.

    :param polynomial: a polynomial with p-adic integer coefficients
    :param prime: a prime p
    :param value: a given input x value
    :return: true if f'(x) == 0 (mod p); false otherwise
    """
    derivative_value = function_value(diff(polynomial, x), value)
    return derivative_value % prime == 0