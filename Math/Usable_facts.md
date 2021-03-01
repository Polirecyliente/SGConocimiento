
#   Usable facts

<!--
#T# Table of contents

#C# Math definitions (Definiciones de matemática)
#C# --- Numeral systems (Sistemas de numeración)
#C# --- Coordinate systems (Sistemas de coordenadas)
#C# --- Subsets of the real numbers (Subconjuntos de los números reales)
#C# ---| Counting numbers (Números naturales)
#C# ---| Whole numbers (Números naturales y el cero)
#C# ---| Integer numbers (Números enteros)
#C# ---| Rational numbers (Números racionales)
#C# ---| Irrational numbers (Números irracionales)
#C# ---| Real numbers (Números reales)
#C# ---| Transcendental numbers (Números trascendentes)
#C# --- Number approximation (Aproximación de números)
#C# --- Equations and inequalities (Ecuaciones y desigualdades)
#C# --- Operations with real numbers (Operaciones con números reales)
#C# ---| Addition of real numbers (Adición de números reales)
#C# ---| Subtraction of real numbers (Sustracción de números reales)
#C# ---| Multiplication of real numbers (Multiplicación de números reales)
#C# ---| Division of real numbers (División de números reales)
#C# ---| Exponentiation of real numbers (Exponenciación de números reales)
#C# ---| Order of operations (Orden de las operaciones)
#C# --- Properties of real numbers (Propiedades de los números reales)
#C# --- Multiples and factors of integers (Múltiplos y factores de los enteros)
#C# Logic definitions (Definiciones de lógica)
#C# --- Propositional logic (Lógica proposicional)
#C# --- Logic fallacies (Falacias lógicas)
#C# Algebra definitions (Definiciones de álgebra)
#C# --- Algebra theorems (Teoremas de álgebra)
#C# --- Linear equations (Ecuaciones lineales)
#C# --- Polynomials (Polinomios)
#C# ---| Operations with polynomials (Operaciones con polinomios)
#C# Geometry definitions (Definiciones de geometría)
#C# --- Geometry postulates (Postulados de geometría)
#C# --- Geometry theorems (Teoremas de geometría)
#C# --- Shapes with their parts and formulas (Formas con sus partes y fórmulas)
#C# Probability definitions (Definiciones de probabilidad)
#C# --- Measures of central tendency (Medidas de tendencia central)
#C# Simplifications (Simplificaciones)
#C# Science and engineering definitions (Definiciones de ciencia e ingeniería)
#C# --- Science and engineering formulas (Fórmulas de ciencia e ingeniería)
#C# --- Science and engineering procedure definitions (Definiciones de procedimientos de ciencia e ingeniería)

#T# Beginning of content
-->

## Math definitions (Definiciones de matemática)

(Axioma)
**Axiom**: facts of math that are accepted as true without proof.

(Teorema)
**Theorem**: a statement that can be proved with postulates, axioms and/or with other theorems.

(Corolario)
**Corollary**: a theorem that is not proved, because it's too small and its true follows directly from another theorem or axiom, so it doesn't need to be proved.

(Demostración textual)
**Paragraph proof**: a proof that is written in paragraphs. To know where it ends, the symbol $\blacksquare$ is used, because the black square $\blacksquare$ means that the paragraph proof of the theorem is finished.

(Demostraciones a dos columnas)
**Two column proofs**: a way to write mathematical proofs in a structured manner. The proof is written in a table with two columns. The first column has the header of 'Statement', and its rows contain the steps of the proof. The second column has the header of 'Reason', and its rows state the reason why the step they accompany is correct.

| Statement | Reason           |
| :-------: | :--------------: |
| Step1     | Reason1          |
| (1) Step2 | Reason2          |
| Step3     | Reason3 from (1) |
*Two column proof template*

Step1 is supported by Reason1, Step2 is supported by Reason2, and so on. If ReasonN is a conditional statement, then StepN must be the conclusion or consequent of that conditional statement. For clarity, a parentheses pair with a number can be added to a step, so that it's clear from which step a given reason stems. In the *Two column proof template* table, Reason3 stems from Step2, this is shown with the parentheses '(1)'.

(Variables)
**Variables**: the representation of quantities that can vary, written using letters of the alphabet, such as $a, b, c, x, y, z$.

(Constantes)
**Constants**: the representation of quantities that can not vary, that stay always with the same value, written using letters of the alphabet, such as $m, n$.

The use of a letter of the alphabet as a variable or as a constant is determined from the context, so the context must state which letters are variables and which are constants.

(Funciones)
**Functions**: an operation or set of operations done over a number or numbers, that returns a result. Operators (Operadores) act as functions, e.g. $a + b$ can be written as $sum(a,b)$, where the function $sum$ returns the sum of $a$, $b$.

(Símbolos algebraicos)
**Algebraic symbols**: numbers, variables, constants, operators, functions.

(Enunciado matemático)
**Math statement**: any math writing that can be read as a statement, with symbols, signs, numbers, operators, etcetera, e.g. math expressions, equations, inequalities, and other.

(Expresión matemática)
**Math expression**: a math statement of numbers, symbols, and operations together, such as $a (b + c) - d$

(Simplificación)
**Simplification**: do all possible operations in an expression. $4 \cdot 2 + 1$ can be simplified to $9$. Symbols of rational numbers are left as is, for example $\sqrt{\pi}$ should not be simplified further.

(Evaluar una expresión)
**Evaluate an expression**: this means substitute symbols for specific values and calculate the result, e.g. in $x + 7$ substitute $x$ for $4$ and calculate, $4 + 7 = 11$. Expressions without symbols are ready to be evaluated.

(Subíndice de un símbolo)
**Subscript of a symbol | subindex of a symbol**: a small number put at the bottom front of a symbol (a constant or a variable), to differentiate between related symbols. For example $(x_1, y_1)$ and $(x_2, y_2)$ represent two different points in the $x$-$y$ plane.

The subindex of a symbol can also be a variable itself, for example $x_j$ where the subindex $j$ may vary. When not specified, the variable $j$ is a counting number with a maximum value, meaning that the minimum value of $j$ is $1$, and the maximum value is a given constant $n$.

In cases of symbols that have the same subindex but need to represent different values of the subindex, a number can be appended to the subindex, for example $x_{j1}$ and $x_{j2}$ represent the same symbol $x_j$, but with two distinct values of the subindex $j$.

(Símbolo entonces)
**Then symbol**: the symbol of a double right arrow $\Rightarrow$ is used in mathematics in general, to signify 'then'.

### Numeral systems (Sistemas de numeración)

(Dígitos | Cifras)
**Digits**: each of the numeric values that makes up a number, e.g. the number $834$ has three digits, namely $8$, $3$, and $4$.

(Sistema de numeración posicional)
**Place value system**: system in which the value of a digit depends on its place in the number.

(Sistema de numeración decimal)
**Decimal place value system**: the most common place value system, each place is a power of 10, from right to left, starting at 0 in the first place, 1 in the second place and so on, e.g. $345$ is $3$ in the third position ($3$ of 10 to the power of 2), $4$ is in the second position ($4$ of 10 to the power of 1), and $5$ is in the first position ($5$ of 10 to the power of 0).

(Forma expandida de los números)
**Expanded form of the numbers**: numbers in a place value system can be shown in an expanded form, this expanded form is the sum of each of the digits in a given number multiplied by the base of the place value system to the power of its respective position, e.g. $345$ in expanded form is $3 \cdot 10^2 + 4 \cdot 10^1 + 5 \cdot 10^0$

(Grupos en la numeración posicional)
**Plave value periods**: these periods are the separation of digits in groups of three, each has a name, ones, thousands, millions, thousandths, millionths, etcetera.

### Coordinate systems (Sistemas de coordenadas)

(Recta real)
**Number line**: the numbers depicted in a line. This is the most basic one dimensional (1D) coordinate system.

(Origen)
**Origin**: this is the point at 0 in all dimensions, e.g. in three dimensions, the origin is $(0, 0, 0)$.

(Coordenada de un punto)
**Coordinate of a point**: an ordered tuple of numbers indicating the location of the point. In the three dimensional tuple $(a, b, c)$, $a$ indicates the location of the point along the first dimension, $b$ indicates the location of the point along the second dimension, and $c$ indicates the location of the point along the third dimension. This pattern continues if the tuple has more numbers.

(Sistema de coordenadas rectangulares | Plano coordenado)
**Rectangular coordinate system | Coordinate grid**: the rectangular coordinate system is the 2D version of the number line, it is made with a horizontal number line and a vertical number line that cross each other at zero. The positive numbers in the horizontal number line are at the right of zero, and the positive numbers in the vertical number are above zero.

The horizontal number line is called the $x$-axis (el eje $x$) or abscissa axis (eje de abscisas). The vertical number line is called the $y$-axis (el eje $y$) or ordinate axis (eje de ordenadas).

The rectangular coordinate system is also called the $x$-$y$ plane (el plano $x$-$y$), the coordinate plane (el plano coordenado), or the Cartesian coordinate system (el plano cartesiano)

The rectangular coordinate system forms a grid in which there is a vertical line that passes through each number in the $x$-axis, and there is an horizontal line that passes through each number in the $y$-axis. Each of the four divisions of the $x$-$y$ plane is called a quadrant, they are denoted with roman numerals, $I$, $II$, $III$, and $IV$.

(Par ordenado)
**Ordered pair**: a pair of numbers that can be used to represent a point in the rectangular coordinate system, it's the same concept as the coordinate of a point, but only for the 2D case. Just as in the number line a single number is required to know the location of a point, in the $x$-$y$ plane two numbers are required, which should be ordered to know which number goes in the $x$-axis and which in the $y$-axis. By convention, the first number in an ordered pair indicates the value in the $x$-axis, and the second number indicates the value in the $y$-axis. Let $a$, $b$ be two numbers, then the ordered pair made with them is $(a, b)$, $a$ is the $x$-axis value, and $b$ is the $y$-axis value.

(Punto en el eje)
**Points on the axes**: any point that lies in an axis, i.e. a point whose ordered pair contains at least a zero. A point $(a, 0)$ is in the $x$-axis, and a point $(0, b)$ is in the $y$-axis.

(Gráfica)
**Graph**: the use of the $x$-$y$ plain to show points. These points can come from a mathematical function or equation, points scattered, etcetera. If the graph comes from an equation, it is read as the graph of the equation (la gráfica de la ecuación). The graph itself is the set of points that result from plotting the equation.

(Graficar puntos)
**Point plotting method**: individual points from an equation can be plotted, e.g. in a linear equation, individual points can be plotted and then a single line can be passed through them to form the graph of the equation. This method starts by plotting points of a given equation and then joining them with a line or lines as necessary.

(Gráfica de líneas horizontales y verticales)
**Graph of horizontal and vertical lines**: in the $x$-$y$ plane, the equation $x = a$ represents a vertical line that passes through the point $(a, 0)$, and the equation $y = b$ represents an horizontal line that passes through the point $(0, b)$.

(Intercepto de una gráfica)
**Intercept of a graph**: in a graph, the intercepts are the points in which the graph crosses an axis, i.e. the points of the graph that have a $0$ in the $x$ coordinate or in the $y$ coordinate, or in both.

(Intercepto en $x$)
**$x$-intercept**: an intercept with the $x$-axis, it has the form $(a, 0)$ where $a$ is the $x$ coordinate of the intercept.

(Intercepto en $y$)
**$y$-intercept**: an intercept with the $y$-axis, it has the form $(0, b)$ where $b$ is the $y$ coordinate of the intercept.

A linear equation can be graphed using the intercepts as the points through which the line passes.

### Subsets of the real numbers (Subconjuntos de los números reales)

#### Counting numbers (Números naturales)

(Números naturales)
**Counting numbers**: these are, 1, 2, 3, 4, ..., up to infinity

#### Whole numbers (Números naturales y el cero)

(Números naturales y el cero)
**Whole numbers**: these are, 0, 1, 2, 3, 4, ..., so the set of whole numbers is the same as the set of counting numbers and zero.

#### Integer numbers (Números enteros)

The set of integers is the set of the whole numbers and the negative numbers. This set of numbers also forms an ordered set in which the relational operators can be used to compare the values of two integer numbers.

(Números positivos y negativos)
**Positive and negative numbers**: positive numbers are greater than 0 and negative numbers are less than 0, so 0 is neither. Negative numbers are represented with a minus in front, e.g. $-5$ is negative $5$. Positive numbers are greater than negative numbers.

(Números opuestos)
**Opposite numbers**: pairs of numbers only differentiated by their sign, one is positive and the other one is negative, but their value is the same. Opposite numbers are obtained with the minus sign.

The opposite of $a$ is $-a$, so $-(a) = -a$. The opposite of $-a$ is $a$, so $-(-a) = a$.

(Números enteros consecutivos)
**Consecutive integers**: integers that follow each other by adding $1$ repeatedly, e.g. $-4$, $-3$, $-2$, or $19$, $20$, $21$, etcetera.

#### Rational numbers (Números racionales)

The rational numbers form the set of numbers that can be represented via fractions. This is an ordered set in which the relational operators can be used to compare the values of two rational numbers.

Rational numbers when represented as decimals, have their decimal part with a finite amount of digits, or if the amount is infinite then it repeats itself, which means that a decimal number that is rational can always be represented as a fraction.

(Fracciones)
**Fractions**: numbers that represent a part of a whole number or an integer, so there are many fractions between any two integers.

(Notación de las fracciones)
**Fraction notation**: given that fractions are numbers that can be between two integers, they are represented with a division, a fraction that is not integer has a remainder different from 0 when represented as a division. Given two integers $a$ and $b$, with $b$ being nonzero, the fraction $\frac{a}{b}$ is calculated as $a$ divided by $b$.

For example, $\frac{2}{3}$ means $2$ divided by $3$, and using the definition of division, this calculates the amount of times that the number $3$ is subtracted from $2$ until 0 is reached, but subtracting $3$ from $2$ gives $-1$ because $2 - 3 = -1$, so to reach 0, a proportion, fraction, or part of $3$ must be subtracted from $2$, and not the full unity of the number $3$. 

By the definition of division, $\frac{2}{3}$ is the amount of times that $3$ is subtracted from $2$ to reach 0. This amount, $\frac{2}{3}$ is between $0$ and $1$ and it occupies the same proportional distance to $1$, as the number $2$ occupies to $3$.

(Numerador y denominador)
**Numerator and denominator**: the numbers in a fraction, the numerator is the number on top (called dividend in the division operation), and the denominator is the number at the bottom (called divisor in the division operation). In $\frac{a}{b}$ $a$ is the numerator and $b$ is the denominator.

(Fracciones propias)
**Proper fractions**: a fraction $\frac{a}{b}$ in which $a < b$. A proper fraction is always between 0 and 1.

(Fracciones impropias)
**Improper fractions**: a fraction $\frac{a}{b}$ in which $a \ge b$. An improper fraction can be an integer (when $a$ is a multiple of $b$), and it is always greater than or equal to 1, which means that an improper fraction has an integer part and a proper fraction part, when said parts are added the result is the improper fraction.

(Números mixtos)
**Mixed numbers**: the representation of an improper fraction as an integer part and a proper fraction part. The improper fraction $\frac{ac + b}{c} = a + \frac{b}{c}$ is represented as a mixed number as $a\frac{b}{c}$, so the addition of the integer part and the proper fraction part of a mixed number result in an equivalent improper fraction.

The term $ac$ in the numerator of $\frac{ac + b}{c}$, is a multiple of $c$, and when dividing $ac$ by $c$ the result is an integer $a$. In the mixed number $a\frac{b}{c}$, $a$ is the integer part, and $\frac{b}{c}$ is the proper fraction part.

(Fracciones equivalentes)
**Equivalent fractions**: fractions that have the same value, even when written with different numbers. Fractions written with different numbers can have the same value because those different numbers can show the same fraction. For example, the fraction $\frac{2}{3}$ is the same as the fraction $\frac{4}{6}$, because the proportional distance that the number $2$ occupies in $3$ is the same as the proportional distance that the number $4$ occupies in $6$. The value of each fraction itself is the same in equivalent fractions.

(Propiedad de las fracciones equivalentes)
**Equivalent fractions property**: in a given fraction $\frac{a}{b}$, multiplying (or dividing) both the numerator and the denominator by a nonzero number $c$, doesn't change the value of the fraction, so $\frac{a}{b} = \frac{a c}{b c}$.

(Fracciones complejas)
**Complex fractions**: the division of two fractions, $\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a}{b} \div \frac{c}{d} = \frac{a d}{b c}$.

(Fracciones negativas)
**Negative fractions**: when either the numerator is negative, or the denominator is negative, the fraction itself is negative, $\frac{-a}{b} = -\frac{a}{b}$, and $\frac{a}{-b} = -\frac{a}{b}$.

(Decimales)
**Decimals**: the numeric representation of fractions in the place value system. Proper fractions have a value less than 1, to express them as decimals, the places to the right of the units place are used. The separation between the units place and the decimal places is commonly shown with a dot. For example, the numbers 0.1, 3.541, etc.

About their place value, the first place to the right of the dot has its value multiplied by 10 to the -1, the second place has its value multiplied by 10 to the -2, the third place to the -3, and so on.

(Decimales equivalentes)
**Equivalent decimals**: different decimal numbers that have the same value. For example $10.3$ has the same value as $10.30$, or $10.300$.

(Decimal finito)
**Finite decimal**: a decimal with a finite amount of digits after the decimal period.

(Decimal periódico)
**Repeating decimal**: a decimal in which a group of digits after the decimal period repeats itself indefinitely. Repeating decimals are denoted with a horizontal bar over the digits that repeat. For example, in $\frac{8}{7} = 1.\overline{142857}$, the line over $142857$ indicates that it repeats itself infinitely many times.

(Porcentaje)
**Percent**: ratio with a denominator of 100. A percent number is identified with the percent sign $\%$ after it. For example $54\%$ means the ratio $\frac{54}{100}$.

(Ecuación de porcentaje)
**Percentage equation**: an equation that defines a percent. To define a percent, two concepts are needed, the base (la base) and the amount (la cantidad). The base is the number that represents the whole, and the amount is the number that represents the part or fraction of that whole.

Let $p\%$ be a percent, $B$ be the base, $A$ be the amount, then $A = p\% \cdot B$. Isolating the percent allows finding its value from the amount and the base, $p\% = \frac{A}{B}$.

The reciprocal of a percent, $\frac{1}{p\%}$, means the reciprocal of a ratio. If a percent $p\%$ means the part over the total, i.e. there are $p$ part units per group of $100$ total units, then $\frac{1}{p\%}$ means that there are $100$ total units per group of $p$ part units.

#### Irrational numbers (Números irracionales)

The irrational numbers form the set of numbers such as $\pi$, in which the decimal part of the number is infinite and never repeats itself. The square root of numbers that are not perfect squares is also irrational.

The fact that they are called irrational, doesn't necessarily mean that they can't have predictable patterns, for example, a number such as $0.101001000100001000001...$ is irrational by definition, but it can be understood as the number with a $1$ in between a steady growing number of $0$s. This pattern is infinite and never repeats itself, so it's an irrational number.

#### Real numbers (Números reales)

The set of real numbers is the union of the sets of rational and irrational numbers.

#### Transcendental numbers (Números trascendentes)

The transcendental numbers are numbers that can't be obtained as a solution of a polynomial with rational coefficients.

For example $\sqrt{2}$ is not transcendental because it is the solution of $x^2 = 2$, which is a polynomial with rational coefficients.

(La constante pi)
**The pi constant**: the fraction of the circumference over the diameter. It's represented with the greek letter pi, which is $\pi$. The value of pi is roughly $\pi = 3.14159...$, this is a non repeating decimal. $\pi$ is a transcendental number because there is no polynomial with rational coefficients whose solution is $\pi$.

(Aproximación fraccionaria de pi)
**Fractional approximation of pi**: there are infinitely many fractional approximations of pi, one of the simplest is $\frac{22}{7}$.

### Number approximation (Aproximación de números)

(Redondeo)
**Rounding**: approximating a number with another of less significant digits.

(Función techo)
**Ceiling function**: a function that approximates a number to the nearest bigger integer. Denoted as $\lceil x \rceil$, where $x$ is the number being rounded, e.g. $\lceil 2.5 \rceil = 3$, $\lceil -2.5 \rceil = -2$.

(Función piso)
**Floor function**: a function that approximates a number to the nearest smaller integer. Denoted as $\lfloor x \rfloor$, where $x$ is the number being rounded, e.g. $\lfloor 2.5 \rfloor = 2$, $\lfloor -2.5 \rfloor = -3$.

(Truncamiento)
**Truncation**: rounding a number by removing all digits after the decimal point, e.g. $2.5$ truncated is $2$, and $-2.5$ truncated is $-2$.

### Equations and inequalities (Ecuaciones y desigualdades)

(Signo de igualdad)
**Equality sign**: this sign is $=$, the equal sign.

(Ecuación)
**Equation**: the math statement of two expressions that are equal, e.g. $a + b = c + d$

(Definición matemática)
**Math definition**: an equation in which a symbol is defined. The sign $:=$ is used to make definitions, to differentiate it from the equal sign. $a := b$ defines $a$ as $b$, this is read as $a$ is defined as $b$ ($a$ es definido como $b$).

