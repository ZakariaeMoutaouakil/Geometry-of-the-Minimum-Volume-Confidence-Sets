from typing import Tuple

from tqdm import tqdm

from algorithm.upper_bound.is_pvalue_greater_than_delta import is_pvalue_greater_than_delta


def filter_simplex(p_list: Tuple[Tuple[float, ...], ...], x: Tuple[int, ...], alpha: float) \
        -> Tuple[Tuple[float, ...], ...]:
    """
    Filter the simplex based on the upper bound.

    Args:
    p_list (List[List[float]]): The list of probability vectors.
    x (List[float]): The vector of counts.
    alpha (float): The threshold value.

    Returns:
    List[List[float]]: The filtered simplex.
    """
    # Check if the simplex is empty
    filtered_simplex = tuple(
        p for p in tqdm(p_list, desc="Filtering simplex based on Sanov bound", unit="point")
        if is_pvalue_greater_than_delta(p, x, alpha)
    )
    return filtered_simplex


if __name__ == "__main__":
    # Example usage
    simp = (
        (0.1, 0.2, 0.7),
        (0.3, 0.3, 0.4),
        (0.2, 0.3, 0.5)
    )
    counts = (2, 3, 100)
    d = 0.05

    filtered_simp = filter_simplex(simp, counts, d)
    print("Filtered simplex:")
    for prob in filtered_simp:
        print(prob)
