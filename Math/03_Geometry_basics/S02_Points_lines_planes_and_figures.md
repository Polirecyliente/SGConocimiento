
#   Points, lines, planes, and figures (Puntos, líneas, planos, y figuras)

(Línea transversal)
**Transversal line**: a line that intersects two other distinct lines.
[Transversal line image code](Programs/S02/Transversal_line_image.py)
![Transversal line image](Images/S02/Transversal_line.png)
*Transversal line*

The lime green line is the transversal, although all the lines intersect the other two, which means that effectively all three lines are transversal. The case in which this does not happen, is when the other two lines are parallel.
[Transversal to parallel lines image code](Programs/S02/Transversal_to_parallel_lines_image.py)
![Transversal to parallel lines image](Images/S02/Transversal_to_parallel_lines.png)
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

(Proporcionalidad entre transversales)
**Transversal proportionality**: any set of parallel lines can be crossed by an infinite amount of transversals. The transversals are divided proportionally, so the segments formed by the intersections of each transversal with the parallels, are proportional to those of the other transversals.
[Transversal proportionality image code](Programs/S02/Transversal_proportionality_image.py)
![Transversal proportionality image](Images/S02/Transversal_proportionality.png)
*Transversal proportionality*

There are proportions between the corresponding segments created with the points $A$, $B$, $C$, and the points $D$, $E$, $F$, because of this, it can be said that the figure $ABC$ is similar to the figure $DEF$.

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
**Ruler postulate**: when placing a ruler to measure the distance between two given points, said distance is the absolute value of the difference of the numbers of each point in the ruler. The distance between two points $A$ and $B$ is $B_{value} - A_{value}$, the subindex $value$ indicates that it's a measure, in this case a measure of the ruler.

(Postulado de adición de segmentos)
**Segment addition postulate**: given three collinear points with one point being between the other two (the endpoints), the measure of the distance between the endpoints, is equal to the sum of the distances of each endpoint to the point between them.

> Segment addition postulate
>
> Let $A$, $B$, and $C$, be three collinear points, with $B$ being between $A$ and $C$, then
> $$AB + BC = AC$$

The segment addition postulate can be visualized with the following image.
[Segment addition postulate image code](Programs/S01/Segment_addition_postulate_image.py)
![Segment addition postulate image](Images/S01/Segment_addition_postulate.png)
*Segment addition postulate*

(Postulado del transportador)
**Protractor postulate**: when placing a protractor to measure the angle between two rays, said angle is the absolute value of the difference of the numbers of each ray in the protractor. The measure of the angle $\angle ABC$ is $BC_{value} - AB_{value}$, the subindex $value$ indicates that it's a measure, in this case a measure of the protractor at the segments $\overline{AB}$ and $\overline{BC}$.

(Postulado de adición de ángulos)
**Angle addition postulate**: given two angles that share a common ray and they cover distinct space, the measure of the angle between the two non common rays, is equal to the sum of the two angles given.

> Angle addition postulate
>
> Let $\overrightarrow{AD}$, $\overrightarrow{BD}$, and $\overrightarrow{CD}$, be three rays such that two angles are formed that share the common ray $\overrightarrow{BD}$, i.e. the angles $\angle ADB$ and $\angle CDB$, then
> $$m \angle ADB + m \angle CDB = m \angle ADC$$

[Angle addition postulate image code](Programs/S01/Angle_addition_postulate_image.py)
![Angle addition postulate image](Images/S01/Angle_addition_postulate.png)
*Angle addition postulate*

(Postulado del punto medio)
**Midpoint postulate**: a segment has exactly one midpoint. If the point $B$ is the midpoint of $\overline{AC}$, then $B$ is the only point that is the midpoint.

(Postulado de la mediatriz)
**Perpendicular bisector postulate**: a given segment has only one line that is its perpendicular bisector.

There are infinitely many segment bisectors and only one perpendicular bisector to a given segment. As shown in the *Perpendicular bisector* image, $\overleftrightarrow{DE} \perp \overline{AC}$, and $\overline{AB} \cong \overline{BC}$, so the line $\overleftrightarrow{DE}$ is the perpendicular bisector of $\overline{AC}$.

(Postulado de la bisectriz de un ángulo)
**Angle bisector postulate**: a given angle has only one line that is its angle bisector.

In the *Angle bisector* image, if the segment $\overline{AC}$ is extended into a line, then the line $\overleftrightarrow{AC}$ is the angle bisector of the angle $\angle DAB$, so $m \angle BAC = m \angle DAC$. The angle bisector does not have to be a line, but if it's a line then it's guaranteed to be the only one that is the angle bisector.

