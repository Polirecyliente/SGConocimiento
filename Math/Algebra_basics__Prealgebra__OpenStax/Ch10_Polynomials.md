
#   Polynomials (Polinomios)

<!--
#T# Table of contents

#C# Addition and subtraction of polynomials (Adición y sustracción de polinomios)
#C# Multiplication properties of exponents (Propiedades de los exponentes)
#C# Multiplication of polynomials (Multiplicación de polinomios)
#C# Division of polynomials (División de polinomios)
#C# Scientific notation (Notación científica)
#C# Polynomial factoring (Factorización de polinomios)

#T# Beginning of content
-->

## Addition and subtraction of polynomials (Adición y sustracción de polinomios)
[Ch10_S01](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=861)

Terms (see Ch02_Algebra_language.md) can be represented using symbols, $ax^n$ is a general representation of a term, where $x$ is the variable and $a$, $n$ are constants.

(Polinomio)
**Polynomial**: expression of one or more terms added together. If the variable in a polynomial is $x$, the polynomial can be denoted as $p(x)$ or using other letters.

(Monomio)
**Monomial**: a polynomial with only one term.

(Binomio)
**Binomial**: a polynomial with two terms.

(Trinomio)
**Trinomial**: a polynomial with three terms.

(Grado de un polinomio)
**Degree of a polynomial**: the degree of the term $ax^n$ is the exponent $n$. In a polynomial with several terms, the degree is the maximum of the exponents.

(Forma estándar de un polinomio)
**Standard form of a polynomial**: a polynomial with its terms written in descending order of their exponents.

(Adición de polinomios)
**Addition of polynomials**: the operation of addition made with polynomials. Addition of polynomials is based on combining like terms, i.e. only the terms with the same variables and exponents are added together.

(Sustracción de polinomios)
**Subtraction of polynomials**: the operation of subtraction made with polynomials. Subtraction of polynomials is bases on combining like terms, i.e. only the terms with the same variables and exponents can be subtracted from one another.

Addition and subtraction of polynomials can be done programatically.
[Addition and subtraction of polynomials code](Programs/Ch10/S01_01_Addition_and_subtraction_of_polynomials.py)

(Evaluación de polinomios)
**Polynomial evaluation**: polynomial evaluation is done like regular evaluation of expressions.

## Multiplication properties of exponents (Propiedades de los exponentes)
[Ch10_S02](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=873)

(Producto de potencias de igual base)
**Product property of exponents**: the product of two equal bases, each with their exponent, is equal to the base raised to the sum of the exponents.

> Product property of exponents
>
> Let $a$, $m$, $n$ be numbers, then
> $$a^m \cdot a^n = a^{m + n}$$

(Potencia de una potencia)
**Power property of exponents**: the result of raising a base to an exponent and then raising that power to another exponent, is equal to the base raised to the power of the product of the exponents.

> Power property of exponents
>
> Let $a$, $m$, $n$ be numbers, then
> $$(a^m)^n = a^{m \cdot n}$$

(Producto de potencias con el mismo exponente)
**Product to a power property of exponents**: the product of two bases with the same exponent, is equal to the product of the bases raised to the power of the exponent.

> Product to a power property of exponents
>
> Let $a$, $b$, $n$ be numbers, then
> $$a^n \cdot b^n = (a \cdot b)^n$$

(Multiplicación de monomios)
**Monomial multiplication**: let $a$, $b$, $k$, $l$, $m$, $n$, be numbers and $x$, $y$ be variables, then the product of the monomials $ax^ky^l$ and $bx^my^n$ is $abx^{k + m}y^{l + n}$.

## Multiplication of polynomials (Multiplicación de polinomios)
[Ch10_S03](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=888)

The multiplication of polynomials is based on the distributive property of multiplication over addition (and subtraction). In the product of two polynomials, each term of the first polynomial is multiplied by the second polynomial using the distributive property.
[Multiplication of polynomials code](Programs/Ch10/S03_01_Multiplication_of_polynomials.py)

> Example of multiplication of polynomials
>
> Let $ax^2 + bx + c$ and $dx + e$ be two polynomials, then their product is
> $$(ax^2 + bx + c)(dx + e)\\
> = adx^3 + aex^2 + bdx^2 + bex + cdx + ce\\
> = adx^3 + (ae + bd)x^2 + (be + cd)x + ce$$

## Division of polynomials (División de polinomios)
[Ch10_S04](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=902)

(Cociente de potencias de la misma base)
**Quotient property of exponents**: the quotient of two exponents that have the same base, is equal to the base raised to the power of the exponent in the numerator minus the exponent in the denominator.

> Quotient property of exponents
>
> Let $a$, $m$, $n$, be numbers, then
> $$\frac{a^m}{a^n} = a^{m - n}$$

