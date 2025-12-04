---
pandoc_:
  - output: .pdf
  - pdf-engine: xelatex
header-includes:
  - \usepackage{amsmath, amssymb, amsthm, mathtools}
  - \usepackage[paperwidth=7.5in, paperheight=10in, left=0.8in, right=0.8in, top=1in, bottom=1in]{geometry}
  - \usepackage{fontspec}
  - \usepackage{setspace}
  - \setmainfont{JetBrains Mono}
  - \setstretch{1.4}
  - \usepackage{xcolor}
  - \pagecolor[rgb]{0.15, 0.15, 0.15}
  - \color[rgb]{0.9,0.9,0.9}
  - \makeatletter
  - \renewcommand{\hrulefill}{\color{gray}\leaders\hrule height 0.4pt\hfill\kern0pt}
  - \makeatother
  - \usepackage{hyperref}
  - \makeatletter
  - \renewcommand{\hrule}{\color{gray}\rule{\paperwidth}{0.4pt}}
  - \makeatother
---

# Exam Practice 

Let the structure $\mathcal M = (\mathbb N, <, 0)$. 
Where $<^\mathcal M$ is the usual strict order on the naturals and 
$0^\mathcal M$ is $0 \in \mathbb{N}$.
Determine which 
of the following are true in $\mathcal M$: 

- a) $\forall x \exists y (x < y)$ 
- b) $\exists y \forall x (x < y)$ 
- c) $\exists x (x < 0)$
- d) $\forall x \exists y (y < x)$

**Solutions.**  

a) This formula is true with the usual strict order on 
$\mathbb{N}$ since the successor of any natural number is 
strictly larger than it. 
I.e. $\mathcal M \vDash \forall x \exists y (x < y)$.

b) This formula is not true. There does not exist any natural number 
greater than all other natural numbers as this would imply 
$$ 
    y < y
$$ 
which is true for precisely none of the natural numbers. 
$\mathcal M \nvDash \exists y \forall x (x < y)$.

c) Again, not true. $0$ is smaller than every other natural number.  

d) Again, not true in $\mathcal M$. Same reasoning as in c). 

--- 

Decide whether the following are valid, satisfiable, but not valid or 
unsatisfiable: 

- a) $\exists x P(x) \rightarrow \forall x P(x)$ 
- b) $\forall x (P(x) \lor \lnot P(x))$
- c) $\forall x P(x) \land \exists x \lnot P(x)$ 

**Solutions.**

a) This formula is satisfiable, vaccuously so in any model 
with only one element in the universe, but it is not valid since 
there are structures in which this is not true. 

Short example: 
Let $\mathcal M = (\{a,b\}, P)$, where $P^\mathcal M = \{a\}$. 

b) This is a tautology, hence true in every structure.

c) This is a contradiction so not true in any structure.

