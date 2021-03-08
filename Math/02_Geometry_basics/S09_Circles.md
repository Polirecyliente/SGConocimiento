
#   Circles (Círculos)

<!--
#T# Table of contents

#C# Parts of circles and tangent lines (Partes de los círculos y líneas tangentes)
#C# Properties of arcs (Propiedades de los arcos)
#C# Properties of chords (Propiedades de las cuerdas)
#C# Inscribed angles (Ángulos inscritos)
#C# Angles of chords, secants, and tangents (Ángulos de cuerdas, secantes, y tangentes)
#C# Segments of chords, secants, and tangents (Segmentos de cuerdas, secantes, y tangentes)
#C# Writing and graphing the equations of circles (Escribir y graficar las ecuaciones de los círculos)

#T# Beginning of content
-->

## Parts of circles and tangent lines (Partes de los círculos y líneas tangentes)

(Círculo)
**Circle**: shape in which all of its points are at the same distance from its center. A circle centered around the point $A$ is denoted as $\bigodot A$.

(Radio de un círculo)
**Radius of a circle**: the distance from the center of a circle to any of its points.

(Diámetro de un círculo)
**Diameter of a circle**: the maximum possible distance between two points in a circle. This is the same as twice the radius.

(Cuerda de un círculo)
**Chord of a circle**: a segment that joins two points of a circle.

(Secante de un círculo)
**Secant of a circle**: a line that passes through two points of a circle.

(Tangente de un círculo)
**Tangent of a circle**: a line that passes through a single one point of a circle.

(Punto de tangencia)
**Point of tangency**: in a circle, a tangent passes through only one point of the circle, this is the point of tangency.

Examples of the radius, diameter, chord, secant, and tangent, in a circle, are shown in the following figure.
[Segments and lines of a circle image code](Programs/S09/01_Segments_and_lines_of_a_circle_image.py)
![Segments and lines of a circle image](Images/S09/01_Segments_and_lines_of_a_circle.png)
*Segments and lines of a circle*

(Relaciones entre círculos)
**Relationships between circles**: two given circles can relate to each other. A few ways to relate them are, by their intersection, by their relative position, and by their radii.

(Dos círculos con dos puntos de intersección)
**Two circles with two points of intersection**: two circles can intersect each other at a maximum of two points.
[Two circles with two points of intersection image code](Programs/S09/02_Two_circles_with_two_points_of_intersection_image.py)
![Two circles with two points of intersection image](Images/S09/02_Two_circles_with_two_points_of_intersection.png)
*Two circles with two points of intersection*

(Dos círculos tangentes)
**Two tangent circles**: two circles can intersect each other in a single point, when they are tangent to each other.
[Two tangent circles image code](Programs/S09/03_Two_tangent_circles_image.py)
![Two tangent circles image](Images/S09/03_Two_tangent_circles.png)
*Two tangent circles*

(Dos círculos concéntricos)
**Two concentric circles**: two circles with distinct radii and the same center point.
[Two concentric circles image code](Programs/S09/04_Two_concentric_circles_image.py)
![Two concentric circles image](Images/S09/04_Two_concentric_circles.png)
*Two concentric circles*

(Círculos congruentes)
**Congruent circles**: in a given set of circles, they are congruent if their radii have the same length. In circles $\bigodot A$ and $\bigodot B$, where $r_A$ is the radius of $\bigodot A$ and $r_B$ is the radius of $\bigodot B$, if $r_A = r_B$, then $\bigodot A \cong \bigodot B$.

(Línea tangente)
**Tangent line**: a line that passes through a single point of a curve. It can also be a ray or a segment.

(Tangencia interna de dos círculos)
**Internal tangency of two circles**: two tangent circles are internally tangent when one is inside the other.
[Internal tangency of two circles image code](Programs/S09/05_Internal_tangency_of_two_circles_image.py)
![Internal tangency of two circles image](Images/S09/05_Internal_tangency_of_two_circles.png)
*Internal tangency of two circles*

If two circles are internally tangent, with the tangent line being $\overleftrightarrow{AB}$, then both circles are on the same side of the line $\overleftrightarrow{AB}$.

(Tangencia externa de dos círculos)
**External tangency of two circles**: two tangent circles are externally tangent when they are on different sides of their tangent line.
[External tangency of two circles image code](Programs/S09/06_External_tangency_of_two_circles_image.py)
![External tangency of two circles image](Images/S09/06_External_tangency_of_two_circles.png)
*External tangency of two circles*

