
#   Parallel and perpendicular lines (Líneas paralelas y perpendiculares)

<!--
#T# Table of contents

#C# Parallel lines, skew lines, perpendicular lines, transversals (Líneas paralelas, líneas alabeadas, líneas perpendiculares, transversales)
#C# Properties of parallel lines (Propiedades de las líneas paralelas)
#C# Proving lines parallel (Demostrar el paralelismo entre líneas)
#C# Properties of perpendicular lines (Propiedades de las líneas perpendiculares)
#C# Algebra of parallel and perpendicular lines (Álgebra de las líneas paralelas y perpendiculares)
#C# Distance formula (Fórmula de distancia)

#T# Beginning of content
-->

## Parallel lines, skew lines, perpendicular lines, transversals (Líneas paralelas, líneas alabeadas, líneas perpendiculares, transversales)
[Ch03_S01](https://www.ck12.org/reader/reader-index.html#section/9509902/3.1/9549314)

(Paralelismo en geometría)
**Geometric parallelism**: the relationship that is produced when two distinct figures extend indefinitely and never intersect each other.

Two parallel lines that belong to the same plane, extend indefinitely and never intersect each other. Two parallel planes in space, extend indefinitely and never intersect each other. The distance between parallel lines or planes is constant.

> Parallel relation notation
>
> The symbol $\parallel$ indicates a parallel relation. Let $\overleftrightarrow{AB}$, $\overleftrightarrow{CD}$ be two lines, such that they are parallel to each other, this can be denoted as $\overleftrightarrow{AB} \parallel \overleftrightarrow{CD}$, read as the line $AB$ is parallel to the line $CD$ (la línea $AB$ es paralela a la línea $CD$).

In diagrams, parallel lines are indicated by placing arrowheads inside the lines. Each set of parallel lines has its own amount of arrowheads.
[Parallel lines image code](Programs/Ch03/S01_01_Parallel_lines_image.py)
![Parallel lines image](Images/Ch03/S01_01_Parallel_lines.png)
*Parallel lines*

In the image, $k \parallel l$, which is denoted with one arrowhead inside the lines. Also $m \parallel n$, which is denoted with two arrowheads inside the lines.

(Líneas alabeadas)
**skew lines**: a relationship between two lines, such that they are not parallel but also do not intersect. This is possible in lines that belong to different planes.
[Skew lines image code](Programs/Ch03/S01_02_Skew_lines_image.py)
![Skew lines image](Images/Ch03/S01_02_Skew_lines.png)
*Skew lines*

The blue line and the crimson line are not parallel, and yet they never intersect, because they lie in different planes.

(Postulado de las paralelas)
**Parallel postulate**: given a line and a point not on the line, there is only one parallel to the line that passes through the point.

(Postulado de las perpendiculares)
**Perpendicular postulate**: given a line and a point not on the line, there is only one perpendicular line to the line that passes through the point.

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
[Transversal line image code](Programs/Ch03/S01_03_Transversal_line_image.py)
![Transversal line image](Images/Ch03/S01_03_Transversal_line.png)
*Transversal line*

The lime green line is the transversal, although all the lines intersect the other two, which means that effectively all three lines are transversal. The case in which this does not happen, is when the other two lines are parallel.
[Transversal to parallel lines image code](Programs/Ch03/S01_04_Transversal_to_parallel_lines_image.py)
![Transversal to parallel lines image](Images/Ch03/S01_04_Transversal_to_parallel_lines.png)
*Transversal to parallel lines*

The line $t$ is transversal to the lines $l$ and $m$, and $l \parallel m$. Angles can be denoted with numbers, in the image appear the angles $\angle 1$ through $\angle 8$.

(Partes de una transversal)
**Parts of a transversal**: the following parts will be defined using the *Transversal to parallel lines* image, but these concepts apply to transversals in general.

- **Interior area** (Área interna): the area between the two lines, e.g. the area between $l$ and $m$.

- **Exterior area** (Área externa): the area outside of the two lines, e.g. the area outside of $l$ and $m$.

- **Corresponding angles** (Ángulos correspondientes): two angles that are in the same position relative to the transversal, but each on a different line, e.g. $\angle 1$ and $\angle 5$ are corresponding angles, like $\angle 2$ and $\angle 6$, also $\angle 3$ and $\angle 7$, and lastly $\angle 4$ and $\angle 8$ form corresponding angle pairs.

- **Alternate interior angles** (Ángulos alternos internos): two angles that lie on the interior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 3$ and $\angle 6$ are alternate interior angles, like $\angle 4$ and $\angle 5$.

- **Alternate exterior angles** (Ángulos alternos externos): two angles that lie on the exterior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 1$ and $\angle 8$ are alternate exterior angles, like $\angle 2$ and $\angle 7$.

- **Same side interior angles** (Ángulos conjugados internos): two angles that lie on the interior area, are distinct, and are on the same side of the transversal, e.g. $\angle 3$ and $\angle 5$ are same side interior angles, like $\angle 4$ and $\angle 6$.

- **Same side exterior angles** (Ángulos conjugados externos): two angles that lie on the exterior area, are distinct, and are on the same side of the transversal, e.g. $\angle 1$ and $\angle 7$ are same side exterior angles, like $\angle 2$ and $\angle 8$.

- **Consecutive angles** (Ángulos consecutivos): same side angles are also known as consecutive angles.

## Properties of parallel lines (Propiedades de las líneas paralelas)
[Ch03_S02](https://www.ck12.org/reader/reader-index.html#section/2932933/3.2/9549314)

(Postulado de los ángulos correspondientes)
**Corresponding angles postulate**: in a transversal of two parallels, the corresponding angles are congruent. From the *Transversal to parallel lines* image, $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, and $\angle 4 \cong \angle 8$. Its converse is also a postulate.

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

## Proving lines parallel (Demostrar el paralelismo entre líneas)
[Ch03_S03](https://www.ck12.org/reader/reader-index.html#section/2932934/3.3/9549314)

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

(Propiedad transitiva de las líneas paralelas)
**Transitive property of parallel lines**: given two parallel lines, if the first one is parallel to a third line, then the second line is also parallel to the third.

> Transitive property of parallel lines
>
> Let $k$, $l$, $m$, be lines, if $k \parallel l$ and $l \parallel m$, then $k \parallel m$.

## Properties of perpendicular lines (Propiedades de las líneas perpendiculares)
[Ch03_S04](https://www.ck12.org/reader/reader-index.html#section/2932935/3.4/9549314)

(Teorema de los pares lineales congruentes)
**Congruent linear pairs theorem**: in a linear pair, if the two angles are congruent, then they have a measure of $\pi/2$, meaning that if both angles of a linear pair are congruent then they are right angles.

> Proof of the congruent linear pairs theorem
>
> Let $\angle A$ and $\angle B$ form a linear pair, and let $\angle A \cong \angle B$, then $m \angle A = m \angle B$, $m \angle A + m \angle B = \pi \rArr 2 m \angle A = \pi \rArr m \angle A = \pi/2 = m \angle B$. $\blacksquare$

(Teorema de las transversales perpendiculares)
**Perpendicular transversals theorem**: given three lines, if the first and second lines are parallel, and the first line is perpendicular to the third line, then the second line is also perpendicular to the third line.
[Perpendicular transversal image code](Programs/Ch03/S04_01_Perpendicular_transversal_image.py)
![Perpendicular transversal image](Images/Ch03/S04_01_Perpendicular_transversal.png)
*Perpendicular transversal*

> Proof of the perpendicular transversals theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$ and $l \perp t$ | Given |
> | $\angle 1$, $\angle 2$, $\angle 3$, $\angle 4$, are right angles | Definition of perpendicular lines |
> | $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, $\angle 4 \cong \angle 8$, so $\angle 4$, $\angle 5$, $\angle 6$, $\angle 7$, are right angles | Corresponding angles postulate |
> | $m \perp t$ | Definition of perpendicular lines |

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

(Teorema de los ángulos complementarios adyacentes)
**Adjacent complementary angles theorem**: if two angles are adjacent and complementary, then the two non-shared sides form a right angle.

> Proof of the adjacent complementary angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$ and $\angle B$ be two adjacent complementary angles | Given |
> | $m \angle A + m \angle B = \pi/2$ | Definition of complementary angles |
> | The angle between the non-shared sides is a right angle | Definition of a right angle |

(Converso del teorema de los ángulos complementarios adyacentes)
**Converse of the adjacent complementary angles theorem**: if the non-shared sides of two adjacent angles form a right angle, then the angles are complementary.

> Proof of the converse of the adjacent complementary angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$ and $\angle B$ be adjacent angles, with the non-shared sides forming a right angle | Given |
> | $m \angle A + m \angle B = \pi/2$ | Definition of right angle |
> | $\angle A$ and $\angle B$ are complementary | Definition of complementary angles |

## Algebra of parallel and perpendicular lines (Álgebra de las líneas paralelas y perpendiculares)
[Ch03_S05](https://www.ck12.org/reader/reader-index.html#section/2932936/3.5/9549314)

(Pendiente de una línea)
**Slope of a line**: the amount of inclination of a line. An horizontal line has zero slope, a vertical line has undefined (positive or negative infinity) slope.

From basic algebra, the slope of a line can be defined as an equation in terms of the $x$-$y$ plane coordinates of two points on the line.

> Algebraic definition of the slope of a line
>
> Let $(x_1, y_1)$, $(x_2, y_2)$, be two points on the $x$-$y$ plane, and let $m$ be the slope of the line that passes through these two points, then
> $$m = \frac{y_2 - y_1}{x_2 - x_1}$$

According to this definition of the slope of a line, a positive slope means a line that goes upwards from left to right, and a negative slope means a line that goes downwards from left to right.
[Values of the slope of a line image code](Programs/Ch03/S05_01_Values_of_the_slope_of_a_line_image.py)
![Values of the slope of a line image](Images/Ch03/S05_01_Values_of_the_slope_of_a_line.png)
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
[Slope of perpendicular lines image code](Programs/Ch03/S05_02_Slope_of_perpendicular_lines_image.py)
![Slope of perpendicular lines image](Images/Ch03/S05_02_Slope_of_perpendicular_lines.png)

The blue line is the first line, the lime green line has a slope that is the opposite of the slope of the blue line. The crimson line is perpendicular to the blue line, and has a slope that is the reciprocal of the slope of the lime green line.

## Distance formula (Fórmula de distancia)
[Ch03_S06](https://www.ck12.org/reader/reader-index.html#section/2932937/3.6/9549314)

The distance formula is derived from the Pythagorean theorem (Teorema de Pitágoras).

(Teorema de Pitágoras)
**Pythagorean theorem**: in a right triangle the length of the largest side squared is equal to the sum of the other two lengths individually squared. The largest side is named the hypotenuse (hipotenusa), and the other sides are called legs (catetos).

> Pythagorean theorem
>
> Let $a$, $b$, $c$, be the sides of a right triangle, with $a$ and $b$ being the legs, and $c$ being the hypotenuse, then
> $$c^2 = a^2 + b^2$$

This theorem can be proved with the following image.
![Pythagorean theorem image](../Algebra_basics__Prealgebra__OpenStax/Images/Ch09/S03_02_Pythagorean_theorem.png)
*Pythagorean theorem*

From the image, $(a + b)^2 = c^2 + 2 \cdot a \cdot b$, then $a^2 + 2 \cdot a \cdot b + b^2 = c^2 + 2 \cdot a \cdot b$, and then $a^2 + b^2 = c^2$.

The distance formula takes the distance between two points as the hypotenuse of a right triangle, and the legs as the rise and run in the $x$-$y$ plane.
[Rise and run between two points image code](Programs/Ch03/S06_01_Rise_and_run_between_two_points_image.py)
![Rise and run between two points image](Images/Ch03/S06_01_Rise_and_run_between_two_points.png)

Using the Pythagorean theorem, the distance squared between two points, is the sum of the squared rise plus the squared run.
[Distance formula code](Programs/Ch03/S06_02_Distance_formula.py)

> Distance formula
>
> Let $(x_1, y_1)$, $(x_2, y_2)$, be two points in the $x$-$y$ plane, and let $d$ be the distance between them, then
> $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

(Distancia más corta entre un punto y una recta)
**Shortest distance between a point and a line**: given a point and a line, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line to the given line that passes through the given point, is used to measure this shortest distance, as the distance between the given point and the intersection of the perpendicular line and the given line.
[Shortest distance between a point and a line image code](Programs/Ch03/S06_03_Shortest_distance_between_a_point_and_a_line_image.py)
![Shortest distance between a point and a line image](Images/Ch03/S06_03_Shortest_distance_between_a_point_and_a_line.png)
*Shortest distance between a point and a line*

The shortest distance between the point $A$ and the line $l$ is the distance $AB$.

> Process to find the shortest distance between a point and a line
>
> 1. Use the *Shortest distance between a point and a line* image, let $A$ be the point and $l$ be the line, such that the line $l$ is defined by the equation $y = m_1x + b_1$, and let $B$ be the point of intersection of the line $l$ and a perpendicular line to it that passes through $A$. The shortest distance being measured is the distance $AB$.
> 2. Calculate the slope of the perpendicular line as $m_2 = -\frac{1}{m_1}$.
> 3. Calculate the $y$-intercept of the perpendicular line as $b_2 = y_A - m_2x_A$, where $x_A$ and $y_A$ are the $x$ and $y$ coordinates of the point $A$ respectively.
> 4. Find the coordinates of the point of intersection $B$, namely $x_B$, $y_B$, by equating the equation of the line $l$ and the equation of the perpendicular line, $m_1x_B + b_1 = m_2x_B + b_2$. From this equation, isolate $x_B$ as $x_B = \frac{b_2 - b_1}{m_1 - m_2}$.
> 5. Find $y_B$ as $y_B = m_1x_B + b_1$.
> 6. Calculate the distance between $A$ and $B$ with the distance formula, $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.

(Distancia más corta entre dos líneas paralelas)
**Shortest distance between two parallel lines**: given two parallel lines, the shortest distance possible between them, is the perpendicular distance between them, i.e. a perpendicular line that passes through both parallel lines, is used to measure this shortest distance, as the distance between the two intersections of the perpendicular line with the two parallel lines.

> Process to find the shortest distance between two parallel lines
>
> 1. Pick a point in one of the two parallel lines, name it $A$.
> 2. Apply the Process to find the shortest distance between a point and a line, using $A$ as a point$, and the line is the other parallel line that does not contain $A$. The result is the shortest distance between the two parallel lines.

By definition of parallel lines, the shortest distance between them is a constant.