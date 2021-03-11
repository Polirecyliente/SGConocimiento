
#   Algebra definitions (Definiciones de álgebra)

<!--
#T# Table of contents

#C# The language of algebra (El lenguaje del álgebra)
#C# Evaluation and simplification of expressions (Evaluación y simplificación de expresiones)
#C# Solution of an equation, subtraction and addition properties of equality (Soluciones de una ecuación, propiedades de sustracción y adición de la igualdad)
#C# Multiples, divisibility, factors, prime numbers (Múltiplos, divisibilidad, factores, número primos)
#C# Prime factorization, least common multiple (Descomposición en factores primos, mínimo común múltiplo)

#T# Beginning of content
-->

## The language of algebra (El lenguaje del álgebra)

(Variables)
**Variables**: the representation of quantities that can vary, written using letters of the alphabet, such as $a, b, c, x, y, z$.

(Constantes)
**Constants**: the representation of quantities that can not vary, that stay always with the same value, written using letters of the alphabet, such as $m, n$.

The use of a letter of the alphabet as a variable or as a constant is determined from the context, so the context must state which letters are variables and which are constants.

(Funciones)
**Functions**: an operation or set of operations done over a number or numbers, that returns a result. Operators (Operadores) act as functions, e.g. $a + b$ can be written as $sum(a,b)$, where the function $sum$ returns the sum of $a$, $b$.

(Símbolos y signos algebraicos)
**Algebraic symbols and signs**: numbers, variables, constants, operators, functions.

(Símbolos algebraicos)
**Algebraic symbols**: constants or variables.

(Subíndice de un símbolo)
**Subscript of a symbol | subindex of a symbol**: a small number (or another symbol) written at the bottom front of a symbol, to differentiate between related symbols. For example $(x_1, y_1)$ and $(x_2, y_2)$ represent two different points in the $x$-$y$ plane.

The subindex of a symbol can also be a variable itself, for example $x_j$ where the subindex $j$ may vary. When not specified, the variable $j$ is a counting number with a maximum value, meaning that the minimum value of $j$ is $1$, and the maximum value is a given constant $n$.

In cases of symbols that have the same subindex but need to represent different values of the subindex, a number can be appended to the subindex, for example $x_{j1}$ and $x_{j2}$ represent the same symbol $x_j$, but with two distinct values of the subindex $j$.

(Enunciado matemático)
**Math statement**: any math writing that can be read as a statement, with symbols, signs, numbers, operators, etcetera, e.g. math expressions, equations, inequalities, and other.

(Expresión matemática)
**Math expression**: a math statement of numbers, symbols, and operations together.

> Example of a mathematical expression
> $$a (b + c) - d$$

(Expresiones y ecuaciones)
**Expressions and equations**: two expressions can form an equation by connecting them with an equal sign.

> Two expressions connected with an equal sign form an equation
> $$a + b = \frac{c}{d}$$

(Definición matemática)
**Math definition**: an equation in which a symbol is defined.

> Definition notation
>
> Let $a$, $b$ be symbols, then
> $$a := b$$
> This is read as $a$ is defined as $b$ ($a$ es definido como $b$).

The sign $:=$ is used to make definitions, to differentiate it from the equal sign.

(Fórmula matemática)
**Math formula**: an equation whose purpose is to find the value of a quantity or variable, i.e. formulas are equations expressly intended to find the value of a quantity, they are the "formula" to find said value, e.g. in $x = vt$ the distance $x$ is calculated as the product of velocity $v$ and time $t$.

(Simplificación)
**Simplification**: do all possible operations in an expression. $4 \cdot 2 + 1$ can be simplified to $9$. Symbols of rational numbers are left as is, for example $\sqrt{\pi}$ should not be simplified further.
[Simplification code](Programs/S01/Simplification.py)

## Evaluation and simplification of expressions (Evaluación y simplificación de expresiones)

(Evaluar una expresión)
**Evaluate an expression**: this means substitute symbols for specific values and calculate the result, e.g. in $x + 7$ substitute $x$ for $4$ and calculate, $4 + 7 = 11$. Expressions without symbols are ready to be evaluated.
[Evaluation code](Programs/S01/Evaluation.py)

(Expresión algebraica)
**Algebraic expression**: an expression that uses symbols, it may or may not represent constant values as symbols too, e.g. $x + 7$ or $x + a$.

(Términos algebraicos)
**Algebraic terms**: each of the parts of an algebraic expression separated by a plus or minus, so numbers and symbols multiplied together count as a term, e.g. in $3a + 7 + x^2$ there are three terms, $3a$, $7$, and $x^2$.

(Coeficiente)
**Coefficient**: the numeric constant that multiplies the variable(s) in a term. If a term has no variables then the coefficient is the term itself. If a variable has no numeric constant then the implied coefficient is 1. For example, in $3a + 7 + x^2$, the coefficients are $3$, $7$, and $1$, respectively.

(Términos semejantes)
**Like terms**: terms that can be added together directly, like terms can only differ from each other in the coefficient, so their symbol(s) (variable or constant) has to be the same, e.g. $3x$ and $4x$ are like terms, they may be added (or subtracted) directly.

