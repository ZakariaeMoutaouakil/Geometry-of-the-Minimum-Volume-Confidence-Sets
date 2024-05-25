import time
from itertools import combinations_with_replacement
from typing import List


def discrete_simplex(k: int, n: int) -> List[List[float]]:
    """
    Generate the discrete simplex for k coordinates and common denominator n.

    Args:
    k (int): The number of coordinates.
    n (int): The common denominator.

    Returns:
    List[List[float]]: A list of lists representing the discrete simplex points.
    """
    # Generate all combinations of k integers that sum to n
    combs = combinations_with_replacement(range(n + 1), k - 1)

    simplex = []

    for comb in combs:
        # Compute the differences between successive elements and append 0 at the start and n at the end
        point = [0] + list(comb) + [n]
        diffs = [point[i + 1] - point[i] for i in range(len(point) - 1)]

        # Normalize the point to make the sum equal to 1
        normalized_point = [x / n for x in diffs]
        simplex.append(normalized_point)

    return simplex


if __name__ == "__main__":
    # Example usage:
    k_ = 3
    n_ = 3

    start_time = time.time()
    example_simplex = discrete_simplex(k_, n_)
    end_time = time.time()

    for p in example_simplex:
        print(p)

    print("Time taken:", end_time - start_time, "seconds")