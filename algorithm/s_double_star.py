from math import factorial
from time import time
from typing import Tuple

from building_blocks.shortest_list_for_alpha import shortest_list_for_alpha
from building_blocks.sort_p_hat_by_probability import sort_p_hat_by_probability


def calculate_s_double_star(p: Tuple[float, ...],
                            observations: Tuple[Tuple[int, ...], ...],
                            factorials: Tuple[int, ...],
                            alpha: float) -> Tuple[Tuple[float, ...], ...]:
    """
    Calculate the S** set.

    Args:
    p (List[float]): The vector p.
    discrete_simplex (List[List[int]]): The discrete simplex.
    factorials (List[int]): A list of precomputed factorials from 0! to n!.
    alpha (float): The threshold value.

    Returns:
    List[List[float]]: The S** set.
    """
    # Sort the list of p_hat in descending order based on the calculated probability
    sorted_simplex = sort_p_hat_by_probability(p, observations, factorials)

    # Find the shortest list of consecutive elements such that the sum of their second coordinates is greater than 1
    # - delta
    s_double_star = shortest_list_for_alpha(sorted_simplex, alpha)

    return s_double_star


# Example usage
if __name__ == "__main__":
    p_ = (0.2, 0.3, 0.5)
    simplex = (
        (3, 2, 1),
        (1, 2, 3),
        (2, 1, 3)
    )
    n_ = sum(simplex[0])
    alpha_ = 0.9

    # Precompute factorials from 0! to n!
    factorial_list = tuple([factorial(i) for i in range(n_ + 1)])

    start_time = time()  # Start time
    result = calculate_s_double_star(p_, simplex, factorial_list, alpha_)
    end_time = time()  # End time

    print("S** set:", result)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
