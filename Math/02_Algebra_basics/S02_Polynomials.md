
#   Polynomials (Polinomios)

<!--
#T# Table of contents

#C# Solve equations using the subtraction and addition properties of equality (Solucionar ecuaciones usando las propiedades sustractiva y aditiva de la igualdad)
#C# Solve equations using the division and multiplication properties of equality (Solucionar ecuaciones usando las propiedades divisiva y multiplicativa de la igualdad)
#C# Linear equation definitions (Definiciones de ecuaciones lineales)
#C# Solve equations with fraction or decimal coefficients (Solucionar ecuaciones con coeficientes fraccionales o decimales)

#C# Addition and subtraction of polynomials (Adición y sustracción de polinomios)
#C# Multiplication properties of exponents (Propiedades de los exponentes)
#C# Multiplication of polynomials (Multiplicación de polinomios)
#C# Division of polynomials (División de polinomios)
#C# Scientific notation (Notación científica)
#C# Polynomial factoring (Factorización de polinomios)

#T# Beginning of content
-->

#   Linear equations (Ecuaciones lineales)

## Solve equations using the subtraction and addition properties of equality (Solucionar ecuaciones usando las propiedades sustractiva y aditiva de la igualdad)

Solving an equation commonly means isolating a variable to find its value.

The subtraction property of equality is used to solve equations when there is a positive term added to the variable, then said term is subtracted from both sides of the equality, helping in isolating the variable.

The addition property of equality is used to solve equations when there is a negative term which subtracts from the variable, then said term is added to both sides of the equality, helping in isolating the variable.

## Solve equations using the division and multiplication properties of equality (Solucionar ecuaciones usando las propiedades divisiva y multiplicativa de la igualdad)

The division property of equality is used to solve equations when there is a factor multiplying the variable, then both sides of the equality are divided by said factor, helping in isolating the variable.

The multiplication property of equality is used to solve equations when there is a number dividing the variable, then said number is multiplied to both sided of the equality, helping in isolating the variable.

## Linear equation definitions (Definiciones de ecuaciones lineales)

Linear equations can start with variable terms on both sides. When equations have variables and constants on both sides, the properties of equality can be used to move the variables and put them in one side if needed. For example, if a variable is dividing a number, it can be passed to the other side by using the multiplication property of equality, multiplying both sides by the variable.

(Lado para variables de una ecuación)
**Variable side of an equation**: A side of an equation that can be arbitrarily chosen to hold variables, or a single variable, in order to isolate it and find its value.

(Lado para constantes de una ecuación)
**Constant side of an equation**: The other side of an equation that is produced when choosing a variable side.

(Ecuación lineal)
**Linear equation**: an equation in which the variables have an exponent of $1$.

(Ecuación lineal en una variable)
**Linear equation in one variable**: linear equation in which there is only one variable. These equations can be simplified by using the properties of equality to create a variable side and a constant side.
[Simplification of linear equations in one variable code](Programs/S08/Simplification_of_linear_equations_in_one_variable.py)

> Form of a linear equation in one variable
>
> Let $a$, $b$, be numbers, $x$ be a variable, then
> $$a x = b$$

Every linear equation in one variable can be simplified through the use of the properties of equality, to leave it in the form $a x = b$. The side $a x$ is the variable side, and the side $b$ is the constant side.

(Combinar términos variables)
**Collect variable terms**: the process of combining the like terms of a variable in one side, this creates the variable side of the equation.

(Combinar términos constantes)
**Collect constant terms**: the process of combining like terms without variables, this creates the constant side of the equation.

## Solve equations with fraction or decimal coefficients (Solucionar ecuaciones con coeficientes fraccionales o decimales)

Equations with fractions and decimals behave ultimately the same as regular equations.

(Eliminar los denominadores de una ecuación)
**Clear an equation of fractions**: the process of clearing the fractions of an equation, by multiplying each term on both sides by the least common denominator.

#   Polynomials (Polinomios)

## Addition and subtraction of polynomials (Adición y sustracción de polinomios)

