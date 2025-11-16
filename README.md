# Newton-Hensel RootFinder

One important technique from numerical analysis is Newton's method, which is used to quickly approximate
the roots of real-valued functions. This project aimed to design a program which applied Newton's method over the real numbers, but also the monumental result from Hensel's lemma over the p-adic numbers to find roots of polynomials with p-adic integer coefficients. Future work will be focused on creating a nice UI
for this project and transforming it into an educational tool.

## About Newton-Hensel RootFinder

Newton-Hensel RootFinder is a classic program which outputs the sequence of iterated guesses when given the necessary ingredients to run (whether it be a function, polynomial, prime number, exponent power, etc.). The main files that when ran produce meaningful output is newton.py, congruences.py, and hensel_lift.py.

The file **newton.py** computes the successive iterations of Newton's method when given a real-valued function $f(x)$, an initial guess $x_0$, and an accuracy measured by the number of accurate digits to the root. It applies the formula $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$ iteratively, when $f'(x_n)$ is well defined.

The file **congruences.py** accepts a polynomial $f(x)$ with $p$-adic integer coefficients, a prime number $p$, and a power $n$, and computes the $p$-adic roots to the congruence $$f(x) \equiv 0 \pmod{p^n}.$$ Since $p^n$ can become quite large, please be considerate when entering your desired input values or else the program might take quite some time to run!

The file **hensel_lift.py** uses the result of Hensel's lemma to find roots over the $p$-adics. It accepts a polynomial $f(x)$ with $p$-adic integer coefficients, an initial guess $\alpha_0$, a prime number $p$, and an accuracy measured by the number of terms desired in the converging sequence $\alpha_n$. Here, the formula $$\alpha_{n+1} = \alpha{n} - \frac{f(\alpha_n)}{f'(\alpha_n)}$$ is iteratively applied, ensuring once again that $$f'(\alpha_n) \equiv 0 \pmod{p}.$$

## Using Newton-Hensel RootFinder

TBA