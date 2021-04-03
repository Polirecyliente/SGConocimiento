
#   Number sets (Conjuntos numéricos)

<!--
#T# Table of contents

#C# Introduction (Introducción)
#C# Addition (Adición)
#C# Subtraction (Sustracción)
#C# Multiplication (Multiplicación)
#C# Division (División)

#C# Introduction to integers (Introducción a los enteros)
#C# Addition of integers (Adición de enteros)
#C# Subtraction of integers (Sustracción de enteros)
#C# Multiplication and division of integers (Multiplicación y división de enteros)
#C# Solution of an equation with integers, multiplication and division properties of equality (Soluciones de una ecuación con enteros, propiedades multiplicativa y divisiva de la igualdad)

#C# Visualizing fractions (Visualizando fracciones)
#C# Multiplication and division of fractions (Multiplicación y división de fracciones)
#C# Multiplication and division of mixed numbers and complex fractions (Multiplicación y división de números mixtos y fracciones complejas)
#C# Addition and subtraction of fractions with common denominators (Adición y sustracción de fracciones con denominador común)
#C# Addition and subtraction of fractions with different denominators (Adición y sustracción de fracciones con denominador diferente)
#C# Addition and subtraction of mixed numbers (Adición y sustracción de números mixtos)
#C# Solution of an equation with fractions (Solución de una ecuación con fracciones)

#C# Definitions of decimals (Definiciones de decimales)
#C# Decimal operations (Operaciones con decimales)
#C# Decimals and fractions (Decimales y fracciones)
#C# Solution of an equation with decimals (Solución de una ecuación con decimales)
#C# Averages, probability (Promedios, probabilidad)
#C# Ratios, rates (Ratios, tasas)
#C# Square roots, simplification of square roots (Raíces cuadradas, simplificación de raíces cuadradas)

#C# Definitions of percents (Definiciones de porcentajes)
#C# Percentage applications (Aplicaciones de porcentajes)
#C# Sales tax, commissions, discounts (Impuesto de ventas, comisiones, descuentos)
#C# Simple interest (Interés simple)
#C# Proportions (Proporciones)

#C# Rational and irrational numbers (Números racionales e irracionales)
#C# Associative properties (Propiedades asociativas)
#C# Distributive property (Propiedad distributiva)
#C# Inverse properties, zero properties (Propiedades inversas, propiedades del cero)
#C# Systems of measurement (Sistemas de medida)

#T# Beginning of content
-->

#   Whole numbers (Números naturales y el cero)

## Introduction (Introducción)

(Números naturales)
**Counting numbers**: these are, 1, 2, 3, 4, ..., up to infinity

(Números naturales y el cero)
**Whole numbers**: these are, 0, 1, 2, 3, 4, ..., so the set of whole numbers is the same as the set of counting numbers and zero.

#   Integers (Números enteros)

## Introduction to integers (Introducción a los enteros)

(Números enteros)
**Integers**: the set of integers is the set of the whole numbers and the negative numbers. This set of numbers also forms an ordered set in which the relational operators can be used to compare the values of two integer numbers.

(Números positivos y negativos)
**Positive and negative numbers**: positive numbers are greater than 0 and negative numbers are less than 0, so 0 is neither. Negative numbers are represented with a minus in front, e.g. $-5$ is negative $5$. Positive numbers are greater than negative numbers.

(Números opuestos)
**Opposite numbers**: pairs of numbers only differentiated by their sign, one is positive and the other one is negative, but their value is the same. Opposite numbers are obtained with the minus sign.
[Opposite numbers code](Programs/S03/Opposite_numbers.py)

> Opposite numbers
>
> Let $a$ be a number, and $-a$ be its opposite, then
> $$-(-a) = a$$
> which means that the opposite of $-a$ is $a$, and
> $$-(a) = -a$$
> which means that the opposite of $a$ is $-a$.

(Valor absoluto)
**Absolute value**: the distance between 0 and a given number, it's always positive and it's the same for any number and its opposite.
[Absolute value code](Programs/S03/Absolute_value.py)

> Absolute value notation
>
> Let $a$ be a number, then its absolute value is
> $$\lvert a \rvert$$

For example, the absolute value of $-5$ is $5$, and the absolute value of $5$ is $5$, so $\lvert 5 \rvert = \lvert -5 \rvert = 5$.

(Múltiplos de un número)
**Multiples of a number**: given an integer, its multiples are the result of multiplying it by any of the counting numbers, so an integer has infinite multiples. The smallest multiple (in absolute value) is the integer itself.

(Divisibilidad)
**Divisibility**: if a given integer $b$ is multiple of another $a$, then $b$ is divisible by $a$, because $\frac{b}{a}$ is an integer. All the multiples of $a$ are divisible by $a$.
[Divisibility code](Programs/S02/Divisibility.py)

