
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

(Ecuaciones lineales)
**Linear equations**: a linear equation is an equation in which the variables have an exponent of $1$.

Linear equations can start with variable terms on both sides. When equations have variables and constants on both sides, the properties of equality can be used to move the variables and put them in one side if needed. For example, if a variable is dividing a number, it can be passed to the other side by using the multiplication property of equality, multiplying both sides by the variable.

(Ecuación lineal en una variable)
**Linear equation in one variable**: linear equation in which there is only one variable. These equations can be simplified by using the properties of equality to create a variable side and a constant side.
[Simplification of linear equations in one variable code](Programs/S08/Simplification_of_linear_equations_in_one_variable.py)

> Form of a linear equation in one variable
>
> Let $a$, $b$, be numbers, $x$ be a variable, then
> $$ax = b$$

Every linear equation in one variable can be simplified through the use of the properties of equality, to leave it in the form $ax = b$. The side $ax$ is the variable side, and the side $b$ is the constant side.

(Ecuación lineal en dos variables)
**Linear equation in two variables**: linear equation with two variables, such that a change in one of the variables produces a proportional change in the other variable.

> Standard form of a linear equation in two variables
>
> Let $A$, $B$, $C$, be constants, $x$, $y$, be variables, then
> $$Ax + By = C$$
> This is a linear equation, its solutions form a line when shown in a graph of the $x$-$y$ plane.

The amount of solutions of a linear equation is infinite, the line formed by the equation can be extended indefinitely.

(Pendiente de una ecuación lineal)
**Slope of a linear equation**: the slope of a line is a ratio that shows how many units in the $y$-axis change when a single unit in the $x$-axis changes. In a given line, the slope is measured as the value changed in the $y$-axis divided by the equivalent change in the $x$-axis.

The slope of an horizontal line is $0$ and the slope of a vertical line is undefined (positive or negative infinity).

A negative slope means that whenever the value in the $x$-axis increases, the value in the $y$-axis decreases, and vice versa. A positive slope indicates that both values in $x$ and $y$ increase or decrease together.

(Fórmula de la pendiente)
**Slope formula**: the slope of a line that passes through two given points, is equal to the ratio of the difference of the $y$-axis values of the two points over the difference of the $x$-axis values of the two points.

> Slope formula
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points in the $x$-$y$ plane, and let $m$ be the slope that they form, then
> $$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{y_1 - y_2}{x_1 - x_2}$$

The rise (elevación) of a slope is the amount changed in the $y$ axis, namely $y_2 - y_1$. The run (avance) of a slope is the amount changed in the $x$ axis, namely $x_2 - x_1$. So the algebraic definition of the slope can also be interpreted as rise over run.

(Elevación sobre avance de una pendiente)
**Rise over run of a slope**: in a slope, rise over run is the fraction of the vertical distance called "rise" over the horizontal distance called "run".

(Forma pendiente intercepto de una línea)
**Slope-intercept form of a line**: an equation that expresses the $y$ coordinate of each point of a line, as the the slope multiplied by the $x$ coordinate of that point, plus the $y$-intercept.

> Slope-intercept form of a line
>
> Let $y$ be the $y$ coordinate of a given point, let $x$ be the $x$ coordinate of the same point, let $m$ be the slope, $b$ be the $y$-intercept, then
> $$y = mx + b$$

(Pendiente de líneas paralelas)
**Slope of parallel lines**: the slope of a set of parallel lines is the same for all the lines, i.e. all parallel lines have the same slope. This is because for lines to be parallel, they must have the same rise and run.

Using the slope-intercept form of a line, parallel lines have the same slope but different $y$-intercept values.

(Pendiente de líneas perpendiculares)
**Slope of perpendicular lines**: given the slope $m$ of a line, the slope of a perpendicular line to it, is $-1/m$. This is because given the slope of a line, the slope of a line perpendicular to it, is the opposite reciprocal of the slope of the given line.
[Slope of perpendicular lines image code](Programs/S02/Slope_of_perpendicular_lines_image.py)
![Slope of perpendicular lines image](Images/S02/Slope_of_perpendicular_lines.png)

The blue line is the first line, the lime green line has a slope that is the opposite of the slope of the blue line. The crimson line is perpendicular to the blue line, and has a slope that is the reciprocal of the slope of the lime green line.

(Distancia más corta entre un punto y una recta)
**Shortest distance between a point and a line**: given a point and a line, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line to the given line that passes through the given point, is used to measure this shortest distance, as the distance between the given point and the intersection of the perpendicular line and the given line.
[Shortest distance between a point and a line image code](Programs/S02/Shortest_distance_between_a_point_and_a_line_image.py)
![Shortest distance between a point and a line image](Images/S02/Shortest_distance_between_a_point_and_a_line.png)
*Shortest distance between a point and a line*