Terms can be represented using symbols, $ax^n$ is a general representation of a term, where $x$ is the variable and $a$, $n$ are constants.

(Polinomio)
**Polynomial**: expression of one or more terms added together. If the only variable in a polynomial is $x$, the polynomial can be denoted as $p(x)$ or using other letters, as $q(x)$. For example $p(x) = x^2 + 5x^3 - 4x - 7$.

(Monomio)
**Monomial**: a polynomial with only one term.

(Binomio)
**Binomial**: a polynomial with two terms.

(Trinomio)
**Trinomial**: a polynomial with three terms.

(Grado de un polinomio)
**Degree of a polynomial**: the degree of the term $ax^n$ is the exponent $n$. In a polynomial with several terms, the degree is the maximum of the exponents. For example, in $p(x) = x^2 + 5x^3 - 4x - 7$, the degree of $p(x)$ is $3$ because that's the maximum exponent in the terms.

(Forma estándar de un polinomio)
**Standard form of a polynomial**: a polynomial with its terms written in descending order of the exponents of one given variable. For example, the standard form of $p(x) = x^2 + 5x^3 - 4x - 7$ is $p(x) = 5x^3 + x^2 - 4x - 7$.

(Adición de polinomios)
**Addition of polynomials**: the operation of addition made with polynomials. Addition of polynomials is based on combining like terms, i.e. only the terms with the same variables and exponents are added together. For example, given $p(x) = 2x^3 + 4x - 7$ and $q(x) = 3x - 2$, then $p(x) + q(x) = 2x^3 + 7x - 9$.

(Sustracción de polinomios)
**Subtraction of polynomials**: the operation of subtraction made with polynomials. Subtraction of polynomials is bases on combining like terms, i.e. only the terms with the same variables and exponents can be subtracted from one another. For example, given $p(x) = 2x^3 + 4x - 7$ and $q(x) = 3x - 2$, then $p(x) - q(x) = 2x^3 + x - 5$.

Addition and subtraction of polynomials can be done programatically.
[Addition and subtraction of polynomials code](Programs/S10/Addition_and_subtraction_of_polynomials.py)

(Evaluación de polinomios)
**Polynomial evaluation**: polynomial evaluation is done like regular evaluation of expressions. For example, in $p(x) = 5x^3 + x^2 - 4x - 7$ evaluating $p(x)$ in $2$ gives $p(2) = 5(2)^3 + (2)^2 - 4(2) - 7 = 40 + 4 - 8 - 7 = 44 - 15 = 29$, so evaluating $p(x)$ in $2$ gives $29$.

## Multiplication properties of exponents (Propiedades de los exponentes)

(Producto de potencias de igual base)
**Product property of exponents**: the product of two equal bases, each with their exponent, is equal to the base raised to the sum of the exponents.

> Product property of exponents
>
> Let $a$, $m$, $n$ be numbers, then
> $$a^m a^n = a^{m + n}$$

(Potencia de una potencia)
**Power property of exponents**: the result of raising a base to an exponent and then raising that power to another exponent, is equal to the base raised to the power of the product of the exponents.

> Power property of exponents
>
> Let $a$, $m$, $n$ be numbers, then
> $${(a^m)}^n = a^{m n}$$

(Producto de potencias con el mismo exponente)
**Product to a power property of exponents**: the product of two bases with the same exponent, is equal to the product of the bases raised to the power of the exponent.

> Product to a power property of exponents
>
> Let $a$, $b$, $n$ be numbers, then
> $$a^n b^n = {(a b)}^n$$

(Multiplicación de monomios)
**Monomial multiplication**: let $a$, $b$, $k$, $l$, $m$, $n$, be numbers and $x$, $y$ be variables, then the product of the monomials $ax^ky^l$ and $bx^my^n$ is $abx^{k + m}y^{l + n}$.

## Multiplication of polynomials (Multiplicación de polinomios)