If two circles are externally tangent, with the tangent line being $\overleftrightarrow{AB}$, then each circle is on a different side of the line $\overleftrightarrow{AB}$.

(Tangente interior común)
**Common internal tangent**: in two circles that are not tangent to each other, two tangent lines can be built that are common internal tangents. A common internal tangent, is a line or segment that is tangent to each of the two circles, and it intersects the segment that joins the two centers of the circles.
[Common internal tangent image code](Programs/S09/07_Common_internal_tangent_image.py)
![Common internal tangent image](Images/S09/07_Common_internal_tangent.png)
*Common internal tangent*

In two circles $\bigodot A$ and $\bigodot B$, if the two common internal tangents are $\overline{C_1D_1}$ and $\overline{C_2D_2}$, then those two segments intersect $\overline{AB}$.

(Tangente exterior común)
**Common external tangent**: in two circles that are not tangent to each other, two tangent lines can be built that are common external tangents. A common external tangents, is a line or segment that is tangent to each of the two circles, and does not intersect the segment that joins the two centers of the circles.
[Common external tangent image code](Programs/S09/08_Common_external_tangent_image.py)
![Common external tangent image](Images/S09/08_Common_external_tangent.png)
*Common external tangent*

In two circles $\bigodot A$ and $\bigodot B$, if the two common external tangents are $\overline{C_1D_1}$ and $\overline{C_2D_2}$, then those two segments do not intersect $\overline{AB}$.

(Teorema de la tangente de un círculo)
**Tangent to a circle theorem**: in a circle, the angle between a tangent and the radius at the point of tangency, is a right angle.

> Proof of the tangent to a circle theorem
>
> Given a circle $\bigodot A$, with a radius $\overline{AB}$, and with a tangent $\overline{BC}$, then the angle $\angle ABC$ is a right angle, because the shortest distance between a point and a line is the perpendicular distance between the point and the line. The shortest distance between $A$ and $\overline{BC}$ has to be $AB$ (even extending $\overline{BC}$), because if there was a point from the extended $\overline{BC}$ that was nearer to $A$, that point would have to be inside $\bigodot A$, but this can't happen because of the definition of a tangent line, so the nearest point from $\overline{BC}$ to $A$, is $B$, which means that $\overline{AB} \perp \overline{BC}$, and $\angle ABC$ is a right angle. $\blacksquare$

In a circle $\bigodot A$, a tangent to the circle $\overline{BC}$ with the point of tangency being $B$, then the angle $\angle ABC$ is a right angle.

(Converso del teorema de la tangente de un círculo)
**Converse of the tangent to a circle theorem**: in a circle, if a radius is perpendicular to a line or segment passing through the non-center endpoint of the radius, then that line or segment is tangent to the circle.

> Proof of the converse of the tangent to a circle theorem
>
> Given a circle $\bigodot A$, with $B$ being a point on the circle so that $\overline{AB}$ is a radius of the circle, and given a segment $\overline{BC}$, if $\overline{AB} \perp \overline{BC}$, then $AB$ is the shortest distance from $A$ to $\overline{BC}$, even extending $\overline{BC}$. This means that $\overline{BC}$ is tangent to the circle $\bigodot A$, because there is no point in the extended $\overline{BC}$ that is neared to $A$, than $B$, and so no point of the extended $\overline{BC}$ is inside $\bigodot A$. $\blacksquare$

In a circle $\bigodot A$, with $B$ being a point on the circle, and given a segment $\overline{BC}$, if $\overline{AB} \perp \overline{BC}$, then $\overline{BC}$ is tangent to the circle $\bigodot A$.

(Teorema de las dos tangentes)
**Two tangents theorem**: given a circle and a point outside of the circle, then the two possible tangent segments from the point to the circle are congruent.
[Two tangents theorem image code](Programs/S09/09_Two_tangents_theorem_image.py)
![Two tangents theorem image](Images/S09/09_Two_tangents_theorem.png)
*Two tangents theorem*

> Proof of the two tangents theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with a point $B$ outside of it. The two possible tangents from $B$ to $\bigodot A$, are $\overline{BC}$ and $\overline{BD}$ | Given |
> | $\overline{AB} \cong \overline{AB}$ | Reflexive property of congruence |
> | $\angle ACB$ and $\angle ADB$ are right angles | Tangent to a circle theorem |
> | $\overline{AC} \cong \overline{AD}$ | Definition of radius of a circle |
> | $\triangle ABC \cong \triangle ABD$ | Hypotenuse-leg congruence theorem |
> | $\overline{BC} \cong \overline{BD}$ | Corresponding parts of congruent triangles are congruent |

