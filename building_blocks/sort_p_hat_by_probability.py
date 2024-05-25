import math
from time import time
from typing import List, Tuple

from building_blocks.calculate_probability import calculate_probability


def sort_p_hat_by_probability(p: List[float], p_hat_list: List[List[float]], n: int, factorials: List[int]) \
        -> List[Tuple[List[float], float]]:
    """
    Sort the list of p_hat in descending order based on the calculated probability.

    Args:
    p (List[float]): The vector p.
    p_hat_list (List[List[float]]): A list of vectors p_hat.
    n (int): The common denominator.
    factorials (List[int]): A list of precomputed factorials from 0! to n!.

    Returns:
    List[List[float]]: The list of p_hat sorted in descending order of probability.
    """

    # Calculate the probability for each p_hat and sort by it
    p_hat_probabilities = [(p_hat, calculate_probability(p, p_hat, n, factorials)) for p_hat in p_hat_list]
    sorted_p_hat_probabilities = sorted(p_hat_probabilities, key=lambda x: x[1], reverse=True)

    return sorted_p_hat_probabilities


if __name__ == "__main__":
    # Example usage
    proba = [0.2, 0.3, 0.5]
    p_ = [
        [0.1, 0.2, 0.7],
        [0.3, 0.3, 0.4],
        [0.2, 0.3, 0.5]
    ]
    n_ = 10

    # Precompute factorials from 0! to n!
    factorial_list = [math.factorial(i) for i in range(n_ + 1)]

    start_time = time()  # Start time
    sorted_p_hat = sort_p_hat_by_probability(proba, p_, n_, factorial_list)
    end_time = time()  # End time

    for p_ in sorted_p_hat:
        print(p_)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