The multiplication of polynomials is based on the distributive property of multiplication over addition (and subtraction). In the product of two polynomials, each term of the first polynomial is multiplied by the second polynomial using the distributive property.
[Multiplication of polynomials code](Programs/S10/Multiplication_of_polynomials.py)

> Example of multiplication of polynomials
>
> Let $ax^2 + bx + c$ and $dx + e$ be two polynomials, then their product is
> 
> $$\begin{gathered}
> (ax^2 + bx + c)(dx + e)\\
> = adx^3 + aex^2 + bdx^2 + bex + cdx + ce\\
> = adx^3 + (ae + bd)x^2 + (be + cd)x + ce
> \end{gathered}$$

## Division of polynomials (División de polinomios)

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
[Division of polynomials code](Programs/S10/Division_of_polynomials.py)

> Division of polynomials
>
> Let $x$ be a variable, $p(x)$, $g(x)$ be the two polynomials being divided, let $q(x)$ be the quotient of the division, and $r(x)$ be the remainder, then
> $$\frac{p(x)}{g(x)} = q(x) + \frac{r(x)}{g(x)}$$

This result follows the same form of mixed numbers, but instead of numbers, polynomials are used.

> Example of division of polynomials
>
> Let $3x^2 - 5x + 8$ and $2x - 7$ be the two polynomials being divided, then
> $$\frac{2x - 7}{3x^2 - 5x + 8} = \frac{2x - 7}{3x^2 - 5x + 8}$$
> This division can not be made any further, the degree of the numerator is less than the degree of the denominator. The reciprocal can be done.
>
> $$\frac{3x^2 - 5x + 8}{2x - 7} \quad \to \qquad
> \begin{aligned}
> 3x^2\ -\ 5x\ +\ 8\hspace{8pt} &\underline{|\ 2x - 7}\\
> -3x^2 + \frac{21}{2}x\hspace{25pt} & \ \frac{3}{2}x + \frac{11}{4}\\
> 0 + \frac{11}{2}x + 8\hspace{8pt} &\\
> - \frac{11}{2}x + \frac{77}{4} &\\
> 0 + \frac{109}{4} &
> \end{aligned}$$
> So
> $$\frac{3x^2 - 5x + 8}{2x - 7} = \frac{3x}{2} +  \frac{11}{4} + \frac{109/4}{2x - 7}$$

## Scientific notation (Notación científica)

Scientific notation is a way to express numbers. A given number written in scientific notation is represented as a number greater than or equal to 1 and less than 10, multiplied by a power of 10.

> Scientific notation
>
> Let $N$ be a number, $a$ be a number such that $a \ge 1$ and $a < 10$, and let $n$ be an integer, then
> $$N = a 10^n$$

To convert the given number $N$ to scientific notation, only its first nonzero digit is left as the first digit of $a$, and the remaining digits become decimals of $a$, this conversion is compensated as necessary using $n$, so that the equality $N = a 10^n$ is maintained. If $|N| \ge 1$ then $n$ must be zero or positive, while if $|N| < 1$ then $n$ must be negative. The sign of the number itself $N$ is not changed.

For example, the number $-3894.15509$ expressed in scientific notation is $-3.89415509 \cdot 10^3$, given that the decimal point was moved to the left (higher place values) the value of $n$ is positive $3$.

## Polynomial factoring (Factorización de polinomios)

(Factorización)
**Factoring**: the process of finding the factors of a product.

(Máximo factor común de dos expresiones)
**Greatest common factor of two expressions**: the largest expression that is a factor of the two given expressions. For example, given $3x^2 + 6x$ and $9x$, the greatest common factor is $3x$.
[Greatest common factor of two expressions code](Programs/S10/Greatest_common_factor_of_two_expressions.py)

(Máximo factor común de un polinomio)
**Greatest common factor of a polynomial**: the largest expression that is a factor of all the terms in a given polynomial. For example, in $12x^2 + 24x$ the greatest common factor is $12x$.

After doing polynomial factoring, a polynomial is represented as factors that are multiplying each other.
[Polynomial factoring code](Programs/S10/Polynomial_factoring.py)