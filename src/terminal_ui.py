from sympy import parse_expr, isprime, Symbol
from ui_messages import Messages

def get_newton_info():
    """
    Obtain and return the info needed for Newton's method, which includes the function f,
    the initial guess, and the number of accurate decimal places of the root.

    :return: a tuple containing the function, initial guess, and accuracy
    """
    is_hensel = False

    function = get_function(Messages.NEWTON_INPUT_MESSAGE.value, is_hensel)
    initial_guess = get_initial_guess(Messages.INITIAL_GUESS_MESSAGE.value)
    accuracy = get_accuracy(Messages.NEWTON_ACCURACY_MESSAGE.value)

    return function, initial_guess, accuracy

def get_hensel_info():
    """
    Obtain and return the info needed for Hensel's lemma, which includes the polynomial f,
    the initial guess, the number of iterations of Hensel's lemma desired, and a prime p.

    :return: a tuple containing the polynomial, initial guess, prime, and accuracy
    """
    is_hensel = True

    polynomial = get_function(Messages.HENSEL_INPUT_MESSAGE.value, is_hensel)
    initial_guess = get_initial_guess(Messages.INITIAL_GUESS_MESSAGE.value)
    accuracy = get_accuracy(Messages.HENSEL_ACCURACY_MESSAGE.value)
    prime = get_prime(Messages.PRIME_MESSAGE.value)
    
    return polynomial, initial_guess, prime, accuracy

def get_p_adic_congruences_info():
    """
    Obtain and return the info needed to obtain a p-adic root by solving congruences mod higher
    powers of p, which includes the polynomial f, a prime p, and a power of the modulus.

    :return: a tuple containing the polynomial, prime, and power of modulus
    """
    is_hensel = True

    polynomial = get_function(Messages.HENSEL_INPUT_MESSAGE.value, is_hensel)
    prime = get_prime(Messages.PRIME_MESSAGE.value)
    power = get_power(Messages.MODULUS_POWER_MESSAGE.value)

    return polynomial, prime, power

def validate_func(message, function, is_hensel):
    """
    Given a string as a function and whether we checking for Hensel's Lemma (or not), 
    keep re-prompting the user for a new function or polynomial until actually valid.

    :param message: the message to display to the user asking for input
    :param function: the user's initial input as the function
    :param is_hensel: boolean to specify if the validation is done for Newton's 
    method or Hensel's Lemma
    :return: a parsed expression, which is either a function or a polynomial
    """
    x = Symbol('x')

    while True:
        try:
            expr = parse_expr(function)

            if expr.free_symbols - {x}:
                raise ValueError("Contains invalid symbols")

            if is_hensel:
                if expr.is_polynomial(x):
                    return expr
                else:
                    raise ValueError("Not a polynomial")
            
            return expr
            
        except Exception:
            print(Messages.FUNCTION_ERROR_MESSAGE.value)
            function = input(message)

def get_function(message, is_hensel):
    """
    Obtain, verify, and iterate until a valid function for the given process 
    (either Hensel's Lemma or Newton's method as given by is_hensel) is 
    obtained, and then return it.

    :param message: the message to display to the user asking for input
    :param is_hensel: boolean to specify if the validation is done for 
    Newton's method or Hensel's Lemma
    :return: a verified and valid function/polynomial
    """
    function = input(message)
    return validate_func(message, function, is_hensel)

def validate_guess(message, guess):
    """
    Given the user's initial guess, keep asking until the guess is valid, 
    and then return it.

    :param message: the message to display to the user asking for input
    :param guess: the first input by the user for the guess
    :return: a valid guess as a float
    """
    while True:
        try:
            guess = float(guess)
            return guess
        except Exception:
            print(Messages.FLOAT_ERROR_MSG.value)
            guess = input(message)

def get_initial_guess(message):
    """
    Obtain and return a valid float as the initial guess.

    :param message: the message to display to the user asking for input
    :return: a valid float as the initial guess
    """
    guess = input(message)
    return validate_guess(message, guess)

def validate_pos_integer(message, guess):
    """
    Given the user's input, keep asking until the input is a valid 
    positive integer, and then return it.

    :param message: the message to display to the user asking for input
    :param guess: the first input by the user for the accuracy
    :return: a valid accuracy as an int
    """
    while True:
        try:
            guess = int(guess)

            if guess <= 0:
                raise Exception

            return guess
        except Exception:
            print(Messages.INT_ERROR_MSG.value)
            guess = input(message)

def get_accuracy(message):
    """
    Obtain and return a valid int as the accuracy.

    :param message: the message to display to the user asking for input
    :return: a valid accuracy as an int
    """
    accuracy = input(message)
    return validate_pos_integer(message, accuracy)

def get_power(message):
    """
    Obtain and return a valid int as the power.

    :param message: the message to display to the user asking for input
    :return: a valid power as an int
    """
    power = input(message)
    return validate_pos_integer(message, power)

def verify_prime(message, prime):
    """
    Given the user's input, keep asking until the input is a valid 
    prime number, and then return it.

    :param message: the message to display to the user asking for input
    :param prime: the first input by the user for the prime
    :return: a valid prime as an int
    """
    while not isprime(prime):
        print(Messages.PRIME_ERROR_MESSAGE.value)
        prime = input(message)
        prime = validate_pos_integer(message, prime)
    
    return prime

def get_prime(message):
    """
    Obtain and return a valid int as the prime.

    :param message: the message to display to the user asking for input
    :return: a valid prime as an int
    """
    prime = input(message)
    prime = validate_pos_integer(message, prime)

    """while not isprime(prime):
        print(Messages.PRIME_ERROR_MESSAGE.value)
        prime = input(message)
        prime = validate_pos_integer(message, prime)"""
    
    return verify_prime(message, prime)