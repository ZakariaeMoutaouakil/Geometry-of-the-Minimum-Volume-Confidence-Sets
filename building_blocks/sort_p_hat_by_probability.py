from math import factorial
from time import time
from typing import Tuple

from building_blocks.calculate_probability import calculate_probability


def sort_p_hat_by_probability(p: Tuple[float, ...], x_list: Tuple[Tuple[int, ...], ...], factorials: Tuple[int, ...]) \
        -> Tuple[Tuple[Tuple[int, ...], float], ...]:
    """
    Sort the list of p_hat in descending order based on the calculated probability.

    Args:
    p (List[float]): The vector p.
    x_list (List[List[int]]): The vector of counts.
    factorials (List[int]): A list of precomputed factorials from 0! to n!.

    Returns:
    List[List[float]]: The list of p_hat sorted in descending order of probability.
    """

    # Calculate the probability for each p_hat and sort by it
    p_hat_probabilities = tuple((x, calculate_probability(p, x, factorials)) for x in x_list)
    sorted_p_hat_probabilities = sorted(p_hat_probabilities, key=lambda x: x[1], reverse=True)

    return tuple(sorted_p_hat_probabilities)


if __name__ == "__main__":
    # Example usage
    proba = (0.2, 0.3, 0.5)
    x_values = (
        (3, 2, 1),
        (1, 2, 3),
        (2, 1, 3)
    )
    n_ = sum(x_values[0])

    # Precompute factorials from 0! to n!
    factorial_list = tuple(factorial(i) for i in range(n_ + 1))

    start_time = time()  # Start time
    sorted_p_hat = sort_p_hat_by_probability(proba, x_values, factorial_list)
    end_time = time()  # End time

    for p_ in sorted_p_hat:
        print(p_)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
