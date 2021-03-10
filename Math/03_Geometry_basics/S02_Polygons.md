
#   Triangles and congruence (Triángulos y congruencia)

<!--
#T# Table of contents

#C# Lines and angles (Líneas y ángulos)
#C# Properties of parallel lines (Propiedades de las líneas paralelas)
#C# Proving lines parallel (Demostrar el paralelismo entre líneas)
#C# Properties of perpendicular lines (Propiedades de las líneas perpendiculares)
#C# Parallel and perpendicular lines in the coordinate plane (Líneas paralelas y perpendiculares en el plano coordenado)
#C# The distance formula (La fórmula de distancia)

#C# Triangle sums (Suma de los ángulos de un triángulo)
#C# Congruent figures (Figuras congruentes)
#C# Triangle congruence using SSS and SAS (Congruencia de triángulos usando LLL y LAL)
#C# Triangle congruence using ASA, AAS, and HL (Congruencia de triángulos usando ALA, AAL, e hipotenusa cateto)
#C# Isosceles and equilateral triangles (Triángulos isósceles y equiláteros)

#C# Midsegments of a triangle (Segmentos medios de un triángulo)
#C# Perpendicular bisectors in triangles (Mediatrices de un triángulo)
#C# Angle bisectors in triangles (Bisectrices de los ángulos de un triángulo)
#C# Medians and altitudes in triangles (Medianas y alturas de un triángulo)
#C# Inequalities in triangles (Desigualdades en los triángulos)

#C# The pythagorean theorem (El teorema de Pitágoras)
#C# Converse of the pythagorean theorem (Converso del teorema de Pitágoras)
#C# Using similar right triangles (Usando triángulos rectángulos similares)
#C# Special right triangles (Triángulos rectángulos especiales)
#C# Tangent, sine and cosine (Tangente, seno y coseno)
#C# Inverse trigonometric ratios (Ratios trigonométricos inversos)
#C# Laws of sines and cosines (Leyes de senos y cosenos)

#C# Angles in polygons (Ángulos en polígonos)
#C# Properties of parallelograms (Propiedades de los paralelogramos)
#C# Proving quadrilaterals are parallelograms (Demostraciones de que un cuadrilátero es un paralelogramo)
#C# Rectangles, rhombuses and squares (Rectángulos, rombos y cuadrados)
#C# Trapezoids and kites (Trapezoides y deltoides)

#T# Beginning of content
-->

#   Lines (Líneas)

## Lines and angles (Líneas y ángulos)

(Paralelismo en geometría)
**Geometric parallelism**: the relationship that is produced when two distinct figures extend indefinitely and never intersect each other.

Two parallel lines that belong to the same plane, extend indefinitely and never intersect each other. Two parallel planes in space, extend indefinitely and never intersect each other. The distance between parallel lines or planes is constant.

> Parallel relation notation
>
> The symbol $\parallel$ indicates a parallel relation. Let $\overleftrightarrow{AB}$, $\overleftrightarrow{CD}$ be two lines, such that they are parallel to each other, this can be denoted as $\overleftrightarrow{AB} \parallel \overleftrightarrow{CD}$, read as the line $AB$ is parallel to the line $CD$ (la línea $AB$ es paralela a la línea $CD$).

In diagrams, parallel lines are indicated by placing arrowheads inside the lines. Each set of parallel lines has its own amount of arrowheads.
[Parallel lines image code](Programs/S03/Parallel_lines_image.py)
![Parallel lines image](Images/S03/Parallel_lines.png)
*Parallel lines*

In the image, $k \parallel l$, which is denoted with one arrowhead inside the lines. Also $m \parallel n$, which is denoted with two arrowheads inside the lines.

(Líneas alabeadas)
**skew lines**: a relationship between two lines, such that they are not parallel but also do not intersect. This is possible in lines that belong to different planes.
[Skew lines image code](Programs/S03/Skew_lines_image.py)
![Skew lines image](Images/S03/Skew_lines.png)
*Skew lines*

The blue line and the crimson line are not parallel, and yet they never intersect, because they lie in different planes.

(Postulado de las paralelas)
**Parallel postulate**: given a line and a point not on the line, there is only one parallel to the line that passes through the point. Given a line $l$ and a point $A$ that does not lie on $l$, then only one line $m$ passes through $A$ and $l \parallel m$.

(Postulado de las perpendiculares)
**Perpendicular postulate**: given a line and a point not on the line, there is only one perpendicular line to the line that passes through the point. Given a line $l$ and a point $A$ that does not lie on $l$, then only one line $m$ passes through $A$ and $l \perp m$.

(Construcción de una línea perpendicular)
**Perpendicular line construction**: a geometric construction to draw the unique perpendicular line to a given line that passes through a given point.

> Perpendicular line construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials).
> 1. Draw a segment and a point outside of it, with space around it.
> 2. Center the compass on the point outside the segment, with a radius that goes beyond the segment. Draw an arc such that it intersects the segment two times.
> 3. Apply the perpendicular bisector construction, taking as endpoints the two arc intersections with the segment. The resulting line is perpendicular to the segment and passes through the point outside of it.
>
> This construction can also be used to draw a perpendicular through a point on the line. In that case, the arc from step 2 is drawn so that it intersects the segment at both sides of the point.

(Construcción de dos líneas paralelas)
**Two parallel lines construction**: a geometric construction to draw two lines such that they are parallel to each other.

> Two parallel lines construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials).
> 1. Draw the first line and a point where the second line will pass through.
> 2. Apply the perpendicular line construction, taking the line and the point from step 1, as the segment and the point needed for that construction.
> 3. Apply the perpendicular line construction again, taking the segment created in step 2, and the point from step 1, as the segment and the point needed for that construction. The result is the two parallel lines connected with a perpendicular line that can be erased if needed.

(Línea transversal)
**Transversal line**: a line that intersects two other distinct lines.
[Transversal line image code](Programs/S03/Transversal_line_image.py)
![Transversal line image](Images/S03/Transversal_line.png)
*Transversal line*

The lime green line is the transversal, although all the lines intersect the other two, which means that effectively all three lines are transversal. The case in which this does not happen, is when the other two lines are parallel.
[Transversal to parallel lines image code](Programs/S03/Transversal_to_parallel_lines_image.py)
![Transversal to parallel lines image](Images/S03/Transversal_to_parallel_lines.png)
*Transversal to parallel lines*

The line $t$ is transversal to the lines $l$ and $m$, and $l \parallel m$. Angles can be denoted with numbers, in the image appear the angles $\angle 1$ through $\angle 8$.

(Partes de una transversal)
**Parts of a transversal**: the following parts will be defined using the *Transversal to parallel lines* image, but these concepts apply to transversals in general.

- **Interior area** (Área interna): the area between the two lines crossed by the transversal, e.g. the area between $l$ and $m$.

- **Exterior area** (Área externa): the area outside of the two lines crossed by the transversal, e.g. the area outside of $l$ and $m$.

- **Corresponding angles** (Ángulos correspondientes): two angles that are in the same position relative to the transversal, but each on a different line, e.g. $\angle 1$ and $\angle 5$ are corresponding angles, like $\angle 2$ and $\angle 6$, also $\angle 3$ and $\angle 7$, and lastly $\angle 4$ and $\angle 8$ form corresponding angle pairs.

- **Alternate interior angles** (Ángulos alternos internos): two angles that lie on the interior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 3$ and $\angle 6$ are alternate interior angles, like $\angle 4$ and $\angle 5$.

- **Alternate exterior angles** (Ángulos alternos externos): two angles that lie on the exterior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 1$ and $\angle 8$ are alternate exterior angles, like $\angle 2$ and $\angle 7$.

- **Same side interior angles** (Ángulos conjugados internos): two angles that lie on the interior area, are distinct, and are on the same side of the transversal, e.g. $\angle 3$ and $\angle 5$ are same side interior angles, like $\angle 4$ and $\angle 6$.

- **Same side exterior angles** (Ángulos conjugados externos): two angles that lie on the exterior area, are distinct, and are on the same side of the transversal, e.g. $\angle 1$ and $\angle 7$ are same side exterior angles, like $\angle 2$ and $\angle 8$.

- **Consecutive angles** (Ángulos consecutivos): same side angles are also known as consecutive angles.

## Properties of parallel lines (Propiedades de las líneas paralelas)

(Postulado de los ángulos correspondientes)
**Corresponding angles postulate**: in a transversal of two parallels, the corresponding angles are congruent. From the *Transversal to parallel lines* image, $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, and $\angle 4 \cong \angle 8$.

(Converso del postulado de los ángulos correspondientes)
**Converse of the corresponding angles postulate**: if the corresponding angles of a transversal are congruent, then the transversal is a transversal of two parallels. From the *Transversal to parallel lines* image, if $\angle 1 \cong \angle 5$, and/or $\angle 2 \cong \angle 6$, and/or $\angle 3 \cong \angle 7$, and/or $\angle 4 \cong \angle 8$, then $l \parallel m$, with transversal $t$.

(Teorema de los ángulos alternos internos)
**Alternate interior angles theorem**: two parallel lines that are intersected by a transversal, have their alternate interior angles congruent.

> Proof of the alternate interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | Given, from the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 1 \cong \angle 4$ | Vertical angles theorem |
> | $\angle 4 \cong \angle 5$ | Transitive property of congruence |

The same proof applies for the other three pairs of alternate interior angles.

From the *Transversal to parallel lines* image, $\angle 3 \cong \angle 6$ and $\angle 4 \cong \angle 5$.

(Teorema de los ángulos alternos externos)
**Alternate exterior angles theorem**: two parallel lines that are intersected by a transversal, have their alternate exterior angles congruent.

> Proof of the alternate exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | Given, from the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 5 \cong \angle 8$ | Vertical angles theorem |
> | $\angle 1 \cong \angle 8$ | Transitive property of congruence |

The same proof applies for the other three pairs of alternate exterior angles.

From the *Transversal to parallel lines* image, $\angle 1 \cong \angle 8$ and $\angle 2 \cong \angle 7$.

(Teorema de los ángulos conjugados internos)
**Same side interior angles theorem**: two parallel lines that are intersected by a transversal, have supplementary same side interior angles.

> Proof of the same side interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | Given, from the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 1$ and $\angle 3$ are supplementary | Linear pair postulate |
> | $\angle 3$ and $\angle 5$ are supplementary | Converse of the congruent supplements theorem |

The same proof applies for the other pair of same side interior angles.

From the *Transversal to parallel lines* image, $\angle 3$ and $\angle 5$ are supplementary, and $\angle 4$ and $\angle 6$ are supplementary.

(Teorema de los ángulos conjugados externos)
**Same side exterior angles theorem**: two parallel lines that are intersected by a transversal, have supplementary same side exterior angles.

> Proof of the same side exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | Given, from the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 5$ and $\angle 7$ are supplementary | Linear pair postulate |
> | $\angle 1$ and $\angle 7$ are supplementary | Converse of the congruent supplements theorem |

The same proof applies for the other pair of same side exterior angles.

From the *Transversal to parallel lines* image, $\angle 1$ and $\angle 7$ are supplementary, and $\angle 2$ and $\angle 8$ are supplementary.

## Proving lines parallel (Demostrar el paralelismo entre líneas)

(Converso del teorema de los ángulos alternos internos)
**Converse of the alternate interior angles theorem**: given two lines intersected by a transversal, if their alternate interior angles are congruent, then the two lines are parallel.

> Proof of the converse of the alternate interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 3 \cong \angle 6$ | Given, from the *Transversal to parallel lines* image |
> | $\angle 3 \cong \angle 2$ | Vertical angles theorem |
> | $\angle 2 \cong \angle 6$ | Transitive property of congruence |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

From the *Transversal to parallel lines* image, if $\angle 3 \cong \angle 6$ and/or $\angle 4 \cong \angle 5$, then $l \parallel m$, with transversal $t$.

(Converso del teorema de los ángulos alternos externos)
**Converse of the alternate exterior angles theorem**: given two lines intersected by a transversal, if their alternate exterior angles are congruent, then the two lines are parallel.

> Proof of the converse of the alternate exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 1 \cong \angle 8$ | Given, from the *Transversal to parallel lines* image |
> | $\angle 5 \cong \angle 8$ | Vertical angles theorem |
> | $\angle 1 \cong \angle 5$ | Transitive property of congruence |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

From the *Transversal to parallel lines* image, if $\angle 1 \cong \angle 8$ and/or $\angle 2 \cong \angle 7$, then $l \parallel m$, with transversal $t$.

(Converso del teorema de los ángulos conjugados internos)
**Converse of the same side interior angles theorem**: given two lines intersected by a transversal, if their same side interior angles are supplementary, then the two lines are parallel.

> Proof of the converse of the same side interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 3$ and $\angle 5$ are supplementary | Given, from the *Transversal to parallel lines* image |
> | $\angle 1$ and $\angle 3$ are supplementary | Linear pair postulate |
> | $\angle 1 \cong \angle 5$ | Congruent supplements theorem |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

From the *Transversal to parallel lines* image, if $\angle 3$ and $\angle 5$ are supplementary, and $\angle 4$ and $\angle 6$ are supplementary, then $l \parallel m$, with transversal $t$.

(Converso del teorema de los ángulos conjugados externos)
**Converse of the same side exterior angles theorem**: given two lines intersected by a transversal, if their same side exterior angles are supplementary, then the two lines are parallel.

> Proof of the converse of the same side exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 1$ and $\angle 7$ are supplementary | Given, rom the *Transversal to parallel lines* image |
> | $\angle 5$ and $\angle 7$ are supplementary | Linear pair postulate |
> | $\angle 1 \cong \angle 5$ | Congruent supplements theorem |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

From the *Transversal to parallel lines* image, if $\angle 1$ and $\angle 7$ are supplementary, and/or $\angle 2$ and $\angle 8$ are supplementary, then $l \parallel m$, with transversal $t$.

(Propiedad transitiva de las líneas paralelas)
**Transitive property of parallel lines**: given two parallel lines, if the first one is parallel to a third line, then the second line is also parallel to the third.

> Transitive property of parallel lines
>
> Let $k$, $l$, $m$, be lines, if $k \parallel l$ and $l \parallel m$, then $k \parallel m$.

## Properties of perpendicular lines (Propiedades de las líneas perpendiculares)

(Teorema de los pares lineales congruentes)
**Congruent linear pairs theorem**: in a linear pair, if the two angles are congruent, then they have a measure of $\pi/2$, meaning that if both angles of a linear pair are congruent then they are right angles.

> Proof of the congruent linear pairs theorem
>
> Let $\angle A$ and $\angle B$ form a linear pair, and let $\angle A \cong \angle B$, then $m \angle A = m \angle B$, $m \angle A + m \angle B = \pi \Rightarrow 2 m \angle A = \pi \Rightarrow m \angle A = \pi/2 = m \angle B$. So $\angle A$ and $\angle B$ are right angles. $\blacksquare$

If $\angle A$ and $\angle B$ form a linear pair, and $\angle A \cong \angle B$, then $\angle A$ and $\angle B$ are right angles.

(Teorema de las transversales perpendiculares)
**Perpendicular transversals theorem**: given three lines, if the first and second lines are parallel, and the first line is perpendicular to the third line, then the second line is also perpendicular to the third line.
[Perpendicular transversal image code](Programs/S03/Perpendicular_transversal_image.py)
![Perpendicular transversal image](Images/S03/Perpendicular_transversal.png)
*Perpendicular transversal*

> Proof of the perpendicular transversals theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$ and $l \perp t$ | Given |
> | $\angle 1$, $\angle 2$, $\angle 3$, $\angle 4$, are right angles | Definition of perpendicular lines |
> | $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, $\angle 4 \cong \angle 8$, so $\angle 4$, $\angle 5$, $\angle 6$, $\angle 7$, are right angles | Corresponding angles postulate |
> | $m \perp t$ | Definition of perpendicular lines |

If $l \parallel m$ and $l \perp t$, then $m \perp t$.

(Converso del teorema de las transversales perpendiculares)
**Converse of the perpendicular transversals theorem**: if a first line and a second line are perpendicular to a third line, then the first and second lines are parallel.

