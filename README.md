# Problem Formulation

> Given a table of $n$ variants $v_i$ with associated minor allele frequencies (MAF) $P(v_i) = p_i$, is it possible to model the distribution of the total number of variants any certain individual is expected to carry?

# Solution

The "ground-truth" distribution can be simulated by generating individuals,
iterating through the entire list of variants, sampling a uniform distribution
for each variant to determine whether the variant is present in the individual
(individual Bernoulli tests) and creating a histogram of the total sum of
variants with successful tests.

Considering each variant $X_i$ to be binomial distribution of exactly one test
(i.e. does the patient exhibit this variant or no?) with probability $p_i$ of
success, the [mean and variance](https://en.wikipedia.org/wiki/Binomial_distribution#Expected_value_and_variance)
of $X_i$ is $\mu_i = p_i$ and $\sigma_i^2 = p_i (1 - p_i)$. Further considering
each of these random variables to be independent, the sum of all variants
$X = \sum_i^n X_i$ will have a mean and variance of

$$\mu = \sum_i^n \mu_i = \sum_i^n p_i$$
$$\sigma^2 = \sum_i^n \sigma_i^2 = \sum_i^n p_i (1 - p_i)$$

Due to the Central Limit Theorem (CTL), the total number of variants any
individual carries is normally distributed with mean $\mu$ and variance
$\sigma^2$.

# Usage

To retrive ten thousand minor allele frequencies from Ensembl BioMart, use

```
python get_mafs.py 10000 --outfile mafs.tsv
```

To perform simulations with ten thousand patients, use

```
python simulate.py 10000 --mafs mafs.tsv
```
