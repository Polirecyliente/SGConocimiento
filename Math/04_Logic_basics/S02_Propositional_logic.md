
#   Reasoning and proof (Razonamiento y demostración)

<!--
#T# Table of contents

#C# Inductive reasoning (Razonamiento inductivo)
#C# Conditional statements (Proposiciones condicionales)
#C# Deductive reasoning (Razonamiento deductivo)
#C# Algebraic and congruence properties (Propiedades de la igualdad y de la congruencia)
#C# Proofs about angle pairs and segments (Demostraciones sobre pares de ángulos y segmentos)

#T# Beginning of content
-->

(Lógica proposicional)
**Propositional logic**: branch of logic that condenses events and logical statements into symbols to operate over them and create propositions, which are logical statements themselves.

> Propositional logic notation
>
> Let $p$, $q$ be two events or logical statements, then those symbols, $p$ and $q$, represent said events or logical statements.

Logical operations can be made over $p$ and $q$.
[Logical statements code](Programs/S02/Logical_statements.py)

(Valor de verdad de una proposición o evento)
**Truth value of a statement or event**: value that results from a statement, or that is assigned to an event. The value $1$ means true, and the value $0$ means false. An event can be assigned a truth value, $1$ if the event happens, and $0$ if the event does not happen. A statement results in a truth value, $1$ if the statement is true, and $0$ if the statement is false.

> Example of truth value
>
> Let $p$ be the event 'I am healthy today', assigning it a truth value of $1$ means that $p$ happens, and assigning it a truth value of $0$ means that $p$ does not happen.

Truth values are also called logical values (valores lógicos).

## Conditional statements (Proposiciones condicionales)

Conditional statements are also called if-then statements, they are called in these ways because they put an event named conclusion (conclusión) to happen on the condition that another event named hypothesis (hipótesis) happens.

In a conditional statement if the hypothesis happens then the conclusion happens.

The hypothesis is also known as the antecedent (antecedente), and the conclusion is also known as the consequent (consecuente).

(Partes de una proposición condicional)
**Parts of a conditional statement**: a conditional statement has three parts, the hypothesis, the conclusion, and the connector between them.
[Conditional statement code](Programs/S02/Conditional_statement.py)

> Conditional statement notation
>
> Let $p$, $q$ be two events, such that $p$ is the hypothesis of a conditional statement, and $q$ is the conclusion of the same conditional statement, then
> $$p \to q$$
> denotes the conditional statement. It is read as if $p$ then $q$ (si $p$ entonces $q$), also read as $p$ implies $q$ ($p$ implica $q$).

> Example of a conditional statement
>
> Let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \to q$ means that 'if I am healthy today then I work today'.

(Negación lógica)
**Logical negation**: an operator used to negate an event. A negated event means that its negation happens.
[Logical negation code](Programs/S02/Logical_negation.py)

> Notation of the logical negation
>
> Let $p$ be an event, then its negation is
>
> $$\begin{gathered}
> \neg p\\
> \sim p
> \end{gathered}$$
> Both symbols $\neg$ and $\sim$ are used as the negation operator. $\neg p$ is read as not $p$ (no $p$).

> Example of a negation
>
> Let $p$ be the event 'I am healthy today', then $\neg p$ means the event 'I am not healthy today', which asserts that the negation of the event $p$ happens.

(Converso de una proposición)
**Converse of a statement**: the result of switching the order of the events of the statement.

> Converse of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \to q$, then the converse is
> $$q \to p$$

(Inverso de una proposición)
**Inverse of a statement**: the result of negating the events of the statement.

> Inverse of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \to q$, then the inverse is
> $$\neg p \to \neg q$$

(Contrapositivo de una proposición | Contrarrecíproco de una proposición)
**Contrapositive of a statement**: the result of negating and switching the order of the events of the statement.

> Contrapositive of a conditional statement
>
> Let $p$, $q$ be two events, such that $p \to q$, then the contrapositive is
> $$\neg q \to \neg p$$

(Proposiciones lógicas equivalentes)
**Logically equivalent statements**: two distinct statements with the same events that lead to the same truth values.
[Logically equivalent statements](Programs/S02/Logically_equivalent_statements.py)

> Example of logically equivalent statements
>
> Let $p$, $q$ be two events, such that $p \to q$, then its contrapositive is logically equivalent, i.e. $\neg q \to \neg p$ has the same logical meaning as $p \to q$.
>
> As a concrete example, let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the conditional statement $p \to q$ means that 'if I am healthy today then I work today'. On the other hand, $\neg q$ means 'I don't work today', and for this to happen, $\neg p$ 'I am not healthy today' must also happen, so $\neg q \to \neg p$.
>
> The converse and the inverse of a conditional statement are not necessarily true. In the example, the converse $q \to p$ means 'if I work today, then I am healthy today', but this is not logically guaranteed, because it can be that 'I work today' and 'I am not healthy today'. The statement $p \to q$ does not invalidate the statement $\neg p \to q$, both can be true at the same time. For this same reason the inverse $\neg p \to \neg q$ is not necessarily true.
>
> Only the contrapositive of a conditional statement is logically equivalent to the conditional statement. But the converse and the inverse of a conditional statement are logically equivalent to each other as well, because one is the contrapositive of the other.

(Proposición bicondicional)
**Biconditional statement**: a logical statement with a hypothesis that conditionates a conclusion, in which the conclusion conditionates the hypothesis. In a biconditional statement, the conclusion can be used as the hypothesis, and the hypothesis can be used as the conclusion.
[Biconditional statement code](Programs/S02/Biconditional_statement.py)

