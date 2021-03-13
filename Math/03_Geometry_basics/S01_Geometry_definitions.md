
#   Geometry definitions (Definiciones de geometría)

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

(Figuras congruentes)
**Congruent figures**: figures that have the same shape and also the same size. Let $\overline{AB}$ be a segment, the congruence with itself is denoted as $\overline{AB} \cong \overline{BA}$. This symbol $\cong$ is used in general to indicate two congruent geometric figures.

(Figuras similares | Figuras semejantes)
**Similar figures**: figures that have the same shape but not the same size. Similarity (semejanza) is denoted with the $\sim$ symbol. Let $Fig_1$ and $Fig_2$ represent two figures that are similar, this is written as $Fig_1 \sim Fig_2$. Similar figures have their corresponding angles congruent and their corresponding sides proportional. This can be said as "corresponding sides of similar figures are proportional", and "corresponding angles of similar figures are congruent".
[Similar figures image code](Programs/S07/Similar_figures_image.py)
![Similar figures image](Images/S07/Similar_figures.png)
*Similar figures*

Following this definition, similar polygons are polygons with the same shape, but their size may differ.

(Factor de escala)
**Scale factor**: in two similar figures, the scale factor is the constant that allows getting one figure from the other. Multiplying each length of the first figure by the scale factor, results in the lengths of the second figure. Dividing each length of the second figure by the scale factor, results in the lengths of the first figure.

In the *Similar figures* the scale factor needed to get from the figure to the left, to the figure to the right, is $1/2$, which is a ratio of $1:2$, so the lengths of the figure to the right are half of those of the figure to the left.

> Scale factor
>
> Let $Fig_1$ and $Fig_2$ be two similar figures, $Fig_1 \sim Fig_2$, let $A_1$ and $B_1$ be two points on $Fig_1$ that are correspondent to the points $A_2$ and $B_2$ on $Fig_2$, and let $k$ be the scale factor to obtain $Fig_2$ from $Fig_1$, then
>
> $$A_2B_2 = k A_1B_1$$

This means that to obtain the length $A_2B_2$, the scale factor $k$ must be multiplied by the length $A_1B_1$.

(Autosimilaridad)
**Self-similarity**: Self-similarity is a property of the figures in which a part of the figure has the same shape as the whole figure, which means that the part is similar to the whole, the figure is similar to itself.

(Fractales)
**Fractals**: figures that have infinite self-similarity, meaning that in a fractal, each part is similar to the whole, and then each part has subparts similar to the part, and each subpart has subsubparts similar to the subpart, and so on infinitely. Because of this, fractals can be created in iterations. The initial shape before the first iteration is called stage 0 (etapa 0), and then the result of each iteration is the respective stage.

(Punto)
**Point**: a single piece of space that has no extension, i.e. a figure with zero dimensions. Points are used to indicate locations in space, they are represented with dots in diagrams.
[Points in space image code](Programs/S01/Points_in_space_image.py)
![Points in space image](Images/S01/Points_in_space.png)
*Points in space*

The points shown in the *Points in space* image, are in the shape of blue dots. These shapes have an extension, a size, they are two dimensional, and they must be, otherwise they would be invisible if they truly were zero dimensional. These dots represent points with no dimensions.

Points are commonly labeled using an uppercase letter. The image shown has four points, namely $A$, $B$, $C$, and $D$.

(Línea | Recta)
**Line**: a shape with infinite points that extends in a single dimension indefinitely. A line has no start nor ending, it has a given direction and a location in space.
[Line in space image code](Programs/S01/Line_in_space_image.py)
![Line in space image](Images/S01/Line_in_space.png)
*Line in space*

Lines are labeled using a single lowercase letter, such as $g$, or with the labels of two points on the line and a bidirectional arrow on top, such as $\overleftrightarrow{PQ}$ and $\overleftrightarrow{QP}$. All these three labels denote the same line.

(Plano)
**Plane**: a shape with infinite lines that extends in two dimensions (2D) indefinitely. A plane has no start nor ending, it has a given direction and a location in space.
![Planes in space image](Images/S01/Planes_in_space.png)
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
[Line segment image code](Programs/S01/Line_segment_image.py)
![Line segment image](Images/S01/Line_segment.png)
*Line segment*

