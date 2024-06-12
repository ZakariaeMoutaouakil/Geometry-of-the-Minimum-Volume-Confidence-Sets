from typing import Tuple

from algorithm.upper_bound.upper_bound import evaluate_upper_bound


def is_pvalue_greater_than_delta(p: Tuple[float, ...], x: Tuple[int, ...], delta: float) -> bool:
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
    result = evaluate_upper_bound(p, x)
    return result > delta


if __name__ == "__main__":
    # Example usage
    p_ = (0.001, 0.999)
    x_ = (3, 2)
    alpha = 0.0001

    is_greater = is_pvalue_greater_than_delta(p_, x_, alpha)
    print(f"Is x likely given p? {'Yes' if is_greater else 'No'}")

    x_ = (1, 100)
    is_greater = is_pvalue_greater_than_delta(p_, x_, alpha)
    print(f"Is x likely given p? {'Yes' if is_greater else 'No'}")