(Fórmula matemática)
**Math formula**: an equation whose purpose is to find the value of a quantity or variable, i.e. formulas are equations expressly intended to find the value of a quantity, they are the "formula" to find said value, e.g. in $x = vt$ the distance $x$ is calculated as the product of velocity $v$ and time $t$.

(Operadores relacionales)
**Relational operators**: operators that compare the values of two numbers. These operators serve to make the set of numbers an ordered set, ordered according to the values of the numbers.

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

(Solución de una ecuación)
**Solution of an equation**: an equation that contains a variable can be solved by determining the value of the variable that makes the equation true, e.g. in $x + 7 = 11$, $x$ must be $4$ so that the equation is true, and $4$ is the solution of the equation. An equation with several variables has solution tuples, e.g. an equation with three variables, $x$, $y$, and $z$, has solution tuples of size three, such as $(4, 3, 8)$.

(Despejar una variable)
**Isolate a variable**: using properties of equality, to make a variable stand alone in one side of an equation, e.g. $4 + y/2 = x + 1 \Rightarrow y = 2x - 6$, here the variable $y$ is isolated.

(Solucionar ecuaciones)
**Solve equations**: Solving an equation commonly means isolating a variable to find its value.

The addition property of equality is used to solve equations when there is a negative term which subtracts from the variable, then said term is added to both sides of the equality, helping in isolating the variable.

The subtraction property of equality is used to solve equations when there is a positive term added to the variable, then said term is subtracted from both sides of the equality, helping in isolating the variable.

The multiplication property of equality is used to solve equations when there is a number dividing the variable, then said number is multiplied to both sided of the equality, helping in isolating the variable.

The division property of equality is used to solve equations when there is a factor multiplying the variable, then both sides of the equality are divided by said factor, helping in isolating the variable.

(Propiedad reflexiva de la igualdad)
**Reflexive property of equality**: a real number is equal to itself, $a = a$.

(Propiedad simétrica de la igualdad)
**Symmetric property of equality**: if a first real number is equal to a second, then the second number is equal to the first, $a = b \leftrightarrow b = a$.

(Propiedad transitiva de la igualdad)
**Transitive property of equality**: if a first real number is equal to a second, and the second number is equal to a third, then the third number is equal to the first, if $a = b$ and $b = c$ then $a = c$.

(Propiedad de sustitución de la igualdad)
**Substitution property of equality**: if two real numbers are equal, one can be substituted by the other, if $a = b$ then $b$ can substitute $a$ and vice versa.

(Propiedad aditiva de la igualdad)
**Addition property of equality**: adding a number to both sides of an equality preserves the equality. Given $a = b$, then $a + c = b + c$.

(Propiedad sustractiva de la igualdad)
**Subtraction property of equality**: subtracting a number from both sides of an equality preserves the equality. Given $a = b$, then $a - c = b - c$.

(Propiedad multiplicativa de la igualdad)
**Multiplication property of equality**: multiplying a number to both sides of an equality preserves the equality. Given $a = b$, then $a c = b c$.

(Propiedad divisiva de la igualdad)
**Division property of equality**: dividing both sides of an equality by a nonzero number preserves the equality. Given $a = b$ and $c \ne 0$, then $\frac{a}{c} = \frac{b}{c}$.

(Proporción)
**Proportion**: an equation in which two fractions (ratios or rates) are equated. Let $a$, $b$, $c$, $d$, be numbers, with $b$ and $d$ being nonzero, then $\frac{a}{b} = \frac{c}{d}$ is a proportion, it's read as $a$ is to $b$ as $c$ is to $d$ ($a$ es a $b$ como $c$ es a $d$).

(Producto cruzado)
**Cross product**: a proportion where the denominators have been multiplied in both sides, i.e. in the proportion $\frac{a}{b} = \frac{c}{d}$, the cross product is $ad = bc$. This concept is used to test if a proportion is true without dividing.

(Medios y extremos de una proporción)
**Means and extremes of a proportion**: any proportion $\frac{a}{b} = \frac{c}{d}$ can be represented with ratios as $a:b = c:d$. Following this representation, the numbers $b$ and $c$ are called the means (they are in the center), and the numbers $a$ and $d$ are called the extremes (they are in the extremes). Using these definitions, it can be said that the cross product $ad = bc$ is the same as saying that the product of the extremes is equal to the product of the means of the proportion.

(Proporción extendida)
**Extended proportion**: a proportion with more than one equal sign, which means that an extended proportion makes several fractions equal, e.g. $\frac{a}{b} = \frac{c}{d} = \frac{e}{f}$.

(Proporción con porcentajes)
**Percent proportion**: a proportion in which one of the fractions is a percentage. Using terms from before, let $B$ be the base, $A$ the amount, then $\frac{A}{B} = \frac{p}{100}$, this means that the amount $A$ is to the base $B$ as $p$ is to $100$.

(Ecuación en dos variables)
**Equation in two variables**: an equation that has two variables. Setting the value of one of the variables allows finding the value of the other.

### Operations with real numbers (Operaciones con números reales)

#### Addition of real numbers (Adición de números reales)

Addition is the operation of adding numbers together. Addition means starting at the end of the first number, and then moving the amount being added by the second number.

Addition is the inverse operation of subtraction. Given that addition means after the first number move the amount of the second, commutativity means that no matter which number comes first and which second, the end position is the same.

Adding a negative number is the same as subtracting its opposite (just as adding a positive number is the same as subtracting its opposite). If the number being added is positive then the addition moves in the positive direction, if the number being added is negative then the addition moves in the negative direction.

(Operador suma)
**Sum operator**: this operator is $+$, the plus sign.

(Notación de la suma)
**Addition notation**: the addition of $a$ and $b$ is $a + b = c$, read as $a$ plus $b$ ($a$ más $b$), $a$, $b$ are called the addends (sumandos), the result $c$ is called the sum (suma).

(Propiedad de identidad de la suma)
**Identity property of addition**: adding to zero doesn't change the number, $a + 0 = a$

(Identidad aditiva)
**Additive identity**: The number 0.

(Propiedad conmutativa de la suma)
**Commutative property of addition**: changing the order of the addends doesn't change the sum, $a + b = b + a$.

(Propiedad asociativa de la adición)
**Associative property of addition**: using grouping symbols to group addition operations does not change the sum, $a + b + c = (a + b) + c = a + (b + c)$.

(Inverso aditivo)
**Additive inverse**: the opposite of a number, is its additive inverse. The additive inverse of a number $a$ is $-a$.

(Propiedad inversa aditiva)
**Inverse property of addition**: the sum of a number and its additive inverse is zero, $a + (-a) = a - a = 0$.

(Símbolo de sumatoria)
**Summation symbol**: the symbol $\sum_i$ that represents the sum of the elements of the set to which $i$ belongs, e.g. $\sum_{i = 1}^{n}{x_i} = x_1 + x_2 + ... + x_n$, where $1, 2, ..., n$ is the set of values of $i$ over which the summation is done.

(Adición de fracciones con denominador común)
**Addition of fractions with common denominators**: the same as normal addition. It must be noted that $\frac{a}{b} = a\frac{1}{b}$, which means that $\frac{a}{b} + \frac{c}{b} = a\frac{1}{b} + c\frac{1}{b} = (a + c)\frac{1}{b} = \frac{a + c}{b}$.

(Adición de fracciones con denominador diferente)
**Addition of fractions with different denominators**: first the fractions being added must have common denominators, for this, each fraction is converted to an equivalent fraction such that its denominator is the common one. The common denominator can be found as the least common denominator of the fractions. The addition is done like regular addition when the denominators are common.

(Adición de números mixtos)
**Addition of mixed numbers**: like regular addition. The integer parts of the mixed numbers can be added directly, and the proper fraction parts are added with the rules of addition of fractions, the result is the sum of the integer and fraction parts. To show the result as a mixed number, the integer part is left alone, and the fraction part is converted to a proper fraction if necessary, this may change the integer part.

#### Subtraction of real numbers (Sustracción de números reales)

Subtraction is the operation of subtracting a number from another. Subtraction means starting at the end of the first number, and then moving in the opposite direction the amount of units being subtracted by the second number.

Subtraction is the inverse operation of addition. Subtraction is not commutative.

Subtracting a negative number means moving opposite to its direction, i.e. moving in the positive direction. In $a - (-b)$ the expression $- (-b)$ subtracts negative $b$, so moving opposite to negative $b$ means adding positive $b$, and $a - (-b) = a + b$.

(Operador resta)
**Subtraction operator**: this operator is $-$, the minus sign.

(Notación de la resta)
**Subtraction notation**: the subtraction of $a$ from $b$ is $b - a = c$, read as $b$ minus $a$ ($b$ menos $a$), $b$ is called the minuend (minuendo), $a$ is called the subtrahend (sustraendo), the result $c$ is called the difference (diferencia)

(Sustracción de fracciones con denominador común)
**Subtraction of fractions with common denominators**: the same as normal subtraction. It must be noted that $\frac{a}{b} = a\frac{1}{b}$, which means that $\frac{a}{b} - \frac{c}{b} = a\frac{1}{b} - c\frac{1}{b} = (a - c)\frac{1}{b} = \frac{a - c}{b}$.

(Sustracción de fracciones con denominador diferente)
**Subtraction of fractions with different denominator**: first the fractions being subtracted must have common denominators, for this, each fraction is converted to an equivalent fraction such that its denominator is the common one. The common denominator can be found as the least common denominator of the fractions. The subtraction is done like regular subtraction when the denominators are common.

(Sustracción de números mixtos)
**Subtraction of mixed numbers**: like regular subtraction. The integer parts of the mixed numbers can be subtracted directly, and the proper fraction parts are subtracted with the rules of subtraction of fractions, the result is the difference of the integer and fraction parts. To show the result as a mixed number, the integer part is left alone, and the fraction part is converted to a proper fraction if necessary, this may change the integer part.

#### Multiplication of real numbers (Multiplicación de números reales)

Multiplication is the operation of multiplying numbers together. Multiplication means the repeated addition of a number with itself, the amount of repeated additions is the other number in the operation.

Multiplication is the inverse operation of division. Given that multiplication means the repeated addition of the first number with itself a number of times equal to the second number, this means that no matter which number comes first and which second, the final repeated addition is the same.

When multiplying or dividing by a negative number, it changes the sign of the other number, so multiplying or dividing a negative number by another negative number results in a positive number, and multiplying or dividing a positive number by a negative number results in a negative number.

In a multiplication operation, if the amount of repeated additions is negative, then this means repeated addition with each addition done in the opposite direction. For example, $4 \cdot -3 = -4 -4 -4$, each addition is done in the opposite direction of $4$, and in $-4 \cdot -3 = 4 + 4 + 4$, each addition is done in the opposite direction of $-4$.

Multiplication by a number is the same as division by its reciprocal, $a b = a \div \frac{1}{b}$, because it follows the definition of division as repeated subtraction. Starting from $a$, to reach 0 by subtracting $\frac{1}{b}$, it must be done $a b$ times, this is because to reach 0 by subtracting $1$ it is done $a$ times, $\frac{a}{1} = a$, and to do it by subtracting $\frac{1}{b}$, it must be done $b$ times as much.

(Operador multiplicación)
**Multiplication operator**: this operator is $\times$, the times sign. Another is $\cdot$, the dot sign. Another is $()$, the parentheses signs.

(Notación de la multiplicación)
**Multiplication notation**: the multiplication of $a$ and $b$ is $a b = c$, read as $a$ times $b$ ($a$ veces $b$), $a$, $b$ are called the factors (factores), the result $c$ is called the product (producto).

(Propiedad anulativa de la multiplicación)
**Multiplication property of zero**: the product of any number multiplied by 0, is 0, $a \cdot 0 = 0$.

(Propiedad modulativa de la multiplicación)
**Identity property of multiplication**: the product of any number multiplied by 1, is the number itself, $a \cdot 1 = a$.

(Identidad multiplicativa | elemento neutro | elemento identidad)
**Multiplicative identity**: The number 1.

(Propiedad conmutativa de la multiplicación)
**Commutative property of multiplication**: changing the order of the factors doesn't change the product, $a b = b a$.

(Propiedad asociativa de la multiplicación)
**Associative property of multiplication**: using grouping symbols to group multiplication operations does not change the product, $a b c = (a b) c = a (b c)$.

(Propiedad distributiva de la multiplicación respecto a la suma)
**Distributive property of multiplication over addition**: when a group of addends (grouped using a grouping symbol) is multiplied by a number, it's the same as the sum of the products of said number by each addend, $a (b + c) = a b + a c$.

This property shows itself when multiplying $a$ by the sum $b + c$, the resulting product can be seen as the sum of $a b$ and $a c$. This property actually includes subtraction as a case of the sum, given that the addends can be negative numbers.

(Inverso multiplicativo)
**Multiplicative inverse**: the reciprocal of a number, is its multiplicative inverse. The multiplicative inverse of a number $a$ is $\frac{1}{a}$.

(Propiedad inversa de la multiplicación)
**Inverse property of multiplication**: the product of a number and its multiplicative inverse is one, $a \frac{1}{a} = 1$.

(Multiplicación por -1)
**Multiplication by -1**: a number multiplied by $-1$ results in its opposite, $-1 \cdot a = -a$. Using the definition of multiplication, multiplying $a$ by $-1$ is the same as adding $a$ one time in its opposite direction, which is $-a$, the opposite of $a$.

(Multiplicación por 0)
**Multiplication by 0**: the product of any number and 0 is 0, $a \cdot 0 = 0$. This is because $a$ is added $0$ times with itself.

(Multiplicación de fracciones)
**Fraction multiplication**: the product of two fractions is the product of the numerators over the product of the denominators, $\frac{a}{b} \frac{c}{d} = \frac{a c}{b d}$, this implies two operations, first the multiplication by $c$ and then the division by $d$. Given the PEMDAS order of operations, it's the same if the division by $d$ is done first.

(Multiplicación de decimales)
**Multiplication of decimals**: in the product of decimal numbers, the amount of decimal digits is up to the sum of the decimal digits in the factors.

(Multiplicación y división por 10)
**Multiplication and division by 10**: given that 10 is the base of the decimal place value system, multiplying a number by 10 moves the number one digit to the left, while dividing a number by 10 moves the number one digit to the right. For example, $2 \cdot 10 = 20$, and $2 \div 10 = 0.2$.

(Paradigma de la multiplicación y división)
**Multiplication and division paradigm**: multiplication and division both deal with three concepts: a set of elements, groups of elements, and the size of said groups. Each of this concepts is associated with a number, the total number of elements, the amount of groups, and the size of each group.

Multiplication returns the total number of elements as the product of the amount of groups by the size of each group. For example, $5$ groups of size $4$, have a total number of elements of $5 \cdot 4 = 20$, and $4$ groups each with $5$ elements, have a total number of elements of $4 \cdot 5 = 20$. By itself, the total number of elements remains the same, $20$.

In multiplication, the amount of groups is interchangeable with the size of each group, so a multiplication can be interpreted as the amount of groups times their size, or as the size of the groups times the amount of groups, both interpretations are valid for any single multiplication.

Division has a similar behavior, the total number of elements is the dividend, but then, the divisor can be any of the other two numbers. The divisor can be the amount of groups, or the size of each group, and the quotient is the other number. For example, $24 \div 8 = 3$ means, from the $24$ total elements, with groups of size $8$, then there are $3$ groups, but $24 \div 8 = 3$ also means that from the $24$ total elements, with $8$ groups, each will have a size of $3$. Both conclusions are arrived via repeated subtraction.

The interpretation of $24 \div 8 = 3$ as $24$ elements divided in $8$ groups have a group size of $3$, means that there are $3$ elements per each $1$ group, so $24 \div 8 = 3 \div 1$, in words it could be read as, there are $24$ elements each $8$ groups, or there are $3$ elements each $1$ group.

#### Division of real numbers (División de números reales)

Division is the operation of dividing a first number by a second number. Division means the repeated subtraction of the second number from the first number until reaching 0, the amount of repeated subtractions is the result of the operation.

Division is the inverse operation of Multiplication. Division is not commutative.

If the amount of repeated subtractions is negative, then this means repeated subtraction with each subtraction done in the opposite direction. For example, $24 \div -8 = -3$ so the number $-8$ is subtracted $-3$ times from $24$, i.e. $-8$ is subtracted three times in its opposite direction to reach 0 starting at 24. In $-24 \div -8 = 3$ the amount of repeated subtractions is positive, so $-8$ is subtracted directly from $-24$ three times to reach 0.

Division by a number is the same as multiplication by its reciprocal, $\frac{a}{b} = a \frac{1}{b}$, because having $a$ elements divided in $b$ groups, has each group with size $\frac{a}{b}$, and adding $a$ with itself only a fraction $\frac{1}{b}$ times, ends being at the same place of $\frac{a}{b}$.

(Operador división)
**Division operator**: this operator is $\div$, the division sign. Another is $/$, the slash sign. Another is $\text{---}$, the horizontal line sign.

(Notación de la división)
**Division notation**: the division of $b$ over $a$ is $\frac{b}{a} = c$, read as $b$ divided by $a$ ($b$ dividido $a$), $b$ is called the dividend (dividendo), $a$ is called the divisor (divisor), the result $c$ is called the quotient (cociente).

(Propiedad modulativa de la división)
**Identity property of division**: the quotient of any number divided by 1, is the number itself, $\frac{a}{1} = a$.

(Identidad divisiva)
**Divisive identity**: The number 1.

(Propiedad del cociente uno de la división)
**Division property of quotient one**: any nonzero number divided by itself gives a quotient of 1, $\frac{a}{a} = 1$.

(Propiedades del cero en la división)
**Division properties of zero**: zero divided by any nonzero number is zero, $\frac{0}{a} = 0$. Division by zero is undefined, $\frac{a}{0}\ is\ undef$.

(División por -1)
**Division by -1**: a number divided by $-1$ results in its opposite, $a \div -1 = -a$. Using the definition of division, dividing $a$ by $-1$ is the same as subtracting $-1$ from $a$ until reaching 0, which is $-a$ times, the opposite of $a$.

(Recíproco de un número)
**Reciprocal of a number**: given a number, its reciprocal is another number such that when multipled together the product is 1. In $\frac{a}{b}$, the reciprocal is $\frac{b}{a}$, because $\frac{a}{b} \frac{b}{a} = \frac{a b}{b a} = 1$, and so $a \ne 0$, $b \ne 0$, which means that 0 doesn't have a reciprocal.

Non fraction numbers also have a reciprocal, the reciprocal of $a$ is $\frac{1}{a}$ because $a \frac{1}{a} = 1$. Using the definition of division, $\frac{1}{a}$ means taking the number $1$ and dividing it into $a$ groups, then $\frac{1}{a}$ is the size of each group, which is the same as the place where the first group ends, this place is the definition of the reciprocal of $a$.

(Invertir un número)
**Invert a number**: the process of finding the reciprocal of a number. When a number is inverted the result is its reciprocal.

(División de fracciones)
**Fraction division**: the operation $\frac{a}{b} \div \frac{c}{d}$. This implies two operations, division by $c$ and division by the reciprocal of $d$ which is the same as multiplication by $d$, so $\frac{a}{b} \div \frac{c}{d} = \frac{a d}{b c}$.

(Residuo | Resto)
**Remainder**: in division, this is the number that is left over after doing the repeated subtraction, if any. In $\frac{a}{b} = q + \frac{r}{b}$, $a$, $b$ are numbers with $b$ being nonzero, $q$ is the quotient, and $r$ is the remainder.

#### Exponentiation of real numbers (Exponenciación de números reales)

(Notación exponencial)
**Exponential notation**: used in expressions where a number is multiplied by itself several times, for example, $2 \cdot 2 \cdot 2 \cdot 2$ is written as $2^4$. In general $a a a \ldots a = a^n$, where the value $n$ is the amount of times that $a$ is multiplied by itself.

Using the shown symbols, the exponential notation is read as $a$ to the $n$-th power ($a$ a la $n$-ésima potencia), also read as $a$ to the power of $n$ ($a$ a la $n$). The operation itself is read as raise $a$ to the $n$-th power (elevar $a$ a la $n$-ésima potencia), also read as raise $a$ to the power of $n$ (elevar $a$ a la $n$).

(Potenciación)
**Exponentiation**: the operation of raising a number to a given power, e.g. $a^n$.

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
**Product property of exponents**: the product of two equal bases, each with their exponent, is equal to the base raised to the sum of the exponents, $a^m a^n = a^{m + n}$.

(Potencia de una potencia)
**Power property of exponents**: the result of raising a base to an exponent and then raising that power to another exponent, is equal to the base raised to the power of the product of the exponents, ${(a^m)}^n = a^{m n}$.

(Producto de potencias con el mismo exponente)
**Product to a power property of exponents**: the product of two bases with the same exponent, is equal to the product of the bases raised to the power of the exponent, $a^n b^n = {(a b)}^n$.

(Cociente de potencias de la misma base)
**Quotient property of exponents**: the quotient of two exponents that have the same base, is equal to the base raised to the power of the exponent in the numerator minus the exponent in the denominator, $\frac{a^m}{a^n} = a^{m - n}$.

(Exponente negativo)
**Negative exponent**: the reciprocal of the base raised to the power of the exponent, $a^{-n} = \frac{1}{a^n}$.

(Exponente cero)
**Zero exponent**: a nonzero base raised to the power of zero is equal to one, $a^0 = 1$ such that $a \ne 0$.