In a circle $\bigodot A$, with a point $B$ outside of it, if the two possible tangents from $B$ to $\bigodot A$, are $\overline{BC}$ and $\overline{BD}$, then $\overline{BC} \cong \overline{BD}$.

## Properties of arcs (Propiedades de los arcos)

(Arco en un círculo)
**Arc in a circle**: in a circle, an arc is any continuous portion of points in the shape. Because of the way in that a circle exists, an arc can always be limited by two radii. In a circle $\bigodot A$, given the points $B$ and $C$ that lie on the shape of the circle (meaning that both $\overline{AB}$ and $\overline{AC}$ are radii), the arc between $B$ and $C$ is denoted as $\widehat{BC}$.

(Ángulo central en un círculo)
**Central angle in a circle**: in a circle, a central angle is an angle made with two radii of the circle. In a circle $\bigodot A$, given two radii $\overline{AB}$ and $\overline{AC}$, the angle $\angle BAC$ is a central angle.

(Arco mayor y arco menor)
**Major arc and minor arc**: in a circle, a central angle divides the circle into two arcs, one major arc which is the longer arc, and one minor arc which is the shorter arc (unless the central angle is $\pi$ in which case both arcs are congruent). In a circle $\bigodot A$, given two radii $\overline{AB}$ and $\overline{AC}$, that make an angle $\angle BAC$ with a measure less than $\pi$, then the arc $\widehat{BC}$ is a minor arc. For the corresponding major arc, an extra point is needed to differentiate it from the minor arc. Let a point $D$ lie on the major arc, this arc is then labeled as $\widehat{BDC}$. The central angle refers to the angle spanned by the minor arc.

The central angle, major and minor arcs in a circle can be seen in the following image.
[Arcs and central angle in a circle image code](Programs/S09/10_Arcs_and_central_angle_in_a_circle_image.py)
![Arcs and central angle in a circle image](Images/S09/10_Arcs_and_central_angle_in_a_circle.png)
*Arcs and central angle in a circle*

(Semicírculo)
**Semicircle**: in a circle, a semicircle is an arc that occupies half the circle, i.e. an arc with a central angle of $\pi$, meaning that the major arc and the minor arc are both semicircles.

(Medida de un arco)
**Arc measure**: the measure of an arc is in length units. In the arc $\widehat{BC}$, the measure of this arc is denoted as $m \widehat{BC}$. If not stated, the unit of measure of an arc is the same of that of the radius.

(Arcos congruentes)
**Congruent arcs**: two arcs ar congruent when they have the same length. Given two arcs $\widehat{BC}$ and $\widehat{DE}$, if $m \widehat{BC} = m \widehat{DE}$, then $\widehat{BC} \cong \widehat{DE}$.

(Postulado de adición de arcos)
**Arc addition postulate**: in a circle, given two consecutive arcs, the total arc length of both arcs is equal to the sum of the lengths of the two arcs.

> Arc addition postulate
>
> Let $\widehat{BC}$ and $\widehat{CD}$ be two consecutive arcs, then
> $$m \widehat{BD} = m \widehat{BC} + m \widehat{CD}$$

The arc addition postulate can be visualized with the following image.
[Arc addition postulate image code](Programs/S09/11_Arc_addition_postulate_image.py)
![Arc addition postulate image](Images/S09/11_Arc_addition_postulate.png)
*Arc addition postulate*

## Properties of chords (Propiedades de las cuerdas)

(Cuerdas y arcos correspondientes)
**Corresponding chords and arcs**: in an arc, the corresponding chord is the chord formed with the endpoints of the arc. In an arc $\widehat{BC}$, its corresponding chord is $\overline{BC}$. In a chord, the corresponding arc is the arc formed with the endpoints of the chord. In a chord $\overline{BC}$, its corresponding arc is $\widehat{BC}$.

(Teorema de las cuerdas congruentes desde arcos congruentes)
**Congruent chords from congruent arcs theorem**: in a circle (or in two congruent ones), given two arcs and their corresponding chords, if the two arcs are congruent then the two corresponding chords are congruent.
[Congruent chords from congruent arcs theorem image code](Programs/S09/12_Congruent_chords_from_congruent_arcs_theorem_image.py)
![Congruent chords from congruent arcs theorem image](Images/S09/12_Congruent_chords_from_congruent_arcs_theorem.png)
*Congruent chords from congruent arcs theorem*

