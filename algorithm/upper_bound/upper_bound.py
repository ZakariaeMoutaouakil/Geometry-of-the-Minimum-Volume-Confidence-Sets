from math import log, exp
from typing import Tuple


def kl_divergence(p_hat: Tuple[float, ...], p: Tuple[float, ...]) -> float:
    """
    Calculate the Kullback-Leibler divergence from p to p_hat.

    Args:
    p_hat (List[float]): Estimated probabilities.
    p (List[float]): True probabilities.

    Returns:
    float: The KL divergence value.
    """
    kl_div = 0.0
    for ph, pt in zip(p_hat, p):
        if ph > 0 and pt > 0:
            kl_div += ph * log(ph / pt)
    return kl_div


def evaluate_upper_bound(p: Tuple[float, ...], x: Tuple[int, ...]) -> float:
    """
    Compute the value of the expression (n + 1)^(2k) * exp(-n * KL(p_hat, p)).

    Args:
    n (int): Sample size or total number of observations.
    p (List[float]): True probability distribution.
    p_hat (List[float]): Estimated probability distribution.

    Returns:
    float: Computed value of the formula.
    """
    # Transform the data into probabilities
    n = sum(x)
    p_hat = tuple([x_i / n for x_i in x])

    # Calculate the KL divergence
    kl = kl_divergence(p_hat, p)

    # Calculate the length of p
    k = len(p)

    # Compute the full expression
    result = ((n + 1) ** (2 * k)) * exp(-n * kl)
    return result


if __name__ == "__main__":
    # Example usage
    p_ = (0.001, 0.999)
    x_ = (3, 2, 1)

    bound = evaluate_upper_bound(p_, x_)
    print(f"Result of the formula: {bound}")
