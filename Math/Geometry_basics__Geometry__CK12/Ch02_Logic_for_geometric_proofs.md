
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

(Lógica proposicional)
**Propositional logic**: branch of logic that condenses events into symbols to operate over them and create propositions or statements.

> Propositional logic notation
>
> Let $p$, $q$ be two events, then those symbols, $p$ and $q$, represent said events.

(Partes de una proposición condicional)
**Parts of a conditional statement**: a conditional statement has three parts, the hyphotesis, the conclusion, and the connector between them.

> Conditional statement notation
>
> Let $p$, $q$ be two events, such that $p$ is the hypothesis of a conditional statement, and $q$ is the conclusion of the same conditional statement, then
> $$p \rarr q
> $$ denotes the conditional statement. It is read as if $p$ then $q$ (si $p$ entonces $q$).

> Example of a conditional statement
>
> Let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \rarr q$ means that 'if I am healthy today then I work today'.

(Negación lógica)
**Logic negation**: an operator used to negate an event. A negated event means that its negation happens.

> Notation of the logic negation
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

(Contrapositivo de una proposición)
**Contrapositive of a statement**: the result of negating and switching the order of the events of the statement.

> Contrapositive of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \rarr q$, then the contrapositive is
> $$\neg q \rarr \neg p$$

(Valor de verdad de una proposición o evento)
**Truth value of a statement or event**: value that results from a statement, or that is assigned to an event. The value $1$ means true, and the value $0$ means false. An event can be assigned a truth value, $1$ if the event happens, and $0$ if the event does not happen. A statement results in a truth value, $1$ if the statement is true, and $0$ if the statement is false.

> Example of truth value
>
> Let $p$ be the event 'I am healthy today', assigning it a truth value of $1$ means that $p$ happens, and assigning it a truth value of $0$ means that $p$ does not happen.

(Proposiciones lógicas equivalentes)
**Logically equivalent statements**: two distinct statements with the same events that lead to the same truth values.

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

## Equality and congruence properties, two column proofs (Propiedades de la igualdad y la congruencia, demostraciones a dos columnas)
[Ch02_S04](https://www.ck12.org/reader/reader-index.html#section/2932928/2.4/9549314)

## Proofs about angle pairs and segments (Demostraciones sobre pares de ángulos y segmentos)
[Ch02_S05](https://www.ck12.org/reader/reader-index.html#section/2932929/2.5/9549314)