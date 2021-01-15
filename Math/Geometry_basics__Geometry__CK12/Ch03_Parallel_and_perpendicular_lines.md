
#   Parallel and perpendicular lines (Líneas paralelas y perpendiculares)

## Parallel lines, skew lines, perpendicular lines, transversals (Líneas paralelas, líneas alabeadas, líneas perpendiculares, transversales)
[Ch03_S01](https://www.ck12.org/reader/reader-index.html#section/9509902/3.1/9549314)

(Paralelismo en geometría)
**Geometric parallelism**: the relationship that is produced when two distinct figures extend indefinitely and never intersect each other.

Two parallel lines that belong to the same plane, extend indefinitely and never intersect each other. Two parallel planes in space, extend indefinitely and never intersect each other.

> Parallel relation notation
>
> The symbol $\parallel$ indicates a parallel relation. Let $\overleftrightarrow{AB}$, $\overleftrightarrow{CD}$ be two lines, such that they are parallel to each other, this can be denoted as $\overleftrightarrow{AB} \parallel \overleftrightarrow{CD}$, read as the line $AB$ is parallel to the line $CD$ (la línea $AB$ es paralela a la línea $CD$).

In diagrams, parallel lines are indicated by placing arrowheads inside the lines. Each set of parallel lines has its own amount of arrowheads.
[Parallel lines image code](Programs/Ch03/S01_01_Parallel_lines_image.py)
![Parallel lines image](Images/Ch03/S01_01_Parallel_lines.png)
*Parallel lines*

In the image, $k \parallel l$, which is denoted with one arrowhead inside the lines. Also $m \parallel n$, which is denoted with two arrowheads inside the lines.

(Líneas alabeadas)
**skew lines**: a relationship between two lines, such that they are not parallel but also do not intersect. This is possible in lines that belong to different planes.
[Skew lines image code](Programs/Ch03/S01_02_Skew_lines_image.py)
![Skew lines image](Images/Ch03/S01_02_Skew_lines.png)
*Skew lines*

The blue line and the crimson line are not parallel, and yet they never intersect, because they lie in different planes.

(Postulado de las paralelas)
**Parallel postulate**: given a line and a point not on the line, there is only one parallel to the line that passes through the point.

(Postulado de las perpendiculares)
**Perpendicular postulate**: given a line and a point not on the line, there is only one perpendicular line to the line that passes through the point.

(Construcción de una línea perpendicular)
**Perpendicular line construction**: a geometric construction to draw the unique perpendicular line to a given line that passes through a given point.

> Perpendicular line construction
>
> This construction requires paper, pencil, straightedge, and compass (or equivalent tools and materials)
> 1. Draw a segment and a point outside of it, with space around it.
> 2. Center the compass on the point outside the segment, with a radius that goes beyond the segment. Draw an arc such that it intersects the segment two times.
> 3. Apply the perpendicular bisector construction, taking as endpoints the two arc intersections with the segment. The resulting line is perpendicular to the segment and passes through the point outside of it.
>
> This construction can also be used to draw a perpendicular through a point on the line. In that case, the arc from step 2 is drawn so that it intersects the segment at both sides of the point.

(Línea transversal)
**Transversal line**: a line that intersects two other distinct lines.
[Transversal line image code](Programs/Ch03/S01_03_Transversal_line_image.py)
![Transversal line image](Images/Ch03/S01_03_Transversal_line.png)
*Transversal line*

The lime green line is the transversal, although all the lines intersect the other two, which means that effectively all three lines are transversal. The case in which this does not happen, is when the other two lines are parallel.
[Transversal to parallel lines image code](Programs/Ch03/S01_04_Transversal_to_parallel_lines_image.py)
![Transversal to parallel lines image](Images/Ch03/S01_04_Transversal_to_parallel_lines.png)
*Transversal to parallel lines*

The line $t$ is transversal to the lines $l$ and $m$, and $l \parallel m$. Angles can be denoted with numbers, in the image appear the angles $\angle 1$ through $\angle 8$.

(Partes de una transversal)
**Parts of a transversal**: the following parts will be defined using the *Transversal to parallel lines* image, but these concepts apply to transversals in general.

- **Interior area** (Área interna): the area between the two lines, e.g. the area between $l$ and $m$.

- **Exterior area** (Área externa): the area outside of the two lines, e.g. the area outside of $l$ and $m$.

- **Corresponding angles** (Ángulos correspondientes): two angles that are in the same position relative to the transversal, but each on a different line, e.g. $\angle 1$ and $\angle 5$ are corresponding angles, like $\angle 2$ and $\angle 6$, also $\angle 3$ and $\angle 7$, and lastly $\angle 4$ and $\angle 8$ form corresponding angle pairs.

- **Alternate interior angles** (Ángulos alternos internos): two angles that lie on the interior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 3$ and $\angle 6$ are alternate interior angles, like $\angle 4$ and $\angle 5$.

- **Alternate exterior angles** (Ángulos alternos externos): two angles that lie on the exterior area, do not form a linear pair, and are on opposite sides of the transversal, e.g. $\angle 1$ and $\angle 8$ are alternate exterior angles, like $\angle 2$ and $\angle 7$.

- **Same side interior angles** (Ángulos conjugados internos): two angles that lie on the interior area, are distinct, and are on the same side of the transversal, e.g. $\angle 3$ and $\angle 5$ are same side interior angles, like $\angle 4$ and $\angle 6$.

- **Same side exterior angles** (Ángulos conjugados externos): two angles that lie on the exterior area, are distinct, and are on the same side of the transversal, e.g. $\angle 1$ and $\angle 7$ are same side exterior angles, like $\angle 2$ and $\angle 8$.

## Properties of parallel lines (Propiedades de las líneas paralelas)
[Ch03_S02](https://www.ck12.org/reader/reader-index.html#section/2932933/3.2/9549314)

(Postulado de los ángulos correspondientes)
**Corresponding angles postulate**: in a transversal of two parallels, the corresponding angles are congruent. From the *Transversal to parallel lines* image, $\angle 1 \cong \angle 5$, $\angle 2 \cong \angle 6$, $\angle 3 \cong \angle 7$, and $\angle 4 \cong \angle 8$. Its converse is also a postulate.

(Teorema de los ángulos alternos internos)
**Alternate interior angles theorem**: two parallel lines that are intersected by a transversal, have their alternate interior angles congruent.

> Proof of the alternate interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | From the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 1 \cong \angle 4$ | Vertical angles theorem |
> | $\angle 4 \cong \angle 5$ | Transitive property of congruence |

The same proof applies for the other three pairs of alternate interior angles.

(Teorema de los ángulos alternos externos)
**Alternate exterior angles theorem**: two parallel lines that are intersected by a transversal, have their alternate exterior angles congruent.

> Proof of the alternate exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | From the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 5 \cong \angle 8$ | Vertical angles theorem |
> | $\angle 1 \cong \angle 8$ | Transitive property of congruence |

The same proof applies for the other three pairs of alternate exterior angles.

(Teorema de los ángulos conjugados internos)
**Same side interior angles theorem**: two parallel lines that are intersected by a transversal, have supplementary same side interior angles.

> Proof of the same side interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | From the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 1$ and $\angle 3$ are supplementary | Linear pair postulate |
> | $\angle 3$ and $\angle 5$ are supplementary | Converse of the congruent supplements theorem |

The same proof applies for the other pair of same side interior angles.

(Teorema de los ángulos conjugados externos)
**Same side exterior angles theorem**: two parallel lines that are intersected by a transversal, have supplementary same side exterior angles.

> Proof of the same side exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | $l \parallel m$, with transversal $t$ | From the *Transversal to parallel lines* image |
> | $\angle 1 \cong \angle 5$ | Corresponding angles postulate |
> | $\angle 5$ and $\angle 7$ are supplementary | Linear pair postulate |
> | $\angle 1$ and $\angle 7$ are supplementary | Converse of the congruent supplements theorem |

The same proof applies for the other pair of same side exterior angles.

## Proving lines parallel (Demostrar el paralelismo entre líneas)
[Ch03_S03](https://www.ck12.org/reader/reader-index.html#section/2932934/3.3/9549314)

(Converso del teorema de los ángulos alternos internos)
**Converse of the alternate interior angles theorem**: given two lines intersected by a transversal, if their alternate interior angles are congruent, then the two lines are parallel.

> Proof of the converse of the alternate interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 3 \cong \angle 6$ | From the *Transversal to parallel lines* image |
> | $\angle 3 \cong \angle 2$ | Vertical angles theorem |
> | $\angle 2 \cong \angle 6$ | Transitive property of congruence |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

(Converso del teorema de los ángulos alternos externos)
**Converse of the alternate exterior angles theorem**: given two lines intersected by a transversal, if their alternate exterior angles are congruent, then the two lines are parallel.

> Proof of the converse of the alternate exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 1 \cong \angle 8$ | From the *Transversal to parallel lines* image |
> | $\angle 5 \cong \angle 8$ | Vertical angles theorem |
> | $\angle 1 \cong \angle 5$ | Transitive property of congruence |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

(Converso del teorema de los ángulos conjugados internos)
**Converse of the same side interior angles theorem**: given two lines intersected by a transversal, if their same side interior angles are supplementary, then the two lines are parallel.

> Proof of the converse of the same side interior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 3$ and $\angle 5$ are supplementary | From the *Transversal to parallel lines* image |
> | $\angle 1$ and $\angle 3$ are supplementary | Linear pair postulate |
> | $\angle 1 \cong \angle 5$ | Congruent supplements theorem |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

(Converso del teorema de los ángulos conjugados externos)
**Converse of the same side exterior angles theorem**: given two lines intersected by a transversal, if their same side exterior angles are supplementary, then the two lines are parallel.

> Proof of the converse of the same side exterior angles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Lines $l$ and $m$ have the transversal $t$, and $\angle 1$ and $\angle 7$ are supplementary | From the *Transversal to parallel lines* image |
> | $\angle 5$ and $\angle 7$ are supplementary | Linear pair postulate |
> | $\angle 1 \cong \angle 5$ | Congruent supplements theorem |
> | $l \parallel m$ | Converse of the corresponding angles postulate |

(Propiedad transitiva de las líneas paralelas)
**Transitive property of parallel lines**: given two parallel lines, if the first one is parallel to a third line, then the second line is also parallel to the third.

> Transitive property of parallel lines
>
> Let $k$, $l$, $m$, be lines, if $k \parallel l$ and $l \parallel m$, then $k \parallel m$.

## Properties of perpendicular lines (Propiedades de las líneas perpendiculares)
[Ch03_S04](https://www.ck12.org/reader/reader-index.html#section/2932935/3.4/9549314)

## Algebra of parallel and perpendicular lines (Álgebra de las líneas paralelas y perpendiculares)
[Ch03_S05](https://www.ck12.org/reader/reader-index.html#section/2932936/3.5/9549314)

## Distance fórmula (Fórmula de distancia)
[Ch03_S06](https://www.ck12.org/reader/reader-index.html#section/2932937/3.6/9549314)