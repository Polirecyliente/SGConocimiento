
#   Basics of geometry (Bases de la geometría)

<!--
#T# Table of contents

#C# Points, lines, and planes (Puntos, líneas, y planos)
#C# Segments and distance (Segmentos y distancia)
#C# Angles and measurement (Ángulos y medición)
#C# Midpoints and bisectors (Puntos medios y bisectrices)
#C# Angle pairs (Pares de ángulos)
#C# Classifying polygons (Clasificación de polígonos)

#T# Beginning of content
-->

Attribution and License
![CK-12 Attribution](Images/CK-12_License.png)
Only the chapter name and the sections names are licensed under the CK-12 Curriculum Materials License, because they are copied from the 'Geometry' book by CK-12. The images and the rest of the plain text are licensed under the CC-BY license, the code is licensed under the MIT license (See README.md).

## Points, lines, and planes (Puntos, líneas, y planos)

Geometry (Geometría) means the study of figures and their spatial properties. Spatial refering to the space occupied by the figures, or their location with regards to one another.

(Figura)
**Figure**: a geometric object that occupies space.

(Diagrama)
**Diagram**: a picture or drawing used to show figures and their geometry.

(Forma de una figura)
**Shape of a figure**: the form of the figure.

(Tamaño de una figura)
**Size of a figure**: the amount of space occupied by the figure.

(Punto)
**Point**: a single piece of space that has no extension, i.e. a figure with zero dimensions. Points are used to indicate locations in space, they are represented with dots in diagrams.
[Points in space image code](Programs/S01/01_Points_in_space_image.py)
![Points in space image](Images/S01/01_Points_in_space.png)
*Points in space*

The points shown in the *Points in space* image, are in the shape of blue dots. These shapes have an extension, a size, they are two dimensional, and they must be, otherwise they would be invisible if they truly were zero dimensional. These dots represent points with no dimensions.

Points are commonly labeled using an uppercase letter. The image shown has four points, namely $A$, $B$, $C$, and $D$.

(Línea | Recta)
**Line**: a shape with infinite points that extends in a single dimension indefinitely. A line has no start nor ending, it has a given direction and a location in space.
[Line in space image code](Programs/S01/02_Line_in_space_image.py)
![Line in space image](Images/S01/02_Line_in_space.png)
*Line in space*

Lines are labeled using a single lowercase letter, such as $g$, or with the labels of two points on the line and a bidirectional arrow on top, such as $\overleftrightarrow{PQ}$ and $\overleftrightarrow{QP}$. All these three labels denote the same line.

(Plano)
**Plane**: a shape with infinite lines that extends in two dimensions (2D) indefinitely. A plane has no start nor ending, it has a given direction and a location in space.
![Planes in space image](Images/S01/03_Planes_in_space.png)
*Planes in space*

Planes are labeled using a single uppercase letter in a calligraphic font, such as $\mathcal{M}$. A plane can also be named with the labels of any three points on the plane, such as the plane $ABC$, or $BCA$, or $CAB$ or any other combination.

Planes extend indefinitely in two dimensions, the planes shown in the *Planes in space* image are only squares, but the planes they represent, extend beyond these squares. Any shape in two dimensions can be used to represent a plane.

(Espacio tridimensional)
**3D space**: space in which the basic geometric shapes exist. Shapes in zero, one, or two dimensions, can be seen in 3D space. This space has three dimensions, it extends indefinitely in width, length, and height.

(Puntos colineales)
**Collinear points**: points that are on the same line. All the points on a given line are collinear.

(Puntos coplanares)
**Coplanar points**: points that are on the same plane. All the points on a given plane are coplanar.

(Líneas coplanares)
**Coplanar lines**: lines that are on the same plane. All the lines on a given plane are coplanar.

(Segmento de línea)
**Line segment**: a truncated line that ends in both of its sides and does not extend indefinitely. The points where the line ends are called endpoints (puntos extremos).
[Line segment image code](Programs/S01/04_Line_segment_image.py)
![Line segment image](Images/S01/04_Line_segment.png)
*Line segment*

