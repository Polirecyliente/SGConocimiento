
#   Real numbers (Números reales)

<!--
#T# Table of contents

#C# Definitions of decimals (Definiciones de decimales)
#C# Decimal operations (Operaciones con decimales)
#C# Decimals and fractions (Decimales y fracciones)
#C# Solution of an equation with decimals (Solución de una ecuación con decimales)
#C# Averages, probability (Promedios, probabilidad)
#C# Ratios, rates (Ratios, tasas)
#C# Square roots, simplification of square roots (Raíces cuadradas, simplificación de raíces cuadradas)

#C# Definitions of percents (Definiciones de porcentajes)
#C# Percentage applications (Aplicaciones de porcentajes)
#C# Sales tax, commissions, discounts (Impuesto de ventas, comisiones, descuentos)
#C# Simple interest (Interés simple)
#C# Proportions (Proporciones)

#C# Rational and irrational numbers (Números racionales e irracionales)
#C# Associative properties (Propiedades asociativas)
#C# Distributive property (Propiedad distributiva)
#C# Inverse properties, zero properties (Propiedades inversas, propiedades del cero)
#C# Systems of measurement (Sistemas de medida)

#T# Beginning of content
-->

#   Decimals (Decimales)

## Definitions of decimals (Definiciones de decimales)

(Decimales)
**Decimals**: the numeric representation of fractions in the place value system. Proper fractions have a value less than 1, to express them as decimals, the places to the right of the units place are used. The separation between the units place and the decimal places is commonly shown with a dot. For example, the numbers 0.1, 3.541, etc.

About their place value, the first place to the right of the dot has its value multiplied by 10 to the -1, the second place has its value multiplied by 10 to the -2, the third place to the -3, and so on.

(Decimales equivalentes)
**Equivalent decimals**: different decimal numbers that have the same value. For example $10.3$ has the same value as $10.30$, or $10.300$.

(Conversión entre decimales y fracciones)
**Conversion between decimals and fractions**: decimals can be presented in fraction form, and vice versa. The conversion from fraction to decimal is done by performing the division of the numerator over the denominator of the fraction. The conversion from finite decimal (see finite decimals in this file) to fraction is done by multiplying the decimal by 10 to the positive power of the place of the rightmost digit, and dividing the result over the same power of 10.
[Conversion decimal fraction code](Programs/S05/Conversion_decimal_fraction.py)

(Redondeo de decimales)
**Decimal rounding**: like regular rounding.

## Decimal operations (Operaciones con decimales)

(Adición y sustracción de decimales)
**Addition and subtraction of decimals**: like regular addition and subtraction. When using decimals, the decimal places are added or subtracted correspondingly.

(Multiplicación y división de decimales)
**Multiplication and division of decimals**: like regular multiplication and division. When doing division, an infinite amount of decimal digits can appear. When doing multiplication, the amount of decimal digits is up to the sum of the decimal digits in the factors.

(Multiplicación y división por 10)
**Multiplication and division by 10**: given that 10 is the base of the decimal place value system, multiplying a number by 10 moves the number one digit to the left, while dividing a number by 10 moves the number one digit to the right. For example, $2 \cdot 10 = 20$, and $2 \div 10 = 0.2$.

## Decimals and fractions (Decimales y fracciones)

(Decimal finito)
**Finite decimal**: a decimal with a finite amount of digits after the decimal period.

(Decimal periódico)
**Repeating decimal**: a decimal in which a group of digits after the decimal period repeats itself indefinitely. They can be expressed as fractions and vice versa.
[Repeating decimals code](Programs/S05/Repeating_decimals.py)

Repeating decimals are denoted with a horizontal bar over the digits that repeat. For example, in $\frac{8}{7} = 1.\overline{142857}$, the line over $142857$ indicates that it repeats itself infinitely many times.

(Conversión de decimal periódico a fracción)
**Conversion from repeating decimal to fraction**: The conversion from repeating decimal to fraction is done by creating two numbers, each of which is the product of the decimal by a different power of 10, and then subtracting both numbers and dividing that difference by the subtraction of said powers of 10.

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

