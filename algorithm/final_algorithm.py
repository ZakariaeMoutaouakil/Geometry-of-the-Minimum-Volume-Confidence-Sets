from time import time
from typing import List

from algorithm.filter_simplex import filter_simplex
from algorithm.s_double_star import calculate_s_double_star
from utils.discrete_simplex import discrete_simplex
from utils.factorial import factorial_list
from utils.is_close_or_in_list import is_close_or_in_list


def final_algorithm(n: int, p_hat: List[float], delta: float, grid_size: int, margin: float = 0.) -> List[List[float]]:
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
    print("Discrete simplex:", simplex)
    filtered_simplex = filter_simplex(simplex, p_hat, n, delta)
    print("Filtered simplex:", filtered_simplex)
    factorials = factorial_list(n)
    confidence_region = []
    for p in filtered_simplex:
        print("p:", p)
        # Calculate the S** set
        s_double_star = calculate_s_double_star(p, filtered_simplex, n, factorials, delta)
        print("S** set:", s_double_star)
        if is_close_or_in_list(p_hat, s_double_star, margin):
            print(True)
            confidence_region.append(p)

    return confidence_region


if __name__ == "__main__":
    n_ = 100
    p_hat_ = [2 / n_, 3 / n_, 1. - (2 / n_) - (3 / n_)]
    delta_ = 0.01
    grid_size_ = 40
    margin_ = 0.1

    start_time = time()  # Start time
    region = final_algorithm(n_, p_hat_, delta_, grid_size_, margin_)
    end_time = time()  # End time

    print("Final confidence region:", region)
    for p_ in region:
        print(p_)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
    print("p_hat:", p_hat_)
