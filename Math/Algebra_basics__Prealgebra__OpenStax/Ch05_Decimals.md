
#   Decimals (Decimales)

<!--
#T# Table of contents

#C# Definitions of decimals (Definiciones de decimales)
#C# Decimal operations (Operaciones con decimales)
#C# Decimals and fractions (Decimales y fracciones)
#C# Solution of an equation with decimals (Solución de una ecuación con decimales)
#C# Averages, probability (Promedios, probabilidad)
#C# Ratios, rates (Ratios, tasas)
#C# Square roots, simplification of square roots (Raíces cuadradas, simplificación de raíces cuadradas)

#T# Beginning of content
-->

## Definitions of decimals (Definiciones de decimales)
[Ch05_S01](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=415)

(Decimales)
**Decimals**: the numeric representation of fractions in the place value system. Proper fractions have a value less than 1, to express them as decimals, the places to the right of the units place are used. The separation between the units place and the decimal places is commonly shown with a dot. For example, the numbers 0.1, 3.541, etc.

About their place value, the first place to the right of the dot has its value multiplied by 10 to the -1, the second place has its value multiplied by 10 to the -2, the third place to the -3, and so on.

(Decimales equivalentes)
**Equivalent decimals**: different decimal numbers that have the same value. For example $10.3$ has the same value as $10.30$, or $10.300$.

(Conversión entre decimales y fracciones)
**Conversion between decimals and fractions**: decimals can be presented in fraction form, and vice versa. The conversion from fraction to decimal is done by performing the division of the numerator over the denominator of the fraction. The conversion from finite decimal (see finite decimals in this file) to fraction is done by multiplying the decimal by 10 to the positive power of the place of the rightmost digit, and dividing the result over the same power of 10.
[Conversion decimal fraction code](Programs/Ch05/S01_01_Conversion_decimal_fraction.py)

(Redondeo de decimales)
**Decimal rounding**: like regular rounding.

## Decimal operations (Operaciones con decimales)
[Ch05_S02](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=434)

(Adición y sustracción de decimales)
**Addition and subtraction of decimals**: like regular addition and subtraction. When using decimals, the decimal places are added or subtracted correspondingly.

(Multiplicación y división de decimales)
**Multiplication and division of decimals**: like regular multiplication and division. When doing division, an infinite amount of decimal digits can appear. When doing multiplication, the amount of decimal digits is up to the sum of the decimal digits in the factors.

(Multiplicación y división por 10)
**Multiplication and division by 10**: given that 10 is the base of the decimal place value system, multiplying a number by 10 moves the number one digit to the left, while dividing a number by 10 moves the number one digit to the right. For example, $2 \cdot 10 = 20$, and $2 \div 10 = 0.2$.

## Decimals and fractions (Decimales y fracciones)
[Ch05_S03](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=453)

(Decimal finito)
**Finite decimal**: a decimal with a finite amount of digits after the decimal period.

(Decimal periódico)
**Repeating decimal**: a decimal in which a group of digits after the decimal period repeats itself indefinitely. They can be expressed as fractions and vice versa.
[Repeating decimals code](Programs/Ch05/S03_01_Repeating_decimals.py)

Repeating decimals are denoted with a horizontal bar over the digits that repeat. For example, in $\frac{8}{7} = 1.\overline{142857}$, the line over $142857$ indicates that it repeats itself infinitely many times.

(Conversión de decimal periódico a fracción)
**Conversion from repeating decimal to fraction**: The conversion from repeating decimal to fraction is done by creating two numbers, each of which is the product of the decimal by a different power of 10, and then subtracting both numbers and dividing that difference by the subtraction of said powers of 10 (See Programs/Ch05/S03_01_Repeating_decimals.py).

Repeating decimals have a few parts, for example, in the number $894.57448132653448132653448132653448132653448132653$, the unique part (parte única) is $894.57$, and the repeating part (parte periódica) is $448132653$. In itself, the unique part has two parts (as any decimal number), the decimal part and the integer part.

For the unique part $894.57$, the original number is multiplied by 10 to the positive power of the place of the rightmost digit of the unique part, in this case $10^2$. For the repeating part, the original number is multiplied by 10 to the power of the sum of the amount of repeating digits and the power of 10 used for the unique part (in this case $2$). The amount of digits in $448132653$ is $9$, so for the repeating part, the original number is multiplied by $10^{9 + 2} = 10^{11}$.

