
#   Statistics definitions (Definiciones de estadística)

(Frecuencia de un número en un conjunto)
**Frequency of a number in a set**: the amount of times a given number is repeated in a set.

(Probabilidad de un evento)
**Probability of an event**: the fraction of the number of times an event happens over the number of general outcomes with or without the event.

For example, in a set of $N$ numbers, the probability $P(x)$ to obtain a given number $x$ that has a frequency of $f_x$ is $P(x) = \frac{f_x}{N}$.

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

(Moda)
**Mode**: the number with the highest frequency in a set. A set of numbers can have several modes if several numbers have the same highest frequency, or none if all the numbers have the same frequency.

(Media geométrica)
**Geometric mean**: a measure of central tendency of $n$ numbers, that consists in taking the $n$-th root of the product of the $n$ numbers.
[Geometric mean code](Programs/S08/Geometric_mean.py)

> Definition of the geometric mean
>
> Let there be $n$ numbers, where $x_i$ is the $i$-number. Let $GM(x)$ be the geometric mean of the $n$ numbers, then
> $$GM(x) = \sqrt[n]{x_1 x_2 ... x_n}$$

The geometric mean $GM(x)$ is the number whose repeated multiplication is the same as the product $x_1 x_2 ... x_n$, so if the geometric mean replaced each number $x_i$, then the total product would be the same.