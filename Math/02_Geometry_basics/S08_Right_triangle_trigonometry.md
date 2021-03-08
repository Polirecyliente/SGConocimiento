
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

(Longitud del cateto en un triángulo rectángulo)
**Length of the leg in a right triangle**: in a right triangle with hypotenuse of length $c$, and legs of lengths $a$ and $b$, $a = \sqrt{c^2 - b^2}$, $b = \sqrt{c^2 - a^2}$. This can be considered as a corollary of the pythagorean theorem.

(Ternas pitagóricas)
**Pythagorean triples**: groups of three counting numbers that can make the lengths of the sides of a right triangle. For example $3$, $4$, and $5$ are counting numbers that can build a right triangle because $5^2 = 3^2 + 4^2 = 25 = 9 + 16$. Multiples of a pythagorean triple are also pythagorean triples, for example $9$, $12$, and $15$, because $15^2 = 9^2 + 12^2 = 225 = 81 + 144$.

## Converse of the pythagorean theorem (Converso del teorema de Pitágoras)

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

(Triángulos rectángulos inscritos similares)
**Inscribed similar right triangles**: right triangles inscribed inside other right triangles that are similar.
[Inscribed similar right triangles image code](Programs/S08/01_Inscribed_similar_right_triangles_image.py)
![Inscribed similar right triangles image](Images/S08/01_Inscribed_similar_right_triangles.png)
*Inscribed similar right triangles*

(Teorema de los triángulos rectángulos inscritos similares)
**Inscribed similar right triangles theorem**: Every right triangle has two inscribed similar triangles. To create them, draw the altitude from the right angle vertex, the resulting two triangles are similar to the original one.

> Proof of the inscribed similar right triangles theorem
>
> From the *Inscribed similar right triangles* image, $\triangle ABC \sim \triangle DAC \sim \triangle DBA$ because of the AA triangle similarity postulate. For $\triangle ABC \sim \triangle DAC$, $\angle BAC \cong \angle ADC$ and $\angle C \cong \angle C$. For $\triangle ABC \sim \triangle DBA$, $\angle BAC \cong \angle BDA$ and $\angle B \cong \angle B$. $\blacksquare$

In the right triangle $\triangle ABC$ with the right angle being $\angle A$, if the point $D$ is the point of the altitude from $\angle A$ that lies on $\overline{BC}$, then $\triangle ABC \sim \triangle DAC \sim \triangle DBA$.

(Media geométrica)
**Geometric mean**: a measure of central tendency of $n$ numbers, that consists in taking the $n$-th root of the product of the $n$ numbers.
[Geometric mean code](Programs/S08/02_Geometric_mean.py)

> Definition of the geometric mean
>
> Let there be $n$ numbers, where $x_i$ is the $i$-number. Let $GM(x)$ be the geometric mean of the $n$ numbers, then
> $$GM(x) = \sqrt[n]{x_1 x_2 ... x_n}$$

The geometric mean $GM(x)$ is the number whose repeated multiplication is the same as the product $x_1 x_2 ... x_n$, so if the geometric mean replaced each number $x_i$, then the total product would be the same.

(Media geométrica en triángulos rectángulos)
**Geometric mean in right triangles**: there are at least three geometric means in a right triangle, the two legs and the altitude from the right angle are all geometric means of different segments.

To understand this, consider the definition of geometric mean applied to only two numbers. Let $GM$ be the geometric mean of $x_1$ and $x_2$, so $GM = \sqrt{x_1 x_2}$. Representing this equation as a proportion, $GM^2 = x_1 x_2$, then $\frac{GM}{x_2} = \frac{x_1}{GM}$, and reordering $\frac{x_1}{GM} = \frac{GM}{x_2}$. This shows the numbers $x_1$ and $x_2$ as the extremes of the proportion, and $GM$ as the means of the proportion.

Because of the inscribed similar right triangles theorem, in a right triangle $\triangle ABC$ with the right angle being $\angle A$, if the point $D$ is the point of the altitude from $\angle A$ that lies on $\overline{BC}$, then $\triangle ABC \sim \triangle DAC \sim \triangle DBA$. The altitude of $\triangle ABC$ is $\overline{AD}$ (see the *Inscribed similar right triangles* image).

