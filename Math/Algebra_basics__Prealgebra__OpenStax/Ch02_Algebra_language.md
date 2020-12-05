
#   Algebra language

## The language of algebra
[Ch02_S01](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=109)

(Variables)
**Variables**: the representation of quantities that can vary, written using letters of the alphabet, such as $a, b, c, x, y, z$.

(Constantes)
**Constants**: the representation of quantities that can not vary, that stay always with the same value, written using letters of the alphabet, such as $m, n$.

(Funciones)
**Functions**: an operation or set of operations done over a number or numbers, that returns a result. Operators act as functions, $a + b$ can be written as $sum(a,b)$, where the function $sum$ returns the sum of $a, b$.

(Símbolos algebraicos)
**Algebraic symbols**: operators, functions, variables, numbers.

(Operadores relacionales)
**Relational operators**: operators that compare the values of two quantities.
[Relational operators code](Programs/Ch02/S01_01_Relational_operators.py)

(Igualdad)
**Equality**: when the values of two quantities are equal, $a = b$ means the value of $a$ is equal to the value of $b$.

(Desigualdad)
**Inequality**: when the values of two quantities are not equal, or may not be equal.

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
**PEMDAS**: acronym of Parentheses, Exponentiation, Multiplication, Division, Addition, and Subtraction. This dictates the standard order of operations when there are no parentheses, or grouping symbols in general.

(Expresiones y ecuaciones)
**Expressions and equations**: two expressions can form an equation by connecting them with an equal sign, $a + b = c/d$.

(Simplificación)
**Simplification**: do all possible operations in an expression. $4 \cdot 2 + 1$ can be simplified to $9$.
[Simplification code](Programs/Ch02/S01_03_Simplification.py)

(Notación exponencial)
**Exponential notation**: used in expressions where a number is multiplied by itself several times, $2 \cdot 2 \cdot 2 \cdot 2$ is written as $2^4$, $a \cdot a \cdot a \cdot \ldots \cdot a = a^n$ where $n$ is the amount of times that $a$ is multiplied by itself, read as $a$ to the $n$-th power ($a$ a la $n$-ésima potencia), also read as $a$ to the power of $n$ ($a$ a la $n$). The operation itself is read as raise $a$ to the $n$-th power (elevar $a$ a la $n$-ésima potencia), also read as raise $a$ to the power of $n$ (elevar $a$ a la $n$).

(Potenciación)
**Exponentiation**: the operation of raising a number to a given power, i.e. $a^n$.
[Exponentiation code](Programs/Ch02/S01_04_Exponentiation.py)

(Base y exponente)
**Base and exponent**: in the operation $a^n$, $a$ is called the base, $n$ is called the exponent.

(Expresión exponencial en forma expandida)
**Exponential expression in expanded form**: $a^n$ can be represented in expanded form as $a * a * a * ... * a$ where $a$ is multiplied by itself $n$ times.

(Números al cuadrado)
**Squared numbers**: when a number is raised to the power of 2, it is said that the result is a squared number, e.g. 3 to the power of 2 is 9, or 3 squared is 9 (3 al cuadrado es 9).

(Números al cubo)
**Cubed numbers**: when a number is raised to the power of 3, it is said that the result is a cubed number, e.g. 5 to the power of 3 is 125, or 5 cubed is 125 (5 al cubo es 125).

## Evaluation and simplification of expressions
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

## Subtraction and addition properties of equality
[Ch02_S03](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=144)

<!-- # TODO  -->

## Multiples, factors
[Ch02_S04](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=158)



## Prime factorization, least common multiple
[Ch02_S05](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=172)