Line segments are labeled using its endpoints and a horizontal bar on top of them, such as $\overline{AB}$ and $\overline{BA}$. They can also be simply called segments.

(Rayo)
**Ray**: a line that is only truncated in one side, while the other side extends indefinitely. A ray has one endpoint.
[Ray image code](Programs/S01/Ray_image.py)
![Ray image](Images/S01/Ray.png)
*Ray*

Rays are labeled using the endpoint and the point inside the ray with an arrow on top, such as $\overrightarrow{AB}$ and $\overleftarrow{BA}$. The arrow on top points in the same direction as the ray.

(Intersección)
**Intersection**: the point or points where two shapes cross each other. When two distinct lines intersect, the intersection is a point. When two distinct planes intersect, the intersection is a line. When a line outside of a plane intersects said plane, the intersection is a point. When three distinct planes intersect, the intersection is a point.

(Punto equidistante a otros puntos)
**Equidistant point to other points**: a given point is equidistant to other points when its distance to all the other points is the same.

(Punto de concurrencia)
**Point of concurrency**: the intersection in a single point, of three or more lines, rays, or segments.
[Point of concurrency image code](Programs/S01/Point_of_concurrency_image.py)
![Point of concurrency image](Images/S01/Point_of_concurrency.png)
*Point of concurrency*

The point $A$ is a point of concurrency.

(Figuras irregulares)
**Irregular figures**: irregular figures are figures whose shape is not a basic shape.

(Vértice)
**Vertex**: any point from which one or more lines stem.

(Ángulo)
**Angle**: in two lines that share a vertex, the angle is the measure of rotation of one line to get to the other. 

If a vertex has only two lines, then an angle can be named after said vertex.

> Angle notation
>
> Let $A$ be a vertex with two lines stemming from it, then $\angle A$ is the angle formed between the two lines, and $m \angle A$ is the measure of said angle.

Angles are commonly measured in degrees and in radians. In degrees a whole rotation that ends at the starting position is measured as $360 \text{\textdegree}$ read as $360$ degrees ($360$ grados), and in radians this is measured as $2 \pi$ read as $2 \pi$ radians ($2 \pi$ radianes).

Given those measures, half a whole rotation is $180 \text{\textdegree}$ or $\pi$ radians. Angles are commonly shown in diagrams with an arc between the two lines.

If more than two lines stem from a vertex, then an unambiguous way to label an angle is using three points, the vertex and one point in each of the two lines in the angle. For example, given the vertex $A$, the point $B$ in one line, and the point $C$ in the other line, then the angle formed can be labeled as $\angle BAC$ or $\angle CAB$, putting the vertex $A$ in the middle.

An angle can be measured in two ways, because there are two ways in which a ray can be rotated to coincide with another (rotating the ray clockwise, and rotating the ray counterclockwise). The standard definition of the measure of an angle, is that it's the smallest measure of the two. The smallest measure of an angle is always less than or equal to half a circle, i.e. $180 \text{\textdegree}$ or $\pi$ radians. Still, angles greater than $\pi$ can be considered.

(Postulado)
**Postulate**: the axioms of geometry, i.e. facts of geometry that are accepted as true. Postulates act as definitions.

(Lados y ángulos correspondientes)
**Corresponding sides and angles**: in similar or congruent figures, the sides and angles that would be the same if replacing one figure for the other.

The corresponding sides of two figures have the same ratio (which is $1$ for congruent figures), and their corresponding angles have the same value.

Similar triangles are similar figures.

## Segments and distance (Segmentos y distancia)

(Distancia)
**Distance**: the length between two given points.

(Plano coordenado)
**Coordinate grid**: the two dimensional plane that uses tuples of two numbers, $x$ and $y$, to represent the location of points in the plane. The $x$ coordinate measures horizontal distance, and the $y$ coordinate measures vertical distance.

## Angles and measurement (Ángulos y medición)

Given two distinct rays that share their endpoint, the angle formed between the two rays is the measure of the rotation needed to get from one ray to the other.

