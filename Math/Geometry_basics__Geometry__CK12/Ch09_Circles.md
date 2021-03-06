
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
[Ch09_S01](https://www.ck12.org/reader/reader-index.html#section/2932980/9.1/9549314)

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
[Segments and lines of a circle image code](Programs/Ch09/S01_01_Segments_and_lines_of_a_circle_image.py)
![Segments and lines of a circle image](Images/Ch09/S01_01_Segments_and_lines_of_a_circle.png)
*Segments and lines of a circle*

(Relaciones entre círculos)
**Relationships between circles**: two given circles can relate to each other. A few ways to relate them are, by their intersection, by their relative position, and by their radii.

(Dos círculos con dos puntos de intersección)
**Two circles with two points of intersection**: two circles can intersect each other at a maximum of two points.
[Two circles with two points of intersection image code](Programs/Ch09/S01_02_Two_circles_with_two_points_of_intersection_image.py)
![Two circles with two points of intersection image](Images/Ch09/S01_02_Two_circles_with_two_points_of_intersection.png)
*Two circles with two points of intersection*

(Dos círculos tangentes)
**Two tangent circles**: two circles can intersect each other in a single point, when they are tangent to each other.
[Two tangent circles image code](Programs/Ch09/S01_03_Two_tangent_circles_image.py)
![Two tangent circles image](Images/Ch09/S01_03_Two_tangent_circles.png)
*Two tangent circles*

(Dos círculos concéntricos)
**Two concentric circles**: two circles with distinct radii and the same center point.
[Two concentric circles image code](Programs/Ch09/S01_04_Two_concentric_circles_image.py)
![Two concentric circles image](Images/Ch09/S01_04_Two_concentric_circles.png)
*Two concentric circles*

(Círculos congruentes)
**Congruent circles**: in a given set of circles, they are congruent if their radii have the same length. In circles $\bigodot A$ and $\bigodot B$, where $r_A$ is the radius of $\bigodot A$ and $r_B$ is the radius of $\bigodot B$, if $r_A = r_B$, then $\bigodot A \cong \bigodot B$.

(Línea tangente)
**Tangent line**: a line that passes through a single point of a curve. It can also be a ray or a segment.

(Tangencia interna de dos círculos)
**Internal tangency of two circles**: two tangent circles are internally tangent when one is inside the other.
[Internal tangency of two circles image code](Programs/Ch09/S01_05_Internal_tangency_of_two_circles_image.py)
![Internal tangency of two circles image](Images/Ch09/S01_05_Internal_tangency_of_two_circles.png)
*Internal tangency of two circles*

If two circles are internally tangent, with the tangent line being $\overleftrightarrow{AB}$, then both circles are on the same side of the line $\overleftrightarrow{AB}$.

(Tangencia externa de dos círculos)
**External tangency of two circles**: two tangent circles are externally tangent when they are on different sides of their tangent line.
[External tangency of two circles image code](Programs/Ch09/S01_06_External_tangency_of_two_circles_image.py)
![External tangency of two circles image](Images/Ch09/S01_06_External_tangency_of_two_circles.png)
*External tangency of two circles*

If two circles are externally tangent, with the tangent line being $\overleftrightarrow{AB}$, then each circle is on a different side of the line $\overleftrightarrow{AB}$.

(Tangente interior común)
**Common internal tangent**: in two circles that are not tangent to each other, two tangent lines can be built that are common internal tangents. A common internal tangent, is a line or segment that is tangent to each of the two circles, and it intersects the segment that joins the two centers of the circles.
[Common internal tangent image code](Programs/Ch09/S01_07_Common_internal_tangent_image.py)
![Common internal tangent image](Images/Ch09/S01_07_Common_internal_tangent.png)
*Common internal tangent*

In two circles $\bigodot A$ and $\bigodot B$, if the two common internal tangents are $\overline{C_1D_1}$ and $\overline{C_2D_2}$, then those two segments intersect $\overline{AB}$.

(Tangente exterior común)
**Common external tangent**: in two circles that are not tangent to each other, two tangent lines can be built that are common external tangents. A common external tangents, is a line or segment that is tangent to each of the two circles, and does not intersect the segment that joins the two centers of the circles.
[Common external tangent image code](Programs/Ch09/S01_08_Common_external_tangent_image.py)
![Common external tangent image](Images/Ch09/S01_08_Common_external_tangent.png)
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
[Two tangents theorem image code](Programs/Ch09/S01_09_Two_tangents_theorem_image.py)
![Two tangents theorem image](Images/Ch09/S01_09_Two_tangents_theorem.png)
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
[Ch09_S02](https://www.ck12.org/reader/reader-index.html#section/2932981/9.2/9549314)

## Properties of chords (Propiedades de las cuerdas)
[Ch09_S03](https://www.ck12.org/reader/reader-index.html#section/2932982/9.3/9549314)

## Inscribed angles (Ángulos inscritos)
[Ch09_S04](https://www.ck12.org/reader/reader-index.html#section/2932983/9.4/9549314)

## Angles of chords, secants, and tangents (Ángulos de cuerdas, secantes, y tangentes)
[Ch09_S05](https://www.ck12.org/reader/reader-index.html#section/2932984/9.5/9549314)

## Segments of chords, secants, and tangents (Segmentos de cuerdas, secantes, y tangentes)
[Ch09_S06](https://www.ck12.org/reader/reader-index.html#section/2932985/9.6/9549314)

## Writing and graphing the equations of circles (Escribir y graficar las ecuaciones de los círculos)
[Ch09_S07](https://www.ck12.org/reader/reader-index.html#section/2932986/9.7/9549314)