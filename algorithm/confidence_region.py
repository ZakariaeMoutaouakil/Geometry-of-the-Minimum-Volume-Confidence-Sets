from time import time
from typing import Tuple, Dict

from tqdm import tqdm

from algorithm.filter_simplex import filter_simplex


def confidence_region(x: Tuple[int, ...],
                      all_s_double_stars: Dict[Tuple[float, ...], Tuple[Tuple[float, ...], ...]],
                      alpha: float) \
        -> Tuple[Tuple[float, ...], ...]:
    """
    Calculate the confidence region.

    Args:
    x (List[float]): The vector of counts.
    all_s_double_stars (Dict[List[float], List[List[float]]]): The dictionary of all s_double_stars.

    Returns:
    List[List[float]]: The confidence region.
    """
    # Calculate the probability for each s_double_star
    close_probabilities = filter_simplex(tuple(all_s_double_stars.keys()), x, alpha)
    final_confidence_region = tuple(
        p for p in tqdm(close_probabilities, desc="Calculating confidence region", unit="point")
        if x in all_s_double_stars[p]
    )

    return final_confidence_region


# Example usage
if __name__ == "__main__":
    # Example data
    example_x = (1, 2, 3)
    example_all_s_double_stars = {
        (0.2, 0.3, 0.5): ((1, 2, 3), (2, 2, 2)),
        (0.1, 0.4, 0.5): ((1, 2, 3),),
        (0.3, 0.3, 0.4): ((0, 1, 4), (1, 2, 4)),
    }
    example_alpha = 0.05

    # Calculate confidence region
    result = confidence_region(example_x, example_all_s_double_stars, example_alpha)

    start_time = time()  # Start time
    print("Confidence region:")
    for region in result:
        print(region)
    end_time = time()  # End time

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
