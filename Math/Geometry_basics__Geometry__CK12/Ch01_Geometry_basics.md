
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

## Midpoint and bisector (Punto medio y bisectriz)
[Ch01_S04](https://www.ck12.org/reader/reader-index.html#section/2932920/1.4/9549314)

## Angle pairs (Pares de ángulos)
[Ch01_S05](https://www.ck12.org/reader/reader-index.html#section/4668241/1.5/9549314)

## Polygon classification (Clasificación de polígonos)
[Ch01_S06](https://www.ck12.org/reader/reader-index.html#section/2932922/1.6/9549314)
