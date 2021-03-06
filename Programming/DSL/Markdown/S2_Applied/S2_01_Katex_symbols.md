<!--
    Katex symbols
-->

<!-- #T# Table of contents -->

<!-- #C# Accents -->
<!-- #C# Spacing -->
<!-- #C# Delimiters -->
<!-- #C# --- Delimiter sizing modifiers -->
<!-- #C# Environments -->
<!-- #C# Letters -->
<!-- #C# Layout -->
<!-- #C# --- Annotations -->
<!-- #C# --- Vertical layout -->
<!-- #C# Logic, set theory -->
<!-- #C# Operators -->
<!-- #C# --- Big operators -->
<!-- #C# --- Binary operators -->
<!-- #C# --- Functions -->
<!-- #C# --- Relational operators -->
<!-- #C# Arrows -->
<!-- #C# Style -->
<!-- #C# Symbols, punctuation -->

<!-- #T# Beginning of content -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# katex symbols are used in markdown files, inside single, or double dollar signs -->

<!-- #T# this markdown file is used to show the katex symbols, organized by categories. The character 'L' for Letters, is used for most examples -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Accents -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# accents are a type of diacritic that commonly goes on top of the letter -->
| Accent description             | Example                         |
| :----------------------------- | :-----------------------------: |
| Tilde over letter              | $\tilde{L}$                     |
| Wide tilde over letters        | $\widetilde{Letters}$           |
| Wide tilde under letters       | $\utilde{Letters}$              |
| Acute over letter              | $\acute{L}$                     |
| Grave over letter              | $\grave{L}$                     |
| Breve over letter              | $\breve{L}$                     |
| Caret over letter              | $\hat{L}$                       |
| Wide caret over letters        | $\widehat{Letters}$             |
| Caron over letter              | $\check{L}$                     |
| Wide caron over letters        | $\widecheck{Letters}$           |
| Circle over letter             | $\mathring{L}$                  |
| Dot over letter                | $\dot{L}$                       |
| Double dots over letter        | $\ddot{L}$                      |
| Bar over letter                | $\bar{L}$                       |
| Vector over letter             | $\vec{L}$                       |
| Line over letters              | $\overline{Letters}$            |
| Line under letters             | $\underline{Letters}$           |
| Left arrow over letters        | $\overleftarrow{Letters}$       |
| Left arrow under letters       | $\underleftarrow{Letters}$      |
| Right arrow over letters       | $\overrightarrow{Letters}$      |
| Right arrow under letters      | $\underrightarrow{Letters}$     |
| Big right arrow over letters   | $\Overrightarrow{Letters}$      |
| Left right arrow over letters  | $\overleftrightarrow{Letters}$  |
| Left right arrow under letters | $\underleftrightarrow{Letters}$ |
| Left harpoon over letters      | $\overleftharpoon{Letters}$     |
| Right harpoon over letters     | $\overrightharpoon{Letters}$    |
| Line segment over letters      | $\overlinesegment{Letters}$     |
| Line segment under letters     | $\underlinesegment{Letters}$    |
| Parenthesis over letters       | $\overgroup{Letters}$           |
| Parenthesis under letters      | $\undergroup{Letters}$          |
| Brace over letters             | $\overbrace{Letters}$           |
| Brace under letters            | $\underbrace{Letters}$          |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Spacing -->

<!-- # |------------------------------------------------------------- -->
| Spacing description       | Example             |
| :----------------------   | :------:            |
| Literal space             | $A\ B$              |
| Quadratone space          | $A\quad B$          |
| Double quadratone space   | $A\qquad B$         |
| Small spacing             | $A\, B$             |
| Middle spacing            | $A\enspace B$       |
| Custom horizontal space   | $A\hspace{1.4em}B$  |
| Custom horizontal space 2 | $A\hspace{-2.3em}B$ |
| Small negative spacing    | $A\!B$              |
| Middle negative spacing   | $A\negmedspace B$   |
| Big negative spacing      | $A\negthickspace B$ |
| No break space            | $A\nobreakspace B$  |
| Custom vertical space     | $A\\[12 pt]B$       |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Delimiters -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# delimiters are used as grouping symbols -->
| Delimiter description    | Example                                       |
| :----------------------- | :-------------------------------------------: |
| Left parenthesis         | $\lparen$ or $($                              |
| Right parenthesis        | $\rparen$ or $)$                              |
| Left bracket             | $\lbrack$ or $[$                              |
| Right bracket            | $\rbrack$ or $]$                              |
| Left brace               | $\lbrace$ or $\{$ or $\text{\textbraceleft}$  |
| Right brace              | $\rbrace$ or $\}$ or $\text{\textbraceright}$ |
| Left angle bracket       | $\langle$ or $\lang$                          |
| Right angle bracket      | $\rangle$ or                                  |
| Left group symbol        | $\lgroup$                                     |
| Right group symbol       | $\rgroup$                                     |
| Vertical line            | $\vert$ or a literal vertical line            |
| Left vertical line       | $\lvert$                                      |
| Right vertical line      | $\rvert$                                      |
| Double vertical lines    | $\Vert$ or $\|$                               |
| Left double vertical     | $\lVert$                                      |
| Right double vertical    | $\rVert$                                      |
| Left white bracket       | $\llbracket$                                  |
| Right white bracket      | $\rrbracket$                                  |
| Left white brace         | $\lBrace$                                     |
| Right white brace        | $\rBrace$                                     |
| Upper left bracket       | $\ulcorner$                                   |
| Upper right bracket      | $\urcorner$                                   |
| Lower left bracket       | $\llcorner$                                   |
| Lower right bracket      | $\lrcorner$                                   |
| Left ceiling             | $\lceil$                                      |
| Right ceiling            | $\rceil$                                      |
| Left floor               | $\lfloor$                                     |
| Right floor              | $\rfloor$                                     |
| Left upper half brace    | $\lmoustache$                                 |
| Right upper half brace   | $\rmoustache$                                 |

