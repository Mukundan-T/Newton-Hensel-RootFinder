import hensel_helpers as hnsl
from terminal_ui import get_hensel_info

def hensel_roots(polynomial, initial_guess, prime, accuracy):
    """
    Given a polynomial with p-adic integer coefficients, an initial guess, a prime,
    and an accuracy, return the sequence of values obtained by applying Hensel's
    iteration. If the derivative evaluated at the initial guess is zero, then return
    an empty list and deem that there exist no roots in the p-adics for that particular
    p.

    :param polynomial: a polynomial with p-adic integer coefficients
    :param initial_guess: an initial guess provided by the user
    :param prime: a prime p
    :param accuracy: the number of terms desired by the user
    :return: a list of consecutive guesses computed by Hensel's lemma
    """
    approximations = [initial_guess]
    guess = initial_guess

    for _ in range(accuracy - 1):
        guess = hnsl.hensel_new_guess(polynomial, guess, prime)
        if not guess:
            print(f"""The derivative of the next term is zero, and as such, 
                  the method will likely fail. Therefore, there are no 
                  solutions in the {prime}-adics.""")
            return approximations
        else:
            approximations.append(str(guess))
        
    return approximations

def main():
    polynomial, initial_guess, prime, accuracy = get_hensel_info()
    print(f"Congruence: {polynomial} === 0 (mod {prime}^n)\n")
    
    roots = hensel_roots(polynomial, initial_guess, prime, accuracy)

    if len(roots) > 1:
        print("Sequence:\n")
        for i, root in enumerate(roots):
            print(f"Approximation {i+1}: {root}\n")

if __name__ == "__main__":
    main()