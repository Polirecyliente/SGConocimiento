
#   Number operations (Operaciones numéricas)

(Operadores relacionales)
**Relational operators**: operators that compare the values of two numbers. These operators serve to make the set of numbers an ordered set, ordered according to the values of the numbers.
[Relational operators code](Programs/S03/Relational_operators.py)

(Igualdad)
**Equality**: when the values of two quantities are equal, $a = b$ means the value of $a$ is equal to the value of $b$. The equal sign is the $=$ sign.

(Ecuación)
**Equation**: the math statement of two expressions that are equal

> Example of an equation
> $$a + b = c + d$$

(Desigualdad)
**Inequality**: when the values of two quantities are strictly not equal, or may not be equal.

(Mayor que)
**Greater than**: the comparison of two numbers where the first is greater than the second. The operator is $>$, the greater than sign. $a > b$, read as $a$ greater than $b$ ($a$ mayor que $b$), means that the value of $a$ is greater than the value of $b$.

(Menor que)
**Less than**: the comparison of two numbers where the first is less than the second. The operator is $<$, the less than sign. $a < b$, read as $a$ less than $b$ ($a$ menor que $b$), means that the value of $a$ is less than the value of $b$.

(Mayor o igual que)
**Greater than or equal to**: the comparison of two numbers where the first is greater than or equal to the second. The operator is $\ge$, the greater than or equal to sign. $a \ge b$, read as $a$ greater than or equal to $b$ ($a$ mayor o igual que $b$), means that the value of $a$ is greater than or equal to the value of $b$.

(Menor o igual que)
**Less than or equal to**: the comparison of two numbers where the first is less than or equal to the second. The operator is $\le$, the less than or equal to sign. $a \le b$, read as $a$ less than or equal to $b$ ($a$ menor o igual que $b$), means that the value of $a$ is less than or equal to the value of $b$.

(Diferente a)
**not equal to**: the comparison of two numbers where they have different values. The operator is $\ne$, the not equal to sign. $a \ne b$, read as $a$ not equal to $b$ ($a$ diferente a $b$), means that the value of $a$ is not equal to the value of $b$.

(Adición de números reales)
**Addition of real numbers**: Addition is the operation of adding numbers together. Addition means starting at the end of the first number, and then moving the amount being added by the second number.
[Addition code](Programs/S03/Addition.py)

Addition is the inverse operation of subtraction. Given that addition means after the first number move the amount of the second, commutativity means that no matter which number comes first and which second, the end position is the same.

Adding a negative number is the same as subtracting its opposite (just as adding a positive number is the same as subtracting its opposite). Addition means moving in the same direction of the number being added, if the number being added is positive then the addition moves in the positive direction, if the number being added is negative then the addition moves in the negative direction.

(Operador suma)
**Sum operator**: this operator is $+$, the plus sign.

(Notación de la suma)
**Addition notation**: the addition of $a$ and $b$ is $a + b = c$, read as $a$ plus $b$ ($a$ más $b$), $a$, $b$ are called the addends (sumandos), the result $c$ is called the sum (suma).

> The addition of $a$ and $b$ is $c$
> $$a + b = c$$

(Propiedad de identidad de la suma)
**Identity property of addition**: adding a real number with zero doesn't change the number.

> Identity property of addition
>
> Let $a$ be a real number, then
> $$a + 0 = a$$

(Identidad aditiva)
**Additive identity**: The number 0.

(Propiedad conmutativa de la suma)
**Commutative property of addition**: changing the order of the addends doesn't change the sum.

> Commutative property of addition
>
> Let $a$, $b$ be real numbers, then
> $$a + b = b + a$$

(Propiedad asociativa de la adición)
**Associative property of addition**: using grouping symbols to group addition operations does not change the sum.

> Associative property of addition
>
> Let $a$, $b$, $c$ be real numbers, then
> $$a + b + c = (a + b) + c = a + (b + c)$$

(Inverso aditivo)
**Additive inverse**: the opposite of a number, is its additive inverse. The additive inverse of a number $a$ is $-a$.