(Números pares)
**Even numbers**: 0 and the multiples of 2.

(Números impares)
**Odd numbers**: the integers that are not even numbers.

(Factores de un entero)
**Factors of an integer**: in a given integer, its factors are the integers that multiplied together produce it. An integer can have several different sets of factors, e.g. $12$ has different sets of factors like $3$, $4$, also $2$, $6$, or $2$, $3$, $2$, or others.
[Find factors code](Programs/S02/Find_factors.py)

(Pares de factores)
**Factor pairs**: factors can always be presented in pairs, because at least two integers are required to be multiplied together in order to produce a given integer. In the example of $12 = 2 \cdot 3 \cdot 2$, with factor pairs the equation would be $12 = 2 \cdot 6$ or $12 = 3 \cdot 4$.

(Factorización)
**Factoring**: the process of finding the factors of a product.

(Números primos)
**Prime numbers**: each of the integers with only 2 different factors, the number 1 and the integer itself.

(Números compuestos)
**Composite numbers**: the integers that are not prime, i.e. the integers that have more than one factor pair.

(Factores primos)
**prime factors**: the set of prime numbers that multiplied together produce a given integer. Integers can be represented as the product of prime factors.

(Descomposición en factores primos)
**Prime factorization**: the process of finding the prime factors of an integer.
[Prime factorization code](Programs/S02/Prime_factorization.py)

(Multiplicidad de un factor primo)
**Multiplicity of a prime factor**: the amount of times that a prime factor of a given integer is repeated, e.g. in the number $60$ the prime factors are $2$, $2$, $3$, $5$, the number $2$ has a multiplicity of $2$, the number $3$ has a multiplicity of $1$, and the number $5$ has a multiplicity of $1$.

(Múltiplos comunes)
**Common multiples**: given a set of at least two integers, the common multiples are the numbers that are multiples of all the integers in the set.

(Mínimo común múltiplo)
**Least common multiple**: the smallest common multiple of a given set of at least two integers.
[Least common multiple code](Programs/S02/Least_common_multiple.py)

The least common multiple of two integers can be calculated using their prime factors. The least common multiple of two integers is the product of all their unique prime factors, each raised to the power of their maximum multiplicity.

For example, to find the least common multiple of $12$ and $18$, the prime factors of $12$ are $2$, $2$, $3$, and the prime factors of $18$ are $2$, $3$, $3$. The least common multiple is $2 \cdot 2 \cdot 3 \cdot 3 = 36$, the number $2$ has a maximum multiplicity of $2$ (in $12$), and $3$ has a maximum multiplicity of $2$ (in $18$).

(Mínimo común denominador)
**Least common denominator**: the least common multiple of the denominators from a set of at least two fractions.

(Máximo común divisor)
**Greatest common divisor**: the biggest common divisor of a given set of at least two integers.
[Greatest common divisor code](Programs/S02/Greatest_common_divisor.py)

The greatest common divisor of two integers can be calculated using their prime factors. The greatest common divisor of two integers is the product of their common prime factors, each raised to the power of their minimum multiplicity.

In this use of the term "divisor", it is also a factor of the set of numbers. That's why sometimes this is also called greatest common factor (Máximo factor común).

#   Rational numbers (Números racionales)

(Números racionales)
**Rational numbers**: the set of numbers that can be represented via fractions. This is an ordered set in which the relational operators can be used to compare the values of two rational numbers.

Rational numbers when represented as decimals, have their decimal part with a finite amount of digits, or if the amount is infinite then it repeats itself, which means that a decimal number that is rational can always be represented as a fraction.

## Visualizing fractions (Visualizando fracciones)

(Fracciones)
**Fractions**: numbers that represent a part of a whole number or an integer, so there are many fractions between any two integers. This set of numbers also forms an ordered set in which the relational operators can be used to compare the values of two fractions.

(Notación de las fracciones)
**Fraction notation**: given that fractions are numbers that can be between two integers, they are represented with a division, a fraction that is not integer has a remainder different from 0 when represented as a division. The fraction $\frac{a}{b}$ is calculated as $a$ divided by $b$, with $b$ being nonzero.
[Fraction notation code](Programs/S04/Fraction_notation.py)

For example, $\frac{2}{3}$ means $2$ divided by $3$, and using the definition of division, this calculates the amount of times that the number $3$ is subtracted from $2$ until 0 is reached, but subtracting $3$ from $2$ gives $-1$ because $2 - 3 = -1$, so to reach 0, a proportion, fraction, or part of $3$ must be subtracted from $2$, and not the full unity of the number $3$.

