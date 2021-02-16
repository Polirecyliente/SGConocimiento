
#   Integers (Números enteros)

<!--
#T# Table of contents

#C# Introduction to integers (Introducción a los enteros)
#C# Addition of integers (Adición de enteros)
#C# Subtraction of integers (Sustracción de enteros)
#C# Multiplication and division of integers (Multiplicación y división de enteros)
#C# Solution of an equation with integers, multiplication and division properties of equality (Soluciones de una ecuación con enteros, propiedades multiplicativa y divisiva de la igualdad)

#T# Beginning of content
-->

## Introduction to integers (Introducción a los enteros)
[Ch03_S01](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=191)

(Números positivos y negativos)
**Positive and negative numbers**: positive numbers are greater than 0 and negative numbers are less than 0, so 0 is neither. Negative numbers are represented with a minus in front, e.g. $-5$ is negative $5$. Positive numbers are greater than negative numbers.

(Números opuestos)
**Opposite numbers**: pairs of numbers only differentiated by their sign, one is positive and the other one is negative, but their value is the same. Opposite numbers are obtained with the minus sign.
[Opposite numbers code](Programs/Ch03/S01_01_Opposite_numbers.py)

> Opposite numbers
>
> Let $a$ be a number, and $-a$ be its opposite, then
> $$-(-a) = a$$
> which means that the opposite of $-a$ is $a$, and
> $$-(a) = -a$$
> which means that the opposite of $a$ is $-a$.

(Números enteros)
**Integers**: the set of the whole numbers and the negative numbers. This set of numbers also forms an ordered set in which the relational operators can be used to compare the values of two integer numbers.

(Valor absoluto)
**Absolute value**: the distance between 0 and a given number, it's always positive and it's the same for any number and its opposite.
[Absolute value code](Programs/Ch03/S01_02_Absolute_value.py)

> Absolute value notation
>
> Let $a$ be a number, then its absolute value is
> $$\lvert a \rvert$$

For example, the absolute value of $-5$ is $5$, and the absolute value of $5$ is $5$, so $\lvert 5 \rvert = \lvert -5 \rvert = 5$.

## Addition of integers (Adición de enteros)
[Ch03_S02](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=209)

Addition of integers is no different from regular addition. Adding a negative number is the same as subtracting its opposite (just as adding a positive number is the same as subtracting its opposite).

Addition means moving in the same direction of the number being added, if the number being added is positive then the addition moves in the positive direction, if the number being added is negative then the addition moves in the negative direction.

## Subtraction of integers (Sustracción de enteros)
[Ch03_S03](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=224)

Subtraction of integers is no different from regular subtraction. Subtracting a negative number means moving opposite to its direction, i.e. moving in the positive direction.

In $a - (-b)$ the expression $- (-b)$ subtracts negative $b$, subtracting means moving in the opposite direction, so moving opposite to negative $b$ means adding positive $b$, and $a - (-b) = a + b$.

## Multiplication and division of integers (Multiplicación y división de enteros)
[Ch03_S04](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=244)

Multiplication and division of integers are no different from regular multiplication and division. When multiplying or dividing by a negative number, it changes the sign of the other number, so multiplying or dividing a negative number by another negative number results in a positive number, and multiplying or dividing a positive number by a negative number results in a negative number.

Multiplication means repeated addition, if the amount of repeated additions is negative, then this means repeated addition with each addition done in the opposite direction. For example, $4 \cdot -3 = -4 -4 -4$, each addition is done in the opposite direction of $4$, and in $-4 \cdot -3 = 4 + 4 + 4$, each addition is done in the opposite direction of $-4$.

Division means repeated subtraction until reaching 0, if the amount of repeated subtractions is negative, then this means repeated subtraction with each subtraction done in the opposite direction. For example, $24 \div -8 = -3$ so the number $-8$ is subtracted $-3$ times from $24$, i.e. $-8$ is subtracted three times in its opposite direction to reach 0 starting at 24. In $-24 \div -8 = 3$ the amount of repeated subtractions is positive, so $-8$ is subtracted directly from $-24$ three times to reach 0.

(Multiplicación por -1)
**Multiplication by -1**: a number multiplied by $-1$ results in its opposite.

> Multiply a number by $-1$
>
> Let $a$ be a number, then
> $$-1 \cdot a = -a$$

Using the definition of multiplication, multiplying $a$ by $-1$ is the same as adding $a$ one time in its opposite direction, which is $-a$, the opposite of $a$.

(División por -1)
**Division by -1**: a number divided by $-1$ results in its opposite.

> Divide a number by $-1$
>
> Let $a$ be a number, then
> $$a \div -1 = -a$$

Using the definition of division, dividing $a$ by $-1$ is the same as subtracting $-1$ from $a$ until reaching 0, which is $-a$ times, the opposite of $a$.

## Solution of an equation with integers, multiplication and division properties of equality (Soluciones de una ecuación con enteros, propiedades multiplicativa y divisiva de la igualdad)
[Ch03_S05](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=258)

The solution of an equation with integers is no different from a regular solution of an equation. A variable can be negative to satisfy an equation.

(Propiedad multiplicativa de la igualdad)
**Multiplication property of equality**: multiplying a number to both sides of an equality preserves the equality.

> Multiplication property of equality
>
> Let $a$, $b$, $c$ be numbers
>
> $$\begin{gathered}
> if\ a = b\\
> then\ a c = b c
> \end{gathered}$$

(Propiedad divisiva de la igualdad)
**Division property of equality**: dividing both sides of an equality by a nonzero number preserves the equality.

> Division property of equality
>
> Let $a$, $b$, $c$ be numbers, with $c$ being nonzero
>
> $$\begin{gathered}
> if\ a = b\\
> then\ \frac{a}{c} = \frac{b}{c}
> \end{gathered}$$