> Proof of the converse of the perpendicular transversals theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \perp t$ and $m \perp t$ | Given, from the *Perpendicular transversal* image |
> | All the angles, from $\angle 1$ to $\angle 8$ are right angles | Definition of perpendicular lines |
> | $\angle 1 \cong \angle 5$ | Right angle theorem |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

If $l \perp t$ and $m \perp t$, then $l \parallel m$.

(Teorema de los ángulos complementarios adyacentes)
**Adjacent complementary angles theorem**: if two angles are adjacent and complementary, then the two non-shared sides form a right angle.

> Proof of the adjacent complementary angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$ and $\angle B$ be two adjacent complementary angles | Given |
> | $m \angle A + m \angle B = \pi/2$ | Definition of complementary angles |
> | The angle between the non-shared sides is a right angle | Definition of a right angle |

If $\angle A$ and $\angle B$ are adjacent complementary angles, then $m \angle A + m \angle B = \pi/2$, so the angle between the non-shared sides is a right angle.

(Converso del teorema de los ángulos complementarios adyacentes)
**Converse of the adjacent complementary angles theorem**: if the non-shared sides of two adjacent angles form a right angle, then the angles are complementary.

> Proof of the converse of the adjacent complementary angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$ and $\angle B$ be adjacent angles, with the non-shared sides forming a right angle | Given |
> | $m \angle A + m \angle B = \pi/2$ | Definition of right angle |
> | $\angle A$ and $\angle B$ are complementary | Definition of complementary angles |

If $\angle A$ and $\angle B$ are adjacent angles, with the non-shared sides forming a right angle, then $\angle A$ and $\angle B$ are complementary.

## Parallel and perpendicular lines in the coordinate plane (Líneas paralelas y perpendiculares en el plano coordenado)

(Pendiente de una línea)
**Slope of a line**: the amount of inclination of a line. An horizontal line has zero slope, a vertical line has undefined (positive or negative infinity) slope.

From basic algebra, the slope of a line can be defined as an equation in terms of the $x$-$y$ plane coordinates of two points on the line.

> Algebraic definition of the slope of a line
>
> Let $(x_1, y_1)$, $(x_2, y_2)$, be two points on the $x$-$y$ plane, and let $m$ be the slope of the line that passes through these two points, then
> $$m = \frac{y_2 - y_1}{x_2 - x_1}$$

According to this definition of the slope of a line, a positive slope means a line that goes upwards from left to right, and a negative slope means a line that goes downwards from left to right.
[Values of the slope of a line image code](Programs/S03/Values_of_the_slope_of_a_line_image.py)
![Values of the slope of a line image](Images/S03/Values_of_the_slope_of_a_line.png)
*Values of the slope of a line*

The rise (elevación) of a slope is the amount changed in the $y$ axis, namely $y_2 - y_1$. The run (avance) of a slope is the amount changed in the $x$ axis, namely $x_2 - x_1$. So the algebraic definition of the slope can also be interpreted as rise over run.

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
[Slope of perpendicular lines image code](Programs/S03/Slope_of_perpendicular_lines_image.py)
![Slope of perpendicular lines image](Images/S03/Slope_of_perpendicular_lines.png)

The blue line is the first line, the lime green line has a slope that is the opposite of the slope of the blue line. The crimson line is perpendicular to the blue line, and has a slope that is the reciprocal of the slope of the lime green line.

## The distance formula (La fórmula de distancia)

The distance formula is the application of the Pythagorean theorem in the rectangular coordinate system.

(Teorema de Pitágoras)
**Pythagorean theorem**: in a right triangle the length of the largest side squared is equal to the sum of the other two lengths individually squared. The largest side is named the hypotenuse (hipotenusa), and the other sides are called legs (catetos).

> Pythagorean theorem
>
> Let $a$, $b$, $c$, be the sides of a right triangle, with $a$ and $b$ being the legs, and $c$ being the hypotenuse, then
> $$c^2 = a^2 + b^2$$

This theorem can be proved with the following image.
![Pythagorean theorem image](../01_Algebra_basics/Images/S09/Pythagorean_theorem.png)
*Pythagorean theorem*

> Proof of the pythagorean theorem
>
> From the image, $(a + b)^2 = c^2 + 2 a b$, then $a^2 + 2 a b + b^2 = c^2 + 2 a b$, and then $a^2 + b^2 = c^2$. $\blacksquare$

The distance formula takes the distance between two points as the hypotenuse of a right triangle, and the legs as the rise and run in the $x$-$y$ plane.
[Rise and run between two points image code](Programs/S03/Rise_and_run_between_two_points_image.py)
![Rise and run between two points image](Images/S03/Rise_and_run_between_two_points.png)

Using the Pythagorean theorem, the distance squared between two points, is the sum of the squared rise plus the squared run.
[Distance formula code](Programs/S03/Distance_formula.py)

> Distance formula
>
> Let $(x_1, y_1)$, $(x_2, y_2)$, be two points in the $x$-$y$ plane, and let $d$ be the distance between them, then
> $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

(Distancia más corta entre un punto y una recta)
**Shortest distance between a point and a line**: given a point and a line, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line to the given line that passes through the given point, is used to measure this shortest distance, as the distance between the given point and the intersection of the perpendicular line and the given line.
[Shortest distance between a point and a line image code](Programs/S03/Shortest_distance_between_a_point_and_a_line_image.py)
![Shortest distance between a point and a line image](Images/S03/Shortest_distance_between_a_point_and_a_line.png)
*Shortest distance between a point and a line*

The shortest distance between the point $A$ and the line $l$ is the distance $AB$.

> Algorithm to find the shortest distance between a point and a line
>
> 1. Use the *Shortest distance between a point and a line* image, let $A$ be the point and $l$ be the line, such that the line $l$ is defined by the equation $y = m_1x + b_1$, and let $B$ be the point of intersection of the line $l$ and a perpendicular line to it that passes through $A$. The shortest distance being measured is the distance $AB$.
> 2. Calculate the slope of the perpendicular line as $m_2 = -\frac{1}{m_1}$.
> 3. Calculate the $y$-intercept of the perpendicular line as $b_2 = y_A - m_2x_A$, where $x_A$ and $y_A$ are the $x$ and $y$ coordinates of the point $A$ respectively.
> 4. Find the coordinates of the point of intersection $B$, namely $x_B$, $y_B$, by equating the equation of the line $l$ and the equation of the perpendicular line, $m_1x_B + b_1 = m_2x_B + b_2$. From this equation, isolate $x_B$ as $x_B = \frac{b_2 - b_1}{m_1 - m_2}$.
> 5. Find $y_B$ as $y_B = m_1x_B + b_1$.
> 6. Calculate the distance between $A$ and $B$ with the distance formula, $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.

(Distancia más corta entre dos líneas paralelas)
**Shortest distance between two parallel lines**: given two parallel lines, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line that passes through both parallel lines, is used to measure this shortest distance, as the distance between the two intersections of the perpendicular line with the two parallel lines.

> Algorithm to find the shortest distance between two parallel lines
>
> 1. Pick a point in one of the two parallel lines, name it $A$.
> 2. Apply the Process to find the shortest distance between a point and a line, using $A$ as a point, and the line is the other parallel line that does not contain $A$. The result is the shortest distance between the two parallel lines.

By definition of parallel lines, the shortest distance between them is a constant.

## Triangle sums (Suma de los ángulos de un triángulo)

(Ángulos interiores de un polígono)
**Interior angles of a polygon**: each of the angles at any of the vertices of the polygon, that is inside the polygon.
[Interior angles of a polygon image code](Programs/S04/Interior_angles_of_a_polygon_image.py)
![Interior angles of a polygon image](Images/S04/Interior_angles_of_a_polygon.png)
*Interior angles of a polygon*

The angle $\angle A$ is an interior angle of the polygon. Each vertex has an interior angle.

(Teorema de la suma de los ángulos interiores de un triángulo)
**Triangle interior angles sum theorem**: the sum of the interior angles of a triangle, is exactly $\pi$.
[Triangle interior angles sum image code](Programs/S04/Triangle_interior_angles_sum_image.py)
![Triangle interior angles sum image](Images/S04/Triangle_interior_angles_sum.png)
*Triangle interior angles sum*

> Proof of the triangle interior angles sum theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The $\triangle ABC$ exists, and $\overleftrightarrow{CD} \parallel \overline{AB}$ | Given |
> | $\angle 1 \cong \angle 4$ and $\angle 2 \cong \angle 5$ | Alternate interior angles theorem |
> | $m \angle 1 = m \angle 4$ and $m \angle 2 = m \angle 5$ | Definition of congruence |
> | $m \angle 4 + m \angle ACD = \pi$ | Linear pair postulate |
> | $m \angle ACD = m \angle 3 + m \angle 5$ | Angle addition postulate |
> | $m \angle 4 + m \angle 3 + m \angle 5 = \pi$ | Substitution property of equality |
> | $m \angle 1 + m \angle 3 + m \angle 2 = \pi$ | Substitution property of equality |
> | $m \angle 1 + m \angle 2 + m \angle 3 = \pi$ | Commutative property of addition |

In $\triangle ABC$, $m \angle A + m \angle B + m \angle C = \pi$

(Ángulos exteriores de un polígono)
**Exterior angles of a polygon**: each of the angles at any of the vertices of the polygon, that is outside the polygon, formed by a side of the vertex and the extension of the other side.
[Exterior angles of a polygon image code](Programs/S04/Exterior_angles_of_a_polygon_image.py)
![Exterior angles of a polygon image](Images/S04/Exterior_angles_of_a_polygon.png)
*Exterior angles of a polygon*

The angle $\angle B$ is an exterior angle of the polygon. Given that each vertex in a polygon has two sides, two exterior angles can be drawn from each vertex, both being congruent to each other due to the vertical angles theorem.

In a given vertex of a polygon, the interior angle and one exterior angle (any of the two) form a linear pair, which means they are supplementary.

(Teorema de la suma de los ángulos exteriores de un triángulo)
**Triangle exterior angle sum theorem**: the sum of the exterior angles of a triangle is exactly $2 \pi$, taking only one exterior angle per vertex.
[Triangle exterior angle sum theorem image code](Programs/S04/Triangle_exterior_angle_sum_theorem_image.py)
![Triangle exterior angle sum theorem image](Images/S04/Triangle_exterior_angle_sum_theorem.png)
*Triangle exterior angle sum theorem*

> Proof of the triangle exterior angle sum theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $m \angle 1 + m \angle 2 + m \angle 3 = \pi$ | Triangle interior angles sum theorem |
> | $m \angle 1 + m \angle 4 = \pi$, $m \angle 2 + m \angle 5 = \pi$, and $m \angle 3 + m \angle 6 = \pi$ | Linear pair postulate |
> | $m \angle 1 = \pi - m \angle 4$, $m \angle 2 = \pi - m \angle 5$, and $m \angle 3 = \pi - m \angle 6$ | Subtraction property of equality |
> | $\pi - m \angle 4 + \pi - m \angle 5 + \pi - m \angle 6 = \pi$ | Substitution property of equality |
> | $3 \pi - \pi = m \angle 4 + m \angle 5 + m \angle 6$ | Subtraction property of equality (for $\pi$), addition property of equality (for the angles), and commutative property of addition (to add the $\pi$s) |
> | $m \angle 4 + m \angle 5 + m \angle 6 = 2 \pi$ | Reflexive property of equality |

In $\triangle ABC$, $m \angle A_{ext} + m \angle B_{ext} + m \angle C_{ext} = 2 \pi$. The $ext$ subindex indicates an exterior angle.

(Ángulos interiores remotos)
**Remote interior angles**: the interior angles that are not adjacent to a given exterior angle. In a triangle, given an exterior angle, the remote interior angles are the two interior angles that are not adjacent to said exterior angle.
[Remote interior angles image code](Programs/S04/Remote_interior_angles_image.py)
![Remote interior angles image](Images/S04/Remote_interior_angles.png)
*Remote interior angles*

In the triangle $\triangle ABC$, the marked angle $\angle DAC$ is an exterior angle, its two remote interior angles are $\angle B$ and $\angle C$. The auxiliary segment $\overline{AC_2}$ is placed there to show that the measure of $\angle DAC$ can be seen as the sum of the measures of $\angle B$ and $\angle C$, with the corresponding angles postulate for $\angle B$, and the alternate interior angles theorem for $\angle C$. This is proven in the exterior angle of a triangle theorem.

(Teorema del ángulo exterior de un triángulo)
**Exterior angle of a triangle theorem**: in a triangle, the measure of an exterior angle is equal to the sum of the measures of its two remote interior angles.

> Proof of the exterior angle of a triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The angle $\angle DAC$ is an exterior angle, and the angles $\angle B$ and $\angle C$ are the remote interior angles relative to $\angle DAC$ | Given |
> | $m \angle A + m \angle B + m \angle C = \pi$ | Triangle interior angles sum theorem |
> | $m \angle A + m \angle DAC = \pi$ | Linear pair postulate |
> | $m \angle A + m \angle DAC = m \angle A + m \angle B + m \angle C$ | Transitive property of equality |
> | $m \angle DAC = m \angle B + m \angle C$ | Subtraction property of equality |

In $\triangle ABC$, $m \angle A_{ext} = m \angle B + m \angle C$.

## Congruent figures (Figuras congruentes)

(Triángulos congruentes)
**Congruent triangles**: given two triangles, they are congruent if their corresponding sides are congruent and their corresponding angles are congruent.
[Congruent triangles images code](Programs/S04/Congruent_triangles_image.py)
![Congruent triangles image](Images/S04/Congruent_triangles.png)
*Congruent triangles*

The triangle $\triangle ABC$ is congruent to the triangle $\triangle DEF$, because their corresponding sides are congruent and their corresponding angles are congruent.

> Triangle congruence
>
> The congruence $\triangle ABC \cong \triangle DEF$, is true because $\overline{AB} \cong \overline{DE}$, $\overline{AC} \cong \overline{DF}$, $\overline{BC} \cong \overline{EF}$, $\angle A \cong \angle D$, $\angle B \cong \angle E$, and $\angle C \cong \angle F$. This can be expressed as "corresponding parts of congruent triangles are congruent".

In the statement $\triangle ABC \cong \triangle DEF$ the order of the vertices follows the congruence.

(Teorema del tercer ángulo)
**Third angle theorem**: given two triangles, if two pairs of angles are congruent, then the third pair of angles is congruent.

> Proof of the third angle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The triangles $\triangle ABC$ and $\triangle DEF$, have $\angle A \cong \angle D$ and $\angle B \cong \angle E$ | Given |
> | $m \angle A = m \angle D$, $m \angle B = m \angle E$ | Definition of congruence |
> | $m \angle A + m \angle B + m \angle C = \pi$, $m \angle D + m \angle E + m \angle F = \pi$ | Triangle interior angles sum theorem |
> | $m \angle A + m \angle B + m \angle C = m \angle D + m \angle E + m \angle F$ | Transitive property of equality |
> | $m \angle A + m \angle B + m \angle C = m \angle A + m \angle B + m \angle F$ | Substitution property of equality |
> | $m \angle C = m \angle F$ | Subtraction property of equality |
> | $\angle C \cong \angle F$ | Definition of congruence |

In the triangles $\triangle ABC$ and $\triangle DEF$ if $\angle A \cong \angle D$ and $\angle B \cong \angle E$, then $\angle C \cong \angle F$.

## Triangle congruence using SSS and SAS (Congruencia de triángulos usando LLL y LAL)

(Construcción de un triángulo dados tres lados)
**Triangle from three sides construction**: a geometric construction to draw a triangle, given the lengths of its three sides.

> Triangle from three sides construction
>
> This construction requires paper, pencil, ruler, and compass (or equivalent tools and materials).
> 1. Set the measures of the three sides from the triangle to draw. Let $a$, $b$, $c$ be the measures of the three sides respectively.
> 2. Draw the length $a$ as a segment.
> 3. Open the compass to the length of $b$. Center the compass in one of the endpoints of the segment from step 2 and draw a wide arc.
> 4. Open the compass to the length of $c$. Center the compass in the other endpoint of the segment from step 2 and draw a wide arc, such that it intersects with the arc from step 3.
> 5. Draw two segments, one from each endpoint of the segment from step 2 to the intersection of the arcs. The result is the triangle given the three measures of its sides.