(Propiedad inversa aditiva)
**Inverse property of addition**: the sum of a number and its additive inverse is zero.

> Inverse property of addition
>
> Let $a$ be a real number, then
> $$a + (-a) = a - a = 0$$

(Adición de fracciones con denominador común)
**Addition of fractions with common denominators**: the same as normal addition. It must be noted that $\frac{a}{b} = a\frac{1}{b}$, which means that $\frac{a}{b} + \frac{c}{b} = a\frac{1}{b} + c\frac{1}{b} = (a + c)\frac{1}{b} = \frac{a + c}{b}$.

(Adición de fracciones con denominador diferente)
**Addition of fractions with different denominators**: first the fractions being added must have common denominators, for this, each fraction is converted to an equivalent fraction such that its denominator is the common one. The common denominator can be found as the least common denominator of the fractions. The addition is done like regular addition when the denominators are common.

(Adición de números mixtos)
**Addition of mixed numbers**: like regular addition. The integer parts of the mixed numbers can be added directly, and the proper fraction parts are added with the rules of addition of fractions, the result is the sum of the integer and fraction parts. To show the result as a mixed number, the integer part is left alone, and the fraction part is converted to a proper fraction if necessary, this may change the integer part.

(Sustracción de números reales)
**Subtraction of real numbers**: Subtraction is the operation of subtracting a number from another. Subtraction means starting at the end of the first number, and then moving in the opposite direction the amount of units being subtracted by the second number. Subtraction is the inverse operation of addition.
[Subtraction code](Programs/S03/Subtraction.py)

Subtracting a negative number means moving opposite to its direction, i.e. moving in the positive direction. In $a - (-b)$ the expression $- (-b)$ subtracts negative $b$, so moving opposite to negative $b$ means adding positive $b$, and $a - (-b) = a + b$.

Subtraction is not commutative.

> Non commutativity of subtraction
>
> Let $a$, $b$ be numbers,
>
> $$\begin{gathered}
> if\ a \ne b\\
> then\ a - b \ne b - a
> \end{gathered}$$

(Operador resta)
**Subtraction operator**: this operator is $-$, the minus sign.

(Notación de la sustracción)
**Subtraction notation**: the subtraction of $a$ from $b$ is $b - a = c$, read as $b$ minus $a$ ($b$ menos $a$), $b$ is called the minuend (minuendo), $a$ is called the subtrahend (sustraendo), the result $c$ is called the difference (diferencia).

> The subtraction of $b$ from $a$ is $c$
> $$b - a = c$$
> The value $c$ is the difference.

(Sustracción de fracciones con denominador común)
**Subtraction of fractions with common denominators**: the same as normal subtraction. It must be noted that $\frac{a}{b} = a\frac{1}{b}$, which means that $\frac{a}{b} - \frac{c}{b} = a\frac{1}{b} - c\frac{1}{b} = (a - c)\frac{1}{b} = \frac{a - c}{b}$.

(Sustracción de fracciones con denominador diferente)
**Subtraction of fractions with different denominator**: first the fractions being subtracted must have common denominators, for this, each fraction is converted to an equivalent fraction such that its denominator is the common one. The common denominator can be found as the least common denominator of the fractions. The subtraction is done like regular subtraction when the denominators are common.

(Sustracción de números mixtos)
**Subtraction of mixed numbers**: the integer parts of the mixed numbers can be subtracted directly, and the proper fraction parts are subtracted with the rules of subtraction of fractions, the result is the difference of the integer and fraction parts. To show the result as a mixed number, the integer part is left alone, and the fraction part is converted to a proper fraction if necessary, this may change the integer part. As with addition, the integer parts are subtracted separately from the fraction parts.

(Multiplicación de números reales)
**Multiplication of real numbers**: multiplication is the operation of multiplying numbers together. Multiplication means the repeated addition of a number with itself, the amount of repeated additions is the other number in the operation.
[Multiplication code](Programs/S03/Multiplication.py)

Multiplication is the inverse operation of division. Given that multiplication means the repeated addition of the first number with itself a number of times equal to the second number, this means that no matter which number comes first and which second, the final repeated addition is the same.

