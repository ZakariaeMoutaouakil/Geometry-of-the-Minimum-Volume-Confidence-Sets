from math import factorial
from time import time
from typing import List

from building_blocks.shortest_list_for_alpha import shortest_list_for_alpha
from building_blocks.sort_p_hat_by_probability import sort_p_hat_by_probability


def calculate_s_double_star(p: List[float],
                            discrete_simplex: List[List[float]],
                            n: int,
                            factorials: List[int],
                            delta: float) -> List[List[float]]:
    """
    Calculate the S** set.

    Args:
    p (List[float]): The vector p.
    discrete_simplex (List[List[float]]): A list of lists representing the discrete simplex points.
    n (int): The common denominator.
    factorials (List[int]): A list of precomputed factorials from 0! to n!.
    delta (float): The threshold value.

    Returns:
    List[List[float]]: The S** set.
    """
    # Sort the list of p_hat in descending order based on the calculated probability
    sorted_simplex = sort_p_hat_by_probability(p, discrete_simplex, n, factorials)

    # Find the shortest list of consecutive elements such that the sum of their second coordinates is greater than 1
    # - delta
    s_double_star = shortest_list_for_alpha(sorted_simplex, delta)

    return s_double_star


# Example usage
if __name__ == "__main__":
    p_ = [0.2, 0.3, 0.5]
    simplex = [
        [0.1, 0.2, 0.7],
        [0.3, 0.3, 0.4],
        [0.2, 0.3, 0.5]
    ]
    n_ = 10
    alpha = 0.1

    # Precompute factorials from 0! to n!
    factorial_list = [factorial(i) for i in range(n_ + 1)]

    start_time = time()  # Start time
    result = calculate_s_double_star(p_, simplex, n_, factorial_list, alpha)
    end_time = time()  # End time

    print("S** set:")
    for p_hat in result:
        print(p_hat)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
