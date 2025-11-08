# Problem Formulation

> Given a table of $n$ variants $v_i$ with associated minor allele frequencies (MAF) $P(v_i)$, is it possible to model the distribution of the number of variants any certain individual is expected to carry?

# Solution

The "ground-truth" distribution can be simulated by generating individuals by
iterating through the entire list of variants, sampling a uniform distribution
for each variant to determine whether the variant is present in the individual,
and creating histogram of the total sum of variants.

TODO: Solve it!

# Usage

To retrive minor allele frequencies from Ensembl BioMart, use

```
python get_mafs.py 10000 --outfile mafs.tsv
```

To perform simulations, use

```
python simulate.py
```
