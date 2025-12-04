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
  - \usepackage{booktabs}
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

# Exam practice questions 

## Prøveeksamen 2023 

### Oppgave 1 

La A være matrisen gitt ved 

$$ 
    \begin{bmatrix} 
    2 & 6 & 2 & -1 \\ 
    1 & -3 & -4 & 2 \\ 
    -5 & 15 & 0 & 0 \\ 
    -1 & 3 & -2 & 1
    \end{bmatrix}
$$ 

a) Finn en basis til nullrommet til A og en basis for kolonnerommet. 

b) Finn en ortonormal basis for nullrommet. 

**Løsning a).**

Vi ser fort at det er 3 lineært uavhengige kolonnevektorer i A. 

Siden $\dim \ker T + \dim \text{im} T = 4$ vet vi at kjernen 
er 1-dimensjonell. For kolonnerommet velg de 3 lineært uavhengige 
vektorene. 

Nullrommet $\ker A = \{x \in \mathbb R^4 : Ax = 0\}$. 

$$ 
    \begin{bmatrix} 
    2 & 6 & 2 & -1 \\ 
    1 & -3 & -4 & 2 \\ 
    -5 & 15 & 0 & 0 \\ 
    -1 & 3 & -2 & 1
    \end{bmatrix} 
    \begin{bmatrix}
        x_1 \\ x_2 \\ x_3 \\ x_4
    \end{bmatrix}
    = 0 
$$ 
$$ 
    \begin{cases}
        2x_1 + 6x_2 + 2x_3 - x_4 = 0 \\ 
        x_1 - 3x_2 -4x_3 + 2x_4 = 0 \\ 
        -5x_1 + 15x_2 = 0 \\ 
        -x_1 + 3x_2 - 2x_3 + x_4 = 0 
    \end{cases}
$$ 

Vi får at $-6x_3 + 3x_4 = 0$ samt $-5x_1 + 15x_2 = 0$. 
Med andre ord: 
$$ 
    x_1 = 3x_2 \\ 
    2x_3 = x_4
$$ 
Vi velger 
$$ 
    \begin{bmatrix}
        0 \\ 
        0 \\ 
        1 \\ 
        2
    \end{bmatrix}
$$ 

**Løsning b).** 
$$ 
    \frac{1}{\sqrt{1+4}} 
    \begin{bmatrix}
        0 \\ 
        0 \\ 
        1 \\ 
        2
    \end{bmatrix}
$$ 

--- 

### Oppgave 2 

La $V = \mathcal P_1$ være vektorromet av polynomer av 
grad høgst $1$.

La $T,S: V \to V$ være definert ved 
$$ 
    Tp = p(1) + p(0)t \text{ og } Sp = p+t
$$ 

a) Vis at $T$ er en lineærtransformasjon, men at $S$ ikke er det. 

b) Finn $[T]_{\mathcal B}$ hvor $\mathcal B = \{1,t\}$ er en basis for V.

**Bevis for a).**  
T er veldefinert siden $p(1),p(0) \in \mathbb K$ og 
$\mathcal P_1 = \{c_0 + c_1t \mid c_0,c_1 \in \mathbb K\}$.

Videre ser vi at den er lineær siden 
$$ 
    T(p+q) = p(1) + p(0)t + q(1) + q(0)t = Tp + Tq
$$ 
og 
$$ 
    T(\alpha p) = \alpha p(1) + \alpha p(0)t = \alpha(p(1) + p(0)t) 
    = \alpha Tp
$$ 

Merk at selv om $S$ er veldefinert siden $\mathcal P_1$ er lukket 
under $+$ og $t \in \mathcal P_1$, se dette moteksempellet på 
lineæritet: 
$$ 
    S(t + t) = (t+t) + t = 3t
$$ 
men 
$$ 
    St + St = (t+t) + (t+t) = 4t
$$ 

--- 
## MAT1120 2023

### Oppgave 3 

La $V$ være rommet av funksjoner på formen 
$$ 
    f(x) = ae^x + be^{-x}