<!-- #C# --- Delimiter sizing modifiers -->

<!-- # |----- -->
| Delimiter modifier description       | Example                           |
| :----------------------------------- | :-------------------------------: |
| Left, middle, right, always together | $\left) A \middle\Vert B \right($ |
| big grouping symbol                  | $\big\lparen$                     |
| Big grouping symbol                  | $\Big\lbrack$                     |
| bigg grouping symbol                 | $\bigg\lbrace$                    |
| Bigg grouping symbol                 | $\Bigg\langle$                    |
| bigm grouping symbol                 | $\bigm\lgroup$                    |
| Bigm grouping symbol                 | $\Bigm\lvert$                     |
| biggm grouping symbol                | $\biggm\lVert$                    |
| Biggm grouping symbol                | $\Biggm\lmoustache$               |
| bigr grouping symbol                 | $\bigr\lceil$                     |
| Bigr grouping symbol                 | $\Bigr\rceil$                     |
| biggr grouping symbol                | $\biggr\lfloor$                   |
| Biggr grouping symbol                | $\Biggr\rfloor$                   |
<!-- # |----- -->

<!-- # |------------------------------------------------------------- -->

<!-- #C# Environments -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# Latex environments, used here mostly for specific grids where to write characters -->
| Environment  | Example                                            |
| :----------- | :------------------------------------------------: |
| Array        | $\begin{array}{l:c} a & b \\ c & d \end{array}$    |
| Matrix       | $\begin{matrix} a & b \\[9pt] c & d \end{matrix}$  |
| Parentheses  | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$     |
| Brackets     | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$     |
| Braces       | $\begin{Bmatrix} a & b \\ c & d \end{Bmatrix}$     |
| Single lines | $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$     |
| Double lines | $\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}$     |
| Small        | $\begin{smallmatrix} a \\ c & d \end{smallmatrix}$ |
| Left cases   | $\begin{cases} a & b \\ c & d \end{cases}$         |
| Aligned      | $\begin{aligned} a &= b \\ 2 =& 2 \end{aligned}$   |
| Alignedat    | $\begin{alignedat}{1} ab& \\ &ba \end{alignedat}$  |
| Gathered     | $\begin{gathered} a \\ c = d \end{gathered}$       |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Letters -->

<!-- # |------------------------------------------------------------- -->
| Letter name        | Example                           |
| :----------------- | :-------------------------------: |
| Alpha              | $\alpha$                          |
| Mayus alpha        | $\Alpha$                          |
| Beta               | $\beta$                           |
| Mayus beta         | $\Beta$                           |
| Gamma              | $\gamma$                          |
| Mayus gamma        | $\Gamma$                          |
| Mayus digamma      | $\digamma$                        |
| Mayus vargamma     | $\varGamma$                       |
| Delta              | $\delta$                          |
| Mayus delta        | $\Delta$                          |
| Mayus vardelta     | $\varDelta$                       |
| Epsilon            | $\epsilon$                        |
| Varepsilon         | $\varepsilon$                     |
| Back epsilon       | $\backepsilon$                    |
| Mayus epsilon      | $\Epsilon$                        |
| Zeta               | $\zeta$                           |
| Mayus zeta         | $\Zeta$                           |
| Eta                | $\eta$                            |
| Mayus eta          | $\Eta$                            |
| Theta              | $\theta$                          |
| Vartheta           | $\vartheta$ or $\thetasym$        |
| Mayus theta        | $\Theta$                          |
| Mayus vartheta     | $\varTheta$                       |
| Iota               | $\iota$                           |
| Mayus iota         | $\Iota$                           |
| Kappa              | $\kappa$                          |
| Varkappa           | $\varkappa$                       |
| Mayus kappa        | $\Kappa$                          |
| Lambda             | $\lambda$                         |
| Mayus lambda       | $\Lambda$                         |
| Mayus varlambda    | $\varLambda$                      |
| Mu                 | $\mu$                             |
| Mayus mu           | $\Mu$                             |
| Nu                 | $\nu$                             |
| Mayus nu           | $\Nu$                             |
| Xi                 | $\xi$                             |
| Mayus xi           | $\Xi$                             |
| Mayus varxi        | $\varXi$                          |
| Omicron            | $\omicron$                        |
| Mayus omicron      | $\Omicron$                        |
| Pi                 | $\pi$                             |
| Varpi              | $\varpi$                          |
| Mayus pi           | $\Pi$                             |
| Mayus varpi        | $\varPi$                          |
| Rho                | $\rho$                            |
| Varrho             | $\varrho$                         |
| Mayus rho          | $\Rho$                            |
| Sigma              | $\sigma$                          |
| Varsigma           | $\varsigma$                       |
| Mayus sigma        | $\Sigma$                          |
| Mayus varsigma     | $\varSigma$                       |
| Tau                | $\tau$                            |
| Mayus tau          | $\Tau$                            |
| Upsilon            | $\upsilon$                        |
| Mayus upsilon      | $\Upsilon$                        |
| Mayus varupsilon   | $\varUpsilon$                     |
| Phi                | $\phi$                            |
| Varphi             | $\varphi$                         |
| Mayus phi          | $\Phi$                            |
| Mayus varphi       | $\varPhi$                         |
| Chi                | $\chi$                            |
| Mayus chi          | $\Chi$                            |
| Psi                | $\psi$                            |
| Mayus psi          | $\Psi$                            |
| Mayus varpsi       | $\varPsi$                         |
| Omega              | $\omega$                          |
| Mayus omega        | $\Omega$                          |
| Mayus varomega     | $\varOmega$                       |
| Inverted omega     | $\mho$                            |
| Math i             | $\imath$                          |
| Math j             | $\jmath$                          |
| Aleph              | $\aleph$ or $\alef$ or $\alefsym$ |
| Beth               | $\beth$                           |
| Gimel              | $\gimel$                          |
| Daleth             | $\daleth$                         |
| Eth                | $\eth$                            |
| Aesh               | $\text{\ae}$                      |
| Mayus aesh         | $\text{\AE}$                      |
| Oe ligature        | $\text{\oe}$                      |
| Mayus oe ligature  | $\text{\OE}$                      |
| Eszett             | $\text{\ss}$                      |
| Null symbol        | $\text{\o}$                       |
| Big null symbol    | $\text{\O}$                       |
| Weierstrass p      | $\wp$ or $\weierp$                |
| Inverted F         | $\Finv$                           |
| Mirrored G         | $\Game$                           |
| Blackboard bold k  | $\Bbbk$                           |
| Ell                | $\ell$                            |
| Nabla              | $\nabla$                          |
| Partial derivative | $\partial$                        |
| H bar              | $\hbar$                           |
| H slash            | $\hslash$                         |
| Natural set        | $\N$ or $\natnums$                |
| Whole set          | $\Z$                              |
| Real set           | $\R$ or $\reals$ or $\Reals$      |
| Complex set        | $\cnums$ or $\Complex$            |
| Real part          | $\Re$ or $\real$                  |
| Imaginary part     | $\Im$ or $\image$                 |
| Infinity           | $\infty$ or $\infin$              |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Layout -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# layout serves to set the characters' position -->

