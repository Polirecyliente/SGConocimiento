
#   Polygons and quadrilaterals (Polígonos y cuadriláteros)

<!--
#T# Table of contents

#C# Angles in polygons (Ángulos en polígonos)
#C# Properties of parallelograms (Propiedades de los paralelogramos)
#C# Proofs that a quadrilateral is a parallelogram (Demostraciones de que un cuadrilátero es un paralelogramo)
#C# Rectangles, rhombi, and squares (Rectángulos, rombos, y cuadrados)
#C# Trapezoids and kites (Trapezoides y deltoides)

#T# Beginning of content
-->

## Angles in polygons (Ángulos en polígonos)
[Ch06_S01](https://www.ck12.org/reader/reader-index.html#section/2932955/6.1/9549314)

(Teorema de la suma de los ángulos interiores de un polígono)
**Polygon interior angles sum theorem**: the sum of the interior angles of a polygon, is $\pi$ times the number of unique triangles in which the polygon can be divided, which is the same as $\pi$ times the number of vertices minus $2$.
[Polygon interior angles sum theorem image code](Programs/Ch06/S01_01_Polygon_interior_angles_sum_theorem_image.py)
![Polygon interior angles sum theorem image](Images/Ch06/S01_01_Polygon_interior_angles_sum_theorem.png)
*Polygon interior angles sum theorem*

> Proof of the polygon interior angles sum theorem
>
> In a given polygon, the diagonals can be used to construct unique triangles inside the polygon. In this way, every polygon can be divided into triangles. The number of triangles is finite because each polygon has a finite number of vertices.
>
> Let $n$ be the number of vertices in the polygon. Each triangle must be constructed such that it only contains three vertices and no more. Doing so, each time a triangle is built, it leaves a polygon with minus one vertices, So $n - 3$ diagonals can be drawn, because at the end a polygon of three sides (a triangle) must be left without dividing with diagonals.
>
> $n - 3$ diagonals lead to $n - 2$ triangles. Each triangle has an interior angle sum of $\pi$ because of the triangle interior angles sum theorem, so the total interior angles sum of the polygon is $\pi (n - 2)$. $\blacksquare$

(Polígono equiangular)
**Equiangular polygon**: a convex polygon in which all the interior angles are congruent with each other.

(Fórmula del ángulo en un polígono equiangular)
**Angle in an equiangular polygon formula**: a formula to calculate the measure of the interior angles in an equiangular polygon.

> Angle in an equiangular polygon formula
>
> Let an equiangular polygon have $n$ sides, the measure of each interior angle is
> $$\frac{(n - 2)\pi}{n}$$

This formula can be derived from the polygon interior angles sum theorem. If all the interior angles are equal, there are $n$ interior angles, and the sum of the interior angles is $n - 2$, then the formula is correct.
[Angle in an equiangular polygon formula code](Programs/Ch06/S01_02_Angle_in_an_equiangular_polygon_formula.py)

(Polígono regular)
**Regular polygon**: a polygon that is both equilateral and equiangular, i.e. a polygon with all sides of equal length, and all interior angles of equal measure.
[Regular polygon image code](Programs/Ch06/S01_03_Regular_polygon_image.py)
![Regular polygon image](Images/Ch06/S01_03_Regular_polygon.png)
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

## Properties of parallelograms (Propiedades de los paralelogramos)
[Ch06_S02](https://www.ck12.org/reader/reader-index.html#section/2932956/6.2/9549314)

(Paralelogramo)
**Parallelogram**: a quadrilateral that consists of two pairs of parallel sides.
[Parallelogram image code](Programs/Ch06/S02_01_Parallelogram_image.py)
![Parallelogram image](Images/Ch06/S02_01_Parallelogram.png)
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
[Opposite sides of a parallelogram theorem image code](Programs/Ch06/S02_02_Opposite_sides_of_a_parallelogram_theorem_image.py)
![Opposite sides of a parallelogram theorem image](Images/Ch06/S02_02_Opposite_sides_of_a_parallelogram_theorem.png)
*Opposite sides of a parallelogram theorem*

> Proof of the opposite sides of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{DC}$, $\overline{AD} \parallel \overline{BC}$, and $\overline{AC}$ is a diagonal of the parallelogram | Given |
> | $\angle DCA \cong \angle BAC$, $\angle DAC \cong \angle BCA$ | Alternate interior angles theorem |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | ASA triangle congruence postulate |
> | $\overline{AB} \cong \overline{DC}$, $\overline{AD} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |

(Teorema de los ángulos opuestos de un paralelogramo)
**Opposite angles of a parallelogram theorem**: in a parallelogram, the opposite angles are congruent.

> Proof of the opposite angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{DC}$, $\overline{AD} \parallel \overline{BC}$, and $\overline{AC}$ is a diagonal of the parallelogram | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\angle DCA \cong \angle BAC$, $\angle DAC \cong \angle BCA$ | Alternate interior angles theorem |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | ASA triangle congruence postulate |
> | $\angle ABC \cong \angle CDA$ | Corresponding parts of congruent triangles are congruent |
> | $\angle DAB \cong \angle BCD$ | Repeating this proof but with $\overline{BD}$ as diagonal |

(Teorema de los ángulos consecutivos de un paralelogramo)
**Consecutive angles of a parallelogram theorem**: in a parallelogram, the consecutive angles are supplementary.
[Consecutive angles of a parallelogram theorem image code](Programs/Ch06/S02_03_Consecutive_angles_of_a_parallelogram_theorem_image.py)
![Consecutive angles of a parallelogram theorem image](Images/Ch06/S02_03_Consecutive_angles_of_a_parallelogram_theorem.png)
*Consecutive angles of a parallelogram theorem*

> Proof of the consecutive angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{DC}$, $\overline{AD} \parallel \overline{BC}$, and $A$, $B$, and $E$ are collinear | Given |
> | $\angle ABC$ and $\angle CBE$ are supplementary | Linear pair postulate |
> | $\angle DAB \cong \angle CBE$ | Corresponding angles postulate |
> | $\angle DAB$ and $\angle ABC$ are supplementary | Converse of the congruent supplements theorem | ASA triangle congruence postulate |

The rest of consecutive angle pairs are supplementary by following this same proof, but placing $E$ as a point that extends each of the other three sides of the parallelogram.

(Teorema de las diagonales de un paralelogramo)
**Diagonals of a parallelogram theorem**: in a parallelogram, the two diagonals bisect each other.
[Diagonals of a parallelogram theorem image code](Programs/Ch06/S02_04_Diagonals_of_a_parallelogram_theorem_image.py)
![Diagonals of a parallelogram theorem image](Images/Ch06/S02_04_Diagonals_of_a_parallelogram_theorem.png)
*Diagonals of a parallelogram theorem*

> Proof of the diagonals of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{DC}$, $\overline{AD} \parallel \overline{BC}$, and $E$ lies at the intersection of $\overline{AC}$ and $\overline{BD}$ | Given |
> | $\overline{AB} \cong \overline{DC}$, and also $\overline{AD} \cong \overline{BC}$ | Opposite sides of a parallelogram theorem |
> | $\angle BAC \cong \angle DCA$, $\angle ABD \cong \angle CDB$, and also $\angle DAC \cong \angle BCA$, $\angle ADB \cong \angle CBD$ | Alternate interior angles theorem |
> | $\triangle ABE \cong \triangle CDE$, and also $\triangle ADE \cong \triangle CBE$ | ASA triangle congruence postulate |
> | $\overline{AE} \cong \overline{CE}$, and also $\overline{DE} \cong \overline{BE}$ | Corresponding parts of congruent triangles are congruent |
> | $E$ is the midpoint of $\overline{AC}$, and also $E$ is the midpoint of $\overline{BD}$ | Definition of midpoint |

## Proofs that a quadrilateral is a parallelogram (Demostraciones de que un cuadrilátero es un paralelogramo)
[Ch06_S03](https://www.ck12.org/reader/reader-index.html#section/2932957/6.3/9549314)

(Converso del teorema de los lados opuestos de un paralelogramo)
**Converse of the opposite sides of a parallelogram theorem**: in a quadrilateral, if the opposite sides are congruent, then the quadrilateral is a parallelogram.

> Proof of the converse of the opposite sides of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{DC}$ and $\overline{AD} \cong \overline{BC}$ | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | SSS triangle congruence postulate |
> | $\angle ACD \cong \angle CAB$, and $\angle DAC \cong \angle BCA$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{AB} \parallel \overline{DC}$, and $\overline{AD} \parallel \overline{BC}$ | Converse of the alternate interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

(Teorema de los lados opuestos paralelos y congruentes de un cuadrilátero)
**Parallel and congruent opposite sides of a quadrilateral theorem**: in a quadrilateral, if a single pair of opposite sides is congruent and parallel, then the quadrilateral is a parallelogram.

> Proof of the parallel and congruent opposite sides of a quadrilateral theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \parallel \overline{DC}$ and $\overline{AB} \cong \overline{DC}$ | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\angle DCA \cong \angle BAC$ | Alternate interior angles theorem |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle CDA$ | SAS triangle congruence postulate |
> | $\overline{AD} \cong \overline{BC}$ | Corresponding parts of congruent triangles are congruent |
> | The figure $ABCD$ is a parallelogram | Converse of the opposite sides of a parallelogram theorem |

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
> | $\overline{AB} \parallel \overline{DC}$, and $\overline{AD} \parallel \overline{BC}$ | Same side interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

(Converso del teorema de los ángulos consecutivos de un paralelogramo)
**Converse of the consecutive angles of a parallelogram theorem**: in a quadrilateral, if the consecutive angles are supplementary, then the quadrilateral is a parallelogram.

> Proof of the converse of the consecutive angles of a parallelogram theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle DAB$ and $\angle ABC$ are supplementary, $\angle ABC$ and $\angle BCD$ are supplementary, $\angle BCD$ and $\angle CDA$ are supplementary, $\angle CDA$ and $\angle DAB$ are supplementary | Given, from the *Opposite sides of a parallelogram theorem* image |
> | $\overline{AB} \parallel \overline{DC}$, and $\overline{AD} \parallel \overline{BC}$ | Converse of the same side interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

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
> | $\overline{AB} \parallel \overline{DC}$, and $\overline{AD} \parallel \overline{BC}$ | Converse of the alternate interior angles theorem |
> | The figure $ABCD$ is a parallelogram | Definition of a parallelogram |

(Determinación algebraica de que un cuadrilátero es un paralelogramo)
**Algebraic determination that a quadrilateral is a parallelogram**: There are algebraic ways to show that a quadrilateral is a parallelogram. Using the definition of parallelogram, calculating the slope of the four sides shows if a figure is a parallelogram or not, i.e. the slopes of the opposite sides must be equal.
[Algebraic determination that a quadrilateral is a parallelogram code](Programs/Ch06/S03_01_Algebraic_determination_that_a_quadrilateral_is_a_parallelogram.py)

## Rectangles, rhombi, and squares (Rectángulos, rombos, y cuadrados)
[Ch06_S04](https://www.ck12.org/reader/reader-index.html#section/2932958/6.4/9549314)

(Paralelogramos especiales)
**Special parallelograms**: a set of figures that are parallelograms with a few other characteristics in their definition.

(Rectángulo)
**Rectangle**: a parallelogram in which all its four angles are right angles.
[Rectangle image code](Programs/Ch06/S04_01_Rectangle_image.py)
![Rectangle image](Images/Ch06/S04_01_Rectangle.png)
*Rectangle*

(Rombo)
**Rhombus**: a parallelogram in which all its four sides are congruent.
[Rhombus image code](Programs/Ch06/S04_02_Rhombus_image.py)
![Rhombus image](Images/Ch06/S04_02_Rhombus.png)
*Rhombus*

(Cuadrado)
**Square**: a parallelogram that is also a rectangle and a rhombus, i.e. a parallelogram in which all its four angles are right angles, and all its four sides are congruent.
[Square image code](Programs/Ch06/S04_03_Square_image.py)
![Square image](Images/Ch06/S04_03_Square.png)
*Square*

(Teorema de las diagonales de un rectángulo)
**Diagonals of a rectangle theorem**: in a rectangle, the diagonals are congruent.
[Diagonals of a rectangle theorem image code](Programs/Ch06/S04_04_Diagonals_of_a_rectangle_theorem_image.py)
![Diagonals of a rectangle theorem image](Images/Ch06/S04_04_Diagonals_of_a_rectangle_theorem.png)
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

(Teorema de las diagonales perpendiculares de un rombo)
**Perpendicular diagonals of a rhombus theorem**: in a rhombus, the diagonals are perpendicular.
[Perpendicular diagonals of a rhombus theorem image code](Programs/Ch06/S04_05_Perpendicular_diagonals_of_a_rhombus_theorem_image.py)
![Perpendicular diagonals of a rhombus theorem image](Images/Ch06/S04_05_Perpendicular_diagonals_of_a_rhombus_theorem.png)
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

## Trapezoids and kites (Trapezoides y deltoides)
[Ch06_S05](https://www.ck12.org/reader/reader-index.html#section/2932959/6.5/9549314)

(Trapecio)
**Trapezoid**: a quadrilateral that consists of two opposite sides parallel, and the other two sides non-parallel.
[Trapezoid image code](Programs/Ch06/S05_01_Trapezoid_image.py)
![Trapezoid image](Images/Ch06/S05_01_Trapezoid.png)
*Trapezoid*

(Trapecio isósceles)
**Isosceles trapezoid**: a trapezoid with its two non-parallel sides congruent.
[Isosceles trapezoid image code](Programs/Ch06/S05_02_Isosceles_trapezoid_image.py)
![Isosceles trapezoid image](Images/Ch06/S05_02_Isosceles_trapezoid.png)
*Isosceles trapezoid*

The parts of an isosceles trapezoid are named the same as the parts of an isosceles triangle, except there is no vertex angle, and there is a long base (base larga) and a short base (base corta).

(Teorema de los ángulos de las bases de un trapecio isósceles)
**Bases angles of an isosceles trapezoid theorem**: in an isosceles trapezoid, the long base angles are congruent, and the short base angles are congruent.
[Bases angles of an isosceles trapezoid theorem image code](Programs/Ch06/S05_03_Bases_angles_of_an_isosceles_trapezoid_theorem_image.py)
![Bases angles of an isosceles trapezoid theorem image](Images/Ch06/S05_03_Bases_angles_of_an_isosceles_trapezoid_theorem.png)
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

(Converso del teorema de los ángulos de las bases de un trapecio isósceles)
**Converse of the bases angles of an isosceles trapezoid theorem**: in a trapezoid, if the two angles in each of the parallel sides are congruent, then the trapezoid is an isosceles trapezoid.
[Converse of the bases angles of an isosceles trapezoid theorem image code](Programs/Ch06/S05_04_Converse_of_the_bases_angles_of_an_isosceles_trapezoid_theorem_image.py)
![Converse of the bases angles of an isosceles trapezoid theorem image](Images/Ch06/S05_04_Converse_of_the_bases_angles_of_an_isosceles_trapezoid_theorem.png)
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

(Teorema de las diagonales de un trapecio isósceles)
**Diagonals of an isosceles trapezoid theorem**: in an isosceles trapezoid, the diagonals are congruent.
[Diagonals of an isosceles trapezoid theorem image code](Programs/Ch06/S05_05_Diagonals_of_an_isosceles_trapezoid_theorem_image.py)
![Diagonals of an isosceles trapezoid theorem image](Images/Ch06/S05_05_Diagonals_of_an_isosceles_trapezoid_theorem.png)
*Diagonals of an isosceles trapezoid theorem*

> Proof of the diagonals of an isosceles trapezoid theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AD} \cong \overline{BC}$, $\angle A \cong \angle B$ | Given |
> | $\overline{AB} \cong \overline{AB}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle BAC$ | SAS triangle congruence postulate |
> | $\overline{AC} \cong \overline{BD}$ | Corresponding parts of congruent triangles are congruent |

(Converso del teorema de las diagonales de un trapecio isósceles)
**Converse of the diagonals of an isosceles trapezoid theorem**: in a trapezoid, if the diagonals are congruent, then the trapezoid is an isosceles trapezoid.
[Converse of the diagonals of an isosceles trapezoid theorem image code](Programs/Ch06/S05_06_Converse_of_the_diagonals_of_an_isosceles_trapezoid_theorem_image.py)
![Converse of the diagonals of an isosceles trapezoid theorem image](Images/Ch06/S05_06_Converse_of_the_diagonals_of_an_isosceles_trapezoid_theorem.png)
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

(Segmento medio de un trapecio | mediana de un trapecio)
**Midsegment of a trapezoid**: in a trapezoid, the midsegment is a segment that connects the two midpoints of the non-parallel sides.
[Midsegment of a trapezoid image code](Programs/Ch06/S05_07_Midsegment_of_a_trapezoid_image.py)
![Midsegment of a trapezoid image](Images/Ch06/S05_07_Midsegment_of_a_trapezoid.png)
*Midsegment of a trapezoid*

(Teorema del segmento medio de un trapecio)
**Midsegment of a trapezoid theorem**: the length of the midsegment of a trapezoid is the average of the two lengths of the long base and the short base.
[Midsegment of a trapezoid theorem image code](Programs/Ch06/S05_08_Midsegment_of_a_trapezoid_theorem_image.py)
![Midsegment of a trapezoid theorem image](Images/Ch06/S05_08_Midsegment_of_a_trapezoid_theorem.png)
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

(Deltoide | Cometa)
**Kite**: a quadrilateral that consists of two pairs of congruent adjacent sides.
[Kite image code](Programs/Ch06/S05_09_Kite_image.py)
![Kite image](Images/Ch06/S05_09_Kite.png)
*Kite*

(Deltoide cóncavo | Punta de flecha)
**Dart**: a concave kite.
[Dart image code](Programs/Ch06/S05_10_Dart_image.py)
![Dart image](Images/Ch06/S05_10_Dart.png)
*Dart*

(Partes de un deltoide)
**Kite parts**: in a kite, the angles between the congruent sides are called vertex angles (ángulos de los vértices), and the two remaining angles are called non-vertex angles (ángulos no de los vértices).
[Kite parts image code](Programs/Ch06/S05_11_Kite_parts.py)
![Kite parts image](Images/Ch06/S05_11_Kite_parts.png)
*Kite parts*

(Teorema de los ángulos no de los vértices de un deltoide)
**Non-vertex angles of a kite theorem**: the non-vertex angles of a kite are congruent.
[Non-vertex angles of a kite theorem image code](Programs/Ch06/S05_12_Non-vertex_angles_of_a_kite_theorem_image.py)
![Non-vertex angles of a kite theorem image](Images/Ch06/S05_12_Non-vertex_angles_of_a_kite_theorem.png)
*Non-vertex angles of a kite theorem*

> Proof of the non-vertex angles of a kite theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{AD}$, and $\overline{BC} \cong \overline{CD}$ | Given |
> | $\overline{AC} \cong \overline{AC}$ | Reflexive property of congruence |
> | $\triangle ABC \cong \triangle ADC$ | SSS triangle congruence postulate |
> | $\angle B \cong \angle D$ | Corresponding parts of congruent triangles are congruent |

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

(Teorema de las diagonales de un deltoide)
**Diagonals of a kite theorem**: in a kite, the diagonals are perpendicular.
[Diagonals of a kite theorem image code](Programs/Ch06/S05_13_Diagonals_of_a_kite_theorem_image.py)
![Diagonals of a kite theorem image](Images/Ch06/S05_13_Diagonals_of_a_kite_theorem.png)
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