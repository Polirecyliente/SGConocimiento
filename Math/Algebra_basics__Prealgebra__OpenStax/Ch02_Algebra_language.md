
#   Algebra language (Lenguaje del álgebra)

## The language of algebra (El lenguaje del álgebra)
[Ch02_S01](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=109)

(Variables)
**Variables**: the representation of quantities that can vary, written using letters of the alphabet, such as $a, b, c, x, y, z$.

(Constantes)
**Constants**: the representation of quantities that can not vary, that stay always with the same value, written using letters of the alphabet, such as $m, n$.

The use of a letter of the alphabet as a variable or as a constant is determined from the context, so the context must state which letters are variables and which are constants.

(Funciones)
**Functions**: an operation or set of operations done over a number or numbers, that returns a result. Operators act as functions, e.g. $a + b$ can be written as $sum(a,b)$, where the function $sum$ returns the sum of $a, b$.

(Símbolos algebraicos)
**Algebraic symbols**: operators, functions, variables, numbers.

(Operadores relacionales)
**Relational operators**: operators that compare the values of two numbers. These operators serve to make the set of numbers an ordered set, ordered according to the values of the numbers.
[Relational operators code](Programs/Ch02/S01_01_Relational_operators.py)

(Igualdad)
**Equality**: when the values of two quantities are equal, $a = b$ means the value of $a$ is equal to the value of $b$.

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

(Orden de las operaciones)
**Order of operations**: The order in which to execute the operations. In $5 + 10/2$, the result is $10$ if division is done first, but the result is $7.5$ if addition is done first. This can be modified with grouping symbols.
[Order of operations code](Programs/Ch02/S01_02_Order_of_operations.py)

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

(Expresiones y ecuaciones)
**Expressions and equations**: two expressions can form an equation by connecting them with an equal sign, $a + b = c/d$.

(Simplificación)
**Simplification**: do all possible operations in an expression. $4 \cdot 2 + 1$ can be simplified to $9$.
[Simplification code](Programs/Ch02/S01_03_Simplification.py)

(Notación exponencial)
**Exponential notation**: used in expressions where a number is multiplied by itself several times, $2 \cdot 2 \cdot 2 \cdot 2$ is written as $2^4$, $a \cdot a \cdot a \cdot \ldots \cdot a = a^n$ where $n$ is the amount of times that $a$ is multiplied by itself, read as $a$ to the $n$-th power ($a$ a la $n$-ésima potencia), also read as $a$ to the power of $n$ ($a$ a la $n$).

The operation itself is read as raise $a$ to the $n$-th power (elevar $a$ a la $n$-ésima potencia), also read as raise $a$ to the power of $n$ (elevar $a$ a la $n$).

(Potenciación)
**Exponentiation**: the operation of raising a number to a given power, e.g. $a^n$.
[Exponentiation code](Programs/Ch02/S01_04_Exponentiation.py)

(Base y exponente)
**Base and exponent**: in the operation $a^n$, $a$ is called the base, $n$ is called the exponent.

(Expresión exponencial en forma expandida)
**Exponential expression in expanded form**: $a^n$ can be represented in expanded form as $a \cdot a \cdot a \cdot ... \cdot a$ where $a$ is multiplied by itself $n$ times.

(Números al cuadrado)
**Squared numbers**: when a number is raised to the power of 2, it is said that the result is a squared number, e.g. $3$ to the power of $2$ is $9$, or $3$ squared is $9$ ($3$ al cuadrado es $9$).

(Números al cubo)
**Cubed numbers**: when a number is raised to the power of 3, it is said that the result is a cubed number, e.g. $5$ to the power of $3$ is $125$, or $5$ cubed is $125$ ($5$ al cubo es $125$).

## Evaluation and simplification of expressions (Evaluación y simplificación de expresiones)
[Ch02_S02](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=129)

(Evaluar una expresión)
**Evaluate an expression**: this means substitute symbols for specific values and calculate the result, e.g. in $x + 7$ substitute $x$ for $4$ and calculate, $4 + 7 = 11$. Expressions without symbols are ready to be evaluated.
[Evaluation code](Programs/Ch02/S02_01_Evaluation.py)

(Expresión algebraica)
**Algebraic expression**: an expression that uses symbols, it may or may not represent constant values as symbols too, e.g. $x + 7$ or $x + a$.

(Términos algebraicos)
**Algebraic terms**: each of the parts of an algebraic expression separated by a plus or minus, so numbers and symbols multiplied together count as a term, e.g. in $3a + 7 + x^2$ there are three terms, $3a$, $7$, and $x^2$.

(Coeficiente)
**Coefficient**: the numeric constant that multiplies the variable(s) in a term. If a term has no variables then the coefficient is the term itself. If a variable has no numeric constant then the implied coefficient is 1. For example, in $3a + 7 + x^2$, the coefficients are $3$, $7$, and $1$, respectively.

(Términos semejantes)
**Like terms**: terms that can be added together directly, like terms can only differ from each other in the coefficient, so their symbol(s) (variable or constant) has to be the same, e.g. $3x$ and $4x$ are like terms, they may be added (or subtracted) directly.

(Reducción de términos semejantes)
**Combining like terms**: simplification in which like terms are combined, i.e. they are added together according to their sign, e.g. $3x + 4x$ can be combined as $7x$, $3x - 4x$ can be combined as $-x$.

## Solution of an equation, subtraction and addition properties of equality (Soluciones de una ecuación, propiedades de sustracción y adición de la igualdad)
[Ch02_S03](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=144)

(Solución de una ecuación)
**Solution of an equation**: an equation that contains a variable can be solved by determining the value of the variable that makes the equation true, e.g. in $x + 7 = 11$, $x$ must be $4$ so that the equation is true, and $4$ is the solution of the equation.
[Solution of an equation code](Programs/Ch02/S03_01_Solution_of_an_equation.py)

