from time import time
from typing import Tuple


def factorial_list(n: int) -> Tuple[int, ...]:
    """
    Computes the list of all factorials from 0! to n!.

    Parameters:
    n (int): The upper limit for factorial computation.

    Returns:
    Tuple[int, ...]: A tuple of factorials from 0! to n!.
    """
    factorials = [1] * (n + 1)  # Initialize factorials list with 1s
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i
    return tuple(factorials)  # Convert the list to a tuple before returning


# Example usage with time counting
if __name__ == "__main__":
    for limit in [1, 5, 10, 100]:
        start_time = time()  # Start time
        factorials_tuple = factorial_list(limit)
        end_time = time()  # End time

        elapsed_time = end_time - start_time  # Calculate elapsed time

        print(f"Factorials from 0! to {limit}! are: {factorials_tuple}")
        print(f"Time taken to compute: {elapsed_time:.6f} seconds")
