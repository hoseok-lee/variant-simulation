Given $X_i$ to be a binomially distributed variable of one test $n = 1$ with
probability of success $p_i$, the mean and variance is given by

$$\mu_i = p_i$$
$$\sigma_i^2 = p_i (1 - p_i)$$

Let $\epsilon = 1$ for simplicity. The upper bound for $3$rd moment of the
variates $X_i$ can be computed as

$$
\begin{align*}
r_n^3 &= \sum_{i = 1}^n | X_i - p_i |^3 \\
&< \sum_{i = 1}^n | 1 |^3 \\
&< n
$$