From $\triangle DAC \sim \triangle DBA$, $\frac{BD}{AD} = \frac{AD}{CD}$, which shows that the altitude $\overline{AD}$ is the geometric mean of the segments divided by $D$ in $\overline{BC}$. From $\triangle ABC \sim \triangle DBA$, $\frac{BD}{AB} = \frac{AB}{BC}$, which shows that the leg $\overline{AB}$ is the geometric mean of the hypotenuse and the side of the hypotenuse cut by $D$ that is in the same side as the leg $\overline{AB}$. From $\triangle ABC \sim \triangle DAC$, $\frac{CD}{AC} = \frac{AC}{BC}$, which shows that the leg $\overline{AC}$ is the geometric mean of the hypotenuse and the side of the hypotenuse cut by $D$ that is in the same side as the leg $\overline{AC}$.

## Special right triangles (Triángulos rectángulos especiales)

(Triángulo rectángulo isósceles)
**Isosceles right triangle**: a right triangle with congruent legs. Because of this definition, the three angles are always the same, $\pi/2$ for the right angle, and $\pi/4$ and $\pi/4$ for the base angles, so all isosceles right triangles are similar.
[Isosceles right triangle image code](Programs/S08/03_Isosceles_right_triangle_image.py)
![Isosceles right triangle image](Images/S08/03_Isosceles_right_triangle.png)
*Isosceles right triangle*

(Hipotenusa de un triángulo rectángulo isósceles)
**Hypotenuse of an isosceles right triangle**: the length of the legs $l$ is the same for both legs. The length of the hypotenuse is $h = \sqrt{2} l$.

> Hypotenuse of an isosceles right triangle
>
> Let an isosceles right triangle have an hypotenuse with length $h$ and legs with length $l$. By the pythagorean theorem $h^2 = l^2 + l^2 = 2 l^2$, so $h = \sqrt{2 l^2} = \sqrt{2} l$.

(Triángulo 30 60 90)
**30-60-90 triangle**: a right triangle with angles of 30, 60 and 90 degrees (or $\pi/6$, $\pi/3$ and $\pi/2$ in radians). Because of this definition, a 30-60-90 triangle can be seen as an equilateral triangle cut by an altitude in half.
[30-60-90 triangle image code](Programs/S08/04_30-60-90_triangle_image.py)
![30-60-90 triangle image](Images/S08/04_30-60-90_triangle.png)
*30-60-90 triangle*

(Lados de un triángulo 30 60 90)
**Sides of a 30-60-90 triangle**: all the lengths of the sides in a 30-60-90 triangle can be known from the hypotenuse.

> Sides of a 30-60-90 triangle
>
> In a 30-60-90 triangle, let $h$ be the length of the hypotenuse, which is the side opposite to the 90 degrees angle. Let $l_1$ be the length of the smaller leg, which is the side opposite to the 30 degrees angle, and let $l_2$ be the length of the longer leg, which is the side opposite to the 60 degrees angle. To find $l_1$, consider that it is half the side of the equilateral triangle that contains the 30-60-90 triangle, so
> $$l_1 = \frac{h}{2}$$
>
> Now, by the pythagorean theorem
>
> $$\begin{gathered}
h^2 = {l_1}^2 + {l_2}^2\\
l_2 = \sqrt{h^2 - {l_1}^2}\\
l_2 = \sqrt{h^2 - {\frac{h}{2}}^2}\\
l_2 = \sqrt{h^2 - \frac{h^2}{4}}\\
l_2 = \sqrt{\frac{3}{4} h^2}\\
l_2 = \frac{\sqrt{3}}{2} h
\end{gathered}$$

In a 30-60-90 triangle, given $h$ as the length of the hypotenuse, $l_1$ as the length opposite to the 30 degrees angle, and $l_2$ as the length opposite to the 60 degress angle, then $l_1 = \frac{h}{2}$, and $l_2 = \frac{\sqrt{3}}{2} h$.

## Tangent, sine and cosine (Tangente, seno y coseno)

(Ratios trigonométricos en un triángulo rectángulo)
**Trigonometric ratios in a right triangle**: ratios specifically created with the lengths of the sides of right triangles. These ratios change by varying the non-right angles in the right triangle. Given that a right triangle only has three sides, there are only three basic ratios possible between pairs of the three sides.
[Trigonometric ratios in a right triangle image code](Programs/S08/05_Trigonometric_ratios_in_a_right_triangle_image.py)
![Trigonometric ratios in a right triangle image](Images/S08/05_Trigonometric_ratios_in_a_right_triangle.png)
*Trigonometric ratios in a right triangle*

