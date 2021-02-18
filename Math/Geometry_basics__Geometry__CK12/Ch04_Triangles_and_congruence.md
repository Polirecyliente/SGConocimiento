
#   Triangles and congruence (Triángulos y congruencia)

<!--
#T# Table of contents

#C# Triangle angles sum (Suma de los ángulos de un triángulo)
#C# Congruent figures (Figuras congruentes)
#C# Triangle congruence criteria 1 (Criterios de congruencia de triángulos 1)
#C# Triangle congruence criteria 2 (Criterios de congruencia de triángulos 2)
#C# Isosceles and equilateral triangles (Triángulos isósceles y equiláteros)

#T# Beginning of content
-->

## Triangle angles sum (Suma de los ángulos de un triángulo)
[Ch04_S01](https://www.ck12.org/reader/reader-index.html#section/2932940/4.1/9549314)

(Ángulos interiores de un polígono)
**Interior angles of a polygon**: each of the angles at any of the vertices of the polygon, that is inside the polygon.
[Interior angles of a polygon image code](Programs/Ch04/S01_01_Interior_angles_of_a_polygon_image.py)
![Interior angles of a polygon image](Images/Ch04/S01_01_Interior_angles_of_a_polygon.png)
*Interior angles of a polygon*

The angle $\angle A$ is an interior angle of the polygon. Each vertex has an interior angle.

(Teorema de la suma de los ángulos interiores de un triángulo)
**Triangle interior angles sum theorem**: the sum of the interior angles of a triangle, is exactly $\pi$.
[Triangle interior angles sum image code](Programs/Ch04/S01_02_Triangle_interior_angles_sum_image.py)
![Triangle interior angles sum image](Images/Ch04/S01_02_Triangle_interior_angles_sum.png)
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

(Ángulos exteriores de un polígono)
**Exterior angles of a polygon**: each of the angles at any of the vertices of the polygon, that is outside the polygon, formed by a side of the vertex and the extension of the other side.
[Exterior angles of a polygon image code](Programs/Ch04/S01_03_Exterior_angles_of_a_polygon_image.py)
![Exterior angles of a polygon image](Images/Ch04/S01_03_Exterior_angles_of_a_polygon.png)
*Exterior angles of a polygon*

The angle $\angle B$ is an exterior angle of the polygon. Given that each vertex in a polygon has two sides, two exterior angles can be drawn from each vertex, both being congruent to each other due to the vertical angles theorem.

In a given vertex of a polygon, the interior angle and one exterior angle (any of the two) form a linear pair, which means they are supplementary.

(Teorema de la suma de los ángulos exteriores de un triángulo)
**Triangle exterior angle sum theorem**: the sum of the exterior angles of a triangle is exactly $2\pi$, taking only one exterior angle per vertex.
[Triangle exterior angle sum theorem image code](Programs/Ch04/S01_04_Triangle_exterior_angle_sum_theorem_image.py)\
![Triangle exterior angle sum theorem image](Images/Ch04/S01_04_Triangle_exterior_angle_sum_theorem.png)
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

(Ángulos interiores remotos)
**Remote interior angles**: the interior angles that are not adjacent to a given exterior angle. In a triangle, given an exterior angle, the remote interior angles are the two interior angles that are not adjacent to said exterior angle.
[Remote interior angles image code](Programs/Ch04/S01_05_Remote_interior_angles_image.py)
![Remote interior angles image](Images/Ch04/S01_05_Remote_interior_angles.png)
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

## Congruent figures (Figuras congruentes)
[Ch04_S02](https://www.ck12.org/reader/reader-index.html#section/2932941/4.2/9549314)

(Triángulos congruentes)
**Congruent triangles**: given two triangles, they are congruent if their corresponding sides are congruent and their corresponding angles are congruent.
[Congruent triangles images code](Programs/Ch04/S02_01_Congruent_triangles_image.py)
![Congruent triangles image](Images/Ch04/S02_01_Congruent_triangles.png)
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

## Triangle congruence criteria 1 (Criterios de congruencia de triángulos 1)
[Ch04_S03](https://www.ck12.org/reader/reader-index.html#section/6707215/4.3/9549314)

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

## Triangle congruence criteria 2 (Criterios de congruencia de triángulos 2)
[Ch04_S04](https://www.ck12.org/reader/reader-index.html#section/2932943/4.4/9549314)

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
[AAS triangle congruence theorem image code](Programs/Ch04/S04_01_AAS_triangle_congruence_theorem_image.py)
![AAS triangle congruence theorem image](Images/Ch04/S04_01_AAS_triangle_congruence_theorem.png)
*AAS triangle congruence theorem*

> Proof of the AAS triangle congruence theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\angle A \cong \angle D$, $\angle B \cong \angle E$, and $\overline{BC} \cong \overline{EF}$ | Given |
> | $\angle C \cong \angle F$ | Third angle theorem |
> | $\overline{BC}$ is the included side of $\angle B$ and $\angle C$, and $\overline{EF}$ is the included side of $\angle E$ and $\angle F$ | Definition of included side between two angles |
> | $\triangle ABC \cong \triangle DEF$ | ASA triangle congruence postulate |

(Teorema de la congruencia de la hipotenusa-cateto)
**Hypotenuse-leg congruence theorem**: given two right triangles, if the hypotenuse and one leg in one triangle, are congruent to the hypotenuse and one leg in the other triangle, then the two triangles are congruent.

> Proof of the hypotenuse-leg congruence theorem
>
> All right triangles have at least one congruent angle with each other, the right angle. If the hypotenuse of one of the legs is congruent in two triangles, then the two triangles are congruent because of the AAS triangle congruence theorem. $\blacksquare$

The configurations AAA and SSA do not necessarily lead to congruent triangles.

## Isosceles and equilateral triangles (Triángulos isósceles y equiláteros)
[Ch04_S05](https://www.ck12.org/reader/reader-index.html#section/6042181/4.5/9549314)

(Partes de un triángulo isósceles)
**Isosceles triangle parts**: in an isosceles triangle, the congruent sides are called the legs (patas), the remaining side is called the base (base). The two angles formed by the base and each of the legs, are called base angles (ángulos de la base), and the included angle of the two legs is called the vertex angle (ángulo del vértice).
[Isosceles triangle parts image code](Programs/Ch04/S05_01_Isosceles_triangle_parts_image.py)
![Isosceles triangle parts image](Images/Ch04/S05_01_Isosceles_triangle_parts.png)
*Isosceles triangle parts*

(Teorema de los ángulos de la base)
**Base angles theorem**: in an isosceles triangle, the base angles are congruent.
[Base angles theorem image code](Programs/Ch04/S05_02_Base_angles_theorem_image.py)
![Base angles theorem image](Images/Ch04/S05_02_Base_angles_theorem.png)
*Base angles theorem*

> Proof of the base angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AB} \cong \overline{CB}$, $\angle ABD \cong \angle CBD$ | Given |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle CBD$ | SAS triangle congruence postulate |
> | $\angle A \cong \angle C$ | Corresponding parts of congruent triangles are congruent |

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
> | $\overline{AB} \cong \overline{CB}$ | Corresponding parts of congruent triangles are congruent |
> | $\triangle ABC$ is isosceles | Definition of isosceles triangle |

(Teorema del triángulo isósceles)
**Isosceles triangle theorem**: in an isosceles triangle, the angle bisector of the vertex angle is a perpendicular bisector of the base.

> Proof of the isosceles triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\triangle ABC$ is isosceles, $\overline{AB} \cong \overline{CB}$, and $\overline{BD}$ is the angle bisector | Given, from the *Base angles theorem* image |
> | $\angle A \cong \angle C$ | Base angles theorem |
> | $\angle ABD \cong \angle CBD$ | Definition of angle bisector |
> | $\triangle ABD \cong \triangle CBD$ | AAS triangle congruence theorem |
> | $\angle ADB$ and $\angle CDB$ are supplementary | Linear pair postulate |
> | $\angle ADB \cong \angle CDB$ | Corresponding parts of congruent triangles are congruent |
> | $\angle ADB$ and $\angle CDB$ are right angles | Congruent linear pairs theorem |
> | $\overline{BD} \perp \overline{AC}$ | Definition of perpendicular lines |
> | $\overline{AD} \cong \overline{DC}$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$ | Definition of perpendicular bisector |

(Converso del teorema del triángulo isósceles)
**Converse of the isosceles triangle theorem**: in an isosceles triangle, the perpendicular bisector of the base is an angle bisector of the vertex angle.

> Proof of the converse of the isosceles triangle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{BD}$ is a perpendicular bisector of $\overline{AC}$ | Given, from the *Base angles theorem* image |
> | $\overline{AD} \cong \overline{DC}$, $\angle ADB \cong \angle CDB$ | Definition of perpendicular bisector |
> | $\overline{BD} \cong \overline{BD}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle CBD$ | SAS triangle congruence postulate |
> | $\angle ABD \cong \angle CBD$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{BD}$ is an angle bisector of $\angle ABC$ | Definition of angle bisector |

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