An equation with decimals can have a decimal solution, just like a regular solution.

## Averages, probability (Promedios, probabilidad)

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

Simplification of square roots is done like regular simplification.
[Simplification of radicals code](Programs/S05/Simplification_of_radicals.py)

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

The constant $g$ is measured as a rate, its units are length over squared time units. When using feet and seconds, $g = 32 ft/s^2$, and when using meters and seconds $g = 9.81 m/s^2$. Using $g = 32 ft/s^2$, then $t = \sqrt{\frac{2 h}{32}} = \sqrt{\frac{h}{16}} = \frac{\sqrt{h}}{4}$, $h$ must be in feet, and $t$ is in seconds.

(Fórmula de la velocidad antes de frenar)
**Formula of the speed before braking**: formula to find the speed of a car before braking, from the length of the skid mark.

> Formula of the speed before braking
>
> Let $d$ be the skid mark distance in feet, $v$ be the speed of the car before braking in miles per hour, then
> $$v = \sqrt{24 d}$$

#   Percents

## Definitions of percents (Definiciones de porcentajes)

(Porcentaje)
**Percent**: ratio with a denominator of 100. A percent number is identified with the percent sign $\%$ after it. For example $54\%$ means the ratio $\frac{54}{100}$.

(Conversión entre porcentajes y decimales, y entre porcentajes y fracciones)
**Conversion between percents and decimals, and between percents and fractions**: the conversion from percent to fraction and decimal uses the definition of percent. Given that a percent is a ratio with denominator 100, the fraction is the percent number over 100, and the decimal is the result of the division of said fraction. For example, $54\%$ as a fraction is $\frac{54}{100}$, and as a decimal is $0.54$.

The conversion from decimal or fraction to percent is based on equivalent fractions. The decimal is converted to a fraction, and the fraction is converted to an equivalent fraction with a denominator of 100. For example the decimal $0.6$ as a fraction is $\frac{6}{10} = \frac{3}{5}$, and then as an equivalent fraction $\frac{3}{5} = \frac{3 \cdot 20}{5 \cdot 20} = \frac{60}{100} = 60\%$.

A decimal can be converted directly to a percent, by multiplying it for $100$, e.g. $0.6 = 0.6 \cdot 100 \% = 60\%$. The opposite consists in dividing a percent by $100$ to obtain its decimal form.

When handling improper fractions, the resulting percent is greater than $100\%$, for example $\frac{5}{4} = 1.25 = 1.25 \cdot 100\% = 125\%$.

## Percentage applications (Aplicaciones de porcentajes)

(Ecuación de porcentaje)
**Percentage equation**: an equation that defines a percent. To define a percent, two concepts are needed, the base (la base) and the amount (la cantidad). The base is the number that represents the whole, and the amount is the number that represents the part or fraction of that whole.

> Parts of a percentage equation
>
> Let $p\%$ be a percent, $B$ be the base, $A$ be the amount, then
> $$A = p\% \cdot B$$

If $p < 100$, then $A < B$, which means that $A$ is a fraction of $B$.

Isolating the base allows finding its value from the amount and the percent, $B = \frac{A}{p\%}$.

The reciprocal of a percent, $\frac{1}{p\%}$, means the reciprocal of a ratio. If a percent $p\%$ means the part over the total, i.e. there are $p$ part units per group of $100$ total units, then $\frac{1}{p\%}$ means that there are $100$ total units per group of $p$ part units.

Isolating the percent allows finding its value from the amount and the base, $p\% = \frac{A}{B}$.

(Porcentaje de aumento, porcentaje de disminución)
**Percent increase, percent decrease**: in general, the percent change (porcentaje de cambio) from a variable is measured as the difference of final value minus initial value, divided over the initial value, this result tells the amount of units changed per group of $1$ unit before change, and this can be converted to a percent.