> Biconditional statement notation
>
> Let $p$, $q$ be two events, such that each is a condition for the other to happen, then
> $$p \leftrightarrow q$$
> denotes the biconditional statement. It is read as $p$ if and only if $q$ ($p$ sí y solo sí $q$).

The converse, inverse, and contrapositive of a biconditional statement are logically equivalent to each other. $p \leftrightarrow q$ implies $q \leftrightarrow p$ and also $\neg p \leftrightarrow \neg q$ and $\neg q \leftrightarrow \neg p$.

> Example of a biconditional statement
>
> Let $p$ be the event 'I am healthy today', and $q$ be the event 'I work today', then the biconditional statement $p \leftrightarrow q$ means that 'I am healthy today if and only if I work today'.

## Deductive reasoning (Razonamiento deductivo)

(Ley de separación)
**Law of detachment**: given two facts as true, that there exists a conditional statement and that the hypothesis of said conditional statement happens, the conclusion of the conditional statement can be deduced as a third true fact with no need for any other information.
[Law of detachment code](Programs/S02/Law_of_detachment.py)

> Law of detachment
>
> Let $p$, $q$ be two events, let $p$ be true, and let the conditional $p \to q$ be also true, then $q$ is true by deduction.
>
> The law of detachment can be denoted as follows
>
> $$\begin{gathered}
> p \to q\\
> p\\
> \therefore q
> \end{gathered}$$
> The $\therefore$ symbol is the therefore symbol, read as therefore (por lo tanto). The statements before the $\therefore$ are assumed true, and the statements after the $\therefore$ are deduced to be true.

The law of detachment is also known as modus ponendo ponens, which is latin for the mode that by affirming affirms.

(Ley contrarrecíproca)
**Law of contrapositive**: given two facts as true, that there exists a conditional statement and that the consecuent negated happens, then the negation of the antecedent can be deduced as a third true fact.
[Law of contrapositive code](Programs/S02/Law_of_contrapositive.py)

> Law of contrapositive
>
> Let $p$, $q$ be two events, let the conditional $p \to q$ be true and let $\neg q$ be also true, then $\neg p$ is true by deduction.
>
> The law of contrapositive can be denoted as follows
>
> $$\begin{gathered}
> p \to q\\
> \neg q\\
> \therefore \neg p
> \end{gathered}$$

This law is true because the contrapositive of a conditional is logically equivalent to said conditional.

(Ley del silogismo)
**Law of syllogism**: a chain of conditionals can be made, so that the consequent of one conditional is the antecedent of the next conditional. Given a chain of conditionals, one extra conditional can be deduced, namely if the first antecedent in the chain is true, then the last consequent in the chain is true.
[Law of syllogism code](Programs/S02/Law_of_syllogism.py)

> Law of syllogism
>
> Let $p$, $q$, $r$, $s$ events, then
>
> $$\begin{gathered}
> p \to q\\
> q \to r\\
> r \to s\\
> \therefore p \to s
> \end{gathered}$$

For that matter, several other conditionals could be deduced if needed, such as $p \to r$ and $q \to s$.

(Conjunción lógica)
**Logical conjunction**: the operation over two logical statements that returns a logical value of true if both logical statements are true. This is also known as the AND operation, because the first logical statement and the second must be true for the conjunction of them to be true.
[Logical conjunction code](Programs/S02/Logical_conjunction.py)

> Logical conjunction notation
>
> Let $p$, $q$ be two events, their conjunction is denoted as
> $$p \land q$$

The symbol $\land$ is the AND operator, $p \land q$ is read as $p$ and $q$ ($p$ y $q$).

(Disyunción lógica)
**Logical disjunction**: the operation over two logical statements that returns a logical value of true if either one or both logical statements are true. This is also known as the OR operation, because the first or the second logical statement or both can be true for the disjunction of them to be true.
[Logical disjunction code](Programs/S02/Logical_disjunction.py)

> Logical disjunction notation
>
> Let $p$, $q$ be two events, their disjunction is denoted as
> $$p \lor q$$

The symbol $\lor$ is the OR operator, $p \lor q$ is read as $p$ or $q$ ($p$ o $q$).

(Tablas de verdad)
**Truth tables**: tables made to organize the logical values of logical statements. They serve to compare side by side the logical values that result after applying different logical operators to logical statements and events.
[Truth tables code](Programs/S02/Truth_tables.py)

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

Truth tables can be used not only for binary operations but for more complex logical statements, e.g. let $p$, $q$, $r$ be three logical statements, a truth table can be made for the statement $p \land (\neg q \lor r)$, this truth table would have $8$ rows, one for each possible combination of the logical values of $p$, $q$, and $r$, with several intermediate columns showing the logical values of $\neg q$, $\neg q \lor r$, and with the logical values of the statement $p \land (\neg q \lor r)$ in the last column.

The following is a truth table for the statement $p \land (\neg q \lor r)$.

| $p$ | $q$ | $r$ | $\neg q$ | $\neg q \lor r$ | $p \land (\neg q \lor r)$ |
| :-: | :-: | :-: | :------: | :-------------: | :-----------------------: |
| $1$ | $1$ | $1$ | $0$      | $1$             | $1$                       |
| $1$ | $1$ | $0$ | $0$      | $0$             | $0$                       |
| $1$ | $0$ | $1$ | $1$      | $1$             | $1$                       |
| $1$ | $0$ | $0$ | $1$      | $1$             | $1$                       |
| $0$ | $1$ | $1$ | $0$      | $1$             | $0$                       |
| $0$ | $1$ | $0$ | $0$      | $0$             | $0$                       |
| $0$ | $0$ | $1$ | $1$      | $1$             | $0$                       |
| $0$ | $0$ | $0$ | $1$      | $1$             | $0$                       |
*Truth table for the $p \land (\neg q \lor r)$ statement*