(Postulado del par lineal)
**Linear pair postulate**: the two angles of a linear pair are supplementary. If $\angle A$ and $\angle B$ form a linear pair, then $\angle A$ and $\angle B$ are supplementary.

(Postulado de las paralelas)
**Parallel postulate**: given a line and a point not on the line, there is only one parallel to the line that passes through the point. Given a line $l$ and a point $A$ that does not lie on $l$, then only one line $m$ passes through $A$ and $l \parallel m$.

(Postulado de las perpendiculares)
**Perpendicular postulate**: given a line and a point not on the line, there is only one perpendicular line to the line that passes through the point. Given a line $l$ and a point $A$ that does not lie on $l$, then only one line $m$ passes through $A$ and $l \perp m$.

(Postulado de los ángulos correspondientes)
**Corresponding angles postulate**: in a transversal of two parallels, the corresponding angles are congruent. From the *Transversal to parallel lines* image, $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, and $\angle 4 \cong \angle 8$.

(Converso del postulado de los ángulos correspondientes)
**Converse of the corresponding angles postulate**: if the corresponding angles of a transversal are congruent, then the transversal is a transversal of two parallels. From the *Transversal to parallel lines* image, if $\angle 1 \cong \angle 5$, and/or $\angle 2 \cong \angle 6$, and/or $\angle 3 \cong \angle 7$, and/or $\angle 4 \cong \angle 8$, then $l \parallel m$, with transversal $t$.

(Propiedad reflexiva de la congruencia)
**Reflexive property of congruence**: a figure is congruent with itself. Given $\overline{AB}$, and $\angle ABC$, then $\overline{AB} \cong \overline{AB}$ and $\angle ABC \cong \angle ABC$.

(Propiedad simétrica de la congruencia)
**Symmetric property of congruence**: if a first figure is congruent to a second, then the second figure is congruent to the first. Let $\overline{AB}$, $\overline{CD}$ be segments, if $\overline{AB} \cong \overline{CD}$ then $\overline{CD} \cong \overline{AB}$.

(Propiedad transitiva de la congruencia)
**Transitive property of congruence**: if a first figure is congruent to a second, and the second figure is congruent to a third, then the third figure is congruent to the first. Let $\overline{AB}$, $\overline{CD}$, $\overline{EF}$ be segments, if $\overline{AB} \cong \overline{CD}$ and $\overline{CD} \cong \overline{EF}$ then $\overline{AB} \cong \overline{EF}$.

(Teorema del ángulo recto)
**Right angle theorem**: all right angles are congruent.

> Proof of the right angle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$ and $\angle B$ be any two right angles | Given |
> | $m \angle A = \pi/2$ and $m \angle B = \pi/2$ | Definition of right angles |
> | $m \angle A = m \angle B$ | Transitive property of equality |
> | $\angle A \cong \angle B$ | Definition of congruence |

[Right angle theorem image code](Programs/S02/Right_angle_theorem_image.py)
![Right angle theorem image](Images/S02/Right_angle_theorem.png)
*Right angle theorem*

The segments may not be congruent but the right angles are.

If $\angle A$ and $\angle B$ are right angles, then $\angle A \cong \angle B$.

(Teorema de los ángulos verticales)
**Vertical angles theorem**: two angles that are vertical angles, are also congruent.

> Proof of the vertical angles theorem
>
> Using the *Vertical angles* image, the angles $\alpha_1$ and $\beta_1$ form a linear pair, as do the angles $\alpha_2$ and $\beta_1$. This means that the measures of the angles $\alpha_1$ and $\alpha_2$ must be the same, and so $\alpha_1 \cong \alpha_2$.
>
> On the other hand, the angles $\alpha_1$ and $\beta_2$ form a linear pair, as do the angles $\alpha_1$ and $\beta_1$, which means that also $\beta_1 \cong \beta_2$. $\blacksquare$

If $\angle A$ and $\angle B$ are vertical angles, then $\angle A \cong \angle B$.

(Teorema de los pares lineales congruentes)
**Congruent linear pairs theorem**: in a linear pair, if the two angles are congruent, then they have a measure of $\pi/2$, meaning that if both angles of a linear pair are congruent then they are right angles.

> Proof of the congruent linear pairs theorem
>
> Let $\angle A$ and $\angle B$ form a linear pair, and let $\angle A \cong \angle B$, then $m \angle A = m \angle B$, $m \angle A + m \angle B = \pi \Rightarrow 2 m \angle A = \pi \Rightarrow m \angle A = \pi/2 = m \angle B$. So $\angle A$ and $\angle B$ are right angles. $\blacksquare$

If $\angle A$ and $\angle B$ form a linear pair, and $\angle A \cong \angle B$, then $\angle A$ and $\angle B$ are right angles.

