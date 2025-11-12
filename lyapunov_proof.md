Given $X_i$ to be a binomially distributed variable of one test $n = 1$ with
probability of success $p_i$, the mean and variance is given by

$$\mu_i = p_i$$
$$\sigma_i^2 = p_i (1 - p_i)$$

Let $\epsilon = 1$ for simplicity. The upper bound for $(2 + \epsilon)$ th 
moment of the variates $X_i$ can be computed by assuming that all variables have 
probability of success $p_i = 0$ and outcome $X_i = 1 \ \forall \ i$.

$$
\begin{align*}
r_n^3 &= \sum_{i = 1}^n | X_i - p_i |^3 \\
&\le \sum_{i = 1}^n | 1 |^3 \\
&\le n
\end{align*}
$$

The lower bound for the sum of variances can be identified by assuming 
$p_i = \alpha \ \forall \ i$ to be an extremely small non-zero probability (in 
the real-world context, this value would be close to $1 \times 10^{-9}$, or the 
probability of the variant being present in only one individual from the world 
population). Our sum of variances has a lower bound

$$
\begin{align*}
s_n^2 &= \sum_{i = 1}^n p_i (1 - p_i) \\
&\le \sum_{i = 1}^n \alpha (1 - \alpha) \\
&\le n \alpha (1 - \alpha)
\end{align*}
$$

The upper bound for our limit 

$$
\begin{align*}
\lim_{n \to \infty} \frac{r_n}{s_n} &\le \lim_{n \to \infty} \frac{\sqrt[3]{n}}{\sqrt{n \alpha (1 - \alpha)}} \\
&\le \lim_{n \to \infty} \frac{1}{\sqrt{\alpha (1 - \alpha)}} \frac{n^{1/3}}{n^{1/2}} \\
&\le \lim_{n \to \infty} \frac{1}{\sqrt{\alpha (1 - \alpha)}} \frac{1}{n^{1 / 6}} \\
&\le 0
\end{align*}
$$

converges to $0$, therefore the Lyapunov condition must also converge to $0$ as 
$n \to \infty$. Our condition is met and the Central Limit Theorem is 
applicable.