> Angle notation
>
> Let $A$, $B$, and $C$, be three points, such that they form two distinct rays, $\overrightarrow{BA}$ and $\overrightarrow{BC}$, then the angle that these rays form is denoted as $\angle ABC$ or $\angle CBA$ or $\angle B$ if no more than one angle stems from $B$.

[Angle from two rays image code](Programs/S01/Angle_from_two_rays_image.py)
![Angle from two rays image](Images/S01/Angle_from_two_rays.png)
*Angle from two rays*

Angles are commonly shown in diagrams with an arc between the two rays. In the *Angle from two rays* image, the angle $\angle B$ is $\theta$.

(Vértice de un ángulo)
**Vertex of an angle**: in an angle, the vertex is the endpoint where the two lines join. In the angle $\angle ABC$, the vertex is the point $B$.

(Lados de un ángulo)
**Sides of an angle**: each of the two lines that form the angle.

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

(Paralelismo en geometría)
**Geometric parallelism**: the relationship that is produced when two distinct figures extend indefinitely and never intersect each other.

Two parallel lines that belong to the same plane, extend indefinitely and never intersect each other. Two parallel planes in space, extend indefinitely and never intersect each other. The distance between parallel lines or planes is constant.

> Parallel relation notation
>
> The symbol $\parallel$ indicates a parallel relation. Let $\overleftrightarrow{AB}$, $\overleftrightarrow{CD}$ be two lines, such that they are parallel to each other, this can be denoted as $\overleftrightarrow{AB} \parallel \overleftrightarrow{CD}$, read as the line $AB$ is parallel to the line $CD$ (la línea $AB$ es paralela a la línea $CD$).

In diagrams, parallel lines are indicated by placing arrowheads inside the lines. Each set of parallel lines has its own amount of arrowheads.
[Parallel lines image code](Programs/S01/Parallel_lines_image.py)
![Parallel lines image](Images/S01/Parallel_lines.png)
*Parallel lines*

In the image, $k \parallel l$, which is denoted with one arrowhead inside the lines. Also $m \parallel n$, which is denoted with two arrowheads inside the lines.

(Propiedad transitiva de las líneas paralelas)
**Transitive property of parallel lines**: given two parallel lines, if the first one is parallel to a third line, then the second line is also parallel to the third.

> Transitive property of parallel lines
>
> Let $k$, $l$, $m$, be lines, if $k \parallel l$ and $l \parallel m$, then $k \parallel m$.

(Líneas perpendiculares)
**Perpendicular lines**: two lines (or rays, or segments) that cross each other at right angles, i.e. the four angles formed at the intersection of the lines are right angles.
[Perpendicular lines image code](Programs/S01/Perpendicular_lines_image.py)
![Perpendicular lines image](Images/S01/Perpendicular_lines.png)
*Perpendicular lines*

Perpendicularity is denoted with the $\perp$ symbol. From the *Perpendicular lines* image, the lines $l$ and $m$ are perpendicular to each other, so $l \perp m$, which is the same as $m \perp l$, or $\overleftrightarrow{BC} \perp \overleftrightarrow{DE}$.

(Líneas alabeadas)
**skew lines**: a relationship between two lines, such that they are not parallel but also do not intersect. This is possible in lines that belong to different planes.
[Skew lines image code](Programs/S01/Skew_lines_image.py)
![Skew lines image](Images/S01/Skew_lines.png)
*Skew lines*

The blue line and the crimson line are not parallel, and yet they never intersect, because they lie in different planes.

(Marcas de los ángulos)
**Angle markings**: angles can be marked to differentiate between them. Angles are marked with arc marks (marcas del ángulo). Arc marks are commonly of two types: several repeated arcs, or arcs with small perpendicular lines crossing them.
[Angle markings image code](Programs/S01/Angle_markings_image.py)
![Angle markings image](Images/S01/Angle_markings.png)
*Angle markings*

(Marcas de los segmentos)
**Segment markings**: segments can be marked to differentiate between them. Segments are marked with hash marks (marcas del segmento). Hash marks are commonly repeated small lines perpendicular to the segment, placed around the center of the segment.
[Segment markings image code](Programs/S01/Segment_markings_image.py)
![Segment markings image](Images/S01/Segment_markings.png)
*Segment markings*