> Percent change notation
>
> Let $V_i$ be the initial value of a given variable, $V_f$ be the final value of said variable, $\Delta p\%$ be the percent change, then
> $$\Delta p\% = \frac{V_f - V_i}{V_i} 100\%$$

Note that the words "initial" and "final" do not have to mean that they are separated in time, they can be separated under any criteria wanted.

Given that $V_f$ can be smaller or bigger than $V_i$, $\Delta p\%$ can be negative or positive, if it's negative then that means that the percent change is a percent decrease, whereas if it's positive then that means that the percent change is a percent increase.

## Sales tax, commissions, discounts (Impuesto de ventas, comisiones, descuentos)

(Impuesto de ventas)
**Sales tax**: percent applied to the price of a good or service (bien o servicio), the resulting amount of which is paid as taxes.

> Price with sales tax formula
>
> Let $P_i$ be the price before taxes in monetary units, $P$ be the price with sales tax in monetary units, and $t$ be the sales tax as a ratio, then
> $$P = P_i + t P_i$$

The term $t P_i$ is hold as taxes by businesses, and then paid to the government.

(Comisión por ventas)
**Sales commission**: extra wage paid to a sales person for the value sold by them.

> Basic commission formula
>
> Let $C$ be the commission earned by the sales person in monetary units, $P$ be the sales value of the goods or services sold in monetary units, and $c$ be the commission rate (tasa de comisión) as a ratio, then
> $$C = c P$$

The commission rate $c$ is commonly expressed as a percent, which means the percent of each monetary unit sold that becomes commission.

(Descuento de precio)
**Price discount**: reduction in the price of a good or service, to make it more attractive for clients to buy.

> Basic discount formula
>
> Let $D$ be the amount of discount in monetary units, $P_i$ be the regular price in monetary units, $P$ be the price after discount in monetary units, $d$ be the discount rate (tasa de descuento) as a ratio, then
>
> $$\begin{gathered}
> D = d P_i\\
> P = P_i - D = P_i - d P_i
> \end{gathered}$$

The discount rate $d$ is commonly expressed as a percent, which means the percent of each monetary unit of the price that becomes discounted.

(Margen de ganancia)
**Mark-up**: retailers buy goods at a wholesale price (precio mayorista), and then resell said goods at a list price (precio de lista | precio sugerido). Their profit comes from the mark-up which is the extra price added to the wholesale price to obtain the list price.

> Basic mark-up formula
>
> Let $W$ be the wholesale price of a good in monetary units, $M$ be the amount of mark-up in monetary units, $L$ be the list price in monetary units, and $m$ be the mark-up rate as a ratio, then
>
> $$\begin{gathered}
> M = m W\\
> L = W + M = W + m W
> \end{gathered}$$

The mark-up rate is commonly expressed as a percent, which means the percent of each monetary unit of the wholesale price that becomes mark-up.

## Simple interest (Interés simple)

The simple interest is a way to calculate the amount of interest to be received for an investment or paid for a loan.

(Principal de una inversión)
**Investment principal**: the amount of money put into an investment.

(Principal de un préstamo)
**Loan principal**: the amount of money borrowed as a loan.

(Interés financiero)
**Financial interest**: money received in return for an investment, or paid for a loan.

(Fórmula del interés simple)
**Simple interest formula**: formula to calculate the simple interest from the loan principal, the interest rate, and the time elapsed since the loan started.

> Simple interest formula
>
> Let $P$ be the principal of the investment or loan in monetary units, $I$ be the amount of interest in monetary units, $t$ be the time elapsed since the moment of the investment or loan in time units, and $r$ be the interest rate (tasa de interés) paid per period as a ratio, then
> $$I = Prt$$

## Proportions (Proporciones)

(Proporción)
**Proportion**: an equation in which two fractions (ratios or rates) are equated.

> Proportion
>
> Let $a$, $b$, $c$, $d$, be numbers, with $b$ and $d$ being nonzero, then
> $$\frac{a}{b} = \frac{c}{d}$$
> This is a proportion, it's read as $a$ is to $b$ as $c$ is to $d$ ($a$ es a $b$ como $c$ es a $d$).