(Teorema de los suplementos congruentes)
**Congruent supplements theorem**: two angles are congruent when they are supplementary to another angle, or when they are supplementary to two other congruent angles.

> Proof of the congruent supplements theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$, $\angle B$, $\angle C$ be angles | Given |
> | Let $\angle A$ and $\angle C$ be supplements of $\angle B$ | Given |
> | $m \angle A + m \angle B = \pi$, $m \angle C + m \angle B = \pi$ | Definition of supplementary angles |
> | $m \angle A + m \angle B = m \angle C + m \angle B$ | Transitive property of equality |
> | $m \angle A = m \angle C$ | Subtraction property of equality |
> | $\angle A \cong \angle C$ | Definition of congruence |

If $\angle A$ and $\angle C$ are supplements of $\angle B$, then $\angle A \cong \angle C$.

(Converso del teorema de los suplementos congruentes)
**Converse of the congruent supplements theorem**: if two angles are congruent, and one of them is supplementary to a third angle, then both angles are supplementary to the third angle.

> Proof of the converse of the congruent supplements theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$, $\angle B$, $\angle C$ be angles | Given |
> | Let $\angle A \cong \angle C$, and $\angle A$ and $\angle B$ be supplementary | Given |
> | $m \angle A = m \angle C$ | Definition of congruence |
> | $m \angle A + m \angle B = \pi$ | Definition of supplementary angles |
> | $m \angle C + m \angle B = \pi$ | Substitution property of equality |
> | $\angle B$ and $\angle C$ are supplementary | Definition of supplementary angles |

If $\angle A \cong \angle C$, and $\angle A$ and $\angle B$ are supplementary, then $\angle B$ and $\angle C$ are supplementary.

(Teorema de los complementos congruentes)
**Congruent complements theorem**: two angles are congruent when they are complementary to another angle, or when they are complementary to two other congruent angles.

> Proof of the congruent complements theorem
>
> Let $\angle A$, $\angle B$, $\angle C$ be angles, such that $\angle A$ and $\angle C$ are complements of $\angle B$. This means that $m \angle A + m \angle B = \pi/2$ and $m \angle C + m \angle B = \pi/2$, then by transitivity $m \angle A + m \angle B = m \angle C + m \angle B$ which can be simplified to $m \angle A = m \angle C$, and in turn $\angle A \cong \angle C$ by definition. $\blacksquare$

If $\angle A$ and $\angle C$ are complements of $\angle B$, then $\angle A \cong \angle C$.

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

(Teorema de la proporcionalidad entre transversales)
**Transversal proportionality theorem**: given a set of parallel lines, and a set of transversals to the parallels, the transversals are divided proportionally by the parallels, so the segments formed by the intersections of each transversal with the parallels, are proportional to those of the other transversals.

> Proof of the transversal proportionality theorem
>
> Let there be a set of $m$ parallel lines $l_1$, $l_2$, ..., $l_m$, and a set of $n$ transversals to the parallels $t_1$, $t_2$, ..., $t_n$. Let $t_i$ indicate the transversal $i$, and $l_j$ indicate the parallel $j$. Let $i1$ and $i2$ indicate any two distinct values of $i$, and $j1$ and $j2$ indicate any two distinct values of $j$. Let $d_{i, j}$ indicate the length of the segment in the transversal $t_i$, between the parallels $l_j$ and $l_{j + 1}$ (so that $j$ can go up to $m - 1$).
>
> There are only two possible scenarios for each transversal $t_i$ with regards to each of the other transversals. Each pair of transversals $t_{i1}$ and $t_{i2}$ either intersect each other at some point if they are not parallel, or they never intersect each other if they are parallel.
>
> If $t_{i1}$ and $t_{i2}$ are parallel, then the pairs of segments between any two parallel lines are congruent, because one parallel lines can replace the other and the lengths of the segments are the same, so $d_{i1, j1} = d_{i2, j1}$, $d_{i1, j2} = d_{i2, j2}$, and therefore, by the division property of equality, $\frac{d_{i1, j1}}{d_{i1, j2}} = \frac{d_{i2, j1}}{d_{i2, j2}}$, meaning that the segments are divided proportionally.
>
> If $t_{i1}$ and $t_{i2}$ are not parallel, then they intersect each other at a certain point, and they form a triangle with each parallel $l_j$. Because of the triangle proportionality theorem, the parallels divide the transversals proportionally, meaning that $\frac{d_{i1, j1}}{d_{i1, j2}} = \frac{d_{i2, j1}}{d_{i2, j2}}$.
>
> As can be seen, in all cases $\frac{d_{i1, j1}}{d_{i1, j2}} = \frac{d_{i2, j1}}{d_{i2, j2}}$ for all the possible values of $i$ and $j$. $\blacksquare$