$$ 
der $a,b \in \mathbb{R}$. 
La 
$$
    \cosh (x) = \frac{1}{2} (e^x + e^{-x}) 
    \text{ og } 
    \sinh (x) = \frac{1}{2}(e^x - e^{-x})
$$ 

a) La $\mathcal B = \{e^x, e^{-x}\}$. Begrunn at $\mathcal B$ er 
en basis for $V$.

**Løsning a).**

Det er tydelig at $\text{span}\mathcal B = V$ siden $V$, per 
definisjon, er lineære kombinasjoner av funksjonene i 
$\mathcal B$. Så det som gjenstår er å vise at $\mathcal B$ er 
lineært uavhengig. 

Anta at 
$$ 
    \alpha e^x + \beta e^{-x} = 0 
$$ 

Da får vi at 
$$ 
    \alpha e^x + \frac{\beta}{e^x} = \frac{\alpha e^{2x} + \beta}{e^x}
    = 0
$$ 

siden $e^x \neq 0, \forall x\in \mathbb{R}$ får vi da 
$$ 
    \alpha e^{2x} = -\beta
$$ 
men dette betyr da at $\alpha e^{2x}$ er konstant, så 
$$ 
    \frac{d}{dx}\alpha e^{2x} = 0
$$ 
men
$$ 
    \frac{d}{dx} \alpha e^{2x} = 2\alpha e^{2x}
$$ 
som aldri er $0$, utenom når $\alpha = 0$, men 
da får vi også at $\beta = 0$. 
Dermed finnes det ingen ikke-trivielle løsninger for 
$$ 
    \alpha e^x + \beta e^{-x} = 0
$$ 
Med andre ord er de lineært uavhengige og $\text{span}\mathcal B = V$,
altså en basis for $V$.

b) 
La $\mathcal B' = \{\cosh (x), \sinh (x)\}$. Bergunn at dette 
også utgjør en basis for $V$, og finn overgansmatrisen $P$ 
fra $\mathcal B$ til $\mathcal B'$, altså matrisen slik at 
$$ 
    [f]_{\mathcal B'} = P [f]_{\mathcal B}, \forall f \in V
$$ 

**Løsning b).**

Vi sjekker lineær avhengighet først. 

$$ 
    \alpha \cosh (x) + \beta \sinh (x) 
    = \frac{\alpha}{2} (e^x + e^{-x}) + 
    \frac{\beta}{2}(e^x - e^{-x})
    \\ 
    = (\alpha/2 + \beta/2) e^x + (\alpha/2 - \beta/2)e^{-x} 
$$ 
For at dette skal være $0$ trenger vi 
$$ 
    \alpha + \beta + \alpha - \beta = 0 
$$ 
så $\alpha = 0$, men dette medfører at $\beta = 0$. 

Vi ser at elementene i $\mathcal B'$ er lineære kombinasjoner 
av de i $\mathcal B$ dermed får vi at 
$$ 
    \text{span}\mathcal B \subseteq \text{span}\mathcal B'
$$ 
men vi har også 
$$ 
    \text{span}\mathcal B' \subseteq \text{span}\mathcal B
$$ 
siden 
$$ 
    \cosh x + \sinh x = e^x
$$ 
og 
$$ 
    \cosh x - \sinh x = e^{-x} 
$$ 
Dermed får vi at 
$$ 
    \text{span} \mathcal B = \text{span}\mathcal B'
$$ 

For å finne overgangsmatrisen må vi finne 
$$ 
    [e^x]_{\mathcal B'} \text{ og } [e^{-x}]_{\mathcal B'}
$$ 
som vi nå vet til å være 
$$ 
    [e^x]_{\mathcal B'} = \cosh(x) + \sinh(x) = (1,1) 
$$ 
$$ 
    [e^{-x}]_{\mathcal B'} = \cosh(x) - \sinh(x) = (1,-1)
$$ 
så 
$$ 
    P = 
    \begin{bmatrix}
        1 & 1 \\ 
        1 & -1
    \end{bmatrix}
$$ 
