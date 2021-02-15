
#   Whole numbers (Números naturales y el cero)

<!--
#T# Table of contents

#C# Introduction (Introducción)
#C# Addition (Adición)
#C# Subtraction (Sustracción)
#C# Multiplication (Multiplicación)
#C# Division (División)

#T# Beginning of content
-->

## Introduction (Introducción)
[Ch01_S01](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=15)

(Números naturales)
**Counting numbers**: these are, 1, 2, 3, 4, ...

(Recta real)
**Number line**: the numbers depicted in a line.
[Number line image code](Programs/Ch01/S01_01_Number_line_image.py)
![Number line image](Images/Ch01/S01_01_Number_line.png)
*Number line*

(Origen)
**Origin**: this is the point at 0.

(Coordenada de un punto)
**Coordinate of a point**: this is the number, or numbers, tied to the point.

(Números naturales y el cero)
**Whole numbers**: these are, 0, 1, 2, 3, 4, ...

(Dígitos | Cifras)
**Digits**: each of the numeric values that makes up a number, e.g. the number $834$ has three digits, namely $8$, $3$, and $4$.

(Sistema de numeración posicional)
**Place value system**: system in which the value of a digit depends on its place in the number.

(Sistema de numeración decimal)
**Decimal place value system**: the most common place value system, each place is a power of 10, from right to left, starting at 0 in the first place, 1 in the second place and so on, so 10 is the base of the place value system, e.g. $345$ is $3$ in the third position ($3$ of 10 to the power of 2), $4$ is in the second position ($4$ of 10 to the power of 1), and $5$ is in the first position ($5$ of 10 to the power of 0), see Ch02_Algebra_language.md.

(Forma expandida de los números)
**Expanded form of the numbers**: numbers in a place value system can be shown in an expanded form, this expanded form is the sum of each of the digits in a given number multiplied by the base of the place value system to the power of its respective position, e.g. $345$ in expanded form is $3 \cdot 10^2 + 4 \cdot 10^1 + 5 \cdot 10^0$

(Grupos en la numeración posicional)
**Plave value periods**: these periods are the separation of digits in groups of three, each has a name, ones, thousands, millions, thousandths, millionths, etcetera.

(Redondeo)
**Rounding**: approximating a number with another of less significant digits.
[Rounding code](Programs/Ch01/S01_02_Rounding.py)

(Función techo)
**Ceiling function**: a function that approximates a number to the nearest bigger integer. Denoted as $\lceil x \rceil$, where $x$ is the number being rounded, e.g. $\lceil 2.5 \rceil = 3$, $\lceil -2.5 \rceil = -2$.

(Función piso)
**Floor function**: a function that approximates a number to the nearest smaller integer. Denoted as $\lfloor x \rfloor$, where $x$ is the number being rounded, e.g. $\lfloor 2.5 \rfloor = 2$, $\lfloor -2.5 \rfloor = -3$.

(Truncamiento)
**Truncation**: rounding a number by removing all digits after the decimal point, e.g. $2.5$ truncated is $2$, and $-2.5$ truncated is $-2$.

## Addition (Adición)
[Ch01_S02](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=32)

Addition is the operation of adding numbers together. Addition means starting at the end of the first number, and then moving the amount being added by the second number.
[Addition code](Programs/Ch01/S02_01_Addition.py)

(Operador suma)
**Sum operator**: this operator is $+$, the plus sign.

(Notación de la suma)
**Addition notation**: the addition of $a$ and $b$ is $a + b$, read as $a$ plus $b$ ($a$ más $b$), $a$, $b$ are called the addends (sumandos), the result is called the sum (suma).

> The addition of $a$ and $b$ is
> $$a + b$$

(Enunciado matemático)
**Math statement**: any math writing that can be read as a statement, with symbols, signs, numbers, operators, etc.

(Expresión matemática)
**Math expression**: a math statement of numbers, symbols, and operations together.

> Example of a mathematical expression
> $$a + b + c$$

(Signo de igualdad)
**Equality sign**: this sign is $=$, the equal sign.

(Ecuación)
**Equation**: the math statement of two expressions that are equal

> Example of an equation
> $$a + b = c + d$$