The trigonometric ratios can be calculated programatically.
[Trigonometric ratios code](Programs/S08/06_Trigonometric_ratios.py)

(Lado adyacente y lado opuesto a un ángulo en un triángulo rectángulo)
**Adjacent side and opposite side to an angle in a right triangle**: every right triangle has two non-right angles. Each of these two non-right angles has an adjacent side and an opposite side. The opposite side is the regular opposite side of an angle in a triangle. The adjacent side is the side of the angle that is not the hypotenuse.

(Ratios trigonométricos de cualquier ángulo)
**Trigonometric ratios of any angle**: in a right triangle, the non-right angles are always acute, but the trigonometric ratios can still be measured in non-acute angles. For this, the angle is put in the rectangular coordinate system. Because of the definition of an angle, any point in the angle side always falls in one of the four quadrants of the rectangular coordinate system. A right angle is built in that quadrant, using as hypotenuse the segment from the origin to a point in the angle, and using as legs the $x$ and $y$ projections of the point on the rectangular coordinate system, and the trigonometric ratios of the angle are determined using that right triangle (this also works for acute angles).
[Trigonometric ratios of any angle image code](Programs/S08/07_Trigonometric_ratios_of_any_angle_image.py)
![Trigonometric ratios of any angle image](Images/S08/07_Trigonometric_ratios_of_any_angle.png)
*Trigonometric ratios of any angle*

(Racionalizar el denominador)
**Rationalize the denominator**: when a fraction has a radical in the denominator, it can be rationalized to remove the radical from the denominator without changing the value of the fraction. The process is $\frac{a}{\sqrt{b}} = \frac{a \sqrt{b}}{\sqrt{b} \sqrt{b}} = \frac{a \sqrt{b}}{b}$.

(Seno de un ángulo)
**Sine of an angle**: placing an angle in a right triangle, its sine is defined as the ratio of the opposite side over the hypotenuse.

> Definition of the sine of an angle
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the sines of the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
sin(\angle B) = \frac{b}{a}\\
sin(\angle C) = \frac{c}{a}
\end{gathered}$$

$sin$ is called the sine function.

(Coseno de un ángulo)
**Cosine of an angle**: placing an angle in a right triangle, its cosine is defined as the ratio of the adjacent side over the hypotenuse.

> Definition of the cosine of an angle
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the cosines of the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
cos(\angle B) = \frac{c}{a}\\
cos(\angle C) = \frac{b}{a}
\end{gathered}$$

$cos$ is called the cosine function.

(Tangente de un ángulo)
**Tangent of an angle**: placing an angle in a right triangle, its tangent is defined as the ratio of the opposite side over the adjacent side.

> Definition of the tangent of an angle
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the tangents of the non-right $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
tan(\angle B) = \frac{b}{c}\\
tan(\angle C) = \frac{c}{b}
\end{gathered}$$

$tan$ is called the tangent function.

(Lados de un triángulo rectángulo dado un ángulo y un lado)
**Sides of a right triangle given an angle and a side**: In a right triangle, having only one of the non-right angles and the length of any one side, is enough to determine the lengths of the other two sides, via the trigonometric ratios.

> Sides of a right triangle given an angle and a side
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the sides of the right triangle can be found in the following manners (see the *Trigonometric ratios in a right triangle* image)
>
> Having $a$ and $m \angle B$
>
> $$\begin{gathered}
b = a\ sin(\angle B)\\
c = a\ cos(\angle B)
\end{gathered}$$
>
> Having $a$ and $m \angle C$
>
> $$\begin{gathered}
b = a\ cos(\angle C)\\
c = a\ sin(\angle C)
\end{gathered}$$
>
> Having $b$ and $m \angle B$
>
> $$\begin{gathered}
a = \frac{b}{sin(\angle B)}\\
c = \frac{b}{tan(\angle B)}
\end{gathered}$$
>
> Having $b$ and $m \angle C$
>
> $$\begin{gathered}
a = \frac{b}{cos(\angle C)}\\
c = b\ tan(\angle C)
\end{gathered}$$
>
> Having $c$ and $m \angle B$
>
> $$\begin{gathered}
a = \frac{c}{cos(\angle B)}\\
b = c\ tan(\angle B)
\end{gathered}$$
>
> Having $c$ and $m \angle C$
>
> $$\begin{gathered}
a = \frac{c}{sin(\angle C)}\\
b = \frac{c}{tan(\angle C)}
\end{gathered}$$