In the *Segment markings* image, the two segments at the bottom have the same length, as shown by their equal markings. The rest of the segments are different from each other, so each one has it's unique marking.

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
[Midpoint image code](Programs/S01/Midpoint_image.py)
![Midpoint image](Images/S01/Midpoint.png)
*Midpoint*

As shown in the *Midpoint* image, the lengths $AB$ and $BC$ are equal, i.e. $AB = BC$, so the point $B$ is the midpoint of the segment $\overline{AC}$.

(Bisectriz de un segmento)
**Segment bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in any angle.
[Segment bisector image code](Programs/S01/Segment_bisector_image.py)
![Segment bisector image](Images/S01/Segment_bisector.png)
*Segment bisector*

(Mediatriz)
**Perpendicular bisector**: a line, ray, or segment, that passes through the midpoint of a given segment in a perpendicular way.
[Perpendicular bisector image code](Programs/S01/Perpendicular_bisector_image.py)
![Perpendicular bisector image](Images/S01/Perpendicular_bisector.png)
*Perpendicular bisector*

(Bisectriz de un ángulo)
**Angle bisector**: a line, ray, or segment, that divides a given angle into two congruent angles, each with half the measure of the given angle.
[Angle bisector image code](Programs/S01/Angle_bisector_image.py)
![Angle bisector image](Images/S01/Angle_bisector.png)
*Angle bisector*

The segment $\overline{AC}$ is the angle bisector of the angle $\angle DAB$, so $m \angle DAC = m \angle BAC$.

## Angle pairs (Pares de ángulos)

(Ángulos complementarios)
**Complementary angles**: two angles that added together measure $90 \text{\textdegree}$ or $\pi/2$ radians. Each angle in this pair is the complement (complemento) of the other.

(Ángulos suplementarios)
**Supplementary angles**: two angles that added together measure $180 \text{\textdegree}$ or $\pi$ radians. Each angle in this pair is the supplement (suplemento) of the other.

(Ángulos adyacentes)
**Adjacent angles**: two angles that have the same vertex and share one side, without overlapping each other, which means that only three rays are required to create two adjacent angles.

(Par lineal)
**Linear pair**: two adjacent angles such that the two non-shared sides form a straight line.

(Ángulos verticales)
**Vertical angles**: in the intersection of two lines, vertical angles are pairs of angles that are on opposite sides of the intersection.
[Vertical angles image code](Programs/S01/Vertical_angles_image.py)
![Vertical angles image](Images/S01/Vertical_angles.png)
*Vertical angles*

As shown in the *Vertical angles* image, the angles $\alpha_1$ and $\alpha_2$ are vertical angles, and also the angles $\beta_1$ and $\beta_2$ are vertical angles. Each of these pairs have their angles located in opposite sides of the intersection of the lines.

(Ángulo comprendido entre dos lados)
**Included angle between two sides**: the angle between two given sides, is the included angle, so the sides must share a vertex, which is the vertex of the angle.

## Classifying polygons (Clasificación de polígonos)

(Clasificación de triángulos según sus ángulos)
**Classification of triangles based on angles**:

- **Right triangle** (Triángulo rectángulo): a triangle that has one right angle.
[Right triangle image code](Programs/S01/Right_triangle_image.py)
![Right triangle image](Images/S01/Right_triangle.png)
*Right triangle*

(Clasificación de triángulos según sus lados)
**Classification of triangles based on sides**:

(Medida lineal)
**Linear measure**: measure for length, like distances, width, height, depth, etcetera, in linear units (unidades lineales).

(Medida cuadrada)
**Square measure**: measure for area size, in square units (unidades cuadradas).

(Medida cúbica)
**Cubic measure**: measure for volume, in cubic units (unidades cúbicas).

(Perímetro)
**Perimeter**: in a two dimensional shape, the measure of the distance around it.

(Área)
**Area**: in a two dimensional shape, the measure of the surface covered by it.

(Área superficial)
**Surface area**: in a three dimensional shape, the amount of area covered by its surface.

(Volumen)
**Volume**: in a three dimensional shape, the measure of the space occupied by it.

(Sólidos)
**Solids**: three dimensional shapes.