Line segments are labeled using its endpoints and a horizontal bar on top of them, such as $\overline{AB}$ and $\overline{BA}$. They can also be simply called segments.

(Rayo)
**Ray**: a line that is only truncated in one side, while the other side extends indefinitely. A ray has one endpoint.
[Ray image code](Programs/S01/05_Ray_image.py)
![Ray image](Images/S01/05_Ray.png)
*Ray*

Rays are labeled using the endpoint and the point inside the ray with an arrow on top, such as $\overrightarrow{AB}$ and $\overleftarrow{BA}$. The arrow on top points in the same direction as the ray.

(Intersección)
**Intersection**: the point or points where two shapes cross each other. When two distinct lines intersect, the intersection is a point. When two distinct planes intersect, the intersection is a line. When a line outside of a plane intersects said plane, the intersection is a point. When three distinct planes intersect, the intersection is a point.

(Postulado)
**Postulate**: the axioms of geometry, i.e. facts of geometry that are accepted as true. Postulates act as definitions.

(Teorema)
**Theorem**: a statement that can be proved with postulates, axioms and/or with other theorems.

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

## Segments and distance (Segmentos y distancia)

(Distancia)
**Distance**: the length between two given points.

(Medición de distancia)
**Measure of distance**: the process of determining the distance between two points. The ruler (la regla) is the basic instrument to measure distance. Rulers measure distance in units such as inches (pulgadas) and centimeters (centímetros).

> Distance notation
>
> Let $A$ and $B$ be two points, the segment that they form as endpoints is $\overline{AB}$, and the measure of the distance of this segment is denoted by $AB$ or $m \overline{AB}$.

> Method of distance measurement using a ruler
>
> 1. Make sure that the ruler can be fitted in the space between the two points whose distance is being measured.
> 2. Place the $0$ tick of the ruler in one of the points.
> 3. Place the ruler so that the ticks touch the second point.
> 4. Read the number of the tick nearest to the second point, this is the measure of the distance.

This method can be used to draw a given length.

(Postulado de la regla)
**Ruler postulate**: when placing a ruler to measure the distance between two given points, said distance is the absolute value of the difference of the numbers of each point in the ruler. The distance between two points $A$ and $B$ is $B_value - A_value$, the subindex $value$ indicates that it's a measure, in this case a measure of the ruler.

(Postulado de adición de segmentos)
**Segment addition postulate**: given three collinear points with one point being between the other two (the endpoints), the measure of the distance between the endpoints, is equal to the sum of the distances of each endpoint to the point between them.

> Segment addition postulate
>
> Let $A$, $B$, and $C$, be three collinear points, with $B$ being between $A$ and $C$, then
> $$AB + BC = AC$$

The segment addition postulate can be visualized with the following image.
[Segment addition postulate image code](Programs/S01/06_Segment_addition_postulate_image.py)
![Segment addition postulate image](Images/S01/06_Segment_addition_postulate.png)
*Segment addition postulate*

(Plano coordenado)
**Coordinate grid**: the two dimensional plane that uses tuples of two numbers, $x$ and $y$, to represent the location of points in the plane. The $x$ coordinate measures horizontal distance, and the $y$ coordinate measures vertical distance.

## Angles and measurement (Ángulos y medición)

Given two distinct rays that share their endpoint, the angle formed between the two rays is the measure of the rotation needed to get from one ray to the other.

> Angle notation
>
> Let $A$, $B$, and $C$, be three points, such that they form two distinct rays, $\overrightarrow{BA}$ and $\overrightarrow{BC}$, then the angle that these rays form is denoted as $\angle ABC$ or $\angle CBA$ or $\angle B$ if no more than one angle stems from $B$.

