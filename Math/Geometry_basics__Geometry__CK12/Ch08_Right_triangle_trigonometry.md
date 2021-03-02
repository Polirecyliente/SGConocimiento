
#   Right triangle trigonometry (Trigonometría del triángulo rectángulo)

<!--
#T# Table of contents

#C# The pythagorean theorem (El teorema de Pitágoras)
#C# Converse of the pythagorean theorem (Converso del teorema de Pitágoras)
#C# Using similar right triangles (Usando triángulos rectángulos similares)
#C# Special right triangles (Triángulos rectángulos especiales)
#C# Tangent, sine and cosine (Tangente, seno y coseno)
#C# Inverse trigonometric ratios (Ratios trigonométricos inversos)
#C# Laws of sines and cosines (Leyes de senos y cosenos)

#T# Beginning of content
-->

Attribution and License
![CK-12 Attribution](Images/CK-12_License.png)
Only the chapter name and the sections names are licensed under the CK-12 Curriculum Materials License, because they are copied from the 'Geometry' book by CK-12. The images and the rest of the plain text are licensed under the CC-BY license, the code is licensed under the MIT license (See README.md).

## The pythagorean theorem (El teorema de Pitágoras)
[Ch08_S01](https://www.ck12.org/reader/reader-index.html#section/2932971/8.1/9549314)

The pythagorean theorem and its proof have already been introduced (see Ch03_Parallel_and_perpendicular_lines.md).

(Longitud del cateto en un triángulo rectángulo)
**Length of the leg in a right triangle**: in a right triangle with hypotenuse of length $c$, and legs of lengths $a$ and $b$, $a = \sqrt{c^2 - b^2}$, $b = \sqrt{c^2 - a^2}$. This can be considered as a corollary of the pythagorean theorem.

(Ternas pitagóricas)
**Pythagorean triples**: groups of three counting numbers that can make the lengths of the sides of a right triangle. For example $3$, $4$, and $5$ are counting numbers that can build a right triangle because $5^2 = 3^2 + 4^2 = 25 = 9 + 16$. Multiples of a pythagorean triple are also pythagorean triples, for example $9$, $12$, and $15$, because $15^2 = 9^2 + 12^2 = 225 = 81 + 144$.

## Converse of the pythagorean theorem (Converso del teorema de Pitágoras)
[Ch08_S02](https://www.ck12.org/reader/reader-index.html#section/2932972/8.2/9549314)

In a triangle, if the longest side squared is equal to the sum of the other two sides squared, then the triangle is a right triangle, with the right angle being the angle opposite to the longest side.

> Proof of the converse of the pythagorean theorem
>
> Let $\triangle ABC$ have sides with lengths $a$, $b$, and $c$, and let $c^2 = a^2 + b^2$. $\triangle ABC$ is a right triangle with $\angle C$ being the right angle which is the angle opposite to $c$, because any right triangle $\triangle DEF$ with hypotenuse $c$ and legs $a$ and $b$ has $c^2 = a^2 + b^2$. $\blacksquare$

In a triangle $\triangle ABC$ with sides with lengths $a$, $b$, and $c$, if $c^2 = a^2 + b^2$, then $\triangle ABC$ is a right triangle with $\angle C$ being the right angle opposite to the side $c$.

(Teorema de identificación de triángulos agudos)
**Identification of acute triangles theorem**: in a triangle, if the longest side squared is less than the sum of the other two sides squared, then the triangle is an acute triangle.

> Proof of the identification of acute triangles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\triangle ABC$ have sides with lengths $a$, $b$, and $c$, let $c$ be the longest side, and $c^2 < a^2 + b^2$. Let $\triangle DEF$ be a right triangle with sides $a$, $b$, $f$, such that $f^2 = a^2 + b^2$. $c$ is opposite to $\angle C$ and $f$ is opposite to $\angle F$. $\angle F$ is a right angle | Given |
> | $c^2 < f^2$ | Transitive property of equality |
> | $c < f$ | Taking the square root of both sides preserves the inequality |
> | $m \angle C < m \angle F$ | Converse of the hinge theorem |
> | $m \angle C < \pi/2$ | Definition of right angle |
> | $m \angle C > m \angle A$ and $m \angle C > m \angle B$ | Triangle longer side theorem |
> | $\triangle ABC$ is an acute triangle | Definition of acute triangle |

In a triangle $\triangle ABC$ with sides with lengths $a$, $b$, and $c$, and $c$ being the longest side, if $c^2 < a^2 + b^2$, then $\triangle ABC$ is an acute triangle.

(Teorema de identificación de triángulos obtusos)
**Identification of obtuse triangles theorem**: in a triangle, if the longest side squared is greater than the sum of the other two sides squared, then the triangle is an obtuse triangle.

> Proof of the identification of obtuse triangles theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\triangle ABC$ have sides with lengths $a$, $b$, and $c$, let $c$ be the longest side, and $c^2 > a^2 + b^2$. Let $\triangle DEF$ be a right triangle with sides $a$, $b$, $f$, such that $f^2 = a^2 + b^2$. $c$ is opposite to $\angle C$ and $f$ is opposite to $\angle F$. $\angle F$ is a right angle | Given |
> | $c^2 > f^2$ | Transitive property of equality |
> | $c > f$ | Taking the square root of both sides preserves the inequality |
> | $m \angle C > m \angle F$ | Converse of the hinge theorem |
> | $m \angle C > \pi/2$ | Definition of right angle |
> | $\triangle ABC$ is an obtuse triangle | Definition of obtuse triangle |

In a triangle $\triangle ABC$ with sides with lengths $a$, $b$, and $c$, and $c$ being the longest side, if $c^2 > a^2 + b^2$, then $\triangle ABC$ is an obtuse triangle.

## Using similar right triangles (Usando triángulos rectángulos similares)
[Ch08_S03](https://www.ck12.org/reader/reader-index.html#section/2932973/8.3/9549314)

(Triángulos rectángulos inscritos similares)
**Inscribed similar right triangles**: right triangles inscribed inside other right triangles that are similar.
[Inscribed similar right triangles image code](Programs/Ch08/S03_01_Inscribed_similar_right_triangles_image.py)
![Inscribed similar right triangles image](Images/Ch08/S03_01_Inscribed_similar_right_triangles.png)
*Inscribed similar right triangles*

(Teorema de los triángulos rectángulos inscritos similares)
**Inscribed similar right triangles theorem**: Every right triangle has two inscribed similar triangles. To create them, draw the altitude from the right angle vertex, the resulting two triangles are similar to the original one.

> Proof of the inscribed similar right triangles theorem
>
> From the *Inscribed similar right triangles* image, $\triangle ABC \sim \triangle DAC \sim \triangle DBA$ because of the AA triangle similarity postulate. For $\triangle ABC \sim \triangle DAC$, $\angle BAC \cong \angle ADC$ and $\angle C \cong \angle C$. For $\triangle ABC \sim \triangle DBA$, $\angle BAC \cong \angle BDA$ and $\angle B \cong \angle B$. $\blacksquare$

In the right triangle $\triangle ABC$ with the right angle being $\angle A$, if the point $D$ is the point of the altitude from $\angle A$ that lies on $\overline{BC}$, then $\triangle ABC \sim \triangle DAC \sim \triangle DBA$.

(Media geométrica)
**Geometric mean**: a measure of central tendency of $n$ numbers, that consists in taking the $n$-th root of the product of the $n$ numbers.
[Geometric mean code](Programs/Ch08/S03_02_Geometric_mean.py)

> Definition of the geometric mean
>
> Let there be $n$ numbers, where $x_i$ is the $i$-number. Let $GM(x)$ be the geometric mean of the $n$ numbers, then
> $$GM(x) = \sqrt[n]{x_1 x_2 ... x_n}$$

The geometric mean $GM(x)$ is the number whose repeated multiplication is the same as the product $x_1 x_2 ... x_n$, so if the geometric mean replaced each number $x_i$, then the total product would be the same.

(Media geométrica en triángulos rectángulos)
**Geometric mean in right triangles**: there are at least three geometric means in a right triangle, the two legs and the altitude from the right angle are all geometric means of different segments.

To understand this, consider the definition of geometric mean applied to only two numbers. Let $GM$ be the geometric mean of $x_1$ and $x_2$, so $GM = \sqrt{x_1 x_2}$. Representing this equation as a proportion, $GM^2 = x_1 x_2$, then $\frac{GM}{x_2} = \frac{x_1}{GM}$, and reordering $\frac{x_1}{GM} = \frac{GM}{x_2}$. This shows the numbers $x_1$ and $x_2$ as the extremes of the proportion, and $GM$ as the means of the proportion.

Because of the inscribed similar right triangles theorem, in a right triangle $\triangle ABC$ with the right angle being $\angle A$, if the point $D$ is the point of the altitude from $\angle A$ that lies on $\overline{BC}$, then $\triangle ABC \sim \triangle DAC \sim \triangle DBA$. The altitude of $\triangle ABC$ is $\overline{AD}$.

From $\triangle DAC \sim \triangle DBA$, $\frac{BD}{AD} = \frac{AD}{CD}$, which shows that the altitude $\overline{AD}$ is the geometric mean of the segments divided by $D$ in $\overline{BC}$. From $\triangle ABC \sim \triangle DBA$, $\frac{BD}{AB} = \frac{AB}{BC}$, which shows that the leg $\overline{AB}$ is the geometric mean of the hypotenuse and the side of the hypotenuse cut by $D$ that is in the same side as the leg $\overline{AB}$. From $\triangle ABC \sim \triangle DAC$, $\frac{CD}{AC} = \frac{AC}{BC}$, which shows that the leg $\overline{AC}$ is the geometric mean of the hypotenuse and the side of the hypotenuse cut by $D$ that is in the same side as the leg $\overline{AC}$.

## Special right triangles (Triángulos rectángulos especiales)
[Ch08_S04](https://www.ck12.org/reader/reader-index.html#section/2932974/8.4/9549314)

## Tangent, sine and cosine (Tangente, seno y coseno)
[Ch08_S05](https://www.ck12.org/reader/reader-index.html#section/2932975/8.5/9549314)

## Inverse trigonometric ratios (Ratios trigonométricos inversos)
[Ch08_S06](https://www.ck12.org/reader/reader-index.html#section/2932976/8.6/9549314)

## Laws of sines and cosines (Leyes de senos y cosenos)
[Ch08_S07](https://www.ck12.org/reader/reader-index.html#section/2932977/8.7/9549314)