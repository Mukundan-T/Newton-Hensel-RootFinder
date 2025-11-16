from terminal_ui import get_p_adic_congruences_info
from newton_helpers import function_value
from congruence_helpers import solves_congruence, alpha

def congruence_roots(polynomial, prime, power):
    """
    Given a polynomial f(x), prime p, and a power of the modulus n, solve the congruence

    f(x) === 0 (mod p^n)

    by starting with n = 1, then n = 2, and onwards until n == n. After every iteration,
    one more digit will be known in the p-adic expansion of the root. If there are no
    "base" roots mod p that solve the congruence, the polynomial has no roots in Z_p, so
    return none.

    :param polynomial: a polynomial with p-adic integer coefficients
    :param prime: the given prime number base by the user
    :param power: the power of the modulus
    :return: a dictionary containing all of the distinct roots mod p and their individual
    continuations as we solve the congruence mod higher powers of p; none if the polynomial
    has no roots in Z_p
    """
    roots = {}

    for i in range(prime):
        value = function_value(polynomial, i)
        if solves_congruence(value, prime, 1):
            roots[f"Base_Root_{i}"] = [i]

    if len(roots) == 0:
        print(f"There are no roots in the {prime}-adic numbers.")
        return None

    for i in range(2, power + 1):
        for root in list(roots.values()):
            j = 1
            root_candidate = root[0] + prime * j
            while root_candidate < pow(prime, i):
                value = function_value(polynomial, root_candidate)
                if solves_congruence(value, prime, i):
                    roots[f"Base_Root_{root[0]}"].append(root_candidate)
                j += 1
                root_candidate = root[0] + prime * j

    return roots

def compute_sequence(roots, prime):
    """
    Given a dictionary of the base roots mod p mapping to the full expansions mod higher
    powers of p, return a list of strings which each have the actual p-adic expansions
    with the appropriate coefficients for each p^i.

    ex) For a polynomial f(x) = x^2 - 2 === 0 (mod 7^4), one of the values of roots for the base
    root of 3 might look like [3, 10, 108, 2166], which tells us that 

    - f(3) === 0 (mod 7^1)
    - f(10) === 0 (mod 7^2)
    - f(108) === 0 (mod 7^3)
    - f(2166) === 0 (mod 7^4)

    Using this information, this function constructs the actual p-adic expansion of this particular
    root up to the existing accuracy. Here, it would look like

    3 + 1(7^1) + 2(7^2) + 6(7^3) = ...6213.

    :param roots: a dictionary containing all of the distinct roots mod p and their individual
    continuations as we solve the congruence mod higher powers of p
    :param prime: the user's desired prime
    :return: a list of strings, each of which is a p-adic expansion of the root(s)
    """
    sequences = []
    
    if roots:
        for root_list in list(roots.values()):
            digits = str(root_list[0])
            sequence = f"{root_list[0]} + "

            for i in range(1, len(root_list)):
                coefficient = alpha(root_list[i], root_list[i-1], prime ** i)
                sequence += f"{coefficient} ({prime}^{i})"
                digits = str(coefficient) + digits
                if i != len(root_list) - 1:
                    sequence += " + "

            sequence += f" = ...{digits}"
            sequences.append(sequence)
    
    return sequences

def main():
    polynomial, prime, power = get_p_adic_congruences_info()
    print(f"Congruence: {polynomial} === 0 (mod {prime}^{power})\n")
    
    roots = congruence_roots(polynomial, prime, power)
    print(str(roots) + "\n")

    series = compute_sequence(roots, prime)
    
    for i in range(len(series)):
        print(f"Root_{i}: " + series[i])

if __name__ == "__main__":
    main()