(Potencia de un cociente)
**Quotient to a power property of exponents**: the quotient of two bases with the same exponent, is equal to the quotient of the bases raised to the power of the exponent, $\frac{a^n}{b^n} = \left(\frac{a}{b}\right)^n$.

#### Order of operations (Orden de las operaciones)

The order in which to execute the operations. In $5 + \frac{10}{2}$, the result is $10$ if division is done first, but the result is $7.5$ if addition is done first. This can be modified with grouping symbols.

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

### Properties of real numbers (Propiedades de los números reales)

(Valor absoluto)
**Absolute value**: the distance between 0 and a given number, it's always positive and it's the same for any number and its opposite. For a given number $a$, its absolute value is denoted as $\lvert a \rvert$, e.g. $\lvert 5 \rvert = \lvert -5 \rvert = 5$.

### Multiples and factors of integers (Múltiplos y factores de los enteros)

(Múltiplos de un número)
**Multiples of an number**: given an integer, its multiples are the result of multiplying it by any of the counting numbers, so an integer has infinite multiples. The smallest multiple (in absolute value) is the integer itself.

(Divisibilidad)
**Divisibility**: if a given integer $b$ is multiple of another $a$, then $b$ is divisible by $a$, because $\frac{b}{a}$ is an integer. All the multiples of $a$ are divisible by $a$.

(Números pares)
**Even numbers**: 0 and the multiples of 2.

(Números impares)
**Odd numbers**: the integers that are not even numbers.

(Pruebas de divisibilidad)
**Divisibility tests**: a quick test made to check if an integer is divisible by another. The following are the divisibility tests of the first positive integers.

A given integer is divisible by 2 if its last digit is an even number.
A given integer is divisible by 3 if the sum of its digits is divisible by 3.
A given integer is divisible by 4 if its last two digits are divisible by 4.
A given integer is divisible by 5 if its last digit is 0 or 5.
A given integer is divisible by 6 if it's divisible by 2 and 3.
A given integer is divisible by 7 if its last digit is doubled and then subtracted from the rest of the integer, and the result of that is divisible by 7.
A given integer is divisible by 8 if its last three digits are divisible by 8.
A given integer is divisible by 9 if the sum of its digits is divisible by 9.
A given integer is divisible by 10 if its last digit is 0.
A given integer is divisible by 11 if the alternating sum of its digits (i.e. the first digit, minus the second, plus the third, minus the fourth, etc.) is divisible by 11.

(Factores de un número)
**Factors of a number**: in a given integer, its factors are the integers that multiplied together produce it. An integer can have several different sets of factors, e.g. $12$ has different sets of factors like $3$, $4$, also $2$, $6$, or $2$, $3$, $2$, or others.

(Pares de factores)
**factor pairs**: factors can always be presented in pairs, because at least two integers are required to be multiplied together in order to produce a given integer. In the example of $12 = 2 \cdot 3 \cdot 2$, with factor pairs the equation would be $12 = 2 \cdot 6$ or $12 = 3 \cdot 4$.

(Números primos)
**Prime numbers**: each of the integers with only 2 different factors, the number 1 and the integer itself.

(Números compuestos)
**Composite numbers**: the numbers that are not prime, i.e. the integers that have more than one factor pair.

(Factores primos)
**prime factors**: the set of prime numbers that multiplied together produce a given integer. Integers can be represented as the product of prime factors.

(Descomposición en factores primos)
**Prime factorization**: the process of finding the prime factors of a number.

(Multiplicidad de un factor primo)
**Multiplicity of a prime factor**: the amount of times that a prime factor of a given number is repeated, e.g. in the number $60$ the prime factors are $2$, $2$, $3$, $5$, the number $2$ has a multiplicity of $2$, the number $3$ has a multiplicity of $1$, and the number $5$ has a multiplicity of $1$.

(Múltiplos comunes)
**Common multiples**: given a set of at least two integers, the common multiples are the numbers that are multiples of all the integers in the set.

(Mínimo común múltiplo)
**Least common multiple**: the smallest common multiple of a given set of at least two integers.

The least common multiple of two integers can be calculated using their prime factors. The least common multiple of two integers is the product of all their unique prime factors, each raised to the power of their maximum multiplicity.

For example, to find the least common multiple of $12$ and $18$, the prime factors of $12$ are $2$, $2$, $3$, and the prime factors of $18$ are $2$, $3$, $3$. The least common multiple is $2 \cdot 2 \cdot 3 \cdot 3 = 36$, the number $2$ has a maximum multiplicity of $2$ (in $12$), and $3$ has a maximum multiplicity of $2$ (in $18$).

(Mínimo común denominador)
**Least common denominator**: the least common multiple of the denominators from a set of at least two fractions.

(Máximo común divisor)
**Greatest common divisor**: the biggest common divisor of a given set of at least two integers.

In this use of the term "divisor", it is also a factor of the set of numbers. That's why sometimes this is also called greatest common factor (Máximo factor común).

The greatest common divisor of two integers can be calculated using their prime factors. The greatest common divisor of two integers is the product of their common prime factors, each raised to the power of their minimum multiplicity.

## Logic definitions (Definiciones de lógica)

(Razonamiento inductivo)
**Inductive reasoning**: inductive reasoning means reasoning on the basis of observed patterns.

(Patrones numéricos)
**Number patterns**: patterns made with numbers. Discovering the pattern requires inductive reasoning. For example, the numbers $2$, $4$, $6$, $8$... form a pattern, in this pattern, the next numbers are most likely $10$, $12$, $14$, etcetera.

A number pattern may be represented as an equation in two variables, one variable for the position or term in the pattern (first, second, third, etcetera), and one variable for the value of the pattern in that position or term. Continuing the example, let the pattern be $2$, $4$, $6$, $8$..., let $n$ be the term of the pattern, and let $P_n$ be the value of the pattern in the term $n$, then $P_n = 2n$.

(Conjetura)
**Conjecture**: an unproven explanation of a pattern. For example, in the pattern $2$, $4$, $6$, $8$... the conjecture is that the value of the next term is $10$, and that the equation of this pattern is $P_n = 2n$ where $n$ is the term and $P_n$ is the pattern value of the term $n$. But it can happen that the value of the next term is not $10$ but another value, for example it could be $15$.

(Contraejemplo)
**Counterexample**: in a pattern, a counterexample is a pattern value that disproves a given conjecture. For example, in the pattern $2$, $4$, $6$, $8$..., if the conjecture is that the pattern value of the next term is $10$, then a counterexample would be that the pattern value of the next term was actually $15$, this disproves the conjecture.

(Razonamiento deductivo)
**Deductive reasoning**: deductive reasoning means reasoning on the basis of given facts. For example, let $p$, $q$ be two events, such that $p \to q$. Given the fact that $p$ happens, the conclusion is that $q$ happens or will happen. Concluding that $q$ happens is a deduction, because it's a conclusion that was arrived to by reasoning on the basis of the given facts $p$ and $p \to q$.

(Demostración por contradicción)
**Indirect proof**: type of proof of a conditional in which the consequent is negated, and by deduction a contradiction is found, which means that the consequent is true.

### Propositional logic (Lógica proposicional)

Propositional logic is a branch of logic that condenses events and logical statements into symbols to operate over them and create propositions, which are logical statements themselves. For example, let $p$, $q$ be two events or logical statements, then those symbols, $p$ and $q$, represent said events or logical statements. Logical operations can be made over $p$ and $q$.

(Valor de verdad de una proposición o evento)
**Truth value of a statement or event**: value that results from a statement, or that is assigned to an event. The value $1$ means true, and the value $0$ means false. An event can be assigned a truth value, $1$ if the event happens, and $0$ if the event does not happen. A statement results in a truth value, $1$ if the statement is true, and $0$ if the statement is false. For example let $p$ be the event 'I am healthy today', assigning it a truth value of $1$ means that $p$ happens, and assigning it a truth value of $0$ means that $p$ does not happen. Truth values are also called logical values (valores lógicos).

(Proposiciones condicionales)
**Conditional statements**: conditional statements are also called if-then statements, they are called in these ways because they put an event named conclusion (conclusión) to happen on the condition that another event named hypothesis (hipótesis) happens. In a conditional statement if the hypothesis happens then the conclusion happens. The hypothesis is also known as the antecedent (antecedente), and the conclusion is also known as the consequent (consecuente).

(Partes de una proposición condicional)
**Parts of a conditional statement**: a conditional statement has three parts, the hypothesis, the conclusion, and the connector between them. For example, let $p$, $q$ be two events, such that $p$ is the hypothesis of a conditional statement, and $q$ is the conclusion of the same conditional statement, then $p \to q$ denotes the conditional statement. It is read as if $p$ then $q$ (si $p$ entonces $q$), also read as $p$ implies $q$ ($p$ implica $q$).

For example, let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \to q$ means that 'if I am healthy today then I work today'.

(Negación lógica)
**Logical negation**: an operator used to negate an event. A negated event means that its negation happens. For example, let $p$ be an event, then its negation is $\neg p$. As a particular example of negation, let $p$ be the event 'I am healthy today', then $\neg p$ means the event 'I am not healthy today', which asserts that the negation of the event $p$ happens.

(Converso de una proposición)
**Converse of a statement**: the result of switching the order of the events of the statement. For example, let $p$, $q$ be two events, such that $p \to q$, then the converse is $q \to p$.

(Inverso de una proposición)
**Inverse of a statement**: the result of negating the events of the statement. For example, let $p$, $q$ be two events, such that $p \to q$, then the inverse is $\neg p \to \neg q$.

(Contrapositivo de una proposición | Contrarrecíproco de una proposición)
**Contrapositive of a statement**: the result of negating and switching the order of the events of the statement. For example, let $p$, $q$ be two events, such that $p \to q$, then the contrapositive is $\neg q \to \neg p$.

(Proposiciones lógicas equivalentes)
**Logically equivalent statements**: two distinct statements with the same events that lead to the same truth values. For example, let $p$, $q$ be two events, such that $p \to q$, then its contrapositive is logically equivalent, i.e. $\neg q \to \neg p$ has the same logical meaning as $p \to q$.

As a concrete example, let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \to q$ means that 'if I am healthy today then I work today'. On the other hand, $\neg q$ means 'I don't work today', and for this to happen, $\neg p$ 'I am not healthy today' must also happen, so $\neg q \to \neg p$.

The converse and the inverse of a conditional statement are not necessarily true. In the example, the converse $q \to p$ means 'if I work today, then I am healthy today', but this is not logically guaranteed, because it can be that 'I work today' and 'I am not healthy today'. The statement $p \to q$ does not invalidate the statement $\neg p \to q$, both can be true at the same time. For this same reason the inverse $\neg p \to \neg q$ is not necessarily true. Only the contrapositive of a conditional statement is logically equivalent to the conditional statement. But the converse and the inverse of a conditional statement are logically equivalent to each other as well, because one is the contrapositive of the other.

(Proposición bicondicional)
**Biconditional statement**: a logical statement with a hypothesis that conditionates a conclusion, in which the conclusion conditionates the hypothesis. In a biconditional statement, the conclusion can be used as the hypothesis, and the hypothesis can be used as the conclusion. For example, let $p$, $q$ be two events, such that each is a condition for the other to happen, then $p \leftrightarrow q$ denotes the biconditional statement. It is read as $p$ if and only if $q$ ($p$ sí y solo sí $q$).

The converse, inverse, and contrapositive of a biconditional statement are logically equivalent to each other. $p \leftrightarrow q$ implies $q \leftrightarrow p$ and also $\neg p \leftrightarrow \neg q$ and $\neg q \leftrightarrow \neg p$.

As a particular example, let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the biconditional statement $p \leftrightarrow q$ means that 'I am healthy today if and only if I work today'.

(Ley de separación)
**Law of detachment**: given two facts as true, that there exists a conditional statement and that the hypothesis of said conditional statement happens, the conclusion of the conditional statement can be deduced as a third true fact with no need for any other information. Let $p$, $q$ be two events, let $p$ be true, and let the conditional $p \to q$ be also true, then $q$ is true by deduction. The law of detachment is also known as modus ponendo ponens, which is latin for the mode that by affirming affirms.

The law of detachment is written as follows.
$$\begin{gathered}
p \to q\\
p\\
\therefore q
\end{gathered}$$

The $\therefore$ symbol is the therefore symbol, read as therefore (por lo tanto). The statements before the $\therefore$ are assumed true, and the statements after the $\therefore$ are deduced to be true.

(Ley contrarrecíproca)
**Law of contrapositive**: given two facts as true, that there exists a conditional statement and that the consecuent negated happens, then the negation of the antecedent can be deduced as a third true fact. Let $p$, $q$ be two events, let the conditional $p \to q$ be true and let $\neg q$ be also true, then $\neg p$ is true by deduction.

The law of contrapositive is written as follows.
$$\begin{gathered}
p \to q\\
\neg q\\
\therefore \neg p
\end{gathered}$$

This law is true because the contrapositive of a conditional is logically equivalent to said conditional.

(Ley del silogismo)
**Law of syllogism**: a chain of conditionals can be made, so that the consequent of one conditional is the antecedent of the next conditional. Given a chain of conditionals, one extra conditional can be deduced, namely if the first antecedent in the chain is true, then the last consequent in the chain is true.

The law of syllogism is written as follows.
Let $p$, $q$, $r$, $s$ events, then
$$\begin{gathered}
p \to q\\
q \to r\\
r \to s\\
\therefore p \to s
\end{gathered}$$

For that matter, several other conditionals could be deduced if needed, such as $p \to r$ and $q \to s$.

(Conjunción lógica)
**Logical conjunction**: the operation over two logical statements that returns a logical value of true if both logical statements are true. This is also known as the AND operation, because the first logical statement and the second must be true for the conjunction of them to be true. Let $p$, $q$ be two events, their conjunction is denoted as $p \land q$. The symbol $\land$ is the AND operator, $p \land q$ is read as $p$ and $q$ ($p$ y $q$).

(Disyunción lógica)
**Logical disjunction**: the operation over two logical statements that returns a logical value of true if either one or both logical statements are true. This is also known as the OR operation, because the first or the second logical statement or both can be true for the disjunction of them to be true. Let $p$, $q$ be two events, their disjunction is denoted as $p \lor q$. The symbol $\lor$ is the OR operator, $p \lor q$ is read as $p$ or $q$ ($p$ o $q$).

(Tablas de verdad)
**Truth tables**: tables made to organize the logical values of logical statements. They serve to compare side by side the logical values that result after applying different logical operators to logical statements and events. To indicate true and false, truth tables commonly use $1$ for true and $0$ for false, or also $T$ for true and $F$ for false. Truth tables consider all the possible combinations of logical values. 

The following is a truth table for the statement $p \land (\neg q \lor r)$.

| $p$ | $q$ | $r$ | $\neg q$ | $\neg q \lor r$ | $p \land (\neg q \lor r)$ |
| :-: | :-: | :-: | :------: | :-------------: | :-----------------------: |
| $1$ | $1$ | $1$ | $0$      | $1$             | $1$                       |
| $1$ | $1$ | $0$ | $0$      | $0$             | $0$                       |
| $1$ | $0$ | $1$ | $1$      | $1$             | $1$                       |
| $1$ | $0$ | $0$ | $1$      | $1$             | $1$                       |
| $0$ | $1$ | $1$ | $0$      | $1$             | $0$                       |
| $0$ | $1$ | $0$ | $0$      | $0$             | $0$                       |
| $0$ | $0$ | $1$ | $1$      | $1$             | $0$                       |
| $0$ | $0$ | $0$ | $1$      | $1$             | $0$                       |
*Truth table for the $p \land (\neg q \lor r)$ statement*

### Logic fallacies (Falacias lógicas)

(Falacia lógica)
**Logic fallacy**: a set of logical statements that are wrong or misconstrued.

(Falacia del converso)
**Fallacy of the converse**: also known as affirming the consequent (afirmación del consecuente), this fallacy states that given two true facts, a conditional statement and the consequent of said conditional, then the antecedent is deduced as being true.

Let $p$, $q$ be two events, then
$$\begin{gathered}
p \to q\\
q\\
\therefore p
\end{gathered}$$

These logical statements are wrong, because if $p \to q$ is true and $q$ is true, then $p$ may or may not be true. It could be the case that $\neg p \to q$.

## Algebra definitions (Definiciones de álgebra)

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

### Algebra theorems (Teoremas de álgebra)

(Teorema del producto cruzado)
**Cross product theorem | Cross-multiplication theorem**: Let $a$, $b$, $c$, $d$, be real numbers, with $b$ and $d$ being nonzero. If $\frac{a}{b} = \frac{c}{d}$, then $ad = bc$.

(Converso del teorema del producto cruzado)
**Converse of the cross product theorem**: Let $a$, $b$, $c$, $d$, be real numbers, with $b$ and $d$ being nonzero. If $ad = bc$, then $\frac{a}{b} = \frac{c}{d}$.

(Corolarios del teorema del producto cruzado y su converso)
**Corollaries of the cross product theorem and its converse**: the cross product theorem and its converse have a few corollaries as follows. Let $a$, $b$, $c$, $d$ be nonzero real numbers, then:

If $\frac{a}{b} = \frac{c}{d}$, then $\frac{a}{c} = \frac{b}{d}$.
If $\frac{a}{b} = \frac{c}{d}$, then $\frac{d}{b} = \frac{c}{a}$.
If $\frac{a}{b} = \frac{c}{d}$, then $\frac{d}{c} = \frac{b}{a}$.
If $\frac{a}{b} = \frac{c}{d}$, then $\frac{a + b}{b} = \frac{c + d}{d}$.
If $\frac{a}{b} = \frac{c}{d}$, then $\frac{b}{a} = \frac{d}{c}$, so $\frac{a + b}{a} = \frac{c + d}{c}$.
If $\frac{a}{b} = \frac{c}{d}$, then $\frac{a - b}{b} = \frac{c - d}{d}$.

More corollaries can be deduced by adding or subtracting different numbers from both sides, and inverting the results.

### Linear equations (Ecuaciones lineales)

A linear equation is an equation in which the variables have an exponent of $1$.

Linear equations can start with variable terms on both sides. When equations have variables and constants on both sides, the properties of equality can be used to move the variables and put them in one side if needed. For example, if a variable is dividing a number, it can be passed to the other side by using the multiplication property of equality, multiplying both sides by the variable.

(Lado para variables de una ecuación)
**Variable side of an equation**: A side of an equation that can be arbitrarily chosen to hold variables, or a single variable, in order to isolate it and find its value.

(Lado para constantes de una ecuación)
**Constant side of an equation**: The other side of an equation that is produced when choosing a variable side.

(Ecuación lineal en una variable)
**Linear equation in one variable**: linear equation in which there is only one variable. These equations can be simplified by using the properties of equality to create a variable side and a constant side.

Let $a$, $b$, be numbers, $x$ be a variable, then $a x = b$ is the basic form of a linear equation.

Every linear equation in one variable can be simplified through the use of the properties of equality, to leave it in the form $a x = b$. The side $a x$ is the variable side, and the side $b$ is the constant side.

(Combinar términos variables)
**Collect variable terms**: the process of combining the like terms of a variable in one side, this creates the variable side of the equation.

(Combinar términos constantes)
**Collect constant terms**: the process of combining like terms without variables, this creates the constant side of the equation.

(Ecuación lineal en dos variables)
**Linear equation in two variables**: linear equation with two variables, such that a change in one of the variables produces a proportional change in the other variable. For the standard form of a linear equation in two variables, let $A$, $B$, $C$, be constants, $x$, $y$, be variables, then $Ax + By = C$ is the standard form of the linear equation with variables $x$ and $y$. The amount of solutions of a linear equation is infinite, the line formed by the equation can be extended indefinitely.

(Pendiente de una ecuación lineal)
**Slope of a linear equation**: the slope of a line is a ratio that shows how many units in the $y$-axis change when a single unit in the $x$-axis changes. In a given line, the slope is measured as the value changed in the $y$-axis divided by the equivalent change in the $x$-axis.

The slope of an horizontal line is $0$ and the slope of a vertical line is undefined (positive or negative infinity). A negative slope means that whenever the value in the $x$-axis increases, the value in the $y$-axis decreases, and vice versa. A positive slope indicates that both values in $x$ and $y$ increase or decrease together.

(Fórmula de la pendiente)
**Slope formula**: the slope of a line that passes through two given points, is equal to the ratio of the difference of the $y$-axis values of the two points over the difference of the $x$-axis values of the two points. Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points in the $x$-$y$ plane, and let $m$ be the slope that they form, then $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{y_1 - y_2}{x_1 - x_2}$.

The rise (elevación) of a slope is the amount changed in the $y$ axis, namely $y_2 - y_1$. The run (avance) of a slope is the amount changed in the $x$ axis, namely $x_2 - x_1$. So the algebraic definition of the slope can also be interpreted as rise over run.

(Elevación sobre avance de una pendiente)
**Rise over run of a slope**: in a slope, rise over run is the fraction of the vertical distance called "rise" over the horizontal distance called "run".

(Forma pendiente intercepto de una línea)
**Slope-intercept form of a line**: an equation that expresses the $y$ coordinate of each point of a line, as the the slope multiplied by the $x$ coordinate of that point, plus the $y$-intercept. Let $y$ be the $y$ coordinate of a given point, let $x$ be the $x$ coordinate of the same point, let $m$ be the slope, $b$ be the $y$-intercept, then $y = mx + b$.