Now to subtract these two products, let $a = 894.57448132653448132653448132653448132653448132653$, so $a 10^2 = 89457.448132653448132653448132653448132653448132653$, and $a 10^{11} = 89457448132653.448132653448132653448132653448132653448132653$, therefore $a 10^{11} - a 10^2 = 89457448043196$, as can be seen, this subtraction results in an integer. Continuing, $a 10^{11} - a 10^2 = a (10^{11} - 10^2)$, so $a = \frac{89457448043196}{(10^{11} - 10^2)} = \frac{89457448043196}{99999999900}$.

(Círculo)
**Circle**: shape in which all of its points are at the same distance from its center.

(Radio de un círculo)
**Radius of a circle**: the distance from the center of a circle to any of its points.

(Diámetro de un círculo)
**Diameter of a circle**: the maximum possible distance between two points in a circle. This is the same as twice the radius.

(Circunferencia de un círculo)
**Circumference of a circle**: the measure of the distance around a circle, i.e. the distance covered by its points.

(La constante pi)
**The pi constant**: the fraction of the circumference over the diameter. It's represented with the greek letter pi, which is $\pi$. The value of pi is roughly $\pi = 3.14159...$, this is a non repeating decimal.

(Fórmula de la circunferencia)
**Circumference formula**: formula to find the length of the circumference of a circle from the length of its radius.

> Circumference formula
>
> Let $d$ be the diameter in length units, $r$ be the radius in length units, $C$ be the circumference in length units, then
>
> $$\begin{gathered}
> \pi := \frac{C}{d}\\
> d = 2 r\\
> C = \pi d = 2 \pi r
> \end{gathered}$$

(Sector circular)
**Circular sector**: a portion of a circle. A sector is originated from the intersection of two distinct radii segments and the circumference.

(Fórmula del área de un círculo)
**Circle area formula**: formula to find the area occupied by a circle, from the length of its radius.

> Circle area formula
>
> Let $A$ be the area of a circle in squared length units, $r$ be the radius in length units, then
> $$A = \pi r^2$$

This is because when dividing the circle in many small sectors, and then lining the circumference $C$ (measured in length units) to make a straight line, the result is half a rectangle of sides $C$ and $r$, so $A = \frac{C r}{2} = \frac{2 \pi r r}{2} = \pi r^2$.

(Aproximación fraccionaria de pi)
**Fractional approximation of pi**: there are infinitely many fractional approximations of pi, one of the simplest is $\frac{22}{7}$.

## Solution of an equation with decimals (Solución de una ecuación con decimales)
[Ch05_S04](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=467)

An equation with decimals can have a decimal solution, just like a regular solution.

## Averages, probability (Promedios, probabilidad)
[Ch05_S05](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=476)

(Promedios)
**Averages**: measures of the typical number in a set of numbers. A typical number is that which is most likely to appear from the set, or one that has a value in the middle of the values of the set. The measure of an average itself doesn't have to be part of the set of numbers, so a number that is not in the set, could be a representative value for said set.

(La media)
**The mean**: also called the arithmetic average (la media aritmética), it's the sum of a set of numbers divided by the size of the set.

> Definition of the mean
>
> Let $X$ be a set of $N$ numbers, $x_i$ be the $i$-th number in the set, $\bar{x}$ be the mean of the set, then
> $$\bar{x} = \frac{x_1 + x_2 + ... + x_i + ... + x_N}{N} = \sum_i{\frac{x_i}{N}}$$

The mean is the number $\bar{x}$ whose repeated addition with itself $N$ times results in the same value as the sum of the original values $\sum_i{x_i}$, so if the mean $\bar{x}$ replaced each number $x_i$, then the total sum would be the same.

(Mediana)
**Median**: the middle value in a set of numbers, such that half the numbers are greater than the median, and the other half is less than the median. After sorting the set, when the set contains an odd amount of numbers, the median is the value in the middle, and when the set has an even amount of numbers, the median is the mean of the two values in the middle.

(Frecuencia de un número en un conjunto)
**Frequency of a number in a set**: the amount of times a given number is repeated in a set.

(Moda)
**Mode**: the number with the highest frequency in a set. A set of numbers can have several modes if several numbers have the same highest frequency, or none if all the numbers have the same frequency.

