
#   Properties of triangles (Propiedades de los triángulos)

## Midsegments of a triangle (Segmentos medios de un triángulo)
[Ch05_S01](https://www.ck12.org/reader/reader-index.html#section/2932947/5.1/9549314)

(Segmento medio de un triángulo)
**Midsegment of a triangle**: a segment that connects the two midpoints of adjacent sides.
[Midsegment of a triangle image code](Programs/Ch05/S01_01_Midsegment_of_a_triangle_image.py)
![Midsegment of a triangle image](Images/Ch05/S01_01_Midsegment_of_a_triangle.png)
*Midsegment of a triangle*

The segment $\overline{DE}$ is a midsegment of the triangle $\triangle ABC$.

Every triangle has three midsegments.
[Three midsegments of a triangle image code](Programs/Ch05/S01_02_Three_midsegments_of_a_triangle_image.py)
![Three midsegments of a triangle image](Images/Ch05/S01_02_Three_midsegments_of_a_triangle.png)
*Three midsegments of a triangle*

(Teorema del segmento medio)
**Midsegment theorem**: a midsegment of a triangle measures half the length of its parallel side.

> Proof of the midsegment theorem
>
> The proof of this theorem requires the concept of similarity, which is explained in detail in another file (see Ch07_Similarity.md). Two figures are similar when they have the same shape but not necessarily the same size. By SAS, the triangle $\triangle ABC$ is similar to $\triangle DEC$. Given that $D$ is the midpoint of $\overline{AC}$, then $\overline{DC}$ has half the length of $\overline{AC}$, and so by similarity, the scale factor needed to obtain $\triangle DEC$ from $\triangle ABC$ is one half, therefore the measure of $\overline{DE}$ is one half the measure of $\overline{AB}$. $\blacksquare$

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

## Inequalities in triangles (Desigualdades en los triángulos)
[Ch05_S05](https://www.ck12.org/reader/reader-index.html#section/2932951/5.5/9549314)

## Indirect proof (Demostración por contradicción)
[Ch05_S06](https://www.ck12.org/reader/reader-index.html#section/2932952/5.6/9549314)