(Postulado LLL de congruencia de triángulos)
**SSS triangle congruence postulate**: SSS stands for Side-Side-Side (Lado-Lado-Lado). This postulate says that two triangles with side-side-side of the same lengths, are congruent, i.e. if the three sides of a triangle are individually congruent to the three sides of another triangle, then the two triangles are congruent.

> SSS triangle congruence postulate
>
> Let $\triangle ABC$ have sides with measures $a$, $b$, $c$, and $\triangle DEF$ have sides with measures $d$, $e$, $f$. If $a = d$, $b = e$, and $c = f$, then $\triangle ABC \cong \triangle DEF$.

(Ángulo comprendido entre dos lados)
**Included angle between two sides**: the angle between two given sides, is the included angle, so the sides must share a vertex, which is the vertex of the angle.

(Construcción de un triángulo dados dos lados y su ángulo comprendido)
**Triangle from two sides and their included angle construction**: a geometric construction to draw a triangle given two sides and their included angle.

> Triangle from two sides and their included angle construction
>
> This construction requires paper, pencil, ruler, and protractor (or equivalent tools and materials).
> 1. Set the two measures of the sides, and the measure of their included angle from the triangle to draw. Let $a$, $c$ be the measures of the two sides, and $\beta$ be the measure of the included angle.
> 2. Draw the length $a$ as a segment.
> 3. Measure the angle $\beta$ using the segment from step 2 as the first side of the angle. Mark the angle.
> 4. Draw the length $c$ as a segment in the direction of the angle mark from step 3.
> 5. Join the remaining two points to close the triangle. The result is the triangle.

(Postulado LAL de congruencia de triángulos)
**SAS triangle congruence postulate**: SAS stands for Side-Angle-Side (Lado-Ángulo-Lado). This postulate says that if two sides and their included angle are individually congruent to two sides and their included angle of another triangle, then the two triangles are congruent.

> SAS triangle congruence postulate
>
> Let $\triangle ABC$ have two sides with measures $a$, $c$, and let their included angle measure $\beta$. Let $\triangle DEF$ have two sides with measures $d$, $f$, and let their included angle measure $\epsilon$. If $a = d$, $c = f$, and $\beta = \epsilon$, then $\triangle ABC \cong \triangle DEF$.

## Triangle congruence using ASA, AAS, and HL (Congruencia de triángulos usando ALA, AAL, e hipotenusa cateto)

(Lado comprendido entre dos ángulos)
**Included side between two angles**: a side that is common to two differnt angles. The angles surround the side by placing themselves at each endpoint of the side.

(Construcción de un triángulo dados dos ángulos y su lado comprendido)
**Triangle from two angles and their included side construction**: geometric construction to draw a triangle given two angles and their included side.

> Triangle from two angles and their included side construction
>
> This construction requires paper, pencil, ruler, and protractor (or equivalent tools and materials).
> 1. Set the two measures of the angles, and the measure of their included side from the triangle to draw. Let $\alpha$, $\gamma$ be the measures of the two angles, and $b$ be the measure of the included side.
> 2. Draw the length $b$ as a segment.
> 3. Measure the angle $\alpha$ using the segment from step 2 as the first side of the angle. Mark the angle.
> 4. Repeat step 3 but with the angle $\gamma$, with vertex on the remaining endpoint of the segment from step 2.
> 5. Extend the lines in each of the marked angles from step 3 and step 4 so that they cross each other. The result is the triangle.

(Postulado ALA de congruencia de triángulos)
**ASA triangle congruence postulate**: ASA stands for Angle-Side-Angle (Ángulo-Lado-Ángulo). This postulate says that if two angles and their included side are individually congruent to two angles and their included side in another triangle, then the two triangles are congruent.

> ASA triangle congruence postulate
>
> Let $\triangle ABC$ have two angles with measures $\alpha$, $\gamma$, and let their included side measure $b$. Let $\triangle DEF$ have two angles with measures $\delta$, $\zeta$, and let their included side measure $e$. If $\alpha = \delta$, $\gamma = \zeta$, and $b = e$, then $\triangle ABC = \triangle DEF$.

(Teorema AAL de congruencia de triángulos)
**AAS triangle congruence theorem**: AAS stands for Angle-Angle-Side (Ángulo-Ángulo-Lado). This theorem says that if two angles and one of their non included sides are individually congruent to two angles and one of their non included sides in another triangle, then the two triangles are congruent. This result is equivalent for an SAA configuration.
[AAS triangle congruence theorem image code](Programs/S04/AAS_triangle_congruence_theorem_image.py)
![AAS triangle congruence theorem image](Images/S04/AAS_triangle_congruence_theorem.png)
*AAS triangle congruence theorem*

> Proof of the AAS triangle congruence theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle A \cong \angle D$, $\angle B \cong \angle E$, and $\overline{BC} \cong \overline{EF}$ | Given |
> | $\angle C \cong \angle F$ | Third angle theorem |
> | $\overline{BC}$ is the included side of $\angle B$ and $\angle C$, and $\overline{EF}$ is the included side of $\angle E$ and $\angle F$ | Definition of included side between two angles |
> | $\triangle ABC \cong \triangle DEF$ | ASA triangle congruence postulate |

In the triangles $\triangle ABC$ and $\triangle DEF$, if $\angle A \cong \angle D$, $\angle B \cong \angle E$, and $\overline{BC} \cong \overline{EF}$, then $\triangle ABC \cong \triangle DEF$.

(Teorema de la congruencia de la hipotenusa-cateto)
**Hypotenuse-leg congruence theorem**: given two right triangles, if the hypotenuse and one leg in one triangle, are congruent to the hypotenuse and one leg in the other triangle, then the two triangles are congruent.

> Proof of the hypotenuse-leg congruence theorem
>
> All right triangles have at least one congruent angle with each other, the right angle. If the hypotenuse of one of the legs is congruent in two triangles, then the two triangles are congruent because of the AAS triangle congruence theorem. $\blacksquare$

In right triangles $\triangle ABC$ and $\triangle DEF$, if the hypotenuses are congruent $\overline{AC} \cong \overline{DF}$ and two corresponding legs are congruent $\overline{AB} \cong \overline{DE}$, then $\triangle ABC \cong \triangle DEF$.

The configurations AAA and SSA do not necessarily lead to congruent triangles.

## Isosceles and equilateral triangles (Triángulos isósceles y equiláteros)

(Partes de un triángulo isósceles)
**Isosceles triangle parts**: in an isosceles triangle, the congruent sides are called the legs (patas), the remaining side is called the base (base). The two angles formed by the base and each of the legs, are called base angles (ángulos de la base), and the included angle of the two legs is called the vertex angle (ángulo del vértice).
[Isosceles triangle parts image code](Programs/S04/Isosceles_triangle_parts_image.py)
![Isosceles triangle parts image](Images/S04/Isosceles_triangle_parts.png)
*Isosceles triangle parts*

(Teorema de los ángulos de la base)
**Base angles theorem**: in an isosceles triangle, the base angles are congruent.
[Base angles theorem image code](Programs/S04/Base_angles_theorem_image.py)
![Base angles theorem image](Images/S04/Base_angles_theorem.png)
*Base angles theorem*

> Proof of the base angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{BC}$, $\angle ABD \cong \angle CBD$ | Given |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle CBD$ | SAS triangle congruence postulate |
> | $\angle A \cong \angle C$ | Corresponding parts of congruent triangles are congruent |

In an isosceles triangle $\triangle ABC$, such that $\overline{AB} \cong \overline{BC}$, then $\angle A \cong \angle C$.

(Converso del teorema de los ángulos de la base)
**Converse of the base angles theorem**: if two angles in a triangle are congruent, it is an isosceles triangle.

> Proof of the converse of the base angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle A \cong \angle C$ | Given, from the *Base angles theorem* image |
> | $\angle ABD \cong \angle CBD$ | Definition of angle bisector |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle CBD$ | AAS triangle congruence theorem |
> | $\overline{AB} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |
> | $\triangle ABC$ is isosceles | Definition of isosceles triangle |

In a triangle $\triangle ABC$, if $\angle A \cong \angle C$, then $\triangle ABC$ is isosceles.

(Teorema del triángulo isósceles)
**Isosceles triangle theorem**: in an isosceles triangle, the angle bisector of the vertex angle is a perpendicular bisector of the base.

> Proof of the isosceles triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\triangle ABC$ is isosceles, $\overline{AB} \cong \overline{BC}$, and $\overline{BD}$ is the angle bisector | Given, from the *Base angles theorem* image |
> | $\angle A \cong \angle C$ | Base angles theorem |
> | $\angle ABD \cong \angle CBD$ | Definition of angle bisector |
> | $\triangle ABD \cong \triangle CBD$ | AAS triangle congruence theorem |
> | $\angle ADB$ and $\angle CDB$ are supplementary | Linear pair postulate |
> | $\angle ADB \cong \angle CDB$ | Corresponding parts of congruent triangles are congruent |
> | $\angle ADB$ and $\angle CDB$ are right angles | Congruent linear pairs theorem |
> | $\overline{BD} \perp \overline{AC}$ | Definition of perpendicular lines |
> | $\overline{AD} \cong \overline{CD}$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$ | Definition of perpendicular bisector |

If $\triangle ABC$ is isosceles, such that $\overline{AB} \cong \overline{BC}$, $D$ is a point in $\overline{AC}$, and $\overline{BD}$ is the angle bisector of $\angle ABC$, then $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$.

(Converso del teorema del triángulo isósceles)
**Converse of the isosceles triangle theorem**: in an isosceles triangle, the perpendicular bisector of the base is an angle bisector of the vertex angle.

> Proof of the converse of the isosceles triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$ | Given, from the *Base angles theorem* image |
> | $\overline{AD} \cong \overline{CD}$, $\angle ADB \cong \angle CDB$ | Definition of perpendicular bisector |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle CBD$ | SAS triangle congruence postulate |
> | $\angle ABD \cong \angle CBD$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{BD}$ is an angle bisector of $\angle ABC$ | Definition of angle bisector |

If $\triangle ABC$ is isosceles, $D$ is a point in $\overline{AC}$, and $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$, then $\overline{BD}$ is an angle bisector of $\angle ABC$.

(Teorema de los triángulos equiláteros)
**Equilateral triangles theorem**: an equilateral triangle is also equiangular.

> Proof of the equilateral triangles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\triangle ABC$ has sides with measures $a$, $b$, $c$, such that $a = b = c$ | Given |
> | $\angle A \cong \angle B$ | Base angles theorem |
> | $\angle B \cong \angle C$ | Base angles theorem |
> | $\angle A \cong \angle C$ | Transitive property of congruence |

If a triangle $\triangle ABC$ has sides with measures $a$, $b$, $c$, such that $a = b = c$, then $\angle A \cong \angle B \cong \angle C$.

(Converso del teorema de los triángulos equiláteros)
**Converse of the equilateral triangles theorem**: an equiangular triangle is also equilateral.

> Proof of the converse of the equilateral triangles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\triangle ABC$ has $\angle A \cong \angle B \cong \angle C$, and sides with measures $a$, $b$, $c$ | Given |
> | $a = b$ | Converse of the base angles theorem |
> | $b = c$ | Converse of the base angles theorem |
> | $a = c$ | Transitive property of equality |

If a triangle $\triangle ABC$ has $\angle A \cong \angle B \cong \angle C$, then its measures $a$, $b$, $c$ are equal, $a = b = c$.

#   Relationships with triangles (Propiedades de los triángulos)

## Midsegments of a triangle (Segmentos medios de un triángulo)

(Segmento medio de un triángulo)
**Midsegment of a triangle**: in a triangle, the midsegment is a segment that connects the two midpoints of adjacent sides.
[Midsegment of a triangle image code](Programs/S05/Midsegment_of_a_triangle_image.py)
![Midsegment of a triangle image](Images/S05/Midsegment_of_a_triangle.png)
*Midsegment of a triangle*

The segment $\overline{DE}$ is a midsegment of the triangle $\triangle ABC$.

Every triangle has three midsegments.
[Three midsegments of a triangle image code](Programs/S05/Three_midsegments_of_a_triangle_image.py)
![Three midsegments of a triangle image](Images/S05/Three_midsegments_of_a_triangle.png)
*Three midsegments of a triangle*

(Teorema del segmento medio de un triángulo)
**Midsegment of a triangle theorem**: a midsegment of a triangle measures half the length of its parallel side.

> Proof of the midsegment of a triangle theorem
>
> The proof of this theorem requires the concept of similarity. Two figures are similar when they have the same shape but not necessarily the same size. By SAS, the triangle $\triangle ABC$ is similar to $\triangle DEC$. Given that $D$ is the midpoint of $\overline{AC}$, then $\overline{CD}$ has half the length of $\overline{AC}$, and so by similarity, the scale factor needed to obtain $\triangle DEC$ from $\triangle ABC$ is one half, therefore the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$. $\blacksquare$

In a triangle $\triangle ABC$, if $\overline{DE}$ is a midsegment of $\triangle ABC$ that is parallel to $\overline{AB}$, then the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$, or $DE = \frac{AB}{2}$.

(Converso del teorema del segmento medio de un triángulo)
**Converse of the midsegment of a triangle theorem**: in a triangle, if a segment connects two sides, is parallel to the non-connected side, and measures half the length of its parallel side, then the segment is a midsegment of the triangle.

> Proof of the converse of the midsegment of a triangle theorem
>
> Similarly to the proof of the midsegment of a triangle theorem, by similarity, the triangle $\triangle ABC$ is similar to $\triangle DEC$, because by the corresponding angles postulate, $\angle ABC \cong \angle CED$ and $\angle BAC \cong \angle CDE$. The scale factor needed to obtain $\triangle ABC$ from $\triangle DEC$ is two, because $\overline{AB}$ has double the length of $\overline{DE}$. Using this scale factor, $\overline{AC}$ has double the length of $\overline{CD}$, and $\overline{BC}$ has double the length of $\overline{CE}$, which means that $D$ is the midpoint of $\overline{AC}$, and $E$ is the midpoint of $\overline{BC}$, which makes $\overline{DE}$ a midsegment of $\triangle ABC$. $\blacksquare$

In a triangle $\triangle ABC$, if the points $D$ and $E$ lie on different sides of the triangle, $\overline{DE} \parallel \overline{AB}$, and $DE = \frac{AB}{2}$, then $\overline{DE}$ is a midsegment of $\triangle ABC$.

## Perpendicular bisectors in triangles (Mediatrices de un triángulo)

(Punto equidistante a otros puntos)
**Equidistant point to other points**: a given point is equidistant to other points when its distance to all the other points is the same.

(Teorema de la mediatriz)
**Perpendicular bisector theorem**: given a segment and its perpendicular bisector, any point in the perpendicular bisector is equidistant to both endpoints of the segment.
[Perpendicular bisector theorem image code](Programs/S05/Perpendicular_bisector_theorem_image.py)
![Perpendicular bisector theorem image](Images/S05/Perpendicular_bisector_theorem.png)
*Perpendicular bisector theorem*

> Proof of the perpendicular bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overleftrightarrow{CD} \perp \overline{AB}$, $\overline{AD} \cong \overline{BD}$, $\angle CDA$ and $\angle CDB$ are right angles | Given |
> | $\overline{CD} \cong \overline{CD}$ | Reflexive property of congruence |
> | $\triangle ADC \cong \triangle BDC$ | SAS triangle congruence postulate |
> | $\overline{AC} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |

If $\overline{CD}$ is a perpendicular bisector of $\overline{AB}$, and $E$ is any point that lies on $\overline{CD}$, then $\overline{AE} \cong \overline{EB}$.

(Converso del teorema de la mediatriz)
**Converse of the perpendicular bisector theorem**: given a segment, any point equidistant to both endpoints, is in the perpendicular bisector of the segment.

