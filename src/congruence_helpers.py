def alpha(current_root, prev_root, modulus):
    """
    Return the next digit in the p-adic expansion of the root, given the current and previous
    root, by looking at the number of multiples of p that separate the two roots.

    ex) Suppose f(3) === 0 (mod 7) and f(17) === 0 (mod 7^2). Then, we know that the coefficient
    of the (7^1) term in the p-adic expansion of the root is (17-3)/7 = 2. So return 2. Now, if
    f(115) === 0 (mod 7^3), then the coefficient of the (7^2) term is (115-17)/(7^2) = 2. So
    return 2.

    :param current_root: the current value which solves the congruence mod p^(n)
    :param prev_root: the previous value which solved the congruence mod p^(n-1)
    :param modulus: the modulus of the congruence, which is p^(n-1)
    :return: an integer representing the number of factors of the prime that separates the current
    and previous roots
    """
    return (current_root - prev_root) // modulus

def solves_congruence(value, prime, power):
    """
    Given a function value, prime, and a power, return true if this function value is
    congruent to 0 mod prime^power.

    :param value: the function value at a particular input value
    :param prime: the prime number desired by the user
    :param power: the power of the modulus
    :return: true if the given function value is congruent to 0 mod prime^power; false otherwise
    """
    return value % pow(prime, power) == 0