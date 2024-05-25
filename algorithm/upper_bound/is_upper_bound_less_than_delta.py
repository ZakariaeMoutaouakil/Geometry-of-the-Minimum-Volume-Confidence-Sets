from typing import List

from algorithm.upper_bound.upper_bound import evaluate_upper_bound


def is_upper_bound_less_than_delta(n: int, p: List[float], p_hat: List[float], delta: float) -> bool:
    """
    Check if the result of compute_formula is greater than delta.

    Args:
    n (int): Sample size or total number of observations.
    p (List[float]): True probability distribution.
    p_hat (List[float]): Estimated probability distribution.
    delta (float): The threshold value.

    Returns:
    bool: True if the result of compute_formula is greater than delta, False otherwise.
    """
    result = evaluate_upper_bound(n, p, p_hat)
    return result < delta


if __name__ == "__main__":
    # Example usage
    n_ = 100
    p_ = [0.4, 0.6]
    p_hat_ = [0.5, 0.5]
    alpha = 0.0001

    is_greater = is_upper_bound_less_than_delta(n_, p_, p_hat_, alpha)
    print(f"Is the upper bound less than {alpha}? {is_greater}")
