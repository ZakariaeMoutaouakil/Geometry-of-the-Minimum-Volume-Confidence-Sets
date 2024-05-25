import math
from typing import List


def kl_divergence(p_hat: List[float], p: List[float]) -> float:
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
            kl_div += ph * math.log(ph / pt)
    return kl_div


def evaluate_upper_bound(n: int, p: List[float], p_hat: List[float]) -> float:
    """
    Compute the value of the expression (n + 1)^(2k) * exp(-n * KL(p_hat, p)).

    Args:
    n (int): Sample size or total number of observations.
    p (List[float]): True probability distribution.
    p_hat (List[float]): Estimated probability distribution.

    Returns:
    float: Computed value of the formula.
    """
    # Calculate the KL divergence
    kl = kl_divergence(p_hat, p)

    # Calculate the length of p
    k = len(p)

    # Compute the full expression
    result = (n + 1) ** (2 * k) * math.exp(-n * kl)
    return result


if __name__ == "__main__":
    # Example usage
    n_ = 100
    p_ = [0.4, 0.6]
    p_hat_ = [0.5, 0.5]

    bound = evaluate_upper_bound(n_, p_, p_hat_)
    print(f"Result of the formula: {bound}")