(Ángulo de depresión)
**Angle of depression**: an angle measured below a horizontal line.

(Ángulo de elevación)
**Angle of elevation**: an angle measured above a horizontal line.

## Inverse trigonometric ratios (Ratios trigonométricos inversos)

Given a right triangle in which the lengths of two sides are known, the non-right angles can be calculated using the inverse of the trigonometric ratios. The inverse of the trigonometric ratio is a function that returns the angle needed to originate the ratio of the two sides of the right triangle. So, to calculate the inverse of a trigonometric ratio, the lengths of two sides of a right triangle are needed.
[Inverse of the trigonometric ratios code](Programs/S08/08_Inverse_of_the_trigonometric_ratios.py)

(Seno inverso | arcoseno)
**Inverse sine | arcsine**: a function that returns the angle that creates a given sine ratio, i.e. the angle that creates a given ratio of opposite side to the angle over the hypotenuse, in a right triangle.

> Definition of the inverse sine of a ratio
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the arcsines that return the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
m \angle B = sin^{-1}\left(\frac{b}{a}\right)\\
m \angle C = sin^{-1}\left(\frac{c}{a}\right)
\end{gathered}$$

$sin^{-1}$ is the inverse sine, or arcsine function.

(Coseno inverso | arcocoseno)
**Inverse cosine | arccosine**: a function that returns the angle that creates a given cosine ratio, i.e. the angle that creates a given ratio of adjacent side to the angle over the hypotenuse, in a right triangle.

> Definition of the inverse cosine of a ratio
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the arccosines that return the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
m \angle B = cos^{-1}\left(\frac{c}{a}\right)\\
m \angle C = cos^{-1}\left(\frac{b}{a}\right)
\end{gathered}$$

$cos^{-1}$ is the inverse cosine, or arccosine function.

(Tangente inversa | arcotangente)
**Inverse tangent | arctangent**: a function that returns the angle that creates a given tangent ratio, i.e. the angle that creates a given ratio of opposite side over adjacent side of the angle, in a right triangle.

> Definition of the inverse tangent of a ratio
>
> In a right triangle $\triangle ABC$ with the right angle being $\angle A$, making $a = BC$, $b = AC$, and $c = AB$, the arctangents that return the non-right angles $\angle B$ and $\angle C$, are (see the *Trigonometric ratios in a right triangle* image)
>
> $$\begin{gathered}
m \angle B = tan^{-1}\left(\frac{b}{c}\right)\\
m \angle C = tan^{-1}\left(\frac{c}{b}\right)
\end{gathered}$$

$tan^{-1}$ is the inverse tangent, or arctangent function.

## Laws of sines and cosines (Leyes de senos y cosenos)

(Resolver un triángulo)
**Solve a triangle**: determining the measures of the three sides and the three angles of a given triangle.

(Ley de senos)
**Law of sines**: In a triangle, the three ratios of the sine of each angle over the length of the opposite side to the angle, are equal.
[Law of sines image code](Programs/S08/09_Law_of_sines_image.py)
![Law of sines image](Images/S08/09_Law_of_sines.png)
*Law of sines*

> Proof of the law of sines
>
> Let there be a triangle $\triangle ABC$, such that $a = BC$, $b = AC$, and $c = AB$. Let $D_1$ be the point in the altitude from $C$ that lies in $\overline{AB}$, and let $D_2$ be the point in the altitude from $B$ that lies in $\overline{AC}$. Let $h_1 = CD_1$, and $h_2 = BD_2$.
>
> Because of the definition of the sine of an angle, $h_1 = b\ sin(\angle A)$ and $h_1 = a\ sin(\angle B)$, so $b\ sin(\angle A) = a\ sin(\angle B)$, therefore $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b}$. On the other hand, $h_2 = c\ sin(\angle A)$ and $h_2 = a\ sin(\angle C)$, so $c\ sin(\angle A) = a\ sin(\angle C)$, therefore $\frac{sin(\angle A)}{a} = \frac{sin(\angle C)}{c}$. By transitivity, $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b} = \frac{sin(\angle C)}{c}$. $\blacksquare$

