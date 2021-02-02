
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
**Polygon exterior angle sum theorem**: the sum of the exterior angles of a polygon is exactly $2\pi$, taking only one exterior angle per vertex.

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

## Rectangles, rhombi, and squares (Rectángulos, rombos, y cuadrados)
[Ch06_S04](https://www.ck12.org/reader/reader-index.html#section/2932958/6.4/9549314)

## Trapezoids and kites (Trapezoides y deltoides)
[Ch06_S05](https://www.ck12.org/reader/reader-index.html#section/2932959/6.5/9549314)