In a multiplication operation, if the amount of repeated additions is negative, then this means repeated addition with each addition done in the opposite direction. For example, $4 \cdot -3 = -4 -4 -4$, each addition is done in the opposite direction of $4$, and in $-4 \cdot -3 = 4 + 4 + 4$, each addition is done in the opposite direction of $-4$.

(Operador multiplicación)
**Multiplication operator**: this operator is $\times$, the times sign. Another is $\cdot$, the dot sign. Another is $()$, the parentheses signs.

(Notación de la multiplicación)
**Multiplication notation**: the multiplication of $a$ and $b$ is $ab = c$, read as $a$ times $b$ ($a$ veces $b$), $a$, $b$ are called the factors (factores), the result $c$ is called the product (producto).

> The multiplication of $a$ and $b$ is $c$
> $$ab = c$$
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
> $$ab = ba$$

(Propiedad asociativa de la multiplicación)
**Associative property of multiplication**: using grouping symbols to group multiplication operations does not change the product.

> Associative property of multiplication
>
> Let $a$, $b$, $c$ be numbers, then
> $$abc = (ab) c = a (bc)$$

(Propiedad distributiva de la multiplicación respecto a la suma)
**Distributive property of multiplication over addition**: a real number multiplying the sum of other real numbers, is equal to the sum of the products of the real number by each of the other real numbers.

> Distributive property
>
> Let $a$, $b$, $c$ be real numbers, then
> $$a (b + c) = ab + ac$$

This property shows itself when multiplying $a$ by the sum $b + c$, the resulting product can be seen as the sum of $a b$ and $a c$. This property actually includes subtraction as a case of the sum, given that the addends can be negative numbers.

(Inverso multiplicativo)
**Multiplicative inverse**: the reciprocal of a number, is its multiplicative inverse. The multiplicative inverse of a number $a$ is $\frac{1}{a}$.

(Propiedad inversa de la multiplicación)
**Inverse property of multiplication**: the product of a number and its multiplicative inverse is one.

> Inverse property of multiplication
>
> Let $a$ be a number, then
> $$a \frac{1}{a} = 1$$

(Multiplicación por -1)
**Multiplication by -1**: a number multiplied by $-1$ results in its opposite.

> Multiply a number by $-1$
>
> Let $a$ be a number, then
> $$-1 \cdot a = -a$$

Using the definition of multiplication, multiplying $a$ by $-1$ is the same as adding $a$ one time in its opposite direction, which is $-a$, the opposite of $a$.

(Multiplicación por 0)
**Multiplication by 0**: the product of any number and 0 is 0.

> Multiply a number by 0
>
> Let $a$ be a number, then
> $$a \cdot 0 = 0$$

This is because $a$ is added $0$ times with itself.

(Multiplicación de fracciones)
**Fraction multiplication**: the product of two fractions is the product of the numerators over the product of the denominators, $\frac{a}{b} \frac{c}{d} = \frac{a c}{b d}$, this implies two operations, first the multiplication by $c$ and then the division by $d$. Given the PEMDAS order of operations, it's the same if the division by $d$ is done first.

(División de números reales)
**Division of real numbers**: division is the operation of dividing a first number by a second number. Division means the repeated subtraction of the second number from the first number until reaching 0, the amount of repeated subtractions is the result of the operation.
[Division code](Programs/S03/Division.py)

Division is the inverse operation of Multiplication.

Division means repeated subtraction until reaching 0, if the amount of repeated subtractions is negative, then this means repeated subtraction with each subtraction done in the opposite direction. For example, $24 \div -8 = -3$ so the number $-8$ is subtracted $-3$ times from $24$, i.e. $-8$ is subtracted three times in its opposite direction to reach 0 starting at 24. In $-24 \div -8 = 3$ the amount of repeated subtractions is positive, so $-8$ is subtracted directly from $-24$ three times to reach 0.

Division is not commutative.

> Non commutativity of division
>
> Let $a$, $b$ be numbers,
>
> $$\begin{gathered}
> if\ a \ne b\\
> then\ \frac{a}{b} \ne \frac{b}{a}
> \end{gathered}$$

