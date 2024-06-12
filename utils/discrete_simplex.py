from itertools import combinations_with_replacement
from math import comb
from time import time
from typing import Tuple, Union

from tqdm import tqdm


def discrete_simplex(k: int, n: int, normalize: bool) \
        -> Union[Tuple[Tuple[float, ...], ...], Tuple[Tuple[int, ...], ...]]:
    """
    Generate the discrete simplex for k coordinates and common denominator n.

    Args:
    k (int): The number of coordinates.
    n (int): The common denominator.
    normalize (bool): Whether to normalize the point to make the sum equal to 1.

    Returns:
    Tuple[Union[Tuple[float, ...], Tuple[int, ...]], ...]: A tuple of tuples representing the discrete simplex points.
    """
    # Generate all combinations of k integers that sum to n
    combs = combinations_with_replacement(range(n + 1), k - 1)
    num_combinations = comb(n + k - 1, k - 1)

    simplex = []

    # Iterate over the combinations
    for combination in tqdm(combs, total=num_combinations, desc="Generating discrete simplex"):
        # Compute the differences between successive elements and append 0 at the start and n at the end
        point = [0] + list(combination) + [n]
        diffs = [point[i + 1] - point[i] for i in range(len(point) - 1)]

        if normalize:
            # Normalize the point to make the sum equal to 1
            normalized_point = tuple(x / n for x in diffs)
            simplex.append(normalized_point)
        else:
            simplex.append(tuple(diffs))

    return tuple(simplex)


if __name__ == "__main__":
    # Example usage:
    k_ = 3
    n_ = 4

    start_time = time()
    example_simplex = discrete_simplex(k_, n_, normalize=False)
    end_time = time()

    for p in example_simplex:
        print(p)

    print(f"Time taken: {end_time - start_time:.6f} seconds")
