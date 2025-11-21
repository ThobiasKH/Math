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

# Mega Super Awesome Ultimate 3D Notes
**Author:** Thobias K. Høivik  
**Date:** Fall Semester 2025 B.C.

---

## Table of Contents
- [Linear Algebra](#linear-algebra)
- [Real Analysis](#real-analysis)
- [Hilbert Spaces](#hilbert-spaces)
- [Topology](#topology)
- [Probability](#probability)

---

## Linear Algebra


**Definition: Vector Space**

A **vector space** over a field $\mathbb{F}$ is a set $V$ together with two operations (vector addition and scalar multiplication) satisfying the usual axioms (associativity, distributivity, identity elements, inverses, etc.).




**Theorem: Rank-Nullity Theorem**

For a linear transformation $T: V \to W$ between finite-dimensional vector spaces,  
$$
\text{dim}(\ker T) + \text{dim}(\operatorname{im} T) = \text{dim}(V)
$$




**Proof**

Choose a basis for $\ker T$ and extend it to a basis of $V$. The images of the additional basis vectors form a basis of $\operatorname{im} T$. 
Counting dimensions gives the formula. 

---

## Real Analysis


**Definition: Uniform Convergence**

A sequence of functions $\{f_n\}$ converges **uniformly** to $f$ on a set $A$ if  
$$
\forall \epsilon > 0, \exists N \text{ such that } n > N \implies |f_n(x) - f(x)| < \epsilon \ \forall x \in A
$$




**Theorem: Weierstrass M-Test**

Let $\{f_n\}$ be a sequence of functions on $A$, and suppose $|f_n(x)| \le M_n$ for all $x \in A$.  
If $\sum M_n$ converges, then $\sum f_n$ converges **uniformly** on $A$.



---

## Hilbert Spaces


**Definition: Inner Product Space**

A **Hilbert space** is a complete inner product space $(H, \langle \cdot, \cdot \rangle)$ where the norm is induced by the inner product: $\|x\| = \sqrt{\langle x, x \rangle}$.




**Lemma: Cauchy-Schwarz Inequality**

For all $x, y \in H$,  
$$
|\langle x, y \rangle| \le \|x\| \cdot \|y\|
$$




**Proof**

Consider the vector $x - \frac{\langle x, y\rangle}{\|y\|^2} y$. Its norm squared is nonnegative:

$$
\|x - \frac{\langle x, y\rangle}{\|y\|^2} y\|^2 \ge 0
$$

Expanding and simplifying gives the inequality.



---

## Topology


**Definition: Open Set**

A set $U$ in a topological space $(X, \tau)$ is **open** if $U \in \tau$.




**Proposition: Union of Open Sets**

The union of any collection of open sets is open.




**Proof**

Follows directly from the definition of a topology: $\bigcup_{\alpha} U_\alpha \in \tau$.



---

## Probability


**Definition: Expected Value**

For a discrete random variable $X$ taking values $x_i$ with probabilities $p_i$,  
$$
\mathbb{E}[X] = \sum_i x_i p_i
$$




**Theorem: Law of Large Numbers (Weak)**

Let $X_1, X_2, \dots$ be i.i.d. with mean $\mu$ and variance $\sigma^2 < \infty$. Then

$$
\overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i \to \mu \quad \text{in probability as } n \to \infty.
$$




**Proof (Sketch)**

By Chebyshev's inequality:

$$
\mathbb{P}(|\overline{X}_n - \mu| \ge \epsilon) \le \frac{\sigma^2}{n \epsilon^2} \to 0
$$



---