[Angle from two rays image code](Programs/S01/07_Angle_from_two_rays_image.py)
![Angle from two rays image](Images/S01/07_Angle_from_two_rays.png)
*Angle from two rays*

Angles are commonly shown in diagrams with an arc between the two rays. In the *Angle from two rays* image, the angle $\angle B$ is $\theta$.

(Vértice de un ángulo)
**Vertex of an angle**: in an angle, the vertex is the endpoint where the two rays join. In the angle $\angle ABC$, the vertex is the point $B$.

(Lados de un ángulo)
**Sides of an angle**: each of the two rays that form the angle.

(Transportador)
**Protractor**: instrument to measure angles. The most common units of measure are degrees and radians. Degrees denote a rotation of a full circle as $360 \text{\textdegree}$, and in radians this is denoted as $2 \pi$.

An angle can be measured in two ways, because there are two ways in which a ray can be rotated to coincide with another (rotating the ray clockwise, and rotating the ray counterclockwise). The standard definition of the measure of an angle, is that it's the smallest measure of the two. The smallest measure of an angle is always less than or equal to half a circle, i.e. $180 \text{\textdegree}$ or $\pi$ radians.

> Angle measure notation
>
> Let $A$, $B$, $C$, be three points that form an angle with vertex $B$, then the angle $\angle ABC$ has a measure denoted as $m \angle ABC$, or also $m \angle B$.

> Method of angle measurement using a protractor
>
> 1. Place the vertex of the protractor on top of the vertex of the rays whose angle is being measured.
> 2. Make sure that both rays extend beyond the protractor.
> 3. Rotate the protractor around its vertex so that the $0$ tick is aligned with one of the rays. The other ray must be under the protractor, otherwise put the $0$ tick under the other ray.
> 4. Read the number of the tick nearest to the other ray, this is the measure of the angle.

This method can be used to draw a given angle.

(Postulado del transportador)
**Protractor postulate**: when placing a protractor to measure the angle between two rays, said angle is the absolute value of the difference of the numbers of each ray in the protractor. The measure of the angle $\angle ABC$ is $BC_value - AB_value$, the subindex $value$ indicates that it's a measure, in this case a measure of the protractor at the segments $\overline{AB}$ and $\overline{BC}$.

(Vuelta completa)
**Full circle**: the angle measure of $2 \pi$ radians or $360 \text{\textdegree}$.

(Ángulo llano)
**Straight angle**: the angle of half a circle, i.e. $180 \text{\textdegree}$ or $\pi$ radians. Two rays that have this angle form a straight line.

(Rayos opuestos)
**Opposite rays**: two rays with a straight angle between them.

(Ángulo recto)
**Right angle**: the angle of a quarter of a circle, i.e. $90 \text{\textdegree}$ or $\pi/2$ radians. The arc between the rays that is used to denote a right angle is a small square instead of an arc.

(Ángulo agudo)
**Acute angle**: an angle greater than or equal to $0 \text{\textdegree}$ ($0$ radians) and less than $90 \text{\textdegree}$ ($\pi/2$ radians).

(Ángulo obtuso)
**Obtuse angle**: an angle greater than $90 \text{\textdegree}$ ($\pi/2$ radians) and less than $180 \text{\textdegree}$ ($\pi$ radians).

(Líneas perpendiculares)
**Perpendicular lines**: two lines (or rays, or segments) that cross each other at right angles, i.e. the four angles formed at the intersection of the lines are right angles.
[Perpendicular lines image code](Programs/S01/08_Perpendicular_lines_image.py)
![Perpendicular lines image](Images/S01/08_Perpendicular_lines.png)
*Perpendicular lines*

Perpendicularity is denoted with the $\perp$ symbol. From the *Perpendicular lines* image, the lines $l$ and $m$ are perpendicular to each other, so $l \perp m$, which is the same as $m \perp l$, or $\overleftrightarrow{BC} \perp \overleftrightarrow{DE}$.