By the definition of division, $\frac{2}{3}$ is the amount of times that $3$ is subtracted from $2$ to reach 0. This amount, $\frac{2}{3}$ is between $0$ and $1$ and it occupies the same proportional distance to $1$, as the number $2$ occupies to $3$, as shown in the figure.
[Fraction diagram image code](Programs/S04/Fraction_diagram_image.py)
![Fraction diagram image](Images/S04/Fraction_diagram.png)
*Fraction diagram*

(Numerador y denominador)
**Numerator and denominator**: the numbers in a fraction, the numerator is the number on top (called dividend in the division operation), and the denominator is the number at the bottom (called divisor in the division operation). In $\frac{a}{b}$ $a$ is the numerator and $b$ is the denominator.

(Fracciones propias)
**Proper fractions**: a fraction $\frac{a}{b}$ in which $a < b$. A proper fraction is always between 0 and 1.

(Fracciones impropias)
**Improper fractions**: a fraction $\frac{a}{b}$ in which $a \ge b$. An improper fraction can be an integer (when $a$ is a multiple of $b$), and it is always greater than or equal to 1, which means that an improper fraction has an integer part and a proper fraction part, when said parts are added the result is the improper fraction.
[Improper fractions code](Programs/S04/Improper_fractions.py)

(Números mixtos)
**Mixed numbers**: the representation of an improper fraction as an integer part and a proper fraction part.

> Mixed numbers notation
>
> Let $a$ be an integer, and $\frac{b}{c}$ be a proper fraction, the mixed number they form together is denoted as
> $$a\frac{b}{c}$$

When adding together this numbers, $a + \frac{b}{c}$ the result is the improper fraction $\frac{ac + b}{c}$ with the same value.

The term $ac$ in the numerator of $\frac{ac + b}{c}$, is a multiple of $c$, so when dividing $ac$ by $c$ the result is an integer $a$. In the mixed number $a\frac{b}{c}$, $a$ is the integer part, and $\frac{b}{c}$ is the proper fraction part.

(Fracciones equivalentes)
**Equivalent fractions**: fractions that have the same value, even when written with different numbers. Fractions written with different numbers can have the same value because those different numbers can show the same fraction. For example, the fraction $\frac{2}{3}$ is the same as the fraction $\frac{4}{6}$, because the proportional distance that the number $2$ occupies in $3$ is the same as the proportional distance that the number $4$ occupies in $6$. The value of each fraction itself is the same in equivalent fractions.

(Propiedad de las fracciones equivalentes)
**Equivalent fractions property**: in a given fraction $\frac{a}{b}$, multiplying (or dividing) both the numerator and the denominator by a nonzero number $c$, doesn't change the value of the fraction, so $\frac{a}{b} = \frac{ac}{bc}$.

## Multiplication and division of mixed numbers and complex fractions (Multiplicación y división de números mixtos y fracciones complejas)

(Multiplicación y división de números mixtos)
**Multiplication and division of mixed numbers**: this operations are done the same as multiplication and division of proper fractions. The mixed numbers should be converted to improper fractions first, as shown earlier.

(Fracciones complejas)
**Complex fractions**: the division of two fractions, $\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a}{b} \div \frac{c}{d} = \frac{a d}{b c}$.

(Simplificación de fracciones complejas)
**Simplification of complex fractions**: complex fractions are simplified like regular fractions.
[Simplification of complex fractions](Programs/S04/Simplification_of_complex_fractions.py)

(Simplificación de expresiones con fracciones)
**Simplification of expressions with fractions**: expressions with fractions are simplified like regular expressions
[Simplification of expressions with fractions](Programs/S04/Simplification_of_expressions_with_fractions.py)

(Fracciones negativas)
**Negative fractions**: when either the numerator is negative, or the denominator is negative, the fraction itself is negative, $\frac{-a}{b} = -\frac{a}{b}$, and $\frac{a}{-b} = -\frac{a}{b}$.

## Addition and subtraction of fractions with different denominators (Adición y sustracción de fracciones con denominador diferente)

(Evaluación de expresiones con fracciones)
**Evaluation of expressions with fractions**: like regular evaluation.

## Solution of an equation with fractions (Solución de una ecuación con fracciones)

An equation with fractions can have a fraction solution, just like a regular solution.

#   Real numbers (Números reales)

#   Decimals (Decimales)

## Definitions of decimals (Definiciones de decimales)

(Decimales)
**Decimals**: the numeric representation of fractions in the place value system. Proper fractions have a value less than 1, to express them as decimals, the places to the right of the units place are used. The separation between the units place and the decimal places is commonly shown with a dot. For example, the numbers 0.1, 3.541, etc.

About their place value, the first place to the right of the dot has its value multiplied by 10 to the -1, the second place has its value multiplied by 10 to the -2, the third place to the -3, and so on.

