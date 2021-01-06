
#   Logic for geometric proofs (Lógica para pruebas geométricas)

## Inductive reasoning (Razonamiento inductivo)
[Ch02_S01](https://www.ck12.org/reader/reader-index.html#section/2932925/2.1/9549314)

Inductive reasoning means reasoning on the basis of observed patterns.

(Patrones numéricos)
**Number patterns**: patterns made with numbers. Discovering the pattern requires inductive reasoning.

> Example of a number pattern
>
> The numbers $2$, $4$, $6$, $8$... form a pattern, in this pattern, the next numbers are most likely $10$, $12$, $14$, etcetera.

A number pattern may be represented as an equation in two variables, one variable for position or term in the pattern (first, second, third, etcetera), and one variable for the value of the pattern in that position or term.

> Example of the equation of a number pattern
>
> Let the pattern be $2$, $4$, $6$, $8$..., let $n$ be the term of the pattern, and let $P_n$ be the value of the pattern in the term $n$, then
> $$P_n = 2n$$

(Conjetura)
**Conjecture**: an explanation of a pattern that has not been proven.

> Example of a conjecture
>
> In the pattern $2$, $4$, $6$, $8$... the conjecture is that the value of the next term is $10$, and that the equation of this pattern is $P_n = 2n$ where $n$ is the term and $P_n$ is the pattern value of the term $n$. But it can happen that the value of the next term is not $10$ but another value, for example it could be $15%.

(Contraejemplo)
**Counterexample**: in a pattern, a counterexample is a pattern value that disproves a given conjecture.

> Example of a counterexample
>
> In the pattern $2$, $4$, $6$, $8$..., if the conjecture is that the pattern value of the next term is $10$, then a counterexample would be that the pattern value of the next term was actually $15$, this disproves the conjecture.

## Conditional statements (Proposiciones condicionales)
[Ch02_S02](https://www.ck12.org/reader/reader-index.html#section/2932926/2.2/9549314)

Conditional statements are also called if-then statements, they are called in these ways because they put an event named conclusion (conclusión) to happen on the condition that another event named hypothesis (hipótesis) happens.

In a conditional statement if the hypothesis happens then the conclusion happens.

The hypothesis is also known as the antecedent (antecedente), and the conclusion is also known as the consequent (consecuente).

(Lógica proposicional)
**Propositional logic**: branch of logic that condenses events and logical statements into symbols to operate over them and create propositions, which are logical statements themselves.

> Propositional logic notation
>
> Let $p$, $q$ be two events or logical statements, then those symbols, $p$ and $q$, represent said events or logical statements.

Logical operations can be made over $p$ and $q$.
[Logical statements code](Programs/Ch02/S02_01_Logical_statements.py)

(Valor de verdad de una proposición o evento)
**Truth value of a statement or event**: value that results from a statement, or that is assigned to an event. The value $1$ means true, and the value $0$ means false. An event can be assigned a truth value, $1$ if the event happens, and $0$ if the event does not happen. A statement results in a truth value, $1$ if the statement is true, and $0$ if the statement is false.

> Example of truth value
>
> Let $p$ be the event 'I am healthy today', assigning it a truth value of $1$ means that $p$ happens, and assigning it a truth value of $0$ means that $p$ does not happen.

Truth values are also called logical values (valores lógicos).

(Partes de una proposición condicional)
**Parts of a conditional statement**: a conditional statement has three parts, the hypothesis, the conclusion, and the connector between them.
[Conditional statement code](Programs/Ch02/S02_02_Conditional_statement.py)

> Conditional statement notation
>
> Let $p$, $q$ be two events, such that $p$ is the hypothesis of a conditional statement, and $q$ is the conclusion of the same conditional statement, then
> $$p \rarr q
> $$ denotes the conditional statement. It is read as if $p$ then $q$ (si $p$ entonces $q$), also read as $p$ implies $q$ ($p$ implica $q$).

> Example of a conditional statement
>
> Let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \rarr q$ means that 'if I am healthy today then I work today'.

(Negación lógica)
**Logical negation**: an operator used to negate an event. A negated event means that its negation happens.
[Logical negation code](Programs/Ch02/S02_03_Logical_negation.py)

> Notation of the logical negation
>
> Let $p$ be an event, then its negation is
> $$\neg p\\
> \sim p
> $$ Both symbols $\neg$ and $\sim$ are used as the negation operator. $\neg p$ is read as not $p$ (no $p$).

> Example of a negation
>
> Let $p$ be the event 'I am healthy today', then $\neg p$ means the event 'I am not healthy today', which asserts that the negation of the event $p$ happens.

(Converso de una proposición)
**Converse of a statement**: the result of switching the order of the events of the statement.

> Converse of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \rarr q$, then the converse is
> $$q \rarr p$$

(Inverso de una proposición)
**Inverse of a statement**: the result of negating the events of the statement.

> Inverse of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \rarr q$, then the inverse is
> $$\neg p \rarr \neg q$$

(Contrapositivo de una proposición|Contrarrecíproco de una proposición)
**Contrapositive of a statement**: the result of negating and switching the order of the events of the statement.

> Contrapositive of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \rarr q$, then the contrapositive is
> $$\neg q \rarr \neg p$$

(Proposiciones lógicas equivalentes)
**Logically equivalent statements**: two distinct statements with the same events that lead to the same truth values.
[Logically equivalent statements](Programs/Ch02/S02_04_Logically_equivalent_statements.py)

> Example of logically equivalent statements
>
> Let $p$, $q$ be two events, such that $p \rarr q$, then its contrapositive is logically equivalent, i.e. $\neg q \rarr \neg p$ has the same logical meaning as $p \rarr q$.
>
> As a concrete example, let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \rarr q$ means that 'if I am healthy today then I work today'. On the other hand, $\neg q$ means 'I don't work today', and for this to happen, $\neg p$ 'I am not healthy today' must also happen, so $\neg q \rarr \neg p$.
>
> The converse and the inverse of a conditional statement are not necessarily true. In the example, the converse $q \rarr p$ means 'if I work today, then I am healthy today', but this is not logically guaranteed, because it can be that 'I work today' and 'I am not healthy today'. The statement $p \rarr q$ does not invalidate the statement $\neg p \rarr q$, both can be true at the same time. For this same reason the inverse $\neg p \rarr \neg q$ is not necessarily true.
>
> Only the contrapositive of a conditional statement is logically equivalent to the conditional statement. But the converse and the inverse of a conditional statement are logically equivalent to each other as well, because one is the contrapositive of the other.

(Proposición bicondicional)
**Biconditional statement**: a logical statement with a hypothesis that conditionates a conclusion, in which the conclusion conditionates the hypothesis. In a biconditional statement, the conclusion can be used as the hypothesis, and the hypothesis can be used as the conclusion.
[Biconditional statement code](Programs/Ch02/S02_05_Biconditional_statement.py)

> Biconditional statement notation
>
> Let $p$, $q$ be two events, such that each is a condition for the other to happen, then
> $$p \lrarr q
> $$ denotes the biconditional statement. It is read as $p$ if and only if $q$ ($p$ sí y solo sí $q$).

The converse, inverse, and contrapositive of a biconditional statement are logically equivalent to each other. $p \lrarr q$ implies $q \lrarr p$ and also $\neg p \lrarr \neg q$ and $\neg q \lrarr \neg p$.

> Example of a biconditional statement
>
> Let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the biconditional statement $p \lrarr q$ means that 'I am healthy today if and only if I work today'.

## Deductive reasoning (Razonamiento deductivo)
[Ch02_S03](https://www.ck12.org/reader/reader-index.html#section/2932927/2.3/9549314)

Deductive reasoning means reasoning on the basis of given facts.

> Example of deductive reasoning
>
> Let $p$, $q$ be two events, such that $p \rarr q$. Given the fact that $p$ happens, the conclusion is that $q$ happens or will happen. Concluding that $q$ happens is a deduction, because it's a conclusion that was arrived to by reasoning on the basis of the given facts $p$ and $p \rarr q$.

(Ley de separación)
**Law of detachment**: given two facts as true, that there exists a conditional statement and that the hypothesis of said conditional statement happens, the conclusion of the conditional statement can be deduced as a third true fact with no need for any other information.
[Law of detachment code](Programs/Ch02/S03_01_Law_of_detachment.py)

> Law of detachment
>
> Let $p$, $q$ be two events, let $p$ be true, and let the conditional $p \rarr q$ be also true, then $q$ is true by deduction.
>
> The law of detachment can be denoted as follows
> $$p \rarr q\\
> p\\
> \therefore q
> $$ The $\therefore$ symbol is the therefore symbol, read as therefore (por lo tanto). The statements before the $\therefore$ are assumed true, and the statements after the $\therefore$ are deduced to be true.

The law of detachment is also known as modus ponendo ponens, which is latin for the mode that by affirming affirms.

(Falacia lógica)
**Logic fallacy**: a set of logical statements that are wrong or misconstrued.

(Falacia del converso)
**Fallacy of the converse**: also known as affirming the consequent (afirmación del consecuente), this fallacy states that given two true facts, a conditional statement and the consequent of said conditional, then the antecedent is deduced as being true.

> Fallacy of the converse
>
> Let $p$, $q$ be two events, then
> $$p \rarr q\\
> q\\
> \therefore p
> $$ These logical statements are wrong, because if $p \rarr q$ is true and $q$ is true, then $p$ may or may not be true. It could be the case that $\neg p \rarr q$.

The fallacy of the converse is also known as the converse error (error converso), because it would only be true if the converse $q \rarr p$ was true, instead of the actual conditional $p \rarr q$.

(Ley contrarrecíproca)
**Law of contrapositive**: given two facts as true, that there exists a conditional statement and that the consecuent negated happens, then the negation of the antecedent can be deduced as a third true fact.
[Law of contrapositive code](Programs/Ch02/S03_02_Law_of_contrapositive.py)

> Law of contrapositive
>
> Let $p$, $q$ be two events, let the conditional $p \rarr q$ be true and let $\neg q$ be also true, then $\neg p$ is true by deduction.
>
> The law of contrapositive can be denoted as follows
> $$p \rarr q\\
> \neg q\\
> \therefore \neg p$$

This law is true because the contrapositive of a conditional is logically equivalent to said conditional.

(Ley del silogismo)
**Law of syllogism**: a chain of conditionals can be made, so that the consequent of one conditional is the antecedent of the next conditional. Given a chain of conditionals, one extra conditional can be deduced, namely if the first antecedent in the chain is true, then the last consequent in the chain is true.
[Law of syllogism code](Programs/Ch02/S03_03_Law_of_syllogism.py)

> Law of syllogism
>
> Let $p$, $q$, $r$, $s$ events, then
> $$p \rarr q\\
> q \rarr r\\
> r \rarr s\\
> \therefore p \rarr s$$

For that matter, several other conditionals could be deduced if needed, such as $p \rarr r$ and $q \rarr s$.

(Conjunción lógica)
**Logical conjunction**: the operation over two logical statements that returns a logical value of true if both logical statements are true. This is also known as the AND operation, because the first logical statement and the second must be true for the conjunction of them to be true.
[Logical conjunction code](Programs/Ch02/S03_04_Logical_conjunction.py)

> Logical conjunction notation
>
> Let $p$, $q$ be two events, their conjunction is denoted as
> $$p \land q$$

The symbol $\land$ is the AND operator, $p \land q$ is read as $p$ and $q$ ($p$ y $q$).

(Disyunción lógica)
**Logical disjunction**: the operation over two logical statements that returns a logical value of true if either one or both logical statements are true. This is also known as the OR operation, because the first or the second logical statement or both can be true for the disjunction of them to be true.
[Logical disjunction code](Programs/Ch02/S03_05_Logical_disjunction.py)

> Logical disjunction notation
>
> Let $p$, $q$ be two events, their disjunction is denoted as
> $$p \lor q$$

The symbol $\lor$ is the OR operator, $p \lor q$ is read as $p$ or $q$ ($p$ o $q$).

(Tablas de verdad)
**Truth tables**: tables made to organize the logical values of logical statements. They serve to compare side by side the logical values that result after applying different logical operators to logical statements and events.
[Truth tables code](Programs/Ch02/S03_06_Truth_tables.py)

To indicate true and false, truth tables commonly use $1$ for true and $0$ for false, or also $T$ for true and $F$ for false. Truth tables consider all the possible combinations of logical values.

In the following tables, let $p$, $q$ be logical statements.

| $p$ | $\neg p$ |
| :-: | :------: |
| $1$ | $0$      |
| $0$ | $1$      |
*Truth table for the negation operation*

| $p$ | $q$ | $p \land q$ |
| :-: | :-: | :---------: |
| $1$ | $1$ | $1$         |
| $1$ | $0$ | $0$         |
| $0$ | $1$ | $0$         |
| $0$ | $0$ | $0$         |
*Truth table for the and operation*

| $p$ | $q$ | $p \lor q$ |
| :-: | :-: | :--------: |
| $1$ | $1$ | $1$        |
| $1$ | $0$ | $1$        |
| $0$ | $1$ | $1$        |
| $0$ | $0$ | $0$        |
*Truth table for the or operation*

Truth tables can be used not only for binary operations but for more complex logical expressions, e.g. let $p$, $q$, $r$ be three logical statements, a truth table can be made for the expression $p \land (\neg q \lor r)$, this truth table would have $8$ rows, one for each possible combination of the logical values of $p$, $q$, and $r$, and with the logical value of the expression $p \land (\neg q \lor r)$ in the last column.

## Equality and congruence properties, two column proofs (Propiedades de la igualdad y la congruencia, demostraciones a dos columnas)
[Ch02_S04](https://www.ck12.org/reader/reader-index.html#section/2932928/2.4/9549314)

(Propiedades de la igualdad)
**Properties of equality**: the following are some of the several properties that equality has.

- **Reflexive property of equality** (Propiedad reflexiva de la igualdad): a real number is equal to itself. Let $a$ be a real number, then $a = a$.

- **Symmetric property of equality** (Propiedad simétrica de la igualdad): if a first real number is equal to a second, then the second number is equal to the first. Let $a$, $b$ be real numbers, then $a = b \lrarr b = a$.

- **Transitive property of equality** (Propiedad transitiva de la igualdad): if a first real number is equal to a second, and the second number is equal to a third, then the third number is equal to the first. Let $a$, $b$, $c$ be real numbers, if $a = b$ and $b = c$ then $a = c$.

- **Substitution property of equality** (Propiedad de sustitución de la igualdad): if two real numbers are equal, one can be substituted by the other. Let $a$, $b$ be real numbers, if $a = b$ then $b$ can substitute $a$ and vice versa.

- **Addition property of equality** (Propiedad aditiva de la igualdad): adding a real number to both sides of an equality, preserves the equality. Let $a$, $b$, $c$ be real numbers, if $a = b$ then $a + c = b + c$.

- **Subtraction property of equality** (Propiedad sustractiva de la igualdad): subtracting a real number from both sides of an equality, preserves the equality. Let $a$, $b$, $c$ be real numbers, if $a = b$ then $a - c = b - c$.

- **Multiplication property of equality** (Propiedad multiplicativa de la igualdad): multiplying a real number to both sides of an equality, preserves the equality. Let $a$, $b$, $c$ be real numbers, if $a = b$ then $ac = bc$.

- **Division property of equality** (Propiedad divisiva de la igualdad): dividing both sides of an equality by a real number different from zero, preserves the equality. Let $a$, $b$, $c$ be real numbers with $c \ne 0$, if $a = b$ then $\frac{a}{c} = \frac{b}{c}$.

- **Distributive property of multiplication over addition** (Propiedad distributiva de la multiplicación respecto a la suma): a real number multiplying the sum of other real numbers, is equal to the sum of the products of the real number by each of the other real numbers. Let $a$, $b$, $c$ be real numbers, then $a(b + c) = ab + ac$.

(Propiedades de la congruencia)
**Properties of congruence**: the following are some of the several properties that congruence has.

- **Reflexive property of congruence** (Propiedad reflexiva de la congruencia): a figure is congruent with itself. Let $\overline{AB}$ be a segment, and $\angle ABC$ be an angle, then $\overline{AB} \cong \overline{AB}$ and $\angle ABC \cong \angle ABC$.

- **Symmetric property of congruence** (Propiedad simétrica de la congruencia): if a first figure is congruent to a second, then the second figure is congruent to the first. Let $\overline{AB}$, $\overline{CD}$ be segments, if $\overline{AB} \cong \overline{CD}$ then $\overline{CD} \cong \overline{AB}$.

- **Transitive property of congruence** (Propiedad transitiva de la congruencia): if a first figure is congruent to a second, and the second figure is congruent to a third, then the third figure is congruent to the first. Let $\overline{AB}$, $\overline{CD}$, $\overline{EF}$ be segments, if $\overline{AB} \cong \overline{CD}$ and $\overline{CD} \cong \overline{EF}$ then $\overline{AB} \cong \overline{EF}$.

(Demostraciones a dos columnas)
**Two column proofs**: a way to write mathematical proofs in a structured manner. The proof is written in a table with two columns. The first column has the header of 'Statement', and its rows contain the steps of the proof. The second column has the header of 'Reason', and its rows state the reason why the step they accompany is correct.

| Statement | Reason  |
| :-------: | :-----: |
| Step1     | Reason1 |
| Step2     | Reason2 |
| Step3     | Reason3 |
*Two column proof template*

Step1 is supported by Reason1, Step2 is supported by Reason2, and so on.

## Proofs about angle pairs and segments (Demostraciones sobre pares de ángulos y segmentos)
[Ch02_S05](https://www.ck12.org/reader/reader-index.html#section/2932929/2.5/9549314)

(Teorema del ángulo recto)
**Right angle theorem**: all right angles are congruent.

> Proof of the right angle theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$ and $\angle B$ be any two right angles | Given |
> | $m \angle A = \pi/2$ and $m \angle B = \pi/2$ | Definition of right angles |
> | $m \angle A = m \angle B$ | Transitive property of equality |
> | $\angle A \cong \angle B$ | Definition of congruence |

[Right angle theorem image code](Programs/Ch02/S05_01_Right_angle_theorem_image.py)
![Right angle theorem image](Images/Ch02/S05_01_Right_angle_theorem.png)
*Right angle theorem example*

The segments may not be congruent but the right angles are.

(Teorema de los suplementos congruentes)
**Congruent supplements theorem**: two angles are congruent when they are supplementary to another angle, or when they are supplementary to two other congruent angles.

> Proof of the congruent supplements theorem
>
> | Statement                                      | Reason                   |
> | :--------------------------------------------: | :----------------------: |
> | Let $\angle A$, $\angle B$, $\angle C$ be angles | Given |
> | Let $\angle A$ and $\angle C$ be supplements of $\angle B$ | Given |
> | $m \angle A + m \angle B = \pi$, $m \angle C + m \angle B = \pi$ | Definition of supplementary angles |
> | $m \angle A + m \angle B = m \angle C + m \angle B$ | Transitive property of equality |
> | $m \angle A = m \angle C$ | Subtraction property of equality |
> | $\angle A \cong \angle C$ | Definition of congruence |

(Demostración textual)
**Paragraph proof**: a proof that is written in paragraphs. To know where it ends, the symbol $\blacksquare$ is used.

(Teorema de los complementos congruentes)
**Congruent complements theorem**: two angles are congruent when they are complementary to another angle, or when they are complementary to two other congruent angles.

> Proof of the congruent complements theorem
>
> Let $\angle A$, $\angle B$, $\angle C$ be angles, such that $\angle A$ and $\angle C$ are complements of $\angle B$. This means that $m \angle A + m \angle B = \pi/2$ and $m \angle C + m \angle B = \pi/2$, then by transitivity $m \angle A + m \angle B = m \angle C + m \angle B$ which can be simplified to $m \angle A = m \angle C$, and in turn $\angle A \cong \angle C$ by definition. $\blacksquare$