(Regla no graduada)
**Straightedge**: an instrument used to make straight lines, like a ruler but without tick marks.

(Compás)
**Compass**: an instrument used to draw arcs.

(Centrar el compás en un punto dado)
**Center the compass on a given point**: put the needle of the compass in the given point.

(Construcciones geométricas)
**Geometric constructions**: a drawing made with straightedge and compass, commonly with the intention to follow given steps in the use of said instruments, to obtain a given geometric shape.

(Construcción para copiar un ángulo)
**Copy an angle construction**: it's possible to copy an angle by doing a construction.

> Method to copy an angle using a straightedge and a compass
>
> This method assumes both angles are being depicted in paper or in a similar way.
> 1. Choose which is the first ray and which the second ray in the angle being copied.
> 2. Make a copy of the first ray with the straightedge.
> 3. Center the compass on the vertex of the angle being copied, draw an arc at any radius such that the arc passes over both rays. Repeat this arc in the copied ray from step 2.
> 4. Center the compass in the angle being copied at the intersection of the arc from step 3 and the first ray. Open (or close) the compass to draw an arc that passes through the intersection of the arc from step 3 and the second ray. Repeat this arc in the copied ray from step 2.
> 5. Draw a line with the straightedge in the new copy of the angle, that passes through its vertex and the intersection of the two arcs that should have formed from the previous steps, the resulting angle is a copy of the first one.

(Marcas de los ángulos)
**Angle markings**: angles can be marked to differentiate between them. Angles are marked with arc marks (marcas del ángulo). Arc marks are commonly of two types: several repeated arcs, or arcs with small perpendicular lines crossing them.
[Angle markings image code](Programs/S01/09_Angle_markings_image.py)
![Angle markings image](Images/S01/09_Angle_markings.png)
*Angle markings*

(Marcas de los segmentos)
**Segment markings**: segments can be marked to differentiate between them. Segments are marked with hash marks (marcas del segmento). Hash marks are commonly repeated small lines perpendicular to the segment, placed around the center of the segment.
[Segment markings image code](Programs/S01/10_Segment_markings_image.py)
![Segment markings image](Images/S01/10_Segment_markings.png)
*Segment markings*

In the *Segment markings* image, the two segments at the bottom have the same length, as shown by their equal markings. The rest of the segments are different from each other, so each one has it's unique marking.

(Postulado de adición de ángulos)
**Angle addition postulate**: given two angles that share a common ray and they cover distinct space, the measure of the angle between the two non common rays, is equal to the sum of the two angles given.

> Angle addition postulate
>
> Let $\overrightarrow{AD}$, $\overrightarrow{BD}$, and $\overrightarrow{CD}$, be three rays such that two angles are formed that share the common ray $\overrightarrow{BD}$, i.e. the angles $\angle ADB$ and $\angle CDB$, then
> $$m \angle ADB + m \angle CDB = m \angle ADC$$

[Angle addition postulate image code](Programs/S01/11_Angle_addition_postulate_image.py)
![Angle addition postulate image](Images/S01/11_Angle_addition_postulate.png)
*Angle addition postulate*

## Midpoints and bisectors (Puntos medios y bisectrices)

(Congruencia)
**Congruence**: when two geometric figures have the same shape and size, e.g. two segments with the same length, two angles with the same measure, two triangles with the same shape and size.

> Congruence notation
>
> Let $\overline{AB}$ be a segment, the congruence with itself is denoted as
> $$\overline{AB} \cong \overline{BA}$$
> This symbol $\cong$ is used in general to indicate two congruent geometric figures.

(Punto medio)
**Midpoint**: the point on a segment, that divides it into two congruent segments.
[Midpoint image code](Programs/S01/12_Midpoint_image.py)
![Midpoint image](Images/S01/12_Midpoint.png)
*Midpoint*

As shown in the *Midpoint* image, the lengths $AB$ and $BC$ are equal, i.e. $AB = BC$, so the point $B$ is the midpoint of the segment $\overline{AC}$.