(Exponente negativo)
**Negative exponent**: the reciprocal of the base raised to the power of the exponent.

> Negative exponent
>
> Let $a$ and $n$ be numbers, then
> $$a^{-n} = \frac{1}{a^n}$$

(Exponente cero)
**Zero exponent**: a nonzero base raised to the power of zero is equal to one.

> Zero exponent
>
> Let $a$ be a nonzero number, so $a \ne 0$, then
> $$a^0 = 1$$

This is because, with any number $n$, $\frac{a^n}{a^n} = a^0 = 1$.

(Potencia de un cociente)
**Quotient to a power property of exponents**: the quotient of two bases with the same exponent, is equal to the quotient of the bases raised to the power of the exponent.

> Quotient to a power property of exponents
>
> Let $a$, $b$, $n$ be numbers, with $b$ being nonzero, then
> $$\frac{a^n}{b^n} = \left(\frac{a}{b}\right)^n$$

(División de monomios)
**Monomial division**: let $a$, $b$, $k$, $l$, $m$, $n$, be numbers and $x$, $y$ be variables, then the division of the monomial $ax^ky^l$ over $bx^my^n$ is $\frac{a}{b}x^{k - m}y^{l - n}$.

(División de polinomios)
**Division of polynomials**: this operation is done according to the degrees of the polynomials in the dividend and divisor. In a fraction of polynomials, if the degree of the numerator is less than the degree of the denominator, then that fraction can not be simplified further, i.e. it behaves as a proper fraction.

Long division of polynomials (División larga de polinomios) is a way to divide polynomials. With the polynomials in the fraction written in standard form, each individual term of the numerator from left to right is divided by the first term of the denominator, until the degree of the term being divided is less than the degree of the polynomial in the denominator.
[Division of polynomials code](Programs/Ch10/S04_01_Division_of_polynomials.py)

> Division of polynomials
>
> Let $x$ be a variable, $p(x)$, $g(x)$ be the two polynomials being divided, let $q(x)$ be the quotient of the division, and $r(x)$ be the remainder, then
> $$\frac{p(x)}{g(x)} = q(x) + \frac{r(x)}{g(x)}$$

This result follows the same form of mixed numbers, but instead of numbers, polynomials are used.

> Example of division of polynomials
>
> Let $3x^2 - 5x + 8$ and $2x - 7$ be the two polynomials being divided, then
> $$\frac{2x - 7}{3x^2 - 5x + 8} = \frac{2x - 7}{3x^2 - 5x + 8}
> $$ This division can not be made any further, the degree of the numerator is less than the degree of the denominator.
> $$\frac{3x^2 - 5x + 8}{2x - 7} \rarr
> \begin{aligned}3x^2\ -\ 5x\ +\ 8\hspace{8pt}            &\underline{|\ 2x - 7}\\
>               -3x^2 + \frac{21}{2}x\hspace{25pt}    & \ \frac{3}{2}x + \frac{11}{4}\\
>                   0 + \frac{11}{2}x + 8\hspace{8pt} &\\
>                     - \frac{11}{2}x + \frac{77}{4} &\\
>                                   0 + \frac{109}{4} &
> \end{aligned}
> $$ Then $$\frac{3x^2 - 5x + 8}{2x - 7} = \frac{3x}{2} +  \frac{11}{4} + \frac{109/4}{2x - 7}$$

## Scientific notation (Notación científica)
[Ch10_S05](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=922)

Scientific notation is a way to express numbers. A given number written in scientific notation is represented as a number greater than or equal to 1 and less than 10, multiplied by a power of 10.

> Scientific notation
>
> Let $N$ be a number, $a$ be a number such that $a \ge 1$ and $a < 10$, and let $n$ be an integer, then
> $$N = a \cdot 10^n$$

To convert the given number $N$ to scientific notation, only its first nonzero digit is left as the first digit of $a$, and the remaining digits become decimals of $a$, this conversion is compensated as necessary using $n$, so that the equality $N = a \cdot 10^n$ is maintained. If $|N| \ge 1$ then $n$ must be zero or positive, while if $|N| < 1$ then $n$ must be negative.

## Polynomial factoring (Factorización de polinomios)
[Ch10_S06](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=940)

(Factorización)
**Factoring**: the process of finding the factors of a product.

(Máximo factor común de dos expresiones)
**Greatest common factor of two expressions**: the largest expression that is a factor of the two given expressions.
[Greatest common factor of two expressions code](Programs/Ch10/S06_01_Greatest_common_factor_of_two_expressions.py)

(Máximo factor común de un polinomio)
**Greatest common factor of a polynomial**: the largest expression that is a factor of all the terms in a given polynomial.

After doing polynomial factoring, a polynomial is represented as factors that are multiplying each other.
[Polynomial factoring code](Programs/Ch10/S06_02_Polynomial_factoring.py)