from math import factorial
from time import time
from typing import List


def calculate_probability_counts(p: List[float], x: List[int], factorials: List[int]) -> float:
    """
    Calculate the probability according to the multinomial formula.

    Args:
    p (List[float]): The vector p.
    x (List[int]): The vector of counts.
    factorials (List[int]): A list of precomputed factorials from 0! to n!.

    Returns:
    float: The calculated probability.
    """
    n = sum(x)

    # Compute the numerator n!
    numerator = factorials[n]

    # Compute the denominator (x1)! ... (xk)!
    denominator = 1
    for h in x:
        denominator *= factorials[h]

    # Compute the product p1^x1 * ... * pk^xk
    product = 1.
    for i in range(len(p)):
        product *= p[i] ** x[i]

    # Calculate the final probability
    probability = (numerator / denominator) * product

    return probability


if __name__ == "__main__":
    # Example usage
    proba = [0.2, 0.3, 0.5]
    counts = [1, 1, 1]
    total = sum(counts)

    # Precompute factorials from 0! to n!
    factorial_list = [factorial(i) for i in range(total + 1)]

    start_time = time()  # Start time
    final_probability = calculate_probability_counts(proba, counts, factorial_list)
    end_time = time()  # End time

    print(f"The calculated probability is: {final_probability}")
    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
