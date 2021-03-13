
#   Coordinate systems (Sistemas de coordenadas)

<!--
#T# Table of contents

#C# Rectangular coordinate system (Sistema de coordenadas rectangulares)
#C# Graphs of linear equations (Gráficas de ecuaciones lineales)
#C# Intercept (Intercepto)
#C# Slope of a linear equation (Pendiente de una ecuación lineal)

#T# Beginning of content
-->

(Recta real)
**Number line**: the numbers depicted in a line. This is the most basic one dimensional (1D) coordinate system.
[Number line image code](Programs/S01/Number_line_image.py)
![Number line image](Images/S01/Number_line.png)
*Number line*

(Origen)
**Origin**: this is the point at 0 in all dimensions, e.g. in three dimensions, the origin is $(0, 0, 0)$.

(Coordenada de un punto)
**Coordinate of a point**: an ordered tuple of numbers indicating the location of the point. In the three dimensional tuple $(a, b, c)$, $a$ indicates the location of the point along the first dimension, $b$ indicates the location of the point along the second dimension, and $c$ indicates the location of the point along the third dimension. This pattern continues if the tuple has more numbers.

## Rectangular coordinate system | Coordinate grid (Sistema de coordenadas rectangulares | Plano coordenado)

The rectangular coordinate system is the 2D version of the number line, it is made with a horizontal number line and a vertical number line that cross each other at zero. The positive numbers in the horizontal number line are at the right of zero, and the positive numbers in the vertical number are above zero.

The horizontal number line is called the $x$-axis (el eje $x$) or abscissa axis (eje de abscisas). The vertical number line is called the $y$-axis (el eje $y$) or ordinate axis (eje de ordenadas).

The rectangular coordinate system is also called the $x$-$y$ plane (el plano $x$-$y$), the coordinate plane (el plano coordenado), or the Cartesian coordinate system (el plano cartesiano).

The rectangular coordinate system forms a grid in which there is a vertical line that passes through each number in the $x$-axis, and there is an horizontal line that passes through each number in the $y$-axis.
[Rectangular coordinate system image code](Programs/S01/Rectangular_coordinate_system_image.py)
![Rectangular coordinate system image](Images/S01/Rectangular_coordinate_system.png)
*Rectangular coordinate system*

Each of the four divisions of the $x$-$y$ plane is called a quadrant, they are denoted with roman numerals, $I$, $II$, $III$, and $IV$, as shown in the *Rectangular coordinate system* image.

(Par ordenado)
**Ordered pair**: a pair of numbers that can be used to represent a point in the rectangular coordinate system. Just as in the number line a single number is required to know the location of a point, in the $x$-$y$ plane two numbers are required, which should be ordered to know which number goes in the $x$-axis and which in the $y$-axis. By convention, the first number in an ordered pair indicates the value in the $x$-axis, and the second number indicates the value in the $y$-axis.

> Ordered pair notation
>
> Let $a$, $b$ be two numbers, then the ordered pair made with them is
> $$(a, b)$$

$a$ is the $x$-axis value, and $b$ is the $y$-axis value.

(Punto en el eje)
**Points on the axes**: any point that lies in an axis, i.e. a point whose ordered pair contains at least a zero. A point $(a, 0)$ is in the $x$-axis, and a point $(0, b)$ is in the $y$-axis.

(El origen)
**The origin**: the point in which both axes cross each other, i.e. the point $(0, 0)$.

(Gráfica)
**Graph**: the use of the $x$-$y$ plane to show points. These points can come from a mathematical function or equation, points scattered, etcetera. If the graph comes from an equation, it is read as the graph of the equation (la gráfica de la ecuación). The graph itself is the set of points that result from plotting the equation.

## Graphs of linear equations (Gráficas de ecuaciones lineales)

The graph of a given linear equation shows the solutions of the given linear equation, because the graph is constructed from a few solutions of the equation, and then by extending the line in the graph.
[Graph of a linear equation image code](Programs/S01/Graph_of_a_linear_equation_image.py)
![Graph of a linear equation image](Images/S01/Graph_of_a_linear_equation.png)
*Graph of a linear equation*

A polynomial can be graphed similarly
[Graph of a polynomial image code](Programs/S01/Graph_of_a_polynomial_image.py)
![Graph of a polynomial image](Images/S01/Graph_of_a_polynomial.png)
*Graph of a polynomial*

(Graficar puntos)
**Point plotting method**: individual points from an equation can be plotted, e.g. in a linear equation, individual points can be plotted and then a single line can be passed through them to form the graph of the equation. This method starts by plotting points of a given equation and then joining them with a line or lines as necessary.

(Gráfica de líneas horizontales y verticales)
**Graph of horizontal and vertical lines**: in the $x$-$y$ plane, the equation $x = a$ represents a vertical line that passes through the point $(a, 0)$, and the equation $y = b$ represents an horizontal line that passes through the point $(0, b)$.

## Intercept of a graph (Intercepto de una gráfica)

In a graph, the intercepts are the points in which the graph crosses an axis, i.e. the points of the graph that have a $0$ in the $x$ coordinate or in the $y$ coordinate, or in both.

(Intercepto en $x$)
**$x$-intercept**: an intercept with the $x$-axis, it has the form $(a, 0)$ where $a$ is the $x$ coordinate of the intercept.

(Intercepto en $y$)
**$y$-intercept**: an intercept with the $y$-axis, it has the form $(0, b)$ where $b$ is the $y$ coordinate of the intercept.

A linear equation can be graphed using the intercepts as the points through which the line passes.

(Fórmula de distancia)
**Distance formula**: the distance formula is the application of the Pythagorean theorem in the rectangular coordinate system.

The distance formula takes the distance between two points as the hypotenuse of a right triangle, and the legs as the rise and run in the $x$-$y$ plane.
[Rise and run between two points image code](Programs/S01/Rise_and_run_between_two_points_image.py)
![Rise and run between two points image](Images/S01/Rise_and_run_between_two_points.png)

Using the Pythagorean theorem, the distance squared between two points, is the sum of the squared rise plus the squared run.
[Distance formula code](Programs/S01/Distance_formula.py)

> Distance formula
>
> Let $(x_1, y_1)$, $(x_2, y_2)$, be two points in the $x$-$y$ plane, and let $d$ be the distance between them, then
> $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$