<!-- #C# --- Annotations -->

<!-- # |----- -->
| Annotation description | Example             |
| :--------------------- | :-----------------: |
| Slash over letters     | $\cancel{Letters}$  |
| Backslash over letters | $\bcancel{Letters}$ |
| X over letters         | $\xcancel{Letters}$ |
| Not equal              | $\not =$            |
| Strikethrough          | $\sout{Letters}$    |
| Box around letters     | $\boxed{Letters}$   |
<!-- # |----- -->

<!-- #C# --- Vertical layout -->

<!-- # |----- -->
| Layout description        | Example                                     |
| :------------------------ | :-----------------------------------------: |
| Line break                | A $\newline$ B                              |
| Line break inside braces  | ${\substack{Letters1\\Letters2}}$           |
| Letters on top of letters | $Letters1 \atop Letters2$                   |
| Stacked letters           | $\stackrel{L1}{L2}$ or $\overset{L1}{L2}$   |
| Stacked under letters     | $\underset{Letters1}{Letters2}$             |
| Raise letters             | $Letters1\raisebox{.4em}{Letters2}Letters3$ |
| Superscript               | ${Letters1}^{Letters2}$                     |
| Subscript                 | ${Letters1}_{Letters2}$                     |
<!-- # |----- -->

<!-- # |------------------------------------------------------------- -->

<!-- #C# Logic, set theory -->

<!-- # |------------------------------------------------------------- -->
| Symbol description     | Example                                 |
| :--------------------- | :-------------------------------------: |
| Forall                 | $\forall$                               |
| Exists                 | $\exist$ or $\exists$                   |
| Exists only one        | $\exists!$                              |
| Not exists             | $\nexists$                              |
| Belongs to             | $\in$ or $\isin$                        |
| Not belongs to         | $\notin$                                |
| Contains               | $\ni$ or $\owns$                        |
| Not contains           | $\notni$                                |
| Empty set              | $\empty$ or $\emptyset$                 |
| Nothing                | $\varnothing$                           |
| Strict subset          | $\subset$ or $\sub$                     |
| Subset                 | $\subseteq$ or $\sube$ or $\subseteqq$  |
| Subset not equals      | $\subsetneq$ or $\subsetneqq$           |
| Subset not equals 2    | $\varsubsetneq$ or $\varsubsetneqq$     |
| Not subset             | $\nsubseteq$ or $\nsubseteqq$           |
| Strict superset        | $\supset$                               |
| Superset               | $\supseteq$ or $\supe$ or $\supseteqq$  |
| Superset not equals    | $\supsetneq$ or $\supsetneqq$           |
| Superset not equals 2  | $\varsupsetneq$ or $\varsupsetneqq$     |
| Not superset           | $\nsupseteq$ or $\nsupseteqq$           |
| Square strict subset   | $\sqsubset$                             |
| Square subset          | $\sqsubseteq$                           |
| Square strict superset | $\sqsupset$                             |
| Square superset        | $\sqsupseteq$                           |
| Double subset          | $\Subset$                               |
| Double superset        | $\Supset$                               |
| Complement             | $\complement$                           |
| Logic and              | $\land$                                 |
| Logic or               | $\lor$                                  |
| Logic not              | $\lnot$ or $\neg$                       |
| Implies                | $\implies$                              |
| Implied by             | $\impliedby$                            |
| If and only if         | $\iff$                                  |
| Maps to                | $\mapsto$                               |
| Because                | $\because$                              |
| Therefore              | $\therefore$                            |
| Proves                 | $\vdash$                                |
| Not proves             | $\nvdash$                               |
| Satisfies              | $\models$ or $\vDash$                   |
| Not satisfies          | $\nvDash$                               |
| Proven by              | $\dashv$                                |
| Forces                 | $\Vdash$ or $\Vvdash$                   |
| Not forces             | $\nVdash$ or $\nVDash$                  |
| Falsum                 | $\bot$                                  |
| Verum                  | $\top$                                  |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Operators -->