(Producto cruzado)
**Cross product**: a proportion where the denominators have been multiplied in both sides, i.e. in the proportion $\frac{a}{b} = \frac{c}{d}$, the cross product is $ad = bc$. This concept is used to test if a proportion is true without dividing.

(Proporción con porcentajes)
**Percent proportion**: a proportion in which one of the fractions is a percentage. Using terms from before, let $B$ be the base, $A$ the amount, then $\frac{A}{B} = \frac{p}{100}$, this means that the amount $A$ is to the base $B$ as $p$ is to $100$.

#   Real numbers (Números reales)

## Rational and irrational numbers (Números racionales e irracionales)

(Números racionales)
**Rational numbers**: the set of numbers that can be represented via fractions. This is an ordered set in which the relational operators can be used to compare the values of two rational numbers.

Rational numbers when represented as decimals, have their decimal part with a finite amount of digits, or if the amount is infinite then it repeats itself, which means that a decimal number that is rational can always be represented as a fraction.

(Números irracionales)
**Irrational numbers**: the set of numbers such as $\pi$, in which the decimal part of the number is infinite and never repeats itself. The square root of numbers that are not perfect squares is also irrational.

The fact that they are called irrational, doesn't necessarily mean that they can't have predictable patterns, for example, a number such as $0.101001000100001000001...$ is irrational by definition, but it can be understood as the number with a $1$ in between a steady growing number of $0$s. This pattern is infinite and never repeats itself, so it's an irrational number.

(Números reales)
**Real numbers**: the union of the sets of rational and irrational numbers.

## Associative properties (Propiedades asociativas)

(Propiedad asociativa de la adición)
**Associative property of addition**: using grouping symbols to group addition operations does not change the sum.

> Associative property of addition
>
> Let $a$, $b$, $c$ be numbers, then
> $$a + b + c = (a + b) + c = a + (b + c)$$

(Propiedad asociativa de la multiplicación)
**Associative property of multiplication**: using grouping symbols to group multiplication operations does not change the product.

> Associative property of multiplication
>
> Let $a$, $b$, $c$ be numbers, then
> $$a b c = (a b) c = a (b c)$$

## Distributive property (Propiedad distributiva)

(Propiedad distributiva de la multiplicación respecto a la suma)
**Distributive property of multiplication over addition**: when a group of addends (grouped using a grouping symbol) is multiplied by a number, it's the same as the sum of the products of said number by each addend.

> Distributive property
>
> Let $a$, $b$, $c$ be numbers, then
> $$a (b + c) = a b + a c$$

This property shows itself when multiplying $a$ by the sum $b + c$, the resulting product can be seen as the sum of $a b$ and $a c$. This property actually includes subtraction as a case of the sum, given that the addends can be negative numbers.

## Inverse properties, zero properties (Propiedades inversas, propiedades del cero)

(Inverso aditivo)
**Additive inverse**: the opposite of a number, is its additive inverse. The additive inverse of a number $a$ is $-a$.

(Propiedad inversa aditiva)
**Inverse property of addition**: the sum of a number and its additive inverse is zero.

> Inverse property of addition
>
> Let $a$ be a number, then
> $$a + (-a) = a - a = 0$$

$0$ is the additive identity.

(Inverso multiplicativo)
**Multiplicative inverse**: the reciprocal of a number, is its multiplicative inverse. The multiplicative inverse of a number $a$ is $\frac{1}{a}$.

(Propiedad inversa de la multiplicación)
**Inverse property of multiplication**: the product of a number and its multiplicative inverse is one.

> Inverse property of multiplication
>
> Let $a$ be a number, then
> $$a \frac{1}{a} = 1$$

$1$ is the multiplicative identity.

(Multiplicación por 0)
**Multiplication by 0**: the product of any number and 0 is 0.

> Multiply a number by 0
>
> Let $a$ be a number, then
> $$a \cdot 0 = 0$$

This is because $a$ is added $0$ times with itself.