(Operador división)
**Division operator**: this operator is $\div$, the division sign. Another is $/$, the slash sign. Another is $\text{---}$, the horizontal line sign.

(Notación de la división)
**Division notation**: the division of $b$ over $a$ is $\frac{b}{a} = c$, read as $b$ divided by $a$ ($b$ dividido $a$), $b$ is called the dividend (dividendo), $a$ is called the divisor (divisor), the result $c$ is called the quotient (cociente).

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
**Division property of quotient one**: any nonzero number divided by itself gives a quotient of 1.

> Division property of quotient one
>
> Let $a$ be a number, then
> $$\frac{a}{a} = 1$$

(Propiedades del cero en la división)
**Division properties of zero**: zero divided by any nonzero number is zero. Division by zero is undefined.

> Zero divided by a nonzero number
>
> Let $a$ be a real number, then
> $$\frac{0}{a} = 0$$

> Division by zero is undefined
>
> Let $a$ be a real number, then
> $$\frac{a}{0}\ is\ undefined$$

(División por -1)
**Division by -1**: a number divided by $-1$ results in its opposite.

> Divide a number by $-1$
>
> Let $a$ be a number, then
> $$a \div -1 = -a$$

Using the definition of division, dividing $a$ by $-1$ is the same as subtracting $-1$ from $a$ until reaching 0, which is $-a$ times, the opposite of $a$.

(Recíproco de un número)
**Reciprocal of a number**: given a number, its reciprocal is another number such that when multipled together the product is 1. In $\frac{a}{b}$, the reciprocal is $\frac{b}{a}$, because $\frac{a}{b} \frac{b}{a} = \frac{a b}{b a} = 1$, and so $a \ne 0$, $b \ne 0$, which means that 0 doesn't have a reciprocal.

Non fraction numbers also have a reciprocal, the reciprocal of $a$ is $\frac{1}{a}$ because $a \frac{1}{a} = 1$. Using the definition of division, $\frac{1}{a}$ means taking the number $1$ and dividing it into $a$ groups, then $\frac{1}{a}$ is the size of each group, which is the same as the place where the first group ends, this place is the definition of the reciprocal of $a$.

(Invertir un número)
**Invert a number**: the process of finding the reciprocal of a number. When a number is inverted the result is its reciprocal.

(División de fracciones)
**Fraction division**: the operation $\frac{a}{b} \div \frac{c}{d}$. This implies two operations, division by $c$ and division by the reciprocal of $d$ which is the same as multiplication by $d$, so $\frac{a}{b} \div \frac{c}{d} = \frac{ad}{bc}$.

(Residuo | Resto)
**Remainder**: in division, this is the number that is left over after doing the repeated subtraction, if any.
[Remainder code](Programs/S03/Remainder.py)

> Division with quotient and remainder
>
> Let $a$, $b$ be numbers with $b$ being nonzero, let $q$ be the quotient, $r$ be the remainder, then
> $$\frac{a}{b} = q + \frac{r}{b}$$

(Paradigma de la multiplicación y división)
**Multiplication and division paradigm**: when multiplying or dividing by a negative number, it changes the sign of the other number, so multiplying or dividing a negative number by another negative number results in a positive number, and multiplying or dividing a positive number by a negative number results in a negative number.

Multiplication and division both deal with three concepts: a set of elements, groups of elements, and the size of said groups. Each of this concepts is associated with a number, the total number of elements, the amount of groups, and the size of each group.

Multiplication returns the total number of elements as the product of the amount of groups by the size of each group. For example, $5$ groups of size $4$, have a total number of elements of $5 \cdot 4 = 20$, and $4$ groups each with $5$ elements, have a total number of elements of $4 \cdot 5 = 20$. By itself, the total number of elements remains the same, $20$.

In multiplication, the amount of groups is interchangeable with the size of each group, so a multiplication can be interpreted as the amount of groups times their size, or as the size of the groups times the amount of groups, both interpretations are valid for any single multiplication.