<!-- # |------------------------------------------------------------- -->
<!-- #C# --- Big operators -->

<!-- # |----- -->
| Operator description     | Example                           |
| :----------------------- | :-------------------------------: |
| Summation                | $\sum$                            |
| Product of a sequence    | $\prod$                           |
| Coproduct                | $\coprod$                         |
| Integral                 | $\int$ or $\intop$ or $\smallint$ |
| Double integral          | $\iint$                           |
| Triple integral          | $\iiint$                          |
| Closed line integral     | $\oint$                           |
| Closed surface integral  | $\oiint$                          |
| Closed volume integral   | $\oiiint$                         |
| OR sequence              | $\bigvee$                         |
| AND sequence             | $\bigwedge$                       |
| XOR sequence             | $\bigoplus$                       |
| XNOR sequence            | $\bigodot$                        |
| Tensor product sequence  | $\bigotimes$                      |
| Arbitrary union          | $\bigcup$                         |
| Arbitrary intersection   | $\bigcap$                         |
| Arbitrary disjoint union | $\biguplus$ or $\bigsqcup$        |
<!-- # |----- -->

<!-- #C# --- Binary operators -->

<!-- # |----- -->
| Operator description                 | Example                         |
| :----------------------------------- | :-----------------------------: |
| Asterisk                             | $\ast$                          |
| Square dot                           | $\centerdot$                    |
| Dot multiplication                   | $\cdot$ or $\cdotp$ or $\ldotp$ |
| Bullet dot                           | $\bullet$                       |
| Times                                | $\times$                        |
| Division                             | $\div$                          |
| Division times                       | $\divideontimes$                |
| Modulo                               | $\bmod A$ or $\mod A$           |
| Ampersand                            | $\And$                          |
| Minus plus                           | $\mp$                           |
| Plus minus                           | $\pm$                           |
| Coproduct                            | $\amalg$                        |
| Antijoin                             | $\rhd$                          |
| Natural join                         | $\bowtie$ or $\Join$            |
| Left semijoin                        | $\ltimes$                       |
| Right semijoin                       | $\rtimes$                       |
| Normal subgroup                      | $\lhd$                          |
| Wreath product                       | $\wr$                           |
| Tensor product                       | $\otimes$                       |
| Logic and                            | $\wedge$ or $\land$             |
| Logic or                             | $\vee$ or $\lor$                |
| Logic nand                           | $\barwedge$                     |
| Logic nor                            | $\veebar$                       |
| Logic xor                            | $\oplus$                        |
| Logic xnor                           | $\odot$                         |
| Union                                | $\cup$                          |
| Intersection                         | $\cap$                          |
| Set subtraction                      | $\setminus$ or $\smallsetminus$ |
| Disjoint union                       | $\uplus$ or $\sqcup$            |
| Square intersection                  | $\sqcap$                        |
| Double union                         | $\doublecup$ or $\Cup$          |
| Double intersection                  | $\doublecap$ or $\Cap$          |
| Function composition                 | $\circ$ or $\bigcirc$           |
| Boxed dot                            | $\boxdot$                       |
| Boxed minus                          | $\boxminus$                     |
| Boxed plus                           | $\boxplus$                      |
| Boxed times                          | $\boxtimes$                     |
| Circled asterisk                     | $\circledast$                   |
| Circled circle                       | $\circledcirc$                  |
| Circled dash                         | $\circleddash$                  |
| Circled minus                        | $\ominus$                       |
| Circled slash                        | $\oslash$                       |
| Circled dot                          | $\odot$ or $\bigodot$           |
| Circled plus                         | $\oplus$ or $\bigoplus$         |
| Circled X                            | $\otimes$ or $\bigotimes$       |
| Three times left                     | $\leftthreetimes$               |
| Three times right                    | $\rightthreetimes$              |
| Plus with dot                        | $\dotplus$                      |
<!-- # |----- -->

<!-- #C# --- Functions -->