(Decimales equivalentes)
**Equivalent decimals**: different decimal numbers that have the same value. For example $10.3$ has the same value as $10.30$, or $10.300$.

(Redondeo de decimales)
**Decimal rounding**: like regular rounding.

## Decimals and fractions (Decimales y fracciones)

(Decimal finito)
**Finite decimal**: a decimal with a finite amount of digits after the decimal period.

(Decimal periódico)
**Repeating decimal**: a decimal in which a group of digits after the decimal period repeats itself indefinitely. They can be expressed as fractions and vice versa.
[Repeating decimals code](Programs/S05/Repeating_decimals.py)

Repeating decimals are denoted with a horizontal bar over the digits that repeat. For example, in $\frac{8}{7} = 1.\overline{142857}$, the line over $142857$ indicates that it repeats itself infinitely many times.

(La constante pi)
**The pi constant**: the fraction of the circumference over the diameter. It's represented with the greek letter pi, which is $\pi$. The value of pi is roughly $\pi = 3.14159...$, this is a non repeating decimal.

(Fórmula de la circunferencia)
**Circumference formula**: formula to find the length of the circumference of a circle from the length of its radius.

> Circumference formula
>
> Let $d$ be the diameter in length units, $r$ be the radius in length units, $C$ be the circumference in length units, then
>
> $$\begin{gathered}
> \pi := \frac{C}{d}\\
> d = 2 r\\
> C = \pi d = 2 \pi r
> \end{gathered}$$

(Fórmula del área de un círculo)
**Circle area formula**: formula to find the area occupied by a circle, from the length of its radius.

> Circle area formula
>
> Let $A$ be the area of a circle in squared length units, $r$ be the radius in length units, then
> $$A = \pi r^2$$

This is because when dividing the circle in many small sectors, and then lining the circumference $C$ (measured in length units) to make a straight line, the result is half a rectangle of sides $C$ and $r$, so $A = \frac{C r}{2} = \frac{2 \pi r r}{2} = \pi r^2$.

(Aproximación fraccionaria de pi)
**Fractional approximation of pi**: there are infinitely many fractional approximations of pi, one of the simplest is $\frac{22}{7}$.

#   Percents

## Definitions of percents (Definiciones de porcentajes)

(Porcentaje)
**Percent**: ratio with a denominator of 100. A percent number is identified with the percent sign $\%$ after it. For example $54\%$ means the ratio $\frac{54}{100}$.

## Percentage applications (Aplicaciones de porcentajes)

(Ecuación de porcentaje)
**Percentage equation**: an equation that defines a percent. To define a percent, two concepts are needed, the base (la base) and the amount (la cantidad). The base is the number that represents the whole, and the amount is the number that represents the part or fraction of that whole.

> Parts of a percentage equation
>
> Let $p\%$ be a percent, $B$ be the base, $A$ be the amount, then
> $$A = p\% \cdot B$$

If $p < 100$, then $A < B$, which means that $A$ is a fraction of $B$.

Isolating the base allows finding its value from the amount and the percent, $B = \frac{A}{p\%}$.

The reciprocal of a percent, $\frac{1}{p\%}$, means the reciprocal of a ratio. If a percent $p\%$ means the part over the total, i.e. there are $p$ part units per group of $100$ total units, then $\frac{1}{p\%}$ means that there are $100$ total units per group of $p$ part units.

Isolating the percent allows finding its value from the amount and the base, $p\% = \frac{A}{B}$.

#   Real numbers (Números reales)

## Rational and irrational numbers (Números racionales e irracionales)

(Números irracionales)
**Irrational numbers**: the set of numbers such as $\pi$, in which the decimal part of the number is infinite and never repeats itself. The square root of numbers that are not perfect squares is also irrational.

The fact that they are called irrational, doesn't necessarily mean that they can't have predictable patterns, for example, a number such as $0.101001000100001000001...$ is irrational by definition, but it can be understood as the number with a $1$ in between a steady growing number of $0$s. This pattern is infinite and never repeats itself, so it's an irrational number.

(Números reales)
**Real numbers**: the union of the sets of rational and irrational numbers.

## Transcendental numbers (Números trascendentes)

The transcendental numbers are numbers that can't be obtained as a solution of a polynomial with rational coefficients.

For example $\sqrt{2}$ is not transcendental because it is the solution of $x^2 = 2$, which is a polynomial with rational coefficients.

(La constante pi)
**The pi constant**: the fraction of the circumference over the diameter. It's represented with the greek letter pi, which is $\pi$. The value of pi is roughly $\pi = 3.14159...$, this is a non repeating decimal. $\pi$ is a transcendental number because there is no polynomial with rational coefficients whose solution is $\pi$.