(Pendiente de líneas paralelas)
**Slope of parallel lines**: the slope of a set of parallel lines is the same for all the lines, i.e. all parallel lines have the same slope. This is because for lines to be parallel, they must have the same rise and run. Using the slope-intercept form of a line, parallel lines have the same slope but different $y$-intercept values.

(Pendiente de líneas perpendiculares)
**Slope of perpendicular lines**: given the slope $m$ of a line, the slope of a perpendicular line to it, is $-1/m$. This is because given the slope of a line, the slope of a line perpendicular to it, is the opposite reciprocal of the slope of the given line.

(Fórmula de distancia)
**Distance formula**: the distance formula is the application of the Pythagorean theorem in the rectangular coordinate system. Let $(x_1, y_1)$, $(x_2, y_2)$, be two points in the $x$-$y$ plane, and let $d$ be the distance between them, then $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.

(Distancia más corta entre un punto y una recta)
**Shortest distance between a point and a line**: given a point and a line, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line to the given line that passes through the given point, is used to measure this shortest distance, as the distance between the given point and the intersection of the perpendicular line and the given line.

(Distancia más corta entre dos líneas paralelas)
**Shortest distance between two parallel lines**: given two parallel lines, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line that passes through both parallel lines, is used to measure this shortest distance, as the distance between the two intersections of the perpendicular line with the two parallel lines. By definition of parallel lines, the shortest distance between them is a constant.

### Polynomials (Polinomios)

A polynomial is an expression of one or more terms added together. The terms may contain variables. If the only variable in a polynomial is $x$, the polynomial can be denoted as $p(x)$ or using other letters, as $q(x)$. For example $p(x) = x^2 + 5x^3 - 4x - 7$.

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

(Evaluación de polinomios)
**Polynomial evaluation**: polynomial evaluation is done like regular evaluation of expressions. For example, in $p(x) = 5x^3 + x^2 - 4x - 7$ evaluating $p(x)$ in $2$ gives $p(2) = 5(2)^3 + (2)^2 - 4(2) - 7 = 40 + 4 - 8 - 7 = 44 - 15 = 29$, so evaluating $p(x)$ in $2$ gives $29$.

#### Operations with polynomials (Operaciones con polinomios)

(Adición de polinomios)
**Addition of polynomials**: the operation of addition made with polynomials. Addition of polynomials is based on combining like terms, i.e. only the terms with the same variables and exponents are added together. For example, given $p(x) = 2x^3 + 4x - 7$ and $q(x) = 3x - 2$, then $p(x) + q(x) = 2x^3 + 7x - 9$.

(Sustracción de polinomios)
**Subtraction of polynomials**: the operation of subtraction made with polynomials. Subtraction of polynomials is bases on combining like terms, i.e. only the terms with the same variables and exponents can be subtracted from one another. For example, given $p(x) = 2x^3 + 4x - 7$ and $q(x) = 3x - 2$, then $p(x) - q(x) = 2x^3 + x - 5$.

(Multiplicación de monomios)
**Monomial multiplication**: let $a$, $b$, $k$, $l$, $m$, $n$, be numbers and $x$, $y$ be variables, then the product of the monomials $ax^ky^l$ and $bx^my^n$ is $abx^{k + m}y^{l + n}$.

(Multiplicación de polinomios)
**Multiplication of polynomials**: the multiplication of polynomials is based on the distributive property of multiplication over addition (and subtraction). In the product of two polynomials, each term of the first polynomial is multiplied by the second polynomial using the distributive property.

For example, given $p(x) = 2x^3 + 4x - 7$ and $q(x) = 3x - 2$, then $p(x)q(x) = (2x^3)(3x) + (2x^3)(-2) + (4x)(3x) + (4x)(-2) + (-7)(3x) + (-7)(-2) = 6x^4 - 4x^3 + 12x^2 - 8x - 21x + 14 = 6x^4 - 4x^3 + 12x^2 - 29x + 14$, so $p(x)q(x) = 6x^4 - 4x^3 + 12x^2 - 29x + 14$.

(División de monomios)
**Monomial division**: let $a$, $b$, $k$, $l$, $m$, $n$, be numbers and $x$, $y$ be variables, then the division of the monomial $ax^ky^l$ over $bx^my^n$ is $\frac{a}{b}x^{k - m}y^{l - n}$.

(División de polinomios)
**Division of polynomials**: this operation is done according to the degrees of the polynomials in the dividend and divisor. In a fraction of polynomials, if the degree of the numerator is less than the degree of the denominator, then that fraction can not be simplified further, i.e. it behaves as a proper fraction.

Long division of polynomials (División larga de polinomios) is a way to divide polynomials. With the polynomials in the fraction written in standard form, each individual term of the numerator from left to right is divided by the first term of the denominator, until the degree of the term being divided is less than the degree of the polynomial in the denominator.

In general, let $x$ be a variable, $p(x)$, $g(x)$ be the two polynomials being divided, let $q(x)$ be the quotient of the division, and $r(x)$ be the remainder, then $\frac{p(x)}{g(x)} = q(x) + \frac{r(x)}{g(x)}$.

For example, given $p(x) = 3x^2 + 7x + 4$ and $g(x) = x + 1$, then $\frac{p(x)}{g(x)} = \frac{3x^2 + 7x + 4}{x + 1}$. The first term in the quotient is $3x$ because $3x(x) = 3x^2$ which is the first term in the dividend. Multiplying $3x$ by the divisor and then subtracting the result from the dividend gives, $3x(x + 1) = 3x^2 + 3x$, $3x^2 + 7x + 4 - 3x^2 - 3x = 4x + 4$, now the current dividend is $4x + 4$. The second term in the quotient is $4$, because $4(x) = 4x$ which is the first term in the current dividend. Doing the same process as before gives, $4(x + 1) = 4x + 4$, $4x + 4 - 4x - 4 = 0$. A current dividend of $0$ means that the division is over, and this $0$ is the remainder of the division, and so $\frac{p(x)}{g(x)} = 4x + 4$.

(Factorización)
**Factoring**: the process of finding the factors of a product.

(Factorización de polinomios)
**Polynomial factoring**: factoring applied to a polynomial, treating the polynomial as the product. After doing polynomial factoring, a polynomial is represented as factors that are multiplying each other.

(Máximo factor común de dos expresiones)
**Greatest common factor of two expressions**: the largest expression that is a factor of the two given expressions. For example, given $3x^2 + 6x$ and $9x$, the greatest common factor is $3x$.

(Máximo factor común de un polinomio)
**Greatest common factor of a polynomial**: the largest expression that is a factor of all the terms in a given polynomial. For example, in $12x^2 + 24x$ the greatest common factor is $12x$.

## Geometry definitions (Definiciones de geometría)

Geometry (Geometría) means the study of figures and their spatial properties. Spatial refering to the space occupied by the figures, or their location with regards to one another.

(Postulado)
**Postulate**: the axioms of geometry, i.e. facts of geometry that are accepted as true. Postulates act as definitions.

(Figura)
**Figure**: a geometric object that occupies space.

(Diagrama)
**Diagram**: a picture or drawing used to show figures and their geometry.

(Forma de una figura)
**Shape of a figure**: the form of the figure.

(Tamaño de una figura)
**Size of a figure**: the amount of space occupied by the figure.

(Figuras similares | Figuras semejantes)
**Similar figures**: figures that have the same shape but not the same size. Similarity (semejanza) is denoted with the $\sim$ symbol. Let $Fig_1$ and $Fig_2$ represent two figures that are similar, this is written as $Fig_1 \sim Fig_2$. Similar figures have their corresponding angles congruent and their corresponding sides proportional.  This can be said as "corresponding sides of similar figures are proportional", and "corresponding angles of similar figures are congruent".

(Autosimilaridad)
**Self-similarity**: Self-similarity is a property of the figures in which a part of the figure has the same shape as the whole figure, which means that the part is similar to the whole, the figure is similar to itself.

(Fractales)
**Fractals**: figures that have infinite self-similarity, meaning that in a fractal, each part is similar to the whole, and then each part has subparts similar to the part, and each subpart has subsubparts similar to the subpart, and so on infinitely. Because of this, fractals can be created in iterations. The initial shape before the first iteration is called stage 0 (etapa 0), and then the result of each iteration is the respective stage.

(Factor de escala)
**Scale factor**: in two similar figures, the scale factor is the constant that allows getting one figure from the other. Multiplying each length of the first figure by the scale factor, results in the lengths of the second figure. Dividing each length of the second figure by the scale factor, results in the lengths of the first figure.

Let $Fig_1$ and $Fig_2$ be two similar figures, $Fig_1 \sim Fig_2$, let $A_1$ and $B_1$ be two points on $Fig_1$ that are correspondent to the points $A_2$ and $B_2$ on $Fig_2$, and let $k$ be the scale factor to obtain $Fig_2$ from $Fig_1$, then $A_2B_2 = k A_1B_1$.

(Figuras congruentes)
**Congruent figures**: figures that have the same shape and also the same size. Let $\overline{AB}$ be a segment, the congruence with itself is denoted as $\overline{AB} \cong \overline{BA}$. This symbol $\cong$ is used in general to indicate two congruent geometric figures.

(Figuras irregulares)
**Irregular figures**: irregular figures are figures whose shape is not a basic shape.

(Lados y ángulos correspondientes)
**Corresponding sides and angles**: in similar or congruent figures, the sides and angles that would be the same if replacing one figure for the other. The corresponding sides of two figures have the same ratio (which is $1$ for congruent figures), and their corresponding angles have the same value. Similar triangles are similar figures.

(Punto)
**Point**: a single piece of space that has no extension, i.e. a figure with zero dimensions. Points are used to indicate locations in space, they are represented with dots in diagrams. Points are commonly labeled using an uppercase letter, such as $A$, $B$, $C$, and $D$.

(Línea | Recta)
**Line**: a shape with infinite points that extends in a single dimension indefinitely. A line has no start nor ending, it has a given direction and a location in space. Lines are labeled using a single lowercase letter, such as $g$, or with the labels of two points on the line and a bidirectional arrow on top, such as $\overleftrightarrow{PQ}$ and $\overleftrightarrow{QP}$. All these three labels denote the same line.

(Plano)
**Plane**: a shape with infinite lines that extends in two dimensions (2D) indefinitely. A plane has no start nor ending, it has a given direction and a location in space. Planes are labeled using a single uppercase letter in a calligraphic font, such as $\mathcal{M}$. A plane can also be named with the labels of any three points on the plane, such as the plane $ABC$, or $BCA$, or $CAB$ or any other combination.

(Espacio tridimensional)
**3D space**: space in which the basic geometric shapes exist. Shapes in zero, one, or two dimensions, can be seen in 3D space. This space has three dimensions, it extends indefinitely in width, length, and height.

(Puntos colineales)
**Collinear points**: points that are on the same line. All the points on a given line are collinear.

(Puntos coplanares)
**Coplanar points**: points that are on the same plane. All the points on a given plane are coplanar.

(Punto equidistante a otros puntos)
**Equidistant point to other points**: a given point is equidistant to other points when its distance to all the other points is the same.

(Líneas coplanares)
**Coplanar lines**: lines that are on the same plane. All the lines on a given plane are coplanar.

(Segmento de línea)
**Line segment**: a truncated line that ends in both of its sides and does not extend indefinitely. The points where the line ends are called endpoints (puntos extremos). Line segments are labeled using its endpoints and a horizontal bar on top of them, such as $\overline{AB}$ and $\overline{BA}$. They can also be simply called segments.

(Rayo)
**Ray**: a line that is only truncated in one side, while the other side extends indefinitely. A ray has one endpoint. Rays are labeled using the endpoint and the point inside the ray with an arrow on top, such as $\overrightarrow{AB}$ and $\overleftarrow{BA}$. The arrow on top points in the same direction as the ray.

(Intersección)
**Intersection**: the point or points where two shapes cross each other. When two distinct lines intersect, the intersection is a point. When two distinct planes intersect, the intersection is a line. When a line outside of a plane intersects said plane, the intersection is a point. When three distinct planes intersect, the intersection is a point.

(Punto de concurrencia)
**Point of concurrency**: the intersection in a single point, of three or more lines, rays, or segments.

(Vértice)
**Vertex**: any point from which one or more lines stem.

(Ángulo)
**Angle**: in two lines (or segments, or rays) that share a vertex, the angle is the measure of rotation of one line to get to the other. If a vertex has only two lines, then an angle can be named after said vertex. Let $A$ be a vertex with two lines stemming from it, then $\angle A$ is the angle formed between the two lines, and $m \angle A$ is the measure of said angle. Angles are commonly shown in diagrams with an arc between the two lines.

If more than two lines stem from a vertex, then an unambiguous way to label an angle is using three points, the vertex and one point in each of the two lines in the angle. For example, given the vertex $A$, the point $B$ in one line, and the point $C$ in the other line, then the angle formed can be labeled as $\angle BAC$ or $\angle CAB$, putting the vertex $A$ in the middle.

Angles are commonly measured in degrees and in radians. In degrees a whole rotation that ends at the starting position is measured as $360 \text{\textdegree}$ read as $360$ degrees ($360$ grados), and in radians this is measured as $2 \pi$ read as $2 \pi$ radians ($2 \pi$ radianes). Given those measures, half a whole rotation is $180 \text{\textdegree}$ or $\pi$ radians.

An angle can be measured in two ways, because there are two ways in which a ray can be rotated to coincide with another (rotating the ray clockwise, and rotating the ray counterclockwise). The standard definition of the measure of an angle, is that it's the smallest measure of the two. The smallest measure of an angle is always less than or equal to half a circle, i.e. $180 \text{\textdegree}$ or $\pi$ radians. Still, angles greater than $\pi$ can be considered.

(Vértice de un ángulo)
**Vertex of an angle**: in an angle, the vertex is the endpoint where the two lines join. In the angle $\angle ABC$, the vertex is the point $B$.

(Lados de un ángulo)
**Sides of an angle**: each of the two lines that form the angle.

(Ángulo recto)
**Right angle**: the angle of a quarter of a circle, i.e. $90 \text{\textdegree}$ or $\pi/2$ radians. The arc between the rays that is used to denote a right angle is a small square instead of an arc.

(Líneas perpendiculares)
**Perpendicular lines**: two lines (or rays, or segments) that cross each other at right angles, i.e. the four angles formed at the intersection of the lines are right angles. Perpendicularity is denoted with the $\perp$ symbol, e.g. given two lines $l$ and $m$ that are perpendicular to each other, this is denoted as $l \perp m$, which is the same as $m \perp l$.

(Paralelismo en geometría)
**Geometric parallelism**: the relationship that is produced when two distinct figures extend indefinitely and never intersect each other. Two parallel lines that belong to the same plane, extend indefinitely and never intersect each other. Two parallel planes in space, extend indefinitely and never intersect each other. The distance between parallel lines or planes is constant. The symbol $\parallel$ indicates a parallel relation. Let $\overleftrightarrow{AB}$, $\overleftrightarrow{CD}$ be two lines, such that they are parallel to each other, this can be denoted as $\overleftrightarrow{AB} \parallel \overleftrightarrow{CD}$, read as the line $AB$ is parallel to the line $CD$ (la línea $AB$ es paralela a la línea $CD$). In diagrams, parallel lines are indicated by placing arrowheads inside the lines. Each set of parallel lines has its own amount of arrowheads.

(Propiedad transitiva de las líneas paralelas)
**Transitive property of parallel lines**: given two parallel lines, if the first one is parallel to a third line, then the second line is also parallel to the third, if $k \parallel l$ and $l \parallel m$, then $k \parallel m$.

(Líneas alabeadas)
**skew lines**: a relationship between two lines, such that they are not parallel but also do not intersect. This is possible in lines that belong to different planes.

(Línea transversal)
**Transversal line**: a line that intersects two other distinct lines.

(Partes de una transversal)
**Parts of a transversal**: a few named parts of transversals in general.

- **Interior area** (Área interna): the area between the two lines crossed by the transversal, e.g. the area between $l$ and $m$.

- **Exterior area** (Área externa): the area outside of the two lines crossed by the transversal, e.g. the area outside of $l$ and $m$.

- **Corresponding angles** (Ángulos correspondientes): two angles that are in the same position relative to the transversal, but each on a different line, e.g. $\angle 1$ and $\angle 5$ are corresponding angles, like $\angle 2$ and $\angle 6$, also $\angle 3$ and $\angle 7$, and lastly $\angle 4$ and $\angle 8$ form corresponding angle pairs.

- **Alternate interior angles** (Ángulos alternos internos): two angles that lie on the interior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 3$ and $\angle 6$ are alternate interior angles, like $\angle 4$ and $\angle 5$.

- **Alternate exterior angles** (Ángulos alternos externos): two angles that lie on the exterior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 1$ and $\angle 8$ are alternate exterior angles, like $\angle 2$ and $\angle 7$.

- **Same side interior angles** (Ángulos conjugados internos): two angles that lie on the interior area, are distinct, and are on the same side of the transversal, e.g. $\angle 3$ and $\angle 5$ are same side interior angles, like $\angle 4$ and $\angle 6$.

- **Same side exterior angles** (Ángulos conjugados externos): two angles that lie on the exterior area, are distinct, and are on the same side of the transversal, e.g. $\angle 1$ and $\angle 7$ are same side exterior angles, like $\angle 2$ and $\angle 8$.

- **Consecutive angles** (Ángulos consecutivos): same side angles are also known as consecutive angles.

(Proporcionalidad entre transversales)
**Transversal proportionality**: any set of parallel lines can be crossed by an infinite amount of transversals. The transversals are divided proportionally, so the segments formed by the intersections of each transversal with the parallels, are proportional to those of the other transversals. For example, given three parallels and two transversals, the first transversal with intersections $A$, $B$, and $C$, and the second transversal with intersections $D$, $E$, and $F$ respectively, then there are proportions between the corresponding segments created with the points $A$, $B$, $C$, and the points $D$, $E$, $F$, because of this, it can be said that the figure $ABC$ is similar to the figure $DEF$.

(Ángulo llano)
**Straight angle**: the angle of half a circle, i.e. $180 \text{\textdegree}$ or $\pi$ radians. Two rays that have this angle form a straight line.

(Rayos opuestos)
**Opposite rays**: two rays with a straight angle between them.

(Ángulo agudo)
**Acute angle**: an angle greater than or equal to $0 \text{\textdegree}$ ($0$ radians) and less than $90 \text{\textdegree}$ ($\pi/2$ radians).

(Ángulo obtuso)
**Obtuse angle**: an angle greater than $90 \text{\textdegree}$ ($\pi/2$ radians) and less than $180 \text{\textdegree}$ ($\pi$ radians).

(Ángulos suplementarios)
**Supplementary angles**: two angles that added together measure $180 \text{\textdegree}$ or $\pi$ radians. Each angle in this pair is the supplement (suplemento) of the other.

(Ángulos complementarios)
**Complementary angles**: two angles that added together measure $90 \text{\textdegree}$ or $\pi/2$ radians. Each angle in this pair is the complement (complemento) of the other.

(Vuelta completa)
**Full circle**: the angle measure of $2 \pi$ radians or $360 \text{\textdegree}$.

(Ángulos adyacentes)
**Adjacent angles**: two angles that have the same vertex and share one side, without overlapping each other, which means that only three rays are required to create two adjacent angles.

(Par lineal)
**Linear pair**: two adjacent angles such that the two non-shared sides form a straight line.

(Ángulos verticales)
**Vertical angles**: in the intersection of two lines, vertical angles are pairs of angles that are on opposite sides of the intersection.

(Ángulo comprendido entre dos lados)
**Included angle between two sides**: the angle between two given sides, is the included angle, so the sides must share a vertex, which is the vertex of the angle.

(Lado comprendido entre dos ángulos)
**Included side between two angles**: a side that is common to two differnt angles. The angles surround the side by placing themselves at each endpoint of the side.

(Bisectriz de un segmento)
**Segment bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in any angle.

(Mediatriz)
**Perpendicular bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in a perpendicular way.

(Bisectriz de un ángulo)
**Angle bisector**: a line, ray, or segment, that divides a given angle into two congruent angles, each with half the measure of the given angle. Given that the segment $\overline{AC}$ is the angle bisector of the angle $\angle DAB$, then $m \angle DAC = m \angle BAC$.

(Transformaciones geométricas)
**Geometric transformations**: procedures that take a figure and modify it in different ways. A transformed figure is commonly denoted by appending an apostrophe to its name, or the parts of its name. For example the figure $ABC$ can be transformed into the figure $A'B'C'$, read as figure $A$ prime $B$ prime $C$ prime (figura $A$ prima $B$ prima $C$ prima).

(Transformaciones rígidas)
**Rigid transformations**: geometric transformations over a figure, that do not change the size of the figure.

(Mapeo de un punto a otro)
**Mapping from a point to another**: mappings are a way to symbolize geometric transformations in the coordinate plane. Let the point $(x, y)$ be transformed into the point $(x', y')$, this can be denoted as $(x, y) \to (x', y')$, read as the point $(x, y)$ is mapped to $(x', y')$ (el punto $(x, y)$ es mapeado a $(x', y')$).