(Postulado del punto medio)
**Midpoint postulate**: a segment has exactly one midpoint. If the point $B$ is the midpoint of $\overline{AC}$, then $B$ is the only point that is the midpoint.

(Fórmula del punto medio)
**Midpoint formula**: a formula to calculate the midpoint from two points, which can be the endpoints of a segment.

> Midpoint formula
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points in the $x$-$y$ plane, then the midpoint of the segment they form is
> $$\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

This formula can be derived from a more general formula
[Divide segment formula code](Programs/S01/13_Divide_segment_formula.py)

> General formula to divide a segment into $n$ subsegments and get the location of the $k$-th subsegment
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be the two points that define a segment, this segment can be divided into $n$ subsegments. Counting from $(x_1, y_1)$, the coordinates of the $k$-th subsegment are
> $$\left(x_1 + k\frac{x_2 - x_1}{n}, y_1 + k\frac{y_2 - y_1}{n}\right)$$

Making $k = 1$ and $n = 2$ results in the midpoint formula.

(Bisectriz de un segmento)
**Segment bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in any angle.
[Segment bisector image code](Programs/S01/14_Segment_bisector_image.py)
![Segment bisector image](Images/S01/14_Segment_bisector.png)
*Segment bisector*

(Mediatriz)
**Perpendicular bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in a perpendicular way.
[Perpendicular bisector image code](Programs/S01/15_Perpendicular_bisector_image.py)
![Perpendicular bisector image](Images/S01/15_Perpendicular_bisector.png)
*Perpendicular bisector*

(Postulado de la mediatriz)
**Perpendicular bisector postulate**: a given segment has only one line that is its perpendicular bisector.

There are infinitely many segment bisectors and only one perpendicular bisector to a given segment. As shown in the *Perpendicular bisector* image, $\overleftrightarrow{DE} \perp \overline{AC}$, and $\overline{AB} \cong \overline{BC}$, so the line $\overleftrightarrow{DE}$ is the perpendicular bisector of $\overline{AC}$.

(Construcción de la mediatriz)
**Perpendicular bisector construction**: a geometric construction to draw the perpendicular bisector of a given segment.

> Perpendicular bisector construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials).
> 1. Draw the segment whose perpendicular bisector will be constructed, with space around it.
> 2. Center the compass on one of the endpoints of the segment from step 1, with a radius greater than half the length of the segment. Draw arcs above and below the segment. Repeat this step with the other endpoing of the segment, ensuring that the arcs above and below intercept, and being careful to not change the radius of the compass.
> 3. Draw a line that passes through both arc interceptions above and below the segment, this line bisects the segment perpendicularly.
>
> This construction works as long as the radius of the compass is the same on both endpoints, because this would create two circles of equal radii, and the line that passes through their arc interceptions must be at equal distance from both centers, which is the midpoint of the segment between the centers.
>
> If one radius is smaller, this can serve to create lines that cross the segment at other fractions different from one half the lenght of the segment.

(Bisectriz de un ángulo)
**Angle bisector**: a line, ray, or segment, that divides a given angle into two congruent angles, each with half the measure of the given angle.
[Angle bisector image code](Programs/S01/16_Angle_bisector_image.py)
![Angle bisector image](Images/S01/16_Angle_bisector.png)
*Angle bisector*

The segment $\overline{AC}$ is the angle bisector of the angle $\angle DAB$, so $m \angle DAC = m \angle BAC$.

(Postulado de la bisectriz de un ángulo)
**Angle bisector postulate**: a given angle has only one line that is its angle bisector.

In the *Angle bisector* image, if the segment $\overline{AC}$ is converted into a line, then the line $\overleftrightarrow{AC}$ is the angle bisector of the angle $\angle DAB$. The angle bisector does not have to be a line, but if it's a line then it's guaranteed to be the only one that is the angle bisector.