In a triangle $\triangle ABC$, making $a = BC$, $b = AC$, and $c = AB$, $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b} = \frac{sin(\angle C)}{c}$.

(Ley de senos en triángulos obtusos)
**Law of sines in obtuse triangles**: the law of sines can be used to calculate the measure of obtuse angles. Because of the definitions of the trigonometric ratios, the trigonometric ratios of an obtuse angle are calculated using its supplement instead, which is an acute angle that allows building a right triangle. So when using the law of sines to determine an obtuse angle, the result should be corrected by calculating the supplement of the result, this yields the measure of the obtuse angle.
[Law of sines in obtuse triangles image code](Programs/S08/10_Law_of_sines_in_obtuse_triangles_image.py)
![Law of sines in obtuse triangles image](Images/S08/10_Law_of_sines_in_obtuse_triangles.png)
*Law of sines in obtuse triangles*

> Law of sines in obtuse triangles
>
> To prove that the law of sines in obtuse triangles, when used to calculate the measure of the obtuse angle, results in the measure of the acute supplementary angle, let $\triangle ABC$ be an obtuse triangle, with $\angle A$ being the obtuse angle. The objective is to determine $m \angle A$. Notice that $\frac{sin(\angle A)}{a} = \frac{sin(\angle B)}{b}$. Extending $\overline{AB}$ leads to $A_{supp}$, which is the point where $A_{supp}C = b$. From this, it can be visualized that $\frac{sin(\angle A_{supp})}{a} = \frac{sin(\angle B)}{b}$, and by transitivity $\frac{sin(\angle A_{supp})}{a} = \frac{sin(\angle A)}{a}$, so $sin(\angle A_{supp}) = sin(\angle A)$. Also, $\angle A_{supp}$ and $\angle A$ are supplementary because of the base angles theorem. In the end, the law of sines has no way to distinguish between the measure of an obtuse angle and the measure of its acute supplement, so to find the measure of the obtuse angle, the acute angle result must be corrected as $m \angle A = \pi - m \angle A_{supp}$.

In a triangle $\triangle ABC$ where the obtuse angle is $\angle A$, calculating $m \angle A$ with the law of sines results in $m \angle A_{supp}$, this is corrected as $m \angle A = \pi - m \angle A_{supp}$.

(Ley de cosenos)
**Law of cosines**: in a triangle, the squared length of a side, is equal to the sum of the other two sides, each squared, minus twice the product of the other two sides times the cosine of the opposite angle to the original side.
[Law of cosines image code](Programs/S08/11_Law_of_cosines_image.py)
![Law of cosines image](Images/S08/11_Law_of_cosines.png)
*Law of cosines*

> Proof of the law of cosines
>
> In a triangle $\triangle ABC$, let $a = BC$, $b = AC$, and $c = AB$, let $D$ be the point in the altitude from $C$ that lies on $\overline{AB}$, let $h = CD$.
>
> The idea is to isolate $a$, in function of $b$, $c$, and $\angle A$. For this, because of the pythagorean theorem, $a^2 = h^2 + BD^2$. $h = b\ sin(\angle A)$, $BD = c - AD$, $AD = b\ cos(\angle A)$, so $BD = c - b\ cos(\angle A)$, and so $a^2 = (b\ sin(\angle A))^2 + (c - b\ cos(\angle A))^2 = b^2\ sin^2(\angle A) + c^2 - 2bc\ cos(\angle A) + b^2\ cos^2(\angle A)$. Because $sin^2 x + cos^2 x = 1$ for any angle $x$, then $a^2 = b^2 (sin^2(\angle A) + cos^2(\angle A)) + c^2 - 2bc\ cos(\angle A) = b^2 + c^2 - 2bc\ cos(\angle A)$. The same proof can be applied to determine the other two sides. $\blacksquare$

In a triangle $\triangle ABC$, making $a = BC$, $b = AC$, and $c = AB$, the law of cosines is $a^2 = b^2 + c^2 - 2bc\ cos(\angle A)$, $b^2 = a^2 + c^2 - 2ac\ cos(\angle B)$, and $c^2 = a^2 + b^2 - 2ab\ cos(\angle C)$.