> Proof of the converse of the perpendicular bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AC} \cong \overline{BC}$, $D$ is the midpoint of $\overline{AB}$ | Given, from the *Perpendicular bisector theorem* image |
> | $\triangle ABC$ is isosceles | Definition of isosceles triangle |
> | $\angle A \cong \angle B$ | Base angles theorem |
> | $\overline{AD} \cong \overline{BD}$ | Definition of midpoint |
> | $\triangle ADC \cong \triangle BDC$ | SAS triangle congruence postulate |
> | $\angle CDA \cong \angle CDB$ | Corresponding parts of congruent triangles are congruent |
> | $\angle CDA$ and $\angle CDB$ are supplementary | Linear pair postulate |
> | $\angle CDA$ and $\angle CDB$ are right angles | Congruent linear pairs theorem |
> | $\overleftrightarrow{CD}$ is a perpendicular bisector of $\overline{AB}$ | Definition of perpendicular bisector |

If $\overline{AC} \cong \overline{BC}$, and $D$ is the midpoint of $\overline{AB}$, then $\overline{CD}$ is a perpendicular bisector of $\overline{AB}$.

(Punto de concurrencia)
**Point of concurrency**: the intersection in a single point, of three or more lines, rays, or segments.
[Point of concurrency image code](Programs/S05/Point_of_concurrency_image.py)
![Point of concurrency image](Images/S05/Point_of_concurrency.png)
*Point of concurrency*

The point $A$ is a point of concurrency.

(Circuncentro de un triángulo)
**Circumcenter of a triangle**: in a triangle, the circumcenter is the point of concurrency formed at the intersection of the three perpendicular bisectors, one from each side.
[Circumcenter of a triangle image code](Programs/S05/Circumcenter_of_a_triangle_image.py)
![Circumcenter of a triangle image](Images/S05/Circumcenter_of_a_triangle.png)
*Circumcenter of a triangle*

The circumcenter is in the three perpendicular bisectors of a triangle, and due to the perpendicular bisector theorem, the circumcenter is equidistant to the three vertices of the triangle. This allows building a circle that circumscribes (circunscribe) the triangle, using the circumcenter as center of said circle, and the distance from the circumcenter to any vertex as the radius.

(Teorema de la concurrencia de las mediatrices de un triángulo)
**Concurrency of the perpendicular bisectors of a triangle theorem**: in a triangle, the three perpendicular bisectors, one from each side, intersect each other at a single point which is the circumcenter.

> Proof of the concurrency of the perpendicular bisectors of a triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{GD}$ is a perpendicular bisector of $\overline{AB}$, $\overline{GE}$ is a perpendicular bisector of $\overline{AC}$, $\overline{GF}$ is a perpendicular bisector of $\overline{BC}$ | Given, from the *Circumcenter of a triangle* image |
> | $G$ is equidistant to $A$, $B$, $C$ | Perpendicular bisector theorem |
> | $G$ is the circumcenter of $\triangle ABC$ | Definition of circumcenter |

In a triangle $\triangle ABC$, there is a point $G$, such that $G$ is in the three perpendicular bisectors from the three sides of the triangle, $G$ is equidistant to $A$, $B$, $C$, and $G$ is the circumcenter of $\triangle ABC$.

## Angle bisectors in triangles (Bisectrices de los ángulos de un triángulo)

(Teorema de la equidistancia en la bisectriz de un ángulo)
**Equidistance in an angle bisector theorem**: given an angle, any point in its angle bisector is equidistant to the sides of the angle, using the shortest distance between the point and the sides.
[Equidistance in an angle bisector theorem image code](Programs/S05/Equidistance_in_an_angle_bisector_theorem_image.py)
![Equidistance in an angle bisector theorem image](Images/S05/Equidistance_in_an_angle_bisector_theorem.png)
*Equidistance in an angle bisector theorem*

> Proof of the equidistance in an angle bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{BD}$ is an angle bisector of $\angle ABC$, $\angle DEB$ and $\angle DFB$ are right angles | Given |
> | $\angle EBD \cong \angle FBD$ | Definition of angle bisector |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle EBD \cong \triangle FBD$ | AAS triangle congruence theorem |
> | $\overline{DE} \cong \overline{DF}$ | Corresponding parts of congruent triangles are congruent |

If $\overline{BD}$ is an angle bisector of $\angle ABC$, the distance from $D$ to $\overline{AB}$ creates the segment $\overline{DE}$, and the distance from $D$ to $\overline{BC}$ creates the segment $\overline{DF}$, then $\overline{DE} \cong \overline{DF}$.

(Converso del teorema de la equidistancia en la bisectriz de un ángulo)
**Converse of the equidistance in an angle bisector theorem**: in an angle, if a given point is equidistant to the sides of the angle, using the shortest distance between the point and the sides, then the point lies in the angle bisector.

> Proof of the converse of the equidistance in an angle bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{DE} \cong \overline{DF}$, $\angle DEB$ and $\angle DFB$ are right angles | Given, from the *Equidistance in an angle bisector theorem* image |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle EBD \cong \triangle FBD$ | Hypotenuse-leg congruence theorem |
> | $\angle EBD \cong \angle FBD$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{BD}$ is an angle bisector of $\angle ABC$ | Definition of angle bisector |

In angle $\angle ABC$, given a point $D$, the distance from $D$ to $\overline{AB}$ creates the segment $\overline{DE}$, and the distance from $D$ to $\overline{BC}$ creates the segment $\overline{DF}$, if $\overline{DE} \cong \overline{DF}$, then $\overline{BD}$ is an angle bisector of $\angle ABC$.

(Incentro de un triángulo)
**Incenter of a triangle**: in a triangle, the incenter is the point of concurrency formed at the intersection of the three angle bisectors, one from each vertex.
[Incenter of a triangle image code](Programs/S05/Incenter_of_a_triangle_image.py)
![Incenter of a triangle image](Images/S05/Incenter_of_a_triangle.png)
*Incenter of a triangle*

The incenter is in the three angle bisectors of a triangle, and due to the equidistance in an angle bisector theorem, the incenter is equidistant to the three sides of the triangle. This allows building a circle that inscribes (inscribe) the triangle, using the incenter as center of said circle, and the shortest distance from the incenter to any side as the radius.

(Teorema de la concurrencia de las bisectrices de los ángulos de un triángulo)
**Concurrency of the angle bisectors of a triangle theorem**: in a triangle, the three angle bisectors, one from each vertex, intersect each other at a single point which is the incenter.

> Proof of the concurrency of the angle bisectors of a triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle GAB \cong \angle GAC$, $\angle GBA \cong \angle GBC$, $\angle GCA \cong GCB$ | Given, from the *Incenter of a triangle* image |
> | $\overline{GD} \cong \overline{GE}$ | Equidistance in an angle bisector theorem |
> | $\overline{GE} \cong \overline{GF}$ | Equidistance in an angle bisector theorem |
> | $\overline{GD} \cong \overline{GF}$ | Transitive property of congruence |
> | $G$ lies in the three angle bisectors of $\triangle ABC$ | Converse of the equidistance in an angle bisector theorem |
> | $G$ is the incenter of $\triangle ABC$ | Definition of incenter |

In a triangle $\triangle ABC$, if a point $G$ lies in the three angle bisectors of $\triangle ABC$ then $G$ is the incenter of $\triangle ABC$.

## Medians and altitudes in triangles (Medianas y alturas de un triángulo)

(Mediana de un triángulo)
**Median of a triangle**: in a triangle, a median is a segment that connects one vertex with the midpoint of the side opposite to the vertex.
[Median of a triangle image code](Programs/S05/Median_of_a_triangle_image.py)
![Median of a triangle image](Images/S05/Median_of_a_triangle.png)
*Median of a triangle*

The segment $\overline{CD}$ is a median of the triangle $\triangle ABC$.

(Centroide de un triángulo)
**Centroid of a triangle**: in a triangle, the centroid is the point of concurrency formed at the intersection of the three medians, one from each vertex.
[Centroid of a triangle image code](Programs/S05/Centroid_of_a_triangle_image.py)
[Centroid of a triangle image](Images/S05/Centroid_of_a_triangle.png)
*Centroid of a triangle*

(Teorema de la concurrencia de las medianas de un triángulo)
**Concurrency of the medians of a triangle theorem**: in a triangle, the three medians, one from each vertex to the midpoint of the side opposite to the vertex, intersect each other at a single point which is the centroid. In any given median, the length from the centroid to the vertex is twice the length from the centroid to the midpoint.
[Concurrency of the medians of a triangle theorem image code](Programs/S05/Concurrency_of_the_medians_of_a_triangle_theorem_image.py)
[Concurrency of the medians of a triangle theorem image](Images/S05/Concurrency_of_the_medians_of_a_triangle_theorem.png)
*Concurrency of the medians of a triangle theorem*

> Proof of the concurrency of the medians of a triangle theorem
>
> The segment $\overline{DE}$ is a midsegment of $\triangle ABC$, which means that the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$, because of the midsegment theorem. By the alternate interior angles theorem, $\angle AED \cong \angle BAE$ and $\angle BDE \cong \angle ABD$, which means that $\triangle GED$ is similar to $\triangle GAB$. The scale factor to obtain $\triangle GAB$ from $\triangle GED$ is $2$, because of the said proportion between $\overline{AB}$ and $\overline{DE}$. $\overline{AE}$ intersects $\overline{BD}$ at two thirds of its length from $B$, and by using this same logic $\overline{CF}$ intersects $\overline{BD}$ at two thirds of its length from $B$, which means that the three medians intersect at a single point, the centroid. $AG = 2 EG$, $BG = 2 DG$, and $CG = 2 FG$. $\blacksquare$

In a triangle $\triangle ABC$, if a point $G$ lies in the three medians of $\triangle ABC$ then $G$ is the centroid of $\triangle ABC$. If $D$ is the midpoint of $\overline{AC}$, $E$ is the midpoint of $\overline{BC}$, and $F$ is the midpoint of $\overline{AB}$, then $AG = 2 EG$, $BG = 2 DG$, and $CG = 2 FG$.

(Altura de un triángulo)
**Altitude of a triangle**: in a triangle, an altitude is a segment that connects one vertex perpendicularly to the side opposite to the vertex.
[Altitude of a triangle image code](Programs/S05/Altitude_of_a_triangle_image.py)
![Altitude of a triangle image](Images/S05/Altitude_of_a_triangle.png)
*Altitude of a triangle*

The altitude $\overline{CD}$ of the triangle $\triangle ABC$ is outside of the triangle, and $D$ does not lie on the side $\overline{AB}$. The altitudes of a triangle don't have to be inside the triangle itself.

(Ortocentro de un triángulo)
**Orthocenter of a triangle**: in a triangle, the orthocenter is the point of concurrency formed at the intersection of the three altitudes, one from each vertex.
[Orthocenter of a triangle image code](Programs/S05/Orthocenter_of_a_triangle_image.py)
![Orthocenter of a triangle image](Images/S05/Orthocenter_of_a_triangle.png)
*Orthocenter of a triangle*

The location of the orthocenter depends on the type of triangle. In an obtuse triangle, the orthocenter is outside the triangle. In a right triangle, the orthocenter is the vertex opposite to the hypotenuse. In an acute triangle, the orthocenter is inside the triangle.

## Inequalities in triangles (Desigualdades en los triángulos)

(Teorema del lado mayor de un triángulo)
**Triangle longer side theorem**: in a triangle, given two sides, if one side is longer than the other side, then the angle opposite to the longer side is greater than the angle opposite to the other side.
[Triangle longer side theorem image code](Programs/S05/Triangle_longer_side_theorem_image.py)
![Triangle longer side theorem image](Images/S05/Triangle_longer_side_theorem.png)
*Triangle longer side theorem*

> Proof of the triangle longer side theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $CB > AC$ | Given |
> | $AC = CD$ | Ruler postulate |
> | $\triangle ACD$ is isosceles | Definition of isosceles triangle |
> | $m \angle CAD = m \angle CDA$ | Base angles theorem |
> | $m \angle CDA = m \angle B + m \angle DAB$ | Exterior angle of a triangle theorem |
> | $m \angle CAD = m \angle B + m \angle DAB$ | Substitution property of equality |
> | $m \angle CAB = m \angle CAD + m \angle DAB$ | Angle addition postulate |
> | $m \angle CAB = m \angle B + 2 m \angle DAB$ | Substitution property of equality |
> | $m \angle CAB > m \angle B$ | Definition of the greater than operator |

In a triangle $\triangle ABC$, if $CB > AC$, then $m \angle A > m \angle B$.

(Converso del teorema del lado mayor de un triángulo)
**Converse of the triangle longer side theorem**: in a triangle, given two angles, if the measure of one angle is greater than the measure of the other angle, then the side opposite to the greater angle is longer than the side opposite to the other angle.

> Proof of the converse of the triangle longer side theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $m \angle CAB > m \angle B$ | Given, from the *Triangle longer side theorem* image |
> | $AC = CD$ | Ruler postulate |
> | $\triangle ACD$ is isosceles | Definition of isosceles triangle |
> | $m \angle CDA = m \angle B + m \angle DAB$ | Exterior angle of a triangle theorem |
> | $m \angle DAB + m \angle B + m \angle ADB = \pi$ | Triangle interior angles sum theorem |
> | $m \angle CDA + m \angle ADB = \pi$ | Substitution property of equality |
> | $\angle CDA$ and $\angle ADB$ form a linear pair | Linear pair postulate |
> | The non-shared sides of $\angle CDA$ and $\angle ADB$ form the straight segment $\overline{CDB}$ | Definition of linear pair |
> | $D$ is between $B$ and $C$ | Definition of collinearity |
> | $CB = CD + DB$ | Segment addition postulate |
> | $CB = AC + DB$ | Substitution property of equality |
> | $CB > AC$ | Definition of the greater than operator |

In a triangle $\triangle ABC$, if $m \angle A > m \angle B$, then $CB > AC$.

(Teorema de la desigualdad del triángulo)
**Triangle inequality theorem**: in a triangle, the sum of the lengths of any two sides, is greater than the length of the remaining side.
[Triangle inequality theorem image code](Programs/S05/Triangle_inequality_theorem_image.py)
![Triangle inequality theorem image](Images/S05/Triangle_inequality_theorem.png)
*Triangle inequality theorem*

> Proof of the triangle inequality theorem
>
> Let $\triangle ABC$ have sides with lengths $a$, $b$, $c$. As shown in the image, a triangle can't be formed when $c \ge a + b$ or $c \le |a - b|$. A triangle can be formed when
> $$|a - b| < c < a + b\ \ \blacksquare$$

In a triangle $\triangle ABC$ that has sides with lengths $a$, $b$, $c$, the following relation is true, $|a - b| < c < a + b$, which is equivalent to $c < a + b$, $b < a + c$, and $a < b + c$.

(Teorema de la bisagra)
**Hinge theorem**: given two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the included angle from the first triangle has a measure greater than the one from the second triangle, then the remaining side of the first triangle is longer than the one of the second triangle.

> Proof of the hinge theorem
>
> Let $\triangle ABC$ and $\triangle DEF$ be two triangles, let $AB = DE$ and $BC = EF$, and let $m \angle B > m \angle E$, then $AC > DF$ because of the converse of the triangle longer side theorem. $\blacksquare$

In the triangles $\triangle ABC$ and $\triangle DEF$, if $AB = DE$, $BC = EF$, and $m \angle B > m \angle E$, then $AC > DF$.

(Converso del teorema de la bisagra)
**Converse of the hinge theorem**: given two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the remaining side of the first triangle is longer than the one of the second triangle, then the included angle from the first triangle has a measure greater than the one from the second triangle.

> Proof of the converse of the hinge theorem
>
> Let $\triangle ABC$ and $\triangle DEF$ be two triangles, let $AB = DE$ and $BC = EF$, and let $AC > DF$, then $m \angle B > m \angle E$ because of the triangle longer side theorem. $\blacksquare$

In the triangles $\triangle ABC$ and $\triangle DEF$, if $AB = DE$, $BC = EF$, and $AC > DF$, then $m \angle B > m \angle E$.

#   Right triangle trigonometry (Trigonometría del triángulo rectángulo)

## The pythagorean theorem (El teorema de Pitágoras)

(Longitud del cateto en un triángulo rectángulo)
**Length of the leg in a right triangle**: in a right triangle with hypotenuse of length $c$, and legs of lengths $a$ and $b$, $a = \sqrt{c^2 - b^2}$, $b = \sqrt{c^2 - a^2}$. This can be considered as a corollary of the pythagorean theorem.

