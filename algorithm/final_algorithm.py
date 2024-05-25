from typing import List

from algorithm.filter_simplex import filter_simplex
from algorithm.s_double_star import calculate_s_double_star
from utils.discrete_simplex import discrete_simplex
from utils.factorial import factorial_list
from utils.is_close_or_in_list import is_close_or_in_list


def final_algorithm(n: int, p_hat: List[float], delta: float, grid_size: int) -> List[List[float]]:
    """
    Calculate the final S** set.

    Args:
    n (int): The common denominator.
    p (List[float]): The vector p.
    p_hat (List[float]): The vector p_hat.
    delta (float): The threshold value.

    Returns:
    List[List[float]]: The final S** set.
    """
    k = len(p_hat)
    simplex = discrete_simplex(k, grid_size)
    filtered_simplex = filter_simplex(simplex, p_hat, n, delta)
    factorials = factorial_list(n)
    confidence_region = []
    for p in filtered_simplex:
        # Calculate the S** set
        s_double_star = calculate_s_double_star(p, filtered_simplex, n, factorials, delta)
        if is_close_or_in_list(p, s_double_star, delta):
            confidence_region.append(p)

    return confidence_region


if __name__ == "__main__":
    n = 10
    p_hat = [0.2, 0.3, 0.5]
    delta = 0.01
    grid_size = 10
    confidence_region = final_algorithm(n, p_hat, delta, grid_size)
    for p in confidence_region:
        print(p)