> Proof of the congruent chords from congruent arcs theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with $B$, $C$, $D$, and $E$ being points that lie on the circle, and $\widehat{BC} \cong \widehat{DE}$ | Given |
> | $\angle BAC \cong \angle DAE$ | Definition of central angle |
> | $\overline{AB} \cong \overline{AC}$ and $\overline{AD} \cong \overline{AE}$ | Definition of radius |
> | $\triangle BAC \cong \triangle DAE$ | SAS triangle congruence postulate |
> | $\overline{BC} \cong \overline{DE}$ | Corresponding parts of congruent triangles are congruent |

In a circle $\bigodot A$ (or in two congruent ones), given two arcs $\widehat{BC}$ and $\widehat{DE}$, with their corresponding chords being $\overline{BC}$ and $\overline{DE}$, if $\widehat{BC} \cong \widehat{DE}$, then $\overline{BC} \cong \overline{DE}$.

(Converso del teorema de las cuerdas congruentes desde arcos congruentes)
**Converse of the congruent chords from congruent arcs theorem**: in a circle (or in two congruent ones), given two chords and their corresponding arcs, if the two chords are congruent then the two corresponding arcs are congruent.

> Proof of the converse of the congruent chords from congruent arcs theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with $B$, $C$, $D$, and $E$ being points that lie on the circle, and $\overline{BC} \cong \overline{DE}$ | Given, from the *Congruent chords from congruent arcs theorem* image |
> | $\overline{AB} \cong \overline{AC}$ and $\overline{AD} \cong \overline{AE}$ | Definition of radius |
> | $\triangle BAC \cong \triangle DAE$ | SSS triangle congruence postulate |
> | $\angle BAC \cong \angle DAE$ | Corresponding parts of congruent triangles are congruent |
> | $\widehat{BC} \cong \widehat{DE}$ | Definition of central angle |

In a circle $\bigodot A$ (or in two congruent ones), given two chords $\overline{BC}$ and $\overline{DE}$, with their corresponding arcs being $\widehat{BC}$ and $\widehat{DE}$, if $\overline{BC} \cong \overline{DE}$, then $\widehat{BC} \cong \widehat{DE}$.

(Teorema de la mediatriz de una cuerda)
**Perpendicular bisector of a chord theorem**: in a circle, given a chord, then the perpendicular bisector of the chord passes through the center of the circle, meaning that the perpendicular bisector of the chord can make a diameter of the circle.
[Perpendicular bisector of a chord theorem image code](Programs/S09/13_Perpendicular_bisector_of_a_chord_theorem_image.py)
![Perpendicular bisector of a chord theorem image](Images/S09/13_Perpendicular_bisector_of_a_chord_theorem.png)
*Perpendicular bisector of a chord theorem*

> Proof of the perpendicular bisector of a chord theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with a chord $\overline{BC}$ that has a perpendicular bisector $\overline{DE}$. The point $F$ is the point of intersection of $\overline{BC}$ and $\overline{DE}$ | Given |
> | (1) $D$, $E$, and $F$ are collinear | Definition of a line |
> | $\overline{AF} \cong \overline{AF}$ | Reflexive property of congruence |
> | $\overline{AB} \cong \overline{AC}$ | Definition of radius |
> | $\overline{BF} \cong \overline{CF}$ | Definition of perpendicular bisector |
> | $\triangle ABF \cong \triangle ACF$ | SSS triangle congruence postulate |
> | $\angle BAF \cong \angle CAF$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{AF}$ is an angle bisector of $\angle BAC$ | Definition of angle bisector |
> | $\overline{DE}$ is an angle bisector of $\angle BAC$ | From (1) |
> | $A$ lies on $\overline{DE}$ | The vertex of an angle lies on its angle bisector |
> | $\overline{DE}$ is a diameter of $\bigodot A$ | Definition of diameter |

In a circle $\bigodot A$, given a chord $\overline{BC}$, the chord's perpendicular bisector $\overline{DE}$ is a diameter of $\bigodot A$.

(Converso del teorema de la mediatriz de una cuerda)
**Converse of the perpendicular bisector of a chord theorem**: in a circle, given a chord and a diameter that intersects the chord perpendicularly, then the diameter bisects the chord.

