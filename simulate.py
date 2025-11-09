import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import norm, kstest


def plot_dist_with_norm(
    dist: np.ndarray,
    mu: float,
    std: float,
    figure: str
):

    x = np.linspace(150, 250, 5000)
    y = norm.pdf(
        x,
        loc = mu,
        scale = std
    )

    plt.clf()
    plt.hist(
        dist,
        bins = 20,
        density = True,
        label = "Experimental"
    )
    plt.plot(x, y, label = "Theoretical")
    plt.legend()
    plt.xlabel("Total Number of Variants")
    plt.ylabel("Probability Density")
    plt.savefig(figure)


def single_bernoulli(mafs):
    ber_test = np.random.rand(mafs.shape[0])
    return (mafs['maf'].values > ber_test).sum()

def bernoulli_test(
    mafs: pd.DataFrame,
    n_patients: int
):

    np.random.seed(0)

    dist = np.array([
        single_bernoulli(mafs)
        for _ in range(n_patients)
    ])

    mu, std = norm.fit(dist)

    plot_dist_with_norm(dist, mu, std, figure = "bernoulli.png")
    res, p = kstest((dist - mu) / std, "norm")

    return mu, std, res, p, dist


def normal_test(
    mafs: pd.DataFrame,
    n_patients: int,
    bernoulli: np.ndarray
):

    # Compute with hypothesized
    mu = mafs['maf'].sum()
    std = np.sqrt((mafs['maf'] * (1 - mafs['maf'])).sum())

    dist = norm.rvs(
        loc = mu,
        scale = std,
        size = n_patients
    )

    plot_dist_with_norm(dist, mu, std, figure = "normal.png")
    res, p = kstest(dist, bernoulli)

    return mu, std, res, p, dist


mafs = pd.read_csv(
    "mafs.tsv",
    delimiter = "\t",
    index_col = 0
)

n_patients = 50000

mu_b, std_b, res_b, p_b, dist_b = bernoulli_test(mafs, n_patients)
mu_n, std_n, res_n, p_n, dist_n = normal_test(mafs, n_patients, dist_b)

df = pd.DataFrame(
    {
        'mean':     [mu_b, mu_n],
        'std':      [std_b, std_n],
        'ks_test':  [res_b, res_n],
        'pvalue':   [p_b, p_n]
    },
    index = ["bernoulli", "normal"]
)

print(df)