(Ternas pitagóricas)
**Pythagorean triples**: groups of three counting numbers that can make the lengths of the sides of a right triangle. For example $3$, $4$, and $5$ are counting numbers that can build a right triangle because $5^2 = 3^2 + 4^2 = 25 = 9 + 16$. Multiples of a pythagorean triple are also pythagorean triples, for example $9$, $12$, and $15$, because $15^2 = 9^2 + 12^2 = 225 = 81 + 144$.

## Converse of the pythagorean theorem (Converso del teorema de Pitágoras)

In a triangle, if the longest side squared is equal to the sum of the other two sides squared, then the triangle is a right triangle, with the right angle being the angle opposite to the longest side.

> Proof of the converse of the pythagorean theorem
>
> Let $\triangle ABC$ have sides with lengths $a$, $b$, and $c$, and let $c^2 = a^2 + b^2$. $\triangle ABC$ is a right triangle with $\angle C$ being the right angle which is the angle opposite to $c$, because any right triangle $\triangle DEF$ with hypotenuse $c$ and legs $a$ and $b$ has $c^2 = a^2 + b^2$. $\blacksquare$

In a triangle $\triangle ABC$ with sides with lengths $a$, $b$, and $c$, if $c^2 = a^2 + b^2$, then $\triangle ABC$ is a right triangle with $\angle C$ being the right angle opposite to the side $c$.

(Teorema de identificación de triángulos agudos)
**Identification of acute triangles theorem**: in a triangle, if the longest side squared is less than the sum of the other two sides squared, then the triangle is an acute triangle.

> Proof of the identification of acute triangles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\triangle ABC$ have sides with lengths $a$, $b$, and $c$, let $c$ be the longest side, and $c^2 < a^2 + b^2$. Let $\triangle DEF$ be a right triangle with sides $a$, $b$, $f$, such that $f^2 = a^2 + b^2$. $c$ is opposite to $\angle C$ and $f$ is opposite to $\angle F$. $\angle F$ is a right angle | Given |
> | $c^2 < f^2$ | Transitive property of equality |
> | $c < f$ | Taking the square root of both sides preserves the inequality |
> | $m \angle C < m \angle F$ | Converse of the hinge theorem |
> | $m \angle C < \pi/2$ | Definition of right angle |
> | $m \angle C > m \angle A$ and $m \angle C > m \angle B$ | Triangle longer side theorem |
> | $\triangle ABC$ is an acute triangle | Definition of acute triangle |

In a triangle $\triangle ABC$ with sides with lengths $a$, $b$, and $c$, and $c$ being the longest side, if $c^2 < a^2 + b^2$, then $\triangle ABC$ is an acute triangle.

(Teorema de identificación de triángulos obtusos)
**Identification of obtuse triangles theorem**: in a triangle, if the longest side squared is greater than the sum of the other two sides squared, then the triangle is an obtuse triangle.

> Proof of the identification of obtuse triangles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\triangle ABC$ have sides with lengths $a$, $b$, and $c$, let $c$ be the longest side, and $c^2 > a^2 + b^2$. Let $\triangle DEF$ be a right triangle with sides $a$, $b$, $f$, such that $f^2 = a^2 + b^2$. $c$ is opposite to $\angle C$ and $f$ is opposite to $\angle F$. $\angle F$ is a right angle | Given |
> | $c^2 > f^2$ | Transitive property of equality |
> | $c > f$ | Taking the square root of both sides preserves the inequality |
> | $m \angle C > m \angle F$ | Converse of the hinge theorem |
> | $m \angle C > \pi/2$ | Definition of right angle |
> | $\triangle ABC$ is an obtuse triangle | Definition of obtuse triangle |

In a triangle $\triangle ABC$ with sides with lengths $a$, $b$, and $c$, and $c$ being the longest side, if $c^2 > a^2 + b^2$, then $\triangle ABC$ is an obtuse triangle.

## Using similar right triangles (Usando triángulos rectángulos similares)

(Triángulos rectángulos inscritos similares)
**Inscribed similar right triangles**: right triangles inscribed inside other right triangles that are similar.
[Inscribed similar right triangles image code](Programs/S08/Inscribed_similar_right_triangles_image.py)
![Inscribed similar right triangles image](Images/S08/Inscribed_similar_right_triangles.png)
*Inscribed similar right triangles*

(Teorema de los triángulos rectángulos inscritos similares)
**Inscribed similar right triangles theorem**: Every right triangle has two inscribed similar triangles. To create them, draw the altitude from the right angle vertex, the resulting two triangles are similar to the original one.

> Proof of the inscribed similar right triangles theorem
>
> From the *Inscribed similar right triangles* image, $\triangle ABC \sim \triangle DAC \sim \triangle DBA$ because of the AA triangle similarity postulate. For $\triangle ABC \sim \triangle DAC$, $\angle BAC \cong \angle ADC$ and $\angle C \cong \angle C$. For $\triangle ABC \sim \triangle DBA$, $\angle BAC \cong \angle BDA$ and $\angle B \cong \angle B$. $\blacksquare$

In the right triangle $\triangle ABC$ with the right angle being $\angle A$, if the point $D$ is the point of the altitude from $\angle A$ that lies on $\overline{BC}$, then $\triangle ABC \sim \triangle DAC \sim \triangle DBA$.

(Media geométrica)
**Geometric mean**: a measure of central tendency of $n$ numbers, that consists in taking the $n$-th root of the product of the $n$ numbers.
[Geometric mean code](Programs/S08/Geometric_mean.py)

> Definition of the geometric mean
>
> Let there be $n$ numbers, where $x_i$ is the $i$-number. Let $GM(x)$ be the geometric mean of the $n$ numbers, then
> $$GM(x) = \sqrt[n]{x_1 x_2 ... x_n}$$

The geometric mean $GM(x)$ is the number whose repeated multiplication is the same as the product $x_1 x_2 ... x_n$, so if the geometric mean replaced each number $x_i$, then the total product would be the same.

(Media geométrica en triángulos rectángulos)
**Geometric mean in right triangles**: there are at least three geometric means in a right triangle, the two legs and the altitude from the right angle are all geometric means of different segments.

To understand this, consider the definition of geometric mean applied to only two numbers. Let $GM$ be the geometric mean of $x_1$ and $x_2$, so $GM = \sqrt{x_1 x_2}$. Representing this equation as a proportion, $GM^2 = x_1 x_2$, then $\frac{GM}{x_2} = \frac{x_1}{GM}$, and reordering $\frac{x_1}{GM} = \frac{GM}{x_2}$. This shows the numbers $x_1$ and $x_2$ as the extremes of the proportion, and $GM$ as the means of the proportion.

Because of the inscribed similar right triangles theorem, in a right triangle $\triangle ABC$ with the right angle being $\angle A$, if the point $D$ is the point of the altitude from $\angle A$ that lies on $\overline{BC}$, then $\triangle ABC \sim \triangle DAC \sim \triangle DBA$. The altitude of $\triangle ABC$ is $\overline{AD}$ (see the *Inscribed similar right triangles* image).

From $\triangle DAC \sim \triangle DBA$, $\frac{BD}{AD} = \frac{AD}{CD}$, which shows that the altitude $\overline{AD}$ is the geometric mean of the segments divided by $D$ in $\overline{BC}$. From $\triangle ABC \sim \triangle DBA$, $\frac{BD}{AB} = \frac{AB}{BC}$, which shows that the leg $\overline{AB}$ is the geometric mean of the hypotenuse and the side of the hypotenuse cut by $D$ that is in the same side as the leg $\overline{AB}$. From $\triangle ABC \sim \triangle DAC$, $\frac{CD}{AC} = \frac{AC}{BC}$, which shows that the leg $\overline{AC}$ is the geometric mean of the hypotenuse and the side of the hypotenuse cut by $D$ that is in the same side as the leg $\overline{AC}$.

## Special right triangles (Triángulos rectángulos especiales)

(Triángulo rectángulo isósceles)
**Isosceles right triangle**: a right triangle with congruent legs. Because of this definition, the three angles are always the same, $\pi/2$ for the right angle, and $\pi/4$ and $\pi/4$ for the base angles, so all isosceles right triangles are similar.
[Isosceles right triangle image code](Programs/S08/Isosceles_right_triangle_image.py)
![Isosceles right triangle image](Images/S08/Isosceles_right_triangle.png)
*Isosceles right triangle*

(Hipotenusa de un triángulo rectángulo isósceles)
**Hypotenuse of an isosceles right triangle**: the length of the legs $l$ is the same for both legs. The length of the hypotenuse is $h = \sqrt{2} l$.

> Hypotenuse of an isosceles right triangle
>
> Let an isosceles right triangle have an hypotenuse with length $h$ and legs with length $l$. By the pythagorean theorem $h^2 = l^2 + l^2 = 2 l^2$, so $h = \sqrt{2 l^2} = \sqrt{2} l$.

(Triángulo 30 60 90)
**30-60-90 triangle**: a right triangle with angles of 30, 60 and 90 degrees (or $\pi/6$, $\pi/3$ and $\pi/2$ in radians). Because of this definition, a 30-60-90 triangle can be seen as an equilateral triangle cut by an altitude in half.
[30-60-90 triangle image code](Programs/S08/30-60-90_triangle_image.py)
![30-60-90 triangle image](Images/S08/30-60-90_triangle.png)
*30-60-90 triangle*

(Lados de un triángulo 30 60 90)
**Sides of a 30-60-90 triangle**: all the lengths of the sides in a 30-60-90 triangle can be known from the hypotenuse.

> Sides of a 30-60-90 triangle
>
> In a 30-60-90 triangle, let $h$ be the length of the hypotenuse, which is the side opposite to the 90 degrees angle. Let $l_1$ be the length of the smaller leg, which is the side opposite to the 30 degrees angle, and let $l_2$ be the length of the longer leg, which is the side opposite to the 60 degrees angle. To find $l_1$, consider that it is half the side of the equilateral triangle that contains the 30-60-90 triangle, so
> $$l_1 = \frac{h}{2}$$
>
> Now, by the pythagorean theorem
>
> $$\begin{gathered}
h^2 = {l_1}^2 + {l_2}^2\\
l_2 = \sqrt{h^2 - {l_1}^2}\\
l_2 = \sqrt{h^2 - {\frac{h}{2}}^2}\\
l_2 = \sqrt{h^2 - \frac{h^2}{4}}\\
l_2 = \sqrt{\frac{3}{4} h^2}\\
l_2 = \frac{\sqrt{3}}{2} h
\end{gathered}$$

In a 30-60-90 triangle, given $h$ as the length of the hypotenuse, $l_1$ as the length opposite to the 30 degrees angle, and $l_2$ as the length opposite to the 60 degress angle, then $l_1 = \frac{h}{2}$, and $l_2 = \frac{\sqrt{3}}{2} h$.

## Tangent, sine and cosine (Tangente, seno y coseno)

(Ratios trigonométricos en un triángulo rectángulo)
**Trigonometric ratios in a right triangle**: ratios specifically created with the lengths of the sides of right triangles. These ratios change by varying the non-right angles in the right triangle. Given that a right triangle only has three sides, there are only three basic ratios possible between pairs of the three sides.
[Trigonometric ratios in a right triangle image code](Programs/S08/Trigonometric_ratios_in_a_right_triangle_image.py)
![Trigonometric ratios in a right triangle image](Images/S08/Trigonometric_ratios_in_a_right_triangle.png)
*Trigonometric ratios in a right triangle*

The trigonometric ratios can be calculated programatically.
[Trigonometric ratios code](Programs/S08/Trigonometric_ratios.py)

(Lado adyacente y lado opuesto a un ángulo en un triángulo rectángulo)
**Adjacent side and opposite side to an angle in a right triangle**: every right triangle has two non-right angles. Each of these two non-right angles has an adjacent side and an opposite side. The opposite side is the regular opposite side of an angle in a triangle. The adjacent side is the side of the angle that is not the hypotenuse.

(Ratios trigonométricos de cualquier ángulo)
**Trigonometric ratios of any angle**: in a right triangle, the non-right angles are always acute, but the trigonometric ratios can still be measured in non-acute angles. For this, the angle is put in the rectangular coordinate system. Because of the definition of an angle, any point in the angle side always falls in one of the four quadrants of the rectangular coordinate system. A right angle is built in that quadrant, using as hypotenuse the segment from the origin to a point in the angle, and using as legs the $x$ and $y$ projections of the point on the rectangular coordinate system, and the trigonometric ratios of the angle are determined using that right triangle (this also works for acute angles).
[Trigonometric ratios of any angle image code](Programs/S08/Trigonometric_ratios_of_any_angle_image.py)
![Trigonometric ratios of any angle image](Images/S08/Trigonometric_ratios_of_any_angle.png)
*Trigonometric ratios of any angle*

(Racionalizar el denominador)
**Rationalize the denominator**: when a fraction has a radical in the denominator, it can be rationalized to remove the radical from the denominator without changing the value of the fraction. The process is $\frac{a}{\sqrt{b}} = \frac{a \sqrt{b}}{\sqrt{b} \sqrt{b}} = \frac{a \sqrt{b}}{b}$.

(Seno de un ángulo)
**Sine of an angle**: placing an angle in a right triangle, its sine is defined as the ratio of the opposite side over the hypotenuse.

> Definition of the sine of an angle
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the sines of the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
sin(\angle B) = \frac{b}{a}\\
sin(\angle C) = \frac{c}{a}
\end{gathered}$$

$sin$ is called the sine function.

(Coseno de un ángulo)
**Cosine of an angle**: placing an angle in a right triangle, its cosine is defined as the ratio of the adjacent side over the hypotenuse.

> Definition of the cosine of an angle
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the cosines of the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
cos(\angle B) = \frac{c}{a}\\
cos(\angle C) = \frac{b}{a}
\end{gathered}$$

$cos$ is called the cosine function.

(Tangente de un ángulo)
**Tangent of an angle**: placing an angle in a right triangle, its tangent is defined as the ratio of the opposite side over the adjacent side.

> Definition of the tangent of an angle
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the tangents of the non-right $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
tan(\angle B) = \frac{b}{c}\\
tan(\angle C) = \frac{c}{b}
\end{gathered}$$

$tan$ is called the tangent function.

(Lados de un triángulo rectángulo dado un ángulo y un lado)
**Sides of a right triangle given an angle and a side**: In a right triangle, having only one of the non-right angles and the length of any one side, is enough to determine the lengths of the other two sides, via the trigonometric ratios.

> Sides of a right triangle given an angle and a side
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the sides of the right triangle can be found in the following manners (see the *Trigonometric ratios in a right triangle* image)
>
> Having $a$ and $m \angle B$
>
> $$\begin{gathered}
b = a\ sin(\angle B)\\
c = a\ cos(\angle B)
\end{gathered}$$
>
> Having $a$ and $m \angle C$
>
> $$\begin{gathered}
b = a\ cos(\angle C)\\
c = a\ sin(\angle C)
\end{gathered}$$
>
> Having $b$ and $m \angle B$
>
> $$\begin{gathered}
a = \frac{b}{sin(\angle B)}\\
c = \frac{b}{tan(\angle B)}
\end{gathered}$$
>
> Having $b$ and $m \angle C$
>
> $$\begin{gathered}
a = \frac{b}{cos(\angle C)}\\
c = b\ tan(\angle C)
\end{gathered}$$
>
> Having $c$ and $m \angle B$
>
> $$\begin{gathered}
a = \frac{c}{cos(\angle B)}\\
b = c\ tan(\angle B)
\end{gathered}$$
>
> Having $c$ and $m \angle C$
>
> $$\begin{gathered}
a = \frac{c}{sin(\angle C)}\\
b = \frac{c}{tan(\angle C)}
\end{gathered}$$

(Ángulo de depresión)
**Angle of depression**: an angle measured below a horizontal line.

(Ángulo de elevación)
**Angle of elevation**: an angle measured above a horizontal line.

## Inverse trigonometric ratios (Ratios trigonométricos inversos)