> Proof of the converse of the perpendicular bisector of a chord theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with a chord $\overline{BC}$, and a diameter $\overline{DE}$ that intersects $\overline{BC}$ such that $\overline{BC} \perp \overline{DE}$ | Given, from the *Perpendicular bisector of a chord theorem* image |
> | $\overline{AF} \cong \overline{AF}$ | Reflexive property of congruence |
> | $\overline{AB} \cong \overline{AC}$ | Definition of radius |
> | $\triangle ABF \cong \triangle ACF$ | Hypotenuse-leg congruence theorem |
> | $\overline{BF} \cong \overline{CF}$ | Corresponding parts of congruent triangles are congruent |
> | $\overline{DE}$ is a perpendicular bisector of $\overline{BC}$ | Definition of perpendicular bisector |

In a circle $\bigodot A$, given a chord $\overline{BC}$ and a diameter $\overline{DE}$ that intersects $\overline{BC}$ perpendicularly, then $\overline{DE}$ is a perpendicular bisector of $\overline{BC}$.

(Teorema de las cuerdas equidistantes)
**Equidistant chords theorem**: in a given circle, if two chords are equidistant from the center, then the two chords are congruent.
[Equidistant chords theorem image code](Programs/S09/14_Equidistant_chords_theorem_image.py)
![Equidistant chords theorem image](Images/S09/14_Equidistant_chords_theorem.png)
*Equidistant chords theorem*

> Proof of the equidistant chords theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with a chord $\overline{BC}$ having its shortest distance to $A$ being $\overline{AD}$, and a chord $\overline{EF}$ having its shortest distance to $A$ being $\overline{AG}$, such that $\overline{AD} \cong \overline{AG}$ | Given |
> | $\overline{AB} \cong \overline{AC} \cong \overline{AE} \cong \overline{AF}$ | Definition of radius |
> | $\overline{AD} \cong \overline{AD}$ and $\overline{AG} \cong \overline{AG}$ | Reflexive property of congruence |
> | $\triangle ABD \cong \triangle ACD \cong \triangle AEG \cong \triangle AFG$ | Hypotenuse-leg congruence theorem |
> | $\overline{BD} \cong \overline{CD} \cong \overline{EG} \cong \overline{FG}$ | Corresponding parts of congruent triangles are congruent |
> | $BD = CD = EG = FG$ | Definition of congruence |
> | $BC = BD + CD = EF = EG + FG$ | Segment addition postulate |
> | $\overline{BC} \cong \overline{EF}$ | Definition of congruence |

In a circle $\bigodot A$ with a chord $\overline{BC}$ having its shortest distance to $A$ being $\overline{AD}$, and a chord $\overline{EF}$ having its shortest distance to $A$ being $\overline{AG}$, if $\overline{AD} \cong \overline{AG}$, then $\overline{BC} \cong \overline{EF}$.

(Converso del teorema de las cuerdas equidistantes)
**Converse of the equidistant chords theorem**: in a given circle, if two chords are congruent, then they are equidistant from the center.

> Proof of the converse of the equidistant chords theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | The circle $\bigodot A$ exists, with a chord $\overline{BC}$ having its shortest distance to $A$ being $\overline{AD}$, and a chord $\overline{EF}$ having its shortest distance to $A$ being $\overline{AG}$, such that $\overline{BC} \cong \overline{EF}$ | Given, from the *Equidistant chords theorem* image |
> | $\overline{AB} \cong \overline{AC} \cong \overline{AE} \cong \overline{AF}$ | Definition of radius |
> | $\triangle ABC \cong \triangle AEF$ | SSS triangle congruence postulate |
> | $\overline{AD} \cong \overline{AG}$ | Corresponding parts of congruent triangles are congruent |

In a circle $\bigodot A$ with a chord $\overline{BC}$ having its shortest distance to $A$ being $\overline{AD}$, and a chord $\overline{EF}$ having its shortest distance to $A$ being $\overline{AG}$, if $\overline{BC} \cong \overline{EF}$, then $\overline{AD} \cong \overline{AG}$.

<!-- TODO lengths of chords, props of chords and arcs-->

## Inscribed angles (Ángulos inscritos)

## Angles of chords, secants, and tangents (Ángulos de cuerdas, secantes, y tangentes)

## Segments of chords, secants, and tangents (Segmentos de cuerdas, secantes, y tangentes)

## Writing and graphing the equations of circles (Escribir y graficar las ecuaciones de los círculos)