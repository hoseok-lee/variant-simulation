Given $X_i$ to be a one-test binomially distributed random variable $n = 1$ with 
probability of success $p_i \in (0, 1]$,

$$\mu_i = p_i$$
$$\sigma_i^2 = p_i (1 - p_i)$$

We must prove that the mean of a series of binomially distributed variables 
$X_i$ meets [Lyapunov's condition for the Central Limit Theorem](https://mathworld.wolfram.com/LyapunovCondition.html). 
Let $\epsilon = 1$ for simplicity. The upper bound for the $(2 + \epsilon)$ th 
moment of the variates $X_i$ can be computed by assuming that all variables have 
probability of success $p_i = 1$ and outcome $X_i = 0 \ \forall \ i$.

$$
\begin{align*}
r_n^3 &= \sum_{i = 1}^n \mathbb{E} \ \left[ | X_i - p_i |^3 \right] \\
&\le \sum_{i = 1}^n \mathbb{E} \ \left[ | 1 |^3 \right] \\
&\le n
\end{align*}
$$

The lower bound for the sum of variances can be identified by assuming 
$p_i = \alpha \ \forall \ i$ to be an extremely small non-zero probability (in 
the real-world context, this value would be close to $1 \times 10^{-9}$, or the 
probability of the variant being present in only one individual from the world 
population). The lower bound becomes

$$
\begin{align*}
s_n^2 &= \sum_{i = 1}^n p_i (1 - p_i) \\
&\ge \sum_{i = 1}^n \alpha (1 - \alpha) \\
&\ge n \alpha (1 - \alpha)
\end{align*}
$$

The upper bound for our limit 

$$
\begin{align*}
\frac{r_n}{s_n} &\le \frac{n^{1/3}}{\left[ n \alpha (1 - \alpha) \right]^{1/2}} \\
\lim_{n \to \infty} \ \frac{r_n}{s_n} &\le \lim_{n \to \infty} \ \frac{n^{1/3}}{\left[ n \alpha (1 - \alpha) \right]^{1/2}} \\
&\le \frac{1}{\left[ \alpha (1 - \alpha) \right]^{1/2}} \cdot \lim_{n \to \infty} \ \frac{n^{1/3}}{n^{1/2}} \\
&\le \frac{1}{\left[ \alpha (1 - \alpha) \right]^{1/2}} \cdot \lim_{n \to \infty} \ \frac{1}{n^{1/6}} \\
&\le 0
\end{align*}
$$

converges to $0$, therefore the Lyapunov condition must also converge to $0$ as 
$n \to \infty$. The Central Limit Theorem is applicable.