Given a right triangle in which the lengths of two sides are known, the non-right angles can be calculated using the inverse of the trigonometric ratios. The inverse of the trigonometric ratio is a function that returns the angle needed to originate the ratio of the two sides of the right triangle. So, to calculate the inverse of a trigonometric ratio, the lengths of two sides of a right triangle are needed.
[Inverse of the trigonometric ratios code](Programs/S08/Inverse_of_the_trigonometric_ratios.py)

(Seno inverso | arcoseno)
**Inverse sine | arcsine**: a function that returns the angle that creates a given sine ratio, i.e. the angle that creates a given ratio of opposite side to the angle over the hypotenuse, in a right triangle.

> Definition of the inverse sine of a ratio
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the arcsines that return the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
m \angle B = sin^{-1}\left(\frac{b}{a}\right)\\
m \angle C = sin^{-1}\left(\frac{c}{a}\right)
\end{gathered}$$

$sin^{-1}$ is the inverse sine, or arcsine function.

(Coseno inverso | arcocoseno)
**Inverse cosine | arccosine**: a function that returns the angle that creates a given cosine ratio, i.e. the angle that creates a given ratio of adjacent side to the angle over the hypotenuse, in a right triangle.

> Definition of the inverse cosine of a ratio
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the arccosines that return the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
m \angle B = cos^{-1}\left(\frac{c}{a}\right)\\
m \angle C = cos^{-1}\left(\frac{b}{a}\right)
\end{gathered}$$

$cos^{-1}$ is the inverse cosine, or arccosine function.

(Tangente inversa | arcotangente)
**Inverse tangent | arctangent**: a function that returns the angle that creates a given tangent ratio, i.e. the angle that creates a given ratio of opposite side over adjacent side of the angle, in a right triangle.

> Definition of the inverse tangent of a ratio
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the arctangents that return the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
m \angle B = tan^{-1}\left(\frac{b}{c}\right)\\
m \angle C = tan^{-1}\left(\frac{c}{b}\right)
\end{gathered}$$

$tan^{-1}$ is the inverse tangent, or arctangent function.

## Laws of sines and cosines (Leyes de senos y cosenos)

(Resolver un triángulo)
**Solve a triangle**: determining the measures of the three sides and the three angles of a given triangle.

(Ley de senos)
**Law of sines**: In a triangle, the three ratios of the sine of each angle over the length of the opposite side to the angle, are equal.
[Law of sines image code](Programs/S08/Law_of_sines_image.py)
![Law of sines image](Images/S08/Law_of_sines.png)
*Law of sines*

> Proof of the law of sines
>
> Let there be a triangle $\triangle ABC$, such that $a = BC$, $b = AC$, and $c = AB$. Let $D_1$ be the point in the altitude from $C$ that lies in $\overline{AB}$, and let $D_2$ be the point in the altitude from $B$ that lies in $\overline{AC}$. Let $h_1 = CD_1$, and $h_2 = BD_2$.
>
> Because of the definition of the sine of an angle, $h_1 = b\ sin(\angle A)$ and $h_1 = a\ sin(\angle B)$, so $b\ sin(\angle A) = a\ sin(\angle B)$, therefore $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b}$. On the other hand, $h_2 = c\ sin(\angle A)$ and $h_2 = a\ sin(\angle C)$, so $c\ sin(\angle A) = a\ sin(\angle C)$, therefore $\frac{sin(\angle A)}{a} = \frac{sin(\angle C)}{c}$. By transitivity, $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b} = \frac{sin(\angle C)}{c}$. $\blacksquare$

In a triangle $\triangle ABC$, making $a = BC$, $b = AC$, and $c = AB$, $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b} = \frac{sin(\angle C)}{c}$.

(Ley de senos en triángulos obtusos)
**Law of sines in obtuse triangles**: the law of sines can be used to calculate the measure of obtuse angles. Because of the definitions of the trigonometric ratios, the trigonometric ratios of an obtuse angle are calculated using its supplement instead, which is an acute angle that allows building a right triangle. So when using the law of sines to determine an obtuse angle, the result should be corrected by calculating the supplement of the result, this yields the measure of the obtuse angle.
[Law of sines in obtuse triangles image code](Programs/S08/Law_of_sines_in_obtuse_triangles_image.py)
![Law of sines in obtuse triangles image](Images/S08/Law_of_sines_in_obtuse_triangles.png)
*Law of sines in obtuse triangles*

> Law of sines in obtuse triangles
>
> To prove that the law of sines in obtuse triangles, when used to calculate the measure of the obtuse angle, results in the measure of the acute supplementary angle, let $\triangle ABC$ be an obtuse triangle, with $\angle A$ being the obtuse angle. The objective is to determine $m \angle A$. Notice that $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b}$. Extending $\overline{AB}$ leads to $A_{supp}$, which is the point where $A_{supp}C = b$. From this, it can be visualized that $\frac{sin(\angle A_{supp})}{a} = \frac{sin(\angle B)}{b}$, and by transitivity $\frac{sin(\angle A_{supp})}{a} = \frac{sin(\angle A)}{a}$, so $sin(\angle A_{supp}) = sin(\angle A)$. Also, $\angle A_{supp}$ and $\angle A$ are supplementary because of the base angles theorem. In the end, the law of sines has no way to distinguish between the measure of an obtuse angle and the measure of its acute supplement, so to find the measure of the obtuse angle, the acute angle result must be corrected as $m \angle A = \pi - m \angle A_{supp}$.

In a triangle $\triangle ABC$ where the obtuse angle is $\angle A$, calculating $m \angle A$ with the law of sines results in $m \angle A_{supp}$, this is corrected as $m \angle A = \pi - m \angle A_{supp}$.

(Ley de cosenos)
**Law of cosines**: in a triangle, the squared length of a side, is equal to the sum of the other two sides, each squared, minus twice the product of the other two sides times the cosine of the opposite angle to the original side.
[Law of cosines image code](Programs/S08/Law_of_cosines_image.py)
![Law of cosines image](Images/S08/Law_of_cosines.png)
*Law of cosines*

> Proof of the law of cosines
>
> In a triangle $\triangle ABC$, let $a = BC$, $b = AC$, and $c = AB$, let $D$ be the point in the altitude from $C$ that lies on $\overline{AB}$, let $h = CD$.
>
> The idea is to isolate $a$, in function of $b$, $c$, and $\angle A$. For this, because of the pythagorean theorem, $a^2 = h^2 + BD^2$. $h = b\ sin(\angle A)$, $BD = c - AD$, $AD = b\ cos(\angle A)$, so $BD = c - b\ cos(\angle A)$, and so $a^2 = (b\ sin(\angle A))^2 + (c - b\ cos(\angle A))^2 = b^2\ sin^2(\angle A) + c^2 - 2bc\ cos(\angle A) + b^2\ cos^2(\angle A)$. Because $sin^2 x + cos^2 x = 1$ for any angle $x$, then $a^2 = b^2 (sin^2(\angle A) + cos^2(\angle A)) + c^2 - 2bc\ cos(\angle A) = b^2 + c^2 - 2bc\ cos(\angle A)$. The same proof can be applied to determine the other two sides. $\blacksquare$

In a triangle $\triangle ABC$, making $a = BC$, $b = AC$, and $c = AB$, the law of cosines is $a^2 = b^2 + c^2 - 2bc\ cos(\angle A)$, $b^2 = a^2 + c^2 - 2ac\ cos(\angle B)$, and $c^2 = a^2 + b^2 - 2ab\ cos(\angle C)$.

#   Polygons (Polígonos)

## Angles in polygons (Ángulos en polígonos)

(Teorema de la suma de los ángulos interiores de un polígono)
**Polygon interior angles sum theorem**: the sum of the interior angles of a polygon, is $\pi$ times the number of unique triangles in which the polygon can be divided, which is the same as $\pi$ times the number of vertices minus $2$.
[Polygon interior angles sum theorem image code](Programs/S06/Polygon_interior_angles_sum_theorem_image.py)
![Polygon interior angles sum theorem image](Images/S06/Polygon_interior_angles_sum_theorem.png)
*Polygon interior angles sum theorem*

> Proof of the polygon interior angles sum theorem
>
> In a given polygon, the diagonals can be used to construct unique triangles inside the polygon. In this way, every polygon can be divided into triangles. The number of triangles is finite because each polygon has a finite number of vertices.
>
> Let $n$ be the number of vertices in the polygon. Each triangle must be constructed such that it only contains three vertices and no more. Doing so, each time a triangle is built, it leaves a polygon with minus one vertices, So $n - 3$ diagonals can be drawn, because at the end a polygon of three sides (a triangle) must be left without dividing with diagonals.
>
> $n - 3$ diagonals lead to $n - 2$ triangles. Each triangle has an interior angle sum of $\pi$ because of the triangle interior angles sum theorem, so the total interior angles sum of the polygon is $\pi (n - 2)$. $\blacksquare$

Let $Ang_{int}$ be the sum of the interior angles of a polygon, then $Ang_{int} = \pi(n - 2)$.

(Polígono equiangular)
**Equiangular polygon**: a convex polygon in which all the interior angles are congruent with each other.

(Fórmula del ángulo en un polígono equiangular)
**Angle in an equiangular polygon formula**: a formula to calculate the measure of the interior angles in an equiangular polygon.

> Angle in an equiangular polygon formula
>
> Let an equiangular polygon have $n$ sides, the measure of each interior angle is
> $$\frac{(n - 2)\pi}{n}$$

This formula can be derived from the polygon interior angles sum theorem. If all the interior angles are equal, there are $n$ interior angles, and the sum of the interior angles is $n - 2$, then the formula is correct.
[Angle in an equiangular polygon formula code](Programs/S06/Angle_in_an_equiangular_polygon_formula.py)

(Polígono regular)
**Regular polygon**: a polygon that is both equilateral and equiangular, i.e. a polygon with all sides of equal length, and all interior angles of equal measure.
[Regular polygon image code](Programs/S06/Regular_polygon_image.py)
![Regular polygon image](Images/S06/Regular_polygon.png)
*Regular polygon*

In a regular polygon, each side has a length of $d$, and each interior angle has a measure of $\theta$.

(Teorema de la suma de los ángulos exteriores de un polígono)
**Polygon exterior angle sum theorem**: the sum of the exterior angles of a polygon is exactly $2 \pi$, taking only one exterior angle per vertex.

> Proof of the polygon exterior angle sum theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let there be a polygon of $n$ sides, $n$ vertices. Let $i$ be an index for the $i$-th vertex. Let $a_i$ be the measure of the interior angle at vertex $i$, and let $x_i$ be the measure of the exterior angle at vertex $i$ | Given |
> | $x_i + a_i = \pi\ \ \forall i$ | Definition of interior and exterior angles of a polygon |
> | $\sum_{i = 1}^n{x_i} + \sum_{i = 1}^n{a_i} = \pi n$ | Sum of the pairs of interior and exterior angles from all the $n$ vertices of the polygon |
> | $\sum_{i = 1}^n{a_i} = \pi (n - 2)$ | Polygon interior angles sum theorem |
> | $\sum_{i = 1}^n{x_i} + \pi (n - 2) = \pi n$ | Substitution property of equality |
> | $\sum_{i = 1}^n{x_i} + \pi n - 2 \pi = \pi n$ | Distributive property of multiplication over addition |
> | $\sum_{i = 1}^n{x_i} = 2 \pi$ | Addition and subtraction properties of equality |

Let $Ang_{ext}$ be the sum of the exterior angles of a polygon, then $Ang_{ext} = 2 \pi$.

## Properties of parallelograms (Propiedades de los paralelogramos)

(Paralelogramo)
**Parallelogram**: a quadrilateral that consists of two pairs of parallel sides.
[Parallelogram image code](Programs/S06/Parallelogram_image.py)
![Parallelogram image](Images/S06/Parallelogram.png)
*Parallelogram*

(Construcción de un paralelogramo)
**Parallelogram construction**: a geometric construction to draw a parallelogram.

> Parallelogram construction
>
> This construction requires paper, pencil, and straightedge (or equivalent tools and materials).
> 1. Draw two non-parallel lines that intersect each other.
> 2. Apply the two parallel lines construction, once per line from step 1, so that the resulting lines close the parallelogram.

(Teorema de los lados opuestos de un paralelogramo)
**Opposite sides of a parallelogram theorem**: in a parallelogram, the opposite sides are congruent.
[Opposite sides of a parallelogram theorem image code](Programs/S06/Opposite_sides_of_a_parallelogram_theorem_image.py)
![Opposite sides of a parallelogram theorem image](Images/S06/Opposite_sides_of_a_parallelogram_theorem.png)
*Opposite sides of a parallelogram theorem*

> Proof of the opposite sides of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\overline{AD} \parallel \overline{BC}$, and $\overline{AC}$ is a diagonal of the parallelogram | Given |
> | $\angle DCA \cong \angle BAC$, $\angle DAC \cong \angle BCA$ | Alternate interior angles theorem |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | ASA triangle congruence postulate |
> | $\overline{AB} \cong \overline{CD}$, $\overline{AD} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |

In a parallelogram $ABCD$, $\overline{AB} \cong \overline{CD}$, and $\overline{AD} \cong \overline{BC}$.

(Teorema de los ángulos opuestos de un paralelogramo)
**Opposite angles of a parallelogram theorem**: in a parallelogram, the opposite angles are congruent.

> Proof of the opposite angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\overline{AD} \parallel \overline{BC}$, and $\overline{AC}$ is a diagonal of the parallelogram | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\angle DCA \cong \angle BAC$, $\angle DAC \cong \angle BCA$ | Alternate interior angles theorem |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | ASA triangle congruence postulate |
> | $\angle ABC \cong \angle CDA$ | Corresponding parts of congruent triangles are congruent |
> | $\angle DAB \cong \angle BCD$ | Repeating this proof but with $\overline{BD}$ as diagonal |

In a parallelogram $ABCD$, $\angle A \cong \angle C$, and $\angle B \cong \angle D$.

(Teorema de los ángulos consecutivos de un paralelogramo)
**Consecutive angles of a parallelogram theorem**: in a parallelogram, the consecutive angles are supplementary.
[Consecutive angles of a parallelogram theorem image code](Programs/S06/Consecutive_angles_of_a_parallelogram_theorem_image.py)
![Consecutive angles of a parallelogram theorem image](Images/S06/Consecutive_angles_of_a_parallelogram_theorem.png)
*Consecutive angles of a parallelogram theorem*

> Proof of the consecutive angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\overline{AD} \parallel \overline{BC}$, and $A$, $B$, and $E$ are collinear | Given |
> | $\angle ABC$ and $\angle CBE$ are supplementary | Linear pair postulate |
> | $\angle DAB \cong \angle CBE$ | Corresponding angles postulate |
> | $\angle DAB$ and $\angle ABC$ are supplementary | Converse of the congruent supplements theorem |

The rest of consecutive angle pairs are supplementary by following this same proof, but placing $E$ as a point that extends each of the other three sides of the parallelogram.

In a parallelogram $ABCD$, $\angle A$ and $\angle B$ are supplementary, $\angle B$ and $\angle C$ are supplementary, $\angle C$ and $\angle D$ are supplementary, and $\angle A$ and $\angle D$ are supplementary.

(Teorema de las diagonales de un paralelogramo)
**Diagonals of a parallelogram theorem**: in a parallelogram, the two diagonals bisect each other.
[Diagonals of a parallelogram theorem image code](Programs/S06/Diagonals_of_a_parallelogram_theorem_image.py)
![Diagonals of a parallelogram theorem image](Images/S06/Diagonals_of_a_parallelogram_theorem.png)
*Diagonals of a parallelogram theorem*

> Proof of the diagonals of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\overline{AD} \parallel \overline{BC}$, and $E$ lies at the intersection of $\overline{AC}$ and $\overline{BD}$ | Given |
> | $\overline{AB} \cong \overline{CD}$, and also $\overline{AD} \cong \overline{BC}$ | Opposite sides of a parallelogram theorem |
> | $\angle BAC \cong \angle DCA$, $\angle ABD \cong \angle CDB$, and also $\angle DAC \cong \angle BCA$, $\angle ADB \cong \angle CBD$ | Alternate interior angles theorem |
> | $\triangle ABE \cong \triangle CDE$, and also $\triangle ADE \cong \triangle CBE$ | ASA triangle congruence postulate |
> | $\overline{AE} \cong \overline{CE}$, and also $\overline{DE} \cong \overline{BE}$ | Corresponding parts of congruent triangles are congruent |
> | $E$ is the midpoint of $\overline{AC}$, and also $E$ is the midpoint of $\overline{BD}$ | Definition of midpoint |