(Construcción de la bisectriz de un ángulo)
**Angle bisector construction**: a geometric construction to draw the angle bisector of a given angle.

> Angle bisector construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials).
> 1. Draw the angle whose bisector will be constructed, with space around it.
> 2. Center the compass on the vertex of the angle, draw an arc at any radius such that it crosses both sides of the angle.
> 3. Apply the perpendicular bisector construction, taking as endpoints the intersections of the arc with the sides of the angle.
> 4. Extend the line of the perpendicular bisector construction made in step 3 until it crosses the vertex of the angle, this line is the angle bisector.

## Angle pairs (Pares de ángulos)

(Ángulos complementarios)
**Complementary angles**: two angles whose measures when added together add up to $90 \text{\textdegree}$ or $\pi/2$ radians. Each angle is the complement (complemento) of the other.

(Ángulos suplementarios)
**Supplementary angles**: two angles whose measures when added together add up to $180 \text{\textdegree}$ or $\pi$ radians. Each angle is the supplement (suplemento) of the other.

(Ángulos adyacentes)
**Adjacent angles**: two angles that have the same vertex and share one side, without overlapping each other, which means that only three rays are required to create two adjacent angles.

(Par lineal)
**Linear pair**: two adjacent angles such that the two non-shared sides form a straight line.

(Postulado del par lineal)
**Linear pair postulate**: the two angles of a linear pair are supplementary. If $\angle A$ and $\angle B$ form a linear pair, then $\angle A$ and $\angle B$ are supplementary.

(Ángulos verticales)
**Vertical angles**: in the intersection of two lines, vertical angles are pairs of angles that are on opposite sides of the intersection.
[Vertical angles image code](Programs/S01/17_Vertical_angles_image.py)
![Vertical angles image](Images/S01/17_Vertical_angles.png)
*Vertical angles*

As shown in the *Vertical angles* image, the angles $\alpha_1$ and $\alpha_2$ are vertical angles, and also the angles $\beta_1$ and $\beta_2$ are vertical angles. Each of these pairs have their angles located in opposite sides of the intersection of the lines.

(Teorema de los ángulos verticales)
**Vertical angles theorem**: two angles that are vertical angles, are also congruent.

> Proof of the vertical angles theorem
>
> Using the *Vertical angles* image, the angles $\alpha_1$ and $\beta_1$ form a linear pair, as do the angles $\alpha_2$ and $\beta_1$. This means that the measures of the angles $\alpha_1$ and $\alpha_2$ must be the same, and so $\alpha_1 \cong \alpha_2$.
>
> On the other hand, the angles $\alpha_1$ and $\beta_2$ form a linear pair, as do the angles $\alpha_1$ and $\beta_1$, which means that also $\beta_1 \cong \beta_2$. $\blacksquare$

The black square $\blacksquare$ means that the proof of the theorem is finished.

If $\angle A$ and $\angle B$ are vertical angles, then $\angle A \cong \angle B$.

## Classifying polygons (Clasificación de polígonos)

(Triángulo)
**Triangle**: a shape formed with three segments in which each segment is connected to the other two with their endpoints.
[Triangle image code](Programs/S01/18_Triangle_image.py)
![Triangle image](Images/S01/18_Triangle.png)
*Triangle*

The triangle in the image can be denoted as $\triangle ABC$ or $\triangle BCA$ or using any other order of the points of the triangle.

(Clasificación de triángulos según sus ángulos)
**Classification of triangles based on angles**:

- **Right triangle** (Triángulo rectángulo): a triangle that has one right angle.
[Right triangle image code](Programs/S01/19_Right_triangle_image.py)
![Right triangle image](Images/S01/19_Right_triangle.png)
*Right triangle*

- **Obtuse triangle** (Triángulo obtuso): a triangle that has one obtuse angle.
[Obtuse triangle image code](Programs/S01/20_Obtuse_triangle_image.py)
![Obtuse triangle image](Images/S01/20_Obtuse_triangle.png)
*Obtuse triangle*