(Reducción de términos semejantes)
**Combining like terms | Combine like terms**: simplification in which like terms are combined, i.e. they are added together according to their sign, e.g. $3x + 4x$ can be combined as $7x$, $3x - 4x$ can be combined as $-x$.

## Solution of an equation, subtraction and addition properties of equality (Soluciones de una ecuación, propiedades de sustracción y adición de la igualdad)

(Solución de una ecuación)
**Solution of an equation**: an equation that contains a variable can be solved by determining the value of the variable that makes the equation true, e.g. in $x + 7 = 11$, $x$ must be $4$ so that the equation is true, and $4$ is the solution of the equation.
[Solution of an equation code](Programs/S01/Solution_of_an_equation.py)

An equation with several variables has solution tuples, e.g. an equation with three variables, $x$, $y$, and $z$, has solution tuples of size three, such as $(4, 3, 8)$.

(Propiedad reflexiva de la igualdad)
**Reflexive property of equality**: a real number is equal to itself, Let $a$ be a real number, then $a = a$.

(Propiedad simétrica de la igualdad)
**Symmetric property of equality**: if a first real number is equal to a second, then the second number is equal to the first. Let $a$, $b$ be real numbers, then $a = b \leftrightarrow b = a$.

(Propiedad transitiva de la igualdad)
**Transitive property of equality**: if a first real number is equal to a second, and the second number is equal to a third, then the third number is equal to the first. Let $a$, $b$, $c$ be real numbers, if $a = b$ and $b = c$ then $a = c$.

(Propiedad de sustitución de la igualdad)
**Substitution property of equality**: if two real numbers are equal, one can be substituted by the other. Let $a$, $b$ be real numbers, if $a = b$ then $b$ can substitute $a$ and vice versa.

(Propiedad aditiva de la igualdad)
**Addition property of equality**: adding a real number to both sides of an equality, preserves the equality.

> Addition property of equality
>
> Let $a$, $b$, $c$ be real numbers
>
> $$\begin{gathered}
> if\ a = b\\
> then\ a + c = b + c
> \end{gathered}$$

(Propiedad sustractiva de la igualdad)
**Subtraction property of equality**: subtracting a real number from both sides of an equality, preserves the equality.

> Subtraction property of equality
>
> Let $a$, $b$, $c$ be real numbers
>
> $$\begin{gathered}
> if\ a = b\\
> then\ a - c = b - c
> \end{gathered}$$

Note, in spanish this property may be bundled as part of the addition property of equality, since changing the sign of $c$ shows both properties.

(Propiedad multiplicativa de la igualdad)
**Multiplication property of equality**: multiplying a real number to both sides of an equality, preserves the equality.

> Multiplication property of equality
>
> Let $a$, $b$, $c$ be real numbers
>
> $$\begin{gathered}
> if\ a = b\\
> then\ ac = bc
> \end{gathered}$$

(Propiedad divisiva de la igualdad)
**Division property of equality**: dividing both sides of an equality by a nonzero real number, preserves the equality.

> Division property of equality
>
> Let $a$, $b$, $c$ be real numbers, with $c$ being nonzero
>
> $$\begin{gathered}
> if\ a = b\\
> then\ \frac{a}{c} = \frac{b}{c}
> \end{gathered}$$

(Despejar una variable)
**Isolate a variable**: using properties of equality (such as the ones from addition and subtraction, but also from multiplication and division), to make a variable stand alone in one side of an equation.

> Isolating a variable using the properties of equality
>
> Let $a$, $b$, $c$, $d$ be numbers, and let
> $$a + b = c + d$$
> Isolate $a$ using the subtraction property of equality, by subtracting $b$ from each side.
> $$a = c + d - b$$

For example, $4 + y/2 = x + 1 \Rightarrow y = 2x - 6$, here the variable $y$ is isolated.

Isolating a variable in an equation can be synonymous with solving said equation for the variable isolated.

(Solucionar ecuaciones)
**Solve equations**: Solving an equation commonly means isolating a variable to find its value.

The addition property of equality is used to solve equations when there is a negative term which subtracts from the variable, then said term is added to both sides of the equality, helping in isolating the variable.

The subtraction property of equality is used to solve equations when there is a positive term added to the variable, then said term is subtracted from both sides of the equality, helping in isolating the variable.

The multiplication property of equality is used to solve equations when there is a number dividing the variable, then said number is multiplied to both sided of the equality, helping in isolating the variable.

The division property of equality is used to solve equations when there is a factor multiplying the variable, then both sides of the equality are divided by said factor, helping in isolating the variable.

(Ecuación en dos variables)
**Equation in two variables**: an equation that has two variables. Setting the value of one of the variables allows finding the value of the other.

(Símbolo de sumatoria)
**Summation symbol**: the symbol $\sum_i$ represents the sum of the elements of the set to which $i$ belongs, e.g. $\sum_{i = 1}^{n}{x_i} = x_1 + x_2 + ... + x_n$, where $1, 2, ..., n$ is the set of values of $i$ over which the summation is done.