Division has a similar behavior, the total number of elements is the dividend, but then, the divisor can be any of the other two numbers. The divisor can be the amount of groups, or the size of each group, and the quotient is the other number. For example, $24 \div 8 = 3$ means, from the $24$ total elements, with groups of size $8$, then there are $3$ groups, but $24 \div 8 = 3$ also means that from the $24$ total elements, with $8$ groups, each will have a size of $3$. Both conclusions are arrived via repeated subtraction.

The interpretation of $24 \div 8 = 3$ as $24$ elements divided in $8$ groups have a group size of $3$, means that there are $3$ elements per each $1$ group, so $24 \div 8 = 3 \div 1$, in words it could be read as, there are $24$ elements each $8$ groups, or there are $3$ elements each $1$ group.

Multiplication by a number is the same as division by its reciprocal, $ab = a \div \frac{1}{b}$, because it follows the definition of division as repeated subtraction. Starting from $a$, to reach 0 by subtracting $\frac{1}{b}$, it must be done $a b$ times, this is because to reach 0 by subtracting $1$ it is done $a$ times, $\frac{a}{1} = a$, and to do it by subtracting $\frac{1}{b}$, it must be done $b$ times as much.

Division by a number is the same as multiplication by its reciprocal, $\frac{a}{b} = a \frac{1}{b}$, because having $a$ elements divided in $b$ groups, has each group with size $\frac{a}{b}$, and adding $a$ with itself only a fraction $\frac{1}{b}$ times, ends being at the same place of $\frac{a}{b}$.

(Multiplicación y división por 10)
**Multiplication and division by 10**: given that 10 is the base of the decimal place value system, multiplying a number by 10 moves the number one digit to the left, while dividing a number by 10 moves the number one digit to the right. For example, $2 \cdot 10 = 20$, and $2 \div 10 = 0.2$.

(Multiplicación y división de decimales)
**Multiplication and division of decimals**: like regular multiplication and division. When doing division, an infinite amount of decimal digits can appear. When doing multiplication, the amount of decimal digits is up to the sum of the decimal digits in the factors.

(Potenciación)
**Exponentiation**: the operation of raising a number to a given power, e.g. $a^n$.
[Exponentiation code](Programs/S03/Exponentiation.py)

(Notación exponencial)
**Exponential notation**: used in expressions where a number is multiplied by itself several times, for example, $2 \cdot 2 \cdot 2 \cdot 2$ is written as $2^4$.

> General exponential notation
>
> Let $a$ be a number, $n$ be a whole number, then
> $$aaa \ldots a = a^n$$
> The value $n$ is the amount of times that $a$ is multiplied by itself.

Using the shown symbols, the exponential notation is read as $a$ to the $n$-th power ($a$ a la $n$-ésima potencia), also read as $a$ to the power of $n$ ($a$ a la $n$).

The operation itself is read as raise $a$ to the $n$-th power (elevar $a$ a la $n$-ésima potencia), also read as raise $a$ to the power of $n$ (elevar $a$ a la $n$).

(Base y exponente)
**Base and exponent**: in the operation $a^n$, $a$ is called the base and $n$ is called the exponent.

(Expresión exponencial en forma expandida)
**Exponential expression in expanded form**: $a^n$ can be represented in expanded form as $a a a \ldots a$ where $a$ is multiplied by itself $n$ times.

(Números al cuadrado)
**Squared numbers**: when a number is raised to the power of 2, it is said that the result is a squared number, e.g. $3$ to the power of $2$ is $9$, or $3$ squared is $9$ ($3$ al cuadrado es $9$).

(Cuadrado perfecto)
**Perfect square**: any whole number that is the square of an integer. For example $9$ is the perfect square of $3$, because $3^2 = 9$ and $\sqrt{9} = 3$.

(Números al cubo)
**Cubed numbers**: when a number is raised to the power of 3, it is said that the result is a cubed number, e.g. $5$ to the power of $3$ is $125$, or $5$ cubed is $125$ ($5$ al cubo es $125$).

