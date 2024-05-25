from typing import List

from algorithm.upper_bound.is_upper_bound_less_than_delta import is_upper_bound_less_than_delta


def filter_simplex(simplex: List[List[float]], p_hat: List[float], n: int, delta: float) -> List[List[float]]:
    """
    Filter the simplex based on the upper bound.

    Args:
    simplex (List[List[float]]): The list of points in the simplex.
    p_hat (List[float]): The estimated probability distribution.
    n (int): The total number of observations.
    delta (float): The threshold value.

    Returns:
    List[List[float]]: The filtered simplex.
    """
    # Check if the simplex is empty
    filtered_simplex = [p for p in simplex if not is_upper_bound_less_than_delta(n, p, p_hat, delta)]
    return filtered_simplex


if __name__ == "__main__":
    # Example usage
    simp = [
        [0.1, 0.2, 0.7],
        [0.3, 0.3, 0.4],
        [0.2, 0.3, 0.5]
    ]
    p_hat_ = [0.2, 0.3, 0.5]
    n_ = 10
    d = 1233333

    filtered_simp = filter_simplex(simp, p_hat_, n_, d)
    print("Filtered simplex:")
    for prob in filtered_simp:
        print(prob)