- **Acute triangle** (Triángulo agudo): a triangle whose three angles are acute.
[Acute triangle image code](Programs/S01/21_Acute_triangle_image.py)
![Acute triangle image](Images/S01/21_Acute_triangle.png)
*Acute triangle*

- **Equiangular triangle** (Triángulo equiángulo): a triangle whose three angles are congruent.
[Equiangular triangle image code](Programs/S01/22_Equiangular_triangle_image.py)
![Equiangular triangle image](Images/S01/22_Equiangular_triangle.png)
*Equiangular triangle*

(Clasificación de triángulos según sus lados)
**Classification of triangles based on sides**:

- **Scalene triangle** (Triángulo escaleno): a triangle whose three sides have different lengths from each other.
[Scalene triangle image code](Programs/S01/23_Scalene_triangle_image.py)
![Scalene triangle image](Images/S01/23_Scalene_triangle.png)
*Scalene triangle*

- **Isosceles triangle** (Triángulo isósceles): a triangle with two sides of equal length.
[Isosceles triangle image code](Programs/S01/24_Isosceles_triangle_image.py)
![Isosceles triangle image](Images/S01/24_Isosceles_triangle.png)
*Isosceles triangle*

- **Equilateral triangle** (Triángulo equilátero): a triangle whose three sides have equal length. An equilateral triangle is also isosceles.
[Equilateral triangle image code](Programs/S01/25_Equilateral_triangle_image.py)
![Equilateral triangle image](Images/S01/25_Equilateral_triangle.png)
*Equilateral triangle*

(Polígono)
**Polygon**: any geometric figure made with segments joined by their endpoints. Each of the endpoints of the segments in a polygon must be intersecting the endpoint of another segment.

(Lados de un polígono)
**Sides of a polygon**: the segments of the polygon.

(Vértices de un polígono)
**Vertices of a polygon**: the points of a polygon where the segments intersect.

(Polígono convexo)
**Convex polygon**: a polygon such that in each of its vertices, the angle measured inside the polygon is less than the angle measured outside the polygon.
[Convex polygon image code](Programs/S01/26_Convex_polygon_image.py)
![Convex polygon image](Images/S01/26_Convex_polygon.png)
*Convex polygon*

(Polígono cóncavo)
**Concave polygon**: a polygon such that in at least one of its vertices, the angle measured inside the polygon is greater than the angle measured outside the polygon.
[Concave polygon image code](Programs/S01/27_Concave_polygon_image.py)
![Concave polygon image](Images/S01/27_Concave_polygon.png)
*Concave polygon*

In the image, the marked angle has a measure greater than the measure of the angle from that same vertex but outside the polygon, this makes the polygon to be concave.

(Diagonales de un polígono)
**Polygon diagonals**: the segments that are formed by connecting all the vertices of the polygon with each other, but that are not the sides of the polygon.
[Polygon diagonals image code](Programs/S01/28_Polygon_diagonals_image.py)
![Polygon diagonals image](Images/S01/28_Polygon_diagonals.png)
*Polygon diagonals*

The blue lines in the image are the diagonals of the polygon.

(Clasificación de polígonos según el número de lados)
**Classification of polygons based on the number of sides**:

- **Triangle** (Triángulo): a polygon with three sides.
- **Quadrilateral** (Cuadrilátero): a polygon with four sides.
- **Pentagon** (Pentágono): a polygon with five sides.
- **Hexagon** (Hexágono): a polygon with six sides.
- **Heptagon** (Heptágono): a polygon with seven sides.
- **Octagon** (Octágono): a polygon with eight sides.
- **Nonagon** (Nonágono): a polygon with nine sides.
- **Decagon** (Decágono): a polygon with ten sides.
- **Undecagon** (Undecágono): a polygon with eleven sides.
- **Dodecagon** (Dodecágono): a polygon with twelve sides.