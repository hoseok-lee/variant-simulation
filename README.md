# Problem Formulation

> Given a table of $n$ variants $v_i$ with associated minor allele frequencies (MAF) $P(v_i) = p_i$, is it possible to model the distribution of the number of variants any certain individual is expected to carry?

# Solution

The "ground-truth" distribution can be simulated by generating individuals by
iterating through the entire list of variants, sampling a uniform distribution
for each variant to determine whether the variant is present in the individual,
and creating histogram of the total sum of variants.

Considering each variant $X_i$ to be binomial distribution of exactly one test
(i.e. does the patient exhibit this variant or no?) with probability $p_i$ of
success, the [mean and variance](https://en.wikipedia.org/wiki/Binomial_distribution#Expected_value_and_variance)
of $X_i$ is $\mu_i = p_i$ and $\sigma_i^2 = p_i (1 - p_i)$. Further considering
each of these random variables to be independent, the sum of all variants
$X = \sum X_i$ will have a mean and variance of

$$\mu = \sum \mu_i = \sum p_i$$
$$\sigma^2 = \sum \sigma_i^2 = \sum p_i (1 - p_i)$$

Due to the Central Limit Theorem (CTL), the total number of variants any
individual carries is normally distributed with mean $\mu$ and variance
$\sigma^2$.

# Usage

To retrive minor allele frequencies from Ensembl BioMart, use

```
python get_mafs.py 10000 --outfile mafs.tsv
```

To perform simulations, use

```
python simulate.py
```