(Radicación de números)
**Taking a root of a number**: the exponentiation operation using as exponent the reciprocal of an integer, e.g. $a^{1/7}$ in which the exponent is the reciprocal of $7$, this is read as taking the seventh root of $a$ (sacar la raíz séptima de $a$).

(Signo de radical)
**Radical sign**: The symbol around $n$ in $\sqrt{n}$ is the radical sign, it acts as a grouping symbol for the expression inside it. $\sqrt{n} = n^{1/2}$, and $\sqrt[7]{n} = n^{1/7}$, in general $\sqrt[k]{n} = n^{1/k}$.

(Raíz cuadrada)
**Square root**: given two numbers $m$, $n$, such that $m = n^2$, then $n$ is the square root of $m$, $n = \sqrt{m}$. Squared numbers can be seen as squares in a 2D grid. Let $m$ be the area of a given square, then $n$ is the measure of its side's length.

(Raíz cuadrada principal)
**Principal square root**: since any square root can be negative or positive, because $n^2 = (-n)^2 = m$, so both $n$ and $-n$ are roots of $m$, only one is chosen as the square root of $m$, this is the positive value $n$, named the principal square root of $m$, $\sqrt{m}$ stands for $n$.

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

(Orden de las operaciones)
**Order of operations**: The order in which to execute the operations. In $5 + \frac{10}{2}$, the result is $10$ if division is done first, but the result is $7.5$ if addition is done first. This can be modified with grouping symbols.
[Order of operations code](Programs/S03/Order_of_operations.py)

(Signos de agrupación)
**Grouping symbols**: symbols that act as operators by grouping algebraic symbols. The grouped symbols are operated together. The grouping symbols serve to make explicit the order of operations.

(Paréntesis)
**Parentheses**: this operator is $()$, the parentheses signs. $8(14 - 8)$ returns $48$.

(Corchetes)
**Brackets**: this operator is $[]$, the brackets signs. $21 - 3[2 + 4(9 - 8)]$ returns $3$.

(Llaves)
**Braces**: this operator is $\{\}$, the braces signs. $24 \div \{13 - 2[(6 - 5) + 4]\}$ returns $8$.

(PEMDAS)
**PEMDAS**: acronym of Parentheses, Exponentiation, Multiplication, Division, Addition, and Subtraction. This dictates the standard order of operations when there are no parentheses, or grouping symbols in general. Multiplication and division have the same relevance, so they can be switched in order, same with addition and subtraction.

(Redondeo)
**Rounding**: approximating a number with another of less significant digits.
[Rounding code](Programs/S03/Rounding.py)

(Función techo)
**Ceiling function**: a function that approximates a number to the nearest bigger integer. Denoted as $\lceil x \rceil$, where $x$ is the number being rounded, e.g. $\lceil 2.5 \rceil = 3$, $\lceil -2.5 \rceil = -2$.

(Función piso)
**Floor function**: a function that approximates a number to the nearest smaller integer. Denoted as $\lfloor x \rfloor$, where $x$ is the number being rounded, e.g. $\lfloor 2.5 \rfloor = 2$, $\lfloor -2.5 \rfloor = -3$.

(Truncamiento)
**Truncation**: rounding a number by removing all digits after the decimal point, e.g. $2.5$ truncated is $2$, and $-2.5$ truncated is $-2$.

(Reducir fracciones)
**Reduce fractions**: form of simplification in which a fraction is expressed as an equivalent fraction that has no common factors between the numerator and the denominator. If there is a common factor, both the numerator and the denominator are divided by it, this simplifies the fraction.

For example $\frac{6}{9} = \frac{4}{6}$, but their reduced form is $\frac{2}{3}$. In $\frac{6}{9}$ a common factor is $3$ and dividing the numerator and denominator by $3$ results in $\frac{2}{3}$. In $\frac{4}{6}$ a common factor is $2$ and dividing the numerator and denominator by $2$ results in $\frac{2}{3}$.

The same simplification can be done with variables, e.g. $\frac{2 x}{x}$ can be simplified to $\frac{2}{1}$ or $2$.

