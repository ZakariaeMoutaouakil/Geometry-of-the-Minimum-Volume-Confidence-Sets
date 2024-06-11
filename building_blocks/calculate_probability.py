import math
from time import time
from typing import List

from building_blocks.calculate_probability_counts import calculate_probability_counts


def calculate_probability(p: List[float], p_hat: List[float], n: int, factorials: List[int]) -> float:
    """
    Calculate the probability according to the multinomial formula.

    Args:
    p (List[float]): The vector p.
    p_hat (List[int]): The vector of p_hat.
    factorials (List[int]): A list of precomputed factorials from 0! to n!.

    Returns:
    float: The calculated probability.
    """
    # Turn p_hat into a vector of counts
    x = [int(prob * n) for prob in p_hat]

    # Calculate the probability
    probability = calculate_probability_counts(p, x, factorials)

    return probability


if __name__ == "__main__":
    # Example usage
    proba = [0.2, 0.3, 0.5]
    p_hat_ = [1 / 3, 1 / 3, 1 / 3]
    total = 3

    # Precompute factorials from 0! to n!
    factorial_list = [math.factorial(i) for i in range(total + 1)]

    start_time = time()  # Start time
    final_probability = calculate_probability(proba, p_hat_, total, factorial_list)
    end_time = time()  # End time

    print(f"The calculated probability is: {final_probability}")
    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