(Transformación de dilatación)
**Dilation transformation**: a non-rigid transformation that is used to increase or decrease the size of a figure, to 'dilate' it. The resulting figure of a dilation is similar to the original figure.

Dilations are defined with two parts, a center (centro) and an scale factor (factor de escala). The scale factor is defined the same as the definition already given (it's always greater than zero). The center is the point around which the dilation is performed, the point around which the scale factor is applied. This means that the farther away that the center of dilation is from the figure, the farther away that the resulting dilation is from the original.

(Dilatación de un punto)
**Point dilation**: the most basic dilation transformation. All dilations can be seen as point dilations applied to each point in a figure, and then connecting the dilated points with corresponding segments. Given a figure consisting of a single point $B$, and a center of dilation $A$, the dilation is a point $C$, such that $AC = k AB$.

(Dilataciones en el plano coordenado)
**Dilations in the coordinate plane**: a given 2D figure $Fig_1$ is composed of a set of points $(x, y)$ in the coordinate plane. Let $Fig_1$ be dilated with dilation center $C$ located at $(x_C, y_C)$, and scale factor $k$, into the dilation $Fig_1'$. The figure $Fig_1'$ is composed of a set of points $(x', y')$ in the coordinate plane, this can be denoted with the mapping $(x, y) \to (x', y')$. The point $(x', y')$ can be obtained from $C$ and $k$, as $(x', y') = (x_C + k (x - x_C), y_C + k (y - y_C))$. In the case where $C$ is the origin $(0, 0)$, the mapping becomes $(x', y') = (kx, ky)$.

(Medida lineal)
**Linear measure**: measure for length, like distances, width, height, depth, etcetera, in linear units (unidades lineales).

(Medida cuadrada)
**Square measure**: measure for area size, in square units (unidades cuadradas).

(Medida cúbica)
**Cubic measure**: measure for volume, in cubic units (unidades cúbicas).

(Distancia)
**Distance**: the length between two given points.

(Perímetro)
**Perimeter**: in a two dimensional shape, the measure of the distance around it.

(Área)
**Area**: in a two dimensional shape, the measure of the surface covered by it.

(Área superficial)
**Surface area**: in a three dimensional shape, the amount of area covered by its surface.

(Volumen)
**Volume**: in a three dimensional shape, the measure of the space occupied by it.

(Sólidos)
**Solids**: three dimensional shapes.

### Geometry postulates (Postulados de geometría)

(Postulado de línea)
**Unique line postulate**: given two points, only one line passes through the points. Given the points $A$ and $B$, they lie on the line $l$ that passes through them.

(Postulado de plano)
**Unique plane postulate**: given three non-collinear points, only one plane contains them. Given the points $A$, $B$, and $C$, they lie on the plane $\mathcal{M}$ that contains them.

(Postulado de plano línea)
**Plane-line postulate**: a line that connects points from a plane, is in the plane. If the line $l$ connects the points $A$ and $B$ in the plane $\mathcal{M}$, then $l$ lies on $\mathcal{M}$.

(Postulado de la intersección entre dos rectas)
**Line intersection postulate**: if two distinct lines intersect, then their intersection is a point. If the lines $l$ and $m$ intersect, then they intersect at a single point $A$.

(Postulado de la intersección entre dos planos)
**Plane intersection postulate**: if two distinct planes intersect, then their intersection is a line. If the planes $\mathcal{M}$ and $\mathcal{N}$ intersect, then they intersect at a single line $l$.

(Postulado de la regla)
**Ruler postulate**: when placing a ruler to measure the distance between two given points, said distance is the absolute value of the difference of the numbers of each point in the ruler. The distance between two points $A$ and $B$ is $B_value - A_value$, the subindex $value$ indicates that it's a measure, in this case a measure of the ruler.

(Postulado de adición de segmentos)
**Segment addition postulate**: given three collinear points with one point being between the other two (the endpoints), the measure of the distance between the endpoints, is equal to the sum of the distances of each endpoint to the point between them. Let $A$, $B$, and $C$, be three collinear points, with $B$ being between $A$ and $C$, then $AB + BC = AC$.

(Postulado del transportador)
**Protractor postulate**: when placing a protractor to measure the angle between two rays, said angle is the absolute value of the difference of the numbers of each ray in the protractor. The measure of the angle $\angle ABC$ is $BC_value - AB_value$, the subindex $value$ indicates that it's a measure, in this case a measure of the protractor at the segments $\overline{AB}$ and $\overline{BC}$.

(Postulado de adición de ángulos)
**Angle addition postulate**: given two angles that share a common ray and are adjacent, the measure of the angle between the two non common rays, is equal to the sum of the two angles given. Let $\overrightarrow{AD}$, $\overrightarrow{BD}$, and $\overrightarrow{CD}$, be three rays such that two angles are formed that share the common ray $\overrightarrow{BD}$, i.e. the angles $\angle ADB$ and $\angle CDB$, then $m \angle ADB + m \angle CDB = m \angle ADC$.

(Postulado del punto medio)
**Midpoint postulate**: a segment has exactly one midpoint. If the point $B$ is the midpoint of $\overline{AC}$, then $B$ is the only point that is the midpoint.

(Postulado de la mediatriz)
**Perpendicular bisector postulate**: a given segment has only one line that is its perpendicular bisector. Given $\overleftrightarrow{DE} \perp \overline{AC}$, $B$ lies in $\overleftrightarrow{DE}$, and $\overline{AB} \cong \overline{BC}$, then the line $\overleftrightarrow{DE}$ is the perpendicular bisector of $\overline{AC}$.

(Postulado de la bisectriz de un ángulo)
**Angle bisector postulate**: a given angle has only one line that is its angle bisector. A line $\overleftrightarrow{AC}$ is the angle bisector of the angle $\angle DAB$, given that $m \angle DAC = m \angle BAC$.

(Postulado del par lineal)
**Linear pair postulate**: the two angles of a linear pair are supplementary. If $\angle A$ and $\angle B$ form a linear pair, then $\angle A$ and $\angle B$ are supplementary.

(Postulado de las paralelas)
**Parallel postulate**: given a line and a point not on the line, there is only one parallel to the line that passes through the point. Given a line $l$ and a point $A$ that does not lie on $l$, then only one line $m$ passes through $A$ and $l \parallel m$.

(Postulado de las perpendiculares)
**Perpendicular postulate**: given a line and a point not on the line, there is only one perpendicular line to the line that passes through the point. Given a line $l$ and a point $A$ that does not lie on $l$, then only one line $m$ passes through $A$ and $l \perp m$.

(Postulado de los ángulos correspondientes)
**Corresponding angles postulate**: in a transversal of two parallels, the corresponding angles are congruent. If $l \parallel m$, with transversal $t$, the lines $l$ and $m$ are placed horizontally, and numerating the angles left to right and then top to bottom, then $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, and $\angle 4 \cong \angle 8$.

(Converso del postulado de los ángulos correspondientes)
**Converse of the corresponding angles postulate**: if the corresponding angles of a transversal are congruent, then the transversal is a transversal of two parallels. Using the same lines of the corresponding angles postulate, if $\angle 1 \cong \angle 5$, and/or $\angle 2 \cong \angle 6$, and/or $\angle 3 \cong \angle 7$, and/or $\angle 4 \cong \angle 8$, then $l \parallel m$, with transversal $t$.

(Postulado LLL de congruencia de triángulos)
**SSS triangle congruence postulate**: SSS stands for Side-Side-Side (Lado-Lado-Lado). This postulate says that two triangles with side-side-side of the same lengths, are congruent, i.e. if the three sides of a triangle are individually congruent to the three sides of another triangle, then the two triangles are congruent. Let $\triangle ABC$ have sides with measures $a$, $b$, $c$, and $\triangle DEF$ have sides with measures $d$, $e$, $f$. If $a = d$, $b = e$, and $c = f$, then $\triangle ABC \cong \triangle DEF$.

(Postulado LAL de congruencia de triángulos)
**SAS triangle congruence postulate**: SAS stands for Side-Angle-Side (Lado-Ángulo-Lado). This postulate says that if two sides and their included angle are individually congruent to two sides and their included angle of another triangle, then the two triangles are congruent. Let $\triangle ABC$ have two sides with measures $a$, $c$, and let their included angle measure $\beta$. Let $\triangle DEF$ have two sides with measures $d$, $f$, and let their included angle measure $\epsilon$. If $a = d$, $c = f$, and $\beta = \epsilon$, then $\triangle ABC \cong \triangle DEF$.

(Postulado ALA de congruencia de triángulos)
**ASA triangle congruence postulate**: ASA stands for Angle-Side-Angle (Ángulo-Lado-Ángulo). This postulate says that if two angles and their included side are individually congruent to two angles and their included side in another triangle, then the two triangles are congruent. Let $\triangle ABC$ have two angles with measures $\alpha$, $\gamma$, and let their included side measure $b$. Let $\triangle DEF$ have two angles with measures $\delta$, $\zeta$, and let their included side measure $e$. If $\alpha = \delta$, $\gamma = \zeta$, and $b = e$, then $\triangle ABC = \triangle DEF$.

(Postulado AA de semejanza de triángulos)
**AA triangle similarity postulate**: given two triangles, if the first triangle has two angles that are congruent to the corresponding angles in the second triangle, then the triangles are similar. Given two triangles $\triangle ABC$ and $\triangle DEF$, if $\angle A \cong \angle D$ and $\angle B \cong \angle E$, or if $\angle A \cong \angle D$ and $\angle C \cong \angle F$, or if $\angle B \cong \angle E$ and $\angle C \cong \angle F$, then $\triangle ABC \sim \triangle DEF$.

(Propiedad reflexiva de la congruencia)
**Reflexive property of congruence**: a figure is congruent with itself. Given $\overline{AB}$, and $\angle ABC$, then $\overline{AB} \cong \overline{AB}$ and $\angle ABC \cong \angle ABC$.

(Propiedad simétrica de la congruencia)
**Symmetric property of congruence**: if a first figure is congruent to a second, then the second figure is congruent to the first. Let $\overline{AB}$, $\overline{CD}$ be segments, if $\overline{AB} \cong \overline{CD}$ then $\overline{CD} \cong \overline{AB}$.

(Propiedad transitiva de la congruencia)
**Transitive property of congruence**: if a first figure is congruent to a second, and the second figure is congruent to a third, then the third figure is congruent to the first. Let $\overline{AB}$, $\overline{CD}$, $\overline{EF}$ be segments, if $\overline{AB} \cong \overline{CD}$ and $\overline{CD} \cong \overline{EF}$ then $\overline{AB} \cong \overline{EF}$.

### Geometry theorems (Teoremas de geometría)

(Teorema del ángulo recto)
**Right angle theorem**: all right angles are congruent. If $\angle A$ and $\angle B$ are right angles, then $\angle A \cong \angle B$.

(Teorema de los ángulos verticales)
**Vertical angles theorem**: two angles that are vertical angles, are also congruent. If $\angle A$ and $\angle B$ are vertical angles, then $\angle A \cong \angle B$.

(Teorema de los pares lineales congruentes)
**Congruent linear pairs theorem**: in a linear pair, if the two angles are congruent, then they have a measure of $\pi/2$, meaning that if both angles of a linear pair are congruent then they are right angles. If $\angle A$ and $\angle B$ form a linear pair, and $\angle A \cong \angle B$, then $\angle A$ and $\angle B$ are right angles.

(Teorema de los suplementos congruentes)
**Congruent supplements theorem**: two angles are congruent when they are supplementary to another angle, or when they are supplementary to two other congruent angles. If $\angle A$ and $\angle C$ are supplements of $\angle B$, then $\angle A \cong \angle C$.

(Converso del teorema de los suplementos congruentes)
**Converse of the congruent supplements theorem**: if two angles are congruent, and one of them is supplementary to a third angle, then both angles are supplementary to the third angle. If $\angle A \cong \angle C$, and $\angle A$ and $\angle B$ are supplementary, then $\angle B$ and $\angle C$ are supplementary.

(Teorema de los complementos congruentes)
**Congruent complements theorem**: two angles are congruent when they are complementary to another angle, or when they are complementary to two other congruent angles. If $\angle A$ and $\angle C$ are complements of $\angle B$, then $\angle A \cong \angle C$.

(Teorema de los ángulos complementarios adyacentes)
**Adjacent complementary angles theorem**: if two angles are adjacent and complementary, then the two non-shared sides form a right angle. If $\angle A$ and $\angle B$ are adjacent complementary angles, then $m \angle A + m \angle B = \pi/2$, so the angle between the non-shared sides is a right angle.

(Converso del teorema de los ángulos complementarios adyacentes)
**Converse of the adjacent complementary angles theorem**: if the non-shared sides of two adjacent angles form a right angle, then the angles are complementary. If $\angle A$ and $\angle B$ are adjacent angles, with the non-shared sides forming a right angle, then $\angle A$ and $\angle B$ are complementary.

(Teorema de la mediatriz)
**Perpendicular bisector theorem**: given a segment and its perpendicular bisector, any point in the perpendicular bisector is equidistant to both endpoints of the segment. If $\overline{CD}$ is a perpendicular bisector of $\overline{AB}$, and $E$ is any point that lies on $\overline{CD}$, then $\overline{AE} \cong \overline{EB}$.

(Converso del teorema de la mediatriz)
**Converse of the perpendicular bisector theorem**: given a segment, any point equidistant to both endpoints, is in the perpendicular bisector of the segment. If $\overline{AC} \cong \overline{BC}$, and $D$ is the midpoint of $\overline{AB}$, then $\overline{CD}$ is a perpendicular bisector of $\overline{AB}$.

(Teorema de la equidistancia en la bisectriz de un ángulo)
**Equidistance in an angle bisector theorem**: given an angle, any point in its angle bisector is equidistant to the sides of the angle, using the shortest distance between the point and the sides. If $\overline{BD}$ is an angle bisector of $\angle ABC$, the distance from $D$ to $\overline{AB}$ creates the segment $\overline{DE}$, and the distance from $D$ to $\overline{BC}$ creates the segment $\overline{DF}$, then $\overline{DE} \cong \overline{DF}$.

(Converso del teorema de la equidistancia en la bisectriz de un ángulo)
**Converse of the equidistance in an angle bisector theorem**: in an angle, if a given point is equidistant to the sides of the angle, using the shortest distance between the point and the sides, then the point lies in the angle bisector. In angle $\angle ABC$, given a point $D$, the distance from $D$ to $\overline{AB}$ creates the segment $\overline{DE}$, and the distance from $D$ to $\overline{BC}$ creates the segment $\overline{DF}$, if $\overline{DE} \cong \overline{DF}$, then $\overline{BD}$ is an angle bisector of $\angle ABC$.

(Teorema de los ángulos alternos internos)
**Alternate interior angles theorem**: two parallel lines that are intersected by a transversal, have their alternate interior angles congruent. If $l \parallel m$, with transversal $t$, the lines $l$ and $m$ are placed horizontally, and numerating the angles left to right and then top to bottom, then $\angle 3 \cong \angle 6$ and $\angle 4 \cong \angle 5$.

(Converso del teorema de los ángulos alternos internos)
**Converse of the alternate interior angles theorem**: given two lines intersected by a transversal, if their alternate interior angles are congruent, then the two lines are parallel. Using the same lines of the alternate interior angles theorem, if $\angle 3 \cong \angle 6$ and/or $\angle 4 \cong \angle 5$, then $l \parallel m$, with transversal $t$.

(Teorema de los ángulos alternos externos)
**Alternate exterior angles theorem**: two parallel lines that are intersected by a transversal, have their alternate exterior angles congruent. Using the same lines of the alternate interior angles theorem, then $\angle 1 \cong \angle 8$ and $\angle 2 \cong \angle 7$.

(Converso del teorema de los ángulos alternos externos)
**Converse of the alternate exterior angles theorem**: given two lines intersected by a transversal, if their alternate exterior angles are congruent, then the two lines are parallel. Using the same lines of the alternate interior angles theorem, if $\angle 1 \cong \angle 8$ and/or $\angle 2 \cong \angle 7$, then $l \parallel m$, with transversal $t$.

(Teorema de los ángulos conjugados internos)
**Same side interior angles theorem**: two parallel lines that are intersected by a transversal, have supplementary same side interior angles. Using the same lines of the alternate interior angles theorem, then $\angle 3$ and $\angle 5$ are supplementary, and $\angle 4$ and $\angle 6$ are supplementary.

(Converso del teorema de los ángulos conjugados internos)
**Converse of the same side interior angles theorem**: given two lines intersected by a transversal, if their same side interior angles are supplementary, then the two lines are parallel. Using the same lines of the alternate interior angles theorem, if $\angle 3$ and $\angle 5$ are supplementary, and $\angle 4$ and $\angle 6$ are supplementary, then $l \parallel m$, with transversal $t$.

(Teorema de los ángulos conjugados externos)
**Same side exterior angles theorem**: two parallel lines that are intersected by a transversal, have supplementary same side exterior angles. Using the same lines of the alternate interior angles theorem, then $\angle 1$ and $\angle 7$ are supplementary, and $\angle 2$ and $\angle 8$ are supplementary.

(Converso del teorema de los ángulos conjugados externos)
**Converse of the same side exterior angles theorem**: given two lines intersected by a transversal, if their same side exterior angles are supplementary, then the two lines are parallel. Using the same lines of the alternate interior angles theorem, if $\angle 1$ and $\angle 7$ are supplementary, and/or $\angle 2$ and $\angle 8$ are supplementary, then $l \parallel m$, with transversal $t$.

(Teorema de las transversales perpendiculares)
**Perpendicular transversals theorem**: given three lines, if the first and second lines are parallel, and the first line is perpendicular to the third line, then the second line is also perpendicular to the third line. If $l \parallel m$ and $l \perp t$, then $m \perp t$.

(Converso del teorema de las transversales perpendiculares)
**Converse of the perpendicular transversals theorem**: if a first line and a second line are perpendicular to a third line, then the first and second lines are parallel. If $l \perp t$ and $m \perp t$, then $l \parallel m$.

(Teorema de la proporcionalidad entre transversales)
**Transversal proportionality theorem**: given a set of parallel lines, and a set of transversals to the parallels, the transversals are divided proportionally by the parallels, so the segments formed by the intersections of each transversal with the parallels, are proportional to those of the other transversals. Given a set of $m$ parallel lines $l_1$, $l_2$, ..., $l_m$, and a set of $n$ transversals to the parallels $t_1$, $t_2$, ..., $t_n$, the intersections of each transversal with the parallels form $m - 1$ segments. Let $d_{i, j}$ indicate the length of the segment in the transversal $t_i$, between the parallels $l_j$ and $l_{j + 1}$ (so that $j$ can go up to $m - 1$), then $\frac{d_{i1, j1}}{d_{i1, j2}} = \frac{d_{i2, j1}}{d_{i2, j2}}$ for all the possible values of $i$ and $j$ ($i1$ and $i2$ indicate two different values of $i$, the same for $j1$ and $j2$ which are different values of $j$).

(Teorema de la suma de los ángulos interiores de un triángulo)
**Triangle interior angles sum theorem**: the sum of the interior angles of a triangle, is exactly $\pi$. In $\triangle ABC$, $m \angle A + m \angle B + m \angle C = \pi$

(Teorema de la suma de los ángulos exteriores de un triángulo)
**Triangle exterior angle sum theorem**: the sum of the exterior angles of a triangle is exactly $2 \pi$, taking only one exterior angle per vertex. In $\triangle ABC$, $m \angle A_{ext} + m \angle B_{ext} + m \angle C_{ext} = 2 \pi$. The $ext$ subindex indicates an exterior angle.

(Teorema del ángulo exterior de un triángulo)
**Exterior angle of a triangle theorem**: in a triangle, the measure of an exterior angle is equal to the sum of the measures of its two remote interior angles. In $\triangle ABC$, $m \angle A_{ext} = m \angle B + m \angle C$.

(Teorema del tercer ángulo)
**Third angle theorem**: given two triangles, if two pairs of angles are congruent, then the third pair of angles is congruent. In the triangles $\triangle ABC$ and $\triangle DEF$ if $\angle A \cong \angle D$ and $\angle B \cong \angle E$, then $\angle C \cong \angle F$.

(Teorema AAL de congruencia de triángulos)
**AAS triangle congruence theorem**: AAS stands for Angle-Angle-Side (Ángulo-Ángulo-Lado). This theorem says that if two angles and one of their non included sides are individually congruent to two angles and one of their non included sides in another triangle, then the two triangles are congruent. This result is equivalent for an SAA configuration. In the triangles $\triangle ABC$ and $\triangle DEF$, if $\angle A \cong \angle D$, $\angle B \cong \angle E$, and $\overline{BC} \cong \overline{EF}$, then $\triangle ABC \cong \triangle DEF$.

(Teorema de la congruencia de la hipotenusa-cateto)
**Hypotenuse-leg congruence theorem**: given two right triangles, if the hypotenuse and one leg in one triangle, are congruent to the hypotenuse and one leg in the other triangle, then the two triangles are congruent. In right triangles $\triangle ABC$ and $\triangle DEF$, if the hypotenuses are congruent $\overline{AC} \cong \overline{DF}$ and two corresponding legs are congruent $\overline{AB} \cong \overline{DE}$, then $\triangle ABC \cong \triangle DEF$.

(Teorema LLL de semejanza de triángulos)
**SSS triangle similarity theorem**: given two triangles, if the sides of the first triangle have each the same ratio to the corresponding sides of the second triangle, then the triangles are similar. Given two triangles $\triangle ABC$ and $\triangle DEF$, and given a scale factor $k$, if $k = \frac{DE}{AB} = \frac{DF}{AC} = \frac{EF}{BC}$, then $\triangle ABC \sim \triangle DEF$.

(Teorema LAL de semejanza de triángulos)
**SAS triangle similarity theorem**: given two triangles, if two sides of the first triangle have each the same ratio to the corresponding sides of the second triangle, and the included angles of the given sides are congruent in both triangles, then the triangles are similar. Given two triangles $\triangle ABC$ and $\triangle DEF$, and given a scale factor $k$, if $k = \frac{DE}{AB} = \frac{DF}{AC}$, and $\angle A \cong \angle D$, then $\triangle ABC \sim \triangle DEF$.

(Teorema de los ángulos de la base)
**Base angles theorem**: in an isosceles triangle, the base angles are congruent. In an isosceles triangle $\triangle ABC$, such that $\overline{AB} \cong \overline{BC}$, then $\angle A \cong \angle C$.

(Converso del teorema de los ángulos de la base)
**Converse of the base angles theorem**: if two angles in a triangle are congruent, it is an isosceles triangle. In a triangle $\triangle ABC$, if $\angle A \cong \angle C$, then $\triangle ABC$ is isosceles.

(Teorema del triángulo isósceles)
**Isosceles triangle theorem**: in an isosceles triangle, the angle bisector of the vertex angle is a perpendicular bisector of the base. If $\triangle ABC$ is isosceles, such that $\overline{AB} \cong \overline{BC}$, $D$ is a point in $\overline{AC}$, and $\overline{BD}$ is the angle bisector of $\angle ABC$, then $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$.

(Converso del teorema del triángulo isósceles)
**Converse of the isosceles triangle theorem**: in an isosceles triangle, the perpendicular bisector of the base is an angle bisector of the vertex angle. If $\triangle ABC$ is isosceles, $D$ is a point in $\overline{AC}$, and $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$, then $\overline{BD}$ is an angle bisector of $\angle ABC$.

(Teorema de los triángulos equiláteros)
**Equilateral triangles theorem**: an equilateral triangle is also equiangular. If a triangle $\triangle ABC$ has sides with measures $a$, $b$, $c$, such that $a = b = c$, then $\angle A \cong \angle B \cong \angle C$.

(Converso del teorema de los triángulos equiláteros)
**Converse of the equilateral triangles theorem**: an equiangular triangle is also equilateral. If a triangle $\triangle ABC$ has $\angle A \cong \angle B \cong \angle C$, then its measures $a$, $b$, $c$ are equal, $a = b = c$.

(Teorema del segmento medio de un triángulo)
**Midsegment of a triangle theorem**: a midsegment of a triangle measures half the length of its parallel side. In a triangle $\triangle ABC$, if $\overline{DE}$ is a midsegment of $\triangle ABC$ that is parallel to $\overline{AB}$, then the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$, or $DE = \frac{AB}{2}$.

(Converso del teorema del segmento medio de un triángulo)
**Converse of the midsegment of a triangle theorem**: in a triangle, if a segment connects two sides, is parallel to the non-connected side, and measures half the length of its parallel side, then the segment is a midsegment of the triangle. In a triangle $\triangle ABC$, if the points $D$ and $E$ lie on different sides of the triangle, $\overline{DE} \parallel \overline{AB}$, and $DE = \frac{AB}{2}$, then $\overline{DE}$ is a midsegment of $\triangle ABC$.

(Teorema de la concurrencia de las mediatrices de un triángulo)
**Concurrency of the perpendicular bisectors of a triangle theorem**: in a triangle, the three perpendicular bisectors, one from each side, intersect each other at a single point which is the circumcenter. In a triangle $\triangle ABC$, there is a point $G$, such that $G$ is in the three perpendicular bisectors from the three sides of the triangle, $G$ is equidistant to $A$, $B$, $C$, and $G$ is the circumcenter of $\triangle ABC$.

(Teorema de la concurrencia de las bisectrices de los ángulos de un triángulo)
**Concurrency of the angle bisectors of a triangle theorem**: in a triangle, the three angle bisectors, one from each vertex, intersect each other at a single point which is the incenter. In a triangle $\triangle ABC$, if a point $G$ lies in the three angle bisectors of $\triangle ABC$ then $G$ is the incenter of $\triangle ABC$.

(Teorema de la concurrencia de las medianas de un triángulo)
**Concurrency of the medians of a triangle theorem**: in a triangle, the three medians, one from each vertex to the midpoint of the side opposite to the vertex, intersect each other at a single point which is the centroid. In any given median, the length from the centroid to the vertex is twice the length from the centroid to the midpoint. In a triangle $\triangle ABC$, if a point $G$ lies in the three medians of $\triangle ABC$ then $G$ is the centroid of $\triangle ABC$. If $D$ is the midpoint of $\overline{AC}$, $E$ is the midpoint of $\overline{BC}$, and $F$ is the midpoint of $\overline{AB}$, then $AG = 2 EG$, $BG = 2 DG$, and $CG = 2 FG$.

(Teorema del lado mayor de un triángulo)
**Triangle longer side theorem**: in a triangle, given two sides, if one side is longer than the other side, then the angle opposite to the longer side is greater than the angle opposite to the other side. In a triangle $\triangle ABC$, if $CB > AC$, then $m \angle A > m \angle B$.

(Converso del teorema del lado mayor de un triángulo)
**Converse of the triangle longer side theorem**: in a triangle, given two angles, if the measure of one angle is greater than the measure of the other angle, then the side opposite to the greater angle is longer than the side opposite to the other angle. In a triangle $\triangle ABC$, if $m \angle A > m \angle B$, then $CB > AC$.

(Teorema de la desigualdad del triángulo)
**Triangle inequality theorem**: in a triangle, the sum of the lengths of any two sides, is greater than the length of the remaining side. In a triangle $\triangle ABC$ that has sides with lengths $a$, $b$, $c$, the following relation is true, $|a - b| < c < a + b$, which is equivalent to $c < a + b$, $b < a + c$, and $a < b + c$.

(Teorema de la bisagra)
**Hinge theorem**: given two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the included angle from the first triangle has a measure greater than the one from the second triangle, then the remaining side of the first triangle is longer than the one of the second triangle. In the triangles $\triangle ABC$ and $\triangle DEF$, if $AB = DE$, $BC = EF$, and $m \angle B > m \angle E$, then $AC > DF$.

(Converso del teorema de la bisagra)
**Converse of the hinge theorem**: given two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the remaining side of the first triangle is longer than the one of the second triangle, then the included angle from the first triangle has a measure greater than the one from the second triangle. In the triangles $\triangle ABC$ and $\triangle DEF$, if $AB = DE$, $BC = EF$, and $AC > DF$, then $m \angle B > m \angle E$.

(Corolario del teorema de la bisagra)
**Corollary of the hinge theorem**: in two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the included angle from the first triangle is congruent to the one from the second triangle, then the remaining side of the first triangle is congruent to the one of the second triangle. In the triangles $\triangle ABC$ and $\triangle DEF$, if $AB = DE$, $BC = EF$, and $\angle B \cong \angle E$, then $AC = DF$.

(Teorema de la proporcionalidad entre triángulos)
**Triangle proportionality theorem**: in a triangle, any parallel line to one of the sides of the triangle, that intersects the other two sides, divides these other two sides proportionally. In a triangle $\triangle ADE$, if a point $B$ lies in $\overline{AD}$, a point $C$ lies in $\overline{AE}$, and $\overline{BC} \parallel \overline{DE}$, then $\overline{BC}$ divides $\overline{AD}$ and $\overline{AE}$ proportionally, meaning that a proportion is created, $\frac{BD}{AB} = \frac{CE}{AC}$. Many other proportions can be derived with the corollaries of the cross product theorem and its converse.

(Converso del teorema de la proporcionalidad entre triángulos)
**Converse of the triangle proportionality theorem**: in a triangle, if a given segment divides two sides proportionally, then the segment is parallel to the other side. In a triangle $\triangle ADE$, if a segment $\overline{BC}$ divides $\overline{AD}$ and $\overline{AE}$ proportionally, then $\overline{BC} \parallel \overline{DE}$.

(Teorema de la proporcionalidad en la bisectriz de un ángulo)
**Proportionality in an angle bisector theorem**: in a triangle, the angle bisector of any one of its angles creates a proportion. The angle bisector in a triangle, cuts the opposite side to the angle into two segments. The proportion created is that the first segment cut is to the second segment cut as the first side of the angle is to the second side of the angle bisected. In this definition, the first side can be any of the two sides of the angle, what matters is that the first segment cut is on the same side of the angle bisector as the first side of the angle, and the same for the second segment cut.

In a triangle $\triangle ABC$, the angle bisector of $\angle B$ intersects the side $\overline{AC}$ at a point $D$. This creates the proportion $\frac{AD}{CD} = \frac{AB}{BC}$.

(Teorema de la suma de los ángulos interiores de un polígono)
**Polygon interior angles sum theorem**: the sum of the interior angles of a polygon, is $\pi$ times the number of unique triangles in which the polygon can be divided, which is the same as $\pi$ times the number of vertices minus $2$. Let $Ang_{int}$ be the sum of the interior angles of a polygon, and let $n$ be the number of vertices in the polygon, then $Ang_{int} = \pi(n - 2)$.

(Teorema de la suma de los ángulos exteriores de un polígono)
**Polygon exterior angle sum theorem**: the sum of the exterior angles of a polygon is exactly $2 \pi$, taking only one exterior angle per vertex. Let $Ang_{ext}$ be the sum of the exterior angles of a polygon, and let $n$ be the number of vertices in the polygon, then $Ang_{ext} = 2 \pi$.

(Teorema de los lados opuestos de un paralelogramo)
**Opposite sides of a parallelogram theorem**: in a parallelogram, the opposite sides are congruent. In a parallelogram $ABCD$, $\overline{AB} \cong \overline{CD}$, and $\overline{AD} \cong \overline{BC}$.

(Converso del teorema de los lados opuestos de un paralelogramo)
**Converse of the opposite sides of a parallelogram theorem**: in a quadrilateral, if the opposite sides are congruent, then the quadrilateral is a parallelogram. In a quadrilateral $ABCD$, if $\overline{AB} \cong \overline{CD}$, and $\overline{AD} \cong \overline{BC}$, then $ABCD$ is a parallelogram.

(Teorema de los ángulos opuestos de un paralelogramo)
**Opposite angles of a parallelogram theorem**: in a parallelogram, the opposite angles are congruent. In a parallelogram $ABCD$, $\angle A \cong \angle C$, and $\angle B \cong \angle D$.

(Converso del teorema de los ángulos opuestos de un paralelogramo)
**Converse of the opposite angles of a parallelogram theorem**: in a quadrilateral, if the opposite angles are congruent, then the quadrilateral is a parallelogram. In a quadrilateral $ABCD$, if $\angle A \cong \angle C$, and $\angle B \cong \angle D$, then $ABCD$ is a parallelogram.

(Teorema de los ángulos consecutivos de un paralelogramo)
**Consecutive angles of a parallelogram theorem**: in a parallelogram, the consecutive angles are supplementary. In a parallelogram $ABCD$, $\angle A$ and $\angle B$ are supplementary, $\angle B$ and $\angle C$ are supplementary, $\angle C$ and $\angle D$ are supplementary, and $\angle A$ and $\angle D$ are supplementary.

(Converso del teorema de los ángulos consecutivos de un paralelogramo)
**Converse of the consecutive angles of a parallelogram theorem**: in a quadrilateral, if the consecutive angles are supplementary, then the quadrilateral is a parallelogram. In a quadrilateral $ABCD$, if $\angle A$ and $\angle B$ are supplementary, $\angle B$ and $\angle C$ are supplementary, $\angle C$ and $\angle D$ are supplementary, and $\angle A$ and $\angle D$ are supplementary, then $ABCD$ is a parallelogram.

(Teorema de las diagonales de un paralelogramo)
**Diagonals of a parallelogram theorem**: in a parallelogram, the two diagonals bisect each other. In a parallelogram $ABCD$, $\overline{AC}$, and $\overline{BD}$ bisect each other.

(Converso del teorema de las diagonales de un paralelogramo)
**Converse of the diagonals of a parallelogram theorem**: in a quadrilateral, if the two diagonals bisect each other, then the quadrilateral is a parallelogram. In a quadrilateral $ABCD$, if $\overline{AC}$, and $\overline{BD}$ bisect each other, then $ABCD$ is a parallelogram.

(Teorema de los lados opuestos paralelos y congruentes de un cuadrilátero)
**Parallel and congruent opposite sides of a quadrilateral theorem**: in a quadrilateral, if a single pair of opposite sides is congruent and parallel, then the quadrilateral is a parallelogram. In a quadrilateral $ABCD$, if $\overline{AB} \parallel \overline{CD}$ and $\overline{AB} \cong \overline{CD}$, then $ABCD$ is a parallelogram.

(Teorema de las diagonales de un rectángulo)
**Diagonals of a rectangle theorem**: in a rectangle, the diagonals are congruent. In a rectangle $ABCD$, $\overline{AC} \cong \overline{BD}$.

(Converso del teorema de las diagonales de un rectángulo)
**Converse of the diagonals of a rectangle theorem**: in a parallelogram, if the diagonals are congruent, then the parallelogram is a rectangle. In a parallelogram $ABCD$, if $\overline{AC} \cong \overline{BD}$, then $ABCD$ is a rectangle.

(Teorema de las diagonales perpendiculares de un rombo)
**Perpendicular diagonals of a rhombus theorem**: in a rhombus, the diagonals are perpendicular. In a rhombus $ABCD$, $\overline{AC} \perp \overline{BD}$.

(Converso del teorema de las diagonales perpendiculares de un rombo)
**Converse of the perpendicular diagonals of a rhombus theorem**: in a parallelogram, if the diagonals are perpendicular, then the parallelogram is a rhombus. In a parallelogram $ABCD$, if $\overline{AC} \perp \overline{BD}$, then $ABCD$ is a rhombus.

(Teorema de los ángulos bisecados de un rombo)
**Bisected angles of a rhombus theorem**: in a rhombus, the diagonals are angle bisectors of the interior angles of the rhombus. In a rhombus $ABCD$, $\overline{AC}$ is an angle bisector of $\angle A$ and $\angle C$, and $\overline{BD}$ is an angle bisector of $\angle B$ and $\angle D$.

(Converso del teorema de los ángulos bisecados de un rombo)
**Converse of the bisected angles of a rhombus theorem**: in a parallelogram, if the diagonals bisect the interior angles, then the parallelogram is a rhombus. In a parallelogram $ABCD$, if $\overline{AC}$ is an angle bisector of $\angle A$ and $\angle C$, and $\overline{BD}$ is an angle bisector of $\angle B$ and $\angle D$, then $ABCD$ is a rhombus.

(Teorema de los ángulos de las bases de un trapecio isósceles)
**Bases angles of an isosceles trapezoid theorem**: in an isosceles trapezoid, the long base angles are congruent, and the short base angles are congruent. In an isosceles trapezoid $ABCD$, $\angle A \cong \angle B$ and $\angle C \cong \angle D$.

(Converso del teorema de los ángulos de las bases de un trapecio isósceles)
**Converse of the bases angles of an isosceles trapezoid theorem**: in a trapezoid, if the two angles in each of the parallel sides are congruent, then the trapezoid is an isosceles trapezoid. In a trapezoid $ABCD$, if $\angle A \cong \angle B$ and $\angle C \cong \angle D$, then $ABCD$ is an isosceles trapezoid.

(Teorema de las diagonales de un trapecio isósceles)
**Diagonals of an isosceles trapezoid theorem**: in an isosceles trapezoid, the diagonals are congruent. In an isosceles trapezoid $ABCD$, $\overline{AC} \cong \overline{BD}$.

(Converso del teorema de las diagonales de un trapecio isósceles)
**Converse of the diagonals of an isosceles trapezoid theorem**: in a trapezoid, if the diagonals are congruent, then the trapezoid is an isosceles trapezoid. In a trapezoid $ABCD$, if $\overline{AC} \cong \overline{BD}$, then $ABCD$ is an isosceles trapezoid.

(Teorema del segmento medio de un trapecio)
**Midsegment of a trapezoid theorem**: the length of the midsegment of a trapezoid is the average of the two lengths of the long base and the short base. In a trapezoid $ABCD$, in which $\overline{EF}$ is the midsegment of $ABCD$, then $EF = \frac{AB + CD}{2}$.

(Teorema de los ángulos no de los vértices de un deltoide)
**Non-vertex angles of a kite theorem**: the non-vertex angles of a kite are congruent. In a kite $ABCD$, in which $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$, then $\angle B \cong \angle D$.

(Teorema de los ángulos de los vértices de un deltoide)
**Vertex angles of a kite theorem**: in a kite, the vertex angles are bisected by the diagonal that connects them. In a kite $ABCD$, in which $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$, then $\overline{AC}$ is an angle bisector of $\angle A$ and $\angle C$.

(Teorema de las diagonales de un deltoide)
**Diagonals of a kite theorem**: in a kite, the diagonals are perpendicular. In a kite $ABCD$, in which $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$, then $\overline{AC} \perp \overline{BD}$.

(Teorema del perímetro de figuras similares)
**Perimeter of similar figures theorem**: given two similar figures, that have a scale factor that measures the ratio of each length from the second figure over the respective length in the first figure, then the ratio of the perimeter of the second figure over the perimeter of the first figure is equal to the scale factor. In two similar figures $Fig_1$ and $Fig_2$, $Fig_1 \sim Fig_2$, with perimeters $P_1$ and $P_2$ respectively, and with a scale factor $k$ to obtain $Fig_2$ from $Fig_1$, then $P_2 = k P_1$.

### Shapes with their parts and formulas (Formas con sus partes y fórmulas)

(Marcas de los ángulos)
**Angle markings**: angles can be marked to differentiate between them. Angles are marked with arc marks (marcas del ángulo). Arc marks are commonly of two types: several repeated arcs, or arcs with small perpendicular lines crossing them.

(Marcas de los segmentos)
**Segment markings**: segments can be marked to differentiate between them. Segments are marked with hash marks (marcas del segmento). Hash marks are commonly repeated small lines perpendicular to the segment, placed around the center of the segment.

(Punto medio)
**Midpoint**: the point on a segment, that divides it into two congruent segments. Given three collinear points $A$, $B$, and $C$, with $B$ between $A$ and $C$, and $AB = BC$, then point $B$ is the midpoint of the segment $\overline{AC}$.

(Fórmula del punto medio)
**Midpoint formula**: a formula to calculate the midpoint from two points, which can be the endpoints of a segment. Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points in the $x$-$y$ plane, then the midpoint of the segment they form is $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$.

(Fórmula general para dividir un segmento en $n$ subsegmentos y calcular la localización del $k$-ésimo subsegmento)
**General formula to divide a segment into $n$ subsegments and get the location of the $k$-th subsegment**: let $(x_1, y_1)$ and $(x_2, y_2)$ be the two points that define a segment, this segment can be divided into $n$ subsegments. Counting from $(x_1, y_1)$, the coordinates of the $k$-th subsegment are $\left(x_1 + k\frac{x_2 - x_1}{n}, y_1 + k\frac{y_2 - y_1}{n}\right)$. Making $k = 1$ and $n = 2$ results in the midpoint formula.

(Triángulo)
**Triangle**: shape with three straight sides and therefore three angles. The three straight sides are three segments, in which each segment is connected to the other two with their endpoints. Triangles can be named using the three vertices that form at the intersections of their sides. Each vertex has an opposite side, i.e. the side that does not stem from the vertex. Let $A$, $B$, $C$ be three vertices that form a triangle, then the triangle is denoted as $\triangle ABC$ read as triangle ABC (triángulo ABC). Other form to denote the same triangle is $\triangle BCA$, or any other order of the points of the triangle. The length of the opposite side (lado opuesto) to each vertex is denoted with a lowercase letter, in this case $a$, $b$, and $c$. The sides can also be noted with the two vertices that form the side, in this case $BC$, $AC$, and $AB$ respectively.

(Lado opuesto a un vértice en un triángulo)
**Opposite side of a vertex in a triangle**: in a triangle $\triangle ABC$, each vertex has an opposite side, the opposite side to $A$ is the side $\overline{BC}$, the opposite side to $B$ is $\overline{AC}$, and the opposite side to $C$ is $\overline{AB}$.

(Lado opuesto a un ángulo en un triángulo)
**Opposite side of an angle in a triangle**: in a triangle $\triangle ABC$, each angle has an opposite side, the opposite side to $\angle A$ is the side $\overline{BC}$, the opposite side to $\angle B$ is $\overline{AC}$, and the opposite side to $\angle C$ is $\overline{AB}$.

(Suma de los ángulos de un triángulo)
**Sum of the measures of the angles of a triangle**: the three measures of the angles of any triangle add up to $180 \text{\textdegree}$ or $\pi$ radians. Let $A$, $B$, $C$, be three vertices that form a triangle, then $m \angle A + m \angle B + m \angle C = \pi$.

(Teorema de Pitágoras)
**Pythagorean theorem**: in a right triangle, the hypotenuse squared has the same value as the sum of each leg squared. Let $a$, $b$, $c$, be the sides of a right triangle, with $a$ and $b$ being the legs, and $c$ being the hypotenuse, then $c^2 = a^2 + b^2$.

(Triángulo rectángulo)
**Right triangle**: a triangle in which one of its angles measures $90 \text{\textdegree}$ or $\pi/2$ radians, i.e. a triangle with a right angle. The right angle is denoted in the triangle with a square.

Right triangles have three sides, one hypotenuse (hipotenusa) which is the side opposite to the right angle, and two legs (catetos) which are the two sides that stem from the vertex with the right angle.

(Triángulo obtuso)
**Obtuse triangle**: a triangle that has one obtuse angle.

(Triángulo agudo)
**Acute triangle**: a triangle whose three angles are acute.

(Triángulo equiángulo)
**Equiangular triangle**: a triangle whose three angles are congruent.

(Triángulo escaleno)
**Scalene triangle**: a triangle in which all the sides have different measures of length.

(Triángulo isósceles)
**Isosceles triangle**: a triangle in which two of its sides have the same measure of length.

(Partes de un triángulo isósceles)
**Isosceles triangle parts**: in an isosceles triangle, the congruent sides are called the legs (patas), the remaining side is called the base (base). The two angles formed by the base and each of the legs, are called base angles (ángulos de la base), and the included angle of the two legs is called the vertex angle (ángulo del vértice).

(Triángulo equilátero)
**Equilateral triangle**: a triangle in which all the sides have the same measure of length. All equilateral triangles are similar or congruent.

(Triángulos congruentes)
**Congruent triangles**: given two triangles, they are congruent if their corresponding sides are congruent and their corresponding angles are congruent. The congruence $\triangle ABC \cong \triangle DEF$, is true when $\overline{AB} \cong \overline{DE}$, $\overline{AC} \cong \overline{DF}$, $\overline{BC} \cong \overline{EF}$, $\angle A \cong \angle D$, $\angle B \cong \angle E$, and $\angle C \cong \angle F$. This can be expressed as "corresponding parts of congruent triangles are congruent". In the statement $\triangle ABC \cong \triangle DEF$ the order of the vertices follows the congruence.

The configurations AAA and SSA do not necessarily lead to congruent triangles.

(Segmento medio de un triángulo)
**Midsegment of a triangle**: in a triangle, the midsegment is a segment that connects the two midpoints of adjacent sides. In a triangle $\triangle ABC$, if $D$ is the midpoint of $\overline{AC}$, and $E$ is the midpoint of $\overline{BC}$, then the segment $\overline{DE}$ is a midsegment of the triangle $\triangle ABC$. Every triangle has three midsegments.

(Circuncentro de un triángulo)
**Circumcenter of a triangle**: in a triangle, the circumcenter is the point of concurrency formed at the intersection of the three perpendicular bisectors, one from each side. The circumcenter is in the three perpendicular bisectors of a triangle, and due to the perpendicular bisector theorem, the circumcenter is equidistant to the three vertices of the triangle. This allows building a circle that circumscribes (circunscribe) the triangle, using the circumcenter as center of said circle, and the distance from the circumcenter to any vertex as the radius.

(Incentro de un triángulo)
**Incenter of a triangle**: in a triangle, the incenter is the point of concurrency formed at the intersection of the three angle bisectors, one from each vertex. The incenter is in the three angle bisectors of a triangle, and due to the equidistance in an angle bisector theorem, the incenter is equidistant to the three sides of the triangle. This allows building a circle that inscribes (inscribe) the triangle, using the incenter as center of said circle, and the shortest distance from the incenter to any side as the radius.

(Mediana de un triángulo)
**Median of a triangle**: in a triangle, a median is a segment that connects one vertex with the midpoint of the side opposite to the vertex.

(Centroide de un triángulo)
**Centroid of a triangle**: in a triangle, the centroid is the point of concurrency formed at the intersection of the three medians, one from each vertex.

(Altura de un triángulo)
**Altitude of a triangle**: in a triangle, an altitude is a segment that connects one vertex perpendicularly to the side opposite to the vertex. The altitudes of a triangle don't have to be inside the triangle itself.

(Ortocentro de un triángulo)
**Orthocenter of a triangle**: in a triangle, the orthocenter is the point of concurrency formed at the intersection of the three altitudes, one from each vertex. The location of the orthocenter depends on the type of triangle. In an obtuse triangle, the orthocenter is outside the triangle. In a right triangle, the orthocenter is the vertex opposite to the hypotenuse. In an acute triangle, the orthocenter is inside the triangle.

(Proporcionalidad entre triángulos)
**Triangle proportionality**: from any given triangle, an infinite amount of triangles can be created that are proportional and distinct from the given one. This is done by extending two sides indefinitely, and joining them with a segment parallel to the remaining side.

(Perímetro de un triángulo)
**Triangle perimeter**: let $a$, $b$, $c$, be the lengths of the sides of a triangle, then $P = a + b + c$.

(Área de un triángulo)
**Triangle area**: let $h$ be the height of the triangle as measured when $b$ is the floor, then $A = \frac{b h}{2}$.

(Polígono)
**Polygon**: any geometric figure made with segments joined by their endpoints. Each of the endpoints of the segments in a polygon must be intersecting the endpoint of another segment.

(Lados de un polígono)
**Sides of a polygon**: the segments of the polygon.

(Vértices de un polígono)
**Vertices of a polygon**: the points of a polygon where the segments intersect.

(Ángulos interiores de un polígono)
**Interior angles of a polygon**: each of the angles at any of the vertices of the polygon, that is inside the polygon.

(Ángulos exteriores de un polígono)
**Exterior angles of a polygon**: each of the angles at any of the vertices of the polygon, that is outside the polygon, formed by a side of the vertex and the extension of the other side.

Given that each vertex in a polygon has two sides, two exterior angles can be drawn from each vertex, both being congruent to each other due to the vertical angles theorem. In a given vertex of a polygon, the interior angle and one exterior angle (any of the two) form a linear pair, which means they are supplementary.

(Ángulos interiores remotos)
**Remote interior angles**: the interior angles that are not adjacent to a given exterior angle. In a triangle, given an exterior angle, the remote interior angles are the two interior angles that are not adjacent to said exterior angle.

(Diagonales de un polígono)
**Polygon diagonals**: the segments that are formed by connecting all the vertices of the polygon with each other, but that are not the sides of the polygon.

(Clasificación de polígonos según el número de lados)
**Classification of polygons based on the number of sides**:

- **Triangle** (Triángulo): a polygon with three sides.
- **Quadrilateral** (Cuadrilátero): a polygon with four sides.
- **Pentagon** (Pentágono): a polygon with five sides.
- **Hexagon** (Hexágono): a polygon with six sides.
- **Heptagon** (Heptágono): a polygon with seven sides.
- **Octagon** (Octágono): a polygon with eight sides.
- **Nonagon** (Nonágono): a polygon with nine sides.
- **Decagon** (Decágono): a polygon with ten sides.
- **Undecagon** (Undecágono): a polygon with eleven sides.
- **Dodecagon** (Dodecágono): a polygon with twelve sides.

(Polígono convexo)
**Convex polygon**: a polygon such that in each of its vertices, the angle measured inside the polygon is less than the angle measured outside the polygon.

(Polígono equiangular)
**Equiangular polygon**: a convex polygon in which all the interior angles are congruent with each other.

(Polígono regular)
**Regular polygon**: a polygon that is both equilateral and equiangular, i.e. a polygon with all sides of equal length, and all interior angles of equal measure.

(Polígono cóncavo)
**Concave polygon**: a polygon such that in at least one of its vertices, the angle measured inside the polygon is greater than the angle measured outside the polygon.

(Fórmula del ángulo en un polígono equiangular)
**Angle in an equiangular polygon formula**: a formula to calculate the measure of the interior angles in an equiangular polygon. Let an equiangular polygon have $n$ sides, the measure of each interior angle is $\frac{(n - 2)\pi}{n}$.

(Cuadrilátero)
**Quadrilateral**: a shape with four straight sides.

(Lados opuestos en un cuadrilátero)
**Opposite sides in a quadrilateral**: in a quadrilateral, each side has an opposite side. Given a side of a quadrilateral, its opposite side is the one without any common vertex. In a quadrilateral $ABCD$ the opposite side to $\overline{AB}$ is $\overline{CD}$, and the opposite side to $\overline{AD}$ is $\overline{BC}$.

(Paralelogramo)
**Parallelogram**: a quadrilateral that consists of two pairs of parallel sides.

(Paralelogramos especiales)
**Special parallelograms**: a set of figures that are parallelograms with a few other characteristics in their definition, specifically the rectangle,the rhombus, and the square.

(Rectángulo)
**Rectangle**: a parallelogram with four right angles. This configuration produces a shape in which the opposite sides are of equal length. Its perimeter is equal to the sum of its four sides, and its area is equal to the product of any two adjacent sides.

(Perímetro de un rectángulo)
**Rectangle perimeter**: let $L$ and $W$ be the lengths of the sides of a rectangle, let $P$ be the perimeter of the rectangle, then $P = 2(L + W)$.

(Área de un rectángulo)
**Rectangle area**: let $L$ and $W$ be the lengths of the sides of a rectangle, let $A$ be the area of the rectangle, then $A = L W$.

(Sólido rectangular)
**Rectangular solid**: solid with six faces and with right angles between its faces.

A rectangular solid can be defined with only three measures, length (largo), widht (ancho), and height (alto). When looking at the front of one of the faces from a rectangular solid, the length is defined as the horizontal left to right distance, the width is defined as the horizontal front to back distance, and the height is defined as the vertical distance.

(Área superficial de un sólido rectangular)
**Rectangular solid surface area**: in a rectangular solid, let $L$ be its length, $W$ be its width, $H$ be its height, and $S$ be its surface area, then $S = 2 (L W + L H + W H)$.

(Volumen de un sólido rectangular)
**Rectangular solid volume**: in a rectangular solid, let $L$ be its length, $W$ be its width, $H$ be its height, and $V$ be its volume, then $V = L W H$.

(Rombo)
**Rhombus**: a parallelogram in which all its four sides are congruent.

(Cuadrado)
**Square**: a parallelogram that is also a rectangle and a rhombus, i.e. a parallelogram in which all of its four angles are right angles, and all of its four sides are congruent.

(Cubo)
**Cube**: rectangular solid with all its sides equal in length. This configuration creates a shape in which all of its faces have equal areas.

(Área superficial de un cubo)
**Cube surface area**: in a cube, let $s$ be the the length of any of its sides, and $S$ be its surface area, then $S = 6s^2$.

(Volumen de un cubo)
**Cube volume**: in a cube, let $s$ be the the length of any of its sides, and $V$ be its volume, then $V = s^3$.

(Trapecio)
**Trapezoid**: a quadrilateral with two opposite parallel sides and two opposite non parallel sides. This configuration creates a shape where the two parallel sides are opposite, and the non parallel sides are also opposite. 

The two parallel sides in a trapezoid have different sizes, and they are called the bases (las bases), there is a short base (base corta) and a long base (base larga). The height of a trapezoid is the distance between its bases.

(Trapecio isósceles)
**Isosceles trapezoid**: a trapezoid with its two non-parallel sides congruent.

(Segmento medio de un trapecio | mediana de un trapecio)
**Midsegment of a trapezoid**: in a trapezoid, the midsegment is a segment that connects the two midpoints of the non-parallel sides. In a trapezoid $ABCD$, in which $E$ is the midpoint of $\overline{AD}$ and $F$ is the midpoint of $\overline{BC}$, $\overline{EF}$ is the midsegment of $ABCD$.

(Deltoide | Cometa)
**Kite**: a quadrilateral that consists of two pairs of congruent adjacent sides.

(Deltoide cóncavo | Punta de flecha)
**Dart**: a concave kite.

(Partes de un deltoide)
**Kite parts**: in a kite, the angles between the congruent sides are called vertex angles (ángulos de los vértices), and the two remaining angles are called non-vertex angles (ángulos no de los vértices).

(Área de un trapezoide)
**Trapezoid area**: in a trapezoid, let $b$ be the length of the smaller base, let $B$ be the length of the bigger base, let $h$ be the height, and let $A$ be the area, then $A = \frac{1}{2}h(b + B)$.

(Círculo)
**Circle**: shape in which all of its points are at the same distance from its center.

(Radio de un círculo)
**Radius of a circle**: the distance from the center of a circle to any of its points.

(Diámetro de un círculo)
**Diameter of a circle**: the maximum possible distance between two points in a circle. This is the same as twice the radius.

(Sector circular)
**Circular sector**: a portion of a circle. A sector is originated from the intersection of two distinct radii segments and the circumference.

(Circunferencia de un círculo)
**Circumference of a circle**: the measure of the distance around a circle, i.e. the distance covered by its points. This is the same as the perimeter of the circle.

Let $d$ be the diameter in length units, $r$ be the radius in length units, $C$ be the circumference in length units, then $C = \pi d$ or also $C = 2 \pi r$.

(Área de un círculo)
**Circle area**: let $A$ be the area of a circle in squared length units, $r$ be the radius in length units, then $A = \pi r^2$.

(Esfera)
**Sphere**: three dimensional shape in which all of its points are at the same distance from its center, this distance is called the radius.

(Área superficial de una esfera)
**Sphere surface area**: in a sphere, let $r$ be its radius, and $S$ be its surface area, then $S = 4 \pi r^2$.

(Volumen de una esfera)
**Sphere volume**: in a sphere, let $r$ be its radius, and $V$ be its volume, then $V = \frac{4}{3} \pi r^3$.

(Cilindro)
**Cylinder**: a solid made with two parallel circles separated along an axis.

(Área superficial de un cilindro)
**Cylinder surface area**: in a cylinder, let $r$ be the radius of its circles, $h$ be its height, and $S$ be its surface area, then $S = 2 \pi r^2 + 2 \pi r h$.

(Volumen de un cilindro)
**Cylinder volume**: in a cylinder, let $r$ be the radius of its circles, $h$ be its height, and $V$ be its volume, then $V = \pi r^2 h$.

(Cono)
**Cone**: a solid made with a circle called the base (base) and a point called the apex (ápice) above the center of the base, in such a way that the circumference of the base converges to the apex.

(Área superficial de un cono)
**Cone surface area**: in a cone, let $r$ be the radius of its base, $l$ be the distance from the apex to its circumference, and $S$ be its surface area, then $S = \pi r^2 + \pi r l$.

(Volumen de un cono)
**Cone volume**: in a cone, let $r$ be the radius of its base, $h$ be the distance from the apex to its base, and $V$ be its volume, then $V = \frac{1}{3} \pi r^2 h$.

(Área de una figura irregular)
**Area of an irregular figure**: there is no single formula for the area of an irregular figure, but rather, said area is divided into smaller areas with basic shapes, such as triangles and quadrilaterals, and then the area of the irregular figure is calculated as the sum of the areas of the smaller shapes.

(Triángulo de Sierpinski)
**Sierpinski triangle**: a triangle fractal with infinite upside down triangles inside. The stage 0 shape is a triangle (commonly an equilateral triangle, but it doesn't have to be).

Every triangle has a smaller similar triangle that is formed with its midsegments, with a scale factor of $1/2$ because of the midsegment of a triangle theorem. The smaller similar triangle is always upside down, relative to the original triangle. The Sierpinski triangle is created by 'cutting out', or coloring the smaller similar upside down triangle formed with the midsegments. For this work, lets call the 'smaller similar upside down triangle formed with the midsegments' simply as the 'upside down triangle' because that's the most important visual feature for the Sierpinski triangle.

To create this fractal, the first iteration colors the only one upside down triangle, in the result there are now three non-colored triangles, one in each side of the colored triangle. The second iteration colors the three upside down triangles inside the three non-colored triangles from iteration 1, this leaves now 9 non-colored triangles. The next iteration colors all the upside down triangles inside all the non-colored triangles from the former iteration, and so on.

(Cantidad de triángulos por etapa en un triángulo de Sierpinski)
**Amount of triangles per stage in a Sierpinski triangle**: the amounts of non-colored triangles and of colored triangles in a Sierpinski triangle, follow certain patterns.

The amount of non-colored triangles of stage $n$ is $NCT_n = 3^n$ where $n = 0, 1, 2, ...$, because in stage 0 there is only $1 = 3^0$ non-colored triangle. In stage 1, the colored triangle divides the initial triangle into $3 = 3^1$ non-triangles. The logic here is that each colored triangle will divide its container non-colored triangle into three non-colored triangles. So in stage 2, the $3$ non-colored triangles are divided into $3 \cdot 3 = 9$ non-colored triangles. In stage 3, the $9$ non-colored triangles are divided into $9 \cdot 3 = 27$ non-colored triangles, and so on.

The amount of colored triangles of stage $n$ is $CT_n = CT_{n - 1} + NCT_{n - 1}$, with $CT_0 = 0$, because in stage 0 there are $0$ colored triangles, in stage 1 there is $1$ colored triangle which comes from the $1$ non-colored triangle from stage 0. In stage 2 there are $4$ colored triangles, $1$ colored triangle from stage 1 and $3$ new ones from stage 1, and so on.

(Copo de nieve de Koch)
**Koch snowflake**: a triangle fractal with infinite similar triangles, one coming out of the center third of each side. The stage 0 shape is a triangle (commonly an equilateral triangle, but it doesn't have to be).

To create this fractal, the first iteration divides each side of the original triangle into three thirds, a triangle similar to the original is drawn in the center third, such that the sides of the new triangle are placed parallel to the original triangle. The second iteration divides each side that resulted from iteration 1 into three thirds and the process is repeated (draw a similar triangle in the center third with its sides parallel to the original), and so on. This procedure causes that the new triangles from an iteration are upside down from the triangles in the former iteration, because of the need to maintain corresponding sides parallel.

(Lados y longitud por lado en un copo de nieve de Koch)
**Sides and length per side in a Koch snowflake**: the amount of sides and the length per side in a Koch snowflake, both follow certain patterns.

The amount of sides $s_n$ of stage $n$ is $s_n = 3 \cdot 4^n$, because in stage 0 there are only the $3 = 3 \cdot 4^0$ sides of the initial triangle. In stage 1, each one of the $3$ sides of the triangle gives origin to $4$ new sides, for a total of $12 = 3 \cdot 4^1$ sides in total for stage 1, because each side of stage 0 is divided in three parts but the center third is divided into two sides of the smaller new triangle, resulting in $4$ new sides, and so on for the rest of stages (each side creates $4$ new sides).

The length per side is $1/3$ of the side that it stems from. If a Koch snowflake is created from an scalene triangle, then each there are three lengths, one for each side of the initial triangle. The length per side $l_{i, n}$ parallel to the side $i$ of the initial triangle in stage $n$, is $l_{i, n} = \frac{L_i}{3^n}$, where $L_i$ is the length of the side $i$ of the initial triangle. This is because stage $n$ divides each side in thirds (which explains the denominator $3^n$), and the original length from which each side is divided is $L_i$.

(Conjunto de Cantor)
**Cantor set**: a segment fractal with infinite smaller subsegments, each originated by dividing a previous segment into three thirds and removing the center third. The stage 0 shape is a segment.

To create this fractal, the first iteration divides the initial segment into three thirds and removes the center third. The second iteration takes the two subsegments that resulted from the first iteration, and divides them into three thirds and removes the center third, and so on.

(Cantidad de subsegmentos y longitud por subsegmento en un conjunto de Cantor)
**Amount of subsegments and length per subsegment in a Cantor set**: the amount of subsegments and the length per subsegment in a Cantor set, both follow certain patterns.

The amount of subsegments $s_n$ of stage $n$ is $s_n = 2^n$, because dividing a segment into three thirds and then removing the center third leaves only two subsegments each time, and given that all subsegments undergo this process in each iteration, the result is that the amount of subsegments is double the amount of subsegments in the previous iteration.

The length per subsegment $l_n$ of stage $n$ is $l_n = \frac{L}{3^n}$, where $L$ is the length of the initial segment. This is because the initial segment is divided into thirds each iteration.

## Probability definitions (Definiciones de probabilidad)

(Frecuencia de un número en un conjunto)
**Frequency of a number in a set**: the amount of times a given number is repeated in a set.

(Probabilidad de un evento)
**Probability of an event**: the fraction of the number of times an event happens over the number of general outcomes with or without the event.

For example, in a set of $N$ numbers, the probability $P(x)$ to obtain a given number $x$ that has a frequency of $f_x$ is $P(x) = \frac{f_x}{N}$.

### Measures of central tendency (Medidas de tendencia central)

(Promedios)
**Averages**: measures of the typical number in a set of numbers. A typical number is that which is most likely to appear from the set, or one that has a value in the middle of the values of the set. The measure of an average itself doesn't have to be part of the set of numbers, so a number that is not in the set, could be a representative value for said set.

(La media)
**The mean**: also called the arithmetic average (la media aritmética), it's the sum of a set of numbers divided by the size of the set. Let $X$ be a set of $N$ numbers, $x_i$ be the $i$-th number in the set, $\bar{x}$ be the mean of the set, then $\bar{x} = \sum_i{\frac{x_i}{N}}$.

(Mediana)
**Median**: the middle value in a set of numbers, such that half the numbers are greater than the median, and the other half is less than the median. After sorting the set, when the set contains an odd amount of numbers, the median is the value in the middle, and when the set has an even amount of numbers, the median is the mean of the two values in the middle.

(Moda)
**Mode**: the number with the highest frequency in a set. A set of numbers can have several modes if several numbers have the same highest frequency, or none if all the numbers have the same frequency.

## Simplifications (Simplificaciones)

(Reducir fracciones)
**Reduce fractions**: form of simplification in which a fraction is expressed as an equivalent fraction that has no common factors between the numerator and the denominator. If there is a common factor, both the numerator and the denominator are divided by it, this simplifies the fraction.

For example $\frac{6}{9} = \frac{4}{6}$, but their reduced form is $\frac{2}{3}$. In $\frac{6}{9}$ a common factor is $3$ and dividing the numerator and denominator by $3$ results in $\frac{2}{3}$. In $\frac{4}{6}$ a common factor is $2$ and dividing the numerator and denominator by $2$ results in $\frac{2}{3}$.

The same simplification can be done with variables, e.g. $\frac{2 x}{x}$ can be simplified to $\frac{2}{1}$ or $2$.

(Fracción irreducible)
**Simplified fraction**: a fraction in which the numerator and the denominator have no common factors.

(Eliminar los denominadores de una ecuación)
**Clear an equation of fractions**: the process of clearing the fractions of an equation, by multiplying each term on both sides by the least common denominator.

(Conversión entre decimales y fracciones)
**Conversion between decimals and fractions**: decimals can be presented in fraction form, and vice versa. The conversion from fraction to decimal is done by performing the division of the numerator over the denominator of the fraction. The conversion from finite decimal to fraction is done by multiplying the decimal by 10 to the positive power of the place of the rightmost digit, and dividing the result over the same power of 10.

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

## Science and engineering definitions (Definiciones de ciencia e ingeniería)

(Ratio)
**Ratio**: a fraction of any two numbers that are measured with the same unit or scale, therefore ratios have no units themselves. For example the ratio of height to width, both are measured in distance.

The notation of ratios in particular, includes the use of the colon : symbol to replace the division symbol. So the ratio $\frac{a}{b}$ can be denoted as $a:b$. If $b = 1$ then the ratio is still presented as $\frac{a}{1}$, and if the ratio is an improper fraction, it is not converted to a mixed number. The ratio $a:b$ is read as $a$ to $b$ ($a$ a $b$).

In a ratio, the division operation is not actually made, for example the ratio $a:b$, in this ratio, if $a$ and $b$ are measured in type1 units, the ratio indicates that there are $a$ units of type1 per every $b$ units of type1. The division is not performed. This allows writing ratios with more than two numbers, for example the ratio $a:b:c$ with $c$ also measured in type1 units, indicates that there are $a$ units of type1 per every $b$ units, and also there are $a$ units per every $c$ units, and there are $b$ units per every $c$ units. When a ratio has more than two numbers, the fraction notation is not used, only the colon notation.

(Tasa)
**Rate**: a fraction of any two numbers that are measured in differente units or scales, so the unit of a rate is the fraction of the units. For example the rate of speed which is measured as a fraction of distance over time.

Ratios can be considered rates when the particular units in the numerator and denominator are also considered, even though they are the same. For example, width over height can be seen as a ratio, but also as the rate of width per unit of height, this rate is still dimensionless like a ratio.

(Tasa unitaria)
**Unit rate**: a rate expressed with a denominator of $1$.

(Precio unitario)
**Unit price**: a unit rate in which the unit is $\text{\textdollar}/unit$, it tells the price per unit.

(Porcentaje de aumento, porcentaje de disminución)
**Percent increase, percent decrease**: in general, the percent change (porcentaje de cambio) from a variable is measured as the difference of final value minus initial value, divided over the initial value, this result tells the amount of units changed per group of $1$ unit before change, and this can be converted to a percent.

Let $V_i$ be the initial value of a given variable, $V_f$ be the final value of said variable, $\Delta p\%$ be the percent change, then $\Delta p\% = \frac{V_f - V_i}{V_i} 100\%$. Note that the words "initial" and "final" do not have to mean that they are separated in time, they can be separated under any criteria wanted.

Given that $V_f$ can be smaller or bigger than $V_i$, $\Delta p\%$ can be negative or positive, if it's negative then that means that the percent change is a percent decrease, whereas if it's positive then that means that the percent change is a percent increase.

(Notación científica)
**Scientific notation**: scientific notation is a way to express numbers. A given number written in scientific notation is represented as a number greater than or equal to 1 and less than 10, multiplied by a power of 10.

Any number $N$ can be expressed in scientific notation, for this let $a$ be a number such that $a \ge 1$ and $a < 10$, and let $n$ be an integer, then $N = a 10^n$. To convert the given number $N$ to scientific notation, only its first nonzero digit is left as the first digit of $a$, and the remaining digits become decimals of $a$, this conversion is compensated as necessary using $n$, so that the equality $N = a 10^n$ is maintained. If $|N| \ge 1$ then $n$ must be zero or positive, while if $|N| < 1$ then $n$ must be negative.

For example, the number $-3894.15509$ expressed in scientific notation is $-3.89415509 \cdot 10^3$, given that the decimal point was moved to the left (higher place values) the value of $n$ is positive $3$.

(Sistemas de medida)
**Systems of measurement**: The systems of measurement are systems intended to be internally consistent, to provide a unit of measure for any physical quantity. The main quantities measured in these systems are time and space (time, distance, area, volume), derived quantities are also included like speed (distance divided by time), and also units of measure for other quantities, like electric field, radiation levels, etcetera.

There are two main systems of measurement used at the time of this writing, the U.S. system and the international metric system.

(Sistema anglosajón de unidades)
**United States customary units**: system of measurement with units for length, volume, weight, time, and more.

The following table contains a few of the units of the United States customary units system of measurement. Inside parentheses appears the abbreviation of each unit of measure.

| United States customary units      | Sistema anglosajón de unidades |
| :--------------------------------: | :----------------------------: |
| **Length**                         | **Longitud**                   |
| 1 foot (ft) = 12 inches (in)       | 1 pie = 12 pulgadas            |
| 1 yard (yd) = 3 feet (ft)          | 1 yarda = 3 pies               |
| 1 mile (mi) = 5280 feet (ft)       | 1 milla = 5280 pies            |
| **Volume**                         | **Volumen**                    |
| 3 teaspoons (t) = 1 tablespoon (T) | 3 cucharaditas = 1 cucharada   |
| 16 tablespoons (T) = 1 cup (C)     | 16 cucharadas = 1 taza         |
| 1 cup (C) = 8 fluid ounces (fl oz) | 1 taza = 8 onzas fluidas       |
| 1 pint (pt) = 2 cups (C)           | 1 pinta = 2 tazas              |
| 1 quart (qt) = 2 pints (pt)        | 1 cuarto de galón = 2 pintas   |
| 1 gallon (gal) = 4 quarts (qt)     | 1 galón = 4 cuartos de galón   |
| **Weight**                         | **Peso**                       |
| 1 pound (lb) = 16 ounces (oz)      | 1 libra = 16 onzas             |
| 1 ton (ton) = 2000 pounds (lb)     | 1 tonelada = 2000 libras       |
| **Time**                           | **Tiempo**                     |
| 1 minute (min) = 60 seconds (s)    | 1 minuto = 60 segundos         |
| 1 hour (h) = 60 minutes (min)      | 1 hora = 60 minutos            |
| 1 day (day) = 24 hours (h)         | 1 día = 24 horas               |
| 1 week (wk) = 7 days (days)        | 1 semana = 7 días              |
| 1 year (yr) = 365 days (days)      | 1 año = 365 días               |

(Sistema métrico internacional)
**International metric system**: system of measurement whose units are based on powers of 10. Prefixes are used to indicate the power of 10.

The following table contains a few of the units of the international metric system of measurement. Inside parentheses appears the abbreviation of each unit of measure.

| International metric system | Sistema métrico internacional |
| :-------------------------: | :---------------------------: |
| **Length**                  | **Longitud**                  |
| 1 meter (m) = 1 m           | 1 metro = 1 m                 |
| 1 kilometer (km) = 1000 m   | 1 kilómetro = 1000 m          |
| 1 hectometer (hm) = 100 m   | 1 hectómetro = 100 m          |
| 1 dekameter (dam) = 10 m    | 1 decámetro = 10 m            |
| 1 decimeter (dm) = 0.1 m    | 1 decímetro = 0.1 m           |
| 1 centimeter (cm) = 0.01 m  | 1 centímetro = 0.01 m         |
| 1 millimeter (mm) = 0.001 m | 1 milímetro = 0.001 m         |
| **Mass**                    | **Masa**                      |
| 1 gram (g) = 1 g            | 1 gramo = 1 g                 |
| 1 kilogram (kg) = 1000 g    | 1 kilogramo = 1000 g          |
| 1 hectogram (hg) = 100 g    | 1 hectogramo = 100 g          |
| 1 dekagram (dag) = 10 g     | 1 decagramo = 10 g            |
| 1 decigram (dg) = 0.1 g     | 1 decigramo = 0.1 g           |
| 1 centigram (cg) = 0.01 g   | 1 centigramo = 0.01 g         |
| 1 milligram (mg) = 0.001 g  | 1 miligramo = 0.001 g         |
| **Volume**                  | **Volumen**                   |
| 1 liter (L) = 1 L           | 1 litro = 1 L                 |
| 1 kiloliter (kL) = 1000 L   | 1 kilolitro = 1000 L          |
| 1 hectoliter (hL) = 100 L   | 1 hectolitro = 100 L          |
| 1 dekaliter (daL) = 10 L    | 1 decalitro = 10 L            |
| 1 deciliter (dL) = 0.1 L    | 1 decilitro = 0.1 L           |
| 1 centiliter (cL) = 0.01 L  | 1 centilitro = 0.01 L         |
| 1 milliliter (mL) = 0.001 L | 1 mililitro = 0.001 L         |

(Conversión de unidades)
**Unit conversion**: changing the units of a measure. Unit conversion is based on multiplying the unit to be changed by $1$, but writing $1$ in such a way that it changes the unit of measure. In general, given the units of measure $unit1$ and $unit2$, and given $A\ unit1 = B\ unit2$ meaning that $A$ units of $unit1$ are equal in measure to $B$ units of $unit2$, so $1 = \frac{B\ unit2}{A\ unit1}$, and also $1 = \frac{A\ unit1}{B\ unit2}$. These fractions are called conversion factors (factores de conversión).

Using real units, $1\ foot = 12\ inches$, so $1 = \frac{1\ foot}{12\ inches}$, and $1 = \frac{12\ inches}{1\ foot}$. The fraction chosen to do the unit conversion is the one that divides the unit being changed, so, the one that has the unit being changed in the denominator. For example, to convert $60\ inches$ to $feet$, the conversion factor must have $inches$ in the denominator, $60\ inches \frac{1\ foot}{12\ inches} = 5 feet$.

Several conversions can be made one after the other, for example, $60\ inches \frac{1\ foot}{12\ inches} \frac{1\ yard}{3\ feet} = \frac{5}{3}\ yard$.

(Conversión entre sistemas de medida)
**Conversion between systems of measurement**: units of measure can be converted from one system to another by having their equivalencies (equivalencias), and then performing regular unit conversion using said equivalencies.

The following table contains a few of the equivalencies between units in the U.S. customary units system and units in the international metric system. The values presented in the table are approximations.

| Equivalencies   |
| :------------:  |
| **Length**      |
| 1 in = 2.54 cm  |
| 1 ft = 0.305 m  |
| 1 yd = 0.914 m  |
| 1 mi = 1.61 km  |
| **Weight**      |
| 1 lb = 0.45 kg  |
| 1 oz = 28 g     |
| **Volume**      |
| 1 qt = 0.95 L   |
| 1 fl oz = 30 mL |

(Unidades de medida mixtas)
**Mixed units of measurement**: units of measure that are combined together to measure a single quantity. For example, using hours and minutes together to measure time.

When handling mixed units of measurement, each separate unit is added or subtracted separately. In the case of using hours and minutes together, for example $3\ hours, 12\ minutes$ plus $2\ hours, 20\ minutes$ is $5\ hours, 32\ minutes$, because hours and minutes are added separately. In this particular case, any amount of minutes over 60 is converted to hours accordingly, and in general the smaller unit is converted to the bigger unit if needed.

(Combinar unidades mixtas)
**Combine mixed units**: Mixed units of measure can be combined together into a single unit. For example, time measured in minutes and seconds can be combined into minutes alone, by adding the seconds divided by $60$ to the minutes.

Money measured in different currency valued coins and bills can be combined together into a single currency value (a standard value), by converting the total of each type of coin and bill to said currency value and then adding them.

Let $I$ be the set of unique units to be mixed, $i$ be a subindex of $I$, $v_i$ be the standard value per unit $i$, $a_i$ be the amount of unit $i$, $V_i$ be the subtotal standard value of unit $i$, and let $V$ be the total standard value, then $V_i = a_i v_i$ and $V = \sum_i{V_i}$.

(Conversión Fahrenheit Celsius)
**Fahrenheit Celsius conversion**: two formulas that allow converting temperature (temperatura) measured in the Fahrenheit scale to the Celsius scale, and vice versa, let $C$ be the temperature in Celsius, $F$ be the temperature in Fahrenheit, then $C = \frac{5}{9}(F - 32)$ and $F = \frac{9}{5}C + 32$.

(Problemas con números)
**Number problems**: Problems with numbers stated as words, for example, there is a number whose product with $3$ is $24$, finding that number gives $8$.

(Interés simple)
**Simple interest**: The simple interest is a way to calculate the amount of interest to be received for an investment or paid for a loan.

(Principal de una inversión)
**Investment principal**: the amount of money put into an investment.

(Principal de un préstamo)
**Loan principal**: the amount of money borrowed as a loan.

(Interés financiero)
**Financial interest**: money received in return for an investment, or paid for a loan.

### Science and engineering formulas (Fórmulas de ciencia e ingeniería)

(Fórmula de la velocidad, distancia y tiempo)
**Velocity, distance and time formula**: velocity is defined as the rate of distance change over time.

Let $d$ be the distance in length units, $t$ be the time in time units, $v$ be the velocity in distance over time units, then $v = \frac{d}{t}$. From this formula it can be deduced that $d = vt$, and $t = \frac{d}{v}$.

(Fórmula de tiempo en caída libre)
**Free fall time formula**: formula to find the fall time in a free fall scenario. The fall starts at a given height, and the time calculated by this formula is the time from the moment the fall starts, to the moment of reaching the ground.

Let $t$ be the fall time in time units, $h$ be the starting height in length units, $g$ be the standard gravity (gravedad estándar), then $t = \sqrt{\frac{2 h}{g}}$.

(Fórmula de la velocidad antes de frenar)
**Formula of the speed before braking**: formula to find the speed of a car before braking, from the length of the skid mark. Let $d$ be the skid mark distance in feet, $v$ be the speed of the car before braking in miles per hour, then $v = \sqrt{24 d}$.

(Impuesto de ventas)
**Sales tax**: percent applied to the price of a good or service (bien o servicio), the resulting amount of which is paid as taxes. Let $P_i$ be the price before taxes in monetary units, $P$ be the price with sales tax in monetary units, and $t$ be the sales tax as a ratio, then $P = P_i + t P_i$. The term $t P_i$ is hold as taxes by businesses, and then paid to the government.

(Comisión por ventas)
**Sales commission**: extra wage paid to a sales person for the value sold by them. Let $C$ be the commission earned by the sales person in monetary units, $P$ be the sales value of the goods or services sold in monetary units, and $c$ be the commission rate (tasa de comisión) as a ratio, then $C = c P$. The commission rate $c$ is commonly expressed as a percent, which means the percent of each monetary unit sold that becomes commission.

(Descuento de precio)
**Price discount**: reduction in the price of a good or service, to make it more attractive for clients to buy. Let $D$ be the amount of discount in monetary units, $P_i$ be the regular price in monetary units, $P$ be the price after discount in monetary units, $d$ be the discount rate (tasa de descuento) as a ratio, then $D = d P_i$ and $P = P_i - D = P_i - d P_i$. The discount rate $d$ is commonly expressed as a percent, which means the percent of each monetary unit of the price that becomes discounted.

(Margen de ganancia)
**Mark-up**: retailers buy goods at a wholesale price (precio mayorista), and then resell said goods at a list price (precio de lista | precio sugerido). Their profit comes from the mark-up which is the extra price added to the wholesale price to obtain the list price. Let $W$ be the wholesale price of a good in monetary units, $M$ be the amount of mark-up in monetary units, $L$ be the list price in monetary units, and $m$ be the mark-up rate as a ratio, then $M = m W$ and $L = W + M = W + m W$. The mark-up rate is commonly expressed as a percent, which means the percent of each monetary unit of the wholesale price that becomes mark-up.

(Fórmula del interés simple)
**Simple interest formula**: formula to calculate the simple interest from the loan principal, the interest rate, and the time elapsed since the loan started. Let $P$ be the principal of the investment or loan in monetary units, $I$ be the amount of interest in monetary units, $t$ be the time elapsed since the moment of the investment or loan in time units, and $r$ be the interest rate (tasa de interés) paid per period as a ratio, then $I = Prt$.

### Science and engineering procedure definitions (Definiciones de procedimientos de ciencia e ingeniería)

(Medición de distancia)
**Measure of distance**: the process of determining the distance between two points. The ruler (la regla) is the basic instrument to measure distance. Rulers measure distance in units such as inches (pulgadas) and centimeters (centímetros). Let $A$ and $B$ be two points, the segment that they form as endpoints is $\overline{AB}$, and the measure of the distance of this segment is denoted by $AB$ or $m \overline{AB}$.

(Transportador)
**Protractor**: instrument to measure angles. The most common units of measure are degrees and radians. Degrees denote a rotation of a full circle as $360 \text{\textdegree}$, and in radians this is denoted as $2 \pi$.

(Método de medición de un ángulo usando un transportador)
**Method of angle measurement using a protractor**: a method to measure an angle using a protractor. This method can be used to draw a given angle.

(Regla no graduada)
**Straightedge**: an instrument used to make straight lines, like a ruler but without tick marks.

(Compás)
**Compass**: an instrument used to draw arcs.

(Centrar el compás en un punto dado)
**Center the compass on a given point**: put the needle of the compass in the given point.

(Construcciones geométricas)
**Geometric constructions**: a drawing made with straightedge and compass, commonly with the intention to follow given steps in the use of said instruments, to obtain a given geometric shape.

(Construcción para copiar un ángulo)
**Copy an angle construction**: it's possible to copy an angle by doing a construction.

(Construcción de la mediatriz)
**Perpendicular bisector construction**: a geometric construction to draw the perpendicular bisector of a given segment.

(Construcción de la bisectriz de un ángulo)
**Angle bisector construction**: a geometric construction to draw the angle bisector of a given angle.

(Construcción de una línea perpendicular)
**Perpendicular line construction**: a geometric construction to draw the unique perpendicular line to a given line that passes through a given point.

(Construcción de dos líneas paralelas)
**Two parallel lines construction**: a geometric construction to draw two lines such that they are parallel to each other.

(Construcción de un triángulo dados tres lados)
**Triangle from three sides construction**: a geometric construction to draw a triangle, given the lengths of its three sides.

(Construcción de un triángulo dados dos lados y su ángulo comprendido)
**Triangle from two sides and their included angle construction**: a geometric construction to draw a triangle given two sides and their included angle.

(Construcción de un triángulo dados dos ángulos y su lado comprendido)
**Triangle from two angles and their included side construction**: geometric construction to draw a triangle given two angles and their included side.

(Construcción de dos triángulos similares dados dos ángulos)
**Two similar triangles given two angles construction**: a geometric construction to draw two similar triangles given two angles.

(Construcción de dos triángulos similares dados tres lados)
**Two similar triangles given three sides construction**: a geometric construction to draw two similar triangles given three sides.

(Construcción de dos triángulos similares dados dos lados y su ángulo comprendido)
**Two similar triangles given two sides and their included angle construction**: a geometric construction to draw two similar triangles given two sides and their included angle.

(Construcción de un paralelogramo)
**Parallelogram construction**: a geometric construction to draw a parallelogram.

(Algoritmo para encontrar la distancia más corta entre un punto y una línea)
**Algorithm to find the shortest distance between a point and a line**: there is an algorithm to find this distance based on algebra in the rectangular coordinate system.

(Algoritmo para encontrar la distancia más corta entre dos líneas paralelas)
**Algorithm to find the shortest distance between two parallel lines**: there is an algorithm to find this distance based on algebra in the rectangular coordinate system.

(Medición indirecta)
**Indirect measurement**: a way to measure lengths that can't be accessed directly (lengths to places that are unreachable), using triangle similarity. For example, this can serve to measure lengths such as the width of a river, or the height of a tall building. It's an algorithm.

(Medición indirecta usando un triángulo recto)
**Indirect measurement using a right triangle**: there is a different way to do indirect measurement, that doesn't require a smaller similar triangle.
In $\triangle ABC$, if $\angle B$ is a right angle, $C$ is the unreachable point, and $BC$ is the length to measure indirectly, then $BC = AB tan(\angle A)$, where $tan$ is the tangent function, so $\angle A$ and $AB$ must be measured.