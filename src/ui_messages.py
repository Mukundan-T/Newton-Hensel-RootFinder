from enum import Enum

class Messages(Enum):
    """
    This class holds all of the messages that could be displayed to the user.
    """
    # Input messages
    NEWTON_INPUT_MESSAGE = "Please enter a real-valued function (ex. 2*x**2 + cos(x)): "
    HENSEL_INPUT_MESSAGE = "Please enter a polynomial with integer coefficients " \
    "(e.g. 2*x**2 + 3x - 1): "
    PRIME_MESSAGE = "Please enter a prime to be the base of the modulus: "
    INITIAL_GUESS_MESSAGE = "Please enter an initial guess: "
    MODULUS_POWER_MESSAGE = "Please enter a power of the modulus: "
    
    # Accuracy messages
    NEWTON_ACCURACY_MESSAGE = "Please enter the number of decimal places of the desired root: "
    HENSEL_ACCURACY_MESSAGE = "Please enter the number of terms desired in the sequence: "

    # Error messages
    FUNCTION_ERROR_MESSAGE = "Error parsing the function. Please ensure that your " \
    "function is a valid mathematical expression."
    FLOAT_ERROR_MSG = "Please make sure you enter a valid real number!"
    INT_ERROR_MSG = "Please make sure you enter a valid positive integer!"
    PRIME_ERROR_MESSAGE = "Please ensure your prime number is actually prime!"