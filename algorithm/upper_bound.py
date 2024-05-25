import math
from typing import List


def kl_divergence(p_hat: List[float], p: List[float]) -> float:
    """
    Calculate the Kullback-Leibler divergence KL(p_hat || p).

    Args:
    p_hat (List[float]): The estimated probabilities.
    p (List[float]): The true probabilities.

    Returns:
    float: The KL divergence.
    """
    return sum(ph * math.log(ph / pi) for ph, pi in zip(p_hat, p) if ph > 0)


def upper_bound(n: int, k: int, p: List[float], p_hat: List[float]) -> float:
    """
    Calculate the value of the formula (n + 1)^(2k) * exp(-n * KL(p_hat, p)).

    Args:
    n (int): The parameter n.
    k (int): The parameter k.
    p (List[float]): The true probabilities.
    p_hat (List[float]): The estimated probabilities.

    Returns:
    float: The calculated value.
    """
    # Calculate (n + 1)^(2k)
    term1 = (n + 1) ** (2 * k)

    # Calculate KL(p_hat || p)
    kl = kl_divergence(p_hat, p)

    # Calculate exp(-n * KL(p_hat, p))
    term2 = math.exp(-n * kl)

    # Calculate the final value
    result = term1 * term2

    return result


if __name__ == "__main__":
    # Example usage:
    n_ = 10
    k_ = 3
    p_ = [0.2, 0.3, 0.5]
    p_hat_ = [0.25, 0.25, 0.5]

    bound = upper_bound(n_, k_, p_, p_hat_)
    print(f"The calculated value is: {bound}")