(Probabilidad de un evento)
**Probability of an event**: the fraction of the number of times an event happens over the number of general outcomes with or without the event.

## Ratios, rates (Ratios, tasas)
[Ch05_S06](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=489)

(Ratio)
**Ratio**: a fraction of any two numbers that are measured with the same unit or scale, therefore ratios have no units themselves. For example the ratio of height to width, both are measured in distance.

The notation of ratios in particular, includes the use of the colon : symbol to replace the division symbol. So the ratio $\frac{a}{b}$ can be denoted as $a:b$. If $b = 1$ then the ratio is still presented as $\frac{a}{1}$, and if the ratio is an improper fraction, it is not converted to a mixed number.

(Elevación sobre avance de una pendiente)
**Rise over run of a slope**: in a slope, rise over run is the fraction of the vertical distance called "rise" over the horizontal distance called "run".

(Tasa)
**Rate**: a fraction of any two numbers that are measured in differente units or scales, so the unit of a rate is the fraction of the units. For example the rate of speed which is measured as a fraction of distance over time.

Ratios can be considered rates when the particular units in the numerator and denominator are also considered, even though they are the same. For example, width over height can be seen as a ratio, but also as the rate of width per unit of height, this rate is still dimensionless like a ratio.

(Tasa unitaria)
**Unit rate**: a rate expressed with a denominator of $1$.

(Precio unitario)
**Unit price**: a unit rate in which the unit is $\text{\textdollar}/unit$, it tells the price per unit.

## Square roots, simplification of square roots (Raíces cuadradas, simplificación de raíces cuadradas)
[Ch05_S07](../../../Libros/Mathematics/Algebra_basics__Prealgebra__OpenStax.pdf#page=502)

Simplification of square roots is done like regular simplification.
[Simplification of radicals code](Programs/Ch05/S07_01_Simplification_of_radicals.py)

(Signo de radical)
**Radical sign**: The symbol around $n$ in $\sqrt{n}$ is the radical sign, it acts as a grouping symbol for the expression inside it. $\sqrt{n} = n^{1/2}$, and $\sqrt[7]{n} = n^{1/7}$, in general $\sqrt[k]{n} = n^{1/k}$.

(Cuadrado perfecto)
**Perfect square**: any whole number that is the square of an integer. For example $9$ is the perfect square of $3$, because $3^2 = 9$ and $\sqrt{9} = 3$.

(Raíz cuadrada)
**Square root**: given two numbers $m$, $n$, such that $m = n^2$, then $n$ is the square root of $m$, $n = \sqrt{m}$. Squared numbers can be seen as squares in a 2D grid. Let $m$ be the area of a given square, then $n$ is the measure of its side's length.

(Raíz cuadrada principal)
**Principal square root**: since any square root can be negative or positive, because $n^2 = (-n)^2 = m$, so both $n$ and $-n$ are roots of $m$, only one is chosen as the square root of $m$, this is the positive value $n$, named the principal square root of $m$, $\sqrt{m}$ stands for $n$.

(Fórmula de tiempo en caída libre)
**Free fall time formula**: formula to find the fall time in a free fall scenario. The fall starts at a given height, and the time calculated by this formula is the time from the moment the fall starts, to the moment of reaching the ground.

> Free fall time formula
>
> Let $t$ be the fall time in time units, $h$ be the starting height in length units, $g$ be the standard gravity (gravedad estándar), then
> $$t = \sqrt{\frac{2 h}{g}}$$

The constant $g$ is measured as a rate, its units are length over squared time units (see Ch07_Real_numbers.md). When using feet and seconds, $g = 32 ft/s^2$, and when using meters and seconds $g = 9.81 m/s^2$. Using $g = 32 ft/s^2$, then $t = \sqrt{\frac{2 h}{32}} = \sqrt{\frac{h}{16}} = \frac{\sqrt{h}}{4}$, $h$ must be in feet, and $t$ is in seconds.

(Fórmula de la velocidad antes de frenar)
**Formula of the speed before braking**: formula to find the speed of a car before braking, from the length of the skid mark.

> Formula of the speed before braking
>
> Let $d$ be the skid mark distance in feet, $v$ be the speed of the car before braking in miles per hour, then
> $$v = \sqrt{24 d}$$