In a parallelogram $ABCD$, $\overline{AC}$, and $\overline{BD}$ bisect each other.

## Proving quadrilaterals are parallelograms (Demostraciones de que un cuadrilátero es un paralelogramo)

(Converso del teorema de los lados opuestos de un paralelogramo)
**Converse of the opposite sides of a parallelogram theorem**: in a quadrilateral, if the opposite sides are congruent, then the quadrilateral is a parallelogram.

> Proof of the converse of the opposite sides of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{CD}$ and $\overline{AD} \cong \overline{BC}$ | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | SSS triangle congruence postulate |
> | $\angle ACD \cong \angle CAB$, and $\angle DAC \cong \angle BCA$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{AB} \parallel \overline{CD}$, and $\overline{AD} \parallel \overline{BC}$ | Converse of the alternate interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

In a quadrilateral $ABCD$, if $\overline{AB} \cong \overline{CD}$, and $\overline{AD} \cong \overline{BC}$, then $ABCD$ is a parallelogram.

(Teorema de los lados opuestos paralelos y congruentes de un cuadrilátero)
**Parallel and congruent opposite sides of a quadrilateral theorem**: in a quadrilateral, if a single pair of opposite sides is congruent and parallel, then the quadrilateral is a parallelogram.

> Proof of the parallel and congruent opposite sides of a quadrilateral theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$ and $\overline{AB} \cong \overline{CD}$ | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\angle DCA \cong \angle BAC$ | Alternate interior angles theorem |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | SAS triangle congruence postulate |
> | $\overline{AD} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |
> | The figure $ABCD$ is a parallelogram | Converse of the opposite sides of a parallelogram theorem |

In a quadrilateral $ABCD$, if $\overline{AB} \parallel \overline{CD}$ and $\overline{AB} \cong \overline{CD}$, then $ABCD$ is a parallelogram.

(Converso del teorema de los ángulos opuestos de un paralelogramo)
**Converse of the opposite angles of a parallelogram theorem**: in a quadrilateral, if the opposite angles are congruent, then the quadrilateral is a parallelogram.

> Proof of the converse of the opposite angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle ABC \cong \angle CDA$ and $\angle DAB \cong \angle BCD$ | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $m \angle ABC = m \angle CDA$, and $m \angle DAB = m \angle BCD$ | Definition of congruence |
> | $m \angle ABC + m \angle CDA + m \angle DAB + m \angle BCD = 2 \pi$ | Polygon interior angles sum theorem |
> | $m \angle ABC + m \angle ABC + m \angle DAB + m \angle DAB = 2 \pi$ | Substitution property of equality |
> | $2 m \angle ABC + 2 m \angle DAB = 2 \pi$ | Combine like terms |
> | $m \angle ABC + m \angle DAB = \pi$ | Division property of equality |
> | $m \angle ABC + m \angle BCD = \pi$ | Substitution property of equality |
> | $\angle ABC$ and $\angle DAB$ are supplementary, and also $\angle ABC$ and $\angle BCD$ are supplementary | Definition of supplementary angles |
> | $\overline{AB} \parallel \overline{CD}$, and $\overline{AD} \parallel \overline{BC}$ | Same side interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

In a quadrilateral $ABCD$, if $\angle A \cong \angle C$, and $\angle B \cong \angle D$, then $ABCD$ is a parallelogram.

(Converso del teorema de los ángulos consecutivos de un paralelogramo)
**Converse of the consecutive angles of a parallelogram theorem**: in a quadrilateral, if the consecutive angles are supplementary, then the quadrilateral is a parallelogram.

> Proof of the converse of the consecutive angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle DAB$ and $\angle ABC$ are supplementary, $\angle ABC$ and $\angle BCD$ are supplementary, $\angle BCD$ and $\angle CDA$ are supplementary, $\angle CDA$ and $\angle DAB$ are supplementary | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\overline{AB} \parallel \overline{CD}$, and $\overline{AD} \parallel \overline{BC}$ | Converse of the same side interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

In a quadrilateral $ABCD$, if $\angle A$ and $\angle B$ are supplementary, $\angle B$ and $\angle C$ are supplementary, $\angle C$ and $\angle D$ are supplementary, and $\angle A$ and $\angle D$ are supplementary, then $ABCD$ is a parallelogram.

(Converso del teorema de las diagonales de un paralelogramo)
**Converse of the diagonals of a parallelogram theorem**: in a quadrilateral, if the two diagonals bisect each other, then the quadrilateral is a parallelogram.

> Proof of the converse of the diagonals of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AE} \cong \overline{EC}$ and $\overline{BE} \cong \overline{ED}$, $E$ is the midpoint of $\overline{AC}$ and $\overline{BD}$ | Given, from the *Diagonals of a parallelogram theorem* image |
> | $\angle AEB \cong \angle CED$, and $\angle AED \cong \angle CEB$ | Vertical angles theorem |
> | $\triangle ABE \cong \triangle CDE$, and $\triangle ADE \cong \triangle CBE$ | SAS triangle congruence postulate |
> | $\angle BAE \cong \angle DCE$, and $\angle DAE \cong \angle BCE$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{AB} \parallel \overline{CD}$, and $\overline{AD} \parallel \overline{BC}$ | Converse of the alternate interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

In a quadrilateral $ABCD$, if $\overline{AC}$, and $\overline{BD}$ bisect each other, then $ABCD$ is a parallelogram.

(Determinación algebraica de que un cuadrilátero es un paralelogramo)
**Algebraic determination that a quadrilateral is a parallelogram**: There are algebraic ways to show that a quadrilateral is a parallelogram. Using the definition of parallelogram, calculating the slope of the four sides shows if a figure is a parallelogram or not, i.e. the slopes of the opposite sides must be equal.
[Algebraic determination that a quadrilateral is a parallelogram code](Programs/S06/Algebraic_determination_that_a_quadrilateral_is_a_parallelogram.py)

## Rectangles, rhombuses and squares (Rectángulos, rombos y cuadrados)

(Paralelogramos especiales)
**Special parallelograms**: a set of figures that are parallelograms with a few other characteristics in their definition, specifically the rectangle,the rhombus, and the square.

(Rectángulo)
**Rectangle**: a parallelogram in which all its four angles are right angles.
[Rectangle image code](Programs/S06/Rectangle_image.py)
![Rectangle image](Images/S06/Rectangle.png)
*Rectangle*

(Rombo)
**Rhombus**: a parallelogram in which all its four sides are congruent.
[Rhombus image code](Programs/S06/Rhombus_image.py)
![Rhombus image](Images/S06/Rhombus.png)
*Rhombus*

(Cuadrado)
**Square**: a parallelogram that is also a rectangle and a rhombus, i.e. a parallelogram in which all of its four angles are right angles, and all of its four sides are congruent.
[Square image code](Programs/S06/Square_image.py)
![Square image](Images/S06/Square.png)
*Square*

(Teorema de las diagonales de un rectángulo)
**Diagonals of a rectangle theorem**: in a rectangle, the diagonals are congruent.
[Diagonals of a rectangle theorem image code](Programs/S06/Diagonals_of_a_rectangle_theorem_image.py)
![Diagonals of a rectangle theorem image](Images/S06/Diagonals_of_a_rectangle_theorem.png)
*Diagonals of a rectangle theorem*

> Proof of the diagonals of a rectangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | ${AC}^2 = {AB}^2 + {BC}^2$ | Pythagorean theorem |
> | ${BD}^2 = {AB}^2 + {AD}^2$ | Pythagorean theorem |
> | $AD = BC$ | Opposite sides of a parallelogram theorem |
> | ${BD}^2 = {AB}^2 + {BC}^2$ | Substitution property of equality |
> | ${AC}^2 = {BD}^2$ | Transitive property of equality |
> | $AC = BD$ | Take the square root at both sides of the equation |
> | $\overline{AC} \cong \overline{BD}$ | Definition of congruence |

In a rectangle $ABCD$, $\overline{AC} \cong \overline{BD}$.

(Converso del teorema de las diagonales de un rectángulo)
**Converse of the diagonals of a rectangle theorem**: in a parallelogram, if the diagonals are congruent, then the parallelogram is a rectangle.

> Proof of the converse of the diagonals of a rectangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AC} \cong \overline{BD}$ | Given, from the *Diagonals of a rectangle theorem* image |
> | $\overline{AE} \cong \overline{BE} \cong \overline{CE} \cong \overline{DE}$ | Definition of midpoint |
> | $\triangle AEB$, $\triangle BEC$, $\triangle CED$, and $\triangle AED$, are isosceles triangles | Definition of isosceles triangle |
> | $\angle AEB \cong \angle CED$, and $\angle BEC \cong \angle AED$ | Vertical angles theorem |
> | $\triangle AEB \cong \triangle CED$, and $\triangle BEC \cong \triangle AED$ | SAS triangle congruence postulate |
> | $\angle BAE \cong \angle ABE \cong \angle DCE \cong \angle CDE$, and $\angle DAE \cong \angle ADE \cong \angle CBE \cong \angle BCE$ | Base angles theorem, and corresponding parts of congruent triangles are congruent |
> | $m \angle BAE = m \angle ABE = m \angle DCE = m \angle CDE$, and $m \angle DAE = m \angle ADE = m \angle CBE = m \angle BCE$ | Definition of congruence |
> | $m \angle DAE = m \angle CBE = m \angle BCE = m \angle ADE$ | Commutative property of addition |
> | $m \angle BAE + m \angle DAE = m \angle ABE + m \angle CBE = m \angle BCE + m \angle DCE = m \angle ADE + m \angle CDE$ | Addition property of equality, and substitution property of equality |
> | $m \angle DAB + m \angle ABC + m \angle BCD + m \angle ADC = 2 \pi$ | Polygon interior angles sum theorem |
> | $m \angle DAB = m \angle BAE + m \angle DAE$, $m \angle ABC = m \angle ABE + m \angle CBE$, $m \angle BCD = m \angle BCE + m \angle DCE$, and $m \angle ADC = m \angle ADE + m \angle CDE$ | Angle addition postulate |
> | $m \angle BAE + m \angle DAE + m \angle ABE + m \angle CBE + m \angle BCE + m \angle DCE + m \angle ADE + m \angle CDE = 2 \pi$ | Substitution property of equality |
> | $m \angle BAE + m \angle DAE + m \angle BAE + m \angle DAE + m \angle BAE + m \angle DAE + m \angle BAE + m \angle DAE = 2 \pi$ | Substitution property of equality |
> | $4(m \angle BAE + m \angle DAE) = 2 \pi$ | Combine like terms |
> | $m \angle BAE + m \angle DAE = \frac{\pi}{2}$ | Division property of equality |
> | $m \angle BAE + m \angle DAE = m \angle ABE + m \angle CBE = m \angle BCE + m \angle DCE = m \angle ADE + m \angle CDE = \frac{\pi}{2}$ | Transitive property of equality |
> | $m \angle DAB = m \angle ABC = m \angle BCD = m \angle ADC = \frac{\pi}{2}$ | Substitution property of equality |
> | $\angle DAB$, $\angle ABC$, $\angle BCD$, and $\angle ADC$ are right angles | Definition of right angle |
> | The figure $ABCD$ is a rectangle | Definition of rectangle |

In a parallelogram $ABCD$, if $\overline{AC} \cong \overline{BD}$, then $ABCD$ is a rectangle.

(Teorema de las diagonales perpendiculares de un rombo)
**Perpendicular diagonals of a rhombus theorem**: in a rhombus, the diagonals are perpendicular.
[Perpendicular diagonals of a rhombus theorem image code](Programs/S06/Perpendicular_diagonals_of_a_rhombus_theorem_image.py)
![Perpendicular diagonals of a rhombus theorem image](Images/S06/Perpendicular_diagonals_of_a_rhombus_theorem.png)
*Perpendicular diagonals of a rhombus theorem*

> Proof of the perpendicular diagonals of a rhombus theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{BC} \cong \overline{CD} \cong \overline{AD}$ | Given |
> | $\overline{AE} \cong \overline{CE}$, and $\overline{BE} \cong \overline{DE}$ | Diagonals of a parallelogram theorem |
> | $\overline{AE} \cong \overline{AE}$, $\overline{BE} \cong \overline{BE}$, $\overline{CE} \cong \overline{CE}$, and $\overline{DE} \cong \overline{DE}$ | Reflexive property of congruence |
> | $\triangle AEB \cong \triangle CEB \cong \triangle CED \cong \triangle AED$ | SSS triangle congruence postulate |
> | $\angle AEB \cong \angle CEB \cong \angle CED \cong \angle AED$ | Corresponding parts of congruent triangles are congruent |
> | $m \angle AEB = m \angle CEB = m \angle CED = m \angle AED$ | Definition of congruence |
> | $m \angle AEB + m \angle CEB + m \angle CED + m \angle AED = 2 \pi$ | Definition of full circle |
> | $m \angle AEB + m \angle AEB + m \angle AEB + m \angle AEB = 2 \pi$ | Substitution property of equality |
> | $4(m \angle AEB) = 2 \pi$ | Combine like terms |
> | $m \angle AEB = \frac{\pi}{2}$ | Division property of equality |
> | $m \angle AEB = m \angle CEB = m \angle CED = m \angle AED = \frac{\pi}{2}$ | Transitive property of equality |
> | $\angle AEB$, $\angle CEB$, $\angle CED$, and $\angle AED$ are right angles | Definition of right angle |
> | $\overline{AC} \perp \overline{BD}$ | Definition of perpendicular lines |

In a rhombus $ABCD$, $\overline{AC} \perp \overline{BD}$.

(Converso del teorema de las diagonales perpendiculares de un rombo)
**Converse of the perpendicular diagonals of a rhombus theorem**: in a parallelogram, if the diagonals are perpendicular, then the parallelogram is a rhombus.

> Proof of the converse of the perpendicular diagonals of a rhombus theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AC} \perp \overline{BD}$ | Given, from the *Perpendicular diagonals of a rhombus theorem* image |
> | $\overline{AE} \cong \overline{CE}$, and $\overline{BE} \cong \overline{DE}$ | Diagonals of a parallelogram theorem |
> | $AE = CE$, and $BE = DE$ | Definition of congruence |
> | ${AB}^2 = {AE}^2 + {BE}^2$ | Pythagorean theorem |
> | ${BC}^2 = {CE}^2 + {BE}^2$ | Pythagorean theorem |
> | ${BC}^2 = {AE}^2 + {BE}^2$ | Substitution property of equality |
> | ${CD}^2 = {CE}^2 + {DE}^2$ | Pythagorean theorem |
> | ${CD}^2 = {AE}^2 + {BE}^2$ | Substitution property of equality |
> | ${AD}^2 = {AE}^2 + {DE}^2$ | Pythagorean theorem |
> | ${AD}^2 = {AE}^2 + {BE}^2$ | Substitution property of equality |
> | ${AB}^2 = {BC}^2 = {CD}^2 = {AD}^2$ | Transitive property of equality |
> | $AB = BC = CD = AD$ | Take the square root at all sides of the equations |
> | $\overline{AB} \cong \overline{BC} \cong \overline{CD} \cong \overline{AD}$ | Definition of congruence |
> | The figure $ABCD$ is a rhombus | Definition of rhombus |

In a parallelogram $ABCD$, if $\overline{AC} \perp \overline{BD}$, then $ABCD$ is a rhombus.

(Teorema de los ángulos bisecados de un rombo)
**Bisected angles of a rhombus theorem**: in a rhombus, the diagonals are angle bisectors of the interior angles of the rhombus.