## Systems of measurement (Sistemas de medida)

The systems of measurement are systems intended to be internally consistent, to provide a unit of measure for any physical quantity. The main quantities measured in these systems are time and space (time, distance, area, volume), derived quantities are also included like speed (distance divided by time), and also units of measure for other quantities, like electric field, radiation levels, etcetera.

There are two main systems of measurement used at the time of this writing, the U.S. system and the international metric system.

(Sistema anglosajón de unidades)
**United States customary units**: system of measurement with units for length, volume, weight, time, and more.

The following table contains a few of the units of the United States customary units system of measurement. Inside parentheses appears the abbreviation of each unit of measure.

| United States customary units      | Sistema anglosajón de unidades |
| :--------------------------------: | :----------------------------: |
| **Length**                         | **Longitud**                   |
| 1 foot (ft) = 12 inches (in)       | 1 pie = 12 pulgadas            |
| 1 yard (yd) = 3 feet (ft)          | 1 yarda = 3 pies               |
| 1 mile (mi) = 5280 feet (ft)       | 1 milla = 5280 pies            |
| **Volume**                         | **Volumen**                    |
| 3 teaspoons (t) = 1 tablespoon (T) | 3 cucharaditas = 1 cucharada   |
| 16 tablespoons (T) = 1 cup (C)     | 16 cucharadas = 1 taza         |
| 1 cup (C) = 8 fluid ounces (fl oz) | 1 taza = 8 onzas fluidas       |
| 1 pint (pt) = 2 cups (C)           | 1 pinta = 2 tazas              |
| 1 quart (qt) = 2 pints (pt)        | 1 cuarto de galón = 2 pintas   |
| 1 gallon (gal) = 4 quarts (qt)     | 1 galón = 4 cuartos de galón   |
| **Weight**                         | **Peso**                       |
| 1 pound (lb) = 16 ounces (oz)      | 1 libra = 16 onzas             |
| 1 ton (ton) = 2000 pounds (lb)     | 1 tonelada = 2000 libras       |
| **Time**                           | **Tiempo**                     |
| 1 minute (min) = 60 seconds (s)    | 1 minuto = 60 segundos         |
| 1 hour (h) = 60 minutes (min)      | 1 hora = 60 minutos            |
| 1 day (day) = 24 hours (h)         | 1 día = 24 horas               |
| 1 week (wk) = 7 days (days)        | 1 semana = 7 días              |
| 1 year (yr) = 365 days (days)      | 1 año = 365 días               |

(Sistema métrico internacional)
**International metric system**: system of measurement whose units are based on powers of 10. Prefixes are used to indicate the power of 10.

The following table contains a few of the units of the international metric system of measurement. Inside parentheses appears the abbreviation of each unit of measure.

| International metric system | Sistema métrico internacional |
| :-------------------------: | :---------------------------: |
| **Length**                  | **Longitud**                  |
| 1 meter (m) = 1 m           | 1 metro = 1 m                 |
| 1 kilometer (km) = 1000 m   | 1 kilómetro = 1000 m          |
| 1 hectometer (hm) = 100 m   | 1 hectómetro = 100 m          |
| 1 dekameter (dam) = 10 m    | 1 decámetro = 10 m            |
| 1 decimeter (dm) = 0.1 m    | 1 decímetro = 0.1 m           |
| 1 centimeter (cm) = 0.01 m  | 1 centímetro = 0.01 m         |
| 1 millimeter (mm) = 0.001 m | 1 milímetro = 0.001 m         |
| **Mass**                    | **Masa**                      |
| 1 gram (g) = 1 g            | 1 gramo = 1 g                 |
| 1 kilogram (kg) = 1000 g    | 1 kilogramo = 1000 g          |
| 1 hectogram (hg) = 100 g    | 1 hectogramo = 100 g          |
| 1 dekagram (dag) = 10 g     | 1 decagramo = 10 g            |
| 1 decigram (dg) = 0.1 g     | 1 decigramo = 0.1 g           |
| 1 centigram (cg) = 0.01 g   | 1 centigramo = 0.01 g         |
| 1 milligram (mg) = 0.001 g  | 1 miligramo = 0.001 g         |
| **Volume**                  | **Volumen**                   |
| 1 liter (L) = 1 L           | 1 litro = 1 L                 |
| 1 kiloliter (kL) = 1000 L   | 1 kilolitro = 1000 L          |
| 1 hectoliter (hL) = 100 L   | 1 hectolitro = 100 L          |
| 1 dekaliter (daL) = 10 L    | 1 decalitro = 10 L            |
| 1 deciliter (dL) = 0.1 L    | 1 decilitro = 0.1 L           |
| 1 centiliter (cL) = 0.01 L  | 1 centilitro = 0.01 L         |
| 1 milliliter (mL) = 0.001 L | 1 mililitro = 0.001 L         |