Given a set of $m$ parallel lines $l_1$, $l_2$, ..., $l_m$, and a set of $n$ transversals to the parallels $t_1$, $t_2$, ..., $t_n$, the intersections of each transversal with the parallels form $m - 1$ segments. Let $d_{i, j}$ indicate the length of the segment in the transversal $t_i$, between the parallels $l_j$ and $l_{j + 1}$ (so that $j$ can go up to $m - 1$), then $\frac{d_{i1, j1}}{d_{i1, j2}} = \frac{d_{i2, j1}}{d_{i2, j2}}$ for all the possible values of $i$ and $j$ ($i1$ and $i2$ indicate two different values of $i$, the same for $j1$ and $j2$ which are different values of $j$).

(Teorema de la proporcionalidad en la bisectriz de un ángulo)
**Proportionality in an angle bisector theorem**: in a triangle, the angle bisector of any one of its angles creates a proportion. The angle bisector in a triangle, cuts the opposite side to the angle into two segments. The proportion created is that the first segment cut is to the second segment cut as the first side of the angle is to the second side of the angle bisected.
[Proportionality in an angle bisector theorem image code](Programs/S07/Proportionality_in_an_angle_bisector_theorem_image.py)
![Proportionality in an angle bisector theorem image](Images/S07/Proportionality_in_an_angle_bisector_theorem.png)
*Proportionality in an angle bisector theorem*

In this definition, the first side can be any of the two sides of the angle, what matters is that the first segment cut is on the same side of the angle bisector as the first side of the angle, and the same for the second segment cut.

> Proof of the proportionality in an angle bisector theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $\triangle ABC$ exists, $\overline{BD}$ is an angle bisector of $\angle B$. The point $D$ is the point where $\overline{BD}$ intersects $\overline{AC}$. The auxiliary point $E$ is created such that $A$, $B$, and $E$ are collinear, and $\overline{BD} \parallel \overline{CE}$ | Given |
> | (1) $\angle ABD \cong \angle AEC$ and $\angle ADB \cong \angle ACE$ | Corresponding angles postulate |
> | (2) $\angle ABD \cong \angle CBD$ | Definition of angle bisector |
> | (3) $\angle CBD \cong \angle BCE$ | Alternate interior angles theorem |
> | $\angle AEC \cong \angle BCE$ | Transitive property of congruence from (1) into (2) into (3) |
> | $\triangle BCE$ is isosceles | Converse of the base angles theorem |
> | (4) $BC = BE$ | Definition of isosceles triangle |
> | $\triangle ABD \sim \triangle AEC$ | AA triangle similarity postulate from (1) |
> | $\frac{CD}{AD} = \frac{BE}{AB}$ | Triangle proportionality theorem |
> | $\frac{CD}{AD} = \frac{BC}{AB}$ | Substitution property of equality from (4) |
> | $\frac{AD}{CD} = \frac{AB}{BC}$ | Corollaries of the cross product theorem and its converse |

In a triangle $\triangle ABC$, the angle bisector of $\angle B$ intersects the side $\overline{AC}$ at a point $D$. This creates the proportion $\frac{AD}{CD} = \frac{AB}{BC}$.

(Teorema del perímetro de figuras similares)
**Perimeter of similar figures theorem**: given two similar figures, that have a scale factor that measures the ratio of each length from the second figure over the respective length in the first figure, then the ratio of the perimeter of the second figure over the perimeter of the first figure is equal to the scale factor.

> Proof of the perimeter of similar figures theorem
>
> Let $Fig_1$ and $Fig_2$ be two similar figures, $Fig_1 \sim Fig_2$, and let $k$ be the scale factor to obtain $Fig_2$ from $Fig_1$. Let the most external sides of $Fig_1$ have lengths with measures $a_1$, $b_1$, $c_1$, ..., $z_1$, so the most external sides of $Fig_2$ have lengths with measures $a_2 = k a_1$, $b_2 = k b_1$, $c_2 = k c_1$, ..., $z_2 = k z_1$. Finally, let $P_1$ be the perimeter of $Fig_1$, and let $P_2$ be the perimeter of $Fig_2$. Because of the definition of perimeter, $P_1 = a_1 + b_1 + c_1 + ... + z_1$ and $P_2 = a_2 + b_2 + c_2 + ... + z_2$, and then by substitution and factoring the common factor $k$, $P_2 = k (a_1 + b_1 + c_1 + ... + z_1)$, so $P_2 = k P_1$. $\blacksquare$

In two similar figures $Fig_1$ and $Fig_2$, $Fig_1 \sim Fig_2$, with perimeters $P_1$ and $P_2$ respectively, and with a scale factor $k$ to obtain $Fig_2$ from $Fig_1$, then $P_2 = k P_1$.