The shortest distance between the point $A$ and the line $l$ is the distance $AB$.

(Distancia más corta entre dos líneas paralelas)
**Shortest distance between two parallel lines**: given two parallel lines, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line that passes through both parallel lines, is used to measure this shortest distance, as the distance between the two intersections of the perpendicular line with the two parallel lines.

By definition of parallel lines, the shortest distance between them is a constant.

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

(Multiplicación de monomios)
**Monomial multiplication**: let $a$, $b$, $k$, $l$, $m$, $n$, be numbers and $x$, $y$ be variables, then the product of the monomials $ax^ky^l$ and $bx^my^n$ is $abx^{k + m}y^{l + n}$.

## Multiplication of polynomials (Multiplicación de polinomios)

(Multiplicación de polinomios)
**Multiplication of polynomials**: the multiplication of polynomials is based on the distributive property of multiplication over addition (and subtraction). In the product of two polynomials, each term of the first polynomial is multiplied by the second polynomial using the distributive property.
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

For example, given $p(x) = 2x^3 + 4x - 7$ and $q(x) = 3x - 2$, then $p(x)q(x) = (2x^3)(3x) + (2x^3)(-2) + (4x)(3x) + (4x)(-2) + (-7)(3x) + (-7)(-2) = 6x^4 - 4x^3 + 12x^2 - 8x - 21x + 14 = 6x^4 - 4x^3 + 12x^2 - 29x + 14$, so $p(x)q(x) = 6x^4 - 4x^3 + 12x^2 - 29x + 14$.

## Division of polynomials (División de polinomios)

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

For example, given $p(x) = 3x^2 + 7x + 4$ and $g(x) = x + 1$, then $\frac{p(x)}{g(x)} = \frac{3x^2 + 7x + 4}{x + 1}$. The first term in the quotient is $3x$ because $3x(x) = 3x^2$ which is the first term in the dividend. Multiplying $3x$ by the divisor and then subtracting the result from the dividend gives, $3x(x + 1) = 3x^2 + 3x$, $3x^2 + 7x + 4 - 3x^2 - 3x = 4x + 4$, now the current dividend is $4x + 4$. The second term in the quotient is $4$, because $4(x) = 4x$ which is the first term in the current dividend. Doing the same process as before gives, $4(x + 1) = 4x + 4$, $4x + 4 - 4x - 4 = 0$. A current dividend of $0$ means that the division is over, and this $0$ is the remainder of the division, and so $\frac{p(x)}{g(x)} = 4x + 4$.

## Polynomial factoring (Factorización de polinomios)

(Factorización de polinomios)
**Polynomial factoring**: factoring applied to a polynomial, treating the polynomial as the product. After doing polynomial factoring, a polynomial is represented as factors that are multiplying each other.

(Máximo factor común de dos expresiones)
**Greatest common factor of two expressions**: the largest expression that is a factor of the two given expressions. For example, given $3x^2 + 6x$ and $9x$, the greatest common factor is $3x$.
[Greatest common factor of two expressions code](Programs/S10/Greatest_common_factor_of_two_expressions.py)

(Máximo factor común de un polinomio)
**Greatest common factor of a polynomial**: the largest expression that is a factor of all the terms in a given polynomial. For example, in $12x^2 + 24x$ the greatest common factor is $12x$.

After doing polynomial factoring, a polynomial is represented as factors that are multiplying each other.
[Polynomial factoring code](Programs/S10/Polynomial_factoring.py)

(Fórmula del punto medio)
**Midpoint formula**: a formula to calculate the midpoint from two points, which can be the endpoints of a segment.

> Midpoint formula
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points in the $x$-$y$ plane, then the midpoint of the segment they form is
> $$\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

(Fórmula general para dividir un segmento en $n$ subsegmentos y calcular la localización del $k$-ésimo subsegmento)
**General formula to divide a segment into $n$ subsegments and get the location of the $k$-th subsegment**: formula to calculate the location of the $k$-th subsegment in a segment divided into $n$ subsegments. $k$ can be greater than $n$, and it can also be negative.
[Divide segment formula code](Programs/S01/Divide_segment_formula.py)

> General formula to divide a segment into $n$ subsegments and get the location of the $k$-th subsegment
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be the two points that define a segment, this segment can be divided into $n$ subsegments. Counting from $(x_1, y_1)$, the coordinates of the $k$-th subsegment are
> $$\left(x_1 + k\frac{x_2 - x_1}{n}, y_1 + k\frac{y_2 - y_1}{n}\right)$$

Making $k = 1$ and $n = 2$ results in the midpoint formula.