(Conversión de unidades)
**Unit conversion**: changing the units of a measure. Unit conversion is based on multiplying the unit to be changed by $1$, but writing $1$ in such a way that it changes the unit of measure. In general, given the units of measure $unit1$ and $unit2$, and given $A\ unit1 = B\ unit2$ meaning that $A$ units of $unit1$ are equal in measure to $B$ units of $unit2$, so $1 = \frac{B\ unit2}{A\ unit1}$, and also $1 = \frac{A\ unit1}{B\ unit2}$. These fractions are called conversion factors (factores de conversión).

Using real units, $1\ foot = 12\ inches$, so $1 = \frac{1\ foot}{12\ inches}$, and $1 = \frac{12\ inches}{1\ foot}$. The fraction chosen to do the unit conversion is the one that divides the unit being changed, so, the one that has the unit being changed in the denominator. For example, to convert $60\ inches$ to $feet$, the conversion factor must have $inches$ in the denominator, $60\ inches \frac{1\ foot}{12\ inches} = 5 feet$.

Several conversions can be made one after the other, for example, $60\ inches \frac{1\ foot}{12\ inches} \frac{1\ yard}{3\ feet} = \frac{5}{3}\ yard$.

(Conversión entre sistemas de medida)
**Conversion between systems of measurement**: units of measure can be converted from one system to another by having their equivalencies (equivalencias), and then performing regular unit conversion using said equivalencies.

The following table contains a few of the equivalencies between units in the U.S. customary units system and units in the international metric system. The values presented in the table are approximations.

| Equivalencies   |
| :------------:  |
| **Length**      |
| 1 in = 2.54 cm  |
| 1 ft = 0.305 m  |
| 1 yd = 0.914 m  |
| 1 mi = 1.61 km  |
| **Weight**      |
| 1 lb = 0.45 kg  |
| 1 oz = 28 g     |
| **Volume**      |
| 1 qt = 0.95 L   |
| 1 fl oz = 30 mL |

(Unidades de medida mixtas)
**Mixed units of measurement**: units of measure that are combined together to measure a single quantity. For example, using hours and minutes together to measure time.

When handling mixed units of measurement, each separate unit is added or subtracted separately. In the case of using hours and minutes together, for example $3\ hours, 12\ minutes$ plus $2\ hours, 20\ minutes$ is $5\ hours, 32\ minutes$, because hours and minutes are added separately. In this particular case, any amount of minutes over 60 is converted to hours accordingly, and in general the smaller unit is converted to the bigger unit if needed.

(Conversión Fahrenheit Celsius)
**Fahrenheit Celsius conversion**: two formulas that allow converting temperature (temperatura) measured in the Fahrenheit scale to the Celsius scale, and vice versa.

> Fahrenheit to Celsius conversion formula
>
> Let $C$ be the temperature in Celsius, $F$ be the temperature in Fahrenheit, then
> $$C = \frac{5}{9}(F - 32)$$

> Celsius to Fahrenheit conversion formula
>
> Let $C$ be the temperature in Celsius, $F$ be the temperature in Fahrenheit, then
> $$F = \frac{9}{5}C + 32$$