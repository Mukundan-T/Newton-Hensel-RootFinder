from sympy import diff
from sympy.abc import x

def function_value(function, value):
    """
    Given a function and an input value, return the function evaluated at that input.

    :param function: a function f (or polynomial)
    :param value: an input x value
    :return: the function's value at that input or f(x)
    """
    return function.subs(x, value)

def count_decimal_places(number):
    """
    Given a number, return the number of decimal places it has, or 0 if none.

    :param number: a real number
    :return: the number of decimal places in number
    """
    s = str(number)
    if '.' in s:
        return len(s[s.index('.') + 1 : len(s)])
    return 0

def number_of_common_decimal_places(num_1, num_2):
    """
    Given two numbers, return the number of decimal places that they share in common.

    :param num_1: a real number
    :param num_2: a real number
    :return: an integer number of decimal places shared between num_1 and num_2
    """
    num_1 = str(num_1)
    num_2 = str(num_2)

    num_1_decimals = num_1[num_1.index('.') + 1 : len(num_1)]
    num_2_decimals = num_2[num_2.index('.') + 1 : len(num_2)]

    count = 0
    for i in range(len(num_1_decimals)):
        if i < len(num_2_decimals):
            if num_1_decimals[i] == num_2_decimals[i]:
                count += 1
        else:
            break

    return count

def newton_new_guess(function, old_guess):
    """
    Given a function f : R --> R and a guess x_n, return the next term in the Newton
    iteration sequence which is defined as

    x_{n+1} = x_n - [f(x_n)]/[f'(x_n)].

    If f'(x_n) is 0, the next guess is undefined; as such, return None.

    :param function: a real-valued function
    :param old_guess: a guess in Newton's method that determines the next one
    :return: the next term by Newton's method, or None if not applicable
    """
    if newton_derivative_is_zero(function, old_guess):
        return None
    
    numerator = function_value(function, old_guess)
    denominator = function_value(diff(function, x), old_guess)
    return old_guess - numerator / denominator

def newton_derivative_is_zero(function, value):
    """
    Return true if the derivative of the given function at the given value is
    zero, and false otherwise.

    :param function: a real-valued function f
    :param value: a given input x value
    :return: true if f'(x) == 0; false if f'(x) != 0
    """
    derivative_function = diff(function, x)
    return function_value(derivative_function, value) == 0