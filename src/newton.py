from terminal_ui import get_newton_info
import newton_helpers as nwtn

def newton_root(function, guess, accuracy):
    """
    Given a function, initial guess, and accuracy (in terms of number of decimal
    places), return the list of guesses by Newton's method. If at any point in
    the iterative process, the derivative becomes zero, then return the guesses 
    computed so far and deem that reaching the root isn't possible.

    :param function: a real-valued function
    :param guess: the initial guess given by the user
    :param accuracy: the number of accurate decimal places given by the user
    :return: a list of consecutive guesses computed by Newton's method
    """
    approximations = [guess]
    refining_our_guess = True

    while refining_our_guess:
        previous_guess = guess
        guess = nwtn.newton_new_guess(function, previous_guess)

        if not guess:
            print("\nSince the derivative value at the initial guess is zero, " \
            "the existence of a root is not guaranteed.")
            return approximations
        else:
            approximations.append(guess)
        
        agreed_places = nwtn.number_of_common_decimal_places(guess, previous_guess)
        if agreed_places >= accuracy:
            refining_our_guess = False

    return approximations

def main():
    function, guess, accuracy = get_newton_info()
    sequence_of_guesses = newton_root(function, guess, accuracy)
    print("\nSequence of root values: " + str(sequence_of_guesses) + "\n")

if __name__ == "__main__":
    main()