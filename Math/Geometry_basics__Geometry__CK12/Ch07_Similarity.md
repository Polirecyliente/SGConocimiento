
#   Similarity (Similaridad)

<!--
#T# Table of contents

#C# Ratios and proportions (Ratios y proporciones)
#C# Similar polygons (Polígonos similares)
#C# Similarity by AA (Similaridad por AA)
#C# Similarity by SSS and SAS (Similaridad por LLL y LAL)
#C# Proportionality relationships (Relaciones de proporcionalidad)
#C# Similarity transformations (Transformaciones de similaridad)
#C# Self-similarity (Autosimilaridad)

#T# Beginning of content
-->

## Ratios and proportions (Ratios y proporciones)
[Ch07_S01](https://www.ck12.org/reader/reader-index.html#section/2932962/7.1/9549314)

A ratio is a division of two numbers measured in the same scale or unit of measure. The notation of ratios in particular, includes the use of the colon : symbol to replace the division symbol. So the ratio $\frac{a}{b}$ can be denoted as $a:b$. The ratio $a:b$ is read as $a$ to $b$ ($a$ a $b$).

In a ratio, the division operation is not actually made, for example the ratio $a:b$, in this ratio, if $a$ and $b$ are measured in type1 units, the ratio indicates that there are $a$ units of type1 per every $b$ units of type1. The division is not performed. This allows writing ratios with more than two numbers, for example the ratio $a:b:c$ with $c$ also measured in type1 units, indicates that there are $a$ units of type1 per every $b$ units, and also there are $a$ units per every $c$ units, and there are $b$ units per every $c$ units. When a ratio has more than two numbers, the fraction notation is not used, only the colon notation.

(Proporción)
**Proportion**: an equation in which two fractions (ratios or rates) are equated. Let $a$, $b$, $c$, $d$, be numbers, with $b$ and $d$ being nonzero, then $\frac{a}{b} = \frac{c}{d}$ is a proportion, it's read as $a$ is to $b$ as $c$ is to $d$ ($a$ es a $b$ como $c$ es a $d$).

(Producto cruzado)
**Cross product**: a proportion where the denominators have been multiplied in both sides, i.e. in the proportion $\frac{a}{b} = \frac{c}{d}$, the cross product is $ad = bc$. This concept is used to test if a proportion is true without dividing.

(Medios y extremos de una proporción)
**Means and extremes of a proportion**: any proportion $\frac{a}{b} = \frac{c}{d}$ can be represented with ratios as $a:b = c:d$. Following this representation, the numbers $b$ and $c$ are called the means (they are in the center), and the numbers $a$ and $d$ are called the extremes (they are in the extremes). Using these definitions, it can be said that the cross product $ad = bc$ is the same as saying that the product of the extremes is equal to the product of the means of the proportion.

(Proporción extendida)
**Extended proportion**: a proportion with more than one equal sign, which means that an extended proportion makes several fractions equal, e.g. $\frac{a}{b} = \frac{c}{d} = \frac{e}{f}$.

(Teorema del producto cruzado)
**Cross product theorem | Cross-multiplication theorem**: Let $a$, $b$, $c$, $d$, be real numbers, with $b$ and $d$ being nonzero. If $\frac{a}{b} = \frac{c}{d}$, then $ad = bc$.

> Proof of the cross product theorem
>
> Because of the multiplication property of equality, the equality $\frac{a}{b} = \frac{c}{d}$ is maintained when multiplying both sides by $b$ and $d$, and so $ad = bc$. $\blacksquare$

(Converso del teorema del producto cruzado)
**Converse of the cross product theorem**: Let $a$, $b$, $c$, $d$, be real numbers, with $b$ and $d$ being nonzero. If $ad = bc$, then $\frac{a}{b} = \frac{c}{d}$.

> Proof of the converse of the cross product theorem
>
> Because of the division property of equality, the equality $ad = bc$ is maintained when dividing both sides by $b$ and $d$, and so $\frac{a}{b} = \frac{c}{d}$. $\blacksquare$

(Corolario)
**Corollary**: a theorem that is not proved, because it's too small and its true follows directly from another theorem or axiom, so it doesn't need to be proved.

(Corolarios del teorema del producto cruzado y su converso)
**Corollaries of the cross product theorem and its converse**: the cross product theorem and its converse have a few corollaries as follows.

> Corollaries of the cross product theorem and its converse
>
> Let $a$, $b$, $c$, $d$ be nonzero real numbers, then
>
> If $\frac{a}{b} = \frac{c}{d}$, then $\frac{a}{c} = \frac{b}{d}$.
> If $\frac{a}{b} = \frac{c}{d}$, then $\frac{d}{b} = \frac{c}{a}$.
> If $\frac{a}{b} = \frac{c}{d}$, then $\frac{d}{c} = \frac{b}{a}$.

## Similar polygons (Polígonos similares)
[Ch07_S02](https://www.ck12.org/reader/reader-index.html#section/2932963/7.2/9549314)

(Figuras similares | Figuras semejantes)
**Similar figures**: figures that have the same shape but not the same size. Similarity (semejanza) is denoted with the $\sim$ symbol. Let $Fig_1$ and $Fig_2$ represent two figures that are similar, this is written as $Fig_1 \sim Fig_2$. Similar figures have their corresponding angles congruent and their corresponding sides proportional.
[Similar figures image code](Programs/Ch07/S01_01_Similar_figures_image.py)
![Similar figures image](Images/Ch07/S01_01_Similar_figures.png)
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

(Teorema del perímetro de figuras similares)
**Perimeter of similar figures theorem**: given two similar figures, that have a scale factor that measures the ratio of each length from the second figure over the respective length in the first figure, then the ratio of the perimeter of the second figure over the perimeter of the first figure is equal to the scale factor.

> Proof of the perimeter of similar figures theorem
>
> Let $Fig_1$ and $Fig_2$ be two similar figures, $Fig_1 \sim Fig_2$, and let $k$ be the scale factor to obtain $Fig_2$ from $Fig_1$. Let the most external sides of $Fig_1$ have lengths with measures $a_1$, $b_1$, $c_1$, ..., $z_1$, so the most external sides of $Fig_2$ have lengths with measures $a_2 = k a_1$, $b_2 = k b_1$, $c_2 = k c_1$, ..., $z_2 = k z_1$. Finally, let $P_1$ be the perimeter of $Fig_1$, and let $P_2$ be the perimeter of $Fig_2$. Because of the definition of perimeter, $P_1 = a_1 + b_1 + c_1 + ... + z_1$ and $P_2 = a_2 + b_2 + c_2 + ... + z_2$, and then by substitution and factoring the common factor $k$, $P_2 = k (a_1 + b_1 + c_1 + ... + z_1)$, so $P_2 = k P_1$. $\blacksquare$

In two similar figures $Fig_1$ and $Fig_2$, $Fig_1 \sim Fig_2$, with perimeters $P_1$ and $P_2$ respectively, and with a scale factor $k$ to obtain $Fig_2$ from $Fig_1$, then $P_2 = k P_1$.

## Similarity by AA (Similaridad por AA)
[Ch07_S03](https://www.ck12.org/reader/reader-index.html#section/2932964/7.3/9549314)

Similarity by AA means similarity by Angle-Angle (Similaridad (o semejanza) por Ángulo-Ángulo), so this similarity applies only to triangles.

(Construcción de dos triángulos similares dados dos ángulos)
**Two similar triangles given two angles construction**: a geometric construction to draw two similar triangles given two angles.

> Two similar triangles given two angles construction
>
> This construction requires paper, pencil, ruler, and protractor (or equivalent tools and materials).
> 1. Apply the triangle from two angles and their included side construction, to draw the first triangle, using the two given angles as the two angles of the construction, and using any wanted length for the included side.
> 2. Apply the triangle from two angles and their included side construction, to draw the second triangle, using the two given angles as the two angles of the construction, and using any other wanted length for the included side.

(Postulado AA de semejanza de triángulos)
**AA triangle similarity postulate**: given two triangles, if the first triangle has two angles that are congruent to the corresponding angles in the second triangle, then the triangles are similar. Given two triangles $\triangle ABC$ and $\triangle DEF$, if $\angle A \cong \angle D$ and $\angle B \cong \angle E$, or if $\angle A \cong \angle D$ and $\angle C \cong \angle F$, or if $\angle B \cong \angle E$ and $\angle C \cong \angle F$, then $\triangle ABC \sim \triangle DEF$.

(Medición indirecta)
**Indirect measurement**: a way to measure lengths that can't be accessed directly (lengths to places that are unreachable), using triangle similarity. For example, this can serve to measure lengths such as the width of a river, or the height of a tall building. It's an algorithm.
[Indirect measurement image code](Programs/Ch07/S03_01_Indirect_measurement_image.py)
![Indirect measurement image](Images/Ch07/S03_01_Indirect_measurement.png)
*Indirect measurement*

As shown, $\triangle ABC \sim \triangle ADE$. In indirect measurement, the length $DE$ is the length that wants to be measured but is inaccessible. The points $A$, $B$, $C$, and $D$, should be walkable, so only the point $E$ can be unreachable.

> Indirect measurement
>
> These steps follow the *Indirect measurement* image notation.
> 1. Observe the terrain to place the points $A$, $B$, $C$, $D$, and $E$. The point $E$ can be out of reach.
> 2. Make sure that $\angle ABC \cong \angle ADE$, that the points $A$, $C$, and $E$ are collinear, and that the points $A$, $B$, and $D$ are also collinear.
> 3. Measure the lengths $AB$, $AD$, and $BC$.
> 4. Calculate the scale factor $k$ to obtain $\triangle ADE$ from $\triangle ABC$, $k = \frac{AD}{AB}$.
> 5. Calculate $DE$ which is the indirect measurement, as $DE = k BC$.

## Similarity by SSS and SAS (Similaridad por LLL y LAL)
[Ch07_S04](https://www.ck12.org/reader/reader-index.html#section/2932965/7.4/9549314)

## Proportionality relationships (Relaciones de proporcionalidad)
[Ch07_S05](https://www.ck12.org/reader/reader-index.html#section/2932966/7.5/9549314)

## Similarity transformations (Transformaciones de similaridad)
[Ch07_S06](https://www.ck12.org/reader/reader-index.html#section/2932967/7.6/9549314)

## Self-similarity (Autosimilaridad)
[Ch07_S07](https://www.ck12.org/reader/reader-index.html#section/2932968/7.7/9549314)