(Fracción irreducible)
**Simplified fraction**: a fraction in which the numerator and the denominator have no common factors.

(Eliminar los denominadores de una ecuación)
**Clear an equation of fractions**: the process of clearing the fractions of an equation, by multiplying each term on both sides by the least common denominator.

(Racionalizar el denominador)
**Rationalize the denominator**: when a fraction has a radical in the denominator, it can be rationalized to remove the radical from the denominator without changing the value of the fraction. The process is $\frac{a}{\sqrt{b}} = \frac{a \sqrt{b}}{\sqrt{b} \sqrt{b}} = \frac{a \sqrt{b}}{b}$.

(Conversión entre decimales y fracciones)
**Conversion between decimals and fractions**: decimals can be presented in fraction form, and vice versa. The conversion from fraction to decimal is done by performing the division of the numerator over the denominator of the fraction. The conversion from finite decimal (see finite decimals in this file) to fraction is done by multiplying the decimal by 10 to the positive power of the place of the rightmost digit, and dividing the result over the same power of 10.
[Conversion decimal fraction code](Programs/S05/Conversion_decimal_fraction.py)

(Conversión de decimal periódico a fracción)
**Conversion from repeating decimal to fraction**: The conversion from repeating decimal to fraction is done by creating two numbers, each of which is the product of the decimal by a different power of 10, and then subtracting both numbers and dividing that difference by the subtraction of said powers of 10 (See Programs/Ch05/S03_01_Repeating_decimals.py).

Repeating decimals have a few parts, for example, in the number $894.57448132653448132653448132653448132653448132653$, the unique part (parte única) is $894.57$, and the repeating part (parte periódica) is $448132653$. In itself, the unique part has two parts (as any decimal number), the decimal part and the integer part.

For the unique part $894.57$, the original number is multiplied by 10 to the positive power of the place of the rightmost digit of the unique part, in this case $10^2$. For the repeating part, the original number is multiplied by 10 to the power of the sum of the amount of repeating digits and the power of 10 used for the unique part (in this case $2$). The amount of digits in $448132653$ is $9$, so for the repeating part, the original number is multiplied by $10^{9 + 2} = 10^{11}$.

Now to subtract these two products, let $a = 894.57448132653448132653448132653448132653448132653$, so $a 10^2 = 89457.448132653448132653448132653448132653448132653$, and $a 10^{11} = 89457448132653.448132653448132653448132653448132653448132653$, therefore $a 10^{11} - a 10^2 = 89457448043196$, as can be seen, this subtraction results in an integer. Continuing, $a 10^{11} - a 10^2 = a (10^{11} - 10^2)$, so $a = \frac{89457448043196}{(10^{11} - 10^2)} = \frac{89457448043196}{99999999900}$.

(Conversión entre porcentajes y decimales, y entre porcentajes y fracciones)
**Conversion between percents and decimals, and between percents and fractions**: the conversion from percent to fraction and decimal uses the definition of percent. Given that a percent is a ratio with denominator 100, the fraction is the percent number over 100, and the decimal is the result of the division of said fraction. For example, $54\%$ as a fraction is $\frac{54}{100}$, and as a decimal is $0.54$.

The conversion from decimal or fraction to percent is based on equivalent fractions. The decimal is converted to a fraction, and the fraction is converted to an equivalent fraction with a denominator of 100. For example the decimal $0.6$ as a fraction is $\frac{6}{10} = \frac{3}{5}$, and then as an equivalent fraction $\frac{3}{5} = \frac{3 \cdot 20}{5 \cdot 20} = \frac{60}{100} = 60\%$.

A decimal can be converted directly to a percent, by multiplying it for $100$, e.g. $0.6 = 0.6 \cdot 100 \% = 60\%$. The opposite consists in dividing a percent by $100$ to obtain its decimal form.

When handling improper fractions, the resulting percent is greater than $100\%$, for example $\frac{5}{4} = 1.25 = 1.25 \cdot 100\% = 125\%$.

Simplification of square roots is done like regular simplification.
[Simplification of radicals code](Programs/S05/Simplification_of_radicals.py)