> Proof of the bisected angles of a rhombus theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{BC} \cong \overline{CD} \cong \overline{AD}$ | Given, from the *Perpendicular diagonals of a rhombus theorem* image |
> | $\overline{AE} \cong \overline{CE}$, and $\overline{BE} \cong \overline{DE}$ | Diagonals of a parallelogram theorem |
> | $\overline{AE} \cong \overline{AE}$, $\overline{BE} \cong \overline{BE}$, $\overline{CE} \cong \overline{CE}$, and $\overline{DE} \cong \overline{DE}$ | Reflexive property of congruence |
> | $\triangle AEB \cong \triangle CEB \cong \triangle CED \cong \triangle AED$ | SSS triangle congruence postulate |
> | $\angle DAE \cong \angle BAE \cong \angle BCE \cong \angle DCE$, and $\angle ABE \cong \angle CBE \cong \angle CDE \cong \angle ADE$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{AC}$ is an angle bisector of $\angle DAB$ and $\angle BCD$, and $\overline{BD}$ is an angle bisector of $\angle ABC$ and $\angle ADC$ | Definition of angle bisector |

In a rhombus $ABCD$, $\overline{AC}$ is an angle bisector of $\angle A$ and $\angle C$, and $\overline{BD}$ is an angle bisector of $\angle B$ and $\angle D$.

(Converso del teorema de los ángulos bisecados de un rombo)
**Converse of the bisected angles of a rhombus theorem**: in a parallelogram, if the diagonals bisect the interior angles, then the parallelogram is a rhombus.

> Proof of the converse of the bisected angles of a rhombus theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AC}$ is an angle bisector of $\angle DAB$ and $\angle BCD$, and $\overline{BD}$ is an angle bisector of $\angle ABC$ and $\angle ADC$, $E$ is the intersection of $\overline{AC}$ and $\overline{BD}$ | Given, from the *Perpendicular diagonals of a rhombus theorem* image |
> | $\angle DAB \cong \angle BCD$, and $\angle ABC \cong \angle ADC$ | Opposite angles of a parallelogram theorem |
> | $\angle DAE \cong \angle BAE \cong \angle BCE \cong \angle DCE$, and $\angle ABE \cong \angle CBE \cong \angle CDE \cong \angle ADE$ | Definition of angle bisector |
> | $\overline{AE} \cong \overline{AE}$, $\overline{BE} \cong \overline{BE}$, $\overline{CE} \cong \overline{CE}$, and $\overline{DE} \cong \overline{DE}$ | Reflexive property of congruence |
> | $\triangle AEB \cong \triangle CEB \cong \triangle CED \cong \triangle AED$ | AAS triangle congruence theorem |
> | $\overline{AB} \cong \overline{BC} \cong \overline{CD} \cong \overline{AD}$ | Corresponding parts of congruent triangles are congruent |
> | The figure $ABCD$ is a rhombus | Definition of rhombus |

In a parallelogram $ABCD$, if $\overline{AC}$ is an angle bisector of $\angle A$ and $\angle C$, and $\overline{BD}$ is an angle bisector of $\angle B$ and $\angle D$, then $ABCD$ is a rhombus.

## Trapezoids and kites (Trapezoides y deltoides)

(Trapecio)
**Trapezoid**: a quadrilateral that consists of two opposite parallel sides, and two opposite non parallel sides. It has a long base (base larga) and a short base (base corta), the bases are the parallel sides.
[Trapezoid image code](Programs/S06/Trapezoid_image.py)
![Trapezoid image](Images/S06/Trapezoid.png)
*Trapezoid*

(Trapecio isósceles)
**Isosceles trapezoid**: a trapezoid with its two non-parallel sides congruent.
[Isosceles trapezoid image code](Programs/S06/Isosceles_trapezoid_image.py)
![Isosceles trapezoid image](Images/S06/Isosceles_trapezoid.png)
*Isosceles trapezoid*

The parts of an isosceles trapezoid are named the same as the parts of an isosceles triangle, except there is no vertex angle.

(Teorema de los ángulos de las bases de un trapecio isósceles)
**Bases angles of an isosceles trapezoid theorem**: in an isosceles trapezoid, the long base angles are congruent, and the short base angles are congruent.
[Bases angles of an isosceles trapezoid theorem image code](Programs/S06/Bases_angles_of_an_isosceles_trapezoid_theorem_image.py)
![Bases angles of an isosceles trapezoid theorem image](Images/S06/Bases_angles_of_an_isosceles_trapezoid_theorem.png)
*Bases angles of an isosceles trapezoid theorem*

> Proof of the bases angles of an isosceles trapezoid theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\overline{AD} \cong \overline{BC}$ | Given |
> | $\overline{AE} \cong \overline{BE}$ | By definition of parallel lines, congruent segments separating two parallel lines, have the same inclination |
> | $\triangle ABE$ is isosceles | Definition of isosceles triangle |
> | $\angle CDE \cong \angle DCE$ | Base angles theorem |
> | $\angle ADC$ and $\angle CDE$ are supplementary, and also $\angle BCD$ and $\angle DCE$ are supplementary | Linear pair postulate |
> | $\angle BCD$ and $\angle CDE$ are supplementary | Converse of the congruent supplements theorem |
> | $\angle ADC \cong \angle BCD$ | Congruent supplements theorem |
> | $\angle A \cong \angle B$ | Base angles theorem |

In an isosceles trapezoid $ABCD$, $\angle A \cong \angle B$ and $\angle C \cong \angle D$.

(Converso del teorema de los ángulos de las bases de un trapecio isósceles)
**Converse of the bases angles of an isosceles trapezoid theorem**: in a trapezoid, if the two angles in each of the parallel sides are congruent, then the trapezoid is an isosceles trapezoid.
[Converse of the bases angles of an isosceles trapezoid theorem image code](Programs/S06/Converse_of_the_bases_angles_of_an_isosceles_trapezoid_theorem_image.py)
![Converse of the bases angles of an isosceles trapezoid theorem image](Images/S06/Converse_of_the_bases_angles_of_an_isosceles_trapezoid_theorem.png)
*Converse of the bases angles of an isosceles trapezoid theorem*

> Proof of the converse of the bases angles of an isosceles trapezoid theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\angle A \cong \angle B$, and $\angle ADC \cong \angle BCD$ | Given |
> | $\overline{DE} \cong \overline{CF}$ | Definition of parallel lines |
> | $\angle AED \cong \angle BFC$ | Right angle theorem |
> | $\triangle AED \cong \triangle BFC$ | AAS triangle congruence theorem |
> | $\overline{AD} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |
> | The figure $ABCD$ is an isosceles trapezoid | Definition of isosceles trapezoid |

In a trapezoid $ABCD$, if $\angle A \cong \angle B$ and $\angle C \cong \angle D$, then $ABCD$ is an isosceles trapezoid.

(Teorema de las diagonales de un trapecio isósceles)
**Diagonals of an isosceles trapezoid theorem**: in an isosceles trapezoid, the diagonals are congruent.
[Diagonals of an isosceles trapezoid theorem image code](Programs/S06/Diagonals_of_an_isosceles_trapezoid_theorem_image.py)
![Diagonals of an isosceles trapezoid theorem image](Images/S06/Diagonals_of_an_isosceles_trapezoid_theorem.png)
*Diagonals of an isosceles trapezoid theorem*

> Proof of the diagonals of an isosceles trapezoid theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AD} \cong \overline{BC}$, $\angle A \cong \angle B$ | Given |
> | $\overline{AB} \cong \overline{AB}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle BAC$ | SAS triangle congruence postulate |
> | $\overline{AC} \cong \overline{BD}$ | Corresponding parts of congruent triangles are congruent |

In an isosceles trapezoid $ABCD$, $\overline{AC} \cong \overline{BD}$.

(Converso del teorema de las diagonales de un trapecio isósceles)
**Converse of the diagonals of an isosceles trapezoid theorem**: in a trapezoid, if the diagonals are congruent, then the trapezoid is an isosceles trapezoid.
[Converse of the diagonals of an isosceles trapezoid theorem image code](Programs/S06/Converse_of_the_diagonals_of_an_isosceles_trapezoid_theorem_image.py)
![Converse of the diagonals of an isosceles trapezoid theorem image](Images/S06/Converse_of_the_diagonals_of_an_isosceles_trapezoid_theorem.png)
*Converse of the diagonals of an isosceles trapezoid theorem*

> Proof of the converse of the diagonals of an isosceles trapezoid theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{CD}$, $\overline{BD} \parallel \overline{CE}$, and $\overline{AC} \cong \overline{BD}$ | Given |
> | $\overline{BD} \cong \overline{CE}$ | Opposite sides of a parallelogram theorem |
> | $\overline{AC} \cong \overline{CE}$ | Transitive property of congruence |
> | $\triangle ACE$ is an isosceles triangle | Definition of isosceles triangle |
> | $\angle BAC \cong \angle E$ | Base angles theorem |
> | $\angle E \cong \angle ABD$ | Corresponding angles postulate |
> | $\angle ABD \cong \angle BAC$ | Transitive property of congruence |
> | $\overline{AB} \cong \overline{AB}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle BAC$ | SAS triangle congruence postulate |
> | $\overline{AD} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |
> | The figure $ABCD$ is an isosceles trapezoid | Definition of isosceles trapezoid |

In a trapezoid $ABCD$, if $\overline{AC} \cong \overline{BD}$, then $ABCD$ is an isosceles trapezoid.

(Segmento medio de un trapecio | mediana de un trapecio)
**Midsegment of a trapezoid**: in a trapezoid, the midsegment is a segment that connects the two midpoints of the non-parallel sides. In a trapezoid $ABCD$, in which $E$ is the midpoint of $\overline{AD}$ and $F$ is the midpoint of $\overline{BC}$, $\overline{EF}$ is the midsegment of $ABCD$.
[Midsegment of a trapezoid image code](Programs/S06/Midsegment_of_a_trapezoid_image.py)
![Midsegment of a trapezoid image](Images/S06/Midsegment_of_a_trapezoid.png)
*Midsegment of a trapezoid*

(Teorema del segmento medio de un trapecio)
**Midsegment of a trapezoid theorem**: the length of the midsegment of a trapezoid is the average of the two lengths of the long base and the short base.
[Midsegment of a trapezoid theorem image code](Programs/S06/Midsegment_of_a_trapezoid_theorem_image.py)
![Midsegment of a trapezoid theorem image](Images/S06/Midsegment_of_a_trapezoid_theorem.png)
*Midsegment of a trapezoid theorem*

> Proof of the midsegment of a trapezoid theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{EF} \parallel \overline{CD}$, $E$ is the midpoint of $\overline{AD}$, $F$ is the midpoint of $\overline{BC}$ | Given |
> | $\angle BFG \cong \angle CFD$ | Vertical angles theorem |
> | $\angle CDF \cong \angle BGF$ | Alternate interior angles theorem |
> | $\overline{BF} \cong \overline{CF}$ | Definition of midpoint |
> | $\triangle BFG \cong \triangle CFD$ | AAS triangle congruence theorem |
> | $\overline{DF} \cong \overline{FG}$ | Corresponding parts of congruent triangles are congruent |
> | $F$ is the midpoint of $\overline{DG}$ | Definition of midpoint |
> | $\overline{EF}$ is a midsegment of $\triangle ADG$ | Definition of midsegment |
> | $EF = \frac{AG}{2}$ | Midsegment of a triangle theorem |
> | $AG = AB + BG$ | Segment addition postulate |
> | $\overline{BG} \cong \overline{CD}$ | Corresponding parts of congruent triangles are congruent |
> | $BG = CD$ | Definition of congruence |
> | $AG = AB + CD$ | Substitution property of equality |
> | $EF = \frac{AB + CD}{2}$ | Substitution property of equality |

In a trapezoid $ABCD$, in which $\overline{EF}$ is the midsegment of $ABCD$, then $EF = \frac{AB + CD}{2}$.

(Deltoide | Cometa)
**Kite**: a quadrilateral that consists of two pairs of congruent adjacent sides.
[Kite image code](Programs/S06/Kite_image.py)
![Kite image](Images/S06/Kite.png)
*Kite*

(Deltoide cóncavo | Punta de flecha)
**Dart**: a concave kite.
[Dart image code](Programs/S06/Dart_image.py)
![Dart image](Images/S06/Dart.png)
*Dart*

(Partes de un deltoide)
**Kite parts**: in a kite, the angles between the congruent sides are called vertex angles (ángulos de los vértices), and the two remaining angles are called non-vertex angles (ángulos no de los vértices).
[Kite parts image code](Programs/S06/Kite_parts.py)
![Kite parts image](Images/S06/Kite_parts.png)
*Kite parts*

(Teorema de los ángulos no de los vértices de un deltoide)
**Non-vertex angles of a kite theorem**: the non-vertex angles of a kite are congruent.
[Non-vertex angles of a kite theorem image code](Programs/S06/Non-vertex_angles_of_a_kite_theorem_image.py)
![Non-vertex angles of a kite theorem image](Images/S06/Non-vertex_angles_of_a_kite_theorem.png)
*Non-vertex angles of a kite theorem*

> Proof of the non-vertex angles of a kite theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$ | Given |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle ADC$ | SSS triangle congruence postulate |
> | $\angle B \cong \angle D$ | Corresponding parts of congruent triangles are congruent |

In a kite $ABCD$, in which $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$, then $\angle B \cong \angle D$.

(Teorema de los ángulos de los vértices de un deltoide)
**Vertex angles of a kite theorem**: in a kite, the vertex angles are bisected by the diagonal that connects them.

> Proof of the vertex angles of a kite theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$ | Given, from the *Non-vertex angles of a kite theorem* image |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle ADC$ | SSS triangle congruence postulate |
> | $m \angle DAB = m \angle CAD + m \angle BAC$, and $m \angle BCD = m \angle ACB + m \angle ACD$ | Angle addition postulate |
> | $\angle CAD \cong \angle BAC$, and $\angle ACB \cong \angle ACD$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{AC}$ is an angle bisector of $\angle DAB$ and $\angle BCD$ | Definition of angle bisector |

In a kite $ABCD$, in which $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$, then $\overline{AC}$ is an angle bisector of $\angle A$ and $\angle C$.

(Teorema de las diagonales de un deltoide)
**Diagonals of a kite theorem**: in a kite, the diagonals are perpendicular.
[Diagonals of a kite theorem image code](Programs/S06/Diagonals_of_a_kite_theorem_image.py)
![Diagonals of a kite theorem image](Images/S06/Diagonals_of_a_kite_theorem.png)
*Diagonals of a kite theorem*

> Proof of the diagonals of a kite theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$ | Given |
> | $\triangle BCD$ is an isosceles triangle | Definition of isosceles triangle |
> | $\angle CBD \cong \angle BDC$ | Base angles theorem |
> | $\overline{AC}$ is an angle bisector of $\angle BCD$ | Vertex angles of a kite theorem |
> | $\angle ACB \cong \angle ACD$ | Definition of angle bisector |
> | $\triangle BCE \cong \triangle DCE$ | ASA triangle congruence postulate |
> | $\angle BEC \cong \angle CED$ | Corresponding parts of congruent triangles are congruent |
> | $\angle AEB \cong \angle CED$ | Vertical angles theorem |
> | $\angle AED \cong \angle BEC$ | Vertical angles theorem |
> | $m \angle BEC = m \angle CED$, $m \angle AEB = m \angle CED$, and $m \angle AED = m \angle BEC$ | Definition of congruence |
> | $m \angle AEB = m \angle BEC = m \angle CED = m \angle AED$ | Transitive property of equality |
> | $m \angle AEB + m \angle BEC + m \angle CED + m \angle AED = 2 \pi$ | Definition of full circle |
> | $m \angle AEB + m \angle AEB + m \angle AEB + m \angle AEB = 2 \pi$ | Substitution property of equality |
> | $4 m \angle AEB = 2 \pi$ | Combine like terms |
> | $m \angle AEB = \frac{\pi}{2}$ | Division property of equality |
> | $m \angle AEB = m \angle BEC = m \angle CED = m \angle AED = \frac{\pi}{2}$ | Transitive property of equality |
> | $\angle AEB$, $\angle BEC$, $\angle CED$, and $\angle AED$ are right angles | Definition of right angle |
> | $\overline{AC} \perp \overline{BD}$ | Definition of perpendicular lines |

In a kite $ABCD$, in which $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$, then $\overline{AC} \perp \overline{BD}$.