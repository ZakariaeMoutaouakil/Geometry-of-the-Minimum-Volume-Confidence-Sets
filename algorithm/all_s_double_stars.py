from math import factorial
from time import time
from typing import Dict, Tuple

from tqdm import tqdm

from algorithm.s_double_star import calculate_s_double_star


def calculate_all_s_double_stars(probabilities: Tuple[Tuple[float, ...], ...],
                                 observations: Tuple[Tuple[int, ...], ...],
                                 factorials: Tuple[int, ...],
                                 alpha: float) -> Dict[Tuple[float, ...], Tuple[Tuple[float, ...], ...]]:
    """
    Calculates all s_double_stars for a given list of probabilities.
    """
    return {
        p: calculate_s_double_star(p, observations, factorials, alpha)
        for p in tqdm(probabilities, desc="Calculating all S** sets", unit="point")
    }


if __name__ == "__main__":
    # Example input data
    p_values = (
        (0.1, 0.2, 0.7),
        (0.3, 0.4, 0.3),
        (0.25, 0.25, 0.5)
    )
    counts = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (0, 1, 1)
    )
    factorial_list = tuple(factorial(i) for i in range(6))
    risk = 0.05

    # Call the function
    start_time = time()  # Start time
    result = calculate_all_s_double_stars(p_values, counts, factorial_list, risk)
    end_time = time()  # End time

    # Print the result
    for key, value in result.items():
        print(f"Probability: {key} => S**(p): {value}")

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