(Definición matemática)
**Math definition**: an equation in which a symbol is defined.

> Definition notation
>
> Let $a$, $b$ be symbols, then
> $$a := b$$
> This is read as $a$ is defined as $b$ ($a$ es definido como $b$).

The sign $:=$ is used to make definitions, to differentiate it from the equal sign.

(Fórmula matemática)
**Math formula**: an equation whose purpose is to find the value of a quantity or variable, i.e. formulas are equations expressly intended to find the value of a quantity, they are the "formula" to find said value.

(Propiedad de identidad de la suma)
**Identity property of addition**: adding to zero doesn't change the number

> Identity property of addition
>
> Let $a$ be a number, then
> $$a + 0 = a$$

(Identidad aditiva)
**Additive identity**: The number 0.

(Propiedad conmutativa de la suma)
**Commutative property of addition**: changing the order of the addends doesn't change the sum.

> Commutative property of addition
>
> Let $a$, $b$ be numbers, then
> $$a + b = b + a$$

Given that addition means after the first number move the amount of the second, commutativity means that no matter which number comes first and which second, the end position is the same.

(Símbolo de sumatoria)
**Summation symbol**: the symbol $\sum_i$ that represents the sum of the elements of the set to which $i$ belongs.

> General example of addition
> $$2 + 2 = 4$$

## Subtraction (Sustracción)
[Ch01_S03](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=48)

Subtraction is the operation of subtracting a number from another. Subtraction means starting at the end of the first number, and then moving in the opposite direction the amount of units being subtracted by the second number.
[Subtraction code](Programs/Ch01/S03_01_Subtraction.py)

(Operador resta)
**Subtraction operator**: this operator is $-$, the minus sign.

(Notación de la resta)
**Subtraction notation**: the subtraction of $a$ from $b$ is $b - a$, read as $b$ minus $a$ ($b$ menos $a$), $b$ is called the minuend (minuendo), $a$ is called the subtrahend (sustraendo), the result is called the difference (diferencia)

> The subtraction of $b$ from $a$ is
> $$b - a = c$$
> The value $c$ is the difference.

Addition and subtraction are inverse operations. 

Subtraction is not commutative.

> Non commutativity of subtraction
>
> Let $a$, $b$ be numbers,
>
> $$\begin{gathered}
> if\ a \ne b\\
> then\ a - b \ne b - a
> \end{gathered}$$

> General example of subtraction
> $$5 - 3 = 2$$

## Multiplication (Multiplicación)
[Ch01_S04](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=63)

Multiplication is the operation of multiplying numbers together. Multiplication means the repeated addition of a number with itself, the amount of repeated additions is the other number in the operation.
[Multiplication code](Programs/Ch01/S04_01_Multiplication.py)

(Operador multiplicación)
**Multiplication operator**: this operator is $\times$, the times sign. Another is $\cdot$, the dot sign. Another is $()$, the parentheses signs.

(Notación de la multiplicación)
**Multiplication notation**: the multiplication of $a$ and $b$ is $a b$, read as $a$ times $b$ ($a$ veces $b$), $a$, $b$ are called the factors (factores), the result is called the product (producto).

> The multiplication of $a$ and $b$ is
> $$a b = c$$
> The value $c$ is the product.

(Propiedad anulativa de la multiplicación)
**Multiplication property of zero**: the product of any number multiplied by 0, is 0.

> Multiplication property of zero
>
> Let $a$ be a number, then
> $$a \cdot 0 = 0$$

(Propiedad modulativa de la multiplicación)
**Identity property of multiplication**: the product of any number multiplied by 1, is the number itself.

> Identity property of multiplication
>
> Let $a$ be a number, then
> $$a \cdot 1 = a$$

(Identidad multiplicativa | elemento neutro | elemento identidad)
**Multiplicative identity**: The number 1.

(Propiedad conmutativa de la multiplicación)
**Commutative property of multiplication**: changing the order of the factors doesn't change the product.

> Commutative property of multiplication
>
> Let $a$, $b$, be numbers, then
> $$a b = b a$$

Given that multiplication means the repeated addition of the first number with itself a number of times equal to the second number, this means that no matter which number comes first and which second, the final repeated addition is the same.

