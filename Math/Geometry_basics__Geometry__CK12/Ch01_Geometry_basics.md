
#   Geometry basics (Bases de la geometría)

## Points, lines, and planes (Puntos, líneas, y planos)
[Ch01_S01](https://www.ck12.org/reader/reader-index.html#section/2932917/1.1/9549314)

Geometry (Geometría) means the study of shapes and their spatial properties. Spatial refering to the space occupied by the shapes, or their location with regards to one another.

(Diagrama)
**Diagram**: a picture or drawing used to show shapes and their geometry.

(Punto)
**Point**: a single piece of space that has no extension, i.e. a shape with zero dimensions. Points are used to indicate locations in space, they are represented with dots in diagrams.
[Points in space image code](Programs/Ch01/S01_01_Points_in_space_image.py)
![Points in space image](Images/Ch01/S01_01_Points_in_space.png)
*Points in space*

The points shown in the *Points in space* image, are in the shape of blue dots. These shapes have an extension, a size, they are two dimensional, and they must be, otherwise they would be invisible if they truly were zero dimensional. These dots represent points with no dimensions.

Points are commonly labeled using an uppercase letter. The image shown has four points, namely $A$, $B$, $C$, and $D$.

(Línea|Recta)
**Line**: a shape with infinite points that extends in a single dimension indefinitely. A line has no start nor ending, it has a given direction and a location in space.
[Line in space image code](Programs/Ch01/S01_02_Line_in_space_image.py)
![Line in space image](Images/Ch01/S01_02_Line_in_space.png)
*Line in space*

Lines are labeled using a single lowercase letter, such as $g$, or with the labels of two points and a bidirectional arrow on top, such as $\overleftrightarrow{PQ}$ and $\overleftrightarrow{QP}$. All these three labels denote the same line.

(Plano)
**Plane**: a shape with infinite lines that extends in two dimensions indefinitely. A plane has no start nor ending, it has a given direction and a location in space.
![Planes in space image](Images/Ch01/S01_03_Planes_in_space.png)
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
[Line segment image code](Programs/Ch01/S01_04_Line_segment_image.py)
![Line segment image](Images/Ch01/S01_04_Line_segment.png)
*Line segment*

Line segments are labeled using its endpoints and a horizontal bar on top of them, such as $\overline{AB}$ and $\overline{BA}$.

(Rayo)
**Ray**: a line that is only truncated in one side, while the other side extends indefinitely. A ray has one endpoint.
[Ray image code](Programs/Ch01/S01_05_Ray_image.py)
![Ray image](Images/Ch01/S01_05_Ray.png)
*Ray*

Rays are labeled using the endpoint and the point inside the ray with an arrow on top, such as $\overrightarrow{AB}$ and $\overleftarrow{BA}$. The arrow on top points in the same direction as the ray.

(Intersección)
**Intersection**: the point or points where two shapes cross each other. When two distinct lines intersect, the intersection is a point. When two distinct planes intersect, the intersection is a line. When a line outside of a plane intersects said plane, the intersection is a point. When three distinct planes intersect, the intersection is a point.

(Postulado)
**Postulate**: the axioms of geometry, i.e. facts of geometry that are accepted as true. Postulates act as definitions.

(Teorema)
**Theorem**: a statement that can be proved with postulates and/or with other theorems.

(Postulado de línea)
**Unique line postulate**: given two points, only one line passes through the points.

(Postulado de plano)
**Unique plane postulate**: given three non-collinear points, only one plane contains them.

(Postulado de plano línea)
**Plane-line postulate**: a line that connects points from a plane, is in the plane. 

(Postulado de la intersección entre dos rectas)
**Line intersection postulate**: if two distinct lines intersect, then their intersection is a point.

(Postulado de la intersección entre dos planos)
**Plane intersection postulate**: if two distinct planes intersect, then their intersection is a line.

## Segments and distance (Segmentos y distancia)
[Ch01_S02](https://www.ck12.org/reader/reader-index.html#section/2932918/1.2/9549314)

(Distancia)
**Distance**: the length between two given points.

(Medición de distancia)
**Measure of distance**: the process of determining the distance between two points. The ruler (la regla) is the basic instrument to measure distance. Rulers measure distance in units such as inches (pulgadas) and centimeters (centímetros).

> Distance notation
>
> Let $A$ and $B$ be two points, the segment that they form as endpoints is $\overline{AB}$, and the measure of the distance of this segment is denoted by $AB$ or $m\overline{AB}$.

> Method of distance measurement using a ruler
>
> 1. Make sure that the ruler can be fitted in the space between the two points whose distance is being measured.
> 2. Place the $0$ tick of the ruler in one of the points.
> 3. Place the ruler so that the ticks touch the second point.
> 4. Read the number of the tick nearest to the second point, this is the measure of the distance.

This method can be used to draw a given length.

(Postulado de la regla)
**Ruler postulate**: when placing a ruler to measure the distance between two given points, said distance is the absolute value of the difference of the numbers of each point in the ruler.

(Postulado de adición de segmentos)
**Segment addition postulate**: given three collinear points with one point being between the other two (the endpoints), the measure of the distance between the endpoints, is equal to the sum of the distances of each endpoint to the point between them.

> Segment addition postulate
>
> Let $A$, $B$, and $C$, be three collinear points, with $B$ being between $A$ and $C$, then
> $$AB + BC = AC$$

[Segment addition postulate image code](Programs/Ch01/S02_01_Segment_addition_postulate_image.py)
![Segment addition postulate image](Images/Ch01/S02_01_Segment_addition_postulate.png)
*Segment addition postulate*

(Plano coordenado)
**Coordinate grid**: the two dimensional plane that uses tuples of two numbers, $x$ and $y$, to represent the location of points in the plane. The $x$ coordinate measures horizontal distance, and the $y$ coordinate measures vertical distance.

## Angles (Ángulos)
[Ch01_S03](https://www.ck12.org/reader/reader-index.html#section/2932919/1.3/9549314)

Given two distinct rays that share their endpoint, the angle formed between the two rays is the measure of the rotation needed to get from one ray to the other.

> Angle notation
>
> Let $A$, $B$, and $C$, be three points, such that they form two distinct rays, $\overrightarrow{BA}$ and $\overrightarrow{BC}$, then the angle that these rays form is denoted as $\angle ABC$ or $\angle CBA$ or $\angle B$, letting $B$ as the point in the middle or the only one to denote the angle.

[Angle from two rays image code](Programs/Ch01/S03_01_Angle_from_two_rays_image.py)
![Angle from two rays image](Images/Ch01/S03_01_Angle_from_two_rays.png)
*Angle from two rays*

Angles are commonly shown in diagrams with an arc between the two rays. In the *Angle from two rays* image, the angle $\angle B$ is $\theta$.

(Vértice)
**Vertex**: in an angle, the vertex is the endpoint where the two rays join. In the angle $\angle ABC$, the vertex is the point $B$.

(Lados)
**Sides**: in an angle, the sides are each of the rays that form the angle.

(Transportador)
**Protractor**: instrument to measure angles. The most common units of measure are degrees and radians. Degrees denote a rotation of a full circle as $360 \degree$, and in radians this is denoted as $2 \pi$.

An angle can be measured in two ways, because there are two ways in which a ray can be rotated to coincide with another. The standard definition of the measure of an angle, is that it's the smallest measure of the two. The smallest measure of an angle is always less than or equal to half a circle, i.e. $180 \degree$ or $\pi$ radians.

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
**Protractor postulate**: when placing a protractor to measure the angle between two rays, said angle is the absolute value of the difference of the numbers of each ray in the protractor.

(Ángulo llano)
**Straight angle**: the angle of half a circle, i.e. $180 \degree$ or $\pi$ radians. Two rays that have this angle form a straight line. 

(Rayos opuestos)
**Opposite rays**: two rays with a straight angle between them.

(Ángulo recto)
**Right angle**: the angle of a quarter of a circle, i.e. $90 \degree$ or $\pi/2$ radians. The arc between the rays that is used to denote a right angle is a small square instead of an arc.

(Ángulo agudo)
**Acute angle**: an angle greater than or equal to $0 \degree$ ($0$ radians) and less than $90 \degree$ ($\pi/2$ radians).

(Ángulo obtuso)
**Obtuse angle**: an angle greater than $90 \degree$ ($\pi/2$ radians) and less than $180 \degree$ ($\pi$ radians).

(Líneas perpendiculares)
**Perpendicular lines**: two lines (or rays, or segments) that cross each other at right angles, i.e. the angles formed at the intersection of the lines are right angles.
[Perpendicular lines image code](Programs/Ch01/S03_02_Perpendicular_lines_image.py)
![Perpendicular lines image](Images/Ch01/S03_02_Perpendicular_lines.png)
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

(Copiar un ángulo)
**Copy an angle**: it's possible to copy an angle by doing a construction.

> Method to copy an angle using a straightedge and a compass
>
> This method assumes both angles are being depicted in paper or in a similar way.
> 1. Choose which is the first ray and which the second ray in the angle being copied.
> 2. Make a copy of the first ray with the straightedge.
> 3. Center the compass on the vertex of the angle being copied, draw an arc at any radius such that the arc passes over both rays. Repeat this arc in the copied ray from step 2.
> 4. Center the compass in the angle being copied at the intersection of the arc from step 3 and the first ray. Open (or close) the compass to draw an arc that passes through the intersection of the arc from step 3 and the second ray. Repeat this arc in the copied ray from step 2.
> 5. Draw a line with the straightedge in the new copy of the angle, that passes through its vertex and the intersection of the two arcs that should have formed from the previous steps, the resulting angle is a copy of the first one.

(Marcas de los ángulos)
**Angle markings**: angles can be marked to differentiate between them. Angles are marked with arc marks (marcas del ángulo). Arc marks are commonly of two types: several repeated arcs, or these arcs with small perpendicular lines crossing them.
[Angle markings image code](Programs/Ch01/S03_03_Angle_markings_image.py)
![Angle markings image](Images/Ch01/S03_03_Angle_markings.png)
*Angle markings*

(Marcas de los segmentos)
**Segment markings**: segments can be marked to differentiate between them. Segments are marked with hash marks (marcas del segmento). Hash marks are commonly repeated small lines perpendicular to the segment, placed around the center of the segment.
[Segment markings image code](Programs/Ch01/S03_04_Segment_markings_image.py)
![Segment markings image](Images/Ch01/S03_04_Segment_markings.png)
*Segment markings*

In the *Segment markings* image, the two segments at the bottom have the same length, as shown by their equal markings. The rest of the segments are different from each other, so each one has it's unique marking.

(Postulado de adición de ángulos)
**Angle addition postulate**: given two angles that share a common ray, the measure of the angle between the two non common rays, is equal to the sum of the two angles given.

> Angle addition postulate
>
> Let $\overrightarrow{DA}$, $\overrightarrow{DB}$, and $\overrightarrow{DC}$, be three rays such that two angles are formed that share the common ray $\overrightarrow{DB}$, i.e. the angles $\angle ADB$ and $\angle CDB$, then
> $$m \angle ADB + m \angle CDB = m \angle ADC$$

[Angle addition postulate image code](Programs/Ch01/S03_05_Angle_addition_postulate_image.py)
![Angle addition postulate image](Images/Ch01/S03_05_Angle_addition_postulate.png)
*Angle addition postulate*

## Midpoint and bisector (Punto medio y bisectriz)
[Ch01_S04](https://www.ck12.org/reader/reader-index.html#section/2932920/1.4/9549314)

(Congruencia)
**Congruence**: when two geometric figures have the same shape and size, e.g. two segments with the same length, two angles with the same measure, two triangles with the same shape and size.

> Congruence notation
>
> Let $\overline{AB}$ be a segment, the congruence with itself is denoted as
> $$\overline{AB} \cong \overline{BA}$$
> This symbol \cong is used in general to indicate two congruent geometric figures.

(Punto medio)
**Midpoint**: the point on a segment, that divides it into two congruent segments.
[Midpoint image code](Programs/Ch01/S04_01_Midpoint_image.py)
![Midpoint image](Images/Ch01/S04_01_Midpoint.png)
*Midpoint*

As shown in the *Midpoint* image, the lengths $AB$ and $BC$ are equal, i.e. $AB = BC$, so the point $B$ is the midpoint of the segment $\overline{AC}$.

(Postulado del punto medio)
**Midpoint postulate**: a segment has exactly one midpoint.

(Fórmula del punto medio)
**Midpoint formula**: a formula to calculate the midpoint from two points.

> Midpoint formula
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points in the $x$-$y$ plane, then the midpoint of the segment they form is
> $$\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

This formula can be derived from a more general formula

> General formula to divide a segment into $n$ subsegments and get the location of the $k$-th subsegment
>
> Let $(x_1, y_1)$ and $(x_2, y_2)$ be the two points that define a segment, this segment can be divided into $n$ subsegments. Counting from $(x_1, y_1)$, the coordinates of the $k$-th subsegment are
> $$\left(x_1 + k\frac{x_2 - x_1}{n}, y_1 + k\frac{y_2 - y_1}{n}\right)$$

Making $k = 1$ and $n = 2$ results in the midpoint formula.

(Bisectriz de un segmento)
**Segment bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in any angle.
[Segment bisector image code](Programs/Ch01/S04_02_Segment_bisector_image.py)
![Segment bisector image](Images/Ch01/S04_02_Segment_bisector.png)
*Segment bisector*

(Mediatriz)
**Perpendicular bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in a perpendicular way.
[Perpendicular bisector image code](Programs/Ch01/S04_03_Perpendicular_bisector_image.py)
![Perpendicular bisector image](Images/Ch01/S04_03_Perpendicular_bisector.png)
*Perpendicular bisector*

(Postulado de la mediatriz)
**Perpendicular bisector postulate**: a given segment has only one line that is its perpendicular bisector.

There are infinitely many segment bisectors and only one perpendicular bisector to a given segment. As shown in the *Perpendicular bisector* image, $\overleftrightarrow{DE} \perp \overline{AC}$, and $\overline{AB} \cong \overline{BC}$, so the line $\overleftrightarrow{DE}$ is the perpendicular bisector of $\overline{AC}$.

(Construcción de la mediatriz)
**Perpendicular bisector construction**: a geometric construction to draw the perpendicular bisector of a given segment

> Perpendicular bisector construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials)
> 1. Draw the segment whose perpendicular bisector will be constructed, with space around it.
> 2. Center the compass on one of the endpoints of the segment from step 1, with a radius greater than half the length of the segment. Draw arcs above and below the segment. Repeat this step with the other endpoing of the segment, ensuring that the arcs above and below intercept, and being careful to not change the radius of the compass.
> 3. Draw a line that passes through both arc interceptions above and below the segment, this line bisects the segment perpendicularly.
>
> This construction works as long as the radius of the compass is the same on both endpoints, because this would create two circles of equal radii, and the line that passes through their arc interceptions must be at equal distance from both centers, which is the midpoint of the segment between the centers.
>
> If one radius is smaller, this can serve to create lines that cross the segment at other fractions different from one half the lenght of the segment.

(Bisectriz de un ángulo)
**Angle bisector**: a line, ray, or segment, that divides a given angle into two congruent angles, each with half the measure of the given angle.
[Angle bisector image code](Programs/Ch01/S04_04_Angle_bisector_image.py)
![Angle bisector image](Images/Ch01/S04_04_Angle_bisector.png)
*Angle bisector*

The segment $\overline{AC}$ is the angle bisector of the angle $\angle DAB$, so $m \angle DAC = m \angle BAC$.

(Postulado de la bisectriz de un ángulo)
**Angle bisector postulate**: a given angle has only one line that is its angle bisector.

In the *Angle bisector* image, if the segment $\overline{AC}$ is converted into a line, then the line $\overleftrightarrow{AC}$ is the angle bisector of the angle $\angle DAB$. The angle bisector does not have to be a line, but if it's a line then it's guaranteed to be the only one that is the angle bisector.

(Construcción de la bisectriz de un ángulo)
**Angle bisector construction**: a geometric construction to draw the angle bisector of a given angle

> Angle bisector construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials)
> 1. Draw the angle whose bisector will be constructed, with space around it.
> 2. Center the compass on the vertex of the angle, draw an arc at any radius such that it crosses both sides of the angle.
> 3. Apply the perpendicular bisector construction, taking as endpoints the intersections of the arc with the sides of the angle.
> 4. Extend the line of the perpendicular bisector construction made in step 3 until it crosses the vertex of the angle, this line is the angle bisector.

## Angle pairs (Pares de ángulos)
[Ch01_S05](https://www.ck12.org/reader/reader-index.html#section/4668241/1.5/9549314)

(Ángulos complementarios)
**Complementary angles**: two angles whose measures when added together add up to $90 \degree$ or $\pi/2$ radians.

(Ángulos suplementarios)
**Supplementary angles**: two angles whose measures when added together add up to $180 \degree$ or $\pi$ radians.

(Ángulos adyacentes)
**Adjacent angles**: two angles that have the same vertex and share one side, which means that only three rays are required to create two adjacent angles.

(Par lineal)
**Linear pair**: two adjacent angles such that the two non-shared sides form a straight line.

(Postulado del par lineal)
**Linear pair postulate**: the two angles of a linear pair are supplementary.

(Ángulos verticales)
**Vertical angles**: in the intersection of two lines, vertical angles are pairs of angles that are on opposite sides of the intersection.
[Vertical angles image code](Programs/Ch01/S05_01_Vertical_angles_image.py)
![Vertical angles image](Images/Ch01/S05_01_Vertical_angles.png)
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

## Polygon classification (Clasificación de polígonos)
[Ch01_S06](https://www.ck12.org/reader/reader-index.html#section/2932922/1.6/9549314)
