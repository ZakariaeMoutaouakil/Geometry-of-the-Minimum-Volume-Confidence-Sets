from time import time
from typing import Tuple, Dict

from tqdm import tqdm

from algorithm.calculate_margin import find_min_vector_by_function, calculate_margin
from algorithm.filter_simplex import filter_simplex
from algorithm.robustness_radius import robustness_radius


def confidence_region(x: Tuple[int, ...],
                      all_s_double_stars: Dict[Tuple[float, ...], Tuple[Tuple[float, ...], ...]],
                      alpha: float,
                      sigma: float) \
        -> Dict[str, float | Tuple[float, ...] | Tuple[Tuple[float, ...], ...]]:
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

    # Calculate the confidence region
    final_confidence_region = tuple(
        p for p in tqdm(close_probabilities, desc="Calculating confidence region", unit="point")
        if x in all_s_double_stars[p]
    )

    # Find the smallest margin and radius
    margin_vector, smallest_margin = find_min_vector_by_function(final_confidence_region, calculate_margin)
    radius_vector, smallest_radius = find_min_vector_by_function(
        final_confidence_region, lambda p: robustness_radius(p, sigma=sigma)
    )

    return {
        "confidence_region": final_confidence_region,
        "margin_vector": margin_vector,
        "smallest_margin": smallest_margin,
        "radius_vector": radius_vector,
        "smallest_radius": smallest_radius
    }


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
    start_time = time()  # Start time
    result = confidence_region(
        example_x, example_all_s_double_stars, example_alpha, 0.1
    )
    end_time = time()  # End time

    for key, value in result.items():
        print(f"{key}: {value}")

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
