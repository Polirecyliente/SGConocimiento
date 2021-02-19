
#   Properties of triangles (Propiedades de los triángulos)

<!--
#T# Table of contents

#C# Midsegments of a triangle (Segmentos medios de un triángulo)
#C# Perpendicular bisectors of a triangle (Mediatrices de un triángulo)
#C# Angle bisectors of a triangle (Bisectrices de los ángulos de un triángulo)
#C# Medians and altitudes of a triangle (Medianas y alturas de un triángulo)
#C# Inequalities in triangles (Desigualdades en los triángulos)

#T# Beginning of content
-->

## Midsegments of a triangle (Segmentos medios de un triángulo)
[Ch05_S01](https://www.ck12.org/reader/reader-index.html#section/2932947/5.1/9549314)

(Segmento medio de un triángulo)
**Midsegment of a triangle**: in a triangle, the midsegment is a segment that connects the two midpoints of adjacent sides.
[Midsegment of a triangle image code](Programs/Ch05/S01_01_Midsegment_of_a_triangle_image.py)
![Midsegment of a triangle image](Images/Ch05/S01_01_Midsegment_of_a_triangle.png)
*Midsegment of a triangle*

The segment $\overline{DE}$ is a midsegment of the triangle $\triangle ABC$.

Every triangle has three midsegments.
[Three midsegments of a triangle image code](Programs/Ch05/S01_02_Three_midsegments_of_a_triangle_image.py)
![Three midsegments of a triangle image](Images/Ch05/S01_02_Three_midsegments_of_a_triangle.png)
*Three midsegments of a triangle*

(Teorema del segmento medio de un triángulo)
**Midsegment of a triangle theorem**: a midsegment of a triangle measures half the length of its parallel side.

> Proof of the midsegment of a triangle theorem
>
> The proof of this theorem requires the concept of similarity, which is explained in detail in another file (see Ch07_Similarity.md). Two figures are similar when they have the same shape but not necessarily the same size. By SAS, the triangle $\triangle ABC$ is similar to $\triangle DEC$. Given that $D$ is the midpoint of $\overline{AC}$, then $\overline{DC}$ has half the length of $\overline{AC}$, and so by similarity, the scale factor needed to obtain $\triangle DEC$ from $\triangle ABC$ is one half, therefore the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$. $\blacksquare$

(Converso del teorema del segmento medio de un triángulo)
**Converse of the midsegment of a triangle theorem**: in a triangle, if a segment connects two sides, is parallel to the non-connected side, and measures half the length of its parallel side, then the segment is a midsegment of the triangle.

> Proof of the converse of the midsegment of a triangle theorem
>
> Similarly to the proof of the midsegment of a triangle theorem, by similarity, the triangle $\triangle ABC$ is similar to $\triangle DEC$, because by the corresponding angles postulate, $\angle ABC \cong \angle CED$ and $\angle BAC \cong \angle CDE$. The scale factor needed to obtain $\triangle ABC$ from $\triangle DEC$ is two, because $\overline{AB}$ has double the length of $\overline{DE}$. Using this scale factor, $\overline{AC}$ has double the length of $\overline{CD}$, and $\overline{BC}$ has double the length of $\overline{CE}$, which means that $D$ is the midpoint of $\overline{AC}$, and $E$ is the midpoint of $\overline{BC}$, which makes $\overline{DE}$ a midsegment of $\triangle ABC$. $\blacksquare$

## Perpendicular bisectors of a triangle (Mediatrices de un triángulo)
[Ch05_S02](https://www.ck12.org/reader/reader-index.html#section/2932948/5.2/9549314)

(Punto equidistante a otros puntos)
**Equidistant point to other points**: a given point is equidistant to other points when its distance to all the other points is the same.

(Teorema de la mediatriz)
**Perpendicular bisector theorem**: given a segment and its perpendicular bisector, any point in the perpendicular bisector is equidistant to both endpoints of the segment.
[Perpendicular bisector theorem image code](Programs/Ch05/S02_01_Perpendicular_bisector_theorem_image.py)
![Perpendicular bisector theorem image](Images/Ch05/S02_01_Perpendicular_bisector_theorem.png)
*Perpendicular bisector theorem*

> Proof of the perpendicular bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overleftrightarrow{CD} \perp \overline{AB}$, $\overline{AD} \cong \overline{DB}$, $\angle CDA$ and $\angle CDB$ are right angles | Given |
> | $\overline{CD} \cong \overline{CD}$ | Reflexive property of congruence |
> | $\triangle ADC \cong \triangle BDC$ | SAS triangle congruence postulate |
> | $\overline{AC} \cong \overline{CB}$ | Corresponding parts of congruent triangles are congruent |

(Converso del teorema de la mediatriz)
**Converse of the perpendicular bisector theorem**: given a segment, any point equidistant to both endpoints, is in the perpendicular bisector of the segment.

> Proof of the converse of the perpendicular bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\overline{AC} \cong \overline{CB}$, $D$ is the midpoint of $\overline{AB}$ | Given, from the *Perpendicular bisector theorem* image |
> | $\triangle ABC$ is isosceles | Definition of isosceles triangle |
> | $\angle A \cong \angle B$ | Base angles theorem |
> | $\overline{AD} \cong \overline{DB}$ | Definition of midpoint |
> | $\triangle ADC \cong \triangle BDC$ | SAS triangle congruence postulate |
> | $\angle CDA \cong \angle CDB$ | Corresponding parts of congruent triangles are congruent |
> | $\angle CDA$ and $\angle CDB$ are supplementary | Linear pair postulate |
> | $\angle CDA$ and $\angle CDB$ are right angles | Congruent linear pairs theorem |
> | $\overleftrightarrow{CD}$ is a perpendicular bisector of $\overline{AB}$ | Definition of perpendicular bisector |

(Punto de concurrencia)
**Point of concurrency**: the intersection in a single point, of three or more lines, rays, or segments.
[Point of concurrency image code](Programs/Ch05/S02_02_Point_of_concurrency_image.py)
![Point of concurrency image](Images/Ch05/S02_02_Point_of_concurrency.png)
*Point of concurrency*

The point $A$ is a point of concurrency.

(Circuncentro de un triángulo)
**Circumcenter of a triangle**: in a triangle, the circumcenter is the point of concurrency formed at the intersection of the three perpendicular bisectors, one from each side.
[Circumcenter of a triangle image code](Programs/Ch05/S02_03_Circumcenter_of_a_triangle_image.py)
![Circumcenter of a triangle image](Images/Ch05/S02_03_Circumcenter_of_a_triangle.png)
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

## Angle bisectors of a triangle (Bisectrices de los ángulos de un triángulo)
[Ch05_S03](https://www.ck12.org/reader/reader-index.html#section/2932949/5.3/9549314)

(Teorema de la equidistancia en la bisectriz de un ángulo)
**Equidistance in an angle bisector theorem**: given an angle, any point in its angle bisector is equidistant to the sides of the angle, using the shortest distance between the point and the sides.
[Equidistance in an angle bisector theorem image code](Programs/Ch05/S03_01_Equidistance_in_an_angle_bisector_theorem_image.py)
![Equidistance in an angle bisector theorem image](Images/Ch05/S03_01_Equidistance_in_an_angle_bisector_theorem.png)
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

(Incentro de un triángulo)
**Incenter of a triangle**: in a triangle, the incenter is the point of concurrency formed at the intersection of the three angle bisectors, one from each vertex.
[Incenter of a triangle image code](Programs/Ch05/S03_02_Incenter_of_a_triangle_image.py)
![Incenter of a triangle image](Images/Ch05/S03_02_Incenter_of_a_triangle.png)
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

## Medians and altitudes of a triangle (Medianas y alturas de un triángulo)
[Ch05_S04](https://www.ck12.org/reader/reader-index.html#section/9549312/5.4/9549314)

(Mediana de un triángulo)
**Median of a triangle**: in a triangle, a median is a segment that connects one vertex with the midpoint of the side opposite to the vertex.
[Median of a triangle image code](Programs/Ch05/S04_01_Median_of_a_triangle_image.py)
![Median of a triangle image](Images/Ch05/S04_01_Median_of_a_triangle.png)
*Median of a triangle*

The segment $\overline{CD}$ is a median of the triangle $\triangle ABC$.

(Centroide de un triángulo)
**Centroid of a triangle**: in a triangle, the centroid is the point of concurrency formed at the intersection of the three medians, one from each vertex.
[Centroid of a triangle image code](Programs/Ch05/S04_02_Centroid_of_a_triangle_image.py)
[Centroid of a triangle image](Images/Ch05/S04_02_Centroid_of_a_triangle.png)
*Centroid of a triangle*

(Teorema de la concurrencia de las medianas de un triángulo)
**Concurrency of the medians of a triangle theorem**: in a triangle, the three medians, one from each vertex to the midpoint of the side opposite to the vertex, intersect each other at a single point which is the centroid. In any given median, the length from the centroid to the vertex is twice the length from the centroid to the midpoint.
[Concurrency of the medians of a triangle theorem image code](Programs/Ch05/S04_03_Concurrency_of_the_medians_of_a_triangle_theorem_image.py)
[Concurrency of the medians of a triangle theorem image](Images/Ch05/S04_03_Concurrency_of_the_medians_of_a_triangle_theorem.png)
*Concurrency of the medians of a triangle theorem*

> Proof of the concurrency of the medians of a triangle theorem
>
> The segment $\overline{DE}$ is a midsegment of $\triangle ABC$, which means that the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$, because of the midsegment theorem. By the alternate interior angles theorem, $\angle AED \cong \angle BAE$ and $\angle BDE \cong \angle ABD$, which means that $\triangle GED$ is similar to $\triangle GAB$. The scale factor to obtain $\triangle GAB$ from $\triangle GED$ is $2$, because of the said proportion between $\overline{AB}$ and $\overline{DE}$. $\overline{AE}$ intersects $\overline{BD}$ at two thirds of its length from $B$, and by using this same logic $\overline{CF}$ intersects $\overline{BD}$ at two thirds of its length from $B$, which means that the three medians intersect at a single point, the centroid. $AG = 2 EG$, $BG = 2 DG$, and $CG = 2 FG$. $\blacksquare$

(Altura de un triángulo)
**Altitude of a triangle**: in a triangle, an altitude is a segment that connects one vertex perpendicularly to the side opposite to the vertex.
[Altitude of a triangle image code](Programs/Ch05/S04_04_Altitude_of_a_triangle_image.py)
![Altitude of a triangle image](Images/Ch05/S04_04_Altitude_of_a_triangle.png)
*Altitude of a triangle*

The altitude $\overline{CD}$ of the triangle $\triangle ABC$ is outside of the triangle, and $D$ does not lie on the side $\overline{AB}$. The altitudes of a triangle don't have to be inside the triangle itself.

(Ortocentro de un triángulo)
**Orthocenter of a triangle**: in a triangle, the orthocenter is the point of concurrency formed at the intersection of the three altitudes, one from each vertex.
[Orthocenter of a triangle image code](Programs/Ch05/S04_05_Orthocenter_of_a_triangle_image.py)
![Orthocenter of a triangle image](Images/Ch05/S04_05_Orthocenter_of_a_triangle.png)
*Orthocenter of a triangle*

The location of the orthocenter depends on the type of triangle. In an obtuse triangle, the orthocenter is outside the triangle. In a right triangle, the orthocenter is the vertex opposite to the hypotenuse. In an acute triangle, the orthocenter is inside the triangle.

## Inequalities in triangles (Desigualdades en los triángulos)
[Ch05_S05](https://www.ck12.org/reader/reader-index.html#section/2932951/5.5/9549314)

(Teorema del lado mayor de un triángulo)
**Triangle longer side theorem**: in a triangle, given two sides, if one side is longer than the other side, then the angle opposite to the longer side is greater than the angle opposite to the other side.
[Triangle longer side theorem image code](Programs/Ch05/S05_01_Triangle_longer_side_theorem_image.py)
![Triangle longer side theorem image](Images/Ch05/S05_01_Triangle_longer_side_theorem.png)
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

(Teorema de la desigualdad del triángulo)
**Triangle inequality theorem**: in a triangle, the sum of the lengths of any two sides, is greater than the length of the remaining side.
[Triangle inequality theorem image code](Programs/Ch05/S05_02_Triangle_inequality_theorem_image.py)
![Triangle inequality theorem image](Images/Ch05/S05_02_Triangle_inequality_theorem.png)
*Triangle inequality theorem*

> Proof of the triangle inequality theorem
>
> Let $\triangle ABC$ have sides with lengths $a$, $b$, $c$. As shown in the image, a triangle can't be formed when $c \ge a + b$ or $c \le |a - b|$. A triangle can be formed when
> $$|a - b| < c < a + b\ \ \blacksquare$$

This result is equivalent to $c < a + b$, $b < a + c$, and $a < b + c$.

(Teorema de la bisagra)
**Hinge theorem**: given two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the included angle from the first triangle has a measure greater than the one from the second triangle, then the remaining side of the first triangle is longer than the one of the second triangle.

> Proof of the hinge theorem
>
> Let $\triangle ABC$ and $\triangle DEF$ be two triangles, let $AB = DE$ and $BC = EF$, and let $m \angle B > m \angle E$, then $AC > DF$ because of the converse of the triangle longer side theorem. $\blacksquare$

(Converso del teorema de la bisagra)
**Converse of the hinge theorem**: given two triangles, if two sides of a triangle are congruent to two sides from the other triangle, and the remaining side of the first triangle is longer than the one of the second triangle, then the included angle from the first triangle has a measure greater than the one from the second triangle.

> Proof of the converse of the hinge theorem
>
> Let $\triangle ABC$ and $\triangle DEF$ be two triangles, let $AB = DE$ and $BC = EF$, and let $AC > DF$, then $m \angle B > m \angle E$ because of the triangle longer side theorem. $\blacksquare$