<!-- # |----- -->
| Function description     | Example                              |
| :----------------------- | :----------------------------------: |
| Fraction                 | $\frac{A}{B}$ or $A \over B$         |
| Textstyle fraction       | $\tfrac{A}{B}$                       |
| Displaystyle fraction    | $\dfrac{A}{B}$                       |
| Continued fraction       | $\cfrac{A}{B}$                       |
| Combination              | $\binom{n}{k}$ or $n \choose k$      |
| Square root              | $\sqrt{A}$                           |
| General root of a number | $\sqrt[n]{A}$                        |
| Sine                     | $\sin{x}$                            |
| Hyperbolic sine          | $\sinh{x}$ or $\sh{x}$               |
| Arcsine                  | $\arcsin{x}$                         |
| Cosine                   | $\cos{x}$                            |
| Hyperbolic cosine        | $\cosh{x}$ or $\ch{x}$               |
| Arccosine                | $\arccos{x}$                         |
| Tangent                  | $\tan{x}$ or $\tg{x}$                |
| Hyperbolic tangent       | $\tanh{x}$ or $\th{x}$               |
| Arctangent               | $\arctan{x}$ or $\arctg{x}$          |
| Cotangent                | $\cot{x}$ or $\cotg{x}$ or $\ctg{x}$ |
| Hyperbolic cotangent     | $\coth{x}$ or $\cth{x}$              |
| Arccotangent             | $\arcctg{x}$                         |
| Secant                   | $\sec{x}$                            |
| Cosecant                 | $\csc{x}$ or $\cosec{x}$             |
| Logarithm                | $\log{x}$                            |
| Natural logarithm        | $\ln{x}$                             |
| Base 2 logarithm         | $\lg{x}$                             |
| Exponential              | $\exp{x}$                            |
| Determinant              | $\det{x}$                            |
| Maximum                  | $\max{x}$                            |
| Minimum                  | $\min{x}$                            |
| Supremum                 | $\sup{x}$                            |
| Infimum                  | $\inf{x}$                            |
| Greatest common divisor  | $\gcd{x}$                            |
| Limit                    | $\lim{x}$                            |
| Probability limit        | $\plim{x}$                           |
| Hom functor              | $\hom{x}$                            |
| Kernel                   | $\ker{x}$                            |
| Degree of polynomial     | $\deg{x}$                            |
<!-- # |----- -->

<!-- #C# --- Relational operators -->

<!-- # |----- -->
| Operator description     | Example                                       |
| :----------------------- | :-------------------------------------------: |
| Approximately            | $\approx$ or $\thickapprox$                   |
| Approximate or equal     | $\approxeq$                                   |
| Equivalent               | $\equiv$ or $\triangleq$                      |
| Defined by               | $\coloneqq$ or $\Coloneqq$                    |
| Defines                  | $\eqqcolon$ or $\Eqqcolon$                    |
| Not equal                | $\ne$ or $\neq$                               |
| Colon                    | $\colon$ or $\vcentcolon$                     |
| Double colon             | $\dblcolon$                                   |
| Colon tilde              | $\colonsim$ or $\simcolon$                    |
| Double colon tilde       | $\Colonsim$                                   |
| Colon hyphen             | $\coloneq$ or $\eqcolon$                      |
| Double colon hyphen      | $\Coloneq$ or $\Eqcolon$                      |
| Colon tildes             | $\colonapprox$ or $\approxcolon$              |
| Double colon tildes      | $\Colonapprox$                                |
| Congruent                | $\cong$                                       |
| Not congruent            | $\ncong$                                      |
| Similar                  | $\sim$ or $\thicksim$                         |
| Not similar              | $\nsim$                                       |
| Similar or equal         | $\simeq$                                      |
| Proportional to          | $\propto$ or $\varpropto$                     |
| Less than                | $\lt$ or $\text{\textless}$                   |
| Much less than           | $\ll$                                         |
| Triple less than         | $\lll$ or $\llless$                           |
| Less than or equal       | $\le$ or $\leq$ or $\leqq$                    |
| Slanted less or equal    | $\leqslant$ or $\eqslantless$                 |
| Less not equal           | $\lneq$ or $\lneqq$ or $\lvertneqq$           |
| Less or similar          | $\lesssim$                                    |
| Less not similar         | $\lnsim$                                      |
| Less or approximate      | $\lessapprox$                                 |
| Less not approximate     | $\lnapprox$                                   |
| Not less                 | $\nless$                                      |
| Not less or equal        | $\nleq$ or $\nleqq$ or $\nleqslant$           |
| Parallel                 | $\parallel$ or $\shortparallel$               |
| Not parallel             | $\nparallel$ or $\nshortparallel$             |
| Perpendicular            | $\perp$                                       |
| Asymptotic               | $\asymp$                                      |
| Transversal              | $\pitchfork$                                  |
| Greater than             | $\gt$ or $\text{\textgreater}$                |
| Much greater than        | $\gg$                                         |
| Triple greater then      | $\ggg$ or $\gggtr$                            |
| Greater than or equal    | $\ge$ or $\geq$ or $\geqq$                    |
| Slanted greater or equal | $\geqslant$ or $\eqslantgtr$                  |
| Greater not equal        | $\gneq$ or $\gneqq$ or $\gvertneqq$           |
| Greater or similar       | $\gtrsim$                                     |
| Greater not similar      | $\gnsim$                                      |
| Greater or approximate   | $\gtrapprox$                                  |
| Greater not approximate  | $\gnapprox$                                   |
| Not greater              | $\ngtr$                                       |
| Not greater or equal     | $\ngeq$ or $\ngeqq$ or $\ngeqslant$           |
| Greater equal or less    | $\gtreqless$ or $\gtreqqless$                 |
| Greater or less          | $\gtrless$                                    |
| Less equal or greater    | $\lesseqgtr$ or $\lesseqqgtr$                 |
| Less or greater          | $\lessgtr$                                    |
| Covers                   | $\gtrdot$                                     |
| Covered by               | $\lessdot$                                    |
| Same precedence          | $\doteq$                                      |
| Precedes                 | $\prec$                                       |
| Not precedes             | $\nprec$                                      |
| Precedes or equals       | $\preceq$ or $\preccurlyeq$ or $\curlyeqprec$ |
| Precedes not equals      | $\precneqq$                                   |
| Not precedes or equals   | $\npreceq$                                    |
| Precedes or approximate  | $\precapprox$                                 |
| Precedes not approximate | $\precnapprox$                                |
| Precedes or similar      | $\precsim$                                    |
| Precedes not similar     | $\precnsim$                                   |
| Succeeds                 | $\succ$                                       |
| Not succeeds             | $\nsucc$                                      |
| Succeeds or equals       | $\succeq$ or $\succcurlyeq$ or $\curlyeqsucc$ |
| Succeeds not equals      | $\succneqq$                                   |
| Not succeeds or equals   | $\nsucceq$                                    |
| Succeeds or approximate  | $\succapprox$                                 |
| Succeeds not approximate | $\succnapprox$                                |
| Succeeds or similar      | $\succsim$                                    |
| Succeeds not similar     | $\succnsim$                                   |
| Equal or similar         | $\eqsim$                                      |
| Reverse similar or equal | $\backsimeq$                                  |
| Equal with bumps         | $\bumpeq$ or $\Bumpeq$                        |
| Equal with circle        | $\eqcirc$                                     |
| Equal with circle on top | $\circeq$                                     |
| Equal with falling dots  | $\fallingdotseq$                              |
| Equal with rising dots   | $\risingdotseq$                               |
| Equal with double dots   | $\Doteq$ or $\doteqdot$                       |
| Divides                  | $\mid$ or $\shortmid$                         |
| Not divides              | $\nmid$ or $\nshortmid$                       |
<!-- # |----- -->

