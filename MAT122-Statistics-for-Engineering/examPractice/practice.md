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

## Oppgave --- Sannsynlighet og betinget sannsynlighet 

I en produksjonsbedrift kan en komponent enten være:

- H = helt feilfri (60%)

- M = mindre feil (30%)

- A = alvorlig feil (10%)

En maskin tester komponentene og har følgende egenskaper:

- Hvis komponenten har alvorlig feil (A), markerer maskinen feil med sannsynlighet 0.94

- Hvis komponenten er mindre feil (M), markerer den feil med sannsynlighet 0.40

- Hvis den er feilfri (H), markerer den feil med 0.02

a) Hva er sannsynligheten for at en tilfeldig valgt komponent 
blir markert som feil? 

**Løsning:** 

$$ 
    60\% \times 0.02 + 30\% \times 0.40 + 10\% \times 0.94 
    = 0.226 = 22.6\%
$$ 

b) Hva er sannsynligheten for at at en komponent har feil, gitt 
at den blir markert som feil? 

**Løsning** 

Husk at 
$$ 
    P(A\mid B) = \frac{P(A\cap B)}{P(B)} = \frac{P(A)P(B \mid A)}{P(B)}
$$ 

så  
$$ 
    P(\text{Alvorlig Feil}\mid\text{Markert som feil}) 
    = \frac{10\% \times 94\%}{22.6\%} \approx 41.6\%
$$ 

c) Er hendelsene “komponenten har alvorlig feil” og “maskinen markerer feil” uavhengige? Begrunn.

**Løsning:** 

De to hendelsene er ikke uavhengige siden for at de skal være 
uavhengige trenger vi at 
$$ 
    P(\text{Alvorlig Feil}\mid \text{Markert som feil}) 
    = P(\text{Alvorlig Feil})
$$ 

og vi har 
$$
\begin{aligned}
    P(\text{Alvorlig Feil} \mid \text{Markert som feil}) &\approx 41.6\%
    \\ 
    P(\text{Alvorlig Feil}) &= 10\%
\end{aligned}
$$
dermed er de ikke uavhengige. 

---

## Oppgave --- Binomisk Fordeling 

En sensor registrerer om en maskin er over oppvarmingsgrensen. Sannsynligheten for at maskinen “feiler” (for varm) i en tilfeldig måling er 0.12.

Sensoren gjør **n = 30** målinger hver dag.

a) Hva er sannsynligheten for at den registrerer akkurat 5 feil?

**Løsning:** 

$$ 
\begin{aligned}
    P(X=5)=\binom{30}{5} \cdot 0.12^5 \cdot 0.88^{25} 
    = 0.1451\ldots \approx 14.5\% 
\end{aligned}
$$ 

b) Hva er sannsynligheten for at en komponent har alvorlig feil, gitt at maskinen markerer feil?

$$
\begin{aligned}
    P(X \leq 3) &= \sum_{x=0}^3 P(X = x) \\ 
    &= \left(\binom{30}{0}0.12^0 \cdot 0.88^{30}\right)
    +  \left(\binom{30}{1}0.12^1 \cdot 0.88^{29}\right) \\
    &+ \left(\binom{30}{2}0.12^2 \cdot 0.88^{28}\right) 
    +  \left(\binom{30}{3}0.12^3 \cdot 0.88^{27}\right) \\
    &= 0.0216\ldots + 0.08836\ldots + 0.1747\ldots + 0.2223\ldots \\ 
    &\approx 50.6\% 
\end{aligned}
$$

c) Hva er sannsynligheten for minst 1 feil?

**Løsning:**

$$ 
    P(X \geq 1) = 1 - P(X = 0) \approx 1-0.0216 = 0.9784
$$ 

d) Forklar hvorfor binomialmodellen er passende.

**Løsning:**

Vi har en sannsynlighet for at noe skjer og et antall forsøk. 
Da passer binomisk bra. 

--- 

## Oppgave --- Hypotesetest for middelverdi ($\sigma$ kjent)

A machine is designed to cut metal rods to a length of 80.0 mm with known standard deviation σ = 0.6 mm.

A sample of 50 rods gives
$$ 
    \overline X = 79.84 \text{mm}
$$  

Test at $5\%$ significance level whether the machine is cutting 
longer or shorter than intended. 

**Solution:** 

We set up the following hypothesis: 

$H_0: \text{Machine is cutting as long as intended.}$

$H_1: \text{Machine is not cutting as long as intended.}$ 

$$ 
    \begin{cases} 
        H_0: \mu = 80.0\text{mm} \\ 
        H_1: \mu \neq 80.0\text{mm}
    \end{cases}
$$ 

$\sigma$ is known, hence we use a Z test where we 

Discard $H_0$ if $|Z| > Z_{\alpha/2} = Z_{0.025}$. 

$$
\begin{aligned}
    Z &= \frac{\overline X - \mu_0}{\sigma/\sqrt n} 
    = \frac{79.84 - 80}{0.6\sqrt{50}} \\ 
    &= -1.88\ldots
\end{aligned}
$$

We find in a table that 
$$ 
    Z_{0.025} \approx 0.49 < \left|Z\right|
$$ 

Thus we discard $H_0$ and conclude that the machine is indeed 
not cutting the rods to the correct length.