(Propiedad sustractiva de la igualdad)
**Subtraction property of equality**: if two numbers $a$ and $b$ are equal, $a = b$, then subtracting a third number $c$ from each side of the equality preserves the equality $a - c = b - c$. Note, in spanish this property may be bundled as part of the addition property of equality, since changing the sign of $c$ shows both properties.

(Propiedad aditiva de la igualdad)
**Addition property of equality**: if two numbers $a$ and $b$ are equal, $a = b$, then adding a third number $c$ to each side of the equality preserves the equality $a + c = b + c$.

(Despejar una variable)
**Isolate a variable**: using properties of equality (such as the ones from addition and subtraction, but also from multiplication and division, see Ch03_Integers.md), to make a variable stand alone in one side of an equation. For example, in $a + b = c + d$, isolating $a$ requires the use of the subtraction property of equality, by subtracting $b$ from each side, $a = c + d - b$.

## Multiples, divisibility, factors, prime numbers (Múltiplos, divisibilidad, factores, número primos)
[Ch02_S04](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=158)

(Múltiplos de un número)
**Multiples of a number**: the result of multiplying a number by any of the counting numbers, so a number has infinite multiples. The smallest value multiple is the number itself.

(Divisibilidad)
**Divisibility**: if a given number $b$ is multiple of another number $a$, then $b$ is divisible by $a$, because $b/a$ returns a whole number. All the multiples of $a$ are divisible by $a$.
[Divisibility code](Programs/Ch02/S04_01_Divisibility.py)

(Números pares)
**Even numbers**: 0 and the multiples of 2

(Números impares)
**Odd numbers**: the whole numbers that are not even numbers

(Pruebas de divisibilidad)
**Divisibility tests**: a quick test made to check if a number is divisible by another. The following are the divisibility tests of the first numbers.

A given number is divisible by 2 if its last digit is an even number.
A given number is divisible by 3 if the sum of its digits is divisible by 3.
A given number is divisible by 4 if its last two digits are divisible by 4.
A given number is divisible by 5 if its last digit is 0 or 5.
A given number is divisible by 6 if it's divisible by 2 and 3.
A given number is divisible by 7 if its last digit is doubled and then subtracted from the rest of the number, and the result of that is divisible by 7.
A given number is divisible by 8 if its last three digits are divisible by 8.
A given number is divisible by 9 if the sum of its digits is divisible by 9.
A given number is divisible by 10 if its last digit is 0.
A given number is divisible by 11 if the alternating sum of its digits (i.e. the first digit, minus the second, plus the third, minus the fourth, etc.) is divisible by 11.

(Factores de un número)
**Factors of a number**: in a given number, its factors are the numbers that multiplied together produce the given number. A number can have several different sets of factors, e.g. $12$ has different sets of factors like $3$, $4$, also $2$, $6$, or $2$, $3$, $2$, or others.
[Find factors code](Programs/Ch02/S04_02_Find_factors.py)

(Pares de factores)
**factor pairs**: factors can always be presented in pairs, because at least two numbers are required to be multiplied together in order to produce a given number. In the example of $12 = 2 \cdot 3 \cdot 2$, with factor pairs the equation would be $12 = 2 \cdot 6$ or $12 = 3 \cdot 4$.

(Números primos)
**Prime numbers**: each of the numbers with only 2 different factors, the number 1 and the number itself.

(Números compuestos)
**Composite numbers**: the numbers that are not prime, i.e. the numbers that have at least 3 different factors.

## Prime factorization, least common multiple (Descomposición en factores primos, mínimo común múltiplo)
[Ch02_S05](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=172)

(Factores primos)
**prime factors**: the set of prime numbers that multiplied together produce a given number. Numbers can be represented as the product of prime factors.

(Descomposición en factores primos)
**Prime factorization**: the process of finding the prime factors of a number.
[Prime factorization code](Programs/Ch02/S05_01_Prime_factorization.py)

(Multiplicidad de un factor primo)
**Multiplicity of a prime factor**: the amount of times that a prime factor of a given number is repeated, e.g. in the number $60$ the prime factors are $2$, $2$, $3$, $5$, the number $2$ has a multiplicity of $2$, the number $3$ has a multiplicity of $1$, and the number $5$ has a multiplicity of $1$.

(Múltiplos comunes)
**Common multiples**: the numbers that are multiples of a given set of numbers (at least two)

(Mínimo común múltiplo)
**Least common multiple**: the smallest common multiple of a given set of numbers (at least two)
[Least common multiple code](Programs/Ch02/S05_02_Least_common_multiple.py)

The least common multiple of two numbers can be calculated using their prime factors. The least common multiple of two numbers is the product of all their unique prime factors, each raised to the power of their maximum multiplicity.

For example, to find the least common multiple of $12$ and $18$, the prime factors of $12$ are $2$, $2$, $3$, and the prime factors of $18$ are $2$, $3$, $3$. The least common multiple is $2 \cdot 2 \cdot 3 \cdot 3 = 36$, the number $2$ has a maximum multiplicity of $2$ (in $12$), and $3$ has a maximum multiplicity of $2$ (in $18$).

(Máximo común divisor)
**Greatest common divisor**: the biggest common divisor of a given set of numbers (at least two)
[Greatest common divisor code](Programs/Ch02/S05_03_Greatest_common_divisor.py)

The greatest common divisor of two numbers can be calculated using their prime factors. The greatest common divisor of two numbers is the product of their common prime factors, each raised to the power of their minimum multiplicity.

In this use of the term "divisor", it is also a factor of the set of numbers. That's why sometimes this is also called greatest common factor (Máximo factor común).