<!-- # |------------------------------------------------------------- -->

<!-- #C# Arrows -->

<!-- # |------------------------------------------------------------- -->
| Arrow description            | Example                                    |
| :--------------------------- | :----------------------------------------: |
| Left arrow                   | $\gets$ or $\larr$ or $\leftarrow$         |
| Left arrow 2                 | $\longleftarrow$                           |
| Not left arrow               | $\nleftarrow$                              |
| Left double arrow            | $\Larr$ or $\lArr$ or $\Leftarrow$         |
| Left double arrow 2          | $\impliedby$ or $\Longleftarrow$           |
| Not left double arrow        | $\nLeftarrow$                              |
| Right arrow                  | $\to$ or $\rarr$ or $\rightarrow$          |
| Right arrow 2                | $\longrightarrow$                          |
| Not right arrow              | $\nrightarrow$                             |
| Right double arrow           | $\rArr$ or $\Rarr$ or $\Rightarrow$        |
| Right double arrow 2         | $\implies$ or $\Longrightarrow$            |
| Not right double arrow       | $\nRightarrow$                             |
| Left right arrow             | $\leftrightarrow$ or $\lrarr$ or $\harr$   |
| Left right arrow 2           | $\longleftrightarrow$                      |
| Not left right arrow         | $\nleftrightarrow$                         |
| Left right double arrow      | $\lrArr$ or $\Harr$ or $\hArr$ or $\Lrarr$ |
| Left right double arrow 2    | $\iff$ or $\Longleftrightarrow$            |
| Left right double arrow 3    | $\Leftrightarrow$                          |
| Not left right double arrow  | $\nLeftrightarrow$                         |
| Up arrow                     | $\uarr$ or $\uparrow$                      |
| Up double arrow              | $\Uarr$ or $\uArr$ or $\Uparrow$           |
| Down arrow                   | $\darr$ or $\downarrow$                    |
| Down double arrow            | $\Darr$ or $\dArr$ or $\Downarrow$         |
| Up down arrow                | $\updownarrow$                             |
| Up down double arrow         | $\Updownarrow$                             |
| Left harpoon up              | $\leftharpoonup$                           |
| Left harpoon down            | $\leftharpoondown$                         |
| Right harpoon up             | $\rightharpoonup$                          |
| Right harpoon down           | $\rightharpoondown$                        |
| Up harpoon left              | $\upharpoonleft$                           |
| Up harpoon right             | $\restriction$ or $\upharpoonright$        |
| Down harpoon left            | $\downharpoonleft$                         |
| Down harpoon right           | $\downharpoonright$                        |
| Left right harpoons          | $\leftrightharpoons$                       |
| Right left harpoons          | $\rightleftharpoons$                       |
| Right arrow from bar         | $\mapsto$                                  |
| Left dashed arrow            | $\dashleftarrow$                           |
| Right dashed arrow           | $\dashrightarrow$                          |
| Right squiggle arrow         | $\leadsto$ or $\rightsquigarrow$           |
| Left right squiggle arrow    | $\leftrightsquigarrow$                     |
| Left arrow with loop         | $\looparrowleft$                           |
| Right arrow with loop        | $\looparrowright$                          |
| Left arrow with tail         | $\leftarrowtail$                           |
| Right arrow with tail        | $\rightarrowtail$                          |
| Left arrow with hook         | $\hookleftarrow$                           |
| Right arrow with hook        | $\hookrightarrow$                          |
| Left two heads arrow         | $\twoheadleftarrow$                        |
| Right two heads arrow        | $\twoheadrightarrow$                       |
| Left two arrows              | $\leftleftarrows$                          |
| Right two arrows             | $\rightrightarrows$                        |
| Up two arrows                | $\upuparrows$                              |
| Down two arrows              | $\downdownarrows$                          |
| Left right arrows            | $\leftrightarrows$                         |
| Right left arrows            | $\rightleftarrows$                         |
| Left triple arrow            | $\Lleftarrow$                              |
| Right triple arrow           | $\Rrightarrow$                             |
| Up leftwards arrow           | $\Lsh$                                     |
| Up rightwards arrow          | $\Rsh$                                     |
| Up left arrow                | $\nwarrow$                                 |
| Up right arrow               | $\nearrow$                                 |
| Down left arrow              | $\swarrow$                                 |
| Down right arrow             | $\searrow$                                 |
| Left circle arrow            | $\circlearrowleft$                         |
| Right circle arrow           | $\circlearrowright$                        |
| Left semicircle arrow        | $\curvearrowleft$                          |
| Right semicircle arrow       | $\curvearrowright$                         |
| Left text arrow              | $\xleftarrow[L1]{L2}$                      |
| Right text arrow             | $\xrightarrow[L1]{L2}$                     |
| Left text double arrow       | $\xLeftarrow[L1]{L2}$                      |
| Right text double arrow      | $\xRightarrow[L1]{L2}$                     |
| Left right text arrow        | $\xleftrightarrow[L1]{L2}$                 |
| Left right text double arrow | $\xLeftrightarrow[L1]{L2}$                 |
| Left text arrow with hook    | $\xhookleftarrow[L1]{L2}$                  |
| Right text arrow with hook   | $\xhookrightarrow[L1]{L2}$                 |
| Left text two heads arrow    | $\xtwoheadleftarrow[L1]{L2}$               |
| Right text two heads arrow   | $\xtwoheadrightarrow[L1]{L2}$              |
| Left text harpoon up         | $\xleftharpoonup[L1]{L2}$                  |
| Right text harpoon up        | $\xrightharpoonup[L1]{L2}$                 |
| Left text harpoon down       | $\xleftharpoondown[L1]{L2}$                |
| Right text harpoon down      | $\xrightharpoondown[L1]{L2}$               |
| Left right text harpoons     | $\xleftrightharpoons[L1]{L2}$              |
| Right left text harpoons     | $\xrightleftharpoons[L1]{L2}$              |
| Right left text arrows       | $\xtofrom[L1]{L2}$                         |
| Right text arrow from bar    | $\xmapsto[L1]{L2}$                         |
| Two lines text               | $\xlongequal[L1]{L2}$                      |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Style -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# styles are used to change the appearance of the characters -->
| Style description         | Example                                     |
| :------------------------ | :-----------------------------------------: |
| Text color                | $\color{blue}{L1}$ or $\color{#134BF9}{L2}$ |
| Background color          | $\colorbox{aqua}{L1}$                       |
| Outline color             | $\fcolorbox{red}{cyan}{L1}$                 |
| Math roman font           | $\mathrm{L1}$                               |
| Math normal font          | $\mathnormal{L1}$                           |
| Math bold font            | $\mathbf{L1}$                               |
| Math italic font          | $\mathit{L1}$                               |
| Math sans serif font      | $\mathsf{L1}$                               |
| Math blackboard bold font | $\mathbb{L1}$                               |
| Math script font          | $\mathscr{L1}$                              |
| Math calligraphic font    | $\mathcal{L1}$                              |
| Math fraktur font         | $\mathfrak{L1}$                             |
| Math monospace font       | $\mathtt{L1}$                               |
| Text font                 | $\text{L1}$                                 |
| Text roman font           | $\textrm{L1}$                               |
| Text normal font          | $\textnormal{L1}$                           |
| Text upright font         | $\textup{L1}$                               |
| Text medium font          | $\textmd{L1}$                               |
| Text bold font            | $\textbf{L1}$                               |
| Text italic font          | $\textit{L1}$                               |
| Text sans serif font      | $\textsf{L1}$                               |
| Text monospace font       | $\texttt{L1}$                               |
| Roman font                | $\rm{L1}$                                   |
| Bold font                 | $\bf{L1}$ or $\bold{L2}$                    |
| Italic font               | $\it{L1}$                                   |
| Italic bold font          | $\bm{L1}$ or $\boldsymbol{L2}$              |
| Sans serif font           | $\sf{L1}$                                   |
| Blackboard bold font      | $\Bbb{L1}$                                  |
| Fraktur font              | $\frak{L1}$                                 |
| Monospace font            | $\tt{L1}$                                   |
| Huge size 1               | $\Huge L1$                                  |
| Huge size 2               | $\huge L1$                                  |
| Large size 1              | $\LARGE L1$                                 |
| Large size 2              | $\Large L1$                                 |
| Large size 3              | $\large L1$                                 |
| Normal size               | $\normalsize L1$                            |
| Small size                | $\small L1 $                                |
| Footnote size             | $\footnotesize L1$                          |
| Script size               | $\scriptsize L1$                            |
| Tiny size                 | $\tiny L1$                                  |
| Display style             | $\displaystyle L1$                          |
| Text style                | $\textstyle L1$                             |
| Script style              | $\scriptstyle L1$                           |
| Script subscript style    | $\scriptscriptstyle L1$                     |
| Verbatim style            | $\verb°L1°$                                 |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Symbols, punctuation -->

<!-- # |------------------------------------------------------------- -->
| Symbol, punctuation description | Example                                 |
| :------------------------------ | :-------------------------------------: |
| Percent                         | $\%$                                    |
| Hash                            | $\#$                                    |
| Ampersand                       | $\&$                                    |
| Underscore                      | $\_$ or $\text{\textunderscore}$        |
| Dash                            | $-$ or $\text{--}$                      |
| Dash 2                          | $\text{\textendash}$                    |
| Large dash                      | $\text{---}$ or $\text{\textemdash}$    |
| Ascii tilde                     | $\text{\textasciitilde}$                |
| Caret or circumflex             | $\text{\textasciicircum}$               |
| Left quote                      | $\lq$ or $\text{\textquoteleft}$        |
| Right quote                     | $\text{\textquoteright}$                |
| Right apostrophe                | $\rq$                                   |
| Left double quotes              | $\text{\textquotedblleft}$              |
| Right double quotes             | $\text{\textquotedblright}$             |
| Prime                           | $\prime$                                |
| Reversed prime                  | $\backprime$                            |
| Vertical bar                    | $\text{\textbar}$                       |
| Vertical double bar             | $\text{\textbardbl}$                    |
| Backslash                       | $\backslash$ or $\text{\textbackslash}$ |
| Diagonal down                   | $\diagdown$                             |
| Diagonal up                     | $\diagup$                               |
| Transpose                       | $\intercal$                             |
| Reverse tilde                   | $\backsim$                              |
| Multimap                        | $\multimap$                             |
| Upwards arc                     | $\smile$ or $\smallsmile$               |
| Downward arc                    | $\frown$ or $\smallfrown$               |
| Crossed vertical arcs           | $\between$                              |
| Dot                             | $\sdot$                                 |
| Ellipsis                        | $\mathellipsis$ or $\dotsc$ or $\dotso$ |
| Ellipsis 2                      | $\dots$ or $\ldots$                     |
| Ellipsis 3                      | $\text{\textellipsis}$                  |
| Centered ellipsis               | $\cdots$ or $\dotsb$ or $\dotsm$        |
| Centered ellipsis 2             | $\dotsi$                                |
| Vertical ellipsis               | $\vdots$                                |
| Diagonal down ellipsis          | $\ddots$                                |
| Left triangle                   | $\triangleleft$ or $\vartriangleleft$   |
| Filled left triangle            | $\blacktriangleleft$                    |
| Slash left triangle             | $\ntriangleleft$                        |
| Right triangle                  | $\triangleright$ or $\vartriangleright$ |
| Filled right triangle           | $\blacktriangleright$                   |
| Slash right triangle            | $\ntriangleright$                       |
| Underlined left triangle        | $\unlhd$ or $\trianglelefteq$           |
| Slash underlined left triangle  | $\ntrianglelefteq$                      |
| Underlined right triangle       | $\unrhd$ or $\trianglerighteq$          |
| Slash underlined right triangle | $\ntrianglerighteq$                     |
| Up triangle                     | $\triangle$ or $\bigtriangleup$         |
| Up triangle 2                   | $\vartriangle$                          |
| Filled up triangle              | $\blacktriangle$                        |
| Down triangle                   | $\triangledown$ or $\bigtriangledown$   |
| Filled down triangle            | $\blacktriangledown$                    |
| Square                          | $\Box$ or $\square$                     |
| Filled square                   | $\blacksquare$                          |
| Diamond                         | $\diamond$                              |
| Lozenge                         | $\Diamond$ or $\lozenge$                |
| Filled lozenge                  | $\blacklozenge$                         |
| Star                            | $\star$ or $\bigstar$                   |
| Clubs suit                      | $\clubsuit$ or $\clubs$                 |
| Diamonds suit                   | $\diamondsuit$ or $\diamonds$           |
| Hearts suit                     | $\heartsuit$ or $\hearts$               |
| Spades suit                     | $\spadesuit$ or $\spades$               |
| Sharp accidental                | $\sharp$                                |
| Natural accidental              | $\natural$                              |
| Flat accidental                 | $\flat$                                 |
| Maltese cross                   | $\maltese$                              |
| Pilcrow                         | $\text{\P}$                             |
| Silcrow                         | $\text{\S}$ or $\text{\sect}$           |
| Copyright                       | $\copyright$                            |
| Registered                      | $\text{\textregistered}$                |
| Circled R                       | $\circledR$                             |
| Circled S                       | $\circledS$                             |
| Degree                          | $\degree$ or $\text{\textdegree}$       |
| Radical                         | $\surd$                                 |
| Dollar                          | $\$$ or $\text{\textdollar}$            |
| Pounds                          | $\pounds$ or $\mathsterling$            |
| Pounds 2                        | $\text{\textsterling}$                  |
| Yen                             | $\yen$                                  |
| Angle                           | $\angle$ or $\measuredangle$            |
| Spherical angle                 | $\sphericalangle$                       |
| Dagger                          | $\dag$ or $\dagger$                     |
| Dagger 2                        | $\text{\textdagger}$                    |
| Double dagger                   | $\ddag$ or $\ddagger$ or $\Dagger$      |
| Double dagger 2                 | $\text{\textdaggerdbl}$                 |
| Checkmark                       | $\checkmark$                            |
| Tex                             | $\TeX$                                  |
| Latex                           | $\LaTeX$                                |
| Katex                           | $\KaTeX$                                |
<!-- # |------------------------------------------------------------- -->