> General example of multiplication
> $$4 \cdot 3 = 3 + 3 + 3 + 3 = 12$$

## Division (División)
[Ch01_S05](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=81)

Division is the operation of dividing a first number by a second number. Division means the repeated subtraction of the second number from the first number until reaching 0, the amount of repeated subtractions is the result of the operation.
[Division code](Programs/Ch01/S05_01_Division.py)

(Operador división)
**Division operator**: this operator is $\div$, the division sign. Another is $/$, the slash sign. Another is $\text{---}$, the horizontal line sign.

(Notación de la división)
**Division notation**: the division of $b$ over $a$ is $b/a$ or $\frac{b}{a}$, read as $b$ divided by $a$ ($b$ dividido $a$), $b$ is called the dividend (dividendo), $a$ is called the divisor (divisor), the result is called the quotient (cociente).

> The division of $b$ over $a$ is
> $$\frac{b}{a} = c$$
> The value $c$ is the quotient.

(Propiedad modulativa de la división)
**Identity property of division**: the quotient of any number divided by 1, is the number itself.

> Identity property of division
>
> Let $a$ be a number, then
> $$\frac{a}{1} = a$$

(Identidad divisiva)
**Divisive identity**: The number 1.

(Propiedad del cociente uno de la división)
**Division property of quotient one**: any non zero number divided by itself gives a quotient of 1.

> Division property of quotient one
>
> Let $a$ be a number, then
> $$\frac{a}{a} = 1$$

(Propiedades del cero en la división)
**Division properties of zero**: zero divided by any nonzero number is zero. Division by zero is undefined.

> Zero divided by a nonzero number
>
> Let $a$ be a number, then
> $$\frac{0}{a} = 0$$

> Division by zero is undefined
>
> Let $a$ be a number, then
> $$\frac{a}{0}\ is\ undefined$$

(Residuo | Resto)
**Remainder**: in division, this is the number that is left over after doing the repeated subtraction, if any.
[Remainder code](Programs/Ch01/S05_02_Remainder.py)

> Division with quotient and remainder
>
> Let $a$, $b$ be numbers with $b$ being nonzero, let $q$ be the quotient, $r$ be the remainder, then
> $$\frac{a}{b} = q + \frac{r}{b}$$

Multiplication and division are inverse operations.

Division is not commutative.

> Non commutativity of division
>
> Let $a$, $b$ be numbers,
> $$\begin{gathered}
> if\ a \ne b\\
> then\ \frac{a}{b} \ne \frac{b}{a}
> \end{gathered}$$

> General example of division
> $$\frac{28}{8} = 3 + \frac{4}{8}$$

(Paradigma de la multiplicación y división)
**Multiplication and division paradigm**: multiplication and division both deal with three concepts: a set of elements, groups of elements, and the size of said groups. Each of this concepts is associated with a number, the total number of elements, the amount of groups, and the size of each group.

Multiplication returns the total number of elements as the product of the amount of groups by the size of each group. For example, $5$ groups of size $4$, have a total number of elements of $5 \cdot 4 = 20$, and $4$ groups each with $5$ elements, have a total number of elements of $4 \cdot 5 = 20$. By itself, the total number of elements remains the same, $20$.

In multiplication, the amount of groups is interchangeable with the size of each group, so a multiplication can be interpreted as the amount of groups times their size, or as the size of the groups times the amount of groups, both interpretations are valid for any single multiplication.

Division has a similar behavior, the total number of elements is the dividend, but then, the divisor can be any of the other two numbers. The divisor can be the amount of groups, or the size of each group, and the quotient is the other number. For example, $24 \div 8 = 3$ means, from the $24$ total elements, with groups of size $8$, then there are $3$ groups, but $24 \div 8 = 3$ also means that from the $24$ total elements, with $8$ groups, each will have a size of $3$. Both conclusions are arrived via repeated subtraction.

The interpretation of $24 \div 8 = 3$ as $24$ elements divided in $8$ groups have a group size of $3$, means that there are $3$ elements per each $1$ group, so $24 \div 8 = 3 \div 1$, in words it could be read as, there are $24$ elements each $8$ groups, or there are $3$ elements each $1$ group.